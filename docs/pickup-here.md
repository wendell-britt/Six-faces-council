# Picking the board up with no Claude tools

A session in another agent has the repo and nothing else: no ArtifactData, no Send button, no routines. That covers a
board read and landing rows, because his saves reach main by themselves.

This map was written on 2026-10-21 from a Freebuff session on main.

## What reaches main by itself

`.github/workflows/board-pull.yml` runs every 15 minutes with no AI in it. It fetches both boards' saves from
bars-engine (`BOARD=nonprofit`, then `BOARD=council`), records them with `board/pull.py --push --no-room`, gathers a
pasted morning menu, rebuilds the Nonprofit Board, acknowledges every save, and fails the run when a save has waited
more than six hours.

His answers land in `board/board_data.json`. His step ticks, step notes and date moves land in
`council/ledger/*-pull-*.json`, and the needs-work lines sit beside them. On 2026-10-21 main held 74 open needs-work
items and its last pull was 17:56 UTC.

So `git fetch origin main` is a board read.

## The first command

    python3 board/read.py --main-only

It prints the branch and how many commits it is behind `origin/main`, the date of main's board record with its last
pull, the open needs-work count, what is due (`council/due.py --ahead 7`), and a closing line on what the page needs
from this session. It reads main and takes no store folder.

Then pick one piece of work: `council/callsheets/INDEX.md`, the sheet for that strand, and `python3
board/needs_work.py` for what his recorded answers still ask for.

## Landing rows: a question, a position, a battle

    python3 board/sync_board.py --rows rows.json --push

`--live` became optional on 2026-10-21. A rows file alone adds the rows onto main, rebuilds `council-board.html` with
`build_board.py`, and the run still refuses if a row on main would disappear. A run was checked this way on
2026-10-21: the row reached `board_data.json`, the rebuilt page carried it, and the commit landed on main.

bars-engine's [`/board/council`](https://bars-engine.vercel.app/board/council) serves that page from main within its
five-minute cache, behind his own sign-in, so the row shows on a board he reads. From a session with no cookies that
URL answers `307` to `/login`, which is the gate working.

The claude.ai artifact keeps its own published copy, and publishing there takes the Artifact tool. A row landed from
here appears on `/board/council` first and reaches the artifact at the next republish from a Claude session. Name the
board it is on in the reply.

A commit needs an author. Where the platform sets no git identity, pass one for the command or export it for the
session before the first run:

    GIT_AUTHOR_NAME="<agent>" GIT_AUTHOR_EMAIL="<agent@example.com>" \
    GIT_COMMITTER_NAME="<agent>" GIT_COMMITTER_EMAIL="<agent@example.com>" \
    python3 board/sync_board.py --rows rows.json --push

Rows files look like `council/callsheets/rows/*.json`. Run the reach test (`reach_test` in `council/faces.yaml`)
before a question goes in, and let a question the record answers become a position.

## A save newer than the last pull

The record lags by up to fifteen minutes. A session holding `BOARD_PULL_TOKEN` (a fine-grained GitHub token with
Actions read and write, stored as a repository secret) runs the Action's three lines by hand:

    python3 board/fetch_store.py fetch store
    python3 board/pull.py store --push --no-room
    python3 board/fetch_store.py ack store --record "six-faces-council@$(git rev-parse --short HEAD)"

Keep the token in the environment or the platform's secret store. Running pull.py twice records the same saves once.
A session with no token waits for the next Action run.

## What stays with a Claude session

- Saving the live page, republishing the artifact, and the Send button's pickup routine.
- The store's `lists`, `steps`, `contacts` and `shows` documents: Your steps and Outreach. They live in Postgres on
  bars-engine and in the artifact's store, and `board/store_write.py` needs `COUNCIL_MENU_TOKEN`. His step notes that
  did reach main appear through `board/needs_work.py`, and his answered questions arrive as rows.
- `council/morning.py --menu` for a menu pasted on the Morning tab, when the Action skipped it for a missing token.

## The rules hold here too

One session, one piece of work (CLAUDE.md, "Short sessions"). Questions for Wendell go through `sync_board.py` onto
the board, and the reply names the new rows with the link. A finished needs-work item takes the change it asks for
plus one entry in `council/needs-work-done.json`, in the same pull request. Update the strand's callsheet at the end.

The steward merges a ready pull request once its checks pass (`docs/merging.md`), so a branch is enough; a change to
`council/faces.yaml` or a `daily/` branch waits for his label.
