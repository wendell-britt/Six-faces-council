# Derived Movement — Reconstruction and Ontology Decision

**Decision date:** 2026-10-12
**Status:** Provisional ontology ruling from source and implementation reconstruction
**Scope:** Legacy Epiphany-Bridge `translate`/`transcend` derivation, its authority, and correction behavior
**Implementation status:** Descriptive only; no BARS code or stored data was changed

## Governing distinction

> **A system may propose how authored material should route movement. It cannot infer from that proposal that a player moved.**

The current derivation is useful as a deterministic design heuristic. It is not a reading of the player's hidden truth, a transformation finding, or a developmental rank.

## What exists now

The current BARS Quest Grammar:

1. receives creator-authored unpacking answers for satisfaction, dissatisfaction, and self-sabotage;
2. counts selected labels;
3. treats `shadow + dissatisfaction > satisfaction` as `transcend`-dominant;
4. produces a per-node sequence of lowercase legacy values, `translate` or `transcend`;
5. copies that sequence into the quest packet's emotional signature and each compiled spine node;
6. exposes it in the admin outline and direct-AI prompt context;
7. does not provide a dedicated accept, reject, correct, or confidence field;
8. discards the movement metadata when publishing ordinary passages, although movement may already have influenced generated prose.

The derivation is deterministic but under-evidenced. It measures the number of labels, not their intensity, salience, causal role, bodily truth, or eventual effect. The default arc also assigns late `transcend` nodes before any player enactment occurs.

## Terminology collision

Two different grammars currently reuse the same words:

| Grammar | `translate` | `transcend` |
|---|---|---|
| Legacy Epiphany-Bridge binary | integrate within the current frame | cross a frame or structural threshold |
| Fifteen-move Emotional Alchemy grammar | move between emotional channels | move within one channel across altitude |

These are not interchangeable classifications. Capitalization alone is not a sufficient namespace boundary.

For ontology use:

- **LegacyEpiphanyMovementMode** is the compatibility namespace for the binary compiler heuristic;
- its semantic values are `integrate_within_frame` and `cross_frame_threshold`;
- lowercase implementation values `translate` and `transcend` are legacy encodings of those modes;
- **CanonicalAlchemyMoveFamily** retains `Transcend`, `Generative`, and `Control` for the fifteen-move grammar;
- a compatibility adapter may connect the two grammars, but it must not assert equivalence.

## Binding object model

### Source material

**MovementSourceReport** records the authored satisfaction, dissatisfaction, self-sabotage, contextual, or somatic material used by a derivation. It preserves who authored each field and whether the author is the designer, Game Master, player, or another participant.

### System proposal

**DerivedMovementProposal** is a versioned, purpose-bound system interpretation of source reports. It records:

- subject and author of the source material;
- derivation rule and version;
- inputs actually used and relevant inputs omitted;
- proposed grammar and semantic mode;
- uncertainty and known limits;
- intended use;
- status: `unreviewed`, `accepted_for_routing`, `corrected`, `rejected`, `superseded`, or `unknown`;
- correction and downstream lineage.

### Design routing

**MovementRoutingPlan** assigns proposed movement functions to authored beats, nodes, encounters, or other design units. Each per-unit assignment is a **MovementRoutingAssignment**.

The plan says what the design is attempting to invite or stage. It does not say what a player will experience.

### Enacted evidence

Actual play may create a **MovementFinding** linked to a TransformationRecord. Its allowed findings include `reported_shift`, `reported_no_shift`, `unclear`, `reinterpreted`, `refused`, and `unassessed`.

A MovementFinding requires evidence after or during play. It is never backfilled from a routing plan, node label, quest completion, artifact, or engagement trace.

## Authority ruling

1. The system has authority to generate a **proposal** within its declared design purpose.
2. The designer or Game Master has authority to accept or revise a routing plan for material they author, subject to the ontology's consent and evidence constraints.
3. The person whose inner experience is represented has authority to correct or reject claims about that experience.
4. A player does not need to ratify every hidden design instruction before play. Hidden routing may preserve mystery when its data use is permitted and it is not presented as truth about the player.
5. Optional explanation may expose the proposal and its basis. Explanation does not transfer meaning authority to the system.
6. No actor may convert a DerivedMovementProposal into a MovementFinding without appropriate play evidence.
7. In allyship, a self-reported useful or satisfying movement still does not establish helpfulness to another person; consent, relational evidence, and relevant right-quadrant consequences remain necessary.

## Correction and propagation

Correction is append-only at the provenance level and forward-effective at the design level.

When a proposal is corrected or rejected:

1. preserve the source reports without silently rewriting what was originally said;
2. preserve the original proposal as historical provenance unless deletion or revocation requires removal;
3. create a correction record and, when needed, a newly versioned proposal;
4. stop using the rejected proposal for future personalization, generation, routing, or evaluation;
5. invalidate or flag unpublished downstream drafts for regeneration or review;
6. supersede published design artifacts by version rather than silently rewriting play history;
7. retain completed play as an event that occurred under the earlier routing, while removing any claim that the rejected proposal described the player's truth;
8. attach correction notices to still-visible downstream artifacts when they materially reproduce the rejected interpretation;
9. record repair or limitation where external consequences cannot be technically reversed;
10. propagate deletion, revocation, and purpose restrictions according to the Tension Representation privacy ruling.

Correction is not failure, resistance, or proof that the player lacks insight. It is evidence that improves the adaptive model.

## Timing

| Time | Valid claim |
|---|---|
| Before compilation | Source reports exist; no route or movement is established |
| During derivation | The system produces a DerivedMovementProposal |
| During authoring | A MovementRoutingPlan may guide structure or prose |
| During play | The design invites movement; the result remains unknown |
| After relevant evidence | A MovementFinding may record shift, no-shift, uncertainty, reinterpretation, or refusal |
| After later consequences | Transfer, durability, and application fitness may be assessed within scope |

## Required record fields

A DerivedMovementProposal minimally records:

- stable id and creation time;
- source-report ids and field authorship;
- subject and intended audience;
- grammar namespace;
- derivation algorithm and version;
- proposed value or sequence;
- confidence or explicit absence of calibrated confidence;
- purpose and permitted uses;
- explanation availability;
- review status and reviewing authority;
- corrections, rejection, and supersession;
- downstream drafts, prompts, quests, artifacts, and evaluations affected;
- privacy, retention, deletion, and revocation behavior.

## Hard invariants

1. Derived routing is not enacted movement.
2. Narrative assignment is not transformation evidence.
3. Determinism is not validity.
4. Label count is not charge intensity or developmental depth.
5. Creator unpacking is not automatically player experience.
6. Hidden adaptation is not hidden truth.
7. Rejection or correction is not resistance.
8. A rejected proposal cannot continue silently shaping future personalized output.
9. Historical play is not rewritten to simulate a corrected past.
10. The legacy binary and fifteen-move grammars cannot be joined by label alone.
11. Player satisfaction governs self-directed inner validity; it does not establish allyship benefit.
12. Published prose influenced by a proposal remains part of its downstream lineage even when movement metadata was dropped.

## BARS implementation delta

The current implementation lacks proposal status, correction, confidence, explicit grammar namespacing, and downstream invalidation. Its published Passage records do not retain the movement assignment or derivation lineage. Direct AI prompts receive the sequence, while the agent-generation route is given the unpacking material without the same explicit movement field. These are implementation mismatches to address later; they do not invalidate the usefulness of the heuristic as a provisional authoring aid.

## Resolution of the owner-correction question

Derived legacy translate/transcend output is **player-correctable routing hypothesis**, not authoritative classification. More precisely, it is a DerivedMovementProposal that may become an accepted MovementRoutingPlan for authored content. The actual player's movement remains unknown until supported by MovementFinding and TransformationRecord evidence.
