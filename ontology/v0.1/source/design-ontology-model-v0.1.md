# Design Ontology Model — v0.1

**Owner:** Wendell Britt
**Status:** Provisional formal model
**Companion philosophy:** `design-philosophy-draft-v0.1.md`
**Machine-readable seed:** `design-ontology-v0.1.yaml`

## 1. Purpose

This model turns the design philosophy into a vocabulary AI collaborators and Game Master agents can use to describe, compare, generate, test, and revise designs.

It defines entities, relationships, evidence authority, provenance, confidence, lifecycle states, and hard constraints. It does not yet select the smallest operational subset or assign concepts to active, reference, or compost sets.

## 2. Modeling commitments

1. **Model claims, not unquestionable truths.** Every substantive assertion has provenance, scope, evidence, interpretation, confidence, and contestability.
2. **Keep perspectives distinguishable.** First-person experience, observed behavior, shared meaning, and systemic consequence may concern one event without becoming interchangeable evidence.
3. **Represent development contextually.** The ontology can record development within a line, domain, relationship, and context; it cannot rank the whole person.
4. **Preserve every center of agency.** A beneficiary cannot unilaterally define trust, consent, or relationship state when another agent is affected.
5. **Keep interpretations smaller than their subjects.** Multiple interpretations and disagreement may coexist. AI inference cannot replace player-authored inner meaning.
6. **Treat provenance as part of meaning.** The path from seed through action, relationship, transformation, and result belongs to the design object.

### 2.1 Constitutional collections and succession

The ontology recognizes two versioned constitutional collections:

- **eight-principle constitutional seed:** the original collection in `design-ontology-six-face-council-brief.md`;
- **fifteen-principle provisional v0.1 constitution:** the current collection in `design-philosophy-draft-v0.1.md`.

The v0.1 collection `amends_and_expands` the seed. The seed remains historical and provenance-bearing; it is not a co-equal operative alternative. Unqualified current retrieval returns the fifteen. Historical and comparative retrieval preserves both collections and the principle-level lineage map.

The inherited mapping is seed P1–P4 to v0.1 P1–P4 and seed P5–P8 to v0.1 P12–P15. Current P5–P11 are additions produced through the recorded excavation, extraction, and translation process.

## 3. Entity families

### 3.1 Agent

An **Agent** can act, interpret, permit, refuse, or experience consequences.

Roles: Designer, GameMaster, Player, Ally, Helper, AI, Group, Institution, and WorldAgent. One agent may hold several roles; roles do not establish rank.

### 3.2 DesignObject

Something constructed or proposed for play.

Types: Game, DesignTool, Mechanic, Rule, NarrativeElement, CharacterRole, WorldElement, AdaptiveSystem, MotivationMechanism, Credential, Interface, Ritual, Prompt, and ArtifactTemplate.

### 3.3 PlayUnit

A **PlayUnit** distinguishes designed definitions from occurrences in play.

- Definitions: EncounterDefinition, MoveDefinition, QuestDefinition, ArcDefinition, and CompletionContract;
- Occurrences: Session, EncounterOccurrence, MoveInvocation, PracticeInstance, QuestInstance, ArcInstance, and CampaignInstance;
- Transition records: ParticipantExitRecord, EncounterEndRecord, MoveResolutionRecord, QuestDispositionRecord, ArcConclusionRecord, InterruptionRecord, Checkpoint, and ContinuationRecord;
- Claims: CompletionClaim, ResolutionClaim, QuestCompletionClaim, and TransformationClaim.

The common RPG ordering—campaign, arc, quest, encounter, move—is a graph, not a mandatory containment tree. An encounter may advance several quests, a quest may span encounters, and meaningful encounters may exist without quests or authored arcs.

### 3.4 PhilosophyObject

An expression of design meaning or constraint.

Types: ConstitutionalPrinciple, ProvisionalCommitment, AestheticPattern, Polarity, AntiPattern, DesignQuestion, Guardrail, VerificationRule, FrameworkLens, and FrameworkBoundary.

### 3.5 DevelopmentObject

- **DevelopmentLine:** a distinct domain of capacity;
- **Capability:** a situated ability that changes possible action;
- **Affordance:** an action or path available through the interaction of agent and context;
- **Permission:** authorization granted, withheld, conditioned, or revoked;
- **Commitment:** a promise, responsibility, or declared constraint tested over time;
- **Credential:** a contextual representation of demonstrated capability, never the capability itself;
- **DevelopmentClaim:** a claim that possibility changed within a specified line and context.

### 3.6 ExperientialObject

- **Charge:** emotionally or somatically salient energy, tension, attraction, or resistance;
- **LivedTension:** the person’s embodied, emotional, relational, interpretive, and situational phenomenon, which no system record exhausts;
- **State:** a temporary condition invited or encountered in play;
- **Performance:** an enacted form, whether or not it expresses stable identity;
- **Action:** a consequential choice or behavior;
- **ExperienceEvent:** an occurrence joining agents, actions, world state, and responses;
- **Transformation:** a change in relationship to charge, meaning, capacity, action, or artifact;
- **Outcome:** an immediate result;
- **Consequence:** a later change in possibility, relationship, interpretation, or world state;
- **SomaticReport:** first-person bodily evidence;
- **SatisfactionReport:** first-person evidence about an Emotional Alchemy result;
- **DesiredStateReport:** a reported desired state, not evidence that the state was reached;
- **ActionIntention:** a contemplated or selected action, distinct from action performed;
- **TransformationRecord:** evidence of shift, no-shift, uncertainty, refusal, or reinterpretation.

### 3.7 RelationalObject

- **Relationship:** an evolving field among distinct agents;
- **TrustState:** situated evidence of capability and integrity within a relationship and domain;
- **ConsentRecord:** permission, purpose, duration, audience, and revocation conditions;
- **Boundary:** a limit on access, obligation, interpretation, action, or disclosure;
- **Repair:** a process addressing breach without presuming restoration;
- **CoordinationPattern:** a capacity existing among agents rather than inside one;
- **SharedMeaning:** negotiated meaning that need not replace personal meaning.
- **PurposePermission:** authorization binding a data category to a specific collection, persistence, derivation, reuse, audience, retention, or deletion purpose.

### 3.8 EpistemicObject

Types: Claim, Observation, Interpretation, Hypothesis, EvidenceItem, TensionReport, TensionRepresentation, TensionConfiguration, DerivedMovementProposal, MovementFinding, DestinationClaim, RouteHypothesis, Uncertainty, Disagreement, Finding, and Test.

Observation remains separate from interpretation. A hypothesis includes predicted implications. Disagreement is retained as information rather than forced into premature consensus.

### 3.9 ProvenanceObject

Types: Source, ProvenanceRecord, Artifact, Seed, Revision, LifecycleRecord, CompostRecord, TensionSnapshot, TransformationTrace, MovementSourceReport, MovementRoutingPlan, MovementRoutingAssignment, DivergenceRecord, BlockerRecord, RecoverabilityPath, ArtifactDispatch, ActionRecord, and ConsequenceRecord.

A CompostRecord preserves what was released, why, what learning remains, and what may nourish later work.

### 3.10 PsychographicObject

Types: Psychograph, TypePreference, DesiredState, PleasureSignature, DesignShadow, AccessibilityNeed, and AudienceHypothesis.

A psychograph is a revisable design-relevant configuration, not a diagnosis.

### 3.11 FaceNamespaceObject

The word “face” spans several environments that share symbols without sharing identity, authority, or data semantics.

- **GameMasterArchetype:** the shared symbolic lineage of Shaman, Challenger, Regent, Architect, Diplomat, and Sage;
- **AltitudeFace:** an explicitly scoped interpretation within a developmental framework;
- **SectDefinition:** a player-facing thematic school, mission, ethos, and symbolic vocabulary;
- **RuntimeSect:** an executable AI role with configured tools, prompts, and routing;
- **PlayerSectIdentity:** a player’s consented and revisable relation to a sect definition;
- **ReviewDiscipline:** a functional spec-review responsibility such as Ontologist, Systems Architect, Experience Designer, Encounter Designer, Steward, or Integrator;
- **CouncilLens:** a bounded epistemic stance used for multi-lens inquiry;
- **LensInvocation:** one contextual use of a CouncilLens by an agent or person;
- **PhaseVoiceAssignment:** a local phase-to-voice binding that records the voice’s source namespace.

These are distinct record types. A shared archetype key creates correspondence, not identity or inherited authority.

## 4. Relationship vocabulary

### Authorship and participation

`authors`, `co_authors`, `plays`, `facilitates`, `seeds`, `transforms`, `stewards`, `witnesses`

### Mechanical attention

`makes_mechanically_real`, `supports_narratively`, `supports_socially`, `leaves_implicit`, `excludes_from_scope`, `favors_type`, `burdens_type`, `invites_state`

### Development and consequence

`develops`, `belongs_to_line`, `demonstrated_in`, `enables`, `constrains`, `changes_possibility`, `produces`, `leads_to`, `transfers_to`

### Relationship and permission

`relates`, `grants`, `withholds`, `revokes`, `requires_consent_from`, `keeps`, `breaches`, `repairs`, `coordinates_with`

### Evidence and interpretation

`observes`, `interprets`, `authors_personal_meaning`, `supports`, `challenges`, `complicates`, `predicts`, `tested_by`, `finds`, `revises`, `disagrees_with`

### Provenance and lifecycle

`derived_from`, `preserves_trace_of`, `records_path`, `supersedes`, `rests`, `activates`, `references`, `composts`

### Constitutional versioning

`member_of_constitution`, `inherits_principle`, `amends_and_expands`, `current_successor_of`

### Face namespaces

`draws_from_archetype`, `interprets_archetype_as_altitude`, `makes_playable`, `dramatizes`, `operationalizes`, `affiliated_with`, `invokes_lens`, `performed_by`, `routes_to_runtime`, `reviewed_by`, `supports_review`, `bound_to_phase`, `shares_face_key_with`, `claims_altitude`

Cross-namespace relations are typed, scoped, and provenance-bearing. Matching labels never imply `same_as`.

### Motivation and risk

`motivates`, `supports_purpose`, `risks`, `guarded_by`, `exhibits_proxy_capture`

### Representation and transformation lineage

`reports_on`, `represents`, `derived_from_reports`, `snapshot_of`, `proposes_movement`, `routes_design_unit`, `invites_movement`, `records_reported_shift`, `records_no_shift`, `proposes_cause`, `targets_state`, `selects_action`, `dispatches_artifact`, `reused_for`, `revises`, `rejects_representation`, `rejects_proposal`, `supersedes_snapshot`, `supersedes_proposal`, `derived_output_of`, `affected_by_correction`

### Route, divergence, and recoverability

`authors_destination`, `proposes_route`, `advances_destination`, `diverges_from_route`, `constrains_route`, `revises_destination`, `releases_destination`, `offers_recoverability`, `routes_around`, `leaves_unresolved`, `repairs_consequence`

### Play lifecycle and scope

`participates_in`, `occurs_within`, `invokes`, `ends`, `exits`, `refuses`, `rests`, `retreats_from`, `interrupts`, `suspends`, `resumes`, `resolves`, `completes`, `fails`, `expires`, `abandons`, `advances`, `blocks`, `concludes`, `reopens`, `continues_in`, `satisfies_condition_of`, `contributes_evidence_to`

## 5. Evidence model

Every EvidenceItem records its type, source, subject, addressed claim, AQAL perspective, context, developmental line, time, direct content, privacy scope, evidential relationship, and known limits.

| Evidence type | Can establish | Cannot establish alone |
|---|---|---|
| Player statement | Reported meaning, satisfaction, intention, or experience | External effect, permanent trait, another agent’s experience |
| Somatic report | Reported sensation and perceived change | One correct interpretation or external truth |
| Behavioral observation | Enacted behavior under observed conditions | Inner meaning, motive, or global capability |
| Relational attestation | Another agent’s experience of consent, trust, coordination, or harm | The first agent’s inner meaning or universal reputation |
| System trace | Recorded action, state transition, permission, or resource effect | Why it mattered or whether it satisfied |
| Persistent artifact | Evidence that something was produced or preserved | Complete process, motive, or meaning |
| Research source | Claims within that source’s authority | Wendell’s response or universal applicability |
| AI inference | A proposed connection, question, or hypothesis | Personal truth, consent, or final authority |
| Council synthesis | Convergence or disagreement among lenses | Empirical verification or ratification |
| Playtest finding | What occurred for specified players and conditions | Universal validity outside the tested scope |

## 6. Claim and confidence model

Confidence is a profile, not a single score. Every Claim includes:

- scope and applicable contexts;
- source proximity: direct report, direct observation, derived evidence, or inference;
- evidence diversity;
- repeatability: untested, single instance, repeated in context, or transferred across contexts;
- contestation: uncontested, alternatives present, actively disputed, or contradicted;
- interpretive distance: observation, interpretation, synthesis, or speculation;
- epistemic maturity;
- confidence label: unknown, tentative, plausible, supported, or strong-within-scope;
- known limits.

Rules:

1. A user statement is authoritative about the user’s stated preference or meaning, not automatically about its cause.
2. An AI inference never silently becomes a user belief.
3. Council convergence raises interpretive support, not empirical certainty.
4. Repetition increases confidence only within comparable contexts.
5. Conflicting evidence is retained and narrows or complicates the claim.
6. Strong-within-scope never permits whole-person or universal generalization.

## 7. Development model

A DevelopmentClaim specifies:

- the subject: agent, relationship, group, or system;
- the development line;
- prior and current possibilities;
- context;
- evidence and perspective;
- provenance;
- uncertainty;
- whether it concerns transformation validity, application fitness, or both.

> **Development is a contextual change in possibility, never an aggregate measure of personal worth.**

A Performance is one or more enactments. A Capability is a supported claim that a form can be enacted under defined conditions. A Credential communicates a contextual capability claim. Performance may cultivate capability without first expressing a stable identity.

## 8. Emotional Alchemy model

### 8.1 Terminology boundaries

- The five **Basic Moves** are Wake Up, Open Up, Clean Up, Grow Up, and Show Up.
- **WAVE** is reserved for the Open Up breathing practice.
- `Wake → Clean → Grow → Show` is the **within-channel progression**; it is not called WAVE.
- The five Transcend, five Generative, and five Control moves form the **fifteen canonical Emotional Alchemy moves**.

These structures may relate in practice but must remain distinct in records, retrieval, and prompts. The steps and acronym expansion of the WAVE breathing practice are not yet specified in this model.

### 8.2 General evidence sequence

The sequence is:

> Charge → Attention or practice → Transformation → Satisfaction evidence → Capacity, action, relationship, or artifact → Consequence

Not every sequence must reach every term.

For self-directed use, the player’s SatisfactionReport has primary authority over transformation validity. Unchanged, unclear, or unsatisfying results remain valid findings.

For allyship, application requires appropriate consent. Relational attestation and observable consequences inform application fitness. Harm may constrain a particular intervention without invalidating the helper’s entire transformation.

### 8.3 Tension representation boundary

The player lives the tension. The system may preserve a correctable **Tension Map** of what was reported.

- `TensionRepresentation` is the abstract parent for lossy, purpose-bound interpretations derived from reports.
- `TensionConfiguration` is the formal dissatisfied configuration at a declared derivation point.
- `TensionSnapshot` records exactly what was persisted, including omissions and verbatim-text sensitivity.
- `TransformationTrace` connects any subset of configuration, practice, TransformationRecord, SatisfactionReport, ActionIntention, ActionRecord, ArtifactDispatch, and ConsequenceRecord. It may end in no-shift, uncertainty, refusal, rest, or nondispatch.
- `BARS321TensionVector` is a deprecated compatibility alias for a BARS 3-2-1 TensionConfiguration. Bare `TensionVector` is retired from new schemas, prompts, retrieval keys, and player-facing language.

`rootCause` is interpreted as `playerCausalHypothesis`, never established causation. `integrationShift` belongs to TransformationRecord; aligned action belongs to ActionIntention; artifact creation and consequence remain downstream.

Every representation records source reports and encounter, schema and derivation versions, included and omitted fields, purpose, audience, field authorship, uncertainty, player confirmation/correction/rejection status, privacy and retention rules, permitted uses, and downstream lineage.

Session processing, persistence, artifact generation, personalization, NPC/world adaptation, collective reuse, sharing, analytics, and model improvement are separate permission purposes. Structured extraction is not anonymization.

### 8.4 Derived movement and routing authority

The legacy Epiphany-Bridge binary and the fifteen-move Emotional Alchemy grammar are separate namespaces. Legacy lowercase `translate` means integrate within the current frame and legacy lowercase `transcend` means cross a frame or structural threshold. In the fifteen-move grammar, `Translate` is cross-channel movement, while `Transcend` is within-channel altitude movement. Matching labels do not establish equivalence.

A `DerivedMovementProposal` is a correctable, versioned interpretation generated from `MovementSourceReport` records for a declared design purpose. An accepted proposal may inform a `MovementRoutingPlan`, whose assignments describe movement the authored design intends to invite. Neither object records movement that actually occurred.

Actual play may support a `MovementFinding`: reported shift, no-shift, uncertainty, reinterpretation, refusal, or unassessed. It must be linked to appropriate evidence and a TransformationRecord. It cannot be inferred from a routing assignment, node traversal, quest completion, artifact, or engagement trace.

Correction preserves provenance, stops future use of a rejected proposal, invalidates or flags unpublished descendants, versions published descendants, and leaves completed play as historical fact without preserving the rejected interpretation as player truth. Deletion, revocation, and purpose restrictions propagate through the recorded downstream lineage.

### 8.5 Yellow Brick Road and recoverability

The Yellow Brick Road is a mythic orientation and recoverability covenant, not a metaphysical assertion or operational guarantee. Its precise rule is: **no path has to be wasted**.

A DestinationClaim preserves Point B and its author. A RouteHypothesis remains falsifiable. A DivergenceRecord does not decide whether divergence was discovery, evolution, error, failure, escape, or noise. A BlockerRecord names what is constrained without presuming an internal cause or duty to metabolize. A RecoverabilityPath may offer learning, retry, repair, assistance, accommodation, environmental change, another route, a revised destination, rest, unresolved preservation, abandonment, or composting.

Some blockers may remain unresolved indefinitely. An unresolved blocker may still prevent a particular route or quest from completing. Changing or releasing the destination is valid, but it does not retroactively fulfill the earlier DestinationClaim. Learning from harm or error never makes it necessary, correct, or reversible.

### 8.6 Roadblock observation and intention hypotheses

A `RoadblockEvent` is an evidence-bearing specialization of BlockerRecord: it records that a named action, route, capacity, or destination is constrained under declared conditions. The event does not establish motive, emotional state, developmental level, resistance, hidden desire, or misaligned intention.

A `RoadblockClassification` may be technical, dependency, resource, coordination, capability, environmental, relational, emotional/interpretive, safety/ethical, unknown, or multi-causal. A separate `RoadblockCausalAccount` distinguishes correlation, contributing condition, proximate cause, root-cause hypothesis, and cause verified within a declared test scope.

An `IntentionAlignmentHypothesis` is a correctable interpretation comparing a declared intention with a relevant method, condition, capacity, permission, or consequence. Its governing rule is: **a roadblock may reveal a mismatch among intention, method, conditions, and capacity; it does not prove misaligned intention.** The hypothesis records whose intention is represented, its author, supporting and contradicting evidence, uncertainty, and confirmation or rejection status. AI inference remains proposal-only.

A `RoadblockResponse` may repair, retry, test, request help, accommodate, alter the environment, acquire capability, renegotiate, reroute, pause, rest, accept, leave unresolved, set down, abandon, or compost. A `MetabolizationOutcome` records reusable repair, verification, learning, or provenance. Technical metabolization does not imply emotional processing; experiential metabolization is valid only according to the represented person's evidence.

### 8.7 Session depth, practice performance, and artifact tailoring

The legacy future `SessionDepthSignal` does not measure inner depth. `ResponseMaterial` records what the player supplied in a permitted modality. A correctable `ResponseAffordanceProfile` identifies relevant specificity, constraints, relationships, examples, ambiguity, imagery, modality coverage, and preserved omissions for a declared purpose. Character count establishes only character count.

A `PracticePerformanceRecord` records observable action against an explicit move or encounter contract. Performance can be gameplay: it may create capacity, story, relationship, and consequence. It does not establish genuineness, vulnerability, transformation, readiness, or whole-person development.

A `DepthClaim` always names its scope and evidence authority. Player-reported experiential depth, design resolution depth, interpretive complexity, relational depth, artifact specificity, and demonstrated deftness are distinct claims. A `DeftnessFinding` requires repeated relevant performance evidence.

An `ArtifactTailoringPlan` uses permitted ResponseMaterial under an `InputSufficiencyContract`. Artifact specificity, richness dimensions, quality, and fit remain separate. More usable material can support more specific tailoring but cannot purchase better baseline craft, core progress, power, credentials, or social standing. `ArtifactFitFinding` relies on the relevant player, recipient, artifact criteria, or external consequence evidence.

Disclosure volume and intimacy are not progression currency. Equivalent expressive routes and a quality floor protect concise, private, second-language, disabled, neurodivergent, culturally guarded, symbolic, fictionalized, and nonverbal participation. A `PacingAdaptationProposal` remains visible, reversible, and player-correctable.

## 9. Encounter ending and scoped completion

Ending, resolution, quest completion, arc conclusion, satisfaction, and transformation are distinct claims.

- A **participant exits** when that agent’s active participation stops.
- A **session ends or suspends** when the current period of play stops.
- An **encounter ends or suspends** when its bounded field of immediate participation stops or pauses.
- A **move invocation resolves** when its procedure produces a result; failure can be fully resolved.
- A **quest completes** only when its declared completion conditions are met.
- A quest may instead fail, expire, be declined, abandoned, superseded, or composted. These are named quest dispositions, not forms of quest completion.
- An **arc concludes** when its larger trajectory receives an ending; it may retain open or disputed threads.
- A **transformation claim** requires appropriate experiential evidence and cannot be inferred from another lifecycle transition.

Every CompletionClaim identifies its target scope, CompletionContract, criteria and version, evidence, evidence authority, recognizing agent, time, uncertainty, and contestation. Bare or inherited `completed` flags are insufficient.

An EncounterDefinition may compose contest, inquiry, relational, transformational, ritual, creative, recovery, governance, or training contracts. These describe operative stakes and evidence rather than exclusive genre labels.

Independent lifecycle axes include activity, ending mode, resolution result, objective judgment, experiential finding, consent, resumability, persistence, consequence, evidence authority, and contestation. No-shift is an experiential finding rather than an ending mode.

> **Moves resolve; encounters end; quests complete; arcs conclude. None of these alone proves satisfaction, development, transformation, or worth.**

## 10. Adaptive-system model

An AdaptiveSystem distinguishes:

- observed signals;
- inferred interpretations;
- adapted content or conditions;
- permissions for collection, retention, explanation, visibility, reuse, and sharing;
- uncertainty and alternatives;
- player correction or rejection;
- effects on world otherness and player sovereignty.

> **The system may propose relevance; it may not claim final authorship of the player’s inner meaning.**

An adaptive world should retain causes, agents, histories, resistances, or emergent meanings not exhausted by the player model.

## 11. Integral declaration of mechanical attention

Every Game or DesignTool should declare:

| Field | Required content |
|---|---|
| Intended pleasure | What should be intrinsically enjoyable and for whom |
| Mechanical reality | What is tracked, differentiated, rewarded, permitted, and changed |
| Foregrounded quadrants | Primary AQAL perspectives expressed in play |
| Developmental lines | Lines made consequential |
| Implicit support | Dimensions carried through fiction, culture, or facilitation |
| Exclusions | Dimensions intentionally outside scope |
| Favored or burdened types | Psychographic and access assumptions |
| Invited states | Temporary experiences supported |
| Required complexity | Demands at entry and mastery |
| Productive tensions | Polarities intentionally held |
| Risks | Likely anti-patterns or proxy-capture paths |
| Evidence plan | How intended and actual experience will be compared |
| Exit and rest | How refusal, rest, stopping, and composting remain possible |

## 12. Lifecycle model

The ontology separates **epistemic maturity** from **work disposition**.

Epistemic maturity:

`captured → researched → excavated → candidate → translated → drafted → modeled → council_ingested → play_observed → provisionally_adopted → verified`

Any state may become revised or contested. Older forms may be superseded. Weak evidence may return a claim to an earlier maturity state.

Work dispositions are active, resting, reference, delegated, completed, compost-candidate, and composted. No ontology concepts are assigned to governance dispositions in v0.1.

## 13. Hard invariants for AI collaborators

An AI operating with this ontology must not:

1. assign a global developmental level to a person;
2. treat type as level;
3. convert access to an ally into total command;
4. infer consent from compliance, acquisition, disclosure, or continued play;
5. override player-authored inner meaning with system interpretation;
6. treat Emotional Alchemy satisfaction as proof of external helpfulness;
7. treat external approval as proof of inner transformation;
8. silently convert inference or council consensus into user belief;
9. discard contradictory evidence to preserve a clean model;
10. use engagement as sufficient evidence of meaning or benefit;
11. require every game to mechanize the entire integral ontology;
12. convert every captured possibility into implementation obligation;
13. raise a design risk without proposing a proportionate test;
14. infer move success, quest completion, arc conclusion, or transformation from encounter ending;
15. use an unqualified completion claim without its object, contract, evidence, and authority;
16. relabel refusal, rest, retreat, witnessing, interruption, or no-shift as satisfaction of an unmet action gate;
17. retroactively tighten completion criteria to prevent exit or force a preferred story;
18. exhaustively specify a game when the task is ontology development;
19. remove mystery merely to make the system easier to explain;
20. treat altitude face, runtime sect, review discipline, player sect identity, or council lens as interchangeable;
21. infer developmental altitude, whole-person worth, authority, permission, tool access, or stable identity from sect choice, agent invocation, council assignment, review responsibility, psychographic affinity, or a shared face name;
22. infer a one-to-one mapping between the named-six archetypes and the Ontologist-through-Integrator review disciplines;
23. use an unqualified face identifier when the namespace affects storage, permission, retrieval, developmental claims, or audit history.
24. treat a TensionRepresentation as identical to lived experience;
25. treat player causal hypothesis as established cause;
26. fold transformation, satisfaction, action, artifact, or consequence into a dissatisfied TensionConfiguration;
27. treat structured extraction as anonymization or as blanket authorization for reuse;
28. use bare `TensionVector` as an active formal or player-facing term;
29. infer unreported legacy fields or retrospective permission during migration.
30. treat a DerivedMovementProposal or MovementRoutingPlan as evidence that movement occurred;
31. equate the legacy binary movement grammar with the fifteen-move Emotional Alchemy grammar by shared label;
32. continue silently personalizing from a rejected or corrected movement proposal;
33. treat movement correction or rejection as resistance.
34. use Yellow Brick Road language to deny ethical wrong, failed purpose, predictive error, route mismatch, or irreversible consequence;
35. infer hidden desire from divergence;
36. retroactively fulfill an earlier DestinationClaim by silently revising Point B;
37. make continued play or metabolization obligatory because a blocker exists;
38. diagnose refusal to metabolize as resistance or as another blocker without independent evidence.
39. infer misaligned intention from a RoadblockEvent or technical fault alone;
40. collapse roadblock observation, classification, causal account, meaning, response, and outcome;
41. erase structural, environmental, relational, accessibility, or safety constraints by reframing them as inner work;
42. require emotional disclosure as a condition of technical diagnosis or repair.
43. infer session depth, genuineness, transformation, readiness, trust, or deftness from response length or intimate specificity alone;
44. treat disclosure volume, pain magnitude, or vulnerability performance as progression currency;
45. intentionally weaken a baseline artifact to pressure additional disclosure;
46. equate PracticePerformanceRecord with an inner-state or transformation finding;
47. conflate artifact specificity, richness, quality, and fit;
48. make an irreversible pacing or personalization decision from an unconfirmed behavioral proxy.

## 14. Minimum viable ontology record

Every important concept minimally records:

- stable identifier, type, name, and scoped definition;
- epistemic maturity and work disposition;
- sources and derivation history;
- applicable contexts, agents, and developmental lines;
- evidence and interpretations;
- relationships to other objects;
- uncertainty and disagreement;
- proposed or completed tests.

This supports inspectability without requiring every play moment to become administrative data.

## 15. Example trace

An abbreviated trace from the Go excavation:

```text
Seed: intuitive early placement
  → Performance: commitment before full explanation
  → Context: spacious strategic field
  → Relations: opponent moves, connections, conflicts, absences
  → Consequence: the placement acquires a specific function
  → Artifact: persistent stone and board history preserve lineage
  → Interpretation: “the intuition developed into influence”
  → Evidence: prediction, usefulness, satisfaction, board state
  → Claim: enacted intuition can become legible through play
  → Uncertainty: conscious prior intent is not required or fully knowable
```

The trace preserves emergence without pretending the ending existed in fully specified form at the beginning.

## 16. Readiness and next step

The ontology now has a provisional conceptual model. The next stage is six-face council ingestion and translation of the complete philosophy-plus-model package.

The council must first demonstrate accurate restatement and application. Pruning, prioritization, and active/reference/compost governance remain out of scope for that pass.
