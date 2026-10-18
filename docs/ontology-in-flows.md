# The design ontology in the council's flows

Wendell, 2026-10-16: "We've also added a game design ontology to the six faces repo that is designed to be used in
continuing our game design work. I'd say its important for us to review that using the 6 faces and figure out how
best to deftly use the information and processes there in our flows in a way that remains deft and token efficient"

Decided in six-face pass ontology-flows 1 (`council/passes/6FACE_PASS_ontology-flows1_2026-10-16.md`); the `of-*`
positions on the board stand unless he flips them.

## The rule in one line

Load the ontology where a design decision is made; everywhere else carry it as a sentence, a field or a check.

The `default` profile (Quickstart) costs about 5,000 tokens and every deeper profile about 29,000, and a thread pays
that again on every tool call. Threads already open at 100,000 to 140,000 tokens.

## Flow by flow

| Flow | Loads | Carries the ontology as |
|---|---|---|
| Six-face pass on a game, mechanic or design tool | `default` plus the one profile the question needs | the six-faces skill, as now |
| Strand thread that designs a mechanic | the profile its callsheet's `ontology:` line names | the line |
| Round or chamber thread (art, build, tuning) | nothing; `default` at most, and only when the round's `builds` names an ontology object | the loop round's optional `ontology_profile` |
| Board read, board pull, Nonprofit saves | nothing | `term_lint.py` |
| Needs-work list | nothing; an item that becomes a design question goes to its strand thread | `term_lint.py` |
| Daily compost pass | nothing | three sentences in `docs/compost-pass.md` |

## The callsheet line

A strand that designs game mechanics carries one line under its date:

    ontology: game_design; touches: TensionConfiguration, MovementFinding

The profile is a key of `load_profiles` in `ontology/manifest.yaml`, or `none`. `touches` names at most three ontology
objects. A sheet without the line loads nothing in its round threads; a council pass still follows the six-faces
skill. The strand's first design thread sets the line. Nobody backfills old sheets for it.

## The term check

`python3 ontology/tools/term_lint.py` scans callsheets, docs and open board rows for the retired and reserved terms
(the manifest's `compatibility` block and the deprecated WAVE phrases of the binding decision) and for wording that names Wendell's
rest as a deficiency. It warns and never blocks a save; `tests/test_term_lint.py` keeps today's record clean. It
cannot judge "complete WAVE" (valid for a finished breathing run, deprecated for Wake, Clean, Grow, Show) or the
legacy lowercase `translate`/`transcend`, so those still need a reader.

The "WAVE room" is valid: it runs the manual W.A.V.E. breath (Welcome, Acknowledge, Validate, Exhale), which is the
Open Up breathing practice the manifest reserves the word for (`council/callsheets/wave-room.md`, 2026-10-13).

## Precedence

The repo's working rules (CLAUDE.md, the docs here, the loop contracts) govern process: where work runs, when, on
which model, and who is asked. The ontology's binding decisions govern what game objects mean, and its evidence and
consent limits. Both are Wendell's records, so a real conflict between them goes through the reach test and onto
the board as a row; neither wins silently.

## Changes to the ontology itself

The ontology is written with Codex and lands in `ontology/`. A Claude-side thread that finds a conflict writes a
board position or a reconciliation note and leaves the ontology text alone. A change Wendell asks for goes to Codex as a brief
in `docs/codex/` (the first is `asset-sources-brief.md`, 2026-10-17). No flow sorts `ontology/` into active,
reference and compost (Phase B is not authorized, `ontology/v0.1/RELEASE.md`). The ontology does not protect real
player data yet; flows that touch real data follow their own rules.
