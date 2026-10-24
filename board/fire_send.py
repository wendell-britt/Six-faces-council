#!/usr/bin/env python3
"""After board-pull records saves on main, fire the Board Send routine so the steers fan out (ts-fanout).

board-pull (.github/workflows/board-pull.yml) records a save on main with no AI. That reaches the boat and
bars-engine /board/council, which read main on load, but not the coordinator: nobody routed a steer to the thread
that owns its strand, and nobody republished the artifact board, until he pressed Send. This fires the same routine
Send fires (trig_01L138vKTaN9MSJoFKRmaBNx) through its API trigger, with the rows that were recorded, so a save from any
surface (artifact board, bars-engine board, the tall ship, phone or desktop) starts one board read.

  python3 board/fire_send.py pull.log pull-council.log            # fires only if a log says "pushed to main"
  python3 board/fire_send.py pull.log --dry-run                   # print the text, send nothing

Env: SEND_ROUTINE_TOKEN (the routine's API token, a repo secret; missing = warn and exit 0),
SEND_ROUTINE_ID (default the Board Send routine). Fail-soft: a failed fire warns and exits 0, because the save is
already on main and the next Send or board read picks it up.
"""
import argparse
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROUTINE = "trig_01L138vKTaN9MSJoFKRmaBNx"
FIRE = "https://api.anthropic.com/v1/claude_code/routines/{}/fire"
ROW = re.compile(r"^(\d{4}-\d\d-\d\dT\S+)\s+(\S+)\s+(\S+)(?:\s+(.*))?$")


def recorded_rows(logs):
    """The rows pull.py recorded and pushed, as 'kind/id answer'. Empty when nothing reached main."""
    rows = []
    for text in logs:
        if "pushed to main" not in text:
            continue
        for line in text.splitlines():
            m = ROW.match(line.strip())
            if m:
                rows.append(f"{m.group(2)}/{m.group(3)}" + (f" {m.group(4).strip()}" if m.group(4) else ""))
    return rows


def fire_text(rows, now):
    return (f"Board Send at {now:%H:%M} UTC (board-pull, no button): {', '.join(rows)}. These saves are already on "
            "main; the board read routes each steer to the thread that owns its strand and republishes the board.")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("logs", nargs="+")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    logs = [Path(p).read_text(encoding="utf-8") for p in a.logs if Path(p).exists()]
    rows = recorded_rows(logs)
    if not rows:
        print("nothing recorded; no Send fired")
        return 0
    text = fire_text(rows, datetime.now(timezone.utc))
    token = os.environ.get("SEND_ROUTINE_TOKEN", "")
    if a.dry_run or not token:
        print(text)
        if not token and not a.dry_run:
            print("::warning::SEND_ROUTINE_TOKEN is not set; the board read waits for his Send")
        return 0
    req = urllib.request.Request(
        FIRE.format(os.environ.get("SEND_ROUTINE_ID") or ROUTINE), method="POST",
        data=json.dumps({"text": text}).encode(),
        headers={"Authorization": f"Bearer {token}", "anthropic-beta": "experimental-cc-routine-2026-04-01",
                 "anthropic-version": "2023-06-01", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            body = json.loads(r.read() or b"{}")
        print(f"fired Board Send for {len(rows)} rows: {body.get('claude_code_session_url', 'session started')}")
    except Exception as e:  # noqa: BLE001 - the saves are on main whatever happens here
        print(f"::warning::Board Send fire failed ({e}); the board read waits for his Send")
    return 0


if __name__ == "__main__":
    sys.exit(main())
