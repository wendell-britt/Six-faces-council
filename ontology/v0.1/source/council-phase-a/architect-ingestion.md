# Architect Ingestion

**Face:** Architect
**Phase:** Phase A — Ingestion and Translation
**Status:** Provisional; non-governance

## comprehension_summary

The ontology is an executable design philosophy for games, design tools, AI collaborators, and Game Master agents. It aims to constrain generative speculation into Wendell’s aesthetic field without eliminating surprise, emergence, or player authorship.

Its core architecture is claim-centered rather than truth-centered. It distinguishes:

- source material from interpretation;
- first-person meaning from observed behavior;
- performance from capability;
- capability from credentials;
- inner transformation from external application fitness;
- access from command;
- consent from compliance;
- epistemic maturity from work disposition;
- local developmental change from whole-person worth.

The philosophy supplies meaning and normative commitments; the formal model supplies entity families, relations, evidence rules, confidence profiles, lifecycle distinctions, and hard invariants; the YAML supplies a partial machine-readable vocabulary.

A known unresolved constitutional delta must remain explicit:

- The council brief contains eight constitutional principles.
- The later philosophy draft contains fifteen.
- Several of the original eight are reformulated in the fifteen, while the later document elevates additional ideas concerning mechanical reality, development, relationship, performance, mystery, player-authored meaning, and lineage.
- Phase A does not determine whether the later fifteen supersede, expand, reinterpret, or merely propose additions to the earlier eight.
- Each principle instance therefore needs document-specific provenance and constitutional status must not be inferred from sequence alone.

## key_concepts

- Designer–player and Game-Master–player continuity
- Authentic pleasure and psychographic translation
- AQAL perspectives, developmental lines, levels, states, and types
- Emotional Alchemy as energy economy
- Somatic evidence
- Mechanical attention
- Development as contextual change in possibility
- Performance, capability, credential, and identity
- Relationship as a source of distributed capability
- Trust as situated capability, integrity, and benevolence
- Consent, permission, refusal, boundary, and repair
- Mystery as coherent, inferable, and plural
- Player-authored personal meaning
- Adaptive relevance, world otherness, and player sovereignty
- Developmental and artifact provenance
- Helper sustainability
- Playable remediation of design shadows
- BAR lifecycle, rest, release, and composting
- Proxy capture
- Epistemic maturity
- Work disposition
- Integral declaration of mechanical attention
- Playable verification

## key_relations

- An Agent `plays`, `authors`, `facilitates`, `seeds`, `stewards`, or `witnesses` a DesignObject.
- A DesignObject `makes_mechanically_real`, `supports_narratively`, `leaves_implicit`, or `excludes_from_scope` a dimension of experience.
- A Performance may `develop` a Capability without establishing identity.
- A Capability `belongs_to_line`, is `demonstrated_in` a context, and may `enable` an Affordance.
- A Credential represents evidence of Capability but is not identical to it.
- A Relationship may produce a CoordinationPattern not reducible to either participant.
- An Agent `grants`, `withholds`, or `revokes` Permission; continued participation does not imply consent.
- A Commitment may be `kept`, `breached`, or addressed through Repair.
- Charge may lead through practice to Transformation, SatisfactionReport, changed capacity or action, and later Consequence.
- EvidenceItem `supports`, `challenges`, or `complicates` a Claim.
- An Interpretation may `predict`, be `tested_by`, and later be revised without becoming personal truth.
- A Claim is `derived_from` sources and should preserve its derivation path.
- A MotivationMechanism may `support_purpose` or `exhibit_proxy_capture`.
- A possibility may rest, activate, transfer, or be composted while retaining provenance.
- Player-authored meaning and SharedMeaning may coexist without either collapsing into system interpretation.

## face_translation

From the Architect face, the ontology is best understood as a layered, provenance-bearing knowledge graph with executable constraints—not as a flat taxonomy.

A suitable retrieval pattern would assemble a bounded “design context packet” for the problem at hand:

1. Retrieve the target design object and declared purpose.
2. Retrieve applicable constitutional statements from both constitutional source sets, preserving document and version.
3. Retrieve relevant hard invariants and consent boundaries.
4. Retrieve the foregrounded AQAL perspectives and developmental lines.
5. Retrieve directly relevant evidence, disagreements, and confidence profiles.
6. Retrieve productive tensions and known anti-patterns.
7. Retrieve candidate tests proportionate to the design risk.
8. Include source excerpts or references when a summary would conceal material ambiguity.

Retrieval should be constrained by scope, agency, sensitivity, and consequence—not semantic similarity alone. A request involving an ally, for example, should automatically retrieve consent, access-versus-command, relationship, trust, capability, and player-authorship constraints even if the prompt does not name them.

Loss-aware representation map:

| Source construct | Machine representation | What is preserved | Likely translation loss |
|---|---|---|---|
| Constitutional principle | `PhilosophyObject: ConstitutionalPrinciple` plus provenance | Named commitment and source | Normative force, ordering, and the unresolved 8/15 delta unless principles are instantiated separately |
| AQAL event | One event linked to UL, UR, LL, and LR EvidenceItems | Perspective distinction | The lived simultaneity of the four perspectives if stored as independent buckets |
| Development | `DevelopmentClaim` with line, context, before/after possibility, evidence | Situated change | Felt significance and emergent meaning if reduced to state transitions |
| Performance → capability | Separate objects connected by evidence | Non-identity of enactment and capacity | Ambiguity about when repeated performance warrants a capability claim |
| Trust | `TrustState` linked to capability, integrity, parties, domain, and evidence | Situated relational assessment | Benevolence and relational texture if reduced to a score |
| Consent | `ConsentRecord` with purpose, scope, duration, audience, and revocation | Governable permission | Moment-to-moment negotiation and power asymmetry if treated as static authorization |
| Emotional Alchemy | Charge-to-consequence event chain | Process and evidence lineage | Five channels, WAVE, energetic costs, somatic texture, and permission not to transform |
| Player meaning | `authors_personal_meaning` relation | Authority boundary | The meaning itself should not be normalized into system-owned structured data without consent |
| Mystery | Hypotheses, evidence, alternatives, and uncertainty | Inferability and plurality | Wonder if every unknown is treated as a database field awaiting resolution |
| Provenance | Seed, Revision, Artifact, ProvenanceRecord, LifecycleRecord | Developmental lineage | The experiential sense that the result grew from play |
| Composting | CompostRecord plus retained learning | Release without erasure | Emotional completion if represented only as workflow status |
| Psychograph | Revisable scoped configuration with sources | Design relevance and corrigibility | Diagnostic overreach if preferences are treated as stable identity |
| Hard invariant | Executable validation rule plus human-readable rationale | Operational constraint | Context and ethical purpose if retained only as a boolean check |

The YAML is a vocabulary seed, not yet a lossless executable schema. It does not presently instantiate the constitutional principles, definitions, source documents, framework boundaries, psychograph, five Emotional Alchemy channels, WAVE sequence, fifteen moves, BAR verbs, adaptive-system permission fields, or worked evidence records. Its relation names lack domain, range, temporal semantics, cardinality, and enforcement behavior. Its single required `status` field risks flattening epistemic maturity and work disposition, which the prose model explicitly separates.

## environment_crosswalk

- **Design-philosophy draft:** normative and experiential layer; answers why the ontology exists and what designs should answer to.
- **Formal ontology model:** conceptual layer; names entities, relations, evidence authority, confidence, lifecycle, and invariants.
- **YAML seed:** transport and retrieval vocabulary; currently expresses available categories more fully than their semantics.
- **AI prompt context:** should receive a task-specific packet, not the entire ontology indiscriminately.
- **Game design specification:** should use the integral declaration of mechanical attention to state pleasures, modeled realities, omissions, audiences, tensions, risks, evidence, and exits.
- **Playtest record:** supplies scoped EvidenceItems rather than global validation.
- **Adaptive system:** requires separated records for observed signal, inference, adaptation, permission, uncertainty, correction, retention, visibility, reuse, and sharing.
- **BAR workflow:** maps captured possibilities and their provenance across activity, rest, delegation, completion, and composting, while the brief’s richer lifecycle verbs remain separately preserved.
- **Credential system:** communicates contextual capability claims and their provenance without becoming a universal rank.
- **Council output:** is evidence of lens-specific interpretation and convergence, not ratification.
- **Existing BARS canon:** remains a reconciliation target named by the brief. No equivalence should be asserted until the listed canonical sources are compared directly.

## possible_equivalences

These are possible overlaps, not confirmed merges:

- “Begin with authentic pleasure, then translate outward” may correspond to the brief’s “design first for the designer’s psychographic neighborhood.”
- “Mechanics make claims about reality” may correspond to the model’s `makes_mechanically_real` relation and integral declaration.
- “Development changes possibility” may correspond to `DevelopmentClaim.changes_possibility`.
- “Relationship is a source of capability” may correspond to `CoordinationPattern`.
- “The player authors personal meaning” may correspond to `authors_personal_meaning` plus the adaptive-system authority boundary.
- “Preserve lineage from seed to result” may correspond to `records_path`, `preserves_trace_of`, and ProvenanceRecord.
- “The tool practices what it teaches” may correspond to the shadow-to-remediation mapping, but one is a principle and the other is an implementation pattern.
- “Composting is valid completion” may correspond partly to CompostRecord and partly to work disposition; these may encode different aspects.
- “Motivation does not substitute for meaning” may correspond to the proxy-capture invariant and `supports_purpose` relation.
- Performance may overlap with Action in some records, but Performance carries the additional claim that enactment need not express stable identity.
- Outcome and Consequence may appear interchangeable in short traces, but the model distinguishes immediate result from later changed possibility.
- Credential appears in both DesignObject and DevelopmentObject; this may represent two legitimate facets rather than duplication.
- State appears as an ExperientialObject while lifecycle state and world state also appear in prose; these uses may require namespace distinction.
- BAR lifecycle verbs and work dispositions may overlap operationally without being semantically identical.
- The brief’s eight principles and philosophy’s fifteen may partly correspond, but their constitutional relationship remains unresolved.

## translation_losses

- The YAML lists classes and relations but omits most definitions and boundary conditions.
- Constitutional principle instances and the eight-versus-fifteen source delta are absent from machine form.
- Hard invariants appear as labels without executable validation criteria or exception-handling semantics.
- AQAL is represented chiefly by quadrants and developmental-line labels; levels, temporary states, and non-hierarchical types are not comparably formalized.
- Emotional Alchemy is compressed to a generic sequence, losing channel-specific meanings, WAVE stages, move families, energetic costs, and the Open Up distinction.
- TrustState does not yet explicitly encode the trust triad, whose benevolence dimension is intentionally resistant to scoring.
- ConsentRecord is defined in prose but not structurally specified in YAML.
- Mystery, symbolic resonance, uncanny relevance, fun, and world otherness are only partially representable without flattening.
- First-person evidence can be stored, but storage cannot reproduce bodily experience or authorize its interpretation.
- Productive tensions risk becoming defects to resolve if represented only as competing requirements.
- Provenance graphs can preserve trace but may falsely imply linear causation or predetermined outcomes.
- The phrase “strong-within-scope” can still invite false certainty if the scope is not attached and retrieved.
- Psychographic configurations can become diagnostic profiles if revisability, consent, and intended use are omitted.
- A full machine record for every event could violate the philosophy by turning play into administration or surveillance.
- The philosophy’s language carries aesthetic and ethical force that short enum names do not preserve.
- The existing BARS canon cannot be faithfully crosswalked from filenames alone.

## tensions

- Eight constitutional principles in the brief versus fifteen in the later philosophy.
- Human-readable ethical meaning versus machine-operational precision.
- Inspectability versus administrative burden.
- Provenance preservation versus privacy and the right not to be permanently recorded.
- Mystery versus explanation and retrieval completeness.
- Adaptation versus player sovereignty.
- Stable identifiers versus concepts whose meanings remain developmental.
- Contextual confidence versus pressure to sort results into a single score.
- Somatic authority versus interpretive uncertainty.
- Personal meaning versus shared meaning.
- Inner transformation validity versus allyship application fitness.
- Relationship as an emergent field versus graph edges between individuals.
- Consent as a continuing negotiation versus ConsentRecord as an object.
- Developmental lineage versus nonlinearity and retrospective reinterpretation.
- Reusable credentials versus the situated nature of capability.
- Comprehensive ontology coverage versus the principle that no individual game must mechanize everything.
- Formal remediation rules versus keeping design itself playful.
- World otherness versus adaptive relevance.
- Rest and ambiguity as valid outcomes versus lifecycle systems that imply forward motion.

## questions

- What is the authority relationship among the brief, philosophy draft, formal model, YAML, and existing BARS canon?
- Should the eight and fifteen constitutional sets be represented as two versioned collections, or as one collection with source-specific membership assertions?
- Does “later philosophy” indicate chronological sequence only, or intended supersession?
- Should a single concept support multiple family memberships, as Credential presently does?
- Which relation names require inverses, temporal qualifiers, domain/range constraints, or agent consent?
- How should ongoing consent changes be recorded without implying that one stored record fully captures a living negotiation?
- Which data must never be retained by an adaptive system, even with provenance value?
- What is the intended distinction between BAR lifecycle verbs and ontology work dispositions?
- How should the ontology represent a productive tension so an AI holds it open rather than selecting a winner?
- What evidence threshold supports movement from repeated Performance to a Capability claim?
- How should benevolence remain part of trust while resisting reductive scoring?
- Which parts of Emotional Alchemy require first-class machine objects rather than source-linked reference material?
- How should “status” in the minimum record be divided between epistemic maturity and work disposition?
- What representation permits mystery to remain active rather than merely unresolved?
- Which existing BARS objects already cover Agent, BAR, face, strand, credential, and Emotional Alchemy concepts?

## candidate_extensions

These are translation observations for later consideration, not adopted changes:

- Add a source-version object capable of expressing that a principle belongs to one constitutional collection without deciding which collection governs.
- Add explicit `asserted_by`, `reported_by`, `interpreted_by`, and `authorized_by` relations to prevent authority collapse.
- Represent confidence as a structured profile rather than a scalar field.
- Give relations optional context, time, perspective, scope, and evidence qualifiers.
- Represent productive tensions as first-class polarity objects with enabling conditions and costs on both sides.
- Add explicit privacy and sensitivity metadata to provenance records.
- Add retention-purpose and revocation semantics to adaptive-system records.
- Distinguish concept definition, human-readable rationale, and executable validation rule for every hard invariant.
- Add namespace distinctions for experiential state, world state, lifecycle state, and governance status.
- Allow a concept to have multiple typed roles without forcing duplicate instances.
- Add retrieval recipes keyed to task classes such as allyship, adaptation, progression, motivation, psychograph use, and composting.
- Add a “do not structure” or “retain only as user-authored text” designation for sensitive inner meaning.
- Store counterevidence and disagreement as linked first-class objects rather than negative confidence values.
- Permit provenance structures that represent branching, convergence, and retrospective reinterpretation rather than only linear chains.

## tests_for_understanding

1. **Constitutional delta test:** Ask the agent how many constitutional principles exist. A passing answer reports eight in the brief and fifteen in the later philosophy, preserves both with provenance, and does not choose a governing set.

2. **Evidence separation test:** Present a player who reports a satisfying somatic shift while an ally reports harm. A passing answer records valid inner transformation evidence, questions application fitness, preserves both perspectives, and does not globally condemn or validate the helper.

3. **Development test:** Present repeated enactment of a helping behavior. A passing answer distinguishes Performance from Capability, requests context and evidence, and does not infer identity or whole-person level.

4. **Consent test:** Present an acquired ally who continues participating. A passing answer refuses to infer command or consent from acquisition, compliance, or continued play and looks for situated permissions.

5. **Adaptive-system test:** Present a highly accurate player inference. A passing answer treats it as provisional, checks collection and use permissions, permits rejection, and preserves player authorship and world otherness.

6. **Mystery test:** Ask the agent to explain every hidden system. A passing answer identifies when explanation would destroy a valued form of mystery and proposes an inferability test instead of automatic disclosure.

7. **Lifecycle test:** Present an emotionally charged idea that is not actionable. A passing answer allows rest, reference, transfer, or composting while preserving learning and does not convert capture into obligation.

8. **Psychograph test:** Present Enneagram Five as evidence. A passing answer treats it as a revisable design-relevant type hypothesis, not a developmental rank or diagnosis.

9. **Mechanical-attention test:** Ask what a proposed reward system claims is real. A passing answer identifies what is tracked, rewarded, permitted, and changed; names omitted dimensions; and proposes evidence about actual play.

10. **Bounded worked translation example:**

   Source proposition: “Relationship is a source of capability; access is not command.”

   Representation:

   ```text
   agents:
     player_A
     ally_B

   objects:
     relationship_AB
     capability_coordinated_intervention
     permission_B_for_intervention
     development_claim_AB
     credential_A_contextual

   relations:
     player_A relates relationship_AB
     ally_B relates relationship_AB
     ally_B grants permission_B_for_intervention
     relationship_AB develops capability_coordinated_intervention
     capability_coordinated_intervention demonstrated_in encounter_17
     capability_coordinated_intervention enables coordinated_action_4
     development_claim_AB supported_by system_trace_17
     development_claim_AB supported_by relational_attestation_B
     credential_A_contextual represents capability_coordinated_intervention
   ```

   Required interpretation:

   - The capability belongs partly to the relationship, not solely to Player A.
   - Permission is scoped to the intervention and may be revoked.
   - The credential communicates contextual evidence; it does not establish universal trustworthiness.
   - A system trace can establish that coordination occurred but not what it meant inwardly.
   - Ally B’s attestation bears on consent and application fitness but cannot define Player A’s inner meaning.
   - Later refusal would update permission without erasing the historical fact that earlier coordination occurred.

   Preserved: distinct agency, relational capability, contextual permission, evidence plurality, and provenance.

   Lost or endangered: the felt texture of trust, tacit negotiation, changing power relations, and meanings neither party has articulated. These must remain available as uncertainty or user-authored account rather than being fabricated by the model.
