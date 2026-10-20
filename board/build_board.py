#!/usr/bin/env python3
"""Build council-board.html from board/template.html and board/board_data.json.

Usage: python3 board/build_board.py   (from the home repo root)
To change the board, edit board_data.json: add rows to positions, questions, terms or causes, and
when a board read is recorded in the ledger, add the item to `resolved` with its decision and the
ledger file. The page shows open rows on its first view and everything resolved on the second.
Then publish board/council-board.html to the same artifact URL,
https://claude.ai/artifact/DxyShVS8tmvJym4HAsgnho.
Ledger paths in `resolved` before 2026-10-02T22:05Z point into johnair01/bars-engine's
.specify/specs/six-faces-council-agents/; later ones point into this repo's council/ledger/.
A question option is {"v", "label", "c"}: the page saves `v` as the choice, so an option without one can never be
saved (2026-10-17: slice-substrate-home was written with `consequence` and no `v`, and its Save never fired). The
build warns rather than stops, so a bad row never blocks saves reaching main; tests/test_board_options.py fails.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import page_calls  # noqa: E402

HERE = Path(__file__).resolve().parent


def option_problems(data):
    out = []
    for q in data.get("questions", []):
        opts = q.get("options", [])
        for o in opts:
            if not o.get("v") or "c" not in o:
                out.append(f"{q['id']}: option {o.get('label')!r} needs a `v` and a `c`")
        if len({o.get("v") for o in opts}) != len(opts):
            out.append(f"{q['id']}: option `v` values repeat")
    return out


def main():
    data = json.loads((HERE / "board_data.json").read_text())
    problems = option_problems(data)
    if problems:
        print("WARNING: board_data.json has options the page cannot save:\n  " + "\n  ".join(problems), file=sys.stderr)
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = (HERE / "template.html").read_text().replace("__DATA__", blob)
    # A call to a function the page no longer defines throws on load and blanks every tab fed by the store
    # (council/postmortems/2026-10-20-steps-outreach-blank.md), so such a page is never written.
    missing = page_calls.undefined_calls(html)
    if missing:
        sys.exit("refusing to build: the page calls names it never defines: " + ", ".join(missing))
    (HERE / "council-board.html").write_text(html)
    print("wrote council-board.html")


if __name__ == "__main__":
    main()
