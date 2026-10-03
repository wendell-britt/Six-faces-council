#!/usr/bin/env python3
"""Deferred board items that are due back, and the context that changed while they waited.

Wendell, 2026-10-03: "We want to use spaced repetition so that tasks that are deferred come back and
the council can weigh in on them in new context." Spec: .specify/specs/spaced-deferral/spec.md.

    python3 council/due.py                 # items due now, each with what changed since its deferral
    python3 council/due.py --ahead 7       # also items due in the coming 7 days (the weekly run uses this)
    python3 council/due.py --all           # every deferred item, due or not, with its next spaced wait
    python3 council/due.py --at 2026-11-03T09:00:00Z
    python3 council/due.py --context flirtcraft --since 2026-10-02   # the context brief alone

The weekly session, and every session that reads the board, runs it with --ahead 7. For each item due by
then, the council re-weighs it from the brief and writes the result onto the row as `review`, so the item
reaches the Open tab with its new context instead of bare (Wendell, 2026-10-03: "they should prepare items
due in the coming week"). Reading never writes anything.

    python3 council/due.py record questions/ID --saved-at 2026-10-03T18:08:52Z --until spaced --hours 720 \
        --steer "his words" --ledger "council/ledger/<read>.json (six-faces-council)"

records a deferral he saved on the board into board_data.json, with its date worked out the board's way and
every earlier deferral of the item kept. It writes that one file and nothing else.
"""

import argparse
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOARD = ROOT / "board" / "board_data.json"

# Wendell's ladder, 2026-10-03: "The spaced repetition of deferrals should start with 1 hr to 6 hours to 24
# hours to 3 days to a week to 2 weeks to a month". It replaced the council's week-then-double (pass eight).
# Two readings are the session's, not his, and are said so in the spec: a spaced deferral steps to the first
# rung longer than the item's last wait, so a deferral he set by hand counts; and past the top rung it stays at
# a month. The board shows the same ladder; the two copies name each other. A week, a month and "when I ask"
# stay on the board's list.
LADDER_HOURS = [1, 6, 24, 72, 168, 336, 720]
NAMED = {"week": 168, "month": 720}


def when(s: str) -> dt.datetime:
    """An until or saved_at value as a UTC time. A date alone, as the first deferrals were recorded, is midnight UTC."""
    s = s.replace("Z", "+00:00")
    t = dt.datetime.fromisoformat(s if "T" in s else s + "T00:00:00+00:00")
    return t if t.tzinfo else t.replace(tzinfo=dt.timezone.utc)


def iso(t: dt.datetime) -> str:
    return t.astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def human(hours: int) -> str:
    named = {1: "1 hour", 24: "1 day", 168: "1 week", 336: "2 weeks", 720: "1 month"}
    if hours in named:
        return named[hours]
    return f"{hours} hours" if hours < 24 else f"{round(hours / 24)} days"


def history(entry: dict) -> list[dict]:
    """Every deferral of one item, oldest first. An entry recorded before history existed counts as one."""
    h = list(entry.get("history") or [])
    if not h and entry.get("decision") == "deferred":
        h = [{"recorded": entry.get("recorded"), "until": entry.get("until")}]
    return h


def hours_of(d: dict) -> int | None:
    """How long one deferral waited, in hours. The first deferrals were recorded in days."""
    if d.get("hours"):
        return int(d["hours"])
    if d.get("days"):
        return int(d["days"]) * 24
    start = d.get("saved_at") or d.get("recorded")
    if start and d.get("until"):
        return round((when(d["until"]) - when(start)).total_seconds() / 3600)
    return None


def next_hours(entry: dict | None) -> int:
    """The next spaced wait for this item: the ladder's first rung longer than its last wait, or the top rung."""
    waits = [w for w in (hours_of(d) for d in history(entry or {})) if w]
    if not waits:
        return LADDER_HOURS[0]
    return next((r for r in LADDER_HOURS if r > waits[-1]), LADDER_HOURS[-1])


def project_of(entry: dict) -> str | None:
    """The project a deferral concerns: named on the entry, or read from the ledger record it points at."""
    if entry.get("project"):
        return entry["project"]
    rec = (entry.get("record") or "").split(" (")[0]
    for base in (ROOT, ROOT / "council"):
        p = base / rec
        if rec and p.is_file():
            d = json.loads(p.read_text())
            return d.get("subject_project") or d.get("project")
    return None


def git(repo: Path, *args: str) -> str:
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def commits(project: str, since: str) -> list[str]:
    """Changes that landed on the project's main branch since the deferral, read from the sibling clone."""
    repo = ROOT.parent / project
    if not (repo / ".git").exists():
        return [f"(no local clone of {project}; its changes were not read)"]
    git(repo, "fetch", "-q", "origin", "main")
    out = git(repo, "log", "origin/main", f"--since={since}", "--first-parent", "--format=%ad %s", "--date=short")
    return [l for l in out.splitlines() if l.strip()]


def committed_at(path: Path) -> str:
    """When a file first reached its repo, as UTC ISO time. A ledger record carries only a date, and the
    first test of this script (pass eight) showed same-day records from before the deferral."""
    out = git(path.parent, "log", "--diff-filter=A", "--format=%cI", "--", path.name).split()
    if not out:
        return ""
    return dt.datetime.fromisoformat(out[-1]).astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def records(project: str, since: str, skip: str = "") -> list[str]:
    """Ledger records about the project that reached their repo after the deferral, from every sibling repo's ledger."""
    out = []
    for p in sorted(ROOT.parent.glob("*/council/ledger/**/*.json")):
        try:
            d = json.loads(p.read_text())
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not isinstance(d, dict) or (d.get("date") or "") < since[:10] or (skip and p.name == skip):
            continue
        if len(since) > 10 and (committed_at(p) or since) <= since:
            continue
        if project not in (d.get("project"), d.get("subject_project")):
            continue
        what = d.get("question") or d.get("id") or p.stem
        acted = d.get("acted_on") or []
        out.append(f"{d.get('date')} {what} ({p.parent.parent.parent.name}/{p.name})"
                   + "".join(f"\n      acted on: {a}" for a in acted[:4]))
    return out


def lessons(since: str) -> list[str]:
    """Face and council lessons dated after the deferral day, plus that day's, marked. They bind the re-weigh.
    A lesson carries only a date, so a same-day lesson may predate the deferral."""
    try:
        import yaml  # type: ignore
    except ImportError:
        return ["(pyyaml not installed; lessons were not read)"]
    d = yaml.safe_load((ROOT / "council" / "faces.yaml").read_text())
    out = []
    groups = [(n, f.get("lessons") or []) for n, f in d["faces"].items()] + [("council", d.get("council_lessons") or [])]
    for name, ls in groups:
        for l in ls:
            day = str(l.get("date", ""))
            if day >= since[:10]:
                out.append(f"{day}{' (same day)' if day == since[:10] else ''} {name}: {l.get('lesson')}")
    return out


def brief(project: str | None, since: str, skip: str = "") -> str:
    lines = []
    if project:
        c = commits(project, since)
        lines.append(f"  landed in {project} since {since}: {len(c)}")
        lines += [f"    {x}" for x in c[:15]] + ([f"    ... and {len(c) - 15} more"] if len(c) > 15 else [])
        r = records(project, since, skip)
        lines.append(f"  council records about {project} since {since}: {len(r)}")
        lines += [f"    {x}" for x in r[:10]]
    else:
        lines.append("  project unknown: name it on the entry so its changes can be read")
    ls = lessons(since)
    lines.append(f"  lessons ruled since {since}: {len(ls)}")
    lines += [f"    {x}" for x in ls]
    return "\n".join(lines)


def deferred(data: dict):
    for kind in ("questions", "positions"):
        rows = {r["id"]: r for r in data.get(kind, [])}
        for id_, e in (data.get("resolved", {}).get(kind) or {}).items():
            if e.get("decision") == "deferred":
                yield kind, id_, e, rows.get(id_, {})


def record(data: dict, kind: str, id_: str, saved_at: str, until: str, steer: str, ledger: str,
           hours: int | None = None) -> dict:
    """Record one deferral on the board data, the way the board computed it, keeping every earlier deferral.

    until is spaced, week, month or ask, as the board saves it. A spaced deferral waits `hours` (the wait the
    board showed him) or, when that is missing, the next rung of the ladder. The row's old review is cleared,
    because it described the return he has just answered."""
    res = data["resolved"][kind]
    old = res.get(id_) or {}
    h = history(old)
    wait = None if until == "ask" else (hours or next_hours(old) if until == "spaced" else NAMED[until])
    day = saved_at[:10]
    back = iso(when(saved_at) + dt.timedelta(hours=wait)) if wait else None
    h.append({"recorded": day, "saved_at": saved_at, "until": back, "hours": wait, "steer": steer or None})
    res[id_] = {k: v for k, v in {
        "decision": "deferred", "until": back, "project": old.get("project"),
        "label": f"Deferred {human(wait) + ', until ' + back if back else 'until he asks'}",
        "recorded": day, "record": ledger, "history": [{k: v for k, v in d.items() if v is not None} for d in h],
    }.items() if v is not None}
    for row in data.get(kind, []):
        if row["id"] == id_:
            row.pop("review", None)
    return res[id_]


def main(argv: list[str]) -> int:
    if argv[:1] == ["record"]:
        ap = argparse.ArgumentParser(prog="due.py record", description=record.__doc__.split("\n")[0])
        ap.add_argument("item", help="kind/id, for example questions/fcm-oracle-drafts")
        ap.add_argument("--saved-at", required=True, help="the savedAt time from the board's store")
        ap.add_argument("--until", required=True, choices=["spaced", "week", "month", "ask"])
        ap.add_argument("--hours", type=int, help="the wait the board showed, in hours, for a spaced deferral")
        ap.add_argument("--steer", default="")
        ap.add_argument("--ledger", required=True, help="the ledger record of this board read")
        ap.add_argument("--project")
        a = ap.parse_args(argv[1:])
        kind, id_ = a.item.split("/", 1)
        data = json.loads(BOARD.read_text())
        e = record(data, kind, id_, a.saved_at, a.until, a.steer, a.ledger, a.hours)
        if a.project:
            e["project"] = a.project
        BOARD.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
        print(json.dumps(e, indent=1, ensure_ascii=False))
        return 0

    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--at", default=iso(dt.datetime.now(dt.timezone.utc)), help="the time to check against, UTC")
    ap.add_argument("--ahead", type=float, default=0, help="also list items due within this many days")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--context", metavar="PROJECT")
    ap.add_argument("--since")
    a = ap.parse_args(argv)
    if a.context:
        print(brief(a.context, a.since or a.at))
        return 0
    data = json.loads(BOARD.read_text())
    n = 0
    for kind, id_, e, row in deferred(data):
        until = e.get("until")
        now, horizon = when(a.at), when(a.at) + dt.timedelta(days=a.ahead)
        due = bool(until and when(until) <= horizon)
        if not (due or a.all):
            continue
        n += 1
        h = history(e)
        title = row.get("q") or row.get("pos") or ""
        state = ("DUE" if when(until) <= now else "DUE SOON") if due else "waiting"
        print(f"{state} {kind}/{id_}: deferred {len(h)} time(s), until {until or 'he asks'}")
        print(f"  {title[:160]}")
        for d in h:
            print(f"  deferred {d.get('recorded')} until {d.get('until') or 'he asks'}"
                  + (f": \"{d['steer']}\"" if d.get("steer") else ""))
        print(f"  next spaced wait if deferred again: {human(next_hours(e))}")
        if due:
            since = h[-1].get("saved_at") or h[-1].get("recorded") or e.get("recorded")
            print(brief(project_of(e), since, Path((e.get("record") or "").split(" (")[0]).name))
        print()
    if not n:
        print("nothing is deferred" if a.all else f"nothing deferred is due by {iso(when(a.at) + dt.timedelta(days=a.ahead))}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
