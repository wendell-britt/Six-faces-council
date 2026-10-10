#!/usr/bin/env python3
"""One step of a board read: record the saves, list what is due, say whether to republish.

Wendell, 2026-10-08, on board-read-slim: the 00:25 board read took 30 steps, and every step rereads a session that
opens at about 102,000 tokens ($1.54, 2.66M tokens reread). The judgment in a board read is small; the rest is
plumbing. This script does the plumbing, so a read is about five steps:

  1. One message with seven parallel ArtifactData `list` calls on https://claude.ai/artifact/DxyShVS8tmvJym4HAsgnho,
     collections positions, questions, terms, causes, steer, picks, morning; query {"limit": 1000}; the same out_dir
     <dir> on each. picks holds his morning picks and morning the menu he pasted (docs/morning.md).
     The store goes to files in <dir>. Never read it into the conversation, and never read the page itself.
  2. python3 board/read.py <dir>        # (--dry reports without writing)
     # pull.py --push, due.py --ahead 7, and a verdict, all in one command
  3. If the last line says REPUBLISH, one Artifact call on board/council-board.html, no capabilities passed.
  4. Act on the "needs work" list the script printed, if any. Each piece of work is its own thread.
  5. One reply: what changed, new board rows with the link, no question.

Run it from the repo root. It prints a short report, never the store. Output stays under about forty lines.
"""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
NEED = ("positions", "questions", "terms", "causes", "steer")


def run(*cmd):
    r = subprocess.run([sys.executable, *cmd], cwd=ROOT, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()


def main():
    args = [a for a in sys.argv[1:] if a != "--dry"]
    dry = len(args) != len(sys.argv) - 1
    if len(args) != 1:
        sys.exit(__doc__)
    store = Path(args[0])
    missing = [k for k in NEED if not (store / k).is_dir()]
    if missing:
        sys.exit(f"{store} lacks {', '.join(missing)}; list those collections with ArtifactData into this folder first")
    counts = ", ".join(f"{k} {len(list((store / k).glob('*.json')))}" for k in (*NEED, "picks", "morning") if (store / k).is_dir())
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
