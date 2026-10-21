#!/usr/bin/env python3
"""Write Your steps and Outreach documents to the Council Board's store on bars-engine, and check it against the
claude.ai artifact's store (board-home step 5, 2026-10-21).

Until the artifact retires (board-home step 6) both boards are live, so a session that publishes steps, a list, a
contact or a show writes the same documents to both: ArtifactData as before, and this script.

  python3 board/store_write.py push <docs.json> [--dry]   # docs.json: [{collection, docId, mode?, data}, ...]
  python3 board/store_write.py diff <dir> [--push-missing]

push sends the documents to POST /api/board/session-writes. mode defaults to update, which merges top-level fields onto
the document bars-engine holds, so a rewritten step keeps the tick and note he saved on /board/council; set replaces.
A write that changes nothing is skipped there, so a rerun adds nothing. Only lists, steps, contacts and shows are
accepted: his answers are his to save.

diff reads an ArtifactData export folder (<dir>/<collection>/<id>.json, as board/read.py takes) and compares each
document's hash with bars-engine's (GET /api/board/session-writes answers hashes, never contents). It prints what only
the artifact has, what only bars-engine has, and what differs, and exits 1 on any drift. --push-missing sends what
only the artifact has; a document on both sides that differs is listed for a session to judge, never overwritten,
since he can tick a step on either board.

Auth: the egress proxy injects COUNCIL_MENU_TOKEN for bars-engine.vercel.app in a session; elsewhere set it in the env.
BARS_ENGINE_URL overrides https://bars-engine.vercel.app. Never commit a docs file or an export: contacts hold his
outreach notes and both repos are public.
"""
import argparse
import hashlib
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

COLLECTIONS = ("lists", "steps", "contacts", "shows")
BASE = os.environ.get("BARS_ENGINE_URL", "https://bars-engine.vercel.app").rstrip("/")
BATCH = 50


def call(method, path, body=None):
    headers = {"Content-Type": "application/json", "User-Agent": "six-faces-council store-write"}
    token = os.environ.get("COUNCIL_MENU_TOKEN", "").strip()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(BASE + path, method=method, headers=headers,
                                 data=json.dumps(body).encode() if body is not None else None)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        hint = " (COUNCIL_MENU_TOKEN is not accepted; see council/callsheets/board-plumbing.md)" if e.code == 401 else ""
        sys.exit(f"{method} {path} answered {e.code}{hint}: {e.read().decode()[:300]}")
    except urllib.error.URLError as e:
        sys.exit(f"{method} {path} failed: {e.reason}")


def canonical(v):
    """The same form bars-engine hashes (src/lib/board/session-write.ts canonical)."""
    return json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def doc_hash(v):
    return hashlib.sha256(canonical(v).encode()).hexdigest()[:16]


def push(docs, dry):
    total = {"written": [], "same": 0, "refused": []}
    for i in range(0, len(docs), BATCH):
        r = call("POST", "/api/board/session-writes", {"docs": docs[i:i + BATCH], "dry": dry})
        total["written"] += r["written"]
        total["same"] += r["same"]
        total["refused"] += r["refused"]
    print(f'{"would write" if dry else "wrote"} {len(total["written"])}, unchanged {total["same"]}, '
          f'refused {len(total["refused"])}')
    for k in total["written"]:
        print("  +", k)
    for k in total["refused"]:
        print("  refused", k)
    return 1 if total["refused"] else 0


def load_docs(path):
    out = []
    for d in json.loads(Path(path).read_text(encoding="utf-8")):
        doc = {"collection": d["collection"], "docId": d.get("docId") or d["doc_id"], "data": d["data"]}
        if d.get("mode"):
            doc["mode"] = d["mode"]
        out.append(doc)
    return out


def load_export(folder):
    out = {}
    for c in COLLECTIONS:
        d = Path(folder) / c
        out[c] = {f.stem: json.loads(f.read_text(encoding="utf-8")) for f in sorted(d.glob("*.json"))} if d.is_dir() else None
    return out


def diff(folder, push_missing):
    art = load_export(folder)
    there = call("GET", "/api/board/session-writes")["hashes"]
    missing, drift = [], 0
    for c in COLLECTIONS:
        if art[c] is None:
            print(f"{c}: not in the export, skipped")
            continue
        theirs = there.get(c, {})
        only_art = sorted(set(art[c]) - set(theirs))
        only_be = sorted(set(theirs) - set(art[c]))
        differ = sorted(i for i in set(art[c]) & set(theirs) if doc_hash(art[c][i]) != theirs[i])
        drift += len(only_art) + len(only_be) + len(differ)
        print(f"{c}: artifact {len(art[c])}, bars-engine {len(theirs)}; only artifact {len(only_art)}, "
              f"only bars-engine {len(only_be)}, differ {len(differ)}")
        for label, ids in (("only artifact", only_art), ("only bars-engine", only_be), ("differ", differ)):
            for i in ids:
                print(f"  {label}: {c}/{i}")
        missing += [{"collection": c, "docId": i, "mode": "set", "data": art[c][i]} for i in only_art]
    if push_missing and missing:
        push(missing, dry=False)
    return 1 if drift else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("push")
    p.add_argument("docs")
    p.add_argument("--dry", action="store_true")
    d = sub.add_parser("diff")
    d.add_argument("dir")
    d.add_argument("--push-missing", action="store_true")
    a = ap.parse_args()
    sys.exit(push(load_docs(a.docs), a.dry) if a.cmd == "push" else diff(a.dir, a.push_missing))


if __name__ == "__main__":
    main()
