# BAR Scope — Reconstruction and Ontology Decision

**Date:** 2026-10-12

**Status:** Binding v0.1 ontology decision

**Scope:** BAR identity, charge, provenance, kernelhood, expressions, portability, and lifecycle

**Does not authorize:** BARS schema migration, automatic conversion of repository objects into BARs, or lifecycle/work-disposition unification

## Question resolved

Is a BAR any provenance-bearing object, a charged kernel, or a parent class with charged BAR as one subtype?

## Reconstruction: what exists

`FOUNDATIONS.md` defines a BAR as a **kernel**: a compressed unit of potential, small enough to carry and rich enough to bloom. It says BARs are **seeds with provenance** and may become quests, rules, lore, design decisions, feature specifications, implementation plans, community norms, or forked branches of reality.

The ontology council brief later narrows this to “a captured unit of charged possibility with provenance.” Emotional Alchemy supplies a clear charged route into BAR creation, but the canonical examples include many non-emotional kernels. Charge is therefore one source and energetic condition of a BAR, not a requirement for BAR identity.

At the same time, provenance cannot be sufficient by itself. Artifacts, commits, audit events, TensionSnapshots, evidence records, and completed quests may all possess provenance without functioning as portable kernels of potential.

## Reconstruction: where BAR operates

- **Capture:** a possibility receives enough identity and form to be carried.
- **Design and production:** a BAR may seed a specification, plan, implementation, rule, or artifact.
- **Play:** a BAR may seed a quest, piece of lore, relationship possibility, world change, or reward path.
- **Emotional Alchemy:** charge may crystallize into a BAR or route into another artifact family.
- **Governance:** roles or circles may steward, ratify, fork, transfer, or retire a kernel within scope.
- **Versioned worlds:** a kernel may preserve lineage while producing multiple expressions or forks.

## Reconstruction: when BAR identity begins and ends

BAR identity begins at **intentional capture**, not at the first appearance of an idea, feeling, request, note, or artifact. A candidate becomes a BAR when an authorized agent declares it a kernel and the minimum identity and provenance contract is satisfied.

A BAR may remain dormant, be expressed in multiple forms, fork, merge, ship, or be composted. Its current expression and lifecycle state can change without erasing its lineage. Composting can end active obligation without deleting the historical BAR record.

An existing object may later be promoted into a BAR, but the promotion is a recorded event. Provenance is preserved; identity is not retroactively assumed.

## Decision

### 1. BAR is a first-class kernel type

A `BAR` is:

> An intentionally captured, portable kernel of potential with stable identity and provenance, stewarded so it can bloom, be revised, fork, combine, rest, ship, or be released across one or more expressions.

The required properties are:

- intentional capture as a kernel;
- stable identity;
- compressed potential rather than exhaustive realization;
- provenance sufficient to locate origin and lineage;
- at least one plausible expression, development, or transfer context;
- a steward, owning scope, or explicitly unowned state;
- lifecycle and version history;
- portability and permission policy.

### 2. Provenance is necessary but not sufficient

Every BAR has provenance. Not every provenance-bearing object is a BAR.

A note, artifact, log, commit, report, prompt, quest, rule, or specification becomes a BAR only when it is intentionally captured as a reusable kernel and meets the BAR identity contract. Otherwise it may remain source material, evidence, an expression, an artifact, or a lifecycle record linked to a BAR.

### 3. Charge is optional

A `ChargedBAR` is a BAR whose source or active energy includes a represented charge. It is a specialization or scoped role of BAR, not the parent definition.

Other BAR source modes may include:

- request;
- observation;
- inspiration;
- opportunity;
- problem;
- design idea;
- decision;
- rule or norm proposal;
- lore or world seed;
- imported artifact;
- fork of an existing BAR.

Charge may be added, transformed, depleted, renewed, or disputed without determining whether the kernel remains a BAR.

### 4. Kernel and expression remain distinct

A `BARExpression` is a form through which a BAR presently acts or becomes legible: quest, rule, lore, design decision, feature specification, implementation plan, community norm, branch, encounter seed, or another declared form.

The BAR is not reducible to any one expression. One BAR may have several expressions; one expression may combine several BARs. When an expression is itself intentionally preserved as a generative kernel, it may also receive BAR identity through an explicit promotion record.

This avoids two collapses:

- treating every output as a BAR merely because a BAR produced it;
- treating a BAR as destroyed when one expression completes, fails, or is composted.

### 5. Capture is not obligation

BAR capture does not require active implementation. The BAR may be planted, stewarded, grafted, stored, forked, harvested, shipped, composted, or left dormant. These lifecycle verbs do not automatically equal epistemic maturity, work disposition, structural maturity, social adoption, quest completion, or implementation status.

### 6. Portability is governed, not absolute

Portable means the kernel has enough identity and provenance to move across appropriate contexts. It does not mean unrestricted copying, disclosure, reuse, or authority.

A `BARPortabilityPolicy` records:

- permitted worlds, projects, audiences, and purposes;
- ownership and stewardship;
- privacy and sensitivity;
- licenses or sharing constraints;
- required context and dependencies;
- whether charge-derived or personal material must be transformed, redacted, summarized, or excluded;
- fork and recombination permissions.

### 7. Provenance preserves lineage without claiming equivalence

A `BARProvenanceRecord` minimally identifies source, author or capturing agent, capture time and context, predecessor relations, source permissions, and version. Relations distinguish `derived_from`, `expresses`, `forked_from`, `grafted_from`, `revises`, `implements`, `instantiates`, `harvested_from`, and `composted_from` rather than reducing them all to ancestry.

### 8. BAR promotion and demotion are explicit

`BARPromotion` records that existing material has been accepted as a kernel. `BARRoleRelease` records that an object no longer needs to function as an active BAR while preserving its historical identity and lineage. Release may accompany shipping, archival, absorption into another BAR, or composting; it does not rewrite the past.

## Classification test

Before calling something a BAR, ask:

1. Was it intentionally captured as a kernel rather than merely recorded?
2. What potential is compressed within it?
3. What can it plausibly bloom into?
4. What stable identity and provenance does it carry?
5. Who may steward, revise, fork, move, or release it?
6. What is its current expression and lifecycle state?
7. What permissions constrain its portability?

If these questions cannot yet be answered, call it a `BARCandidate`, source material, evidence, or an artifact rather than silently granting BAR identity.

## AI guardrails

An AI collaborator must not:

1. treat every provenance-bearing record as a BAR;
2. require emotional charge for BAR identity;
3. infer charge merely because an object is a BAR;
4. promote private, personal, or sensitive material into a BAR without the required authority and permission;
5. treat every output of a BAR as the same BAR;
6. collapse kernel identity into its current quest, artifact, specification, or implementation;
7. treat capture as an implementation obligation;
8. interpret portability as blanket permission to copy, share, train on, or reuse;
9. collapse BAR lifecycle into structural maturity, social adoption, epistemic maturity, work disposition, completion, or implementation state;
10. erase fork, graft, promotion, expression, or composting lineage.

## Relationship to prior decisions

- The Tension Representation decision keeps charge and its representations distinct from downstream BAR dispatch.
- The completion decision prevents a shipped or completed expression from automatically completing every BAR lineage.
- The Yellow Brick Road and Roadblock decisions allow blockers or learning to seed BAR candidates without requiring metabolization.
- The session-depth decision prevents intimate disclosure from becoming the price of a “better” ChargedBAR.
- Constitutional principle 11 requires the path from source through BAR and expressions to remain visible.

## Result

BAR retains its broad canonical role as the portable kernel of the BARS ecology. Charged possibility remains an important and fully supported BAR pathway, but it no longer narrows the class. Provenance stays mandatory without turning every traceable object into a seed.
