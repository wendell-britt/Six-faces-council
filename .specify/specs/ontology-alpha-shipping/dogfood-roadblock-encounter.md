# Dogfood design brief: Fictional Roadblock Encounter

**Status:** implementation-ready alpha specification; implementation unverified

**Purpose:** exercise the current game-design ontology through one small feature without processing real personal data

## `design_intent`

Create a solo or facilitated fictional encounter in which a traveler meets an obstruction on the way to a chosen destination, tests or declines one route, and leaves with their own account of what happened. The encounter validates the ontology's ability to guide an implementation-ready feature while preserving evidence, consent, refusal, and lifecycle boundaries.

## `intrinsic_pleasure`

The leading pleasure is gentle symbolic inference: combining destination, obstruction, conditions, and route into an unexpectedly apt little story while retaining the power to say “none of those.” Supporting pleasures are genuine route choice, precise naming of fictional conditions, and keeping or releasing a well-made trace. The designer and Game Master also play by composing evocative fixtures and discovering unanticipated routes.

## Player-facing invitation

> Something is in the way of a move your fictional traveler wants to make. You do not have to explain why, disclose anything personal, or defeat it. Choose a preset, symbolic, or self-authored in-world roadblock. We will show what it blocks under these conditions, offer possible routes, and let you test one, rest, refuse, or leave it unresolved. You may correct the premise, change the example, keep no record, or end at any time.

## `ontology_objects`

- `EncounterDefinition`: versioned four-beat contract;
- `EncounterOccurrence`: one transient fictional run;
- `DestinationClaim`: authored for the fictional traveler;
- `RoadblockEvent`: constrained action or route under stated fictional conditions;
- optional correctable `RoadblockClassification`;
- optional scoped `RoadblockCausalAccount`;
- optional, separately granted `IntentionAlignmentHypothesis` about a declared fictional intention;
- two sourced `DerivedMovementProposal` records;
- optional `MovementRoutingPlan` for the selected route;
- `MoveResolutionRecord` for an invoked fictional action;
- player-selected `MovementFinding`;
- `EncounterEndRecord` with ending and resumability separate;
- optional `ArtifactDispatch` for a Route Card;
- `PermissionEnvelope`, `DerivationRecord`, and discard/deletion disposition.

No artifact automatically becomes a BAR. No finding automatically creates a TransformationRecord.

## Smallest playable loop

1. **Choose a destination.** Select a preset, choose a symbol, or enter one short fictional in-world destination.
2. **Place the obstruction.** Select or author one fictional condition and complete: “This prevents the traveler from ___ under ___.”
3. **Meet the routes.** Receive two visibly labeled proposals assembled from current fictional fields. Always retain Correct, Rest, Refuse, and Leave unresolved.
4. **Close the encounter.** Select one route and resolve one observable fictional action, or take an exit. Select a finding or leave it unassessed. End the encounter. Separately accept or decline artifact generation and saving.

## State contract

```text
READY -> ORIENTED -> BLOCKED -> ROUTES_OFFERED

ROUTES_OFFERED -> ROUTE_SELECTED -> MOVE_RESOLVED -> ENCOUNTER_ENDED
ROUTES_OFFERED -> RESTED -> ENCOUNTER_ENDED
ROUTES_OFFERED -> REFUSED -> ENCOUNTER_ENDED
ROUTES_OFFERED -> LEFT_UNRESOLVED -> ENCOUNTER_ENDED

After ENCOUNTER_ENDED, independently:
  movement_finding = shift | no_shift | uncertain | reinterpretation | refusal | unassessed
  artifact_disposition = saved | declined | not_offered
  persistence = none | artifact_only_explicit
```

There is no `quest_completed` field in this slice. `MOVE_RESOLVED` does not imply shift. `ENCOUNTER_ENDED` does not imply completion, satisfaction, development, or transformation.

## Inputs and outputs

Inputs are enumerated fictional fixture IDs and optional capped in-world phrases. Self-authored fields say “fiction only—do not enter real names or personal history.” Alpha fixtures cover fantasy, science-fiction, and everyday-folktale situations.

Required output records include encounter version, authored destination, scoped roadblock, sourced route proposals, selected response or exit, move result when invoked, ending, player-selected or unassessed finding, permission state, and discard disposition.

The optional Route Card contains only fictional inputs, chosen route or exit, named evidence cue, and fictional consequence. It uses the same craft quality for every finding and proves only that an artifact was created.

## `mechanical_claims`

The game treats destination authorship, scoped constraint, route choice, correction, refusal, rest, observable fictional action, and player-selected finding as real. It rewards neither intimacy nor forward motion. It remembers nothing by default and changes only the fictional scene and encounter lifecycle.

## `aqal_attention`

- **UL / I:** curiosity, relief, uncertainty, or resonance may be invited; meaning remains player-authored and optional.
- **UR / It:** selections, correction, action, rest/refusal, and artifact choice are observable; motive is not.
- **LL / We:** facilitator language, witness boundaries, shared respect for correction, and permissions for participation.
- **LR / Its:** state reducer, fixture/version sources, purpose gates, lineage, end-state truth, and deletion behavior.
- **Developmental line:** situated route-finding only; no whole-person development claim.
- **States invited:** curiosity, imaginative distance, and ambiguity tolerance; none becomes a trait.
- **Favored or burdened types:** symbolic-system lovers are favored. Presets, plain labels, concise/nonverbal routes, and no performance scoring reduce language and imagination burdens. Culturally fixed symbolism remains a test risk.
- **Outside scope:** therapy, diagnosis, clinical use, real-life assessment, psychography, persistent progression, allyship-effect claims, and real transformation evidence.

## `agency_and_consent`

Transient processing of fictional encounter fields is disclosed before play. Persistence, personalization, sharing or visibility, export, analytics or evaluation, and model improvement are separate and default off. Publication and model improvement are prohibited in this slice. Artifact generation and artifact saving are separate choices. Declining interpretation, action, artifact, or saving preserves the same core quality and access.

A facilitator or witness may state observable action or their own experience. They may not define the focal player's motive, inward truth, readiness, or transformation. Silent witness, factual reflection, offering options, and joining a move require distinct situated permission.

## `evidence_and_unknowns`

System traces establish only fictional selections and transitions. A player-selected finding establishes that reported finding for this encounter, not an inner fact or durable capability. An artifact establishes only that an artifact was generated or saved.

Unknowns include felt resonance, accessibility across symbolic traditions, whether route proposals feel meaningfully distinct, whether facilitators privilege action, and whether the resulting brief is useful outside the design team. No fictional run establishes real-world efficacy.

## `provenance_effects`

Every proposal records encounter version, rule-table version, destination and obstruction sources, included and omitted fields, and derivation rationale. Corrections append and invalidate unused descendants rather than silently rewriting them. A saved Route Card points to its fictional sources and permission scope. Generation never removes inherited restrictions.

## `risks_and_tests`

1. Observation becomes diagnosis: a closed bridge must not imply fear or resistance.
2. Optional interpretation becomes compulsory: refusal must preserve equal craft and every non-interpretive response.
3. Permission purposes collapse: transient processing must not enable save, personalization, sharing, export, analytics, publication, or model improvement.
4. Correction is decorative: rejected or corrected proposals must stop shaping active state and descendants.
5. Ending states collapse: rest, refusal, interruption, timeout, and suspension must not prove repair, quest completion, satisfaction, or transformation.
6. Recoverability becomes self-sealing: a useful clue may coexist with an unresolved blocker.
7. No-data promise is false: runtime and logs contain only fixture IDs, fictional choices, permitted operational events, and explicitly saved fictional records.
8. Fiction launders permission: generated world descendants remain bound by source envelopes.
9. Disclosure changes quality: preset-only and self-authored routes receive equal choice, craft, and access.
10. Genre assumptions leak into schema: all fixture genres use the same contract without mandatory character advancement or GM authority.

## `implementation_translation`

Build as a local screen or CLI flow using fixed YAML/JSON fixtures and a pure reducer. Minimum modules are encounter definition, state reducer, deterministic proposal builder, permission gate, trace serializer, optional artifact renderer, and semantic fixture suite. No LLM is required for the alpha slice.

The interface always exposes Correct, Rest, Refuse, and Leave unresolved alongside route actions. Permission checks sit at operation boundaries, not only in copy. The serializer defaults to memory-only and may emit a synthetic redacted trace in tests. Rewards attach to participation or fictional consequence, never disclosure or acceptance of an interpretation.

Minimum acceptance payload:

```yaml
ending_mode: resolved | rested | refused | left_unresolved | interrupted | suspended
blocker_status: resolved | partially_resolved | unresolved | unassessed
move_result: succeeded | failed | mixed | not_invoked
movement_finding: shift | no_shift | uncertain | reinterpretation | refusal | unassessed
artifact_disposition: saved | declined | not_offered
persistence: none | artifact_only_explicit
```

Each axis validates independently.

## `decision_or_open_authority`

The council may approve this bounded dogfood specification without owner escalation. It uses only fictional data, creates no canonical prose, and settles no unresolved ontology boundary. Poetic title, world skin, fixture prose, and artifact name remain provisional implementation copy.
