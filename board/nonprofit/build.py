#!/usr/bin/env python3
"""Build the Nonprofit Board from the Council Board's template and the np- rows of board/board_data.json.

Wendell, 2026-10-15: "One of the goals is to be able to access a board structure here for the purposes of the
nonprofit". The Council Board lives in another of his claude.ai organizations, so the nonprofit gets its own page
with the same rows, store and answer flow. Its rows are the ones in board/board_data.json whose ids start with np-,
so a new nonprofit row goes there like any other, and board/pull.py records its answers like any other. The Morning
and Outreach tabs are hidden (they serve the council's day); Open, Your steps and Resolved stay.

The Send button fires the routine "Nonprofit Board: record Wendell's saves" (NONPROFIT_TRIGGER, created 2026-10-15
in the nonprofit's organization; Wendell: "How do we fix that this board can't reach Claude"). Each firing starts a
fresh session that saves this page's store, runs board/pull.py, and republishes this page.

Usage: python3 board/nonprofit/build.py   (from the home repo root)
Then publish board/nonprofit/nonprofit-board.html to https://claude.ai/artifact/8vRXALGmMZKw8g3DdsY8oe without
capabilities (it keeps db and mcp). If capabilities must be passed, pass all of them:
  {"db": {}, "mcp": {"servers": [{"server": "Claude Code Remote", "tools": ["fire_trigger"]}]}}
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
NONPROFIT_TRIGGER = "trig_013Qmc7KZJNNDXAiLbuncGva"
src = json.loads((HERE.parent / "board_data.json").read_text())
ours = lambda rows: [r for r in rows if r["id"].startswith("np-")]
data = {k: type(v)() for k, v in src.items()}
data.update(updated=src["updated"], morning=None, steer_recorded_through=src.get("steer_recorded_through", ""),
            steps_recorded_through=src.get("steps_recorded_through", ""),
            positions=ours(src["positions"]), questions=ours(src["questions"]),
            resolved={k: {i: v for i, v in rows.items() if i.startswith("np-")} for k, rows in src["resolved"].items()})
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
html = (HERE.parent / "template.html").read_text()
trigger = "const PICKUP_TRIGGER = 'trig_01L138vKTaN9MSJoFKRmaBNx'"
assert trigger in html, "the template's pickup trigger line moved; update build.py"
for old, new in [
    (trigger, f"const PICKUP_TRIGGER = '{NONPROFIT_TRIGGER}'"),
    ("<title>Council Board</title>",
     "<title>Nonprofit Board</title>\n<style>#tab-morning,#tab-outreach{display:none!important}</style>"),
    ("<h1>Council Board</h1>", "<h1>Nonprofit Board</h1>"),
    ("on the Council Board at", "on the Nonprofit Board at"),
]:
    html = html.replace(old, new, 1)
html = html.replace("__DATA__", blob)
(HERE / "nonprofit-board.html").write_text(html)
print("wrote nonprofit-board.html")
