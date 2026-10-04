#!/usr/bin/env python3
"""Bring the board's rows onto main in one step, so no row is stranded on a branch or only on the live page.

Wendell, 2026-10-04: "make sure we're automatically merging when we add rows. Or at the least we need a
remediation path that gives us that ability". Two things had gone wrong the same day: board rows sat on a branch
(council/root-game-cloth-board-rows) that main never took, and the live page held rows and a template change
that main did not have, because sessions published from branches. A rebuild from main would have dropped both.

What it does, from the home repo root, on main:
1. Fetches origin/main and fast-forwards to it (stops if the work tree has changes of its own).
2. Reads the live page's data and template from a saved copy of the live board (the Artifact tool's read action
   saves the full page; pass that file with --live). Rows only on the live page are added to main; a row on both
   with different content takes the live version, which was published later; no row is ever removed. `updated`
   takes the later date. The template is compared, and --take-live-template writes the live one.
3. Adds the rows in --rows (a JSON file shaped like board_data.json, with any of positions, questions, terms,
   causes, and resolved). A new row whose id already exists with different content stops the run.
4. Rebuilds council-board.html, commits, and with --push pushes to main, merging again if main moved.
Then publish board/council-board.html to the board URL.

Usage: python3 board/sync_board.py --live <saved live page> [--rows rows.json] [--take-live-template] [--push] [-m message]
       python3 board/sync_board.py --check --live <saved live page>   (report only, writes nothing)
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA = HERE / "board_data.json"
TEMPLATE = HERE / "template.html"
TAG = '<script id="board-data" type="application/json">'
LISTS = ("positions", "questions", "terms", "causes", "battles")
LATER = ("updated", "steer_recorded_through")


def git(*a, check=True):
    r = subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)
    if check and r.returncode:
        sys.exit(f"git {' '.join(a)} failed: {r.stderr.strip()}")
    return r


def read_live(path):
    s = Path(path).read_text(encoding="utf-8")
    i = s.find("<title>Council Board</title>")
    if i < 0:
        sys.exit(f"{path} is not a saved Council Board page")
    body = s[i:]
    a = body.index(TAG) + len(TAG)
    b = body.index("</script>", a)
    data = json.loads(body[a:b])
    template = body[:a] + "__DATA__" + body[b:]
    template = template.rstrip()
    if template.endswith("</body></html>"):
        template = template[: -len("</body></html>")].rstrip()
    return data, template + "\n"


def merge_battle(base, other):
    """A battle grows by rounds. Keep every round either side has, by its number; where both have a round, the
    other side's copy wins. Fields other than rounds take the other side's value. On 2026-10-04 a live page that
    was one publish behind replaced main's copy of fr-ranks-and-badges whole, and round 2 vanished from the board."""
    out = json.loads(json.dumps(base))
    rounds = {r.get("n"): r for r in out.get("rounds", [])}
    for r in other.get("rounds", []):
        rounds[r.get("n")] = r
    for k, v in other.items():
        if k != "rounds":
            out[k] = v
    out["rounds"] = [rounds[n] for n in sorted(rounds, key=lambda n: (n is None, n))]
    return out


def union(main, live, report, path="$"):
    """Main plus everything on live: live's version wins where both have a row, nothing is removed."""
    out = json.loads(json.dumps(main))
    for k, v in live.items():
        if k in LATER and isinstance(v, str) and isinstance(out.get(k), str):
            out[k] = max(out[k], v)
        elif k in LISTS and isinstance(v, list):
            have = {r["id"]: n for n, r in enumerate(out.get(k, [])) if isinstance(r, dict) and "id" in r}
            out.setdefault(k, [])
            for r in v:
                rid = r.get("id") if isinstance(r, dict) else None
                if rid is None:
                    continue
                if rid not in have:
                    out[k].append(r)
                    report.append(f"from live: {k} {rid} (new)")
                elif out[k][have[rid]] != r:
                    new = merge_battle(out[k][have[rid]], r) if k == "battles" else r
                    if new != out[k][have[rid]]:
                        out[k][have[rid]] = new
                        report.append(f"from live: {k} {rid} (changed)")
        elif isinstance(v, list) and isinstance(out.get(k), list):
            # A list without ids, such as steers_recorded, grows on both sides: keep main's entries and add live's
            # missing ones. On 2026-10-04 the live page's older steers_recorded replaced main's whole and three of
            # Wendell's round 2 steers vanished, as the battle's round 2 had before merge_battle.
            for r in v:
                if r not in out[k]:
                    out[k].append(r)
                    report.append(f"from live: {k} (entry added)")
        elif isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = union(out[k], v, report, f"{path}.{k}") if k != "resolved" else merge_resolved(out[k], v, report)
        elif k not in out:
            out[k] = v
            report.append(f"from live: {k} (new field)")
        elif out[k] != v:
            out[k] = v
            report.append(f"from live: {k} (changed)")
    return out


def merge_resolved(main, live, report):
    out = json.loads(json.dumps(main))
    for kind, rows in live.items():
        tgt = out.setdefault(kind, {})
        for rid, val in rows.items():
            if rid not in tgt:
                report.append(f"from live: resolved {kind} {rid}")
            elif tgt[rid] != val:
                report.append(f"from live: resolved {kind} {rid} (changed)")
            tgt[rid] = val
    return out


def add_rows(data, rows, report):
    for k in LISTS:
        have = {r["id"]: r for r in data.get(k, [])}
        for r in rows.get(k, []):
            if r["id"] in have and k == "battles":
                cur = data[k].index(have[r["id"]])
                new = merge_battle(have[r["id"]], r)
                if new != have[r["id"]]:
                    data[k][cur] = new
                    report.append(f"added: {k} {r['id']} (rounds merged)")
                continue
            if r["id"] in have:
                if have[r["id"]] != r:
                    sys.exit(f"--rows: {k} {r['id']} already exists with different content; change the id or edit it in place")
                continue
            data.setdefault(k, []).append(r)
            report.append(f"added: {k} {r['id']}")
    for kind, vals in rows.get("resolved", {}).items():
        for rid, val in vals.items():
            data.setdefault("resolved", {}).setdefault(kind, {})[rid] = val
            report.append(f"resolved: {kind} {rid} ({val.get('decision')})")
    if "updated" in rows:
        data["updated"] = max(data.get("updated", ""), rows["updated"])


def ids(d):
    return {(k, r["id"]) for k in LISTS for r in d.get(k, []) if isinstance(r, dict) and "id" in r}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", required=True, help="saved copy of the live board page")
    ap.add_argument("--rows", help="JSON file of rows to add")
    ap.add_argument("--take-live-template", action="store_true")
    ap.add_argument("--check", action="store_true", help="report only")
    ap.add_argument("--push", action="store_true")
    ap.add_argument("-m", "--message", default="Board: sync the live page and add rows")
    a = ap.parse_args()

    if not a.check:
        if git("status", "--porcelain", "--", "board", "council/ledger").stdout.strip():
            sys.exit("board/ or council/ledger/ has uncommitted changes; commit or stash them first")
        git("fetch", "-q", "origin", "main")
        if git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip() != "main":
            git("checkout", "-q", "main")
        git("merge", "-q", "--ff-only", "origin/main")

    main_data = json.loads(DATA.read_text(encoding="utf-8"))
    live_data, live_template = read_live(a.live)
    report = []
    data = union(main_data, live_data, report)
    if a.rows:
        add_rows(data, json.loads(Path(a.rows).read_text(encoding="utf-8")), report)
    lost = ids(main_data) - ids(data)
    if lost:
        sys.exit(f"refusing: rows would be lost: {sorted(lost)}")
    same_template = live_template.rstrip() == TEMPLATE.read_text(encoding="utf-8").rstrip()
    print("\n".join(report) or "nothing to bring over")
    print("template: " + ("the same as main's" if same_template else
                          "the live page's differs from main's" + (" (taking the live one)" if a.take_live_template else
                                                                  "; pass --take-live-template to take it, after checking which branch it came from")))
    if a.check:
        return
    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    if a.take_live_template and not same_template:
        TEMPLATE.write_text(live_template, encoding="utf-8")
    subprocess.run([sys.executable, str(HERE / "build_board.py")], cwd=ROOT, check=True)
    git("add", "board", "council/ledger")
    if not git("diff", "--cached", "--quiet", check=False).returncode:
        print("no change to commit")
    else:
        git("commit", "-q", "-m", a.message)
        print("committed on main")
    if a.push:
        for _ in range(3):
            if git("push", "-q", "origin", "main", check=False).returncode == 0:
                print("pushed to main; now publish board/council-board.html to https://claude.ai/artifact/DxyShVS8tmvJym4HAsgnho")
                return
            git("pull", "-q", "--no-rebase", "origin", "main")   # the board merge driver merges rows by id
            subprocess.run([sys.executable, str(HERE / "build_board.py")], cwd=ROOT, check=True)
            git("add", "board/council-board.html")
            git("commit", "-q", "-m", "Board: rebuild after merging main", check=False)
        sys.exit("push to main failed three times; run git pull --no-rebase origin main and push by hand")


if __name__ == "__main__":
    main()
