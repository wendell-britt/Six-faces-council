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

## Board rows reach main automatically (Wendell, 2026-10-04)

His words: "make sure we're automatically merging when we add rows. Or at the least we need a remediation path that
gives us that ability". On 2026-10-04 root-game's cloth rows sat on a branch main never took, and the live page held
rows and a template change main did not have, because sessions published from branches. A rebuild from main would
have dropped them. Two paths now close that:

- **The normal path: `board/sync_board.py`, straight to main.** Save the live page with the Artifact tool's read
  action, then run `python3 board/sync_board.py --live <saved page> --rows <rows.json> --push -m "<message>"`. It
  fast-forwards to origin/main, brings over every row the live page has and main lacks (the live version wins where
  both differ; nothing is removed), adds the new rows and resolved entries, rebuilds the page, commits and pushes to
  main, merging again if main moved. Then publish `board/council-board.html`. `--check` reports without writing. A
  template that differs between the live page and main is reported, and `--take-live-template` takes the live one.
- **The safety net: the steward merges board-only pull requests without the label.** A pull request whose files,
  against main, are only `board/board_data.json`, `board/council-board.html` and `council/ledger/*` merges once its
  checks pass, provided no row on main is removed. Every other pull request still waits for the `automerge` label.

**Remediation**, when the live page and main disagree: run `sync_board.py --check --live <saved page>` to see the
difference, then the same command without `--check` and with `--push` to bring main up to the live page.

## Merging into main: Wendell's label

Wendell ruled on 2026-10-03 ("On your label"): a pull request merges into main when it carries the
`automerge` label, is not a draft, and its steward checks pass. The steward then merges it with a merge
commit and brings the other open branches up to the new main. Adding the label is Wendell's yes.
A session adds it only when he says to merge that pull request, and never on its own judgement.
Without the label, a pull request waits for Wendell to merge it by hand.
