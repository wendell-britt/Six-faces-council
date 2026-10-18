#!/usr/bin/env python3
"""Pitch year goals for an empty Lens domain from the board's Tap the Vein free write, and send the ones he keeps to
bars-engine as active goals.

Lenses pass 1 (council/passes/6FACE_PASS_lenses1_2026-10-14.md), `lens-pitch-goals`: "When a domain has no goals, the
board's Tap the Vein box offers that domain's prompt. The board read pitches year goals from what you wrote, quoting
your line, and each pitch you keep is written to bars-engine as an active goal."

It runs alongside council/ttv_bars.py, in the same two board reads:
1. The board's Tap the Vein box shows one empty domain's prompt; sealing saves it as `lensDomain` on morning/freewrite.
   The board read, before it deletes the free write, pitches one to three year goals for that domain. Each pitch
   quotes a line of his word for word (`pitch` refuses any other line) and names the goal in a few words. Rows go in
   with board/sync_board.py, like the BAR pitches.
2. He answers on the board. After board/pull.py records the answers, `kept` posts each kept goal to
   bars-engine's POST /api/lenses/goals with $COUNCIL_MENU_TOKEN. bars-engine skips a goal it already holds, so this
   is safe to run twice. Then run `python3 council/morning.py --write` so the Lenses panel shows it.

Usage:
  python3 council/lens_goals.py pitch <store>/morning/freewrite.json --pitches goals.json > rows.json
      goals.json: [{"title": "<the goal, a few words>", "line": "<his exact words>", "why": "<one line>"}, ...]
  python3 council/lens_goals.py kept [--send]
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ttv_bars import DATA, norm, not_in_write  # noqa: E402

GOALS_URL = "https://bars-engine.vercel.app/api/lenses/goals"
DOMAINS = ("relationships", "career", "money", "health", "allyship")
PASS = "lenses: year goals from the free write"


def pitch_rows(doc, pitches):
    """One board question per pitched goal: keep it as a year goal in that domain, or not."""
    domain = doc.get("lensDomain")
    if domain not in DOMAINS:
        sys.exit("the free write names no Lens domain (lensDomain), so there is nothing to pitch goals for")
    date = doc.get("sessionDate") or (doc.get("savedAt") or "")[:10]
    rows = []
    for i, p in enumerate(pitches, 1):
        goal, line = norm(p["title"]), norm(p["line"])
        rows.append({
            "id": f"lens-goal-{date}-{i}", "faces": ["regent", "shaman"], "pass": PASS,
            "q": f"Keep “{goal}” as a {domain} goal for this year?",
            "why_you": f"From your {date} free write: “{line}” {p.get('why', '')}".strip(),
            "not_before": f"{domain.title()} had no Lens goals, so the Tap the Vein box offered its prompt (lens-pitch-goals).",
            "options": [
                {"v": "keep", "label": "A. Keep it (recommended)", "c": f"It becomes an active {domain} year goal in bars-engine, and the Lenses panel shows it."},
                {"v": "no", "label": "B. Not a goal", "c": "Nothing is saved. Rename it in your steer and the next read pitches your wording."}],
            "why": "Pitched by the board read from the sealed free write (council/lens_goals.py pitch).",
            "lens_goal": goal, "lens_domain": domain, "lens_line": line, "said": date,
        })
    return rows


def kept(data):
    """{domain, title, source[, parentId]} for each pitched goal he kept, from the free write (this script) or the
    intake (council/intake_align.py; a parentId makes it one cadence smaller under that goal)."""
    res = data.get("resolved", {}).get("questions", {})
    out = []
    for q in data.get("questions", []):
        r = res.get(q["id"])
        if q.get("lens_goal") and r and r.get("decision") == "keep":
            where = "intake" if q.get("pass", "").startswith("lenses: aligning") else "free write"
            out.append({"domain": q["lens_domain"], "title": q["lens_goal"],
                        "source": f"Council Board, {q['id']}, from his {q['said']} {where}"
                                  + (f", in the council's words: {q['lens_line']}" if q.get("lens_paraphrase")
                                     else f": “{q['lens_line']}”"),
                        **({"parentId": q["lens_parent"]} if q.get("lens_parent") else {})})
    return out


def send(goals):
    # The cloud environment's proxy adds the token for bars-engine.vercel.app when the session has none.
    token = os.environ.get("COUNCIL_MENU_TOKEN", "").strip()
    headers = {"Content-Type": "application/json"} | ({"Authorization": f"Bearer {token}"} if token else {})
    req = urllib.request.Request(GOALS_URL, data=json.dumps({"goals": goals}).encode("utf-8"), method="POST",
                                 headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read().decode("utf-8"))["goals"]
    except urllib.error.HTTPError as e:
        sys.exit(f"bars-engine refused the goals: HTTP {e.code} {e.read().decode('utf-8', 'replace')[:300]}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("pitch", help="board rows for the pitched goals, printed as sync_board.py --rows JSON")
    p.add_argument("freewrite", help="the store's morning/freewrite.json, saved with ArtifactData")
    p.add_argument("--pitches", required=True, help='JSON list of {"title", "line", "why"}')
    k = sub.add_parser("kept", help="post each kept goal to bars-engine")
    k.add_argument("--send", action="store_true", help="post them; without it, list them")
    a = ap.parse_args()
    if a.cmd == "pitch":
        doc = json.loads(Path(a.freewrite).read_text(encoding="utf-8"))
        pitches = json.loads(Path(a.pitches).read_text(encoding="utf-8"))
        bad = not_in_write(doc, [p["line"] for p in pitches])
        if bad:
            sys.exit("not in the free write word for word, so not his exact words:\n  " + "\n  ".join(bad))
        print(json.dumps({"questions": pitch_rows(doc, pitches)}, ensure_ascii=False, indent=1))
        return
    goals = kept(json.loads(DATA.read_text(encoding="utf-8")))
    if not goals:
        print("no kept goal pitches")
        return
    if not a.send:
        for g in goals:
            print(f"would send {g['domain']}: {g['title']}")
        return
    for g in send(goals):
        print(f"{g['status']} {g['domain']} {g.get('cadence', 'year')}: {g['title']}")


if __name__ == "__main__":
    main()
