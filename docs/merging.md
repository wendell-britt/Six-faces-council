# Merging

## Why pull requests here conflict

Every pass and board read adds rows to the end of the same lists in `board/board_data.json`, and
`board/council-board.html` holds that whole file on one line. So any two branches that both touch the
board conflict, even when they add different rows. Six-faces-council #9 conflicted this way on
2026-10-03: main had already taken all of its board rows (6ad770b copied them from the live board), and
board reads 20 to 22 then appended their own rows after the same spot.

## What resolves it now

- `council/tools/board_merge.py` is a git merge driver for `board_data.json`. It merges rows by id and
  objects by key, keeps main's order with the branch's new rows after it, and takes the later date for
  `updated`. It stops with a conflict only when both sides changed the same field of the same row.
- `.gitattributes` names the driver, and keeps one side of `council-board.html`, which is then rebuilt
  with `python3 board/build_board.py`.
- `council/hooks/council-sync.sh` sets up both drivers at session start, so a session's own
  `git merge origin/main` resolves board conflicts by itself. Rebuild the page after the merge.

## The steward workflow

`.github/workflows/steward.yml` runs on every push to main, on pull request activity and hourly. For each
open pull request from this repo it merges main into the branch with a merge commit when main has moved
(never a rebase or force push), rebuilds the board page, pushes, runs the checks and posts them as the
`steward` status. If main does not merge cleanly it leaves the branch alone and comments once with the
files, for the owning session to resolve.

A session pushing to a branch the steward has updated gets a rejected push. It runs
`git pull --no-rebase origin <branch>` and pushes again.

Merging into main stays with Wendell.
