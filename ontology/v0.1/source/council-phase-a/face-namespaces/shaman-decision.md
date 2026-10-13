# Face Namespace Decision — Shaman

**Decision scope:** Whether altitude face, runtime sect, functional review face, player-facing identity, and council lens are one concept or distinct ontology concepts
**Authority for this decision:** Wendell’s targeted delegation to the six Game Masters
**Status:** Decided for ontology distinction and naming; no broader canon precedence, pruning, or work-disposition decision

## source_inventory

The sources do not establish a reliable chronological publication order among every BARS file. “When” is therefore recorded as the declared architectural or process layer in which each meaning operates.

| Source and section | Layer / when invoked | What it calls a face |
|---|---|---|
| `/Users/wendellbritt/The Library /bars-engine/FOUNDATIONS.md` §§ “How bars-engine maps to (and renames) Wilber” and “The Six Game Master Faces = Integral altitude levels” | Foundational developmental ontology; invoked when describing the vertical axis | Shaman, Challenger, Regent, Architect, Diplomat, and Sage are ordered Integral/Spiral-Dynamics altitude levels: Magenta, Red, Amber, Orange, Green, and Teal. The document also calls the face “what level/lens guides me.” |
| `/Users/wendellbritt/The Library /bars-engine/.agent/context/game-master-sects.md` §§ “The Six Sects,” “Serving a Game Master,” “Domain Constraint,” and “Spiral Dynamics Correspondence” | Player-facing game ontology and agent context; invoked when a player chooses `active_face`, serves a sect, receives aligned quests, or when a face acts in-domain | A face is a Taoist sect headed by a Game Master, a chosen developmental lens, a player-facing school/mission, a trigram preference, and—explicitly—the playable form of a Spiral Dynamics level. This source intentionally couples player identity and altitude semantics. |
| `/Users/wendellbritt/The Library /bars-engine/.cursor/rules/game-master-agents.mdc` opening section and §§ “bars-agents as orchestrators, Cursor subagents as tools” and “Tool mapping” | Runtime execution; invoked when routing AI work through agents, MCP tools, and subagents | A face is an operational agent identity: shaman, regent, challenger, architect, diplomat, or sage, with tool and subagent mappings. Sage is specifically assigned integration, synthesis, meta, and coordination. |
| `/Users/wendellbritt/The Library /bars-engine/.specify/specs/strand-system-bars/spec.md` §§ “Design Decisions,” “Agent Hierarchy,” “Agent Self-Advocacy,” and “Ethos→Stat” | Multi-agent orchestration specification; invoked when a strand sequences sects to investigate and produce BARs | A face is a player-facing sect and executable strand participant with hierarchy mappings, advocacy signals, ethos, and trainable stat. Shaman is a liminal researcher/Compassion/Empathy; the other named sects similarly receive operational roles. |
| `/Users/wendellbritt/The Library /bars-engine/specs/doctrine/gm-faces.md` opening description, all six face sections, and § “GM Face Routing Block” | Functional feature-review doctrine; invoked when routing spec and implementation review | A face is one of six review disciplines: Ontologist, Systems Architect, Experience Designer, Encounter Designer, Steward, or Integrator. Each is a lens; all relevant lenses may apply to a feature. This set differs in both names and function from Shaman–Sage. |
| `/Users/wendellbritt/The Library /bars-engine/docs/process/spec-prework-iching-six-faces.md` §§ “Six Game Master faces — interpret this cast for this work” and “Sage synthesis” | Optional/recommended pre-implementation ritual; invoked while interpreting an I Ching cast for one bounded spec | Shaman–Sage are temporary work lenses: felt pattern, governance, falsification, structure, relational tone, and integration. The instruction says each face should interpret this cast for this work, not classify a person. |
| `/Users/wendellbritt/The Library /bars-engine/specs/doctrine/emotional-alchemy-321.md` § “GM Voice Sequence” | Implemented 3-2-1 encounter voice sequence; invoked at specific ritual phases | Face names become phase-bound voices: Shaman holds Face It, Challenger pushes Talk to It, Sage witnesses Be It, and Integrator reveals the alchemy. This source mixes names from the Shaman–Sage namespace with Integrator from the functional-review namespace, demonstrating that “voice” is another relation rather than proof of identity among face systems. |
| `outputs/design-ontology-six-face-council-brief.md` §§ “Game Master face configuration” and “Council assignments” | New-ontology Phase A inquiry; invoked when six independent perspectives ingest, translate, challenge, govern, bridge, and synthesize material | Shaman–Sage are council lenses with bounded questions and deliverables. They are co-present perspectives; no sequence position establishes a player’s developmental rank. |
| `outputs/design-philosophy-draft-v0.1.md` § “Instructions for AI collaborators” and the companion council brief | Provisional design-philosophy use; invoked when an AI applies the ontology | Faces are not formally modeled as altitude objects; the package instead prohibits global whole-person rank and requires contextual development claims. |
| `outputs/council-phase-a/architect-canon-crosswalk.md` §§ “Six Game Master Faces names three non-identical structures,” “Face,” and `unresolved_authority_questions` | Phase A canon comparison | Records altitude, functional review, runtime sect, and council orientation as non-identical structures and warns that the functional Architect and altitudinal Architect are not coextensive. |
| `outputs/council-phase-a/shaman-canon-crosswalk.md` §§ `conflicts`, `changed_meanings`, and `comprehension_impact` | Phase A felt/symbolic comparison | Records at least three current semantics and concludes that comprehension requires naming which face system and function is intended. |
| `outputs/council-phase-a/challenger-canon-crosswalk.md` §§ `conflicts` and `changed_meanings` | Phase A falsification comparison | Shows that one settled face ontology cannot survive counterexamples: Challenger alone means Red altitude, action/Resolve sect, Codemedic, contrarian runtime tool, and falsification lens. |
| `outputs/council-phase-a/diplomat-canon-crosswalk.md` §§ “The six faces are altitudes in one canon source but lenses or roles in others” and “Six Game Master faces” | Phase A relational/translation comparison | Records the cost of translating one namespace into another and the risk that a face assignment becomes a global player rank. |
| `outputs/council-phase-a/regent-canon-crosswalk.md` §§ “The six faces have incompatible current definitions” and “Game Master face” | Phase A authority comparison | Finds that the definitions cannot be treated as one authority-bearing object without a scoping decision. |
| `outputs/council-phase-a/sage-canon-reconciliation.md` §§ “At least four meanings of Game Master face,” “semantic_namespace_crosswalk,” “Retrieval and prompt construction requirements,” and “Face namespace test” | Phase A cross-source synthesis | Requires explicit namespaces such as `altitude_face`, `review_face`, `runtime_sect`, and `council_lens`, and forbids inference from a chosen lens to a person’s altitude. |

## meaning_by_environment

### Altitude face

- **Object represented:** a position or mode in an ordered developmental model.
- **Members:** Shaman, Challenger, Regent, Architect, Diplomat, Sage.
- **Defining properties:** Spiral/Integral color, vertical order, characteristic sense-making, inclusion/transcendence claim.
- **Primary source:** `FOUNDATIONS.md` § “The Six Game Master Faces = Integral altitude levels.”
- **Truth conditions:** requires a developmental interpretation and a declared subject, line, context, and evidence if applied beyond the abstract map.
- **Primary category risk:** turning a contextual mode into a total rank of a person.

### Runtime sect

- **Object represented:** an executable agent role participating in orchestration.
- **Members:** the same six Shaman–Sage names.
- **Defining properties:** tools, prompts, subagent mapping, domain, self-advocacy, sequencing, outputs, and audit events.
- **Primary sources:** `.cursor/rules/game-master-agents.mdc` and `.specify/specs/strand-system-bars/spec.md` §§ “Agent Hierarchy” and “Agent Self-Advocacy.”
- **Truth conditions:** established by configured behavior and execution, not by developmental assessment.
- **Primary category risk:** treating a tool route as evidence that the user, agent, or response occupies an altitude.

### Functional review face

- **Object represented:** a review discipline applied to a feature or specification.
- **Members:** Ontologist, Systems Architect, Experience Designer, Encounter Designer, Steward, Integrator.
- **Defining properties:** review focus, routing priority, implementation concern, and mapping to Ouroboros tools.
- **Primary source:** `specs/doctrine/gm-faces.md`.
- **Truth conditions:** established by the kind of review work performed.
- **Primary category risk:** assuming Systems Architect is identical to the Shaman–Sage Architect, or Integrator identical to Sage, merely because functions overlap.

### Player-facing identity

- **Object represented:** a diegetic sect, school, mission, and selected developmental lens through which a player receives aligned material.
- **Members:** Shaman–Sage sects.
- **Defining properties:** sect head, mission, role, trigram preference, `active_face`, quest alignment, and service relationship.
- **Primary source:** `.agent/context/game-master-sects.md` §§ “The Six Sects,” “Serving a Game Master,” and `FACE_TRIGRAM_PREFERENCE`; the player-facing status is also explicit in `strand-system-bars/spec.md` § “Design Decisions.”
- **Truth conditions:** established by a player’s selection or current game state, not by an observer’s judgment of their whole developmental status.
- **Primary category risk:** because canon explicitly says the sects make altitude playable, a voluntary in-game alignment can be misread as a psychological classification.

### Council lens

- **Object represented:** a temporary, bounded perspective used to ask characteristic questions and produce an attributed interpretation.
- **Members:** Shaman–Sage.
- **Defining properties:** inquiry mandate, epistemic emphasis, translation loss, bounded deliverable, and no unilateral authority over other lenses.
- **Primary sources:** `outputs/design-ontology-six-face-council-brief.md` § “Council assignments” and `docs/process/spec-prework-iching-six-faces.md` § “Six Game Master faces — interpret this cast for this work.”
- **Truth conditions:** established by the questions and reasoning discipline used during a particular inquiry.
- **Primary category risk:** treating an adopted perspective as a stable type or altitude of the agent or person using it.

### Phase voice

- **Object represented:** a narrative/facilitative voice assigned to one moment of a ritual sequence.
- **Members in the cited implementation:** Shaman, Challenger, Sage, Integrator.
- **Defining properties:** phase, tone, function, and transition.
- **Primary source:** `specs/doctrine/emotional-alchemy-321.md` § “GM Voice Sequence.”
- **Primary category risk:** using a mixed namespace without declaring whether the label names a sect, review function, or simply the voice profile borrowed for that phase.

## shared_structure

The five requested concepts share enough structure to explain why the same metaphor and names recur:

- each presents a **bounded way of attending and acting** rather than an exhaustive account of reality;
- each carries a recognizable **pattern signature**—for example, Shaman/ritual and felt pattern, Challenger/edge and pressure, Regent/order and boundary, Architect/strategy and structure, Diplomat/relationship and care, Sage/integration and meta-view;
- each can influence **routing**: a player route, agent route, review route, inquiry route, or developmental interpretation;
- each can be expressed through a **voice, mission, question set, affordance, or tool configuration**;
- each can be attached to a shared symbolic ecology of trigrams, ethos, stats, missions, colors, and narrative roles;
- each is most useful when its scope is explicit and when other perspectives remain available.

This shared structure supports a common parent concept, but not identity among its manifestations. The best common parent is a **Face Archetype** or **Face Signature**: a symbolic-functional pattern such as Shaman or Architect whose meaning can be instantiated differently by environment.

The common parent should carry only cross-environment semantic material that survives translation—for example, stable name, motif, characteristic attention, recurring question, and provenance. It should not itself carry vertical order, runtime tool binding, player selection, review authority, or council decision rights. Those belong to the environment-specific concepts.

The Ontologist–Integrator review set does not share the same six archetype members. It belongs to the larger metaphorical family of “faces/lenses” but should not be forced beneath the Shaman–Sage Face Archetype as if each member had a one-to-one correspondence.

## non_equivalences

- **Ordered altitude is not selectable lens.** An altitude model asserts vertical relationship; a council lens can be adopted temporarily and coexists with the others.

- **Player choice is not developmental measurement.** Selecting `active_face = shaman` establishes current sect alignment and quest preference under `.agent/context/game-master-sects.md`; it does not, by itself, establish that the player is Magenta in a line, state, or whole-person sense.

- **Agent execution is not player identity.** Running `shaman_read` or using an explore subagent establishes runtime routing, not the identity or altitude of the player, designer, or AI.

- **Functional review is not altitude.** Ontologist–Integrator have a different member set and are applied according to feature needs. They are neither stages nor player schools.

- **Functional review is not runtime sect.** Systems Architect and Architect may overlap around architecture, while Integrator and Sage may overlap around synthesis, but overlap does not create identity. The remaining members also resist a stable one-to-one mapping.

- **Council lens is not runtime sect.** A council response may be generated by an agent, but the lens is the epistemic contract governing that response; the runtime sect is the executable participant and tool route.

- **Council lens is not player-facing identity.** The council’s Shaman asks felt-truth questions for a bounded inquiry. A player-facing Shaman belongs to a sect, mission, trigram alignment, and story state.

- **Player-facing identity is not identical to altitude face even though canon intentionally relates them.** `.agent/context/game-master-sects.md` says faces make Spiral levels playable, but the representation, player choice, and lived role remain distinguishable from the developmental construct they dramatize.

- **Shared name does not transfer authority.** Sage’s integration role in runtime and council environments does not automatically authorize ratification; Regent’s boundary emphasis does not automatically confer governance authority; Diplomat’s coordination role does not establish consent authority.

- **Phase voice is not proof of namespace identity.** The 3-2-1 sequence’s use of Shaman, Challenger, Sage, and Integrator is a compositional borrowing across systems, not evidence that Integrator is a seventh altitude or that Sage and Integrator are the same object.

- **Psychographic affinity is not altitude.** The new ontology’s provisional Sage–Architect–Shaman center describes design-relevant orientation. It must not become a claim that one person simultaneously occupies several ordered altitudes or that preference establishes level.

## decision

**Altitude face, runtime sect, functional review face, player-facing identity, and council lens are distinct ontology concepts. They are not one polymorphic Face object whose context alone changes its meaning.**

They belong to a related family and may reference shared archetypal signatures, but each has different:

- membership rules;
- ordering or non-ordering;
- evidence requirements;
- selection mechanism;
- executable behavior;
- player-facing consequences;
- authority and permission;
- persistence and lifecycle;
- failure modes.

The decisive evidence is not merely that the sources use different prose. The objects support incompatible predicates. An altitude face can be vertically ordered; a runtime sect can execute and emit advocacy; a review face can be assigned primary/secondary/review status; a player identity can be selected and persisted as `active_face`; a council lens can be temporarily adopted without classifying its user. Treating them as one object would allow invalid inference across those predicates.

The Shaman decision is therefore **distinct manifestations linked by provenance and correspondence**, not one concept and not five unrelated concepts.

## naming_or_relation_recommendation

Use explicit ontology types and qualified names:

1. **`FaceArchetype` / `face_archetype`**
   A shared symbolic-functional signature for the Shaman–Sage vocabulary. Suggested fields: stable ID, display name, motifs, characteristic attention, recurring questions, source provenance, and contested interpretations. It has no intrinsic altitude rank or execution authority.

2. **`DevelopmentalAltitudeFace` / `altitude_face`**
   The ordered Integral/Spiral construct from `FOUNDATIONS.md`. Suggested relation: `interprets_archetype_as_altitude(FaceArchetype)`. Any application to a person must state line, context, evidence, time, uncertainty, and prohibition on whole-person worth claims.

3. **`GameMasterSectAgent` / `runtime_sect`**
   The executable orchestration role from `.cursor/rules/game-master-agents.mdc` and the strand spec. Suggested relation: `operationalizes(FaceArchetype)`. Runtime bindings, tools, advocacy, and audit behavior live here.

4. **`PlayerSectAlignment` / `player_facing_identity`**
   The diegetic school/mission and selected `active_face` from `.agent/context/game-master-sects.md`. Suggested relations: `embodies(FaceArchetype)`, `dramatizes(DevelopmentalAltitudeFace)`, `chosen_by(Player)`, and `aligns_quests_with(TrigramPreference)`. The relation to altitude is explicit but does not make selection an assessment.

5. **`CouncilFaceLens` / `council_lens`**
   The bounded inquiry perspective from the council brief and I Ching prework. Suggested relations: `invokes(FaceArchetype)`, `asks(DesignQuestion)`, `produces(AttributedInterpretation)`, and `records_translation_loss`. It should be ephemeral or encounter-scoped unless an output artifact preserves it.

6. **`ReviewDiscipline` / `review_face`**
   Rename the Ontologist–Integrator set at the ontology level to **Review Discipline**, while retaining “GM Face” as a source label/alias for compatibility with `specs/doctrine/gm-faces.md`. Suggested relations: `reviews(DesignObject)`, `has_review_focus`, and `maps_to_tool`. Do not force a one-to-one map to FaceArchetype.

7. **`PhaseVoiceAssignment` / `phase_voice`**
   Represent the 3-2-1 voice sequence as a relation joining a phase to a borrowed face/discipline signature: `uses_voice_of(phase, source_face_or_discipline)`. This prevents the mixed sequence from collapsing namespaces.

Required relation safeguards:

- `chosen_by` **does not imply** `assessed_as_altitude`;
- `operationalizes` **does not imply** `embodies_player_identity`;
- `invokes` **does not imply** stable psychographic type or altitude;
- `maps_to_tool` **does not imply** conceptual equivalence;
- `dramatizes` preserves the canon’s intentional altitude/sect connection without asserting ontological identity;
- any crosswalk between `ReviewDiscipline` and `FaceArchetype` should be many-to-many, purpose-scoped, and explicitly non-equivalent.

Retrieval and prompt rule:

> Never retrieve, store, or reason from bare `face` when the distinction affects action. Require `altitude_face`, `runtime_sect`, `review_discipline`, `player_sect_alignment`, `council_lens`, or `phase_voice`, plus source and scope.

Interface rule:

> Player-facing language may continue to say “face” or “sect” for aesthetic continuity, but internal records must preserve the qualified ontology type. Choosing a face must not silently display or store a developmental diagnosis.

## residual_uncertainty

- **Altitude application remains unresolved.** This decision separates the concept but does not decide whether the canonical altitude model describes whole persons, line-specific capacities, temporary sense-making, or narrative archetypes. The new ontology’s anti-totalization invariant still constrains any application.

- **The shared `FaceArchetype` is a recommended bridge, not an already implemented canonical object.** Its exact fields and authority require later modeling work.

- **Player-facing sect and altitude are intentionally fused in current canon.** The relation `dramatizes` is recommended to preserve that intent safely, but the source itself says the faces “ARE” the levels made playable. Whether code should split existing records is outside this scoped decision.

- **Runtime sect and player-facing sect may share implementation identity in current code.** This decision says their ontology meanings differ; it does not require immediate storage migration or duplicate database rows.

- **The functional review-face set may be legacy, parallel, or current doctrine.** Renaming it `ReviewDiscipline` at the ontology layer prevents collision without deciding whether its source file should be renamed or superseded.

- **Council lens and I Ching prework lens strongly resemble one another but are not proven identical.** The council lens carries Phase A ingestion constraints and face-specific deliverables that the shorter prework ritual does not.

- **Some face-specific mappings remain many-to-many.** Architect may correspond to Systems Architect and parts of Ontologist or Encounter Designer; Sage may correspond to Integrator and Ontologist; Shaman may contribute to Experience and Encounter design. No one-to-one table should be inferred without a bounded use case.

- **Authority does not follow naming.** This decision distinguishes concepts but does not decide who may ratify ontology changes, override agent self-advocacy, assign player altitude, or govern cross-domain action.

- **Chronology remains layer-based rather than date-based.** The sources show coexistence and differing declared purposes more reliably than they show which face vocabulary was authored first.
