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
