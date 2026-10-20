# Move nature (what a move is, across surfaces)

ontology: game_design

- 2026-10-19: Wendell overruled `cc-move-sets-element` and asked for an audit of moves across surfaces. Audit:
  `council/research/2026-10-19-move-audit.md`. Pass `move-nature1`: six `mn-*` positions, questions `mn-q-what-move-is`,
  `mn-q-ke-state`, `mn-q-face-daemon` (rows `council/callsheets/rows/move-nature-2026-10-19.json`).

- 2026-10-19: Answers in (ledger `council/ledger/2026-10-19-pull-225647.json`): both layers, each face and daemon owns
  its moves, ke depends on the start, Transcend in two steps. Built: `schema/move-table.json` with
  `tests/test_move_table.py` (council #310), bars-engine #401 (wuxing reads it; check in CI), sprout #62 (copy, test).
  Temper Action from Anger dissatisfied ends at Fear dissatisfied on all three. Check-in fix is bars-engine #397.
  The three PRs merge together.

## Next
1. Merge council #310, bars-engine #401 and sprout #62 together once checks pass (the copies must match).
2. bars-engine #397 (check-in reads wuxing's tables) merges on its own.
3. Land the four `mt-*` positions on the board (`board/sync_board.py --live <saved page> --rows
   council/callsheets/rows/move-table-2026-10-19.json --push`), Sonnet.
4. Daemon move lists (`owners.daemons` in `schema/move-table.json`): each daemon owns moves, no home channel. Drop
   sprout `data/intake.json` home elements and bars-engine `daemons.ts:14`'s shared Metal pair when they are written.
5. Remaining drift the table now names: bars-engine `alchemy-graph.ts` growth edges (same state on sheng/ke) and
   `vector-move-families.ts`; the Sprout slice fight does not move a charge between cells yet (`slice/moves.js applyMove`).
   Opus thread when a game needs them.
