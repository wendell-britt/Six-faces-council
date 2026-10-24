#!/usr/bin/env python3
"""List the steers recorded on main since this machine last looked, for a coding session's start (ts-fanout).

A steer is a saved board answer that carries his words (from the artifact board, bars-engine /board/council or the
tall ship, which all post the same save, ts-steer-is-save) or a general steer. board/pull.py records each one on main
in board/board_data.json: `resolved.<kind>.<id>.steer` and `steers_recorded`. council/hooks/council-sync.sh runs this
at every session start, in every repo that carries the council, cloud or desktop, so a steer given on the phone is in
front of the next coding session wherever it opens (Wendell, 2026-10-24: "When one does a steer action it should
update the repo and send a hook to update all the surfaces that can access the game including different coding
environments").

  python3 council/tools/steers.py --data <board_data.json>            # since the last look on this machine
  python3 council/tools/steers.py --data <file> --since 2026-10-20     # since a date, without moving the mark

The mark is a file outside the repo (~/.claude/council-steers-seen, or $COUNCIL_STEERS_SEEN), so a desktop clone
remembers its last look. A cloud container starts empty each time, so it shows the last three days. Fail-soft: any
error prints nothing and exits 0, because a session start must never break.
"""
import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

LOOKBACK_DAYS = 3
SHOW = 8


def mark_path():
    return Path(os.environ.get("COUNCIL_STEERS_SEEN") or Path.home() / ".claude" / "council-steers-seen")


def steers(data):
    """Every recorded steer as (saved_at, where, label, text), oldest first."""
    out = []
    for kind, rows in (data.get("resolved") or {}).items():
        for rid, e in (rows or {}).items():
            if isinstance(e, dict) and (e.get("steer") or "").strip():
                at = e.get("saved_at") or e.get("recorded") or ""
                out.append((at, f"{kind}/{rid}", e.get("label") or "", e["steer"].strip()))
    for g in data.get("steers_recorded") or []:
        if (g.get("text") or "").strip():
            out.append((g.get("savedAt") or "", "steer/general", "", g["text"].strip()))
    return sorted(out)


def since_default(now):
    try:
        return mark_path().read_text(encoding="utf-8").strip()
    except OSError:
        return (now - timedelta(days=LOOKBACK_DAYS)).strftime("%Y-%m-%dT%H:%M:%S")


def report(items, since):
    new = [s for s in items if s[0] > since]
    if not new:
        return ""
    lines = [f"Council steers since {since[:16].replace('T', ' ')}: {len(new)} (board/board_data.json on main)."]
    for at, where, label, text in new[-SHOW:]:
        short = text if len(text) <= 160 else text[:157] + "..."
        lines.append(f"- {at[:16].replace('T', ' ')} {where}" + (f" ({label})" if label else "") + f': "{short}"')
    if len(new) > SHOW:
        lines.append(f"- and {len(new) - SHOW} older; python3 council/tools/steers.py --since {since[:10]} lists all.")
    lines.append("A steer that touches this session's work is a ruling: act on it, and record it on the board.")
    return "\n".join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--since")
    a = ap.parse_args(argv)
    now = datetime.now(timezone.utc)
    try:
        items = steers(json.loads(Path(a.data).read_text(encoding="utf-8")))
        text = report(items, a.since or since_default(now))
        if text:
            print(text)
        if not a.since:
            p = mark_path()
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(now.strftime("%Y-%m-%dT%H:%M:%S") + "\n", encoding="utf-8")
    except Exception:  # noqa: BLE001 - a session start never breaks
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
