# Move nature (what a move is, across surfaces)

ontology: game_design

- 2026-10-19: Wendell overruled `cc-move-sets-element` and asked for an audit of moves across surfaces. Audit:
  `council/research/2026-10-19-move-audit.md`. Pass `move-nature1`: six `mn-*` positions, questions `mn-q-what-move-is`,
  `mn-q-ke-state`, `mn-q-face-daemon` (rows `council/callsheets/rows/move-nature-2026-10-19.json`).

## Next
1. Land the rows on the board (`board/sync_board.py --live <saved page> --rows council/callsheets/rows/move-nature-2026-10-19.json --push`), Sonnet.
2. bars-engine fix for `mn-checkin-fix`: DailyCheckInQuest.tsx:13-18 reads the cycle tables from a client-safe module
   shared with wuxing.ts instead of its own wrong copy. Sonnet, small PR; it does not wait on the questions.
3. After his answers to the three questions: one move table (fifteen rows, the state change per family) in this repo,
   read by bars-engine and sprout under a lockstep test; the Temper Action play test (pass, Tests) ends in one cell on
   all surfaces. Opus thread. The crafting ember follows `mn-ember-both` until then.
