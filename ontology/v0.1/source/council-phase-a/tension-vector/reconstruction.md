# TensionVector Reconstruction — What, Where, and When

**Date:** 2026-10-12
**Status:** Source reconstruction before ontology decision

## What the sources currently claim

The canonical 3-2-1 doctrine calls `TensionVector` the structural output of the dialogue and states that it **is** the dissatisfied emotional state made explicit. Its declared fields are:

- mask name;
- desire and desired outcome;
- life state;
- root cause;
- fear;
- interior voice;
- integration shift.

The same doctrine later compresses the dissatisfied state to “mask + desire + fear,” locates transformation in the perspective shift, and locates satisfaction in aligned action plus artifact. The named vector therefore already spans more than the dissatisfied-state definition: `integrationShift` belongs to the transformation side of the process.

## What exists in implementation

There is no single implemented `TensionVector` type bearing the doctrinal fields.

`Shadow321Runner` temporarily gathers a larger `Answers` object:

- charge description, mask shape, and mask name;
- desire, desired outcome, and desired-feeling tags;
- life state, root-cause response, and fear;
- interior voice and integration shift;
- somatic echo;
- desired feeling and desired-feeling tags.

When the session is persisted, the current primary route stores only selected projections:

- `phase3Snapshot.identityFreeText`: mask shape plus mask name;
- `phase2Snapshot.q1`: charge description;
- `phase2Snapshot.q3`: life state;
- `phase2Snapshot.q5`: root-cause response;
- `phase2Snapshot.alignedAction`: selected Basic Move, when present;
- outcome, links, and shadow-name resolution metadata.

Several declared TensionVector fields—desire, desired outcome, fear, interior voice, integration shift, somatic echo, and desired feeling—are not included in that primary persisted snapshot. Conversely, the snapshots contain player-authored narrative content rather than only abstract structural coordinates.

Persistence can also trigger derived effects: a witness BAR, quest, daemon, collective fuel action, blessed-object unlock, or merge into matching NPC inner-work state. Thus storage and downstream reuse are not identical to representing the player’s dissatisfaction.

## Where the layers belong

### 1. Lived tension

The person’s embodied, emotional, interpretive, and situational experience. It exceeds any prompt response or schema. The player has primary authority over its inward meaning.

### 2. Tension report

What the player expresses during a particular encounter: words, selections, somatic descriptions, silences, corrections, and refusals. It is time-bound evidence, not the experience itself.

### 3. Tension representation

A structured, lossy organization of selected reports for a stated purpose. `TensionVector` can be the product name for one such representation, provided it records its source, omissions, derivation, purpose, version, uncertainty, and player correction.

### 4. TensionVector snapshot

The exact fields persisted at a particular time. This must not be confused with either the full session report or the doctrinal ideal type.

### 5. Transformation record

Evidence about what shifted, did not shift, or remained unclear during or after the practice. `integrationShift` belongs here rather than inside the dissatisfied-state vector.

### 6. Action intention and artifact dispatch

The selected Basic Move, proposed action, and resulting BAR, quest, daemon, fuel contribution, or Witness Note. These are consequences or translations of the encounter, not constituents of the original tension.

## When each object exists

1. Lived tension may predate the game and continue after it.
2. Tension reports emerge during the encounter and may change through the dialogue.
3. A TensionVector is assembled from selected reports at a named derivation point.
4. A snapshot exists only when fields are persisted.
5. Transformation and no-shift findings arise through player report or other properly scoped evidence.
6. Action intentions and artifacts arise after or alongside interpretation and may later change the underlying situation.

Every later snapshot is a new representation, not proof that the earlier vector was false or that one stable hidden state has finally been discovered.

## Current semantic and privacy conflicts

1. **Identity error:** saying the vector “is” the lived state collapses subject and representation.
2. **Boundary error:** `integrationShift` mixes transformation evidence into a dissatisfied-state structure.
3. **Causal overclaim:** `rootCause` is produced by the prompt “what would have to be true”; it is better treated as a player-authored root belief or causal hypothesis, not established cause.
4. **Completeness mismatch:** doctrine lists fields that the main persisted snapshot does not retain.
5. **Privacy mismatch:** doctrine and UI say raw journal text is not captured, while persisted snapshots include charge description, life-state text, root-belief text, and mask identity text.
6. **Reuse mismatch:** persisted material may generate a witness BAR or influence NPC state, which is a distinct purpose from completing or preserving the player’s 3-2-1 encounter.
7. **Vector ambiguity:** the current object contains narrative features but does not explicitly encode direction, magnitude, source state, target state, or confidence normally implied by “vector.”

## Provisional ontology finding

The evidence supports this distinction:

> **The lived tension is the phenomenon. A TensionVector is a purpose-bound, versioned, lossy, player-correctable representation derived from reports about that phenomenon. Transformation records and dispatched artifacts are related outputs, not parts of the tension itself.**

This finding preserves the usefulness of structural extraction without allowing the model to claim possession of the player’s interiority.

## Decision subsequently resolved by council

The reconstruction originally left open whether **TensionVector** should name:

1. the structured representation of the dissatisfied configuration only; or
2. a larger before-to-after transformation representation containing source tension, movement, and target state.

The current doctrine gestures toward both. The current implementation persists only partial projections of either.

Wendell directed the council to resolve this through deliberation rather than refer an answerable question back to him. The final ruling retires bare `TensionVector`, adopts formal `TensionConfiguration`, persisted `TensionSnapshot`, full-path `TransformationTrace`, and player-facing **Tension Map**, while preserving `BARS321TensionVector` only as a deprecated compatibility alias. See `council-decision.md`.

## Sources inspected

- `/Users/wendellbritt/The Library /bars-engine/specs/doctrine/emotional-alchemy-321.md`
- `/Users/wendellbritt/The Library /bars-engine/src/app/shadow/321/Shadow321Runner.tsx`
- `/Users/wendellbritt/The Library /bars-engine/src/actions/charge-metabolism.ts`
- `/Users/wendellbritt/The Library /bars-engine/src/lib/quest-grammar/deriveMetadata321.ts`
- `/Users/wendellbritt/The Library /bars-engine/prisma/schema.prisma`
- `/Users/wendellbritt/The Library /bars-engine/src/app/wiki/privacy/page.tsx`
- `/Users/wendellbritt/The Library /bars-engine/specs/spec-kit-well-audit.md`
