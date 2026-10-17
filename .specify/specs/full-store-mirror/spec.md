# Spec: Full store mirror (universal board access)

## The ask

> "Yes this is the first thing to fix because all environments need to be able to access and interface with that data"
> Wendell, in the Zo chat on the outreach-drafts visibility question, 2026-10-15 (recorded as a chat ruling in
> `council/ledger/2026-10-16-store-visibility-ruling.json`).

**Who it is for:** every session that works the council — Claude sessions, Zo sessions, any agent holding the repo.
**What they feel now, and what should change:** the Outreach tab's contacts and shows (and `lists`, `pickup`) live in
bars-engine's Postgres but never reach main, so only the environments that ran the migration can see them. A Zo session
reading `board_data.json` on main finds no contacts at all. The change: the store reaches main whole, and any
environment reads the whole board from git.

## Purpose

Extend the board-pull pipeline (built 2026-10-16: saves land in bars-engine Postgres, pulled by token every 15 minutes,
no AI) so that every collection in the schema reaches main. After it, a session in any environment can read a contact
on the Outreach tab from main and draft against it — the precondition the outreach-drafts spec names.

## What exists (ground truth, verified 2026-10-16)

- `schema/board-save.schema.json` accepts collections: `positions, questions, terms, causes, steer, steps, blockers,
  picks, morning, ttv, lists, contacts, shows, pickup`.
- `board/fetch_store.py` fetches only `STORE_DIRS = positions, questions, terms, causes, steer, steps, blockers,
  picks, morning, ttv` — `contacts, shows, lists, pickup` are dropped at the fetch step.
- bars-engine `src/lib/board/save.ts` says the same: a save to contacts, shows, lists or pickup is "board state only",
  not recorded to main.
- `.github/workflows/board-pull.yml` runs the three-line flow every 15 minutes with no AI: fetch → `pull.py --push
  --no-room` → ack, plus staleness (6 hours) and the needs-work report.
- No `BOARD_PULL_TOKEN` is set in the Zo environment; a Zo session can read main but cannot run the fetch flow.

## User stories

### Universal read

**As any session**, I want the whole store on main, so that I can read a contact, its shows and its chase state from
git without claude.ai, a vendor tool, or a token.
**Acceptance:** after a board-pull run, `board_data.json` on main carries the contacts and shows the Outreach tab
shows, and a session with only the repo can draft against a named contact.

### Token access by hand

**As Wendell**, I want any agent with `BOARD_PULL_TOKEN` to run the three lines by hand, so a stalled run can be
recovered from anywhere.
**Acceptance:** `BOARD_PULL_TOKEN` is set as a Zo secret; a Zo session runs fetch → pull → ack and reports what it
recorded, with the same accounting the scheduled run gives.

### Staleness covers the new collections

**As Wendell**, I want the 6-hour staleness check to treat a waiting contact or show save like any other save, so the
run goes red when the pipeline drops one.
**Acceptance:** `board/staleness.py` counts the new collections.

## Design decisions (for the pass)

| Question | Options | Leaning |
|---|---|---|
| Where contacts/shows/lists/pickup land on main | New top-level keys in `board_data.json` (merged by the boardjson driver, same shape family as positions) vs committed `store/` files | Keys in `board_data.json`; the pass decides |
| Does the main council board page now read its data from bars-engine the way the Nonprofit Board does, and is republishing `council-board.html` still a Claude-only action | Verify at plan stage against `docs/failure-modes.md` and the page's save path | Do not assume either way |
| The outreach draft's home | A `draft` block on the contact row in `board_data.json` vs a separate `drafts` list keyed by contact id | Plan stage, after the pass rules on the shape above |

## Contracts

- `board/fetch_store.py`: `STORE_DIRS` gains `contacts, shows, lists, pickup`; the accounting statuses apply to them
  unchanged (every save accounted for before ack — Wendell, 2026-10-15).
- bars-engine `src/lib/board/save.ts`: the "board state only" comment and any code path that excludes the four
  collections change in the same pair of pull requests, with both contract test suites green
  (`tests/test_save_contract.py` and bars-engine's `board-save-contract.test.ts`).
- Write path stands: saves are Wendell's, on the board. Sessions add rows through `board/sync_board.py`. Nothing in
  this spec gives a session a direct write to the store (pull, not push, stands — 2026-10-07).

## Out of scope

- Session writes direct to the store.
- The Event Pipeline page (the Challenger's dissent on outreach-on-board stands).
- Draft send execution — that is the outreach-drafts spec, unblocked by this one.

## Falsify

The cheap test: run `python3 board/fetch_store.py fetch <dir>` after the change and confirm `contacts/*.json` and
`shows/*.json` files appear; then, from a session that has never touched claude.ai, read one contact from main and
state its shows. If the pull run records no contacts or the read needs a token or a vendor tool, the design is wrong.
