---
name: design-ontology
description: Apply Wendell Britt's integral design ontology when designing, building, reviewing, or translating games, game systems, design tools, adaptive player experiences, Emotional Alchemy mechanics, or council outputs. Use for game-design questions, ontology decisions, player modeling, AQAL analysis, progression, relationship and trust mechanics, evidence claims, and translation between the ontology and an implementation repo. Read ontology/manifest.yaml first and load only the task profile it names.
---

# Design ontology

## Session discipline

Use one fresh session for one bounded task or goal. State that task before loading a profile. Finish it, verify it, record any handoff, and stop.

Do not accumulate unrelated goals, broaden the task in place, or treat context compaction as ordinary workflow. If the goal materially changes, preserve the current result and start a new session with a fresh bounded brief. A request that would require compaction is evidence that the session should split, not a prompt to retain more conversational memory.

## Load deliberately

1. Read `ontology/manifest.yaml`.
2. Read `ontology/v0.1/QUICKSTART.md`.
3. Select one load profile from the manifest for the task. Do not load the complete historical archive by default.
4. When current and historical language conflict, current sources and binding decisions named by the manifest govern. Preserve the historical source as provenance.

## Apply the ontology

For a design or build decision:

1. State the intended intrinsic pleasure and whose pleasure leads.
2. Reconstruct what exists, where it operates, and when it changes before proposing how.
3. Identify the mechanical claim: what is tracked, rewarded, gated, remembered, permitted, and changed.
4. Declare the relevant AQAL perspectives, developmental lines, invited states, favored or burdened types, and exclusions.
5. Separate designed invitation from enacted evidence and intended experience from observed consequence.
6. Preserve player authorship, other agents' agency, consent, refusal, rest, correction, and multiple interpretations.
7. Preserve provenance from seed through route, action, relationship, result, and revision.
8. Name a proportionate test for any material risk or experience claim.

## Hard boundaries

- Do not assign a global developmental rank to a person or treat type as level.
- Do not treat access as command, acquisition as consent, compliance as trust, or a badge as the capability itself.
- Do not treat engagement, completion, artifacts, or system inference as proof of meaning or transformation.
- Do not use WAVE for the Basic Moves or within-channel progression.
- Do not merge the legacy binary movement grammar with the fifteen-move grammar by shared labels.
- Do not use bare `TensionVector` as current formal or player-facing language.
- Do not infer external helpfulness from inner satisfaction in allyship situations.
- Do not turn recoverability into a claim that error, harm, or divergence was secretly correct.
- Do not convert every captured possibility into implementation obligation.
- Do not specify a whole game when the task is an ontology boundary.

## With the Six Faces

When a six-face pass concerns game design or game building, every face receives the same Quickstart and the task-specific profile. Each face contributes through its bounded lens from `council/faces.yaml`; it does not redefine the ontology from memory. Sage names what it retains and sets down, preserves dissent, and does not turn convergence into truth.

## Output contract

Return:

- `design_intent`
- `intrinsic_pleasure`
- `ontology_objects`
- `mechanical_claims`
- `aqal_attention`
- `agency_and_consent`
- `evidence_and_unknowns`
- `provenance_effects`
- `risks_and_tests`
- `implementation_translation`
- `decision_or_open_authority`

Only `decision_or_open_authority` may contain an escalation. Run the council reach test before adding one.
