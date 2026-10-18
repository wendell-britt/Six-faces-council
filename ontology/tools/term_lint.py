#!/usr/bin/env python3
"""Flag retired or reserved ontology terms in the council's working text, with no model in the loop.

    python3 ontology/tools/term_lint.py                 callsheets, docs and open board rows
    python3 ontology/tools/term_lint.py FILE ...        only these files
    python3 ontology/tools/term_lint.py --strict        exit 1 on any finding

Clerical flows (board reads, the compost pass, needs-work) do not load the ontology (docs/ontology-in-flows.md).
This check carries the parts of it they could break: the manifest's `compatibility` block and the deprecated
phrases of the binding WAVE decision. It warns; it never blocks a save. Historical sources under
ontology/v0.1/source/ keep their old words as provenance and are never scanned.
"""
import argparse, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
WAVE_DECISION = "ontology/v0.1/source/council-phase-a/wave-terminology/owner-decision.md"

RULES = [
    (re.compile(r"(?<![A-Za-z0-9_])TensionVector\b"),
     "bare TensionVector is retired; say Tension Map (player-facing) or TensionConfiguration (manifest compatibility)"),
    (re.compile(r"\bBARS321TensionVector\b"),
     "BARS321TensionVector is a deprecated alias of TensionConfiguration (manifest compatibility)"),
    (re.compile(r"\b(five|5) WAVE moves\b", re.I),
     f"the five are the Basic Moves; WAVE is only the Open Up breathing practice ({WAVE_DECISION})"),
    # "complete WAVE" is deprecated only for Wake, Clean, Grow, Show; a finished breathing run is a complete WAVE
    # (oag-wave-ladder), so that phrase needs a reader, not a regex.
    (re.compile(r"\bWAVE order\b|\belemental WAVE\b|\bWAVE progression\b", re.I),
     f"deprecated WAVE usage; Wake, Clean, Grow, Show is the within-channel progression ({WAVE_DECISION})"),
    (re.compile(r"\b(stalled|blocked|stuck) on (Wendell|him)\b|\bWendell'?s? (resistance|avoidance)\b", re.I),
     "names his rest as a deficiency; say what the work waits on (QUICKSTART, Roadblocks; FC-07)"),
]


def default_texts():
    for p in sorted((ROOT / "council/callsheets").glob("*.md")):
        yield p.relative_to(ROOT).as_posix(), p.read_text()
    for p in sorted((ROOT / "docs").glob("*.md")):
        yield p.relative_to(ROOT).as_posix(), p.read_text()
    data = json.loads((ROOT / "board/board_data.json").read_text())
    resolved = data.get("resolved", {})
    for kind in ("positions", "questions", "terms"):
        done = resolved.get(kind, {})
        for row in data.get(kind, []):
            if isinstance(row, dict) and row.get("id") not in done:
                text = " ".join(str(v) for v in row.values() if isinstance(v, str))
                yield f"board/board_data.json {kind} {row.get('id')}", text


def scan(texts):
    hits = []
    for where, text in texts:
        for n, line in enumerate(text.splitlines(), 1):
            for rx, why in RULES:
                m = rx.search(line)
                if m:
                    hits.append(f"{where}:{n}: '{m.group(0)}': {why}")
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()
    texts = [(f, pathlib.Path(f).read_text()) for f in a.files] if a.files else default_texts()
    hits = scan(texts)
    for h in hits:
        print(h)
    print(f"{len(hits)} finding(s)")
    return 1 if a.strict and hits else 0


if __name__ == "__main__":
    sys.exit(main())
