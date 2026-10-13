# Six–Game Master Council Decision — Tension Representation

**Decision date:** 2026-10-12
**Status:** Final council ruling
**Supersedes:** `council-recommendation.md` owner-ratification referral

## Governing principle

> **The player lives the tension. The system may preserve a correctable Tension Map of what was reported. Transformation is recorded separately and connected through a TransformationTrace.**

## Binding vocabulary

- **LivedTension:** the embodied, emotional, relational, interpretive, and situational phenomenon; never a system-owned data object.
- **TensionReport:** a time-bound expression, selection, somatic report, correction, silence, uncertainty, or refusal.
- **TensionRepresentation:** abstract parent for structured, lossy, purpose-bound interpretations derived from reports.
- **TensionConfiguration:** canonical formal representation of the dissatisfied configuration at a declared derivation point.
- **TensionSnapshot:** the exact fields persisted at a named time and schema version.
- **TransformationRecord:** evidence of shift, no-shift, uncertainty, refusal, or changed interpretation.
- **TransformationTrace:** provenance connecting any subset of configuration, practice, transformation finding, satisfaction, intention, action, artifact, and consequence.
- **Tension Map:** default player-facing name for a TensionConfiguration.

`TransformationTrace` does not require successful movement or a destination. It may end in no-shift, uncertainty, refusal, rest, or nondispatch.

## TensionVector disposition

Bare `TensionVector` is retired from new formal schemas, prompts, retrieval keys, and player-facing language.

`BARS321TensionVector` is a deprecated, namespaced compatibility alias:

```text
BARS321TensionVector
  legacy_alias_of → TensionConfiguration
```

It names only the dissatisfied configuration reconstructed through the BARS 3-2-1 practice. It never names lived tension, the full session, a transformation path, action, artifact, or proof of transformation.

Historical quotations and implementation identifiers may retain the old term when labeled legacy. A future quantitative vector requires declared coordinates, units, magnitude, direction, derivation, uncertainty, and permitted operations under a new type.

## Field disposition

| Existing material | Canonical home |
|---|---|
| mask name and shape | MaskMetaphor linked to TensionConfiguration |
| desire and desired outcome | attraction or desired-outcome TensionReports |
| fear | feared-outcome TensionReport |
| life state | contextual TensionReport |
| `rootCause` | `playerCausalHypothesis`; never established cause |
| interior voice | player-authored TensionReport produced through PartPerformance |
| somatic echo | SomaticReport |
| desired feeling | DesiredStateReport |
| `integrationShift` | TransformationRecord |
| selected Basic Move or next step | ActionIntention |
| completed action | ActionRecord |
| BAR, quest, daemon, fuel contribution, Witness Note | ArtifactDispatch |
| later effect | ConsequenceRecord |

Missing, refused, ephemeral, unavailable, and uncollected remain distinct. AI inference remains separate from player report unless the player explicitly adopts it.

## Representation requirements

Every TensionRepresentation or TensionSnapshot records:

- source encounter and source reports;
- report and derivation times;
- schema and derivation versions;
- included and omitted fields;
- purpose and audience;
- field authorship: player-reported, mechanically derived, or AI-inferred;
- uncertainty and limits;
- confirmation state: draft, confirmed, corrected, rejected, superseded, or deleted;
- privacy class, retention, deletion, and revocation behavior;
- permitted uses;
- downstream-output lineage.

## Privacy and purpose ruling

Structured extraction is not anonymization. JSON, tags, and summaries may still contain intimate narrative data.

Permissions are separate for collection, local processing, persistence, derivation, explanation, artifact generation, personalization, NPC/world adaptation, collective aggregation, sharing, analytics, evaluation, model improvement, retention, correction, deletion, and revocation.

Defaults:

- session processing does not authorize persistence;
- persistence does not authorize artifact generation;
- artifact choice authorizes only the selected dispatch;
- NPC/world adaptation, collective reuse, analytics, and model improvement default off and require separate affirmative permission;
- sharing and publication require separate permission;
- correction, rejection, deletion, and revoked permission propagate through lineage to affected outputs wherever technically possible.

The current coupling inside `persist321Session()` is not treated as evidence of valid permission. Witness-BAR creation, blessed-object effects, daemon history, NPC merging, and other reuse require their own purpose and permission.

## Retrieval and migration

1. New ontology records use the binding vocabulary above.
2. A bare legacy `TensionVector` query resolves to `BARS321TensionVector`, never to TransformationTrace.
3. Retrieval distinguishes doctrinal ideal, temporary encounter answers, exact persisted snapshot, derived representation, and downstream outputs.
4. Legacy data remains immutable provenance and is interpreted through adapters rather than global renaming.
5. Existing snapshots receive their actual field manifest and `contains_verbatim_player_text` status.
6. `rootCause` maps semantically to `playerCausalHypothesis` without rewriting the player’s words.
7. `integrationShift` maps to TransformationRecord only when present.
8. Missing fields are never inferred or backfilled merely to satisfy the new model.
9. New writes use canonical types; compatibility emission is limited to declared legacy consumers.
10. Legacy records without affirmative purpose permission remain private and purpose-frozen rather than receiving invented retrospective consent.

## Hard invariants

1. Representation is not identical to lived experience.
2. Reported meaning is not timeless or exhaustive truth.
3. Snapshot is not a complete configuration unless its manifest demonstrates that scope.
4. Player causal hypothesis is not established causation.
5. Transformation does not belong inside the source configuration.
6. Desire is not achieved satisfaction.
7. Action intention is not action; artifact is not consequence.
8. Dialogue completion and artifact production do not prove transformation.
9. No-shift, uncertainty, refusal, and unsatisfying results remain valid.
10. Correction, rejection, redaction, and deletion must not be diagnosed as resistance.
11. Later representations do not reveal one final hidden state.
12. AI inference does not silently become player-authored meaning.
13. Derived structure may remain private, sensitive, and identifying.
14. Permission for one purpose does not authorize another.
15. Relational tension preserves individual reports, negotiated shared meaning, disagreement, and separate consent.

## Required BARS follow-up

- revise 3-2-1 doctrine and privacy copy;
- separate source configuration from transformation evidence;
- audit actual persisted fields and their sensitivity;
- decouple persistence from unrelated downstream effects;
- add purpose-specific permission, correction, deletion, and lineage behavior;
- migrate with adapters and tests rather than mechanical renaming.

This decision settles the ontology and naming question. It does not itself authorize a code or data migration.
