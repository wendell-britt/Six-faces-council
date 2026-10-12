#!/usr/bin/env python3
"""The daily compost pass: every open step on Wendell's board, one block each, for keep, drop or take over.

Wendell, 2026-10-12: "ok can we do a daily pass through the open items for me and see if they are still needed for
our various goals? This is an important composting step and a big opportunitty for the game masters. As context
increased and changes we should be able to take things from my board and act on them if it's the more deft and
aligned path". How the pass runs is in docs/compost-pass.md.

    python3 council/compost.py <store dir>          # the folder an ArtifactData list of steps and lists saved into
    python3 council/compost.py <store dir> --at 2026-10-13

It reads the saved store and prints; it writes nothing. Open rows on the Open tab are counted at the end, so the pass
knows whether the board has anything open besides steps.
"""

import argparse
import datetime as dt
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIELDS = ("where", "href", "enter", "check", "note", "noteAt")


def load(folder):
    out = {}
    for f in sorted(folder.glob("*.json")) if folder.is_dir() else []:
        doc = json.loads(f.read_text())
        out[f.stem] = doc.get("data", doc)
    return out


def days_late(due, today):
    try:
        return (today - dt.date.fromisoformat(due[:10])).days
    except (TypeError, ValueError):
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("store", type=Path)
    ap.add_argument("--at", default=dt.date.today().isoformat())
    a = ap.parse_args()
    today = dt.date.fromisoformat(a.at)
    lists, steps = load(a.store / "lists"), load(a.store / "steps")
    if not steps:
        raise SystemExit(f"no steps in {a.store}/steps: list the steps and lists collections first")
    total = 0
    for lid, l in sorted(lists.items()):
        mine = sorted(((k, s) for k, s in steps.items() if s.get("list") == lid), key=lambda kv: kv[1].get("n", 0))
        live = [(k, s) for k, s in mine if not s.get("done") and not s.get("retired")]
        if not live:
            continue
        print(f"\n## {lid} [{l.get('repo', '')}] {l.get('title', '')}")
        print(f"   why: {l.get('why', '')}")
        print(f"   from: {l.get('source', '')}")
        for k, s in live:
            total += 1
            late = days_late(s.get("due"), today)
            due = f"due {s.get('due')}" + (f", {late} days late" if late and late > 0 else "")
            tags = ", ".join(t for t in (s.get("device"), "optional" if s.get("optional") else "", due) if t)
            print(f"  - {k} (step {s.get('n')}; {tags}): {s.get('do')}")
            for f in FIELDS:
                if s.get(f):
                    print(f"      {f}: {s[f]}")
    orphans = [k for k, s in steps.items() if s.get("list") not in lists and not s.get("done") and not s.get("retired")]
    if orphans:
        print(f"\nOpen steps whose list is missing: {', '.join(sorted(orphans))}")
    data = json.loads((ROOT / "board" / "board_data.json").read_text())
    res = data.get("resolved", {})
    open_rows = sum(1 for kind in ("questions", "positions", "terms", "causes") for x in data.get(kind, [])
                    if x["id"] not in res.get(kind, {}) and not os.path.exists(a.store / kind / f"{x['id']}.json"))
    print(f"\n{total} open steps. Open tab rows with no save yet: {open_rows}"
          + ("" if (a.store / "questions").is_dir() else " (questions not listed, so this counts every unresolved row)"))


if __name__ == "__main__":
    main()
