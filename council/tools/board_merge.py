#!/usr/bin/env python3
"""Git merge driver for board/board_data.json.

Every session adds rows to the end of the same lists, so a line merge conflicts whenever two branches
both touch the board. This merges by meaning instead: lists of rows merge by "id", objects merge by key,
and a row only conflicts when both sides changed the same field to different values. Rows keep the
order of the other branch (usually main), and this branch's new rows follow them. When both sides
changed a date stamp ("updated", "steer_recorded_through"), the later one wins: a choice, since a
later stamp covers both sides' rows.

Git calls it as: board_merge.py %O %A %B  (base, ours, theirs). The result is written to %A.
Exit 0 is a clean merge; exit 1 leaves %A as ours and lists the conflicting fields on stderr.
Set up with: git config merge.boardjson.driver "python3 council/tools/board_merge.py %O %A %B"
"""
import json
import sys

MISSING = object()
LATER_WINS = {"updated", "steer_recorded_through"}


def key(row):
    if isinstance(row, dict) and "id" in row:
        return ("id", row["id"])
    return ("value", json.dumps(row, sort_keys=True))


def merge(base, ours, theirs, path, conflicts):
    if ours == theirs:
        return ours
    if base == ours:
        return theirs
    if base == theirs:
        return ours
    if isinstance(ours, dict) and isinstance(theirs, dict):
        base = base if isinstance(base, dict) else {}
        out = {}
        for k in list(theirs) + [k for k in ours if k not in theirs]:
            r = merge(base.get(k, MISSING), ours.get(k, MISSING), theirs.get(k, MISSING), f"{path}.{k}", conflicts)
            if r is not MISSING:
                out[k] = r
        return out
    if isinstance(ours, list) and isinstance(theirs, list):
        base = base if isinstance(base, list) else []
        bm = {key(x): x for x in base}
        om = {key(x): x for x in ours}
        tm = {key(x): x for x in theirs}
        order = [key(x) for x in theirs] + [key(x) for x in ours if key(x) not in tm]
        out = []
        for k in order:
            r = merge(bm.get(k, MISSING), om.get(k, MISSING), tm.get(k, MISSING), f"{path}[{k[1]}]", conflicts)
            if r is not MISSING:
                out.append(r)
        return out
    name = path.rsplit(".", 1)[-1]
    if name in LATER_WINS and isinstance(ours, str) and isinstance(theirs, str):
        return max(ours, theirs)
    conflicts.append(path)
    return ours


def main():
    base_path, ours_path, theirs_path = sys.argv[1:4]
    try:
        base, ours, theirs = (json.load(open(p, encoding="utf-8")) for p in (base_path, ours_path, theirs_path))
    except (OSError, ValueError) as e:
        print(f"board_merge: cannot parse a side ({e}); falling back to a conflict", file=sys.stderr)
        return 1
    conflicts = []
    result = merge(base, ours, theirs, "$", conflicts)
    if conflicts:
        print("board_merge: both sides changed " + ", ".join(conflicts), file=sys.stderr)
        return 1
    with open(ours_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=1)
        f.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
