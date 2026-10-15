#!/usr/bin/env python3
"""Give every item on his daily intake one written line: the Lens goal it serves, the board row it advances, or a
pitched smaller goal.

Lenses pass 1 (council/passes/6FACE_PASS_lenses1_2026-10-14.md), `lens-intake-align`: "The full intake lists what
you can do today; the board read gives each item one line: the goal it serves, the board row it advances, or a
pitched smaller goal. The reason is written, not word overlap."

The intake is the sealed menu at morning/menu: the lines he lists in the Tap the Vein box under "Everything I can do
today", and the free-write lines he marked To do. The board read reads each item, decides where it goes, and writes
the reason in a sentence. This script checks the read's work and writes it to the board:
- every item gets exactly one alignment, quoted word for word from the menu, so none is skipped or reworded;
- a goal must be one of his active Lens goals (board_data.json `morning.goals`, gathered by council/morning.py);
- a row must be a question or position on the board;
- a pitch names a goal title and either a parent goal (it becomes one cadence smaller under it) or a Lens domain
  (a year goal, for when the domain has none). Each pitch becomes a board question; a kept one is sent to
  bars-engine by `python3 council/lens_goals.py kept --send`.
The alignments go in board_data.json `intake`, and the Morning tab shows each one under its item.

Usage:
  python3 council/intake_align.py <store>/morning/menu.json --aligns aligns.json          # check, write nothing
  python3 council/intake_align.py <store>/morning/menu.json --aligns aligns.json --write  # write and rebuild
      aligns.json: [{"line": "<item, word for word>", "why": "<one sentence>",
                     and one of "goal": "<goal id>" | "row": "<board row id>"
                               | "pitch": {"title": "<a few words>", "parentId": "<goal id>"} or {"title", "domain"}}]
"""
import argparse
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from morning import BOARD, LENS_DOMAINS, ROOT, SMALLER, load_menu  # noqa: E402
from ttv_bars import norm  # noqa: E402

PASS = "lenses: aligning today's intake"
DOMAINS = [d[0] for d in LENS_DOMAINS]


def row_title(r):
    return norm(r.get("q") or r.get("pos") or r.get("id"))[:140]


def align(menu, aligns, data):
    """(intake, pitch questions, problems). Problems stop the write."""
    goals = {g["id"]: g for g in (data.get("morning") or {}).get("goals") or []}
    rows = {r["id"]: r for k in ("questions", "positions") for r in data.get(k, [])}
    lines = [norm(it.get("text")) for it in menu.get("items", [])]
    ids = {l: f"menu-{it.get('key') or i}" for i, (l, it) in enumerate(zip(lines, menu.get("items", [])))}
    date = menu.get("sessionDate") or dt.date.today().isoformat()
    bad, seen, items, pitches = [], set(), [], []
    for a in aligns:
        line, why = norm(a.get("line", "")), norm(a.get("why", ""))
        kinds = [k for k in ("goal", "row", "pitch") if a.get(k)]
        if line not in lines:
            bad.append(f"not an intake item word for word: {line!r}")
            continue
        if line in seen:
            bad.append(f"aligned twice: {line!r}")
        seen.add(line)
        if len(kinds) != 1:
            bad.append(f"needs exactly one of goal, row, pitch: {line!r}")
            continue
        if len(why.split()) < 4:
            bad.append(f"the reason is not written out: {line!r}")
        if kinds[0] == "goal":
            g = goals.get(a["goal"])
            if not g:
                bad.append(f"not one of his active Lens goals: {a['goal']!r}")
                continue
            b = {"kind": "goal", "goalId": g["id"], "goalTitle": g["title"], "cadence": g.get("cadence")}
        elif kinds[0] == "row":
            r = rows.get(a["row"])
            if not r:
                bad.append(f"no board row with id {a['row']!r}")
                continue
            b = {"kind": "row", "rowId": r["id"], "rowTitle": row_title(r)}
        else:
            p, n = a["pitch"], len(pitches) + 1
            title = norm(p.get("title", ""))
            parent = goals.get(p.get("parentId") or "")
            if not title or (p.get("parentId") and not parent) or (not parent and p.get("domain") not in DOMAINS):
                bad.append(f"a pitch needs a title and an active parent goal or one of {DOMAINS}: {line!r}")
                continue
            domain = parent["domain"] if parent else p["domain"]
            cadence = SMALLER.get(parent.get("cadence") or "year", "week") if parent else "year"
            qid = f"intake-goal-{date}-{n}"
            b = {"kind": "pitch", "title": title, "domain": domain, "cadence": cadence, "rowId": qid,
                 **({"parentId": parent["id"], "parentTitle": parent["title"]} if parent else {})}
            under = f"a {cadence} goal under “{parent['title']}”" if parent else f"a {domain} goal for this year"
            pitches.append({
                "id": qid, "faces": ["regent", "diplomat"], "pass": PASS,
                "q": f"Keep “{title}” as {under}?",
                "why_you": f"From your {date} intake: “{line}” {why}",
                "not_before": "No goal you hold covers this item, so the board read pitched one (lens-intake-align).",
                "options": [
                    {"v": "keep", "label": "A. Keep it (recommended)",
                     "c": f"It becomes an active {domain} {cadence} goal in bars-engine, and the Lenses panel shows it."},
                    {"v": "no", "label": "B. Not a goal",
                     "c": "Nothing is saved; the item stays on your intake, unaligned. Rename it in your steer and the next read pitches your wording."}],
                "why": "Pitched by the board read for an intake item (council/intake_align.py).",
                "lens_goal": title, "lens_domain": domain, "lens_line": line, "said": date,
                **({"lens_parent": parent["id"]} if parent else {}),
            })
        items.append({"id": ids[line], "text": line, "bridge": {**b, "why": why}})
    bad += [f"no alignment for: {l!r}" for l in lines if l not in seen]
    intake = {"date": date, "aligned_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
              "items": items}
    return intake, pitches, bad


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("menu", help="the store's morning/menu.json, saved with ArtifactData")
    ap.add_argument("--aligns", required=True, help="the board read's alignments, JSON (see usage)")
    ap.add_argument("--write", action="store_true", help="write `intake` and the pitches into board_data.json")
    a = ap.parse_args()
    data = json.loads(BOARD.read_text(encoding="utf-8"))
    intake, pitches, bad = align(load_menu(a.menu), json.loads(Path(a.aligns).read_text(encoding="utf-8")), data)
    if bad:
        sys.exit("not written:\n  " + "\n  ".join(bad))
    kinds = {}
    for it in intake["items"]:
        kinds[it["bridge"]["kind"]] = kinds.get(it["bridge"]["kind"], 0) + 1
    print(f"intake {intake['date']}: {len(intake['items'])} items, " + ", ".join(f"{k} {n}" for k, n in kinds.items()))
    if not a.write:
        return
    have = {q["id"] for q in data.get("questions", [])}
    clash = [q["id"] for q in pitches if q["id"] in have]
    if clash:
        sys.exit(f"these question ids are already on the board: {clash}")
    data["intake"] = intake
    data.setdefault("questions", []).extend(pitches)
    BOARD.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    subprocess.run([sys.executable, str(ROOT / "board" / "build_board.py")], cwd=ROOT, check=True, capture_output=True)
    print(f"wrote intake and {len(pitches)} goal pitches into board/board_data.json; commit on main and republish")


if __name__ == "__main__":
    main()
