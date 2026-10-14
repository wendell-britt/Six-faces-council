#!/usr/bin/env python3
"""Write Wendell's lines from the board's Tap the Vein free write into the corpus, one BAR per file.

Wendell, 2026-10-14: "The goal for tap the vein is to also pull bars like we are doing from our podcasting episodes and
creating robust context web that our projects and tasks can pull frmo". On ttv-raw-bars (board, 2026-10-14) he chose
"read it once for BARs, then delete it": "For now read it and delete but this is the power of having a private server
like in bars engine". Sealing on the Morning tab saves the free write at morning/freewrite in the board's store. The
board read reads it, picks the lines worth keeping as he said them (the podcast move's rule: his exact words, he tags
nothing), and passes each with --line. The script refuses a line that is not in the free write word for word, so no
paraphrase reaches the corpus. Then the read deletes morning/freewrite from the store and its local copy.

The corpus is wendell-britt/game-masters-guide `corpus/bars/` (format in its corpus/BARS.md). Safe to run twice: a
line already in the corpus under the same file name is skipped.

Usage, after board/pull.py lists morning/freewrite under needs work:
  python3 council/ttv_bars.py <store>/morning/freewrite.json --line "<his words>" [--line ...] [--write]
Then commit the new corpus files in the game-masters-guide checkout and open a pull request there, and delete the
doc: ArtifactData action delete, collection morning, doc_id freewrite; then rm <store>/morning/freewrite.json.
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
verification: "Typed by Wendell in the board's Tap the Vein free write; checked word for word against the sealed free write before it was deleted."
tags: [corpus, tap-the-vein]
---

> {line}

From the board's Tap the Vein free write of {date}, read once for BARs and then deleted (ttv-raw-bars).
"""


def norm(text):
    return " ".join(str(text).split())


def not_in_write(doc, lines):
    """Lines that are not word for word in the free write (whitespace aside)."""
    write = norm(doc.get("text", ""))
    return [ln for ln in lines if norm(ln) not in write]


def plan(doc, bars_dir, lines=None):
    """(path, text) for each line the corpus does not hold yet."""
    date = doc.get("sessionDate") or (doc.get("savedAt") or "")[:10]
    out, taken, seen = [], set(), set()
    for line in (lines if lines is not None else doc.get("bars") or []):
        line = norm(line)
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
    ap.add_argument("freewrite", help="the store's morning/freewrite.json, saved with ArtifactData")
    ap.add_argument("--line", action="append", default=[], help="one of his lines, exactly as written; repeat")
    ap.add_argument("--corpus", default="../game-masters-guide", help="game-masters-guide checkout")
    ap.add_argument("--write", action="store_true", help="write the files; without it, list them")
    a = ap.parse_args()
    doc = json.loads(Path(a.freewrite).read_text(encoding="utf-8"))
    bad = not_in_write(doc, a.line)
    if bad:
        sys.exit("not in the free write word for word, so not his exact words:\n  " + "\n  ".join(bad))
    bars_dir = Path(a.corpus) / "corpus" / "bars"
    if not bars_dir.is_dir():
        sys.exit(f"{bars_dir} not found; clone wendell-britt/game-masters-guide or pass --corpus")
    todo = plan(doc, bars_dir, a.line)
    if not todo:
        print("every marked line is in the corpus")
        return
    for path, text in todo:
        if a.write:
            path.write_text(text, encoding="utf-8")
        print(("wrote " if a.write else "would write ") + str(path))


if __name__ == "__main__":
    main()
