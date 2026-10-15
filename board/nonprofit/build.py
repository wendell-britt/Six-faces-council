#!/usr/bin/env python3
"""Build the Nonprofit Board from the Council Board's template and board/nonprofit/board_data.json.

Wendell, 2026-10-15: "One of the goals is to be able to access a board structure here for the purposes of the
nonprofit". The Council Board lives in another of his claude.ai organizations, so the nonprofit gets its own page
with the same rows, store and answer flow. The Morning and Outreach tabs are hidden (they serve the council's day,
not the nonprofit); Open, Your steps and Resolved stay.

Usage: python3 board/nonprofit/build.py   (from the home repo root)
Then publish board/nonprofit/nonprofit-board.html to https://claude.ai/artifact/8vRXALGmMZKw8g3DdsY8oe with capabilities {"db": {}}.
Answers save to that page's own store; read them with ArtifactData and record them here, the way pull.py records
the Council Board's.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
data = json.loads((HERE / "board_data.json").read_text())
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
html = (HERE.parent / "template.html").read_text()
html = html.replace("<title>Council Board</title>", "<title>Nonprofit Board</title>", 1)
html = html.replace("<h1>Council Board</h1>", "<h1>Nonprofit Board</h1>", 1)
html = html.replace("on the Council Board at", "on the Nonprofit Board at", 1)
html = html.replace("<title>Nonprofit Board</title>",
                    "<title>Nonprofit Board</title>\n<style>#tab-morning,#tab-outreach{display:none!important}</style>", 1)
html = html.replace("__DATA__", blob)
(HERE / "nonprofit-board.html").write_text(html)
print("wrote nonprofit-board.html")
