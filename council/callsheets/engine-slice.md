# The engine slice: twine narrative × daily-chore × encounter × rules layer

## State
Pass slice 1 is merged (`council/passes/6FACE_PASS_slice1_2026-10-16.md`; ledger
`council/ledger/2026-10-16-pass-slice1.json`). It defines the biggest slice that tests the four-layer
contract — one day, one passage, one encounter, one rules resolution — and what each layer must prove.
Wendell ruled 2026-10-16: sprout is a council repo and the slice's home
(`council/ledger/2026-10-16-chat-sprout-registration.json`; question `slice-substrate-home` resolved).

## The discovery that changes the plan
Sprout already has a built slice: `docs/slice-plan.md` describes it and it waits on Wendell's playtest
(sprout `CLAUDE.md`, "Read first"). Before building anything new, the pass's contract must be
reconciled with what exists there.

## Next
- Read `sprout/docs/slice-plan.md` and `sprout/docs/design.md` against the pass's four-layer contract.
  Name what the built slice already proves and what it lacks (rules resolution against the trust
  reducer, encounter slot, substrate hooks).
- The trust reducer and twine IR compiler stay borrowed from bars-engine as libraries; no code moves.
- Bars-engine's specs stay the reference record: `trust-encounter-loop`, `encounter-slot-context-schema`,
  `transformation-encounter-geometry`, `unified-cyoa-graph-authoring`.

## Rulings and positions
- Board rows `pos-slice-day`, `pos-slice-passage`, `pos-slice-encounter`, `pos-slice-rules` stand;
  question `slice-substrate-home` resolved 2026-10-16 (sprout).
- Zo-environment guards apply: local dev, not scheduled agent work; race test and quota wiring before
  any automation.
