#!/usr/bin/env python3
"""Build the Nonprofit Board from the Council Board's template and the np- rows of board/board_data.json.

Wendell, 2026-10-15: "One of the goals is to be able to access a board structure here for the purposes of the
nonprofit". The Council Board lives in another of his claude.ai organizations, so the nonprofit gets its own page
with the same rows, store and answer flow. Its rows are the ones in board/board_data.json whose ids start with np-,
so a new nonprofit row goes there like any other, and board/pull.py records its answers like any other. The Morning
and Outreach tabs are hidden (they serve the council's day); Open, Your steps and Resolved stay.

Where it lives (2026-10-16, board-off-vendor-quota): bars-engine serves this file at /board behind Wendell's own
sign-in, and its saves go to Postgres through bars-engine's API (a small store shim stands in for the claude.ai db).
The scheduled Action .github/workflows/board-pull.yml records them on main with board/pull.py; no Claude routine,
connector or token quota sits between a save and main (docs/failure-modes.md). Until 2026-10-15 the Send button fired
the Claude routine trig_013Qmc7KZJNNDXAiLbuncGva, which stalled at 20:09 UTC that day when the account ran out of
tokens (docs/incidents.md). The Send button is gone; the bar now says a save is waiting for the pull.

The claude.ai artifact (https://claude.ai/artifact/8vRXALGmMZKw8g3DdsY8oe) is retired: a published page can reach
bars-engine only through the Vercel connector, which sends a plain GET with no sign-in, so it cannot save through
the same API. It is republished once as a link to /board.

Usage: python3 board/nonprofit/build.py   (from the home repo root; the board-pull Action runs it after each pull)
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
src = json.loads((HERE.parent / "board_data.json").read_text())
ours = lambda rows: [r for r in rows if r["id"].startswith("np-")]
data = {k: type(v)() for k, v in src.items()}
data.update(updated=src["updated"], morning=None, steer_recorded_through=src.get("steer_recorded_through", ""),
            steps_recorded_through=src.get("steps_recorded_through", ""),
            # picks main has recorded, so the page does not count them as waiting. Until 2026-10-16 this list was
            # emptied, and every Send re-sent picks already on main (the 20:09 Send of 2026-10-15 carried four).
            picks=src.get("picks", []),
            positions=ours(src["positions"]), questions=ours(src["questions"]),
            resolved={k: {i: v for i, v in rows.items() if i.startswith("np-")} for k, rows in src["resolved"].items()})
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
html = (HERE.parent / "template.html").read_text()
trigger = "const PICKUP_TRIGGER = 'trig_01L138vKTaN9MSJoFKRmaBNx'"
assert trigger in html, "the template's pickup trigger line moved; update build.py"
for old, new in [
    (trigger, "const PICKUP_TRIGGER = ''"),
    ("btn.hidden = !mcp || !n;", "btn.hidden = true;"),
    ("else msg.textContent = mcp ? `", "else msg.textContent = false ? `"),
    ("`${what} saved. This view cannot reach Claude, so tell Claude in chat that you saved.`",
     "`${what} saved and waiting for the board pull, which records ${n === 1 ? 'it' : 'them'} on main within 15 "
     "minutes. Nobody needs telling.`"),
    ("<title>Council Board</title>",
     "<title>Nonprofit Board</title>\n<style>#tab-morning,#tab-outreach{display:none!important}</style>"),
    ("<h1>Council Board</h1>", "<h1>Nonprofit Board</h1>"),
    ("const STORE_MUST_HOLD = true;", "const STORE_MUST_HOLD = false;"),
    ("on the Council Board at", "on the Nonprofit Board at"),
]:
    html = html.replace(old, new, 1)
for old in ("btn.hidden = !mcp || !n;", "This view cannot reach Claude", "const STORE_MUST_HOLD = true;"):
    assert old not in html, f"the template's Send bar changed ({old!r}); update build.py"
html = html.replace("__DATA__", blob)
(HERE / "nonprofit-board.html").write_text(html)
print("wrote nonprofit-board.html")
