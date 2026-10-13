# Session Depth and Disclosure — Reconstruction and Ontology Decision

**Date:** 2026-10-12

**Status:** Binding v0.1 ontology decision

**Scope:** Response detail, practice performance, experiential depth, adaptive pacing, disclosure, and artifact tailoring

**Does not authorize:** BARS implementation changes, disclosure scoring, psychological diagnosis, or retention of raw session text

## Question resolved

May answer length, specific fear naming, or mask identification influence artifact richness, pacing, rewards, or other content? What can those signals establish, and what protections apply?

## Reconstruction: what exists

The source material currently places several different phenomena under **session depth**.

1. **Response volume:** the amount of text or other material supplied.
2. **Response specificity:** the presence of concrete distinctions, constraints, relationships, examples, fears, masks, or desired consequences.
3. **Practice performance:** what the player does within the declared form—such as completing perspective shifts, naming a fear, or speaking from a mask.
4. **Experiential depth:** how deep, genuine, meaningful, difficult, or transformative the session was for the player.
5. **Artifact specificity:** how closely an artifact can be tailored to supplied material.
6. **Artifact quality and usefulness:** whether the resulting artifact is satisfying, usable, or effective.
7. **Pacing need:** whether the interface should slow, pause, elaborate, or move on.
8. **Deftness:** demonstrated capacity to perform a practice across relevant situations.

These can relate without being equivalent. A concise answer can be precise. A long answer can be repetitive or protective. A performed move can create capacity and story without proving a hidden inner state. A detailed artifact can still be unhelpful. Intimate disclosure can increase available material while reducing safety, trust, or willingness to continue.

## Reconstruction: where each claim operates

- **Input and interface layer:** volume, modality, field completion, and pacing behavior.
- **Practice and game layer:** explicit actions performed under a move or encounter contract.
- **Interpretive layer:** correctable claims about specificity, relationships, ambiguity, and possible meaning.
- **First-person layer:** reported genuineness, depth, satisfaction, privacy, and transformation.
- **Artifact layer:** specificity, variety, coherence, aesthetic elaboration, and fit.
- **Outcome layer:** later usefulness, action, relationship, or consequence.
- **Capability layer:** repeatable performance across relevant conditions, never whole-person worth.

## Reconstruction: when the claims become available

1. A `ResponseMaterial` record becomes available when the player supplies text, selections, images, audio, somatic notation, fictional material, or another permitted modality.
2. A `ResponseAffordanceProfile` becomes available when the system identifies what that material can support for the declared purpose. It remains a correctable content analysis, not a depth score.
3. A `PracticePerformanceRecord` becomes available when observable action can be compared with an explicit move or encounter contract.
4. A `DepthClaim` becomes available only with its scope and evidence authority. Player-reported experiential depth is not inferred from response behavior.
5. An `ArtifactTailoringPlan` becomes available when permitted response material supports particular adaptations.
6. An `ArtifactFitFinding` becomes available only after the artifact is evaluated by the relevant authority: player report for personal fit, recipient attestation for relational reception, or scoped external evidence for consequence.
7. A `DeftnessFinding` requires repeated, relevant performance evidence and cannot be inferred from one session's disclosure volume.

## Decision

### 1. Retire disclosure volume as a universal depth measure

The future `SessionDepthSignal` is retained only as a legacy implementation proposal. Answer length, intimate specificity, fear naming, or mask identification do not establish genuineness, inner depth, readiness, trust, transformation, or deftness.

The replacement is a purpose-bound `ResponseAffordanceProfile`. It may describe available material using fields such as:

- relevant specificity;
- concrete constraints and desired consequences;
- relational or temporal links;
- examples and counterexamples;
- ambiguity and uncertainty;
- selected imagery, tone, and metaphor;
- modality coverage;
- omissions intentionally preserved;
- confidence and player correction status.

Character count may establish character count. It does not establish depth.

### 2. Performance is legitimate gameplay evidence

Gameplay is performance, and performed practice can create capacity, story, relationship, and consequence. A game may reward a named action within an explicit contract—for example, completing a perspective change, testing a request, or supplying a concrete constraint.

A `PracticePerformanceRecord` says what was performed under which conditions. It does not silently become a claim that the player was genuine, vulnerable enough, healed, transformed, or developmentally advanced. If a game rewards performance, it names the performance rather than the inner state it hopes the performance may support.

### 3. Specificity, richness, quality, and fit are separate

**Artifact specificity** is how closely an output incorporates relevant supplied distinctions. **Artifact richness** must be decomposed into named dimensions such as specificity, variety, structural completeness, aesthetic elaboration, or relational context. **Artifact quality** concerns performance against declared criteria. **Artifact fit** concerns usefulness or satisfaction for a person and purpose.

More usable material may permit more specific tailoring. It does not entitle one player to better baseline craft, greater progress, or more powerful rewards than a concise or private player. The system must not intentionally weaken standard artifacts to incentivize disclosure.

### 4. Tailoring follows an input-sufficiency contract

Every adaptive artifact type declares a minimum `InputSufficiencyContract` containing:

- purpose and promised adaptation;
- necessary and optional fields;
- non-sensitive alternatives;
- uncertainty behavior;
- whether processing is local or external;
- retention and downstream-use rules;
- fallback behavior when material is insufficient.

When tailoring lacks sufficient material, the system may:

- produce a clearly labeled general artifact;
- ask an optional follow-up;
- offer examples, presets, or player selection;
- accept fictionalized, abstracted, symbolic, or nonverbal input;
- preserve uncertainty rather than inventing intimacy.

The system may not demand unnecessary personal disclosure merely because disclosure would make generation easier.

### 5. Intimate disclosure is not progression currency

Game access, core progress, capability credentials, power, and social standing must not depend on the amount or intimacy of personal disclosure unless the disclosure is genuinely constitutive of a narrowly declared, consented practice and an equivalent privacy-preserving route is impossible. Even then, the player must be able to refuse or exit without a false claim of failure or inferiority.

Mechanics may reward completion of a declared practice, contribution of usable design material, testing, revision, or kept commitments. They do not reward the revelation of secrets, pain magnitude, fear intensity, or verbal vulnerability as such.

### 6. Genuineness belongs to the person reporting it

“Genuine mask identification” may be recorded only as a player's report or as an attributed facilitator interpretation that remains correctable. AI cannot establish genuineness from linguistic style. Disclosure, emotional language, somatic description, compliance, and continued play do not equal consent or authenticity.

### 7. Adaptive pacing remains reversible

Response length may inform a `PacingAdaptationProposal` about interface load, but “longer answer means slower pace” is not a fact about the player. Pacing adaptations must be visible or readily correctable, must not trap a player in an intensified sequence, and should offer controls such as continue, pause, summarize, go deeper, or change mode.

### 8. Equivalent expressive routes are first-class

The design must test concise, second-language, neurodivergent, disabled, culturally guarded, private, symbolic, nonverbal, and low-literacy participation. Equivalent routes may include selection, arrangement, image, gesture, scale, analogy, fictionalization, example choice, private-local processing, or later revision.

Equivalence means access to the same core game and quality floor, not identical output wording.

### 9. Evidence for depth and artifact value stays plural

- response volume establishes available volume;
- a ResponseAffordanceProfile proposes what the material can support;
- a PracticePerformanceRecord establishes observed performance within its contract;
- player report establishes reported depth, genuineness, satisfaction, or fit;
- artifact review establishes performance against declared artifact criteria;
- later action and relational evidence establish scoped consequences;
- repeated demonstrations may support a scoped DeftnessFinding.

No single item establishes all the others.

## Required test before implementation

Any session-adaptation feature must compare artifact fit and usefulness across response length, communication style, modality, disclosure preference, language fluency, and accessibility needs. At minimum it must test whether:

1. concise but specific input receives an artifact of equal quality;
2. long but low-relevance input is not mistaken for tailoring value;
3. private or fictionalized routes can reach the core experience;
4. players can correct the ResponseAffordanceProfile and pacing;
5. intimate disclosure produces no hidden progress, power, or ranking advantage;
6. personalization improves player-reported usefulness without increasing coerced disclosure;
7. raw-content processing, persistence, and reuse follow separate permissions.

## AI guardrails

An AI collaborator must not:

1. call a session deep, genuine, vulnerable, avoidant, or superficial from length or style alone;
2. infer transformation, readiness, trust, or developmental altitude from disclosure;
3. reward pain magnitude or intimate specificity as progression currency;
4. make a deliberately weaker artifact to pressure a player into saying more;
5. equate a completed performance with inner transformation;
6. infer that a concise response is resistance, low effort, or low capacity;
7. treat AI-generated semantic specificity as confirmed user meaning;
8. retain or reuse raw session material because structured features were permitted;
9. pace a player irreversibly from a behavioral proxy;
10. hide the difference between general generation and evidence-supported tailoring.

## Relationship to prior decisions

- The Tension Representation decision keeps reported experience distinct from structured extraction and requires purpose-specific permission.
- The completion decision permits a practice to resolve or an encounter to end without proving transformation.
- The Roadblock decision prohibits treating concise, private, or non-disclosing play as resistance.
- The psychograph and evidence rules reserve inward meaning for the represented player.
- The constitutional rule that motivation serves meaning allows performance incentives while preventing engagement metrics from proving benefit.

## Result

The ontology preserves the design insight that what a player supplies and performs can change what the game can make with them. It rejects the shortcut that more words or more intimate confession automatically means deeper play. The game may reward named practice and use relevant material; it may not sell depth, quality, or power in exchange for disclosure.
