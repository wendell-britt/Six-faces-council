# Tasks: Deferred items come back on a spaced schedule, with new context

## Before the build

- [x] [claude] Run the falsification test in spec.md and record the result there. Passed, and found the same-day fault.

## Steps only Wendell can take

He has no steps. His decisions are on the board: question `sd-when`, and positions `sd-intervals`, `sd-review` and `sd-ship`.

## Build

- [x] [claude] `council/due.py`: due items, context brief, next spaced wait, `record`.
- [x] [claude] Board: spaced option, review box, "not re-weighed yet" note.
- [x] [claude] `pipeline.yaml` defer block and both skills.
- [x] [claude] Render a test board in a headless browser: an item due back with no review, one with a review, and one never deferred.

## Verify and ship

- [x] [claude] Definition of done in spec.md, checked.
- [x] [claude] Board position `sd-ship`: merges on the next board read unless flipped. It stood (board read 22).
- [x] [claude] After merge, on main: the oracle drafts' resolved entry gains `history` and `project`.
- [x] [claude] Ledger record written (`council/ledger/2026-10-03-board-read-22.json`); this file ticked.
