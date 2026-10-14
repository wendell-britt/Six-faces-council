#!/usr/bin/env python3
"""Turn the board's Tap the Vein free write into BAR pitches, and the pitches Wendell accepts into corpus BARs.

Wendell, 2026-10-14: "The goal for tap the vein is to also pull bars like we are doing from our podcasting episodes and
creating robust context web that our projects and tasks can pull frmo". On ttv-raw-bars he chose "read it once for
BARs, then delete it": "For now read it and delete but this is the power of having a private server like in bars
engine". Then, the same day: "I think the tap the being should be read and summarized before bars are chosen. It a bit
too raw for me to know what should be a bar [...] This is something where I'd want to use AI to summarize and make
pitches for where things should go."

So it runs in two board reads:
1. Sealing on the Morning tab saves the free write at morning/freewrite in the board's store. The next board read
   reads it, writes a short summary, and pitches the lines worth keeping as BARs, each with the slot from
   game-masters-guide corpus/products.yaml it would go to. Each pitch is one board question built by `pitch`, which
   refuses a line that is not in the free write word for word, so no paraphrase is pitched. The read adds the rows
   with board/sync_board.py, then deletes morning/freewrite from the store and its local copy.
2. He answers each pitch on the board. After board/pull.py records the answers, `accepted` writes one corpus BAR per
   pitch he kept, into game-masters-guide corpus/bars/. Safe to run twice.

Usage:
  python3 council/ttv_bars.py pitch <store>/morning/freewrite.json --pitches pitches.json --summary "<summary>" > rows.json
      pitches.json: [{"line": "<his exact words>", "slot": "<slot id>", "why": "<one line>"}, ...]
  python3 council/ttv_bars.py accepted [--corpus ../game-masters-guide] [--write]
Then commit the new corpus files in the game-masters-guide checkout and open a pull request there.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "board" / "board_data.json"
PASS = "tap the vein on the board"


def norm(text):
    return " ".join(str(text).split())


def slug(text, words=6):
    w = re.findall(r"[a-z0-9]+", text.lower().replace("’", "").replace("'", ""))
    return "-".join(w[:words]) or "line"


def title(text, words=7):
    return " ".join(text.split()[:words]).rstrip(".,;:!?")


def not_in_write(doc, lines):
    """Lines that are not word for word in the free write (whitespace aside)."""
    write = norm(doc.get("text", ""))
    return [ln for ln in lines if norm(ln) not in write]


def pitch_rows(doc, pitches, summary):
    """One board question per pitch: keep it in the pitched slot, keep it unplaced, or not a BAR."""
    date = doc.get("sessionDate") or (doc.get("savedAt") or "")[:10]
    rows = []
    for i, p in enumerate(pitches, 1):
        line, slot = norm(p["line"]), p.get("slot") or "unplaced"
        rows.append({
            "id": f"ttv-{date}-{i}", "faces": ["sage", "shaman"], "pass": PASS,
            "q": f"Keep this line from your {date} free write as a BAR? “{line}”",
            "why_you": f"Summary of the free write: {summary} Why this line: {p.get('why', '')}".strip(),
            "not_before": "The free write was sealed on the board today; it has been read once and deleted (ttv-raw-bars).",
            "options": [
                {"v": "keep", "label": f"A. Keep it, in {slot} (recommended)", "c": "It becomes a BAR in that slot of the corpus."},
                {"v": "unplaced", "label": "B. Keep it, unplaced", "c": "It becomes a BAR in the holding pen until a slot fits. Name a slot in your steer to place it."},
                {"v": "no", "label": "C. Not a BAR", "c": "Nothing is kept. The line is gone with the free write."}],
            "why": "Pitched by the board read from the sealed free write (council/ttv_bars.py pitch).",
            "bar_line": line, "slot": slot, "said": date,
        })
    return rows


def bar_file(line, date, slot, source):
    return f"""---
title: "{title(line).replace('"', '')}"
kind: bar
speaker: Wendell
said: {date}
source: "{source}"
slot: {slot}
maturity: {'captured' if slot == 'unplaced' else 'context_named'}
soil: {'holding_pen' if slot == 'unplaced' else 'campaign'}
face:
used_in: []
verification: "Typed by Wendell in the board's Tap the Vein free write; checked word for word against it before it was deleted, then kept by him on the board."
tags: [corpus, tap-the-vein]
---

> {line}

From the board's Tap the Vein free write of {date}, pitched by the board read and kept by Wendell (ttv-raw-bars).
"""


def accepted(data):
    """(line, date, slot, source) for each pitch he kept."""
    res = data.get("resolved", {}).get("questions", {})
    out = []
    for q in data.get("questions", []):
        r = res.get(q["id"])
        if not q.get("bar_line") or not r or r.get("decision") not in ("keep", "unplaced"):
            continue
        slot = q.get("slot", "unplaced") if r["decision"] == "keep" else "unplaced"
        out.append((q["bar_line"], q["said"], slot, f"Council Board, {q['id']}, {r.get('record', '')}"))
    return out


def plan(kept, bars_dir):
    """(path, text) for each kept line the corpus does not hold yet."""
    out, taken = [], set()
    for line, date, slot, source in kept:
        base, n = f"{date}-{slug(line)}", 1
        name = f"{base}.md"
        while name in taken or ((bars_dir / name).exists() and line not in (bars_dir / name).read_text(encoding="utf-8")):
            n += 1
            name = f"{base}-{n}.md"
        taken.add(name)
        if not (bars_dir / name).exists():
            out.append((bars_dir / name, bar_file(line, date, slot, source)))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("pitch", help="board rows for the pitched lines, printed as sync_board.py --rows JSON")
    p.add_argument("freewrite", help="the store's morning/freewrite.json, saved with ArtifactData")
    p.add_argument("--pitches", required=True, help='JSON list of {"line", "slot", "why"}')
    p.add_argument("--summary", required=True, help="two or three sentences on what the free write holds")
    k = sub.add_parser("accepted", help="write a corpus BAR for each pitch he kept")
    k.add_argument("--corpus", default="../game-masters-guide", help="game-masters-guide checkout")
    k.add_argument("--write", action="store_true", help="write the files; without it, list them")
    a = ap.parse_args()
    if a.cmd == "pitch":
        doc = json.loads(Path(a.freewrite).read_text(encoding="utf-8"))
        pitches = json.loads(Path(a.pitches).read_text(encoding="utf-8"))
        bad = not_in_write(doc, [p["line"] for p in pitches])
        if bad:
            sys.exit("not in the free write word for word, so not his exact words:\n  " + "\n  ".join(bad))
        print(json.dumps({"questions": pitch_rows(doc, pitches, norm(a.summary))}, ensure_ascii=False, indent=1))
        return
    bars_dir = Path(a.corpus) / "corpus" / "bars"
    if not bars_dir.is_dir():
        sys.exit(f"{bars_dir} not found; clone wendell-britt/game-masters-guide or pass --corpus")
    todo = plan(accepted(json.loads(DATA.read_text(encoding="utf-8"))), bars_dir)
    if not todo:
        print("every kept pitch is in the corpus")
        return
    for path, text in todo:
        if a.write:
            path.write_text(text, encoding="utf-8")
        print(("wrote " if a.write else "would write ") + str(path))


if __name__ == "__main__":
    main()
