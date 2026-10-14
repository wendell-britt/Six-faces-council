# Privacy and Consent Authority — Reconstruction and Ontology Decision

**Date:** 2026-10-14

**Status:** Binding v0.1 ontology decision

**Scope:** Personal and creative data collection, processing, persistence, derivation, personalization, explanation, visibility, reuse, sharing or publication, analytics or evaluation, model improvement, retention, correction, deletion, and revocation

**Does not authorize:** Any collection or use, waive legal duties, define a product privacy policy, or certify the present BARS implementation as compliant

## Question resolved

Which permission objects and authorities govern TensionSnapshots, psychographs, somatic reports, adaptive inferences, generated world material, creative-source corpora, council records, exports, analytics, model improvement, deletion, and revocation? How do those permissions change over time and propagate through descendants?

## Reconstruction: what exists

The ontology already distinguishes `Permission`, `ConsentRecord`, `Boundary`, `PurposePermission`, evidence authority, provenance, and downstream lineage. It also requires separate purposes for collection, local processing, persistence, derivation, artifact generation, personalization, world adaptation, reuse, sharing, analytics, model improvement, correction, deletion, and revocation. Those distinctions were commitments without a complete authority or lifecycle grammar.

The canonical BARS 3-2-1 doctrine says raw journal text is not captured and structured tension material is. Current implementation complicates that claim. `Shadow321Session` persists serialized phase snapshots; `persist321Session()` creates a witness BAR from parts of those snapshots; and a completed naming flow may copy a name, a charge excerpt, and metadata into NPC merge records. The public privacy page says agents treat what they see as ephemeral and never as a persistent profile. These are materially different claims about what is collected, persisted, derived, and reused.

Structured extraction can reduce exposure but does not anonymize a record, remove its intimacy, or authorize another purpose. A generated world element may cease to look like its source while remaining a derivative governed by that source's permission envelope.

## Reconstruction: where authority operates

- **The represented person** governs use of their reported interiority, somatic reports, psychograph, identity or likeness, and person-specific inferences, subject to other affected people's independent rights.
- **The source author or rights-holder** governs creative-source use within their actual authority. Authorship alone does not settle third-party privacy, likeness, contract, or shared-work rights.
- **Each affected participant** governs their own contribution and visibility in relational, multiplayer, or council material. One participant cannot grant another's consent.
- **A role steward or operator** may administer records only within an already authorized purpose. Administrative access is not authority to create a new purpose.
- **A designer or Game Master** may govern authored world material within scope, but cannot publish or repurpose player-derived material merely because it entered the game world.
- **The ontology owner or council** may govern official ontology and council records, while quoted, personal, third-party, or confidential contributions keep their own authorities.
- **The receiving audience or institution** may impose additional safety, confidentiality, or publication conditions; it cannot enlarge the source permission.
- **Law, contract, safety, and platform duties** may narrow or require handling outside this ontology. They never convert a prohibited purpose into player consent.

When authorities conflict, the permitted action is the intersection of their scopes. A more restrictive applicable limit wins for that action. A conflict may require redaction, separation, mediation, nonpublication, or abandonment; it does not justify silent expansion.

## Reconstruction: when claims become available

1. A `DataSubjectClaim` identifies whose person, contribution, or rights are implicated; it remains correctable.
2. A `DataAssetRecord` identifies the source material or record, sensitivity, provenance, current location, controllers or stewards, and known subjects.
3. A `PermissionGrant` or `PermissionRefusal` states an authority's decision for a specific purpose envelope.
4. A `ConsentRecord` records that decision, its notice version, context, evidence, and time. It proves only what was recorded then.
5. A `ProcessingEvent` records an actual collection, access, transformation, disclosure, export, or deletion attempt.
6. A `DerivationRecord` links inferences and generated descendants to sources and inherited restrictions.
7. A `CorrectionRecord`, `RevocationRecord`, or `DeletionRequest` changes future authority or challenges existing records.
8. A `PropagationRecord` documents the action taken for known copies and descendants, including failures and irreversible disclosures.
9. A `ResidualObligationRecord` preserves only obligations that must survive content deletion, without retaining the deleted content or rejected interpretation.

## Decision

### 1. Permission is a purpose envelope, not a boolean

`PermissionGrant` binds all of the following:

- granting authority and represented subject;
- data categories and source records;
- purpose and permitted operations;
- processor or role;
- audience, visibility, and destination;
- context or world;
- start, duration, review point, and retention limit;
- explanation and correction route;
- descendant and export policy;
- revocation and deletion behavior;
- notice version and evidence of the grant.

Omitted dimensions are not silently granted. Bundled permission may describe a product choice for convenience, but enforcement and revocation remain purpose-specific.

### 2. The purposes remain distinct

Collection, transient processing, persistence, derivation, personalization, explanation, visibility, reuse, sharing or publication, export, analytics or evaluation, model improvement, retention, correction, deletion, and revocation are separate operations.

Permission to process within one encounter does not authorize persistence. Persistence does not authorize derivation. Personalization does not authorize multiplayer visibility. Publication does not authorize model improvement. An export gives the authorized recipient a copy; it does not remove the source's restrictions or create onward-sharing authority.

### 3. Consent is current action; a ConsentRecord is historical evidence

Consent is an agent's situated authorization at the point an action is proposed or performed. A `ConsentRecord` is evidence that a grant, refusal, or condition was recorded at a prior time. It is not a permanent proxy for present willingness.

A prior grant can authorize a later operation only while its purpose envelope still covers that operation and no expiry, material context change, correction, refusal, boundary, or revocation has intervened. High-sensitivity, surprising, public, relational, or materially changed uses require renewed confirmation. Continued play, disclosure, silence, completion, access, purchase, authorship, or prior consent does not renew consent.

### 4. Every derivative inherits a permission envelope

`PermissionEnvelope` is the effective intersection of all applicable grants, refusals, boundaries, source restrictions, and duties for an operation. A `DerivationRecord` carries that envelope to TensionSnapshots, psychographs, adaptive inferences, generated world material, BARs, NPC memories, council syntheses, analytics rows, embeddings, caches, exports, and model artifacts.

Derivation cannot launder sensitivity or authority. Aggregation or de-identification may reduce risk only when re-identification and small-group inference are proportionately tested; it does not automatically release purpose, deletion, or model-improvement restrictions.

When multiple sources contribute, the descendant receives the intersection of their applicable permissions unless a documented transformation and authority review establishes a lawful, non-identifying independent record. Uncertainty resolves toward non-expansion.

### 5. Data classes carry minimum handling rules

- **TensionSnapshots and somatic reports:** private by default; encounter processing does not imply persistence, world adaptation, analytics, or sharing.
- **Psychographs and adaptive inferences:** proposal-only, visible and correctable to the represented person when used consequentially, never diagnostic by default, and prohibited from hidden eligibility, pricing, rank, or punishment decisions.
- **Generated world material:** records its source lineage and visibility. It may be playable without exposing the private source, but private lineage still constrains reuse and publication.
- **Creative-source corpora and derived voices:** use the granular `ReuseAuthorization` boundary and retain source, attribution, identity, audience, model-use, and deletion constraints.
- **Council records:** official decisions may be durable; personal, quoted, secret, or third-party material is minimized, redacted, or separately permissioned. Deliberation access does not imply public publication or training use.
- **Exports:** are purpose-bound disclosures with manifest, recipient, time, sensitivity, and onward-use constraints. A player export must not silently include other people's protected material.
- **Analytics and evaluation:** default to the minimum events and fields needed for a named question. Product analytics, safety evaluation, research, and public reporting are different purposes.
- **Model improvement:** is never implied by service delivery, analytics, council participation, or creative reuse. It requires an explicit data class, model or model-family purpose, processor, retention, and withdrawal policy.

### 6. Refusal and privacy preserve the core game

A person may refuse persistence, personalization, reuse, analytics beyond essential operations, public sharing, or model improvement without losing baseline craft, core progress, power, credentials, or belonging. A system may offer a local, ephemeral, fictionalized, preset, manual, or non-adaptive route. If a feature genuinely cannot operate without a category, it must state that dependency before collection and provide an honest exit rather than coercive degradation.

### 7. Corrections change claims; revocation changes future authority

A `CorrectionRecord` changes or contests content, attribution, subject identity, or inference. A `RevocationRecord` withdraws a previously granted purpose from its effective time forward. Neither rewrites the historical fact that an earlier authorized event occurred.

After correction or revocation the system must stop the affected future operation, update active profiles and retrieval, propagate the change to reachable descendants and processors, quarantine or review ambiguous descendants, and report material limits. Already published or independently held copies may be impossible to recall; that limitation must have been disclosed and must be recorded, not used to deny the revocation.

### 8. Deletion is a disposition with verified scope

A `DeletionRequest` names subjects, records, purposes, copies, descendants, exports, backups, caches, embeddings, analytics, and model artifacts in scope. A `DeletionDisposition` records deleted, anonymized with a stated test, retained under a named obligation, unreachable, or contested for each class.

Deletion removes content and future use; it is not composting, archival, hiding, account deactivation, or mere exclusion from the interface. Backups may use bounded delayed deletion only when isolated from ordinary processing and covered by a documented expiry. A minimal tombstone may retain request, authority, time, scope, and completion evidence, but not the deleted content or rejected personal claim.

Model artifacts require an honestly stated capability. If example-level removal or unlearning is unavailable, the system must stop future inclusion, remove accessible source and derived datasets, prevent retraining from them, record the limitation, and never promise retroactive erasure it cannot verify.

### 9. Safety access does not become general reuse

Emergency, integrity, abuse-prevention, or legal processing must be separately named, narrowly scoped, access-controlled, logged, and retained only as required. It does not authorize personalization, creative reuse, analytics unrelated to the incident, publication, or model improvement. A safety claim cannot be used as a catch-all permission.

### 10. Explanations reveal claims without exposing protected sources

When an adaptive inference or derivative affects play, the person receives a usable account of what category of information shaped it, for what purpose, and how to correct or disable it. Explanation does not require revealing another person's private contribution, protected council deliberation, or security-sensitive detail. Where those duties conflict, the system narrows or withdraws the consequential use rather than demanding disclosure from another subject.

## Lifecycle

`proposed → granted | refused → active → renewed | narrowed | expired | revoked`

A processing event is allowed only against an active `PermissionEnvelope`. Material purpose, processor, audience, sensitivity, world, or model changes create a new proposal rather than silently editing the old grant. Refusal, expiry, and revocation are normal states, not errors or evidence about inner resistance.

## Minimum implementation tests

1. **Purpose-separation test:** granting session processing does not enable persistence, personalization, analytics, sharing, export, or model improvement.
2. **Snapshot truth test:** the interface, schema, and processing trace agree on every field persisted and every descendant created.
3. **Living-consent test:** an old ConsentRecord cannot authorize a materially changed or high-sensitivity use without a still-valid envelope or renewal.
4. **Lineage test:** a private source creates a generated world object, BAR, inference, council synthesis, export, and analytic row; each descendant retains the effective restrictions.
5. **Multi-subject test:** one participant cannot publish or export another participant's protected contribution.
6. **Correction test:** rejecting a psychographic or adaptive inference removes it from active personalization and marks reachable descendants without recasting rejection as resistance.
7. **Revocation test:** revoking world adaptation stops new adaptation while preserving only permitted historical facts and residual obligations.
8. **Deletion test:** deletion enumerates primary records, copies, caches, backups, embeddings, exports, analytics, and model datasets, then reports the disposition of each.
9. **Export test:** an export carries a manifest and excludes or redacts material outside the requester's authority.
10. **Model-improvement test:** service use, analytics, creative reuse, and model improvement remain independently disabled unless explicitly granted.
11. **Non-coercion test:** refusing optional sensitive uses preserves the core game and quality floor.
12. **BARS reconciliation test:** the 3-2-1 privacy copy, serialized snapshots, witness BAR creation, and NPC merge propagation are described consistently or the feature fails closed.

## AI guardrails

An AI collaborator must not:

1. infer consent from disclosure, participation, silence, purchase, completion, authorship, or a stored record alone;
2. treat structured extraction, aggregation, pseudonymization, or generation as automatic anonymization;
3. use private material for a new purpose because it is technically accessible;
4. hide data collection or reuse to preserve mystery or personalization;
5. diagnose a person from a psychograph, somatic report, or adaptive inference;
6. treat correction, refusal, deletion, or revocation as resistance or loss of trust;
7. publish relational or council material on the authority of only one affected participant;
8. promise deletion, recall, or model unlearning that the implementation cannot verify;
9. preserve content in a provenance log after the authority to retain that content ends;
10. degrade baseline play to pressure consent to optional data uses.

## Result

Privacy authority now travels with the material. Consent is the situated authorization; a ConsentRecord is evidence of a past decision; a PermissionEnvelope determines whether a concrete operation is allowed now. Every derivative inherits applicable restrictions, and correction, revocation, and deletion propagate through recorded lineage with honest residual limits. Existing BARS behavior remains implementation evidence to reconcile, not proof that these permissions were granted.
