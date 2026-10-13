# Six–Game Master Council Recommendation — TensionVector Boundary

**Date:** 2026-10-12
**Status:** Superseded by `council-decision.md`; retained as deliberation provenance

## Unanimous finding

> **The lived tension is the phenomenon. The system can hold only a purpose-bound, versioned, lossy, player-correctable representation derived from reports about that phenomenon. Transformation, satisfaction, action, artifact, and consequence are separate records linked by provenance.**

All six faces reject using TensionVector for the entire before-to-after process. They also reject the doctrinal identity claim that the stored or structured object **is** the dissatisfied emotional state.

## Recommended formal model

### Experiential and evidentiary layers

- **LivedTension:** the embodied, emotional, relational, interpretive, and situational phenomenon; the system cannot claim to exhaust it.
- **TensionReport:** a time-bound player expression, selection, somatic report, correction, silence, uncertainty, or refusal.
- **TensionRepresentation:** parent class for purpose-bound structural interpretations of selected reports.
- **TensionConfiguration:** the formal representation of a dissatisfied configuration at a declared derivation point.
- **TensionSnapshot:** the exact fields persisted at a named time.
- **TransformationRecord:** evidence of shift, no-shift, uncertainty, refusal, or changed interpretation.
- **SatisfactionReport:** the player’s first-person assessment of the result.
- **ActionIntention:** a proposed or selected next action, not evidence that action occurred.
- **ActionRecord:** evidence that action occurred.
- **ArtifactDispatch:** creation or preservation of a BAR, quest, daemon, Witness Note, fuel contribution, or other artifact.
- **ConsequenceRecord:** later changes in possibility, relationship, world, or system.
- **TransformationTrace:** provenance connecting any subset of these records without requiring a successful or complete arc.

## TensionVector naming disposition

The council agrees that the current object is not a mathematical vector: it has no stable coordinate space, units, origin, direction rule, magnitude, comparison operation, or uncertainty model.

The integrative recommendation is:

- use `TensionRepresentation` and `TensionConfiguration` in the general ontology;
- preserve `BARS321TensionVector` as a namespaced subtype, compatibility alias, or deliberately evocative product term;
- forbid bare `TensionVector` in formal schemas or retrieval where its scope matters;
- describe it to players as “what you named” or a “tension map” unless the player-facing metaphor proves useful;
- reserve any future quantitative vector type for a model that declares its dimensions, units, derivation, uncertainty, and permitted operations.

## Field disposition

| Current field or material | Recommended home |
|---|---|
| `maskName`, mask shape | MaskMetaphor linked to TensionConfiguration |
| `desire`, `desireOutcome` | attraction or desired-outcome reports in TensionConfiguration |
| `fear` | avoidance or feared-outcome report in TensionConfiguration |
| `lifeState` | contextual TensionReport |
| `rootCause` | rename to `playerCausalHypothesis` or `rootBeliefReport`; never established cause |
| `interiorVoice` | player-authored report produced through PartPerformance |
| `somaticEcho` | SomaticReport |
| desired feeling | DesiredStateReport, not achieved state |
| `integrationShift` | TransformationRecord |
| selected Basic Move or next step | ActionIntention |
| BAR, quest, daemon, fuel, Witness Note | ArtifactDispatch |

Missing, unreported, refused, ephemeral, and unavailable remain distinct values. AI inferences remain separate from player-authored reports unless explicitly adopted.

## Required representation metadata

Every TensionRepresentation or snapshot records:

- source encounter and source-report identifiers;
- report time and derivation time;
- schema and derivation-method versions;
- included and omitted fields;
- purpose and intended audience;
- field-level authorship: player-reported, mechanically derived, or AI-inferred;
- uncertainty and known limits;
- player status: draft, confirmed, corrected, rejected, superseded, or deleted;
- privacy classification, retention, and deletion behavior;
- purpose-specific permissions and permitted uses;
- downstream artifacts, adaptations, and reuse lineage.

## Privacy and purpose boundary

The council unanimously finds a material mismatch in current BARS sources:

- privacy copy says personal story and raw journal material remain ephemeral;
- persistence stores player-authored charge descriptions, life-state text, causal-hypothesis text, aligned action, and mask identity;
- persistence may automatically create a witness BAR, unlock an object, update daemon history, or merge material into matching NPC state.

Structured JSON is still potentially intimate narrative data. Structural extraction is not anonymization.

The ontology must distinguish permission for:

1. in-session collection;
2. local or server processing;
3. persistence;
4. structural derivation;
5. explanation to the player;
6. BAR, quest, daemon, story, or Witness Note generation;
7. personalization;
8. NPC or world adaptation;
9. collective fuel or aggregation;
10. display, sharing, or publication;
11. analytics, evaluation, or model improvement;
12. retention, correction, deletion, and revocation.

Consent to one purpose does not authorize another. Correction or revocation must remain connected to affected derived outputs. Data minimization can require deleting sensitive content while retaining only a non-content audit of deletion.

## Hard invariants

1. A representation is not identical to lived experience.
2. A report is evidence of what was reported, not proof of timeless truth.
3. A snapshot is what was stored, not proof of a complete representation.
4. `rootCause` cannot be treated as established causation.
5. Transformation material cannot be folded into a dissatisfied-only configuration.
6. Desire is not achieved satisfaction.
7. Action intention is not action; artifact existence is not consequence.
8. Completing a dialogue or producing an artifact does not prove transformation.
9. No-shift, unclear, refusal, and unsatisfying are valid findings.
10. Player correction, rejection, redaction, and deletion must be possible without diagnosing resistance.
11. A later representation revises or supersedes an earlier snapshot; it does not reveal one final hidden state.
12. Inference must not silently become player-authored meaning.
13. Derived structure may remain private, identifying, and sensitive.
14. Permission for collection or one dispatch does not authorize unrelated reuse.
15. No representation may claim direction, magnitude, or target coordinates it does not encode.
16. Shared or relational tension must preserve individual reports, negotiated meaning, disagreement, and separate consent.

## Required canon and implementation follow-up

1. Revise `specs/doctrine/emotional-alchemy-321.md` so TensionVector represents reports about dissatisfaction rather than claiming identity with the state.
2. Move `integrationShift` out of the source configuration.
3. Replace or reinterpret `rootCause` as a player causal hypothesis.
4. Distinguish the ideal doctrinal structure from the exact persisted snapshot.
5. Correct privacy copy to disclose the fields and downstream purposes actually in use.
6. Audit `Shadow321Runner`, `persist321Session`, metadata derivation, artifact generation, NPC merges, and analytics against purpose-specific permissions.
7. Preserve legacy data and identifiers through explicit adapters; do not mechanically rename code or rewrite stored history.
8. Test player rejection, no-shift, stale snapshots, correction propagation, deletion, artifact-without-satisfaction, and unauthorized purpose switching.

## Superseded ratification referral

The council initially referred the final naming choice to Wendell. Wendell correctly returned the answerable question to the council. The final ruling retires bare `TensionVector`, adopts `TensionConfiguration`, `TensionSnapshot`, `TransformationTrace`, and player-facing **Tension Map**, and preserves `BARS321TensionVector` only as a deprecated compatibility alias. See `council-decision.md`.
