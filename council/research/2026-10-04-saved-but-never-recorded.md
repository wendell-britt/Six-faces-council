# Saved on the board, never recorded on main

Daily run, 2026-10-04, move Open up. His words: "find out what's been abandoned in the larger work corpus".

## What I looked at

- The live board's saved answers: ArtifactData, collection `positions`, on the Council Board
  (https://claude.ai/artifact/DxyShVS8tmvJym4HAsgnho). It holds 181 saved positions.
- `board/board_data.json` on main at c82689c: 209 positions, of which 25 have no resolved entry.
- Every unmerged branch and every pull request in wendell-britt/six-faces-council.
- The ledger records written since 2026-10-03.

## The finding

Wendell saved an answer on 23 positions that main still shows as open. No ledger record and no resolved entry
carries those answers. Two of them are positions for pull requests, and both pull requests are still open.

### Seven rows of this repo, saved yesterday

| Row | His save | What it should have done |
|---|---|---|
| `dy-limit-wording` | stands, 2026-10-03 20:54 UTC | Merge pull request #20, still open |
| `dy-research-handoff` | stands, 20:54 | Record only |
| `cost-quiet-wakes` | stands, 23:39 | Record only |
| `cost-daily-script` | stands, 23:39 | Record only |
| `cost-per-row` | stands, 23:39 | Record only |
| `cost-short-rule` | stands, 23:40 | Merge pull request #24, still open |
| `daemon-reports-saved` | stands, 23:40 | Record only |

Each row says it takes effect at the next board read. Pull request #20's row reads: "merges at your next board
read unless you flip it". The save shows `{"status": "stands", "steer": ""}`.

`council/ledger/2026-10-03-board-read-29.json` was committed at 23:37 UTC and records one question,
`cost-session-shape`. The five saves from 23:39 to 23:40 came two minutes after it. The next record in this repo,
`2026-10-03-daily-wake-ruling.json` at 23:43, was written by this session and records only
`dy-2026-10-03-wake`. That session did not read the saves, and no session has read them since.

### Thirteen rows of other projects, saved and not recorded on this board

- The Guide (Art of War artifact): `gn-verify`, `gn-rule17`, `gn-hold-template`, `gn-ke-notes`, all "stands",
  2026-10-03 02:08 UTC, the oldest saves on this list.
- Sprout: `sm-hearing-exposes-bond` (2026-10-03 20:09) and `tr-builder-not-layers` (2026-10-04 13:28), "stands".
- Jev: `jev-select-only`, `jev-fallback`, `jev-candidates-only`, `jev-reserved`, `jev-no-player-text`,
  `jev-spec-first`, all "stands", 2026-10-03 23:40.
- Root-game: `rg-stance-by-move`, "stands", 2026-10-04 03:44.

Records for these projects may live in their own repos, as the council's rule says ("They stay in the repo whose
decision they record"). This run can reach only the home repo, so it could not check them. Either way, this
board's resolved list does not show these answers, and the board still lists the rows as open.

### Three rows in a battle that is still going

`pr-branch-emphasis` (overruled, with a steer), `pr-design-text` and `pr-units-mapping` were saved between 14:20
and 14:21 UTC today through `battle:fr-ranks-and-badges`. The commit after them, c82689c at 14:49, starts round
5 of that battle. That session is still working, so these three are not abandoned. They are listed here so the
count adds up.

### Branches checked and found landed

Six branches still have commits that main lacks by commit id, but their work is on main: the census and its fix,
the retire command, the editorial pass, the saved daemon reports and the root-game cloth rows. Each file on them
matches main or has been changed on main since. `claude/board-go-back` is the work of the open pull request #35,
from today.

## Why it matters

He answered, and the answer did not take effect. Pull request #20 is the rule this daily run works under, and it
has been waiting 19 hours on a save he made 5 minutes after the row went up. The board's rule is that the board
is the only place he answers. A save that nobody reads stops it working that way.

## What would finish it

A session that reads the board records the 20 saves outside the live battle and merges #20 and #24. That session
owns the rows, so a daily run must not do it. The new `board/sync_board.py` brings rows from the live page to
main, but it reads the page's data, not the saved answers, so it would not have caught this. A check that
compares saved answers with resolved entries at the start of every board read would.

## Leads not followed

This run followed none outside the repo. The other projects' repos were out of this run's reach.
