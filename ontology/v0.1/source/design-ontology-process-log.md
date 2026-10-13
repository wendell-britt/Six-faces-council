# Design Ontology — Process Log and Roadmap

**Owner:** Wendell Britt
**Current stage:** Council Phase A ingestion and local canon reconciliation complete; owner correction in progress
**Last updated:** 2026-10-12

## Deferred product step

Upgrade the Aesthetic Intake Adventure from browser-local storage to durable, account-linked storage, then add an explicit AI research and approval stage.

That stage should:

1. preserve entries, images, snippets, source links, and revisions across devices;
2. ask permission before transmitting private notes or attachments for research;
3. resolve ambiguous works, editions, versions, creators, and URLs before analysis;
4. label researched facts, interpretations, and AI hypotheses separately;
5. show the research record to the adventurer for correction or approval;
6. generate medium-specific follow-up questions from both the intake and verified sources;
7. keep raw intake, external research, adventurer clarification, excavation, and ontology synthesis as distinct provenance layers.

This is important infrastructure, but it is not a prerequisite for continuing the current ontology process manually with exported intake records.

## Ontology-development sequence

1. **Psychograph seed** — provisional designer and ideal-user hypotheses.
2. **Aesthetic intake** — collect charged examples without synthesis.
3. **Source research** — understand each example in its actual medium and context.
4. **Dialogical excavation** — ask tailored questions that separate surface preference, living mechanism, felt response, meaning, and design transfer.
5. **Pattern extraction** — propose recurring aesthetic forces, polarities, boundaries, and anti-patterns.
6. **Framework translation** — inspect candidates through AQAL, Emotional Alchemy, Octalysis, somatics, and the BAR lifecycle.
7. **Design philosophy draft** — articulate constitutional principles, aesthetic commitments, and epistemic rules.
8. **Ontology modeling** — define entities, relationships, evidence types, states, provenance, and confidence.
9. **Council ingestion and translation** — teach the six Game Master faces before asking them to evaluate or govern.
10. **Operational synthesis and governance** — only after ingestion, sort material into active, reference, and compost sets and form the smallest coherent working version.
11. **Playable verification** — use the ontology to make and test games and design-tools-that-are-games; revise from player evidence.

## Current decision

First-pass excavation is complete for all five specimens: Pokémon, Monster Rancher’s disc-generation system, *Inception*, Go, and *Dungeon Crawler Carl*. The cross-specimen synthesis is recorded in `design-ontology-pattern-extraction-round-1.md`.

Stage 6 framework translation is recorded in `design-ontology-framework-translation-round-1.md`. It identifies each framework’s function and limits, near-equivalences, preserved tensions, evidence rules, and revisions required before philosophy drafting.

Stage 7 is recorded in `design-philosophy-draft-v0.1.md`. It contains a provisional constitutional layer, design commitments, epistemic rules, productive tensions, inquiry prompts, playable verification, and instructions for AI collaborators.

Stage 8 is recorded in `design-ontology-model-v0.1.md`, with a machine-readable vocabulary seed in `design-ontology-v0.1.yaml`. The model defines entities, relationships, evidence authority, confidence profiles, development and Emotional Alchemy structures, adaptive-system requirements, lifecycle states, and hard invariants for AI collaborators.

Stage 9 Phase A artifacts are collected in `outputs/council-phase-a/`. All six faces demonstrated source-recognizable ingestion; five face records and a Sage synthesis preserve their translations separately. Five face-specific BARS crosswalks and a Sage canon reconciliation compare the new package against the local sources named in the council brief.

Five of six Phase B entry conditions are met or met within the inspected local corpus. Owner correction is the remaining entry condition. Continue through the questions in `sage-canon-reconciliation.md` by reconstructing what, where, and when before deciding how. Resolve questions through evidence and bounded deliberation when possible; escalate only irreducible matters of Wendell's meaning, values, or authority. Do not begin general governance, reduction, or active/reference/compost sorting without Wendell's later explicit authorization.

## Targeted constitutional-evolution decision — 2026-10-10

Wendell delegated the eight-versus-fifteen constitutional relationship to the six Game Master council and directed the council to reconstruct what changed, where, and when before deciding how the collections relate.

The six faces unanimously determined that:

- the eight principles in the original council brief are the preserved constitutional seed;
- the fifteen principles in the design-philosophy draft are the current provisional v0.1 constitution;
- the relationship is a provenance-preserving amendment, expansion, and restatement;
- all eight original lineages continue, while seven principles were added through excavation, pattern extraction, and framework translation;
- the fifteen supersede the eight only as the complete current membership set, without erasing the eight as origin and historical wording.

The decision and full lineage map are recorded in `council-phase-a/constitutional-evolution/council-decision.md`. This authorization resolved only constitutional succession. It did not authorize wider Phase B reduction, canon-conflict resolution, or active/reference/compost sorting.

## Targeted face-namespace decision — 2026-10-10

The six Game Master council reconstructed the meanings of “face” across BARS foundations, player sects, runtime agents, functional review doctrine, I Ching prework, Emotional Alchemy phase voices, and the ontology council.

The council unanimously determined that:

- altitude face, runtime sect, review discipline, player sect identity, and council lens are distinct ontology concepts;
- the named Shaman–Sage uses share a `GameMasterArchetype` lineage but do not share identity, authority, permission, or developmental status;
- the Ontologist–Integrator set is a separate functional review taxonomy with explicit, task-specific mappings;
- choosing, invoking, enjoying, or serving through a face cannot establish a person’s global developmental altitude or worth;
- all cross-namespace relations must be typed, scoped, and provenance-bearing.

The full decision is recorded in `council-phase-a/face-namespaces/council-decision.md`. The face-namespace implementation remains unchanged pending a separately authorized implementation pass; later edits to BARS doctrine corrected the independent WAVE terminology issue.

## Owner WAVE-terminology decision — 2026-10-10

Wendell resolved the WAVE collision by restoring the intended category boundaries:

- Wake Up, Open Up, Clean Up, Grow Up, and Show Up are the five **Basic Moves**;
- **WAVE** is reserved for the breathing practice associated with Open Up;
- Wake → Clean → Grow → Show is a separate Emotional Alchemy **within-channel progression**;
- the fifteen canonical moves remain five Transcend, five Generative, and five Control moves.

The current ontology package now uses these distinctions. Earlier council ingestion and crosswalk files remain unchanged as provenance but are superseded on this terminology. The owner decision is recorded in `council-phase-a/wave-terminology/owner-decision.md`.

## Six-face encounter-and-completion decision — 2026-10-12

At Wendell's direction, all six Game Master faces examined encounter ending and completion for broad genre portability, with tabletop and videogame RPGs as primary stress tests.

The council unanimously separated:

- participant exit;
- session and encounter ending or suspension;
- move resolution;
- quest completion or another named quest disposition;
- arc conclusion;
- satisfaction and transformation.

It also introduced composable encounter contract families, CompletionContracts, separate lifecycle axes, and evidence- and authority-bound CompletionClaims. A player may validly end an encounter through rest, refusal, witnessing, retreat, interruption, or no-shift while leaving a Show Up quest incomplete.

Wendell then established the canonical scope verbs: **moves resolve, encounters end, quests complete, and arcs conclude**. “Quest fulfillment” and “quest termination” are superseded as lifecycle language; failed, expired, declined, abandoned, superseded, and composted are named noncompletion dispositions.

The decision and six face records are stored in `council-phase-a/completion-boundaries/`. The model, YAML, council brief, and canon reconciliation now carry the distinction.

## TensionVector reconstruction begun — 2026-10-12

The doctrinal, interface, persistence, schema, and privacy sources were traced before seeking an owner decision. The reconstruction distinguishes lived tension, player reports, structured representation, persisted snapshot, transformation record, action intention, and artifact dispatch. It also records that the canonical ideal type, actual collected fields, persisted fields, privacy claims, and downstream reuse currently do not fully match.

The evidence and the naming fork subsequently resolved by the council are recorded in `council-phase-a/tension-vector/reconstruction.md`.

## Six-face TensionVector recommendation — 2026-10-12

All six Game Master faces agreed that TensionVector must not contain the full before-to-after process and cannot be identical to lived tension. They recommend a formal separation among LivedTension, TensionReport, TensionRepresentation, TensionConfiguration, TensionSnapshot, TransformationRecord, SatisfactionReport, ActionIntention, ActionRecord, ArtifactDispatch, ConsequenceRecord, and TransformationTrace.

The final naming ruling uses `TensionRepresentation` and `TensionConfiguration` in the general ontology, `TensionSnapshot` for persisted data, `TransformationTrace` for the full lineage, and **Tension Map** for player-facing language. Bare `TensionVector` is retired; `BARS321TensionVector` survives only as a deprecated compatibility alias.

The council also found a material privacy and purpose mismatch between public/doctrinal claims and current persistence and downstream reuse. The final ruling is recorded in `council-phase-a/tension-vector/council-decision.md`. The active ontology schema now carries the ruling; BARS doctrine, privacy copy, runtime, and stored-data migration remain a separately scoped implementation pass.

## Derived movement reconstruction and decision — 2026-10-12

The next owner-correction question was resolved by reconstructing the implemented path before assigning authority. The current Quest Grammar counts creator-authored satisfaction, dissatisfaction, and self-sabotage labels; deterministically creates a lowercase legacy translate/transcend sequence; uses that sequence in the compiled packet, admin review, and some prompt context; and drops the movement metadata when passages are published.

The ontology now treats this output as a correctable `DerivedMovementProposal`. An accepted proposal may become a `MovementRoutingPlan` for authored content, but neither object is evidence that a player moved. Actual play supports a separate `MovementFinding` linked to transformation evidence. The ruling also distinguishes the legacy Epiphany-Bridge meanings from the canonical fifteen-move grammar, where Translate is cross-channel and Transcend is within-channel.

Correction stops future use, flags unpublished descendants, versions published descendants, and preserves historical play without treating the rejected proposal as player truth. The reconstruction and full decision are recorded in `council-phase-a/derived-movement/reconstruction-and-decision.md`. No BARS implementation or data migration was authorized.

## Yellow Brick Road reconstruction and decision — 2026-10-12

The foundational claim that “you can never go the wrong way” was reconstructed alongside the ontology's evidence, completion, authorship, and refusal rules. It is retained as mythic reassurance and a recoverability covenant, not as a metaphysical or operational guarantee. The precise rule is **no path has to be wasted**.

The ontology now preserves authored destinations, falsifiable route hypotheses, divergence records, scoped blockers, and recoverability paths. Divergence does not prove hidden desire; learning does not make harm or error necessary; changing Point B does not retroactively reach the original Point B. Some blockers may remain unresolved indefinitely while continuing to constrain a specific route.

The full ruling is recorded in `council-phase-a/yellow-brick-road/reconstruction-and-decision.md`. A separate packaging assessment in `claude-code-ontology-shipping-readiness.md` finds the corpus usable as manual Claude Code context now, approximately halfway to a dependable repo-local alpha, and recommends a three-pass manifest/skill, council-agent, and evaluation release path.

## Roadblock and intention reconstruction and decision — 2026-10-12

The source collision was reconstructed across its three operating layers: observable obstruction, the pre-commit metabolism ritual, and Yellow Brick Road meaning-making. The ontology now separates `RoadblockEvent`, `RoadblockClassification`, `RoadblockCausalAccount`, `IntentionAlignmentHypothesis`, `RoadblockResponse`, and `MetabolizationOutcome`.

The binding rule is: **a roadblock may reveal a mismatch among intention, method, conditions, and capacity; it does not prove misaligned intention.** Technical faults cannot be used to psychologize a contributor or player. At the technical layer, metabolization may mean repair, verification, safer routing, reusable learning, or provenance without emotional processing. Unresolved, rested, rerouted, abandoned, and composted blockers remain valid possibilities under the Yellow Brick Road decision.

The full ruling is recorded in `council-phase-a/roadblocks/reconstruction-and-decision.md`. No BARS runtime, workflow, or data migration was authorized.
