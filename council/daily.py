#!/usr/bin/env python3
"""The daily session's move: its level, today's move, its limits, and the record of what it did.

Wendell, 2026-10-03: "It should be able to check in it's own and eventually find work to do that pushes the
needle even if I'm unavailable." Spec: .specify/specs/five-moves/spec.md. Settings: council/daily.yaml.

    python3 council/daily.py                  # today's plan: level, move, rows allowed, limits, the record so far
    python3 council/daily.py record --move wake --found "..." --finished "..." [--branch B] [--pr URL] [--row ID]
    python3 council/daily.py usage <record file> --session ID --input N --output N --cost USD

The move rotates in Wendell's order by the number of runs recorded, so a missed day does not skip a move.
A row the session adds to the board has the id dy-<date>-<move>, so its standing can be read back here.
The token figures come from the session record (get_session's usage), which a session that holds the
claude-code-remote tools reads after a run ends; `usage` writes them into that run's record.
"""

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONF = ROOT / "council" / "daily.yaml"
LEDGER = ROOT / "council" / "ledger"
BOARD = ROOT / "board" / "board_data.json"


def conf() -> dict:
    return yaml.safe_load(CONF.read_text())


def runs() -> list[tuple[Path, dict]]:
    """Every recorded run, oldest first, by the time it was recorded. File names cannot order them: a day's
    first record, <date>-daily.json, sorts after its later ones, <date>-daily-2.json."""
    out = []
    for p in LEDGER.glob("*-daily*.json"):
        d = json.loads(p.read_text())
        if d.get("move"):
            out.append((p, d))
    return sorted(out, key=lambda pd: (pd[1].get("recorded_at") or pd[1].get("date", ""), pd[0].name))


def standing(row: str) -> str:
    """How Wendell ruled on one of the session's rows: stands, overrule, another decision, or waiting."""
    res = json.loads(BOARD.read_text()).get("resolved", {})
    for kind in ("positions", "questions"):
        e = (res.get(kind) or {}).get(row)
        if e:
            return e.get("decision", "?")
    return "waiting"


def plan() -> int:
    c, rs = conf(), runs()
    move = c["moves"][len(rs) % len(c["moves"])]
    rows = [r for _, d in rs for r in d.get("rows", [])]
    ruled = [(r, standing(r)) for r in rows]
    decided = [(r, s) for r, s in ruled if s != "waiting"]
    last = decided[-c["propose_level_up_after_stood"]:]
    print(f"level {c['level']}: up to {c['level']} board row(s) this run")
    print(f"today's move: {move['name']} ({len(rs)} run(s) recorded). His words: \"{move['his_words']}\"")
    print(f"if the move finds nothing: {c['fallback']}")
    print("repos: " + ", ".join(c["repos"]))
    print("limits:")
    for l in c["limits"]:
        print(f"  - {l}")
    print(f"rows so far: {len(rows)}, ruled {len(decided)}, standing {sum(s == 'stands' for _, s in decided)}")
    for r, s in ruled[-10:]:
        print(f"  {r}: {s}")
    n = c["propose_level_up_after_stood"]
    if len(last) == n and all(s == "stands" for _, s in last):
        print(f"PROPOSE: the last {n} ruled rows all stood. Put the next level on the board as a position, with "
              "the stood count and the tokens per run from the records; the level changes only by his ruling.")
    if decided and decided[-1][1] == "overrule":
        print("PROPOSE: he overruled the latest row. Put on the board whether the session stays at its level or "
              "drops one.")
    return 0


def record(a) -> int:
    day = dt.date.today().isoformat()
    path = LEDGER / f"{day}-daily.json"
    k = 2
    while path.exists():
        path, k = LEDGER / f"{day}-daily-{k}.json", k + 1
    c = conf()
    if a.move not in [m["id"] for m in c["moves"]] + ["research"]:
        print(f"unknown move {a.move}", file=sys.stderr)
        return 1
    rows = [r for r in (a.row or []) if r]
    if len(rows) > c["level"]:
        print(f"{len(rows)} rows is over level {c['level']}'s allowance", file=sys.stderr)
        return 1
    rec = {"id": path.stem, "date": day, "recorded_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
           "project": "six-faces-council", "cause": "daily-move",
           "convened_by": "routine", "invoked_from": "claude-code", "level": c["level"],
           "move": a.move, "found": a.found, "finished": a.finished,
           "branch": a.branch, "pull_request": a.pr, "rows": rows}
    path.write_text(json.dumps({k: v for k, v in rec.items() if v not in (None, "")}, indent=1, ensure_ascii=False) + "\n")
    print(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path)
    return 0


def usage(a) -> int:
    p = Path(a.file)
    d = json.loads(p.read_text())
    d["usage"] = {"session": a.session, "input_tokens": a.input, "output_tokens": a.output, "cost_usd": a.cost}
    p.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n")
    print(f"{p.name}: {a.input + a.output} tokens, ${a.cost}")
    return 0


def main(argv: list[str]) -> int:
    if not argv:
        return plan()
    ap = argparse.ArgumentParser(prog="daily.py")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("record")
    r.add_argument("--move", required=True)
    r.add_argument("--found", required=True)
    r.add_argument("--finished", required=True)
    r.add_argument("--branch")
    r.add_argument("--pr")
    r.add_argument("--row", action="append")
    u = sub.add_parser("usage")
    u.add_argument("file")
    u.add_argument("--session", required=True)
    u.add_argument("--input", type=int, required=True)
    u.add_argument("--output", type=int, required=True)
    u.add_argument("--cost", type=float, required=True)
    a = ap.parse_args(argv)
    return record(a) if a.cmd == "record" else usage(a)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
