#!/usr/bin/env python3
"""Fetch the board's store from bars-engine into the folder layout board/pull.py reads, and acknowledge what main
now records. No AI and no claude.ai: one bearer token and HTTPS.

From 2026-10-16 the board saves to Postgres through bars-engine (POST /api/board/saves, behind his own sign-in), not
to the claude.ai artifact store, so a save no longer waits on a Claude routine or any vendor's token quota
(docs/failure-modes.md, docs/incidents.md 2026-10-15). The scheduled Action (.github/workflows/board-pull.yml) runs:

  python3 board/fetch_store.py fetch <dir>                  # GET /api/board/pull: every document + unrecorded ids
  python3 board/pull.py <dir> --push --no-room              # unchanged: records what main lacks
  python3 board/fetch_store.py ack <dir> --record <ledger>  # POST /api/board/pull: mark those saves recorded

Any person or agent with the token can run the same three lines. Env: BOARD_PULL_TOKEN (required),
BARS_ENGINE_URL (default https://bars-engine.vercel.app), BOARD (default nonprofit).
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

STORE_DIRS = ("positions", "questions", "terms", "causes", "steer", "steps", "blockers", "picks", "morning", "ttv")
BASE = os.environ.get("BARS_ENGINE_URL", "https://bars-engine.vercel.app").rstrip("/")


def call(method, path, body=None):
    token = os.environ.get("BOARD_PULL_TOKEN", "").strip()
    if not token:
        sys.exit("BOARD_PULL_TOKEN is not set")
    req = urllib.request.Request(BASE + path, method=method, data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json",
                                          "User-Agent": "six-faces-council board-pull"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        sys.exit(f"{method} {path} answered {e.code}: {e.read().decode()[:300]}")
    except urllib.error.URLError as e:
        sys.exit(f"{method} {path} failed: {e.reason}")


def safe_name(doc_id):
    if "/" in doc_id or "\\" in doc_id or doc_id in (".", "..") or not doc_id:
        raise ValueError(f"refusing document id {doc_id!r}")
    return doc_id + ".json"


def write_store(payload, store):
    """payload: {"docs": {collection: {docId: data}}, "unrecorded": [...]} as /api/board/pull returns it."""
    store = Path(store)
    for kind in STORE_DIRS:
        (store / kind).mkdir(parents=True, exist_ok=True)
    n = 0
    for kind, docs in (payload.get("docs") or {}).items():
        if kind not in STORE_DIRS:
            continue
        for doc_id, data in docs.items():
            (store / kind / safe_name(doc_id)).write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n",
                                                          encoding="utf-8")
            n += 1
    (store / "_unrecorded.json").write_text(json.dumps(payload.get("unrecorded") or [], indent=1) + "\n")
    return n


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("fetch"); f.add_argument("store")
    a = sub.add_parser("ack"); a.add_argument("store"); a.add_argument("--record", required=True)
    a.add_argument("--except", dest="skip", action="append", default=[], help="collection/docId to leave unrecorded")
    args = ap.parse_args()
    board = os.environ.get("BOARD", "nonprofit")
    if args.cmd == "fetch":
        payload = call("GET", f"/api/board/pull?board={board}")
        n = write_store(payload, args.store)
        print(f"fetched {n} documents; {len(payload.get('unrecorded') or [])} saves not yet recorded on main")
        return
    pending = json.loads((Path(args.store) / "_unrecorded.json").read_text())
    ids = [s["id"] for s in pending if f"{s['collection']}/{s['docId']}" not in args.skip]
    # Sent even when empty: bars-engine logs every pull, so the board can show when main last caught up.
    r = call("POST", "/api/board/pull", {"board": board, "ids": ids, "record": args.record})
    print(f"acknowledged {r.get('recorded', 0)} saves as {args.record}")


if __name__ == "__main__":
    main()
