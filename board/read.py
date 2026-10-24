#!/usr/bin/env python3
"""One step of a board read: record the saves, list what is due, say whether to republish.

Wendell, 2026-10-08, on board-read-slim: the 00:25 board read took 30 steps, and every step rereads a session that
opens at about 102,000 tokens ($1.54, 2.66M tokens reread). The judgment in a board read is small; the rest is
plumbing. This script does the plumbing, so a read is about five steps:

  1. One message with seven parallel ArtifactData `list` calls on https://claude.ai/artifact/DxyShVS8tmvJym4HAsgnho,
     collections positions, questions, terms, causes, steer, steps (step notes live there, 2026-10-12), blockers, picks,
     morning; query {"limit": 1000}; the same out_dir <dir> on each. blockers (the overdue card's blocker panel,
     2026-10-12) may be left out; pull.py then skips it. picks holds his morning picks and morning the menu he
     pasted (docs/morning.md).
     The store goes to files in <dir>. Never read it into the conversation, and never read the page itself.
  2. python3 board/read.py <dir>        # (--dry reports without writing)
     # pull.py --push, due.py --ahead 7, and a verdict, all in one command
  3. If the last line says REPUBLISH, one Artifact call on board/council-board.html, no capabilities passed.
  4. Act on the "needs work" list the script printed, if any. Each piece of work is its own thread.
  5. One reply: what changed, new board rows with the link, no question.

Run it from the repo root. It prints a short report, never the store. Output stays under about forty lines.
<<<<<<< HEAD

No Claude tools (2026-10-21): every save reaches main through the board-pull Action every 15 minutes, so a session
with no ArtifactData (Codex, Freebuff, a plain clone) reads the board off main instead:

  python3 board/read.py --main-only

It prints how far main is ahead of this clone, when main last recorded a pull, the open needs-work count and what is
due, and says whether the page needs anything from this session (it does not: bars-engine's /board/council serves
board/council-board.html from main). docs/pickup-here.md is the map.
"""
import json
=======
"""
>>>>>>> 8503a0a (Merge main into claude/project-thread-231s0p (steward))
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
NEED = ("positions", "questions", "terms", "causes", "steer", "steps")
OPTIONAL = ("blockers",)  # newer than the pickup routine's prompt, so a read that skips it still runs


def run(*cmd):
    r = subprocess.run([sys.executable, *cmd], cwd=ROOT, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()


<<<<<<< HEAD
def git_out(*cmd):
    r = subprocess.run(["git", *cmd], cwd=ROOT, capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ""


def last_pull():
    """The newest save main has recorded, from the pull ledger's file names, and the date it landed."""
    ledgers = sorted((ROOT / "council" / "ledger").glob("*-pull-*.json"))
    if not ledgers:
        return "", ""
    newest = ledgers[-1]
    stamp = newest.stem.replace("-pull-", "T")  # 2026-10-21-pull-175259 -> 2026-10-21T175259
    return stamp, stamp[11:13] + ":" + stamp[13:15] + " UTC"


def main_only():
    """A board read for a session with no ArtifactData: main is the record, so read main."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("needs_work", HERE / "needs_work.py")
    work = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(work)

    branch = git_out("rev-parse", "--abbrev-ref", "HEAD")
    head = git_out("rev-parse", "--short", "HEAD")
    fetched = subprocess.run(["git", "fetch", "-q", "origin", "main"], cwd=ROOT, capture_output=True)
    behind = git_out("rev-list", "--count", "HEAD..FETCH_HEAD") if fetched.returncode == 0 else ""
    print(f"clone: {branch} {head}" + (f", {behind} commits behind origin/main: git pull first" if behind and behind != "0"
                                       else ", up to date with origin/main" if behind == "0"
                                       else ", origin/main not reached; the record below is this clone's"))

    stamp, clock = last_pull()
    data = json.loads((HERE / "board_data.json").read_text(encoding="utf-8"))
    print(f"main's board record: updated {data.get('updated', '')}" + (f", last pull {stamp[:10]} {clock}" if stamp else ""))

    open_items = work.items()
    oldest = open_items[0]["key"].split("#")[0] if open_items else ""
    print(f"needs work: {len(open_items)} open" + (f", oldest from {oldest}" if oldest else "")
          + " -- python3 board/needs_work.py names each one")
    code, due = run(str(ROOT / "council" / "due.py"), "--ahead", "7")
    print(f"due: {due}")
    print("saves: the board-pull Action records both boards onto main every 15 minutes; a save newer than the last "
          "pull is not here yet (BOARD_PULL_TOKEN would fetch it now: python3 board/fetch_store.py fetch <dir>)")
    print("BOARD: nothing to republish from here; bars-engine's /board/council serves board/council-board.html from main. "
          "The claude.ai artifact keeps its own published copy, and its steps and contacts live only in its store, so a "
          "row landed from here shows on /board/council until a session with the Artifact tool republishes.")


def main():
    if sys.argv[1:] == ["--main-only"]:
        main_only()
        return
=======
def main():
>>>>>>> 8503a0a (Merge main into claude/project-thread-231s0p (steward))
    args = [a for a in sys.argv[1:] if a != "--dry"]
    dry = len(args) != len(sys.argv) - 1
    if len(args) != 1:
        sys.exit(__doc__)
    store = Path(args[0])
    missing = [k for k in NEED if not (store / k).is_dir()]
    if missing:
        sys.exit(f"{store} lacks {', '.join(missing)}; list those collections with ArtifactData into this folder first")
    counts = ", ".join(f"{k} {len(list((store / k).glob('*.json')))}" for k in (*NEED, *OPTIONAL, "picks", "morning") if (store / k).is_dir())
    print(f"store: {counts}")

    code, out = run(str(HERE / "pull.py"), str(store), *([] if dry else ["--push"]))
    print(out)
    if code:
        sys.exit("pull.py failed; fix the line above before anything else")
    code, due = run(str(ROOT / "council" / "due.py"), "--ahead", "7")
    print(f"due: {due}")

    if dry:
        print("REPUBLISH: dry run, nothing written")
    elif "pushed to main" in out:
        print("REPUBLISH: board/council-board.html changed; publish it to the board URL without capabilities")
    elif "no change to commit" in out:
        print("REPUBLISH: no, nothing changed on main")
    else:
        print("REPUBLISH: no, every saved answer was already recorded")


if __name__ == "__main__":
    main()
