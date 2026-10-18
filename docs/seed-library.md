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
| Comes back | yes, on the spaced ladder (rule 1) | no |

## Rules

1. **A resting seed comes back on a spaced ladder.** Wendell overruled the first rule here (`sl-no-pressure`, "nothing
   brings it back unasked") on 2026-10-16: "We need a mechanics to pull in tasks that are resting and use spaced
   repetition to get it back into the board". The ladder (`sl-resurface-ladder`):
   - It comes back 3 days after it was set aside, then 7, 14, 30 and 60 days after each return, then every 90 days
     for as long as it rests. It never stops coming back and never expires.
   - It shows for its day and the two after (a three-day window), so one skipped morning does not lose it.
   - When it comes back he has three moves: **Draw into today**, **Keep resting**, or **Let go**. Keeping it resting
     climbs one rung from that day. Passing it by climbs one rung from its due day, the same as keeping it. Silence
     never composts it (ontology: `silence_or_inactivity_is_not_automatic_composting`).
   - At most three seeds come back on one day, the longest-due first. Any others wait in their window or climb a
     rung, so a large library cannot flood a morning.
   - Coming back is being seen, which is different from being drawn (`sl-resurface-not-a-draw`). A resurfaced seed
     stays `resting`: out of the day's count and never a carry, until he draws it. The library row itself stays
     closed and shows no count; the seeds that came back show open, apart from it.
2. **Drawing is his decision.** Only he draws a seed back, and only then is it a commitment again (ontology:
   "reactivation requires a new explicit decision"). A drawn seed counts toward the day's five like any commitment.
   It is not a carry, so `carryCount` stays as it was and test T4's carry count is not inflated.
3. **One id.** Drawing moves the same task, with its quest or BAR and its notes, into today, so one id still runs from
   the morning it was named to the thread it reaches (`ttv-one-store`).
4. **The path is kept.** Setting aside, keeping resting and drawing each leave a dated note on the task ("Set aside to
   the seed library on 2026-10-16.", "Kept resting on 2026-10-19; it comes back on 2026-10-26."), so the day it was
   named and the days it rested stay readable. The ladder is read back from these notes, so it needs no new column.
5. **The library lives in bars-engine.** The board shows it read-only through `GET /api/tap-the-vein/seed-library`
   (council token). Drawing, keeping resting and letting go happen in bars-engine.

## Where it is built

bars-engine, branch `claude/seed-library-g3qu9x`:

- status `resting` on `TapTheVeinTask` (a string column, so no migration);
- `restTask`, `drawSeed` and `getSeedLibrary` in `src/actions/tap-the-vein.ts`; letting go from the library is the
  existing compost with `no_reason`;
- "Set aside" on a card's action sheet and a closed "Seed library" row on the day's work view, each seed with "Draw
  into today" and "Let go" (`src/app/tap-the-vein/SeedLibrary.tsx`);
- `GET /api/tap-the-vein/seed-library` for the council;
- pure rules and tests in `src/lib/tap-the-vein/seed-library.ts` (`npm run test:ttv-seed-library`).

## The board's surface

Built 2026-10-16 (Six-faces-council `claude/seed-library-board-4vdnzv`, bars-engine branch of the same name):

- **Seed library panel** on the Morning tab, under the Lenses panel. `council/morning.py` reads
  `GET /api/tap-the-vein/seed-library` (or a saved copy with `--seeds`) into `morning.seeds`. The panel is closed and
  its row shows no count. Each seed shows its text, the day it was named and the day it was set aside, and nothing
  else: no age, no reminder. Drawing and letting go link to Tap the Vein.
- **"Set aside"** beside each sealed intake item that has a task id (bars-engine's seal gives one, `ttv-one-store`).
  It saves `seeds/<taskId>` on board=council (`schema/board-save.schema.json`, collection `seeds`). bars-engine's save
  route rests that task in the same transaction, with the same dated note as the card's button
  (`src/lib/tap-the-vein/board-set-aside.ts`), and stores the save as already recorded, so it never waits for main.
  Only a live task (committed or in progress) can rest; anything else is refused and nothing is saved.
- Only the board served by bars-engine (/board/council) can write to bars-engine. On the claude.ai page the button
  is a link to that board instead.
- Until the next gather, a set-aside made on the board shows in the panel from the board's own store.

## Spaced resurfacing

Built 2026-10-16 (Six-faces-council and bars-engine branch `claude/project-thread-9rf0rk`):

- bars-engine `src/lib/tap-the-vein/seed-library.ts`: the ladder (`RESURFACE_LADDER_DAYS`, `RESURFACE_WINDOW_DAYS`,
  `RESURFACE_PER_DAY`), `resurfacing()` placing a seed on it from its set-aside day and keep days, and
  `toSeedLibrary()` marking today's seeds `resurfaced`. Tests: `npm run test:ttv-seed-library`.
- `keepResting` in `src/actions/tap-the-vein.ts` writes the "Kept resting" note.
- Tap the Vein's day's work view shows "Back from the seed library", open, above the closed library row, each seed
  with Draw into today, Keep resting and Let go (`Resurfaced` in `src/app/tap-the-vein/SeedLibrary.tsx`).
- `GET /api/tap-the-vein/seed-library` adds `restDay`, `rung`, `dueDay` and `resurfaced` to each seed, and the ladder.
- The board: `council/morning.py` carries them and lists today's in `morning.seeds.back`; the Morning tab shows them
  first, open, as "Back from your seed library", each linking to Tap the Vein for the three moves.

## Next

1. **Test SL1, 2026-10-30** (Challenger's form): count set-asides, draws, keeps and let-gos since the build, and which
   rung each draw came from. Drawn seeds mean the library is used; draws at the low rungs mean the ladder's first
   steps are right. A library that only grows is reported on the board as an observation, with no automatic action
   on the seeds.
2. **Keep resting from the board.** Today the board links to Tap the Vein for the three moves. A `seeds/<taskId>` save
   with a keep action would need a save-schema change in both repos (CLAUDE.md, "The Nonprofit Board's saves"); build
   it if SL1 shows he works the resurfaced seeds from the board.
