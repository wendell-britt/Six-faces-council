# Creative Reuse and Personal Meaning — Reconstruction and Ontology Decision

**Date:** 2026-10-12

**Status:** Binding v0.1 ontology decision

**Scope:** AI reuse of creative archives, project framing, personal meaning, attribution, derived voices, rejection, and permission

**Does not authorize:** Reuse of any corpus, cloning or impersonation, legal conclusions, or collection of new personal material

## Question resolved

Can BARS frame AI remixing of a creator's past work as “not necromancy” while a player or creator may experience that reuse as uncanny, inappropriate, exploitative, “not mine,” or something else?

## Reconstruction: what exists

`FOUNDATIONS.md` establishes a project-level ethical and mythic frame. It describes a creator's prior voice recordings, prose, characters, and instructional material as compostable creative material. Within the BARS ontology it answers the “necromancy” question with “no,” and proposes agent personalities derived from tonal qualities, vocabulary patterns, and emotional textures in a creator's archive.

The design constitution separately gives the player authority over personal inward meaning and requires AI interpretations to remain correctable. The source also describes generated voices as characters rather than impersonations, but calling something “not impersonation” states design intent; provenance, presentation, behavior, and audience reception determine whether the implementation actually maintains that boundary.

Meaning, permission, authorship, identity, attribution, and consequence therefore cannot share one field.

## Reconstruction: where each authority operates

- **Project meaning:** the designer may define the intended metaphor, ritual, and ethical orientation of the game.
- **Personal meaning:** each affected person may report what the reuse feels like and whether an interpretation is theirs.
- **Source authorship:** identifies who authored or performed the archived material.
- **Generated authorship:** identifies the system and people responsible for selecting, transforming, generating, and curating the new output.
- **Reuse permission:** governs whether material may be processed for a named purpose, audience, duration, and output class.
- **Identity and likeness:** governs how closely a generated voice, persona, or character may evoke or represent a person.
- **Shared-world consequence:** concerns confusion, deception, harm, reception, and institutional or relational effects.

No authority in one layer automatically decides the others.

## Reconstruction: when claims become available

1. A `SourceCorpusRecord` identifies the source material, authorship, subjects, provenance, sensitivity, and existing rights or permissions.
2. A `CreativeReuseProposal` states what transformation is proposed and why.
3. A `ReuseAuthorization` permits specific processing, retention, output, audience, and reuse purposes.
4. A `DerivationRecord` documents what source material and methods contributed to an output.
5. A `ProjectMeaningFrame` states the project's intended metaphor or ethical interpretation.
6. A `PersonalMeaningReport` records an affected person's own experience without requiring agreement with the project.
7. An `AttributionRecord` distinguishes source authorship, generation, curation, character ownership, and publication.
8. A `ReuseRejection` or correction records what is being rejected and which downstream actions follow.
9. A `ReuseConsequenceRecord` preserves observable reception, confusion, benefit, or harm.

## Decision

### 1. Project framing and personal meaning coexist

“AI remix is not necromancy” is a `ProjectMeaningFrame`: an authored statement about how BARS intends its creative-composting ritual to be understood. It may guide narrative, aesthetics, and design.

It does not compel a `PersonalMeaningReport`. A player or creator may experience the same process as generative, uncanny, continuous, alienating, exploitative, inappropriate, sacred, playful, grief-laden, “not mine,” or unresolved.

> **The project may name its ritual; it may not name the player's experience for them.**

Personal meaning does not by itself settle shared facts, ownership, permission, or harm. Project meaning does not overrule personal experience.

### 2. “Not mine” is a scoped correction

“That is not mine” may reject one or more distinct claims:

- semantic fit: the output does not express the person's meaning;
- experiential fit: the interpretation does not match their experience;
- authorship: they did not author the generated words or choices;
- attribution: the output is labeled too closely as theirs;
- identity or likeness: the voice or persona feels falsely representative;
- aesthetic fit: the result does not belong in their work;
- permission: they do not authorize future use;
- relationship: the reuse violates an expectation or boundary.

A `ReuseRejection` identifies its scope. The system must not translate rejection into resistance, denial, lack of integration, or proof that the generated reading was secretly accurate.

### 3. Past-self continuity is a claim, not an automatic fact

A creator may regard earlier work as continuous with, distinct from, or partly alien to their present identity. `IdentityContinuityClaim` records the author and scope of that relationship. The project may invite a compost metaphor but cannot declare that every past self is merely raw material or that present permission is irrelevant because the same legal person created it.

### 4. Derived voices are characters with declared provenance

A `DerivedVoice` is a generated character or voice configuration informed by a permitted corpus. It is not the source person, a past self, or an archived speaker.

Its record identifies:

- source corpus and permissions;
- selected tonal, lexical, structural, or thematic features;
- character identity and fictional role;
- prohibited identity or impersonation claims;
- allowed audiences and uses;
- disclosure and explanation policy;
- correction, retirement, and deletion behavior.

Calling a voice a character does not by itself prevent impersonation. The implementation must avoid presenting generated speech as an authentic statement, memory, endorsement, or continuation authored by the source person.

### 5. Authorship and contribution remain decomposed

An `AttributionRecord` separately names:

- source author or performer;
- corpus selector;
- transformation or generation system;
- prompt or configuration author;
- curator or editor;
- character or world owner;
- publisher;
- person who accepts or rejects the result as part of their work.

Stylistic influence, source contribution, generation, curation, acceptance, and authorship are not interchangeable.

### 6. Permission is granular and prior

`ReuseAuthorization` distinguishes:

- collection or import;
- local analysis;
- external model processing;
- feature or style extraction;
- generation;
- persistent storage;
- use for personalization;
- publication or performance;
- sharing with collaborators or players;
- commercial use;
- model improvement or training;
- derivative voice creation;
- future reuse, correction, revocation, and deletion.

Permission for one purpose does not authorize another. Ownership or prior authorship does not erase current privacy, relationship, contractual, or audience constraints. Third-party and deceased-person material require separate authority outside this decision; the system must not infer it.

### 7. Mystery does not hide provenance or control

The game may preserve surprise about which themes or fragments will reappear. It must still make the reuse mechanism, material categories, permissions, and available controls understandable before authorization. Optional explanation may reveal more detailed derivation later.

Uncanny precision is an aesthetic success only when the person retains correction, mediation, and exit. Hidden outcomes are compatible with consent; hidden collection or unauthorized reuse is not.

### 8. Rejection propagates through lineage

Depending on the ReuseRejection scope, the system must:

- stop future personalization or generation from rejected material;
- correct attribution and identity claims;
- quarantine, regenerate, or retire unpublished descendants;
- version or relabel already-published descendants;
- propagate purpose, audience, retention, deletion, and revocation limits;
- preserve only the minimum lawful audit history;
- disclose consequences that cannot be reversed.

Completed play remains historical fact, but the rejected interpretation does not remain the person's truth.

### 9. Non-AI and non-reuse routes preserve the core game

A participant may disable archive-based adaptation or choose a non-AI route without being assigned inferior meaning, progress, power, craft, or belonging. A creator may use entirely fictional, newly authored, public-domain, licensed, abstracted, or manually curated material instead.

The output need not be identical, but the core game and quality floor remain available.

## AI guardrails

An AI collaborator must not:

1. present the project frame as the player's required meaning;
2. claim that a generated voice is the source person or past self;
3. attribute generated statements, memories, endorsements, or intentions to the source author;
4. treat source authorship as blanket permission for every new use;
5. infer permission for third-party or deceased-person material;
6. interpret “not mine” as resistance or covert confirmation;
7. obscure reuse categories or controls merely to preserve surprise;
8. collapse stylistic influence, contribution, generation, curation, acceptance, and authorship;
9. continue future use after scoped rejection or revocation;
10. make AI reuse necessary for core access, progress, quality, or belonging.

## Relationship to prior decisions

- Constitutional principle 10 assigns personal inward meaning to the player.
- The Tension Representation and derived-movement decisions provide correction and downstream-lineage behavior.
- Session-depth rules prevent intimate material from becoming progression currency.
- Composting separates release from required creative regeneration.
- BAR portability never creates blanket reuse permission.
- Mystery remains compatible with optional explanation but not with hidden collection or unauthorized processing.

## Result

BARS may keep its creative-composting metaphor and “not necromancy” declaration as an explicit project stance. Players and creators remain free to experience the practice differently, reject an interpretation or attribution, and refuse the reuse itself. The system can author the ritual; it cannot author another person's inward response or fabricate their continuing voice.
