#!/usr/bin/env python3
"""Read each sealed Tap the Vein line as a BAR, gather its context from the record, and set it face to face with the
council work competing for the same hours: work it today, defer it, join it to the strand, or offer to let it go.

Wendell, 2026-10-19: "The tasks that emerge in teh free-write are what by subconcious says is relevant, the tasks being
worked by the Council are ones that have more ergonimics to be worked on because they are context aware. I need the
information from my subconcious to be context aware". Pass ttv-bars 1 (council/passes/6FACE_PASS_ttv-bars1_2026-10-19.md)
set the rules this script checks:
- `tb-sealed-is-bar`: every sealed line is a BAR he kept; one read per line, his line word for word above the face's.
- `tb-face-unpacks`: one face reads it and says what it reaches for in one sentence, the kernel, in his terms.
- `tb-context-first`: what stops it being worked today comes from a fixed list; a face fills a piece only from the
  record (a board row, a call sheet, a pull request, a Lens goal, the history export), with its source. What the
  record cannot fill stays missing. Nothing is written into his task or its notes.
- `tb-face-off`: the opponent is the council's best candidate for today in the same area (the same strand or row
  first; else the top of board/needs_work.py; else the next call sheet entry). Four factors, each shown apart and
  never summed: signal, ready, unlocks, waiting. The call names the factor that decided it.
- `tb-call-is-advice`: the call is advice; he taps the outcome in Tap the Vein. Letting go is only ever offered.
- `tb-loss-not-avoidance`: a line that loses says something about conditions, never about him.

The home is checked by council/intake_align.py, so each read also carries the alignment the Morning tab already shows.
The reads go in board_data.json `intake`, one per item beside its alignment, and the Morning tab shows each as a
face-off card under the Tap the Vein box.

Usage:
  python3 council/bar_read.py <store>/morning/menu.json --reads reads.json [--history history.json]          # check
  python3 council/bar_read.py <store>/morning/menu.json --reads reads.json [--history history.json] --write  # write
      history.json: bars-engine's GET /api/tap-the-vein/history, for each task's carryCount, chargeLevel, blockedAt
      and notes count. Without it the signal shows only what the menu carries.
      reads.json: [{"line": "<his line, word for word>", "face": "shaman|architect|challenger|regent|diplomat|sage",
        "kernel": "<one sentence: what the line reaches for>",
        "home": {one of intake_align.py's goal|row|strand|pitch|none, with "why"},
        "missing": ["next step", "home", "input", "capacity", "blocker"],     # any of these, or []
        "gathered": [{"piece": "<one of missing>", "found": "<what the record says>",
                      "source": "row:<id>|callsheet:<name>|goal:<id>|pr:<owner/repo>#<n>|history:<taskId>"}],
        "opponent": {"kind": "strand|row|needs-work|callsheet", "ref": "<call sheet name, row id or needs-work key>",
                     "what": "<the council work, a few words>"},
        "factors": {"unlocks": {"line": <n>, "council": <n>, "note": "..."},
                    "waiting": {"days": <n>, "note": "<what has sat>"}, "signal": {"note": "..."}, "ready": {"note": "..."}},
        "call": "work-today|defer|join|let-go-offered", "decided_by": "signal|ready|unlocks|waiting",
        "why": "<one sentence he can act on>"}]
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "board"))
import intake_align  # noqa: E402
from morning import BOARD, ROOT, load_menu  # noqa: E402
from ttv_bars import norm  # noqa: E402

FACES = ["shaman", "architect", "challenger", "regent", "diplomat", "sage"]
# The fixed list of what can stop a line being worked today, each written as what would make it workable (the
# Diplomat's copy rule: "needs a first step", never a fault).
MISSING = {"next step": "needs a first step", "home": "needs a home in work you hold", "input": "needs an input it is waiting on",
           "capacity": "needs hours today", "blocker": "needs its blocker cleared"}
FACTORS = ["signal", "ready", "unlocks", "waiting"]
CALLS = {"work-today": "Work it today", "defer": "Rest it in the seed library", "join": "Join it to the council's work",
         "let-go-offered": "Let it go, if you want to"}
SOURCE = re.compile(r"^(row|callsheet|goal|pr|history):(.+)$")
# tb-loss-not-avoidance: the read speaks about conditions, never about him. The standing test, from the Shaman:
# "Does it say something is wrong with them, or something about what I have learned?"
ABOUT_HIM = re.compile(r"\b(avoid\w*|procrastinat\w*|resist\w*|lazy|excuse\w*|self-sabotag\w*|should have|failed to)\b", re.I)
CALLSHEETS = ROOT / "council" / "callsheets"


def next_entry(name):
    """The first entry under a call sheet's `## Next` (or `## Next thread brief`), shortened, or None."""
    path = CALLSHEETS / f"{name}.md"
    if not re.fullmatch(r"[a-z0-9-]+", name or "") or not path.is_file():
        return None
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^## Next[^\n]*\n+(.+?)(?:\n\s*\n|\Z)", text, re.M | re.S)
    return norm(re.sub(r"[`*]", "", m.group(1)))[:200] if m else None


def open_work():
    try:
        import needs_work
        return needs_work.items()
    except Exception:
        return []


def history_tasks(history):
    """{taskId: seed} from the history export: the latest day's copy of each task, with the first day it appeared."""
    out = {}
    for d in (history or {}).get("days", []):
        for s in d.get("seeds", []):
            out[s["id"]] = dict(s, day=out[s["id"]]["day"] if s["id"] in out else d.get("date"))
    return out


def signal(item, seed, date):
    """What his own record says about the line's pull, as facts. A long note buys nothing (the Shaman: "Intimate
    disclosure is not progression currency"), so the notes count is shown under ready, never here."""
    s = {"wroteToday": not seed or seed.get("day") in (None, date), "date": date}
    if seed:
        s |= {"carryCount": seed.get("carryCount", 0), "chargeLevel": seed.get("chargeLevel"),
              "firstDay": seed.get("day")}
    return s


def check(menu, reads, data, history=None, work=None):
    """(intake, pitches, problems). Problems stop the write."""
    aligns = [dict(r.get("home") or {}, line=r.get("line", "")) for r in reads]
    intake, pitches, bad = intake_align.align(menu, aligns, data)
    by_line = {it["text"]: it for it in intake["items"]}
    items = {norm(it.get("text")): it for it in menu.get("items", [])}
    rows = {r["id"]: r for k in ("questions", "positions") for r in data.get(k, [])}
    goals = {g["id"] for g in (data.get("morning") or {}).get("goals") or []}
    work = open_work() if work is None else work
    open_keys = {w["key"]: w for w in work}
    tasks = history_tasks(history)
    date = intake["date"]
    for r in reads:
        line = norm(r.get("line", ""))
        it, row = items.get(line), by_line.get(line)
        if not it or not row:
            continue  # intake_align already said why
        p = []
        face, kernel, why = r.get("face"), norm(r.get("kernel", "")), norm(r.get("why", ""))
        if face not in FACES:
            p.append(f"face must be one of {FACES}")
        if len(kernel.split()) < 5 or kernel.count(". ") or kernel.lower() == line.lower():
            p.append("the kernel is one sentence of five words or more, in the face's words, not the line repeated")
        if len(why.split()) < 5:
            p.append("the why is not written out")
        for text in (kernel, why, *(norm((r.get("factors") or {}).get(f, {}).get("note", "")) for f in FACTORS)):
            if ABOUT_HIM.search(text):
                p.append(f"speaks about him, not the conditions (tb-loss-not-avoidance): {ABOUT_HIM.search(text).group(0)!r}")
        task_id, bar_id = it.get("taskId"), it.get("barId")
        seed = tasks.get(task_id) if task_id else None

        missing = list(r.get("missing") or [])
        unknown = [m for m in missing if m not in MISSING]
        if unknown:
            p.append(f"missing comes from {list(MISSING)}: {unknown}")
        if row["bridge"]["kind"] == "none" and "home" not in missing:
            p.append("no home yet, so home is missing")
        if seed and seed.get("blocked") and "blocker" not in missing:
            p.append("his task is marked blocked, so blocker is missing until something in the record clears it")
        found = {}
        for g in r.get("gathered") or []:
            piece, what, src = g.get("piece"), norm(g.get("found", "")), g.get("source", "")
            m = SOURCE.match(src)
            if piece not in missing:
                p.append(f"gathered {piece!r}, which the read does not list as missing")
            elif len(what.split()) < 4:
                p.append(f"gathered {piece!r} without saying what the record holds")
            elif not m:
                p.append(f"gathered {piece!r} needs a source row:|callsheet:|goal:|pr:|history: {src!r}")
            elif m.group(1) == "row" and m.group(2) not in rows:
                p.append(f"no board row {m.group(2)!r}")
            elif m.group(1) == "callsheet" and not (CALLSHEETS / f"{m.group(2)}.md").is_file():
                p.append(f"no call sheet {m.group(2)!r}")
            elif m.group(1) == "goal" and m.group(2) not in goals:
                p.append(f"not one of his active Lens goals: {m.group(2)!r}")
            elif m.group(1) == "pr" and not re.fullmatch(r"[\w.-]+/[\w.-]+#\d+", m.group(2)):
                p.append(f"a pull request source is owner/repo#n: {m.group(2)!r}")
            elif m.group(1) == "history" and m.group(2) != task_id:
                p.append(f"history source names another task: {m.group(2)!r}")
            else:
                found[piece] = {"piece": piece, "found": what, "source": src}
        still = [m for m in missing if m not in found]

        o = r.get("opponent") or {}
        kind, ref, what = o.get("kind"), o.get("ref", ""), norm(o.get("what", ""))
        b = row["bridge"]
        same = {"strand": b.get("strand"), "row": b.get("rowId")}.get(b["kind"])
        opp = None
        if not what or len(what.split()) < 2:
            p.append("the opponent says what the council work is")
        elif kind == "strand":
            entry = next_entry(ref)
            opp = entry and {"kind": kind, "ref": ref, "what": what, "title": (intake_align.strand(ref, {}) or {}).get("strandTitle", ref), "entry": entry}
            if not entry:
                p.append(f"no call sheet with a Next entry: {ref!r}")
        elif kind == "row":
            opp = ref in rows and {"kind": kind, "ref": ref, "what": what, "title": intake_align.row_title(rows[ref])}
            if not opp:
                p.append(f"no board row {ref!r}")
        elif kind == "needs-work":
            opp = ref in open_keys and {"kind": kind, "ref": ref, "what": what, "title": norm(open_keys[ref]["what"])}
            if not opp:
                p.append(f"not an open needs-work item: {ref!r}")
        elif kind == "callsheet":
            entry = next_entry(ref)
            opp = entry and {"kind": kind, "ref": ref, "what": what, "title": ref, "entry": entry}
            if not entry:
                p.append(f"no call sheet with a Next entry: {ref!r}")
        else:
            p.append("opponent kind is strand, row, needs-work or callsheet")
        # The same area first (tb-face-off): a line at home in a strand or row meets that strand's or row's work.
        # A line at home in a goal meets a strand serving that goal (its call sheet's `lens:` line).
        if same and opp and opp["ref"] != same:
            p.append(f"the line is at home in {same!r}, so its opponent is that work, not {ref!r}")
        served = b["kind"] == "goal" and kind == "strand" and (intake_align.strand(ref, {b["goalId"]: {"title": b["goalTitle"]}}) or {}).get("goalId") == b["goalId"]
        if not same and not served and opp and kind in ("strand", "callsheet") and work:
            p.append("no work shares its area and there is open needs-work, so the opponent comes from board/needs_work.py")

        f_in = r.get("factors") or {}
        if any(k in f_in for k in ("score", "total", "sum", "priority")):
            p.append("the factors are shown apart and never summed into one number")
        u, w = f_in.get("unlocks") or {}, f_in.get("waiting") or {}
        if not all(isinstance(u.get(k), int) for k in ("line", "council")):
            p.append("unlocks counts the items each side removes: {\"line\": n, \"council\": n}")
        if not isinstance(w.get("days"), int):
            p.append("waiting counts the days the council's item has sat: {\"days\": n}")
        factors = {
            "signal": dict(signal(it, seed, date), note=norm((f_in.get("signal") or {}).get("note", ""))),
            "ready": {"lineMissing": still, "councilMissing": [], "notes": (seed or {}).get("notes"),
                      "note": norm((f_in.get("ready") or {}).get("note", ""))},
            "unlocks": {"line": u.get("line"), "council": u.get("council"), "note": norm(u.get("note", ""))},
            "waiting": {"days": w.get("days"), "note": norm(w.get("note", ""))},
        }
        call, decided = r.get("call"), r.get("decided_by")
        if call not in CALLS:
            p.append(f"call is one of {list(CALLS)}")
        if decided not in FACTORS:
            p.append(f"decided_by names one factor of {FACTORS}")
        # Gate 2 (Regent): a line goes to work today only once nothing is missing; a deferral names what is.
        if call == "work-today" and still:
            p.append(f"work today needs a workable line; still missing: {still}")
        if call == "join" and not opp:
            p.append("join needs council work to join")
        if call == "defer" and not still and decided == "ready":
            p.append("deferred on readiness, but nothing is missing")
        if p:
            bad += [f"{line!r}: {x}" for x in p]
            continue
        row["read"] = {"face": face, "kernel": kernel, **({"taskId": task_id} if task_id else {}),
                       **({"barId": bar_id} if bar_id else {}), "missing": missing, "gathered": list(found.values()),
                       "workable": True if not still else still, "opponent": opp, "factors": factors,
                       "call": call, "decidedBy": decided, "why": why}
    intake["read_at"] = intake.pop("aligned_at")
    return intake, pitches, bad


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("menu", help="the store's morning/menu.json, or Tap the Vein's sealed menu")
    ap.add_argument("--reads", required=True, help="the faces' reads, JSON (see usage)")
    ap.add_argument("--history", help="bars-engine's /api/tap-the-vein/history, saved")
    ap.add_argument("--write", action="store_true", help="write `intake` and any goal pitches into board_data.json")
    a = ap.parse_args()
    data = json.loads(BOARD.read_text(encoding="utf-8"))
    history = json.loads(Path(a.history).read_text(encoding="utf-8")) if a.history else None
    intake, pitches, bad = check(load_menu(a.menu), json.loads(Path(a.reads).read_text(encoding="utf-8")), data, history)
    if bad:
        sys.exit("not written:\n  " + "\n  ".join(bad))
    calls = {}
    for it in intake["items"]:
        calls[it["read"]["call"]] = calls.get(it["read"]["call"], 0) + 1
    print(f"reads {intake['date']}: {len(intake['items'])} lines, " + ", ".join(f"{k} {n}" for k, n in calls.items()))
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
    print(f"wrote {len(intake['items'])} reads into board/board_data.json; commit on main and republish")


if __name__ == "__main__":
    main()
