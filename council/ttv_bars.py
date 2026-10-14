#!/usr/bin/env python3
"""Write the lines Wendell marked "Keep as a BAR" in the board's Tap the Vein into the corpus, one BAR per file.

Wendell, 2026-10-14: "The goal for tap the vein is to also pull bars like we are doing from our podcasting episodes and
creating robust context web that our projects and tasks can pull frmo". The board's Morning tab seals a menu at
morning/menu in its store; lines he marked as BARs ride in that doc's `bars` field. The free write itself is never
saved (mm-raw), so every line here is his own words, marked by him, and is copied unedited.

The corpus is wendell-britt/game-masters-guide `corpus/bars/` (format in its corpus/BARS.md). Safe to run twice: a
line already in the corpus under the same file name is skipped.

Usage, after board/pull.py lists morning/menu under needs work:
  python3 council/ttv_bars.py <store>/morning/menu.json [--corpus ../game-masters-guide] [--write]
Then commit the new corpus files in the game-masters-guide checkout and open a pull request there.
"""
import argparse
import json
import re
import sys
from pathlib import Path


def slug(text, words=6):
    w = re.findall(r"[a-z0-9]+", text.lower().replace("’", "").replace("'", ""))
    return "-".join(w[:words]) or "line"


def title(text, words=7):
    t = " ".join(text.split()[:words])
    return t.rstrip(".,;:!?")


def bar_file(line, date, saved_at):
    return f"""---
title: "{title(line).replace('"', '')}"
kind: bar
speaker: Wendell
said: {date}
source: "Council Board, Tap the Vein, sealed {saved_at}"
slot: unplaced
maturity: captured
soil: holding_pen
face:
used_in: []
verification: "Typed by Wendell in the board's Tap the Vein free write and marked by him as a BAR; copied unedited from the sealed menu."
tags: [corpus, tap-the-vein]
---

> {line}

Marked as a BAR in the board's Tap the Vein on {date}. The rest of that free write never left his browser (mm-raw).
"""


def plan(doc, bars_dir):
    """(path, text) for each marked line the corpus does not hold yet."""
    date = doc.get("sessionDate") or (doc.get("savedAt") or "")[:10]
    out, taken, seen = [], set(), set()
    for line in doc.get("bars") or []:
        line = " ".join(str(line).split())
        if not line or line in seen:
            continue
        seen.add(line)
        base, n = f"{date}-{slug(line)}", 1
        name = f"{base}.md"
        while name in taken or ((bars_dir / name).exists() and line not in (bars_dir / name).read_text(encoding="utf-8")):
            n += 1
            name = f"{base}-{n}.md"
        taken.add(name)
        if not (bars_dir / name).exists():
            out.append((bars_dir / name, bar_file(line, date, doc.get("savedAt", ""))))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("menu", help="the store's morning/menu.json, saved with ArtifactData")
    ap.add_argument("--corpus", default="../game-masters-guide", help="game-masters-guide checkout")
    ap.add_argument("--write", action="store_true", help="write the files; without it, list them")
    a = ap.parse_args()
    doc = json.loads(Path(a.menu).read_text(encoding="utf-8"))
    bars_dir = Path(a.corpus) / "corpus" / "bars"
    if not bars_dir.is_dir():
        sys.exit(f"{bars_dir} not found; clone wendell-britt/game-masters-guide or pass --corpus")
    todo = plan(doc, bars_dir)
    if not todo:
        print("every marked line is in the corpus")
        return
    for path, text in todo:
        if a.write:
            path.write_text(text, encoding="utf-8")
        print(("wrote " if a.write else "would write ") + str(path))


if __name__ == "__main__":
    main()
