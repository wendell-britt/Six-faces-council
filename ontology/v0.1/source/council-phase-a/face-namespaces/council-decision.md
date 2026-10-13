# Six-Face Council Decision — Face Namespaces

**Decision date:** 2026-10-10
**Decision scope:** Altitude face, runtime sect, functional review face, player-facing identity, and council lens
**Authority:** Wendell's targeted delegation to the six Game Master council
**Status:** Decided for ontology distinction, relations, and inference boundaries only
**Source face records:** Architect, Challenger, Diplomat, Regent, and Shaman decisions in this directory, synthesized here by the Sage

## decision

The six-face council decides that **altitude face, runtime sect, functional review face, player-facing sect identity, and council lens are distinct ontology concepts**. They must not be stored, retrieved, or reasoned from as one unqualified `Face` object whose meaning changes silently with context.

They are neither one concept nor five unrelated concepts. Their correct relationship is:

```text
shared symbolic lineage
        |
        +-- altitude interpretation
        +-- runtime implementation
        +-- player-facing sect expression
        +-- council-lens invocation

functional review disciplines
        |
        +-- explicitly mapped, when useful, to runtime or council capabilities
```

The Shaman–Challenger–Regent–Architect–Diplomat–Sage vocabulary forms a shared **Game Master archetypal family** across altitude, runtime, player-facing, and council environments. Shared names and motifs establish correspondence and provenance, not object identity or inherited authority.

The Ontologist–Systems Architect–Experience Designer–Encounter Designer–Steward–Integrator vocabulary is a separate **functional review taxonomy**. It may route to the named-six family through explicit, scoped, many-to-many mappings; it is not a second naming of the same six members.

The council also establishes this protection:

> Selecting, enjoying, serving, invoking, routing through, or temporarily speaking from a face is not evidence of a person's global developmental altitude, worth, identity, or authority.

An altitude claim, if made at all, must name its developmental framework, subject, line or domain, context, evidence, time, and uncertainty. It cannot be inferred from a sect choice, agent invocation, council assignment, review responsibility, stylistic resemblance, psychographic affinity, or shared name.

### Convergence and dissent

All five preserved face decisions and the Sage synthesis converge on the substantive ruling:

- the five requested concepts are distinct;
- a bare `Face` identifier is unsafe where meaning affects action;
- the named-six uses share archetypal lineage without sharing identity;
- the functional review set has different membership and selection rules;
- authority, permissions, evidence, persistence, and developmental ordering remain local to their namespaces;
- cross-namespace mappings must be explicit and provenance-bearing;
- no role, affiliation, or lens permits a whole-person altitude inference.

There is **no substantive dissent**. The face records contain three modeling variations, resolved here as follows:

1. **Common parent:** Architect allows a broad `PerspectiveRole` or `ArchetypalRole`; the other faces favor `FaceArchetype` or `GameMasterArchetype`. The council adopts `GameMasterArchetype` for the named-six symbolic lineage. A generic `PerspectiveRole` may exist above it, but it carries no face-specific semantics.
2. **Prework lens:** Challenger lists `PreworkLensInvocation` separately, while other faces treat it as closely related to council practice. The council models it as a contextual invocation of `CouncilLens`, not a sixth primary face namespace, unless future evidence shows different durable properties or authority.
3. **Phase voice:** The Emotional Alchemy 3-2-1 sequence mixes named-six and functional-review labels. The council models this as `PhaseVoiceAssignment`, a typed relation to a borrowed voice source, not another face identity.

## source_meanings

The decision preserves the meanings established by each source environment rather than choosing one definition to overwrite the others.

| Source environment | Source meaning | Subject | Activation or selection | Authority and consequence |
|---|---|---|---|---|
| `/Users/wendellbritt/The Library /bars-engine/FOUNDATIONS.md` — **The Six Game Master Faces = Integral altitude levels** | Shaman through Sage are ordered Magenta-through-Teal developmental altitudes | A developmental pattern, level, or lens; the exact unit of attribution remains underspecified | Developmental interpretation or assessment | Supplies vertical-development semantics; does not grant runtime tools, player identity, review coverage, or council authority |
| `/Users/wendellbritt/The Library /bars-engine/.agent/context/game-master-sects.md` — **The Six Sects**, **Serving a Game Master**, **Spiral Dynamics Correspondence** | The named six are Taoist sects, selectable developmental lenses, missions, trigram affinities, and the playable expression of Spiral Dynamics levels | A sect definition and a player's relation to it | Player choice through `active_face`, service, quests, and game state | Shapes affiliation, narrative presentation, and content alignment; choice alone does not diagnose the player's altitude |
| `/Users/wendellbritt/The Library /bars-engine/.cursor/rules/game-master-agents.mdc` — **Game Master Agents** and **Tool mapping** | The named six are executable agents with prompts, subagent mappings, and tools | An AI runtime participant or invocation | Router, MCP operation, strand, or direct agent call | Grants only configured execution capability and produces operational provenance |
| `/Users/wendellbritt/The Library /bars-engine/.specify/specs/strand-system-bars/spec.md` — **Design Decisions**, **Agent Hierarchy**, **Ethos→Stat** | Named sects are both player-facing and strand participants, with roles, hierarchy, ethos, stats, advocacy, and recorded sequence | Sect definitions, player-facing presentation, and runtime participants | Player presentation and/or strand orchestration | Intentionally connects fiction and execution, but does not make the player's affiliation record identical to the runtime agent instance |
| `/Users/wendellbritt/The Library /bars-engine/specs/doctrine/gm-faces.md` — **The Six Game Master Faces** and **GM Face Routing Block** | Ontologist, Systems Architect, Experience Designer, Encounter Designer, Steward, and Integrator are review responsibilities | A feature, specification, or implementation risk | Primary, secondary, and review routing by dominant challenge | Determines review questions and coverage; does not define altitude, sect affiliation, or named-six identity |
| `/Users/wendellbritt/The Library /bars-engine/docs/process/spec-prework-iching-six-faces.md` — **Six Game Master faces** and **Sage synthesis** | The named six are temporary interpretive perspectives on one cast and work item | A bounded design question | Pre-implementation ritual invocation | Produces attributed design counsel; it is not developmental diagnosis or runtime identity |
| `/Users/wendellbritt/The Library /bars-engine/specs/doctrine/emotional-alchemy-321.md` — **GM Voice Sequence** | Shaman, Challenger, Sage, and Integrator are voices bound to encounter phases | A phase in one Emotional Alchemy flow | Flow position | Determines local voice and function; mixed names demonstrate assignment across namespaces, not identity among them |
| `outputs/design-ontology-six-face-council-brief.md` — **Council assignments** | The named six are bounded epistemic lenses for felt truth, structure, falsification, authority, translation, and integration | A question, claim, source package, or design decision | Deliberative assignment | Produces attributable interpretations whose convergence raises support but does not automatically ratify truth |
| `outputs/design-ontology-six-face-council-brief.md` — **Provisional designer psychograph** | Sage–Architect–Shaman is a provisional design-relevant orientation | A revisable psychographic hypothesis | Interpretive modeling from available evidence | Guides design hypotheses; it is neither a global altitude profile nor a required runtime or player identity |

No single source governs every environment. Authority remains domain-specific: foundations govern their developmental model; runtime rules govern execution; doctrine governs feature review; sect sources govern game presentation and affiliation; and the council brief governs deliberative method.

## shared_archetypal_structure

The named-six environments share recurrent symbolic centers:

| Archetype key | Cross-source center | Examples of environment-specific expression |
|---|---|---|
| `shaman` | felt pattern, ritual, liminality, belonging, exploration | Magenta altitude; liminal/research runtime; player sect; somatic-symbolic council lens |
| `challenger` | edge, force, risk, action, falsification | Red altitude; contrarian/action runtime; courage/resolve sect; falsification lens |
| `regent` | order, record, boundary, governance, stewardship | Amber altitude; chronicler/governance runtime; balance/equity sect; authority lens |
| `architect` | structure, strategy, schema, clarity, implementation | Orange altitude; drafting/compilation runtime; structure sect; formalization lens |
| `diplomat` | relationship, care, bridge, translation, community | Green altitude; coordination/bridging runtime; harmony sect; accessibility and allyship lens |
| `sage` | integration, witness, synthesis, meta-system | Teal altitude; integrator runtime; wisdom sect; synthesis lens |

This justifies `GameMasterArchetype` records carrying only cross-environment material:

- stable archetype key and display name;
- recurring motifs, characteristic attention, and question patterns;
- symbolic associations with explicit source provenance;
- documented variations and contested interpretations.

`GameMasterArchetype` must **not** carry intrinsic runtime permissions, a player affiliation, review obligations, whole-person rank, or unilateral decision authority. Those properties belong to the environment-specific concepts.

The functional review disciplines share a still broader pattern—bounded perspective-taking and differentiated coverage—but not the same members or canonical motifs. They may inherit from a generic `PerspectiveRole` if useful. They must not be forced into the named-six archetype table.

## required_distinct_concepts

The ontology requires the following concepts and separation boundaries.

| Concept | Recommended namespace | What it represents | Required distinguishing information |
|---|---|---|---|
| Shared named-six lineage | `gm_archetype` | Symbolic-functional continuity among Shaman–Sage uses | key, motifs, characteristic questions, associations, sources, contested meanings |
| Developmental interpretation | `altitude_face` | Ordered Integral/Spiral developmental pattern | framework, face key, altitude/color, subject, line/domain, context, evidence, time, uncertainty |
| Player/runtime thematic definition | `sect_definition` | Sect mission, head, ethos, trigram, stat, and presentation vocabulary shared where canon intends it | sect key, mission, symbolism, content rules, source version |
| Executable role | `runtime_sect` | AI agent configuration and invocation identity | sect key, tools, capabilities, provider/runtime, routing, inputs, outputs, advocacy, audit provenance |
| Player-facing relation | `player_sect_identity` | A player's consented affiliation, active school, or diegetic identity relation | player, sect definition, active state, selection source, effective time, change/revocation history, presentation consequences |
| Feature/spec review responsibility | `review_discipline` | Ontologist-through-Integrator review coverage | review key, domain, selection reason, required checks, authority, completion evidence |
| Deliberative perspective | `council_lens` | A bounded epistemic stance used in multi-lens inquiry | archetype key, question set, evidence foregrounded, predictable losses, mandate, output provenance |
| Contextual use of a lens | `lens_invocation` | One council turn or I Ching prework use of a lens | lens, performer, question/cast, start/end or task scope, output, provenance |
| Local voice binding | `phase_voice_assignment` | A phase's use of a named face or review-discipline voice | phase, source namespace and ID, voice function, scope, implementation source |

The five primary requested concepts are therefore `altitude_face`, `runtime_sect`, `review_discipline`, `player_sect_identity`, and `council_lens`. `gm_archetype` and `sect_definition` are bridge objects; `lens_invocation` and `phase_voice_assignment` are scoped relation records. They do not collapse the five concepts.

Every durable record must use a qualified namespace. Human-facing copy may use “Shaman,” “Architect,” or “face” when the interface makes the layer unmistakable, but storage, permissions, retrieval, developmental claims, and audit trails must not rely on a bare name.

## allowed_relations

The following cross-namespace relations are allowed when their source, scope, time, and configuration are recorded:

- `draws_from_archetype(environment_object, gm_archetype)` — preserves symbolic lineage without identity.
- `interprets_archetype_as_altitude(altitude_face, gm_archetype)` — records the foundational developmental interpretation.
- `draws_from_archetype(sect_definition, gm_archetype)` — connects a sect's symbolic vocabulary to the named-six lineage.
- `makes_playable(sect_definition, altitude_face)` or `dramatizes(sect_definition, altitude_face)` — preserves the canon's intentional altitude/sect relationship without treating play choice as assessment.
- `operationalizes(runtime_sect, sect_definition_or_gm_archetype)` — records how a runtime role enacts the motif.
- `affiliated_with(player_sect_identity, sect_definition)` — records a player's chosen or assigned game relation.
- `invokes(lens_invocation, council_lens)` and `performed_by(lens_invocation, agent_or_person)` — separates epistemic contract from executor.
- `routes_to_runtime(review_discipline_or_lens, runtime_sect)` — records configured execution routing; cardinality is many-to-many unless a source explicitly constrains it.
- `reviewed_by(design_object, review_discipline)` — records functional coverage without archetypal inference.
- `supports_review(council_lens, review_discipline)` — records a scoped correspondence between inquiry and review needs.
- `bound_to_phase(phase_voice_assignment, source_voice)` — records local voice borrowing, including mixed namespaces.
- `shares_face_key_with(object_a, object_b)` — a weak provenance/correspondence relation only; it carries no authority or property inheritance.
- `claims_altitude(subject, altitude_face, evidence, scope)` — permitted only as an explicit, contestable, bounded claim with line/domain, context, time, uncertainty, and provenance.

No cross-namespace relation defaults from matching labels. A mapping must say what it preserves, what it loses, who or what authorized it, and where it applies.

## forbidden_inferences

The following inferences are forbidden unless independent evidence establishes the target claim in its own namespace:

1. **Shared label → identity:** `architect` in two namespaces does not make the records the same object.
2. **Player sect → altitude:** choosing, serving, enjoying, or being assigned a sect does not establish the corresponding developmental altitude.
3. **Player sect → whole identity:** `active_face` does not exhaust the player's psychograph, values, capacities, or personal meaning.
4. **Player sect → runtime permission:** affiliation does not grant tool access, governance authority, helping credentials, or agent capabilities.
5. **Runtime route → player identity:** invoking a runtime sect or observing its logs does not enroll, classify, or speak for a player.
6. **Runtime route → altitude:** a Sage execution does not establish Teal altitude in the model, operator, subject, or output.
7. **Altitude → permission:** an altitude interpretation does not grant runtime tools, review authority, governance power, or player-state changes.
8. **Council lens → stable type or rank:** temporarily applying a Shaman, Regent, or Sage lens does not establish psychographic identity or developmental level.
9. **Council convergence → empirical truth:** agreement among lenses increases support; it does not replace evidence, owner authority, consent, or play verification.
10. **Sage synthesis → ratification or superiority:** integration responsibility does not imply universal correctness, approval power, or a higher-quality person.
11. **Functional review → named-six identity:** Systems Architect is not automatically Architect; Integrator is not automatically Sage; no ordinal six-to-six mapping is valid.
12. **Review assignment → execution:** assigning a review discipline does not prove that a particular runtime sect or tool performed the review.
13. **Council order → developmental ladder:** a sequence chosen for deliberation or orchestration is not evidence of altitude progression.
14. **Phase voice → face identity:** a flow's use of a Shaman, Challenger, Sage, or Integrator voice does not merge the source namespaces.
15. **Psychographic affinity → altitude:** Wendell's provisional Sage–Architect–Shaman design orientation is not a whole-person developmental assessment.
16. **Undisclosed developmental classification:** player participation through a sect must not silently become an uncorrectable altitude judgment. Any assessment use requires disclosure, evidence, contestability, and a way to participate without accepting it.

## documentation_and_schema_changes

The following changes are required to make the ruling operational. This record specifies them but does not perform them.

1. **Formal ontology model:** Add the concepts and relation boundaries in this decision. State explicitly that the five primary concepts are disjoint record types even when they share a key.
2. **Machine-readable YAML:** Add qualified entity types, namespace-safe identifiers, allowed relations, provenance fields, and forbidden-inference constraints. Do not encode cross-namespace `same_as` links.
3. **Terminology registry:** Create a source-aware alias table for legacy uses of `Face`, `active_face`, “GM Face,” and “sect.” Each alias must resolve only when source and operational layer are known.
4. **Retrieval contract:** Classify face queries before retrieval:
   - developmental interpretation → `altitude_face` plus anti-ranking constraints;
   - agent or strand execution → `runtime_sect` plus tools and runtime rules;
   - feature/spec review → `review_discipline` plus routing requirements;
   - player school, ethos, quests, or affiliation → `player_sect_identity` and `sect_definition`;
   - council reasoning → `council_lens` plus mandate and attribution.
5. **Prompt construction:** Replace ambiguous prompts such as “ask the Architect” with “invoke the Architect runtime sect,” “apply the Architect council lens,” “apply the Systems Architect review discipline,” or “present the Architect sect,” as intended.
6. **Audit and provenance:** Store namespace, source path/version, subject, task scope, performer, time, evidence, confidence, and applicable authority on every invocation or crosswalk.
7. **Altitude claims:** Introduce a bounded claim object requiring developmental framework, line/domain, context, evidence, time, uncertainty, correction path, and explicit prohibition on deriving whole-person worth.
8. **Player-state documentation:** Document legacy `active_face` as a player sect alignment/routing field, not a runtime-agent identity or sufficient altitude assessment. Preserve change and revocation history. Do not migrate or rewrite existing data without a separate implementation decision.
9. **Functional review terminology:** In new ontology/schema work, prefer `ReviewDiscipline`; retain “GM Face” as a source label or compatibility alias for `specs/doctrine/gm-faces.md`.
10. **Council and prework outputs:** Record the `council_lens`, its invocation context, and its actual performer separately. Preserve each lens's contribution before synthesis.
11. **Phase voice documentation:** Qualify each Emotional Alchemy voice by source namespace and phase rather than extending the global face enumeration.
12. **Player-facing explanation:** Explain in accessible language that a sect is a school a player can engage, an agent is a tool that can act, a council lens is a way of asking questions, a review discipline is a responsibility, and an altitude face belongs to a developmental theory. State that choosing one does not rank the player.
13. **Existing source prose:** Preserve canonical wording and attach namespace annotations externally until a separately authorized canon-editing pass decides whether source headings or field names should change.

## residual_uncertainty

- **Altitude subject:** `FOUNDATIONS.md` establishes ordered altitude semantics but does not settle whether a claim describes a whole person, a line-specific capacity, a momentary mode, a center of gravity, a character choice, or a narrative archetype.
- **Strength of sect/altitude identity:** `game-master-sects.md` says the sects “ARE” Spiral Dynamics levels made playable. This decision preserves that intent through `makes_playable` or `dramatizes` while preventing player selection from becoming automatic assessment. The theoretical priority of altitude, archetype, and sect remains unresolved.
- **Archetypal invariant:** The exact minimal content that survives across every Shaman, Challenger, Regent, Architect, Diplomat, and Sage use still needs modeling and testing; poetic similarity must not become inherited permission.
- **Player-facing granularity:** “Identity” may include sect definition, Game Master head-character, player affiliation, active play lens, trained stat, and self-description. Later modeling may require additional subtypes.
- **Affiliation lifecycle:** Selection, consent, exclusivity, multiplicity, switching, persistence, and revocation rules for player sect relations remain underspecified.
- **Shared implementation:** Runtime sect and player-facing sect may currently share IDs or records. This ruling distinguishes their meanings but does not require an immediate storage migration or duplicate rows.
- **Review-doctrine lifecycle:** The Ontologist–Integrator taxonomy may be current, legacy, or complementary. This decision preserves it as a distinct review namespace without deciding whether it should remain sixfold or be renamed in its source.
- **Review/runtime mapping:** No governing one-to-one map exists. Correspondences remain many-to-many and task-dependent.
- **Council versus prework:** I Ching prework resembles a council-lens invocation but has different inputs and output constraints. It remains a specialized invocation unless later evidence requires a separate reusable lens type.
- **Coordination authority:** Sources distribute coordination and integration among Sage, Regent, Diplomat, and Integrator. Namespace separation exposes but does not resolve that unrelated authority conflict.
- **Runtime self-advocacy:** Agent refusal and advocacy rules do not automatically define human consent or player boundaries.
- **Chronology:** The source set establishes coexisting operational layers more reliably than it establishes the historical authoring order of every face meaning.

None of these uncertainties reopens the core decision: the five concepts remain distinct, their shared symbolism is represented through explicit archetypal correspondence, and no authority or developmental judgment crosses namespaces without independent evidence and a typed relation.
