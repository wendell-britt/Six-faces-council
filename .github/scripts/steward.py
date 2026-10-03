#!/usr/bin/env python3
"""Keep every open pull request mergeable with main.

Runs in the steward workflow (.github/workflows/steward.yml). For each open pull request whose branch
lives in this repo:
1. If main has moved ahead, merge main into the branch with a merge commit (never a rebase), using the
   merge drivers in .gitattributes, rebuild the board page if the repo has one, and push.
2. Run the checks and post the result as the "steward" commit status on the branch head.
Merging into main stays with Wendell. If main cannot be merged in cleanly, the branch is left untouched
and the pull request gets one comment naming the files, for the session that owns the branch to resolve.
"""
import json
import os
import subprocess
import sys

REPO = os.environ["GITHUB_REPOSITORY"]
CONFLICT_MARK = "<!-- steward:conflict -->"


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


def tend(pr):
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
            return
        if os.path.exists("board/build_board.py"):
            sh("python3", "board/build_board.py")
            sh("git", "add", "board/council-board.html")
            sh("git", "commit", "-q", "--amend", "--no-edit")
        if sh("git", "push", "-q", "origin", f"HEAD:{head}", check=False).returncode:
            print(f"#{pr['number']}: branch moved while merging; the next run picks it up")
            return
        print(f"#{pr['number']}: merged main into {head}")
    problems = checks()
    set_status(sh("git", "rev-parse", "HEAD").stdout.strip(), problems)
    print(f"#{pr['number']}: {'; '.join(problems) or 'checks pass'}")


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
    prs = gh_json("pr", "list", "--state", "open", "--json", "number,headRefName,headRefOid,isCrossRepository")
    for pr in sorted(prs, key=lambda p: p["number"]):
        if pr["isCrossRepository"]:
            continue
        try:
            tend(pr)
        except RuntimeError as e:
            print(f"#{pr['number']}: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
