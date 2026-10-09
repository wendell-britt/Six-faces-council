#!/usr/bin/env python3
"""Gather the morning menu: the operations backlog as separate categories, and the lines kept from the free write.

Wendell, 2026-10-09 (morning menu pass 1, council/passes/6FACE_PASS_morning-menu1_2026-10-09.md): "If I'm able to
start the day with a free write and with the context of our operations backlog and what emerges for me during the
free write I can create a menu of things to add to the council board each day that are aligned with my goal."
His steers at the 18:21 board read:
- mm-backlog-sources: "Keep them as separate categories people can explore so they aren't just one long list"
- mm-menu-shape: "All items need a bridge to lens goals and game masters suggest ways to align to lens goals or
  suggest adding lens goals a smaller time scales to integrate (side quests merging into main quest)"

So this script keeps every source as its own category and gives every item a bridge to a Lens goal: the goal it
already names, an existing goal it seems to serve, or a new goal at a smaller time scale under one of his year goals.
The bridges this script suggests come from shared words, never a model; he accepts or edits them on the board.
The menu he keeps is his picks, at most seven (mm-menu-shape).

Categories, in the order the board shows them:
  menu      the lines he kept from this morning's Tap the Vein session (--menu)
  board     questions on the board that wait on him
  due       deferred items due within a week (council/due.py)
  handoff   open items in council/HANDOFF.md
  prs       open pull requests in the three repos (GitHub API with $GITHUB_TOKEN, or --prs)
  backlog   bars-engine .specify/backlog/BACKLOG.md rows marked Ready (--bars)

The menu file is the JSON bars-engine exports at /api/tap-the-vein/menu, or copies with Tap the Vein's "Copy the
sealed menu" button, or the board's store holds once he pastes it (docs/morning.md). Its goals are also what backlog
items are bridged to. Without it, every item is marked unaligned and the report says why.

    python3 council/morning.py --menu <file>             # report: categories, counts, bridges; writes nothing
    python3 council/morning.py --menu <file> --write     # also writes `morning` into board/board_data.json and
                                                         # rebuilds the page; commit on main and republish
    python3 council/morning.py --json                    # the gathered morning as JSON, for checking
"""
import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOARD = ROOT / "board" / "board_data.json"
HANDOFF = ROOT / "council" / "HANDOFF.md"
BOARD_URL = "https://claude.ai/artifact/DxyShVS8tmvJym4HAsgnho"
REPOS = ("wendell-britt/six-faces-council", "johnair01/bars-engine", "wendell-britt/game-masters-guide")

sys.path.insert(0, str(ROOT / "council"))
import due  # noqa: E402

CATEGORIES = {
    "menu": ("From your free write", "The lines you kept this morning. Only kept lines leave Tap the Vein (mm-raw)."),
    "board": ("Waiting on you on the board", "Questions with no answer yet, and new positions that stand unless you flip them."),
    "due": ("Deferred and due", "Items you deferred that come back within a week."),
    "handoff": ("Open in the handoff", "Work a thread left open in council/HANDOFF.md."),
    "prs": ("Open pull requests", "Pull requests open in the council, bars-engine and the Game Master's guide."),
    "backlog": ("bars-engine backlog", "Rows marked Ready in bars-engine's BACKLOG.md."),
}

# Smaller time scales under a goal, for a suggested new goal (the side quest that merges into the main quest).
SMALLER = {"year": "quarter", "quarter": "month", "month": "week", "week": "week"}
STOP = set("""a an and are as at be been but by can do for from has have he his i in into is it its me my no not of
on or our out so that the their them then there they this to up was we were what when which who will with you your
waits wait open next now new one two each still once only also then than more most just about after before day days
every week weeks month year today""".split())


# ---------- bridging ----------

def words(text):
    """Content words, cut to five letters so 'podcasts' meets 'podcast' and 'health' meets 'healthy'."""
    return {w[:5] for w in re.findall(r"[a-z][a-z'-]{2,}", (text or "").lower()) if w not in STOP}


def bridge(text, goals, named=None):
    """How an item reaches a Lens goal: the goal it names, an existing goal it shares words with, a new smaller goal
    under the year goal it is closest to, or unaligned. Every bridge but `named` is a suggestion he accepts or edits."""
    by_id = {g["id"]: g for g in goals}
    if named and named in by_id:
        g = by_id[named]
        return {"kind": "named", "goalId": g["id"], "goalTitle": g["title"], "cadence": g.get("cadence")}
    if not goals:
        return {"kind": "unaligned", "why": "no Lens goals were read this morning"}
    mine = words(text)
    scored = sorted(((len(mine & words(f"{g['title']} {g.get('description') or ''} {g.get('domain') or ''}")), g)
                     for g in goals), key=lambda s: (-s[0], order(s[1])))
    best, g = scored[0]
    if best >= 2:
        return {"kind": "existing", "goalId": g["id"], "goalTitle": g["title"], "cadence": g.get("cadence")}
    if best == 1:
        top = year_goal(g, by_id)
        cadence = SMALLER.get(g.get("cadence") or "year", "week")
        return {"kind": "new", "parentId": g["id"], "parentTitle": g["title"], "yearGoalTitle": top["title"],
                "cadence": cadence, "title": short(text)}
    return {"kind": "unaligned", "why": "shares no words with any Lens goal"}


def order(g):
    return ["week", "month", "quarter", "year"].index(g.get("cadence")) if g.get("cadence") in SMALLER else 9


def year_goal(g, by_id):
    seen = set()
    while g.get("parentId") and g["parentId"] in by_id and g["id"] not in seen:
        seen.add(g["id"])
        g = by_id[g["parentId"]]
    return g


def short(text, n=90):
    text = re.sub(r"\s+", " ", re.sub(r"[`*]", "", text or "")).strip()
    return text if len(text) <= n else text[: n - 1].rsplit(" ", 1)[0] + "…"


# ---------- sources ----------

def from_menu(menu):
    """Kept lines and tasks from the sealed menu. Its bridges are his: a suggestion he never accepted comes through as
    unaligned (bars-engine #267), so `bridged` is always a goal he chose."""
    items = []
    for it in menu.get("items", []):
        g = it.get("goal") if it.get("status") == "bridged" else None
        items.append({"id": f"menu-{it.get('key') or len(items)}", "text": short(it.get("text"), 240),
                      "named": (g or {}).get("id"), "note": (g or {}).get("trace") or {"kept_line": "Kept line", "task": "Task"}.get(it.get("source"), "")})
    return items


def menu_goals(menu):
    """His active Lens goals: the export's goals list when it carries one, else the goals its bridged items name."""
    if menu.get("goals"):
        return [g for g in menu["goals"] if g.get("status", "active") == "active"]
    seen = {}
    for it in menu.get("items", []):
        g = it.get("goal")
        if g and g.get("id") and g["id"] not in seen:
            seen[g["id"]] = {k: g.get(k) for k in ("id", "title", "domain", "cadence")} | {"parentId": None}
    return list(seen.values())


def load_menu(path):
    """The menu as Tap the Vein's export or its Copy button gives it, or as the board's store saved it (a doc whose
    `menu` field holds the pasted text)."""
    menu = json.loads(Path(path).read_text(encoding="utf-8"))
    for _ in range(2):
        inner = menu.get("menu") if isinstance(menu, dict) else None
        if inner is None:
            break
        menu = json.loads(inner) if isinstance(inner, str) else inner
    return menu


def from_board(data):
    """Open questions first, then positions on the Open tab that stand unless he flips them."""
    res = data.get("resolved", {})
    qs = [{"id": f"board-{q['id']}", "text": short(q.get("q"), 240), "ref": q["id"], "link": BOARD_URL + "#open",
           "note": f"question, {q.get('pass')}"} for q in data.get("questions", []) if q["id"] not in res.get("questions", {})]
    ps = [{"id": f"board-{p['id']}", "text": short(p.get("pos"), 240), "ref": p["id"], "link": BOARD_URL + "#open",
           "note": f"position, stands unless you flip it, {p.get('pass')}"}
          for p in data.get("positions", []) if p["id"] not in res.get("positions", {})]
    return qs + ps


def from_due(data, ahead=7):
    now = dt.datetime.now(dt.timezone.utc)
    items = []
    for kind, id_, e, row in due.deferred(data):
        until = e.get("until")
        if until and due.when(until) > now + dt.timedelta(days=ahead):
            continue
        title = row.get("q") or row.get("pos") or id_
        items.append({"id": f"due-{id_}", "text": short(title, 240), "ref": id_, "link": BOARD_URL + "#resolved",
                      "note": f"due {until[:10]}" if until else "when you ask"})
    return items


def from_handoff(path=HANDOFF):
    items, section = [], ""
    lines = path.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        if line.startswith("## Open on"):
            section = line[3:].strip()
            continue
        m = re.match(r"- \*\*(.+?)\*\*(.*)", line)
        if not (m and section):
            continue
        label = m.group(1).rstrip(":").strip()
        if re.search(r"\b(done|closed|recorded|picked)\b", label, re.I):
            continue
        rest = m.group(2)
        for nxt in lines[i + 1:i + 3]:
            if not nxt.startswith("  "):
                break
            rest += " " + nxt.strip()
        first = re.split(r"(?<=[.!?])\s", rest.lstrip(" :"), maxsplit=1)[0]
        items.append({"id": "handoff-" + slug(f"{section[8:18]}-{label}"), "text": short(f"{label}: {first}", 240),
                      "note": section})
    return items


def from_prs(path=None):
    if path:
        prs = json.loads(Path(path).read_text(encoding="utf-8"))
    else:
        token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
        if not token:
            return [], "no GitHub token in this session; pass --prs <file> saved from the GitHub tools"
        prs = []
        for repo in REPOS:
            req = urllib.request.Request(f"https://api.github.com/repos/{repo}/pulls?state=open&per_page=50",
                                         headers={"Authorization": f"Bearer {token}",
                                                  "Accept": "application/vnd.github+json"})
            try:
                with urllib.request.urlopen(req, timeout=20) as r:
                    for p in json.load(r):
                        prs.append({"repo": repo, "number": p["number"], "title": p["title"],
                                    "url": p["html_url"], "draft": p.get("draft", False)})
            except Exception as e:  # one repo out of reach should not empty the others
                return prs, f"{repo}: {e}"
    return [{"id": f"pr-{p['repo'].split('/')[1]}-{p['number']}", "text": short(p["title"], 240), "link": p["url"],
             "note": f"{p['repo'].split('/')[1]} #{p['number']}" + (" (draft)" if p.get("draft") else "")}
            for p in prs], None


def from_backlog(bars):
    path = Path(bars) / ".specify" / "backlog" / "BACKLOG.md"
    if not path.exists():
        return [], f"no {path}; pass --bars <bars-engine checkout>"
    items = []
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5 or not re.search(r"\[ \]\s*Ready", cells[4]) or "RETIRED" in cells[2]:
            continue
        code = cells[1].strip("* ")
        m = re.match(r"\[([^\]]+)\]\(([^)]+)\)\s*(?:—\s*)?(.*)", cells[2])
        name, link, rest = (m.group(1), m.group(2), m.group(3)) if m else (re.sub(r"\*\*", "", cells[2]), "", "")
        url = f"https://github.com/johnair01/bars-engine/blob/main/{link.lstrip('./')}" if link.startswith(".") else ""
        items.append({"id": f"backlog-{code.lower()}", "text": short(f"{name}: {re.sub(r'[*`]', '', rest)}", 240),
                      "link": url, "note": f"{cells[0].strip('* ')} {code}"})
    return items, None


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60]


# ---------- gather ----------

def gather(menu, prs_file=None, bars=None, data=None):
    data = data if data is not None else json.loads(BOARD.read_text(encoding="utf-8"))
    goals = menu_goals(menu) if menu else []
    notes = {}
    raw = {"menu": from_menu(menu) if menu else [], "board": from_board(data), "due": from_due(data),
           "handoff": from_handoff()}
    if not menu:
        notes["menu"] = "no menu read this morning; seal Tap the Vein, then fetch the export (docs/morning.md)"
    raw["prs"], notes["prs"] = from_prs(prs_file)
    raw["backlog"], notes["backlog"] = from_backlog(bars or ROOT.parent / "bars-engine")
    cats = []
    for key, (title, blurb) in CATEGORIES.items():
        items = raw[key]
        for it in items:
            it["bridge"] = bridge(it["text"], goals, it.pop("named", None))
        # mm-menu-shape: aligned first, unaligned last, never hidden
        items.sort(key=lambda it: ["named", "existing", "new", "unaligned"].index(it["bridge"]["kind"]))
        cats.append({"key": key, "title": title, "blurb": blurb, "items": items,
                     **({"note": notes[key]} if notes.get(key) else {})})
    return {"date": (menu or {}).get("sessionDate") or dt.date.today().isoformat(),
            "gathered_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "pick_limit": 7,
            "goals": [{k: g.get(k) for k in ("id", "title", "domain", "cadence", "parentId")} for g in goals],
            "categories": cats}


def report(m):
    print(f"morning {m['date']}: {len(m['goals'])} Lens goals read")
    for c in m["categories"]:
        kinds = {}
        for it in c["items"]:
            kinds[it["bridge"]["kind"]] = kinds.get(it["bridge"]["kind"], 0) + 1
        k = ", ".join(f"{v} {n}" for n, v in kinds.items()) or "empty"
        print(f"  {c['key']:<8} {len(c['items']):>3} items ({k})" + (f"  [{c['note']}]" if c.get("note") else ""))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--menu", help="the Tap the Vein export saved to a file")
    ap.add_argument("--prs", help="open pull requests saved to a file: [{repo, number, title, url, draft}]")
    ap.add_argument("--bars", help="a bars-engine checkout (default ../bars-engine)")
    ap.add_argument("--write", action="store_true", help="write `morning` into board/board_data.json and rebuild")
    ap.add_argument("--json", action="store_true", help="print the gathered morning as JSON")
    a = ap.parse_args(argv)
    menu = load_menu(a.menu) if a.menu else None
    if menu and "rawEntry" in json.dumps(menu):
        sys.exit("the menu file carries a rawEntry; only kept lines may leave Tap the Vein (mm-raw)")
    data = json.loads(BOARD.read_text(encoding="utf-8"))
    m = gather(menu, a.prs, a.bars, data)
    if a.json:
        print(json.dumps(m, ensure_ascii=False, indent=1))
        return
    report(m)
    if a.write:
        data["morning"] = m
        BOARD.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        subprocess.run([sys.executable, str(ROOT / "board" / "build_board.py")], cwd=ROOT, check=True,
                       capture_output=True)
        print(f"wrote morning into board/board_data.json; commit on main and republish to {BOARD_URL}")


if __name__ == "__main__":
    main()
