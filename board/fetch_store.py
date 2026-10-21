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

Every save is accounted for before it is acknowledged (Wendell, 2026-10-15, after run 2 acknowledged three saves and
recorded one: "We need to account for these in future"). `ack` gives each pending save one status, prints the table,
writes it to <dir>/_accounting.json and sends each status as its own acknowledgement, so bars-engine's board_saves.record
says why for every row:

  recorded          main holds this save (pull.py, or morning.py for a menu)
  superseded        a newer save of the same document came in; only the newest is fetched and judged
  nothing-to-record the newest save holds nothing pull.py records (an emptied answer, a removed pick, a sealed ttv)
  held              left unacknowledged on purpose: --except, or work pull.py hands to a session (a freewrite, a
                    Tap the Vein to fetch), so the staleness check goes red if nobody does it
  unaccounted       none of the above: left unacknowledged, and ack exits 1 so the run goes red
"""
import argparse
import importlib.util
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


ACKED = ("recorded", "superseded", "nothing-to-record")
RECORD_KINDS = ("positions", "questions", "terms", "causes")


def _pull():
    spec = importlib.util.spec_from_file_location("pull", Path(__file__).resolve().parent / "pull.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _doc(store, collection, doc_id):
    f = Path(store) / collection / safe_name(doc_id)
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else None


def _judge(collection, doc_id, doc, data, store, pull, flagged):
    """(status, why) for the newest save of one document, judged against main as it stands after the pull."""
    key = f"{collection}/{doc_id}"
    if doc is None:
        return "unaccounted", "the fetched store has no copy of this document"
    if key in flagged:
        return ("held", flagged[key]) if flagged[key].startswith("for a session") else ("unaccounted", flagged[key])
    if collection in RECORD_KINDS:
        ans = "deferred" if doc.get("deferred") else pull.answer(collection, doc)
        if not (ans or (doc.get("steer") or "").strip()):
            return "nothing-to-record", "holds no decision and no steer"
        entry = data.get("resolved", {}).get(collection, {}).get(doc_id)
        if pull.recorded(entry, doc, ans):
            return "recorded", f"resolved.{collection}.{doc_id} on main"
    elif collection == "steer" and doc_id == "general":
        if not (doc.get("text") or "").strip():
            return "nothing-to-record", "empty steer"
        if doc.get("savedAt", "") <= data.get("steer_recorded_through", ""):
            return "recorded", f"steer_recorded_through {data.get('steer_recorded_through')}"
    elif collection == "picks":
        if doc_id in {p["id"] for p in data.get("picks", [])}:
            return "recorded", "in picks on main"
        if doc.get("removed"):
            return "nothing-to-record", "pick removed"
    elif collection == "steps":
        if not (doc.get("doneAt") or doc.get("noteAt") or doc.get("moved") or doc.get("fileNotes")):
            return "nothing-to-record", "no tick, note or move on this step"
        return "recorded", f"every change is at or before steps_recorded_through {data.get('steps_recorded_through')}"
    elif collection == "blockers":
        have = pull.BLOCKERS / safe_name(doc_id)
        if have.exists() and json.loads(have.read_text(encoding="utf-8")).get("savedAt", "") >= doc.get("savedAt", ""):
            return "recorded", f"council/blockers/{doc_id}.json on main"
    elif collection == "morning" and doc_id == "menu":
        if doc.get("savedAt", "") <= (data.get("morning") or {}).get("gathered_at", ""):
            return "recorded", f"morning gathered at {(data.get('morning') or {}).get('gathered_at')}"
    elif collection == "ttv":
        if doc.get("status") != "bars-engine" or doc_id <= ((data.get("morning") or {}).get("sealed") or ""):
            return "nothing-to-record", "no Tap the Vein left to fetch for this date"
    return "unaccounted", "pull.py neither recorded it nor passed over it"


def account(pending, store, data, pull, skip=()):
    """One row per pending save: its id, document, receivedAt, status and why. Pure: reads the store and main's data."""
    store = Path(store)
    flagged = {}  # what pull.py would still record, or still hands to a session, with main as it stands now
    new, general, steps = pull.find_new(data, store)
    for n in new:
        flagged[f"{n['kind']}/{n['id']}"] = "pull.py would still record it: main lacks this save"
    if general:
        flagged["steer/general"] = "pull.py would still record it: newer than steer_recorded_through"
    for e in steps:
        flagged[f"steps/{e['id']}"] = f"pull.py would still record a step {e['what']} at {e['at']}"
    for b in pull.find_blockers(store):
        flagged[f"blockers/{b['id']}"] = "pull.py would still record this blocker run"
    if pull.pasted_menu(data, store):
        flagged["morning/menu"] = "for a session: a pasted menu newer than the last gather (council/morning.py --menu)"
    if (store / "morning" / "freewrite.json").exists():
        flagged["morning/freewrite"] = "for a session: read once for BARs (council/ttv_bars.py), then delete"
    for f in sorted((store / "ttv").glob("*.json")) if (store / "ttv").is_dir() else []:
        doc = json.loads(f.read_text(encoding="utf-8"))
        sealed = (data.get("morning") or {}).get("sealed") or ""
        if doc.get("status") == "bars-engine" and sealed != f.stem and f.stem > sealed:
            flagged[f"ttv/{f.stem}"] = f"for a session: fetch the Tap the Vein menu (council/morning.py --fetch {f.stem})"
    newest = {}
    for s in pending:
        k = (s["collection"], s["docId"])
        if k not in newest or (s["receivedAt"], s["id"]) > (newest[k]["receivedAt"], newest[k]["id"]):
            newest[k] = s
    rows = []
    for s in pending:
        c, d = s["collection"], s["docId"]
        if f"{c}/{d}" in skip:
            status, why = "held", "--except: left for a later run"
        elif newest[(c, d)] is not s:
            status, why = "superseded", f"newer save {newest[(c, d)]['id']} of the same document"
        else:
            status, why = _judge(c, d, _doc(store, c, d) if c in STORE_DIRS else None, data, store, pull, flagged)
        rows.append({"id": s["id"], "collection": c, "docId": d, "receivedAt": s["receivedAt"], "status": status,
                     "why": why})
    return rows


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
    store = Path(args.store)
    pending = json.loads((store / "_unrecorded.json").read_text())
    pull = _pull()
    rows = account(pending, store, json.loads(pull.DATA.read_text(encoding="utf-8")), pull, args.skip)
    (store / "_accounting.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for r in rows:
        print(f"{r['receivedAt']}  {r['status']:<17} {r['collection']}/{r['docId']}  {r['why']}")
    counts = {}
    for r in rows:
        counts.setdefault(r["status"], []).append(r["id"])
    acked = 0
    for status in ACKED:
        if counts.get(status):
            acked += call("POST", "/api/board/pull", {"board": board, "ids": counts[status],
                                                       "record": f"{args.record} {status}"}).get("recorded", 0)
    if not acked:  # sent even when empty: bars-engine logs every pull, so the board shows when main last caught up
        call("POST", "/api/board/pull", {"board": board, "ids": [], "record": args.record})
    print(f"acknowledged {acked} of {len(rows)} saves as {args.record}: "
          + (", ".join(f"{len(v)} {k}" for k, v in counts.items()) or "none pending"))
    if counts.get("unaccounted"):
        sys.exit(f"{len(counts['unaccounted'])} saves are unaccounted for and stay unacknowledged; see the table above")


if __name__ == "__main__":
    main()
