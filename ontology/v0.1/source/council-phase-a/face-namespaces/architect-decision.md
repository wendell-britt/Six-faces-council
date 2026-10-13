# Face Namespaces — Architect Decision

**Face:** Architect
**Decision date:** 2026-10-10
**Scope:** Altitude face, runtime sect, functional review face, player-facing identity, and council lens
**Boundary:** This decision distinguishes face concepts only. It does not revise the underlying face descriptions, resolve broader canon precedence, rank people, or assign governance dispositions.

## source_inventory

### Foundational altitude model

- **Source:** `/Users/wendellbritt/The Library /bars-engine/FOUNDATIONS.md`
- **Sections:** **The Five Dimensions**; **How bars-engine maps to (and renames) Wilber**; **The Six Game Master Faces = Integral altitude levels**.
- **What it calls a face:** Shaman, Challenger, Regent, Architect, Diplomat, and Sage are the vertical Integral/Spiral-Dynamics altitude axis. Each has an ordered altitude association from Magenta through Teal. The source explicitly distinguishes this vertical axis from the horizontal Grow Up/developmental-lines move.
- **Where it operates:** Foundational world and developmental ontology. The reference to `choiceType: 'altitudinal'` in `quest-grammar/types.ts` also points toward game-facing representation.
- **When it applies:** When interpreting or representing vertical developmental altitude, not merely when assigning a design-review task.

### Functional review-face doctrine

- **Source:** `/Users/wendellbritt/The Library /bars-engine/specs/doctrine/gm-faces.md`
- **Sections:** opening **The Six Game Master Faces**; the six face definitions; **GM Face Routing Block**; **GM Face Routing**; **Mapping to Ouroboros Agents**.
- **What it calls a face:** Ontologist, Systems Architect, Experience Designer, Encounter Designer, Steward, and Integrator.
- **Where it operates:** Specification review and implementation guidance. The source states that each face is a lens and that all relevant faces should be applied to every feature.
- **When it applies:** During feature scoping, spec review, implementation guidance, and routing to specialized Ouroboros agents. Selection depends on the dominant challenge of a feature.

### Runtime Game Master agents

- **Source:** `/Users/wendellbritt/The Library /bars-engine/.cursor/rules/game-master-agents.mdc`
- **Sections:** **Game Master Agents**; **MCP must be available (do not skip)**; **bars-agents as orchestrators, Cursor subagents as tools**; **Tool mapping (bars-agents MCP)**.
- **What it calls a face:** Shaman, Regent, Challenger, Architect, Diplomat, and Sage are operational agents with MCP tools and Cursor-subagent mappings. Sage is explicitly the integration agent.
- **Where it operates:** Agent runtime and tool orchestration.
- **When it applies:** When an AI workflow invokes a named BARS agent, `mcp_task`, `sage_consult`, or strand behavior. Availability of the model backend affects whether the runtime performs full synthesis or falls back to deterministic templates.

### Runtime sects and player-facing sect presentation

- **Source:** `/Users/wendellbritt/The Library /bars-engine/.specify/specs/strand-system-bars/spec.md`
- **Sections:** **Design Decisions (from Socratic Interview)**; **Unified Strand-as-BAR Schema**; **Strand Lifecycle**; **Agent Hierarchy (BARS-Adapted)**; **Agent Self-Advocacy (internal)**; **Functional Requirements / Phase 5**.
- **What it calls a face:** The named six are “Game Master Sects” orchestrated by strands. The spec explicitly says that sects are player-facing and strands are extensible. It maps external agent functions onto the sects, assigns hierarchy, ethos, stats, and advocacy signals, and stores the executed sect sequence.
- **Where it operates:** Multi-agent orchestration, strand persistence, and the player-facing fiction or presentation of the sects.
- **When it applies:** Runtime when a strand selects and executes sects; presentation time when players encounter sect identity, ethos, stat, narrative journey, or sect-authored output.

This source currently uses one sect vocabulary across executable agents and player-facing presentation. That shared vocabulary does not prove that the runtime process and the player’s identity object are the same kind of entity.

### I Ching prework lenses

- **Source:** `/Users/wendellbritt/The Library /bars-engine/docs/process/spec-prework-iching-six-faces.md`
- **Sections:** **Six Game Master faces — interpret this cast for this work**; each named face subsection; **Sage synthesis (mandatory short block)**.
- **What it calls a face:** The named six are short, task-bound interpretive perspectives: felt pattern, governance, falsification, structure, community tone, and integration.
- **Where it operates:** Design-process prework attached to a concrete spec or backlog item.
- **When it applies:** Before implementation when integration discipline is wanted; optional for tiny fixes and recommended for schema, cross-cutting UX, new modules, or multi-spec work.

This use is closer to a temporary council lens than to a developmental altitude or persistent player identity.

### Emotional Alchemy voice binding

- **Source:** `/Users/wendellbritt/The Library /bars-engine/specs/doctrine/emotional-alchemy-321.md`
- **Section:** **GM Voice Sequence**.
- **What it calls a face or voice:** Shaman voices Face It, Challenger voices Talk to It, Sage voices Be It, and Integrator voices the Alchemy Reveal.
- **Where it operates:** The implemented 3-2-1 encounter sequence.
- **When it applies:** At a particular phase of one Emotional Alchemy flow.

This is best read as a phase-to-voice assignment drawing from more than one face vocabulary—named sect faces plus the functional Integrator—not as proof that those vocabularies are identical.

### Provisional design-ontology council lenses

- **Source:** `/Users/wendellbritt/Documents/Codex/2026-10-09/so-x20/outputs/design-ontology-six-face-council-brief.md`
- **Sections:** **Council mandate**; **Provisional designer psychograph / Game Master face configuration**; **Council assignments**.
- **What it calls a face:** Shaman, Architect, Challenger, Regent, Diplomat, and Sage are distinct interpretive lenses assigned different questions and deliverables. The brief also describes Wendell’s provisional center as Sage–Architect–Shaman.
- **Where it operates:** Ontology ingestion, translation, critique, and later synthesis.
- **When it applies:** During a bounded council pass. Multiple face translations coexist; a selected face does not become the whole ontology or a whole-person rank.

### Provisional ontology model

- **Source:** `/Users/wendellbritt/Documents/Codex/2026-10-09/so-x20/outputs/design-ontology-model-v0.1.md`
- **Sections:** **Modeling commitments**; **Agent**; **PsychographicObject**; **Hard invariants for AI collaborators**.
- **What it formalizes:** Agents may hold several roles without those roles establishing rank; psychographic types are revisable design hypotheses; AI must not assign a global developmental level or treat type as level.
- **Where it operates:** General ontology representation.
- **When it applies:** Whenever face information is stored, inferred, retrieved, or used to make a claim about a player, designer, agent, or council participant.

The model does not yet define a `Face` class or namespace the competing source meanings.

### Phase A crosswalk convergence

The face-specific crosswalks independently identified the same distinction:

- `outputs/council-phase-a/architect-canon-crosswalk.md`, **“Six Game Master Faces” names three non-identical structures**, **Face**, and **comprehension_impact**.
- `outputs/council-phase-a/challenger-canon-crosswalk.md`, **conflicts**, **changed meanings**, and its face-comprehension tests.
- `outputs/council-phase-a/diplomat-canon-crosswalk.md`, **The six faces are altitudes in one canon source but lenses or roles in others** and **changed_meanings / Six Game Master faces**.
- `outputs/council-phase-a/regent-canon-crosswalk.md`, **translation_losses** and **comprehension_impact / Face identity test**.
- `outputs/council-phase-a/shaman-canon-crosswalk.md`, **conflicts**, **changed meanings**, and the requirement to name which six-face system is in use.
- `outputs/council-phase-a/sage-canon-reconciliation.md`, **Face ontology and anti-ranking**, **At least four meanings of “Game Master face”**, **cross_environment_translation_map**, and **Revised comprehension checks / Face namespace test**.

The crosswalks were Phase A evidence rather than decisions. Their convergence establishes that collapsing the meanings causes predictable comprehension loss.

## meaning_by_environment

| Environment | Proposed ontology concept | Members | Selection criterion | Persistence | Primary consequence |
|---|---|---|---|---|---|
| Integral/developmental model | `AltitudeFace` | Shaman, Challenger, Regent, Architect, Diplomat, Sage | The developmental/sense-making altitude being represented | May describe a state, stage, or assessed context; exact persistence remains unresolved | Locates vertical complexity or worldview in the foundational model |
| Spec and implementation review | `ReviewFace` | Ontologist, Systems Architect, Experience Designer, Encounter Designer, Steward, Integrator | The dominant review responsibility of a feature | Task-bound; multiple review faces may apply | Determines questions, review coverage, and Ouroboros routing |
| AI execution | `RuntimeSect` | Shaman, Challenger, Regent, Architect, Diplomat, Sage | Required agent capability or strand route | Persists as executable identity/configuration and audit ID | Determines tools, prompts, advocacy, outputs, and orchestration |
| Player-facing game layer | `PlayerSectIdentity` | Currently presented through the named sect vocabulary | Player-facing affiliation, character framing, training path, ethos, or stat | Potentially persistent in player/game state | Shapes presentation, belonging, progression, narrative voice, or available paths |
| Deliberative ontology/design work | `CouncilLens` | Shaman, Challenger, Regent, Architect, Diplomat, Sage | The perspective needed for a bounded question | Temporary role in a council pass; may be recorded in provenance | Determines what evidence and tensions are foregrounded in deliberation |
| Emotional Alchemy encounter | `NarrativeVoiceBinding` | Shaman, Challenger, Sage, Integrator in the reviewed flow | The current 3-2-1 phase | Encounter-phase-bound | Determines voice and function during a particular interaction |

The final row is a relation/binding rather than a sixth face ontology. It demonstrates why explicit mappings are necessary: a single flow can intentionally draw names from separate face systems.

## shared_structure

The five requested concepts share a family resemblance:

- Each constrains attention by foregrounding some qualities and backgrounding others.
- Each supplies a recognizable role, voice, or interpretive stance.
- Each can help route work, content, questions, or player expectations.
- Several reuse the Shaman–Challenger–Regent–Architect–Diplomat–Sage archetypal vocabulary.
- Each benefits from provenance: source, scope, assignment, time, and evidence should remain visible.
- No assignment should silently become a claim about the entire person, agent, feature, or world.

This supports a shared upper-level abstraction such as `PerspectiveRole` or `ArchetypalRole`. It does not support a single undifferentiated `Face` class with one meaning.

For the named-six family, a shared `FaceArchetype` may preserve symbolic continuity:

```text
FaceArchetype(shaman)
  may_be_expressed_by AltitudeFace(shaman)
  may_be_implemented_by RuntimeSect(shaman)
  may_be_presented_as PlayerSectIdentity(shaman)
  may_be_invoked_as CouncilLens(shaman)
```

The functional review faces use another vocabulary and need explicit crosswalk relations rather than assumed identity:

```text
ReviewFace(systems_architect)
  may_route_to RuntimeSect(architect)

ReviewFace(integrator)
  may_route_to RuntimeSect(sage)
```

Those examples express operational mappings documented in `specs/doctrine/gm-faces.md`, **Mapping to Ouroboros Agents**, and the broader crosswalks. They do not declare semantic equivalence.

## non_equivalences

### Ordered altitude is not task assignment

`AltitudeFace` is explicitly ordered along a vertical developmental axis in `FOUNDATIONS.md`. `ReviewFace`, `RuntimeSect`, and `CouncilLens` are selected because a task needs a capability or perspective. Selecting Sage for synthesis cannot establish that the operator or agent is at Teal altitude; selecting Shaman cannot imply a lower-quality or less-developed person.

### An executable agent is not a perspective

A `RuntimeSect` has tool bindings, backend dependencies, possible deterministic fallback, self-advocacy payloads, an audit identity, and produced artifacts. A `CouncilLens` is a bounded instruction about how to interpret a question. One runtime sect can enact several lenses, and one lens can be enacted by different runtimes or humans.

### A player identity is not a software process

The strand spec says sects are player-facing while also treating them as orchestrated agents. Player presentation may share names, ethos, and imagery with the runtime sect, but a human affiliation or character identity has different consent, persistence, progression, display, and meaning-authority requirements. Runtime logs must not silently become claims about the player’s identity, and player selection must not determine agent capability.

### A review responsibility is not an archetypal identity

The functional review set has different membership and is chosen by feature risk: naming, schema, experience, encounter, ethics, or evaluation. It is possible for the Systems Architect review face to route to the Architect runtime sect, but that relationship is contingent and task-specific. The terms are not interchangeable.

### A council lens is not a psychographic diagnosis

The design-ontology brief’s Sage–Architect–Shaman center is a provisional design-relevant orientation. A face used in one council turn is even narrower: it specifies the evidence and questions to foreground. Neither establishes a stable type or developmental altitude.

### Narrative voice binding is not face identity

The 3-2-1 GM Voice Sequence attaches voices to phases. It does not establish that Face It is identical to Shaman, that all Shaman activity belongs to Face It, or that Integrator and Sage are the same face. It is a contextual role assignment.

### Shared names do not establish shared instances

`Architect` can mean Orange altitude, a runtime sect, an Artificer mapping, a schema/API review role, an I Ching prework lens, or the Architect council perspective. Name equality supplies a crosswalk clue; it does not supply ontological identity.

## decision

**Altitude face, runtime sect, functional review face, player-facing identity, and council lens are five distinct ontology concepts. They are not one concept with interchangeable labels.**

The architecture should preserve two levels simultaneously:

1. A broad common family—`PerspectiveRole` or `ArchetypalRole`—captures their shared ability to foreground a way of perceiving, acting, reviewing, or presenting.
2. Five disjoint contextual subtypes preserve the differences that change behavior and evidence:
   - `AltitudeFace`
   - `RuntimeSect`
   - `ReviewFace`
   - `PlayerSectIdentity`
   - `CouncilLens`

“Disjoint” here means that an individual record must not silently serve as more than one subtype. The same archetypal name may have separately identified records in several namespaces, connected by explicit relations.

The Shaman–Sage vocabulary can function as a shared archetypal lineage across altitude, runtime, player presentation, and council use. That lineage is a relationship among concepts, not proof that the concepts are identical.

The Ontologist–Integrator review vocabulary remains a separate functional taxonomy. It may map to named runtime sects or council lenses for execution, but mappings must be explicit, scoped, and many-to-many capable.

This decision also constrains inference:

- no altitude may be inferred from runtime routing, player affiliation, or council-lens selection;
- no player identity may be inferred from agent logs or tool use;
- no runtime capability may be inferred from a player-facing title;
- no review coverage may be assumed from an archetypal name without a `ReviewFace` assignment;
- no council synthesis role implies approval, ratification, or superior development.

## naming_or_relation_recommendation

### Required namespaces

Use qualified identifiers in schemas, prompts, retrieval records, and prose whenever ambiguity matters:

```text
altitude_face.shaman
altitude_face.challenger
altitude_face.regent
altitude_face.architect
altitude_face.diplomat
altitude_face.sage

runtime_sect.shaman
runtime_sect.challenger
runtime_sect.regent
runtime_sect.architect
runtime_sect.diplomat
runtime_sect.sage

player_sect_identity.shaman
player_sect_identity.challenger
player_sect_identity.regent
player_sect_identity.architect
player_sect_identity.diplomat
player_sect_identity.sage

council_lens.shaman
council_lens.challenger
council_lens.regent
council_lens.architect
council_lens.diplomat
council_lens.sage

review_face.ontologist
review_face.systems_architect
review_face.experience_designer
review_face.encounter_designer
review_face.steward
review_face.integrator
```

Bare `face`, `Architect`, `Sage`, or “the six faces” should not be used as a machine identifier or retrieval key.

### Shared lineage objects

Where symbolic continuity matters, use a separate archetype record:

```text
face_archetype.shaman
face_archetype.challenger
face_archetype.regent
face_archetype.architect
face_archetype.diplomat
face_archetype.sage
```

The archetype record should contain symbolic or historical material, not runtime configuration, player progression, or an altitude judgment.

### Recommended relations

- `expresses_archetype`: a namespaced face/sect/lens draws from a `FaceArchetype`.
- `implements_lens`: a human or runtime agent enacts a `CouncilLens` for a bounded task.
- `routes_to_runtime`: a `ReviewFace` or council assignment selects a `RuntimeSect` or tool.
- `presents_as`: a runtime-generated voice or artifact uses a `PlayerSectIdentity` presentation.
- `affiliated_with`: a player or character chooses or is granted a player-facing sect relation.
- `associated_with_altitude`: records the canonical symbolic association without allowing automatic developmental inference.
- `bound_to_phase`: assigns a face, sect, review role, or voice to an encounter phase.
- `reviewed_by`: attaches one or more `ReviewFace` records to a feature/spec.
- `deliberated_through`: attaches one or more `CouncilLens` records to a council decision.
- `executed_by`: attaches a runtime result to the exact `RuntimeSect` and tool/model configuration.

Every relation should support source, scope, time, confidence, and applicable context. Mappings should be many-to-many unless the governing source explicitly imposes a single route.

### Retrieval contract

For any query containing a face name, retrieval should first classify the task:

| Query intent | Retrieve first |
|---|---|
| Developmental or Integral interpretation | `AltitudeFace` plus anti-global-ranking constraint |
| Execute an agent or strand | `RuntimeSect` plus MCP/tool/runtime rules |
| Review a feature or spec | `ReviewFace` plus routing block |
| Show affiliation, ethos, training, or narrative identity to a player | `PlayerSectIdentity` plus consent/persistence rules |
| Ask the council to reason from a perspective | `CouncilLens` plus council mandate and provenance requirements |

If the intent spans environments, retrieve the relevant records separately and expose their mapping. Do not synthesize them into an unqualified face profile.

### Existing source wording

Existing canonical prose does not need to be silently rewritten for this decision to be usable. When quoting or implementing it, retain its terminology and attach the namespace externally. A future authorized canon-editing pass may decide whether headings should change.

## residual_uncertainty

- `FOUNDATIONS.md` clearly defines altitude faces but does not specify whether altitude describes a whole person, a momentary center of gravity, a response, a character choice, or another scoped unit. This decision prevents inference across namespaces but does not redefine canonical altitude theory.
- The strand specification says sects are player-facing but does not define the persistence, selection, switching, consent, or progression schema of `PlayerSectIdentity`. The identity concept is therefore necessary but structurally incomplete.
- It is not yet clear whether every runtime sect must have a player-facing counterpart or whether some future sects may be execution-only.
- The functional review-face doctrine does not state whether it is parallel to, older than, or intended to replace any earlier review mapping. This decision preserves it as a distinct taxonomy rather than resolving its historical authority.
- The I Ching prework named faces resemble council lenses and runtime roles simultaneously. This decision classifies each invocation by what it is doing; a future schema may model a prework invocation as a `CouncilLensAssignment` executed by a `RuntimeSect`.
- The 3-2-1 GM Voice Sequence mixes Shaman–Sage names with Integrator. Its intended mapping is preserved as a contextual binding, but the reviewed sources do not explain whether Integrator is implemented by Sage, a separate agent, or a presentation voice in that flow.
- Exact version dates for the BARS source files are not declared inside the documents. “When” in this decision therefore means operational layer and process stage, not a reconstructed chronological authoring order.
- The provisional design ontology does not yet encode these namespaces, so this decision currently exists as a conceptual relation contract rather than an implemented schema migration.
