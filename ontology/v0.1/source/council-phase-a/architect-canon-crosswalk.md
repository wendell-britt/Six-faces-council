# Architect Canon Crosswalk

**Face:** Architect
**Phase:** Phase A — Canon Reconciliation
**Status:** Provisional comparison; non-governance
**New-ontology source:** `/Users/wendellbritt/Documents/Codex/2026-10-09/so-x20/outputs/council-phase-a/architect-ingestion.md`
**Canon root:** `/Users/wendellbritt/The Library /bars-engine`

This crosswalk records correspondences, conflicts, omissions, and translation risks. It does not edit canon, determine precedence, merge concepts, or make a governance disposition.

## confirmed_matches

### BARs preserve generative potential and provenance

- Canon defines a BAR as a portable kernel: “seeds with provenance” capable of becoming quests, rules, lore, decisions, specifications, plans, norms, or forks. Source: `/Users/wendellbritt/The Library /bars-engine/FOUNDATIONS.md`, **The Kernel Principle**.
- The new ontology treats `Seed`, `Artifact`, `ProvenanceRecord`, `Revision`, `LifecycleRecord`, and `CompostRecord` as first-class objects and requires important claims and artifacts to retain derivation history. Source: `architect-ingestion.md`, **key_concepts**, **key_relations**, and **face_translation**.
- Both models therefore reject treating captured material as an isolated note. Both preserve a path from originating material into later artifacts and consequences.

### Emotional Alchemy is an energy economy, not a morality scale

- Canon explicitly states that Emotional Alchemy is an energy economy rather than a morality wheel and that Control moves are costly precision moves, not bad moves. Sources: `FOUNDATIONS.md`, **Emotional Alchemy (Narrative Movement)**; `/Users/wendellbritt/The Library /bars-engine/.agent/context/emotional-alchemy-ontology.md`, opening definition and **Control translate (high-cost precision)**.
- The new ontology preserves the same boundary and warns against turning Emotional Alchemy into a good/bad emotion taxonomy. Source: `architect-ingestion.md`, **key_concepts** and loss-aware map entry **Emotional Alchemy**.

### The five channels, four-stage elemental WAVE, and fifteen-move grammar correspond

- Canon defines Metal/Fear, Water/Sadness, Wood/Joy, Fire/Anger, and Earth/Neutrality; elemental WAVE is Wake → Clean → Grow → Show; translation occurs only after Show; and the move set comprises five Transcend, five Generative, and five Control moves. Source: `.agent/context/emotional-alchemy-ontology.md`, **5 Elements + Lessons (canonical)**, **WAVE progression per element**, **15 Canonical Moves**, and **Transcend vs Translate**.
- The source philosophy ingested by Architect preserves those same structures, and the ingestion explicitly identifies their loss from the abbreviated YAML. Source: `architect-ingestion.md`, **face_translation** and **translation_losses**.

### Open Up is separate from the canonical four-stage elemental WAVE

- Canon defines the broader personal-throughput sequence as Wake Up → Open Up → Clean Up → Grow Up → Show Up while explicitly stating that Open Up is a BARS-original receptivity/intake concept, is independent of the five elements, and does not force a five-to-five mapping. Source: `FOUNDATIONS.md`, **The Five Dimensions** and **How bars-engine maps to (and renames) Wilber**.
- The ingested philosophy likewise treats Open Up as a broader personal-throughput term that may occur between Wake and Clean without making it a forced fifth element or part of the canonical fifteen-move grammar. This is a substantive match, although the abbreviated machine seed does not retain it.

### Developmental lines and enacted capacity are central in both systems

- Canon locates line development in Grow Up and distinguishes it from vertical altitude. Source: `FOUNDATIONS.md`, **How bars-engine maps to (and renames) Wilber**, especially the Grow Up and Six Game Master Faces rows.
- The new ontology represents development as a contextual change in possibility within a specified line and separates `Performance`, `Capability`, and `Credential`. Source: `architect-ingestion.md`, **key_concepts**, **key_relations**, and **tests_for_understanding**.
- Both make action and capability more important than abstract self-description, although they do not yet use identical schemas for development.

### Allyship has inner/outer and individual/systemic consequences

- Canon places allyship structurally in the outer expression of each move, requires an `AllyshipTarget`, and distinguishes self-development from action affecting an individual, collective, or system. Source: `FOUNDATIONS.md`, **The allyship board — 4 domains × inner/outer (8 cells)** and **Move × aspect — inner allyship / outer allyship**.
- The new ontology separates first-person evidence, observed behavior, shared meaning, and systemic consequence and requires other agents’ consent and attestation when they are affected. Source: `architect-ingestion.md`, **comprehension_summary**, **key_relations**, and the bounded translation example in **tests_for_understanding**.
- Both therefore prevent an interior intention from being treated as sufficient evidence of allyship impact.

### Provenance, forking, and divergence are preserved rather than treated as failure

- Canon makes forking first-class, requires forks to retain provenance and lineage, and permits structural maturity and social adoption to diverge. Source: `FOUNDATIONS.md`, **Evolution: Forking as First-Class Reality** and **Two Axes of Change**.
- The new ontology includes `Seed`, `Revision`, `Artifact`, lifecycle records, `derived_from`, `preserves_trace_of`, and `records_path`; it also preserves disagreement rather than forcing consensus. Source: `architect-ingestion.md`, **key_relations**, **face_translation**, and **candidate_extensions**.

### Privacy and restricted interpretation are shared concerns

- Canon’s implemented 3-2-1 privacy model captures tension-vector structure while excluding raw journal text from literal transmission or persistence. Source: `/Users/wendellbritt/The Library /bars-engine/specs/doctrine/emotional-alchemy-321.md`, **Privacy Model**.
- The new ontology calls for consent records, privacy scope on evidence, retention-purpose and revocation semantics, and a possible “do not structure” designation for sensitive inner meaning. Source: `architect-ingestion.md`, **face_translation**, **translation_losses**, and **candidate_extensions**.
- The exact boundaries differ, but both reject indiscriminate capture of interior material.

### Agent work should be routed through explicit roles and leave an audit trail

- Canon requires GM Face routing in feature specifications and defines primary, secondary, and review faces. Source: `/Users/wendellbritt/The Library /bars-engine/specs/doctrine/gm-faces.md`, **GM Face Routing Block** and **GM Face Routing**.
- Canon strand execution records agent sequence, advocacy, decisions, retrospectives, outputs, and branch linkage in `strandMetadata`. Source: `/Users/wendellbritt/The Library /bars-engine/.specify/specs/strand-system-bars/spec.md`, **Unified Strand-as-BAR Schema**, **Strand Lifecycle**, and **Agent Self-Advocacy (internal)**.
- The new ontology similarly requires provenance for council synthesis and treats council output as attributed interpretation rather than ratification. Source: `architect-ingestion.md`, **environment_crosswalk**.

### Completion and feedback must become legible

- Canon requires major flows to end with a destination, success feedback, or explicit error guidance and calls for lightweight instrumentation. Source: `FOUNDATIONS.md`, **UX: Major Flows Cannot Be Interrupted**.
- The new ontology requires evidence plans and tests, distinguishes outcome from later consequence, and treats completion, rest, and release as explicit possibilities. Source: `architect-ingestion.md`, **key_concepts**, **key_relations**, and **tests_for_understanding**.

## conflicts

### “Six Game Master Faces” names three non-identical structures

1. `FOUNDATIONS.md`, **The Six Game Master Faces = Integral altitude levels**, defines Shaman, Challenger, Regent, Architect, Diplomat, and Sage as the vertical altitude axis corresponding to Spiral Dynamics / Integral altitude.
2. `.cursor/rules/game-master-agents.mdc`, opening section, names shaman, regent, challenger, architect, diplomat, and sage as runtime agents and assigns orchestration tools and Cursor subagents.
3. `specs/doctrine/gm-faces.md`, **The Six Game Master Faces**, defines a different functional set: Ontologist, Systems Architect, Experience Designer, Encounter Designer, Steward, and Integrator.

The new ontology uses Shaman, Challenger, Regent, Architect, Diplomat, and Sage as interpretive orientations and simultaneously forbids assigning a global developmental level to a person or treating type as level. Source: `architect-ingestion.md`, **comprehension_summary**, **key_concepts**, and **tests_for_understanding**.

These structures may be related, but they are not currently interchangeable. Treating a face name as an altitude, runtime agent, design-review responsibility, personal orientation, and developmental assessment without a namespace would materially change meaning.

### The functional Architect and the altitudinal Architect are not coextensive

- In `FOUNDATIONS.md`, **The Six Game Master Faces = Integral altitude levels**, Architect is Orange: rational, strategic, and achievement-oriented.
- In `specs/doctrine/gm-faces.md`, **Systems Architect**, the corresponding function is schema, database, services, API shape, and migration safety.
- In `.cursor/rules/game-master-agents.mdc`, **Tool mapping (bars-agents MCP)**, Architect maps to `architect_draft` and `architect_compile` and to the `generalPurpose` Cursor subagent.
- In the new council ingestion, Architect covers structure, schema, retrieval, provenance, confidence, and representation loss.

These descriptions overlap but have different selection criteria and scopes. No source currently establishes that they are the same object.

### Canonical vertical development and the new ontology’s anti-ranking invariant are not yet reconciled

- Canon explicitly locates vertical developmental levels in the six named faces. Source: `FOUNDATIONS.md`, **How bars-engine maps to (and renames) Wilber** and **The Six Game Master Faces = Integral altitude levels**.
- The new ontology prohibits global developmental ranking of persons and insists that development be contextual to line, relationship, and situation. Source: `architect-ingestion.md`, **comprehension_summary**, **face_translation**, and **tests_for_understanding**.

The statements are not logically incompatible if faces describe a lens used in a bounded event rather than a total person. Canon does not make that limiting rule explicit in the reviewed sections, so the operational interpretation remains in conflict or at least materially under-specified.

### Emotional Alchemy transformation and satisfaction have different formal boundaries

- `specs/doctrine/emotional-alchemy-321.md`, **Emotional Alchemy States**, defines transformation as the 3-2-1 perspective shift and satisfied state as aligned action plus artifact.
- `.agent/context/emotional-alchemy-ontology.md`, **Derivation rules**, uses counts of satisfaction, dissatisfaction, and self-sabotage selections to route a quest toward translate or transcend.
- The new ontology uses `SatisfactionReport` as first-person evidence of transformation validity and allows an Emotional Alchemy sequence to stop before action, artifact, or consequence. Source: `architect-ingestion.md`, **comprehension_summary**, **key_relations**, **translation_losses**, and **tests_for_understanding**.

One system treats satisfaction partly as structured routing input and completed aligned output; the other treats satisfaction primarily as evidence whose authority and limits must be preserved. Their fields should not be assumed equivalent.

### Action-required completion can conflict with rest, refusal, or no-shift as valid outcomes

- Canon states that Show Up quests require an action attestation and that quest threads end with action, with Wake Up as the exception. Source: `.agent/context/emotional-alchemy-ontology.md`, **Mastery and completion rules**.
- The new ontology permits rest, refusal, non-shift, ambiguity, and setting the work down as legitimate outcomes. Source: `architect-ingestion.md`, **key_concepts**, **tensions**, and **tests_for_understanding**.

This may be a scope distinction between a Show Up quest and transformation generally, but that scope boundary is not represented in the new YAML and should not be silently inferred.

### Strand audit field naming is internally inconsistent in the reviewed canon

- `specs/strand-system-bars/spec.md`, **Unified Strand-as-BAR Schema**, names `audit_trail` as load-bearing and says it was renamed from `decision_audit_log`.
- The same file, **Functional Requirements / Phase 1**, still states that FR1 includes `decision_audit_log`, while **Phase 5** uses `audit_trail`.

The new ontology’s generic `ProvenanceRecord` cannot resolve this implementation-level conflict. Phase A records both spellings and the source-local declaration that `audit_trail` is the renamed field without deciding how existing data or code behaves.

### “BAR” has broader canon scope than the new brief’s charged-possibility formulation

- Canon defines BAR as a general kernel able to become a rule, specification, implementation plan, community norm, or fork, not only emotionally charged material. Source: `FOUNDATIONS.md`, **The Kernel Principle**.
- The new ontology package, as summarized in `architect-ingestion.md`, often treats a BAR as captured charged possibility and does not include `BAR` as a first-class type in its abbreviated machine vocabulary.

The new formulation may describe one source pathway into a BAR rather than the whole canonical class, but that distinction is absent from the new schema.

## omissions_in_new_ontology

### Canon structures missing from the new machine model

- The five BARS dimensions—WHO, WHAT, WHERE, Energy, and Personal throughput—are not represented as a corresponding machine structure. Source: `FOUNDATIONS.md`, **The Five Dimensions**.
- The four allyship domains crossed with inner/outer aspect, the eight-cell board, `MoveCellAffinity`, and `AllyshipTarget` are absent. Source: `FOUNDATIONS.md`, **The allyship board — 4 domains × inner/outer (8 cells)** and **Move × aspect — inner allyship / outer allyship**.
- Structural maturity and social adoption are not represented as two independent axes with their canonical stages. Source: `FOUNDATIONS.md`, **Two Axes of Change**.
- Holacratic circles, role/domain-scoped authority, and ratification events do not have direct counterparts. Source: `FOUNDATIONS.md`, **Governance: Holacratic Orientation**.
- Vibeulons, BAR weight, global inspiration reserve, local instance liquidity, attunement, and governance-ratified transmutation are absent. Source: `FOUNDATIONS.md`, **Inspiration as Currency** and **Contextual Inspiration: Attunement and Transmutation**.
- The version-managed-backlog metaphor and its campaign/period/quest, branch/PR/fork, and CYOA correspondences are absent. Source: `FOUNDATIONS.md`, **BARs Engine as Version-Managed Backlog**.

### Emotional Alchemy implementation structures missing from the new model

- The exact fifteen move names, vector format, element cycles, energy deltas, binary legacy moves, derivation algorithm, node assignment, and mastery rules are not encoded. Source: `.agent/context/emotional-alchemy-ontology.md`, **15 Canonical Moves**, **Transcend vs Translate**, **Binary moves**, **Derivation rules**, and **Mastery and completion rules**.
- The implemented code locations—`MovementType`, `EmotionalChannel`, element mapping, move engine, derivation function, and consumers—are absent from retrieval metadata. Source: `.agent/context/emotional-alchemy-ontology.md`, **Schema / Code**.
- The 3-2-1 invariant, four moves, `TensionVector` fields, artifact types, GM voice sequence, routes, and backend pipeline are absent. Source: `specs/doctrine/emotional-alchemy-321.md`, **Core Invariant**, **The Four Moves**, **Tension Vector**, **Artifact Types**, **GM Voice Sequence**, **Routes**, and **Backend Pipeline**.
- The privacy rule distinguishing captured structure from uncaptured raw journal text is not expressed as an executable record-level constraint. Source: `specs/doctrine/emotional-alchemy-321.md`, **Privacy Model**.
- The future session-depth signal is absent. Source: `specs/doctrine/emotional-alchemy-321.md`, **Session Depth Signal (future)**.

### GM routing and runtime retrieval structures missing from the new model

- The functional GM routing block with primary, secondary, and review faces is absent. Source: `specs/doctrine/gm-faces.md`, **GM Face Routing Block** and **GM Face Routing**.
- The Ouroboros mappings and mini-spec → seed → run path are absent. Source: `specs/doctrine/gm-faces.md`, **Mapping to Ouroboros Agents**.
- The runtime requirement to verify bars-agents MCP availability, the prohibition on silently substituting prose, and the documented retry/escalation path are absent. Source: `.cursor/rules/game-master-agents.mdc`, **MCP must be available (do not skip)**.
- The mappings among named faces, Cursor subagents, and MCP tools are absent. Source: `.cursor/rules/game-master-agents.mdc`, **bars-agents as orchestrators, Cursor subagents as tools** and **Tool mapping (bars-agents MCP)**.
- The deterministic-template fallback when `OPENAI_API_KEY` is unavailable is absent from the new ontology’s evidence and retrieval model. Source: `.cursor/rules/game-master-agents.mdc`, opening **Game Master Agents** section.

### Strand schema and orchestration structures missing from the new model

- `CustomBar.type = "strand"`, `strandMetadata`, `agent_sequence`, `phase_temperature`, `output_thread_links`, `audit_trail`, `branch_reference`, and nullable `thread_linkage` are absent. Source: `specs/strand-system-bars/spec.md`, **Unified Strand-as-BAR Schema**.
- Strand types, trigger surfaces, API input/output, branch naming, player hooks, and replay requirements are absent. Source: the same file, **Strand Types**, **API Contracts**, **Functional Requirements**, and **Non-Functional Requirements**.
- Before/during/after self-advocacy payloads and their advisory semantics are absent. Source: the same file, **Agent Self-Advocacy (internal)** and **Functional Requirements / Phase 5**.
- The L1/L2/L3 hierarchy, dodo-to-sect mapping, and Ethos-to-Stat mapping are absent. Source: the same file, **Agent Hierarchy (BARS-Adapted)** and **Functional Requirements / Ethos→Stat**.

## additions_in_new_ontology

The following structures appear in the new ontology ingestion but are not explicit in the six reviewed canon files:

- A general claim/evidence ontology distinguishing `Observation`, `Interpretation`, `Hypothesis`, `Finding`, `Uncertainty`, `Disagreement`, and `Test`.
- A structured confidence profile covering source proximity, evidence diversity, repeatability, contestation, interpretive distance, maturity, and scoped confidence.
- Explicit evidence-authority limits for player statements, somatic reports, behavioral observations, relational attestations, system traces, artifacts, research, AI inference, council synthesis, and playtests.
- The distinction between epistemic maturity and work disposition.
- `DevelopmentClaim` as a contextual before/after change in possibility rather than a general level.
- Explicit separation of `Performance`, `Capability`, `Credential`, and identity.
- `TrustState`, `ConsentRecord`, `Boundary`, `Repair`, `CoordinationPattern`, and `SharedMeaning` as general relational objects.
- Separate consent permissions for collection, retention, explanation, visibility, reuse, and sharing in adaptive systems.
- Player correction and rejection of AI interpretations, plus the invariant that personal meaning remains player-authored.
- Adaptive-world otherness: the world must contain causes and meanings not exhausted by a player model.
- A psychograph family including pleasure signatures, design shadows, audience hypotheses, types, desired states, and accessibility needs.
- An integral declaration of mechanical attention with intended pleasure, modeled reality, exclusions, favored and burdened types, invited states, risks, evidence plan, and exit/rest.
- Explicit anti-proxy-capture and anti-global-ranking invariants.
- Productive tensions represented as material to preserve rather than contradictions to eliminate.
- A general right to rest, refuse, remain unchanged, leave ambiguity unresolved, or compost a possibility.
- A proposed bounded retrieval packet that selects ontology fragments by task, agency, sensitivity, consequence, source, and authority rather than semantic similarity alone.

These are additions relative to the reviewed canon corpus, not findings that they should be adopted into canon.

## changed_meanings

### Face

- Canon meaning A: an Integral altitude level (`FOUNDATIONS.md`, **The Six Game Master Faces = Integral altitude levels**).
- Canon meaning B: a functional design-review discipline (`specs/doctrine/gm-faces.md`, each face section).
- Canon meaning C: a runtime agent/sect with MCP and subagent mappings (`.cursor/rules/game-master-agents.mdc`, **Game Master Agents**; `specs/strand-system-bars/spec.md`, **Agent Hierarchy**).
- New-ontology meaning: an interpretive orientation used to translate an ontology without replacing it (`architect-ingestion.md`, metadata and **face_translation**).

### Architect

- Canon uses Architect for Orange altitude, backlog stewardship, structural design, a BARS sect, an Ouroboros Artificer mapping, and a schema/API review function across different documents.
- New ontology uses Architect chiefly for loss-aware representation, retrieval, provenance, and executable constraints.
- Retrieval by the bare term `Architect` will therefore be unsafe without namespace and task context.

### BAR

- Canon: general portable kernel and version-managed unit that may become many artifact types (`FOUNDATIONS.md`, **The Kernel Principle** and **BARs Engine as Version-Managed Backlog**).
- New ontology: often a captured unit of charged possibility with lifecycle provenance; the YAML does not instantiate BAR as its own class.
- The emotional origin of a BAR is therefore more central in the new description than in the broad canonical class.

### Development

- Canon: Grow Up covers developmental lines; six faces carry vertical altitude; BARs also develop through structural maturity and social adoption (`FOUNDATIONS.md`, **How bars-engine maps to (and renames) Wilber**, **The Six Game Master Faces**, and **Two Axes of Change**).
- New ontology: any contextual change in possibility across distinct lines, explicitly barred from becoming aggregate personal worth.
- “Development level” and “development claim” cannot be treated as the same schema field.

### Transformation and satisfaction

- Canon 3-2-1: transformation is the perspective shift; satisfied is aligned action plus artifact (`specs/doctrine/emotional-alchemy-321.md`, **Emotional Alchemy States**).
- Canon quest derivation: satisfaction is countable selection data used alongside dissatisfaction and shadow scores (`.agent/context/emotional-alchemy-ontology.md`, **Derivation rules**).
- New ontology: transformation is broader change in relationship to charge, meaning, capacity, action, relationship, or artifact; satisfaction is first-person evidence of inner validity.

### Provenance

- Canon: lineage among BARs, strands, outputs, git branches, forks, and runtime artifacts (`FOUNDATIONS.md`, **Evolution: Forking as First-Class Reality**; `specs/strand-system-bars/spec.md`, **Unified Strand-as-BAR Schema** and **Phase 3: Git + Provenance**).
- New ontology: also includes epistemic derivation, interpretive authority, evidence limits, and the developmental path from seed through consequence.
- The new meaning is broader and cannot be stored solely as branch and BAR identifiers.

### Composting

- Canon: creative metabolism of past authored material and past selves into new creative energy (`FOUNDATIONS.md`, **Creative Composting: Metabolizing the Past Self**).
- New ontology: a general valid completion that releases implementation obligation while retaining learning and lineage.
- These meanings overlap through metabolism and reuse but operate at different scopes.

### State and status

- Canon uses emotional altitude states, quest state, world or instance state, structural maturity, adoption stage, and implementation status in different schemas.
- The new ontology adds experiential `State`, epistemic maturity, work disposition, and a generic required `status` in its minimal record.
- A single unqualified `state` or `status` field would collapse non-equivalent axes.

### Agent output and synthesis

- Canon strand synthesis is coordinator output persisted through BAR metadata and an audit trail (`specs/strand-system-bars/spec.md`, **Strand Lifecycle**).
- New ontology treats council synthesis as an attributed evidence type that does not by itself confer empirical validity or ratification.
- Persistence and synthesis authority are therefore distinct in the new model but not explicitly separated in the strand schema.

## unresolved_authority_questions

- How do the provisional council brief, provisional philosophy/model/YAML package, `FOUNDATIONS.md`, implemented canonical Emotional Alchemy documents, GM doctrine, always-applied Cursor rules, and resolved strand specification rank by domain?
- Does “canonical (implemented)” in `specs/doctrine/emotional-alchemy-321.md` control only the 3-2-1 product flow, or also the general definition of transformation and satisfaction?
- Does `.agent/context/emotional-alchemy-ontology.md` govern all Emotional Alchemy semantics, including the new ontology’s first-person satisfaction authority, or only Quest Grammar compilation?
- Which six-face schema is authoritative for which context: Integral altitude, design-review function, runtime sect, council lens, or player-facing identity?
- Does the prohibition on whole-person developmental ranking constrain the canonical altitude-face system, and if so, how should an altitudinal choice be scoped?
- Is the functional six-face doctrine in `specs/doctrine/gm-faces.md` current, legacy, complementary, or superseded relative to the named six sects? No reviewed source states this.
- Is `audit_trail` authoritative over the lingering `decision_audit_log` reference in strand FR1, and what migration or compatibility behavior exists?
- Is a BAR’s canonical class unrestricted kernel, charged kernel, or a parent class with charged BAR as subtype?
- Do BAR structural maturity, social adoption, epistemic maturity, and work disposition remain four independent axes?
- Which source governs consent and privacy for psychographs, somatic reports, AI adaptation, and player-derived world material beyond the implemented 3-2-1 raw-text rule?
- May council outputs be stored as strand `audit_trail` data, or do they require first-class evidence, disagreement, and confidence records to preserve their epistemic status?
- Does the runtime deterministic fallback count as a valid ontology translation, degraded execution, or failure when a council task requires genuine synthesis?
- Are self-advocacy objections merely advisory in every strand, as current Phase 5 requirements state, or can an ethical/privacy objection halt execution?
- Does Open Up remain solely a throughput move, or should it become a first-class source/intake term in the new ontology’s Emotional Alchemy event chain?
- What is the source of authority for the brief’s eight constitutional principles versus the later philosophy’s fifteen? This pre-existing Phase A delta remains unresolved.

## translation_losses

### Losses when canon is translated into the new ontology

- The five-dimensional BARS world model becomes a generic set of agents, design objects, and relations; WHO/WHAT/WHERE/Energy/throughput topology disappears.
- The eight-cell allyship board loses its authored spatial relationship among domain, aspect, move, and target.
- Named Emotional Alchemy moves become a generic Charge → Transformation → Consequence chain, losing exact cycles, energy costs, vector format, derivation rules, and completion requirements.
- 3-2-1 loses its invariant person-shift sequence, tension-vector field contract, product routes, and data-minimization implementation.
- BAR economics lose Vibeulons, weight, attunement, local liquidity, and ratified transmutation.
- BAR evolution loses the explicit distinction between structural maturity and social adoption.
- Strand execution loses its concrete metadata schema, triggers, API contract, self-advocacy payloads, background execution, replay requirement, and git linkage.
- Runtime retrieval loses the fact that MCP availability, environment configuration, and tool invocation are prerequisites for particular kinds of agent output.
- Functional GM review responsibilities become ambiguous when translated into the named face vocabulary.
- Canonical metaphors—kernel, Yellow Brick Road, kiln, fuel, road, and ecology—lose some of their motivational and explanatory force in a neutral graph representation.

### Losses when the new ontology is translated into current canon schemas

- A strand `audit_trail` can retain events and rationales but has no defined structure for claim scope, source proximity, repeatability, contestation, interpretive distance, or evidence limits.
- `strandMetadata` records which sect ran, not which ontology fragment it used, which source version authorized it, or which alternative interpretation it rejected.
- Canon BAR provenance can link branches and outputs but does not by itself preserve personal-meaning authority or distinguish observation from inference.
- Current face routing selects responsibility but cannot encode the unresolved differences among altitudinal, functional, runtime, and council meanings.
- Emotional Alchemy derivation scores can route narrative movement but cannot represent a first-person satisfaction report’s authority and limits without additional context.
- The 3-2-1 tension vector captures structured interior material but does not express separate permissions for explanation, retention, visibility, reuse, sharing, and adaptation.
- Current schemas do not carry productive tensions as first-class objects, so a consumer may resolve them accidentally.
- Rest, refusal, unchanged experience, and unresolved ambiguity are not consistently represented as successful terminal states across quest and strand flows.
- A generic `status` or BAR type cannot carry epistemic maturity, work disposition, structural maturity, adoption, quest completion, and implementation state without namespace loss.

### Retrieval-specific losses

- Filename or embedding similarity alone can return a semantically relevant but authority-inappropriate source—for example, functional GM faces when the task concerns altitude, or provisional ontology prose when implementing canonical quest grammar.
- The same surface terms—Face, Architect, Grow Up, State, Transformation, Satisfaction, BAR, maturity, and provenance—carry different meanings across sources.
- The current reviewed canon does not expose a unified source registry containing document status, scope, implementation binding, version, and supersession relation.
- The new ontology’s proposed context packet lacks direct pointers to current BARS code and runtime prerequisites unless canon links are added at retrieval time.
- Summarization can erase negative constraints such as “translation only after Show,” “raw journal text is not captured,” “thread_linkage is a nullable stub,” and “do not silently substitute prose for required MCP.”
- Retrieving only a final synthesis can conceal agent disagreement and the provenance needed to distinguish council convergence from empirical evidence.

## comprehension_impact

An agent can accurately recite the new ontology and still fail BARS-specific comprehension if it:

- treats the six named faces only as council lenses and misses their canonical altitude or runtime-agent uses;
- uses the functional six-face taxonomy as a replacement for the named sects;
- inserts Open Up into elemental WAVE as a fifth stage;
- translates between Emotional Alchemy elements before Show;
- treats a generic satisfaction report as interchangeable with quest derivation satisfaction inputs or 3-2-1 completed satisfaction;
- stores raw 3-2-1 journal text because the general provenance model rewards completeness;
- models every BAR as emotionally charged and misses its broader kernel role;
- collapses structural maturity, social adoption, epistemic maturity, and work disposition into one progress field;
- produces a council synthesis without a strand BAR, audit trail, or output provenance where the BARS strand system is in scope;
- silently produces an inline “Sage” answer when the requested workflow requires bars-agents MCP;
- ignores runtime fallback and mistakes deterministic templates for full multi-agent synthesis.

Conversely, an agent can follow the reviewed BARS canon and still fail the new ontology’s comprehension requirements if it:

- treats an altitude face as a whole-person rank;
- treats an audit trail or system trace as proof of personal meaning;
- allows a credential, score, or quest completion to become a global capability judgment;
- infers consent from participation, disclosure, acquisition, or continued play;
- treats aligned action or artifact production as sufficient proof of inward satisfaction;
- treats council synthesis as ratification or empirical verification;
- resolves productive tensions because the runtime schema has no place to store them;
- retains sensitive adaptive material merely because provenance is valued;
- makes every captured possibility an obligation to implement.

For comprehension-sensitive retrieval, the Architect identifies the following requirements without adopting a final schema:

1. Retrieve by **task domain and authority scope**, not terminology alone.
2. Attach exact source path, section, status, and implementation binding to each retrieved fragment.
3. Namespace overloaded terms such as face, Architect, state, maturity, transformation, and satisfaction.
4. Retrieve applicable negative constraints alongside positive definitions.
5. Include direct code/schema references for implementation tasks and philosophy/evidence records for interpretive tasks.
6. Preserve unresolved conflicts in the context packet instead of blending them into smooth prose.
7. Distinguish canon, implemented canon, runtime rule, resolved specification, provisional ontology, council inference, and candidate extension.
8. Require the consumer to state which meaning of an overloaded term it is using.
9. Preserve the reviewed source’s data-minimization rule when provenance and privacy compete.
10. Test comprehension through bounded application: the agent should correctly route one Emotional Alchemy event, one GM responsibility, one BAR lifecycle event, and one strand output while naming any unresolved authority conflict it encounters.

The principal Phase A conclusion is not that the new ontology and BARS canon disagree globally. They share a substantial concern with provenance, emotional energy, contextual development, allyship, agency, forking, and meaningful action. The primary comprehension risk is **semantic overloading across layers**: the same words currently name altitudes, roles, runtime agents, evidence states, product states, and philosophical commitments. Any later operational synthesis will need to preserve those source distinctions before it can safely propose mappings.
