# The engine slice: twine narrative × daily-chore × encounter × rules layer

## State

Pass slice 1 is merged (`council/passes/6FACE_PASS_slice1_2026-10-16.md`; ledger
`council/ledger/2026-10-16-pass-slice1.json`). Wendell ruled 2026-10-16: sprout is a council repo and
the slice's home (`council/ledger/2026-10-16-chat-sprout-registration.json`; question
`slice-substrate-home` resolved). Sprout already has a built slice — S1–S6 all done, waiting on
Wendell's deferred live playtest (sprout `docs/slice-plan.md`, `docs/decisions/whats-next.md`).

This sheet is the handoff for the reconciliation session: one session, analysis only, no code.

## Read first (in order)

1. `sprout/CLAUDE.md` — sprout's rules bind you there.
2. `council/passes/6FACE_PASS_slice1_2026-10-16.md` — the four-layer contract and its positions.
3. `sprout/docs/slice-plan.md` — what the built slice does, layer by layer (9.8 KB, dense, read whole).
4. `ontology/v0.1/QUICKSTART.md` + `design-ontology-model-v0.1.md` § Constitutional collections —
   the tension representation the contract names.
5. bars-engine `.specify/specs/`: `trust-encounter-loop`, `encounter-slot-context-schema`,
   `transformation-encounter-geometry`, `unified-cyoa-graph-authoring` — the reference record.
   The trust reducer and twine IR stay borrowed as libraries; no code moves between repos.

## The reconciliation map (from the 2026-10-16 pass against the built slice)

| Pass contract layer | What the built slice has | Gap the session must name |
|---|---|---|
| 0 World state (one clock owner) | `slice/state.js`: `heart`, `drain`, `edgePts`, mana, compost, `bonded`, `events` log | No day/time clock at all — the slice is a loop, not a day. The `events` log is the seed of resolution records. |
| 1 Chore loop (day engine) | Farm verbs (fertilize), ring access, walking, post-fight grounding choice | No sleep/day-commit; the grounding choice fires per fight, not per day. |
| 2 Rules surface (tabletop) | Declared numbers and formulas in `data/slice.json` (odds, type chart, pity bonus) | Per-feature numbers, not a shared resolution layer; no declared roll or record of how a rule resolved. |
| 3 Narrative (twine IR) | Scripted arrival, push text, placeholder strings in `data/slice.json` | No story graph, no IR, no predicate-fired passages. `edgePts` recognition is the ontology's tension representation already built — keep it. |
| 4 Encounter | Full negotiation fight: stances as type chart, Demand, satisfaction, Ting | Sprout's fight is its own reducer, not the bars-engine trust reducer — two encounter engines now exist. The session must propose: unify, adapt, or declare sprout's the local form. |

## Owner-unresolved items already in sprout (carry through the reach test)

These are Wendell's to answer and predate council registration; they belong on the board if the
reach test passes:

1. **Two inferred type-chart relations** — same element and generated-by outcomes in the S4 fight
   are marked *Inferred: tell me what you want* (`slice-plan.md` S4).
2. **Heart vs separate pool** — S3 built `edgePts` as its own pool; Wendell was asked whether the
   heart itself should drop instead (S3 note).
3. **Deferred live playtest** — the automated playtests stand in until there is more content
   (`docs/decisions/whats-next.md`). Reconciliation may change when the live test makes sense.

## Definition of done

- A reconciliation section in sprout's `docs/slice-plan.md` (or `docs/engine-contract.md` if cleaner):
  the table above filled with evidence and the gap named per layer, citing the pass and the ontology.
- Each surviving owner item on the Council Board with options and consequences, or retired by the
  record.
- Positions appended (or flipped) via the council board process; ledger record in the home repo.
- No code, no balance changes, no story text — sprout's CLAUDE.md rules and placeholder numbers stay
  untouched. Building waits for a following session and the standing positions.

## Rulings and positions (2026-10-17 board answers, pull 062632)

Reconciliation session ran 2026-10-16/17: `docs/engine-contract.md` in sprout names the gap per layer;
board rows added. Wendell answered everything on the board (ledger
`council/ledger/2026-10-17-pull-062632.json`):

- `q-slice-playtest-order` → **B** — build the engine slice first, one combined playtest after.
  The deferred live playtest stays deferred until the engine slice exists.
- `q-slice-heart-pool` → **C** — keep the pool now, revisit after the first live playtest.
- `q-slice-typechart-inferred` → **steer** — deeper research first: a 6-face pass using the Pokémon
  type system as the model, specifically how Pokémon moves use Pokémon stats to balance the game.
- `pos-slice-day` → **stands** (no steer). The no-day-clock gap is acknowledged as the current shape.
- `pos-slice-rules` → **overruled**, steer: explain it in plain terms, to the degree it makes sense
  to Wendell, before anything moves forward — "this sounds like mumbo jumbo".
- `pos-slice-passage` → **overruled**, steer: the narrative layer is the main thing needing
  feasibility testing; if the engine goes, generating content becomes easy.
- `pos-slice-encounter` → **overruled**, steer: don't paper over the two-engine gap — have the six
  faces explore how to actually bridge it.

## Next work (one session each, in the order Wendell's steers set)

1. **Plain-language re-explanation** of `pos-slice-rules` (the shared resolution layer) — no jargon,
   no board row until he says it makes sense. Chat-first, per his steer.
2. **Six-face pass: encounter-gap bridge** — how the trust reducer and sprout's fight actually
   become one engine, not a papered-over seam. Queued as research, not build.
3. **Six-face research pass: type chart** — Pokémon type system as model: how moves use stats to
   balance types. Feeds the S4 inferred relations.
4. **Feasibility testing** of the narrative/IR layer (passage steer) — prove the engine before
   generating content.
5. Then the engine slice build (ruling B), one combined playtest after.
- Zo-environment guards apply: local dev, not scheduled agent work; race test and quota wiring
  before any automation.

## Pass 2 done (2026-10-17): next-work items 1–3

- Item 1: the plain explanation went to Wendell in the thread "slice engine answers" and is on the board as
  `q-slice-referee-clear` (does it make enough sense to build on; A build, B explain more, C something else).
- Items 2–3: `council/passes/6FACE_PASS_slice2_2026-10-17.md`, ledger `council/ledger/2026-10-17-pass-slice2.json`.
  Positions `pos-slice-bridge` (four encounters, one shape: one referee and logbook, each engine keeps its chart),
  `pos-slice-chart-stats` (Pokémon model in simulation only; numbers come back to him with data),
  `pos-slice-feasibility` (five tests, three falsifiers). Simulation: `council/passes/slice2-sim/chart.mjs`
  (`node chart.mjs <sprout checkout>`): with today's placeholders any damage-only line reaches 75% offering odds and
  many reach the 95% cap; the two guessed relations never appear in a best line.

## Next (waits on `q-slice-referee-clear`)

- **On A:** one fresh Opus thread in sprout builds `pos-slice-feasibility` tests 1–5 in order, numbers unchanged
  (sprout CLAUDE.md: no balance change). Load the ontology QUICKSTART only. Test 5 (chart and stats) runs in bots
  only and brings its numbers back to the board as the replacement for `q-slice-typechart-inferred`. Bridge rule from
  `pos-slice-bridge`: when the spirit is made of the player's own feeling, the player reports settledness; the game
  computes only a creature's.
- **On B:** a short Sonnet thread answers his note with a worked example from the slice; the build waits.
- `docs/engine-contract.md` is cited by pass 1 rows but is not on sprout main (checked 2026-10-17); the build
  thread looks for its branch or writes it fresh.

## Referee worked example done (2026-10-17)

Wendell answered `q-slice-referee-clear` B with a note: the referee works on several levels (battle and non-battle
skill rules) and the unclear part is story encounters and faction relationships. The worked example is
`council/passes/slice-referee-worked-example_2026-10-17.md` (ledger `council/ledger/2026-10-17-referee-worked-example.json`):
one referee procedure of five steps, two rule sets (battle chart, story need), a faction as a standing moved only by
logbook lines. The revised question is `q-slice-referee-clear-2`. **On A:** one fresh Opus thread in sprout builds
`pos-slice-feasibility` tests 1 to 5, as in "Next" above, and may take the example's logbook line shape as the
starting point. **On B:** a second short Sonnet example answers the exact point he names.

## Referee on 2d6 done (2026-10-17)

Wendell answered `q-slice-referee-clear-2` B with a steer: story beats on the Apocalypse World model, ranked outcomes
including negative ones, rolled against a 2d6 table. The third example is `council/passes/slice-referee-2d6_2026-10-17.md`
(ledger `council/ledger/2026-10-17-referee-2d6-example.json`): fit becomes a modifier (listened +1, match +1, misread
−1, standing for faction rolls, cap +3); 2d6 plus modifier reads hit 10+, partial 7–9 (player picks the cost), miss 6−
(the referee takes the next rung of the faction's ranked consequence list; a hit climbs one back). Battle keeps its
percentage. The revised question is `q-slice-referee-clear-3`. **On A:** one fresh Opus thread in sprout builds
`pos-slice-feasibility` tests 1 to 5 as in "Next" above, story and faction on the 2d6 table, battle on its percentage.
**On C:** the same build with battle also on 2d6 (the chart becomes its modifier). **On B:** another short example.

## Built (2026-10-17): feasibility tests 1 to 5

Wendell answered `q-slice-referee-clear-3` A. sprout #56 (`docs/engine-contract.md`; ledger
`council/ledger/2026-10-17-engine-slice-build.json`) builds the referee and logbook, a scene from a logbook line, sleep
and the day's page, one line shape (fight, offering, talk, and a bars-engine trust-loop fixture), and the
chart-and-stats bots. `npm run test:engine` and `npm run sim:chart` in sprout; all three falsifiers green, no number in
`data/slice.json` changed. The game screen does not use the engine yet. Tests `slice-bots-chart` and
`slice-referee-off` are green. The board question is `q-slice-chart-stats`: the odds cap hides the stats.

## Next (waits on `q-slice-chart-stats`)

- **On A (recommended):** one fresh Opus thread in sprout puts the referee and story layer on the slice's screen
  (`slice/main.js`: pass a referee to `act` and `offer`, sleep in the farmhouse, Mara at the gate) for the one
  combined playtest. Today's chart; sprout #56 must merge first.
- **On B:** a short bots-only round in `tools/chart-stats.mjs` lets a family move the offering odds, numbers back to
  the board.
- **On C:** the same screen build, with the fight reading `data/engine.json` `simulation` as its chart.

## Built (2026-10-17): the referee on the slice's screen

Wendell answered `q-slice-chart-stats` A (keep today's chart for the playtest). sprout #57 (draft, stacked on #56; its
base is #56's branch) gives the fight and the ring offering one referee, makes the farmhouse door end the day with its
page, brings Mara to the east fence gap the morning after an unfed offering, and runs her talk on 2d6 with the chances
shown before the roll. A Logbook button lists every line; `?referee=off` writes nothing. No number in
`data/slice.json` changed. Screen text is placeholder copy in sprout `data/engine.json` `text`. Board step
`slice-referee-playtest-01` (list `slice-referee-playtest`, due 10-20) is his combined playtest, run on his Mac with
`npm run slice:serve` (the slice has no web host).

## Next (waits on step `slice-referee-playtest-01`)

- **His note says fine (or nothing to change):** a Sonnet thread marks #56 ready, merges it, retargets #57 to main and
  marks it ready (sprout has no auto-merge: he merges or says to).
- **His note names a change:** a fresh Opus thread owning #57 makes it, numbers unchanged unless he rules them.
- **The Terminal line fails:** start a Remote Control session in /Users/wendellbritt/The Library to clone and serve it.
