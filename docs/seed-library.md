# The seed library

Wendell, 2026-10-16, on board position `ttv-fruit-is-his` (board read 1759): "We should also be able to defer those
into a seed library that can be drawn from"

A design thread built this (call sheet `council/callsheets/morning-menu.md`, Next item 2). It is not a full six-face
pass; the positions below stand on the board unless he flips them.

## What it is

Any live commitment (committed or in progress) can be **set aside**. It goes to his seed library and rests there
until he **draws** it back into a day or **lets it go**.

In the design ontology this is the `resting` work disposition (`ontology/v0.1/source/design-ontology-v0.1.yaml`,
`work_dispositions`), which sits apart from `composted`:

| | Set aside (resting) | Let go (composted) |
|---|---|---|
| Still his to pick up | yes, by drawing it | no; picking it up again is a new commitment |
| Owes anything | nothing while it rests | nothing ever ("does not owe the garden a harvest") |
| Reason asked | none | none ("Just let it go" comes first) |

## Rules

1. **No pressure while it rests.** A resting task is out of the day's count, never carried, never counted as unfinished,
   and nothing brings it back unasked: no reminder, no expiry, no nudge. The library opens only when he opens it, and
   its closed row shows no count. Silence is not composting either: a seed rests until he decides
   (ontology: `silence_or_inactivity_is_not_automatic_composting`, `no_hidden_active_backlog`).
2. **Drawing is his decision.** Only he draws a seed back, and only then is it a commitment again (ontology:
   "reactivation requires a new explicit decision"). A drawn seed counts toward the day's five like any commitment.
   It is not a carry, so `carryCount` stays as it was and test T4's carry count is not inflated.
3. **One id.** Drawing moves the same task, with its quest or BAR and its notes, into today, so one id still runs from
   the morning it was named to the thread it reaches (`ttv-one-store`).
4. **The path is kept.** Setting aside and drawing each leave a dated note on the task ("Set aside to the seed library
   on 2026-10-16."), so the day it was named and the days it rested stay readable.
5. **The library lives in bars-engine.** The board shows it read-only through `GET /api/tap-the-vein/seed-library`
   (council token). Drawing and letting go happen in bars-engine.

## Where it is built

bars-engine, branch `claude/seed-library-g3qu9x`:

- status `resting` on `TapTheVeinTask` (a string column, so no migration);
- `restTask`, `drawSeed` and `getSeedLibrary` in `src/actions/tap-the-vein.ts`; letting go from the library is the
  existing compost with `no_reason`;
- "Set aside" on a card's action sheet and a closed "Seed library" row on the day's work view, each seed with "Draw
  into today" and "Let go" (`src/app/tap-the-vein/SeedLibrary.tsx`);
- `GET /api/tap-the-vein/seed-library` for the council;
- pure rules and tests in `src/lib/tap-the-vein/seed-library.ts` (`npm run test:ttv-seed-library`).

## Next

1. **The board's surface**, once bars-engine #341 merges (it makes the board's intake items real tasks): a seed library
   panel on the Morning tab read by `council/morning.py` from the export, and "Set aside" beside each intake item, which
   the board writes to bars-engine. A fresh thread on Opus owns it.
2. **Test SL1, 2026-10-30** (Challenger's form): count set-asides, draws and let-gos since the build. Drawn seeds mean
   the library is used. A library that only grows is reported on the board as an observation, with no automatic
   action on the seeds.
