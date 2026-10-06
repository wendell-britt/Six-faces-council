#!/usr/bin/env python3
"""Keep every open pull request mergeable with main, and merge the ready ones once their checks pass.

Runs in the steward workflow (.github/workflows/steward.yml). For each open pull request whose branch
lives in this repo:
1. If main has moved ahead, merge main into the branch with a merge commit (never a rebase), using the
   merge drivers in .gitattributes, rebuild the board page if the repo has one, and push.
2. Run the checks and post the result as the "steward" commit status on the branch head.
3. If the pull request is not a draft and the checks pass, merge it with a merge commit. Wendell, 2026-10-06:
   "having to manually put the label isn't working for me. Is there a way to automate this part of the process?"
   This replaces his label ruling of 2026-10-03 ("On your label"). Two things still stop a merge: the "hold" label,
   which anyone can add to keep a pull request open, and a change Wendell reviews himself: council/faces.yaml, which
   changes only by his ruling, and the daily session's daily/ branches. Those still wait for his "automerge" label. If main cannot be merged in cleanly, the branch is left untouched
and the pull request gets one comment naming the files, for the session that owns the branch to resolve.
"""
import json
import os
import subprocess
import sys

REPO = os.environ["GITHUB_REPOSITORY"]
CONFLICT_MARK = "<!-- steward:conflict -->"
LABEL = "automerge"
HOLD = "hold"
# Files that change only by Wendell's ruling (CLAUDE.md, "Where the rest lives"). A pull request touching one still
# waits for his "automerge" label.
RESERVED = ("council/faces.yaml",)
# Board-only pull requests merge without the label (Wendell, 2026-10-04: "make sure we're automatically merging when we
# add rows"): every changed file is board data or a ledger record, the checks pass, and no row on main is removed.
BOARD_ONLY = ("board/board_data.json", "board/council-board.html")
BOARD_ONLY_PREFIX = ("council/ledger/",)


def sh(*args, check=True):
    r = subprocess.run(args, capture_output=True, text=True)
    if check and r.returncode:
        raise RuntimeError(f"{' '.join(args)} failed: {r.stderr.strip()}")
    return r


def gh_json(*args):
    return json.loads(sh("gh", *args).stdout or "null")


def checks():
    """Return a list of problems; empty means the branch passes."""
    problems = []
    if os.path.exists("board/board_data.json"):
        try:
            json.load(open("board/board_data.json", encoding="utf-8"))
        except ValueError as e:
            problems.append(f"board_data.json does not parse: {e}")
        else:
            page = "board/council-board.html"
            before = open(page, encoding="utf-8").read() if os.path.exists(page) else None
            sh("python3", "board/build_board.py")
            if open(page, encoding="utf-8").read() != before:
                problems.append("council-board.html is not built from board_data.json (run python3 board/build_board.py)")
            sh("git", "checkout", "--", page, check=False)
    try:
        import yaml
        for path in ("council/faces.yaml", "council/pipeline.yaml"):
            if os.path.exists(path):
                try:
                    yaml.safe_load(open(path, encoding="utf-8"))
                except yaml.YAMLError as e:
                    problems.append(f"{path} does not parse: {e}")
    except ImportError:
        pass
    leftover = sh("git", "grep", "-lE", "^(<<<<<<<|>>>>>>>) ", "--", ".", check=False).stdout.split()
    problems += [f"conflict markers left in {p}" for p in leftover]
    # The board merge tests: a change to sync_board.py or board_merge.py that would drop a row fails here.
    if os.path.isdir("tests"):
        r = sh("python3", "-m", "unittest", "discover", "-s", "tests", check=False)
        if r.returncode:
            last = (r.stderr.strip().splitlines() or ["unknown failure"])[-1]
            problems.append(f"tests fail (python3 -m unittest discover -s tests): {last}")
    return problems


def set_status(sha, problems):
    state = "failure" if problems else "success"
    desc = (problems[0] if problems else "up to date with main, checks pass")[:140]
    sh("gh", "api", f"repos/{REPO}/statuses/{sha}", "-f", f"state={state}", "-f", "context=steward", "-f", f"description={desc}")


def note_conflict(number, files):
    comments = gh_json("api", f"repos/{REPO}/issues/{number}/comments", "--paginate")
    if any(CONFLICT_MARK in (c.get("body") or "") for c in comments):
        return
    body = (f"{CONFLICT_MARK}\nThe steward could not merge main into this branch. These files changed on both sides: "
            + ", ".join(f"`{f}`" for f in files)
            + ". The session that owns this branch should merge main, resolve them, and push.")
    sh("gh", "api", f"repos/{REPO}/issues/{number}/comments", "-f", f"body={body}")


def board_only():
    """True when the branch, against main, changes only board data and ledger records and removes no board row."""
    files = sh("git", "diff", "--name-only", "origin/main...HEAD").stdout.split()
    if not files or not all(f in BOARD_ONLY or f.startswith(BOARD_ONLY_PREFIX) for f in files):
        return False
    def ids(text):
        d = json.loads(text)
        return {(k, r["id"]) for k in ("positions", "questions", "terms", "causes") for r in d.get(k, []) if isinstance(r, dict) and "id" in r}
    main_rows = sh("git", "show", "origin/main:board/board_data.json", check=False).stdout
    if not main_rows:
        return True
    try:
        return ids(main_rows) <= ids(open("board/board_data.json", encoding="utf-8").read())
    except (ValueError, OSError):
        return False


def touches_reserved():
    files = sh("git", "diff", "--name-only", "origin/main...HEAD").stdout.split()
    return [f for f in files if f in RESERVED]


def tend(pr):
    """Bring one pull request up to date, check it, and merge it if it is ready. Returns True if merged."""
    head = pr["headRefName"]
    sh("git", "fetch", "-q", "origin", "main", head)
    sh("git", "checkout", "-q", "-B", "steward-work", f"origin/{head}")
    if sh("git", "merge-base", "--is-ancestor", "origin/main", "HEAD", check=False).returncode:
        r = sh("git", "merge", "--no-edit", "-m", f"Merge main into {head} (steward)", "origin/main", check=False)
        if r.returncode:
            files = sh("git", "diff", "--name-only", "--diff-filter=U").stdout.split()
            if not files:
                print(f"#{pr['number']}: merge failed: {r.stderr.strip() or r.stdout.strip()}", file=sys.stderr)
            sh("git", "merge", "--abort", check=False)
            print(f"#{pr['number']}: conflict in {files}")
            note_conflict(pr["number"], files or ["(unknown)"])
            set_status(pr["headRefOid"], [f"main does not merge cleanly: {', '.join(files)}"])
            return False
        if os.path.exists("board/build_board.py"):
            sh("python3", "board/build_board.py")
            sh("git", "add", "board/council-board.html")
            sh("git", "commit", "-q", "--amend", "--no-edit")
        if sh("git", "push", "-q", "origin", f"HEAD:{head}", check=False).returncode:
            print(f"#{pr['number']}: branch moved while merging; the next run picks it up")
            return False
        print(f"#{pr['number']}: merged main into {head}")
    sha = sh("git", "rev-parse", "HEAD").stdout.strip()
    problems = checks()
    set_status(sha, problems)
    print(f"#{pr['number']}: {'; '.join(problems) or 'checks pass'}")
    labels = {l["name"] for l in pr["labels"]}
    reserved = touches_reserved()
    if reserved and LABEL not in labels:
        print(f"#{pr['number']}: changes {', '.join(reserved)}; waits for Wendell's {LABEL} label")
    # The daily session's pull requests keep waiting for his label: its limits (fm-limits, stood at board read 25)
    # say its changes are proposals he reviews.
    daily = head.startswith("daily/")
    ready = HOLD not in labels and (LABEL in labels or ((not reserved and not daily) or board_only()))
    if ready and not pr["isDraft"] and not problems:
        r = sh("gh", "pr", "merge", str(pr["number"]), "--merge", "--match-head-commit", sha, check=False)
        if r.returncode == 0:
            print(f"#{pr['number']}: merged into main")
            return True
        print(f"#{pr['number']}: merge refused: {r.stderr.strip()}")
    return False


def main():
    sh("git", "config", "user.name", "github-actions[bot]")
    sh("git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
    # Branches cut before the driver existed lack it, so run main's copy from outside the work tree.
    driver = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "board_merge.py")
    if os.path.exists("council/tools/board_merge.py"):
        sh("cp", "council/tools/board_merge.py", driver)
        sh("git", "config", "merge.boardjson.driver", f"python3 {driver} %O %A %B")
    # Attributes come from the work tree, which is the pull request's branch, so pin main's copy.
    if os.path.exists(".gitattributes"):
        sh("cp", ".gitattributes", os.path.join(sh("git", "rev-parse", "--git-dir").stdout.strip(), "info", "attributes"))
    sh("git", "config", "merge.ours.driver", "true")
    sh("gh", "label", "create", LABEL, "--color", "0e8a16", "--force",
       "--description", "Wendell's yes, needed only for a change to council/faces.yaml", check=False)
    sh("gh", "label", "create", HOLD, "--color", "b60205", "--force",
       "--description", "Keeps this pull request open: the steward does not merge it", check=False)
    # A merge moves main, and a push or merge made by this workflow starts no new run, so after each
    # merge go round again to bring the other branches up to the new main.
    for _ in range(10):
        prs = gh_json("pr", "list", "--state", "open", "--json", "number,headRefName,headRefOid,isDraft,labels,isCrossRepository")
        merged = False
        for pr in sorted(prs, key=lambda p: p["number"]):
            if pr["isCrossRepository"]:
                continue
            try:
                if tend(pr):
                    merged = True
                    break
            except RuntimeError as e:
                print(f"#{pr['number']}: {e}", file=sys.stderr)
        if not merged:
            return


if __name__ == "__main__":
    main()
