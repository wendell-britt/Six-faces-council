# Spirit care (Finch folded into spirits, daemons and the Between)

ontology: game_design; touches: ConsequenceRecord, RecoverabilityPath, BARExpression

Started 2026-10-20 from Wendell's message in the thread "Finch and spirit care". Pass:
`council/passes/6FACE_PASS_spirit-care1_2026-10-20.md`. Rows: `council/callsheets/rows/spirit-care-2026-10-20.json`
(positions `sc-*`, questions `sc-undying`, `sc-after-death`, `sc-shadow-what`).

## State, 2026-10-20

- His ruling: spirits can die or be corrupted from neglect; shadow forces act on what you have made; Clean Up
  becomes self care and relationship care; spirits generate quest BARs from solo goals or Between agreements.
- Rows not yet on the board when the pass thread stopped (its context passed the handoff line).

## Brief 1, landing (Sonnet)

Land the rows file on the board: save the live board, then `python3 board/sync_board.py --live <saved page> --rows
council/callsheets/rows/spirit-care-2026-10-20.json --push`, republish to https://claude.ai/artifact/DxyShVS8tmvJym4HAsgnho,
run `python3 council/tools/voice_lint.py` on the new rows first. Reply names the rows and the link.

## Brief 2, simulation (Opus)

Brief 2 done, #327; findings in council/spirit-care/README.md.

Build `council/spirit-care/sim.py` with the decline ladder (thriving, dimming, stale, shadowed, fading, gone) as data,
three tracks (satisfaction, vitality, shadow), declared rest, and four players (daily, busy, rest, vanished three
weeks). Print each player's return. Pass: the vanished player's return welcomes before it reports, and at least one
simulated spirit can die. Leave a test the next round reruns. Read his answers to the three `sc-` questions first if
they are in; otherwise run every option of `sc-undying` and `sc-after-death`. Scout: rung 2 (we have it) for quest
BARs, bars-engine `src/lib/charge-quest-generator/generator.ts`.

## Round 2, shadow copy and quest offers (Opus), done 2026-10-20

His answers: sc-undying A, sc-after-death A, sc-shadow-what A (ledger 2026-10-20-pull-220519). Steers folded into
sim.py and four positions in `council/callsheets/rows/spirit-care-offers-2026-10-20.json` (sc-shadow-copy,
sc-offer-hold, sc-offer-rewrite, sc-offer-release). No new questions: the reach test answered each from his steers
and the hand's vibeulon discard.

## Brief 3, landing (Sonnet)

Land `council/callsheets/rows/spirit-care-offers-2026-10-20.json` on the board the way Brief 1 did (save the live
board, `python3 board/sync_board.py --live <saved page> --rows <file> --push`, republish). voice_lint's one hard
finding is inside his quoted words; leave it.

## Later

- Port to bars-engine: the spirit holds a quest (`generateQuestSuggestions`), buttons Yes / Not now / Rewrite /
  Let it go (one vibeulon). Waits on hd-wallet (vibeulons in his bars-engine wallet).

- Between round with one mortal shared spirit, after the cozy round 2 (`council/passes/BETWEEN_round2_cozy_2026-10-17.md`)
  lands. Changes the live copy "It cannot die" (bars-engine `public/between/garden.js:948`).
- Term pass for the player-facing word for the shadowed state (`sc-word`).
