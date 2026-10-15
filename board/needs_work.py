#!/usr/bin/env python3
"""The needs-work list: what Wendell's recorded answers still ask someone to do, for any agent or person.

board/pull.py writes each pull's needs_work into its ledger record (council/ledger/*-pull-*.json). This prints the
items from pulls on or after the cutoff that council/needs-work-done.json does not mark done. An item is finished
by the change it asks for plus one entry in that file, in the same pull request (AGENTS.md, "Working the needs-work
list"). No vendor's tools are needed to read or close it.

  python3 board/needs_work.py            # open items, oldest first, one per line: <key>  <what to do>
  python3 board/needs_work.py --json     # the same as JSON, for a script
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "council" / "ledger"
DONE = ROOT / "council" / "needs-work-done.json"


def items():
    done = json.loads(DONE.read_text()) if DONE.exists() else {"since": "", "done": {}}
    out = []
    for f in sorted(LEDGER.glob("*-pull-*.json")):
        rec = json.loads(f.read_text(encoding="utf-8"))
        if rec.get("kind") != "board-pull" or rec.get("newest_save", "") < done.get("since", ""):
            continue
        for line in rec.get("needs_work") or []:
            row, _, what = line.partition(": ")
            key = f"{f.stem}#{row}"
            if key not in done["done"]:
                out.append({"key": key, "row": row, "what": what, "ledger": f"council/ledger/{f.name}"})
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    open_items = items()
    if a.json:
        print(json.dumps(open_items, ensure_ascii=False, indent=1))
        return
    for i in open_items:
        print(f"{i['key']}  {i['what']}")
    print(f"{len(open_items)} open")


if __name__ == "__main__":
    main()
