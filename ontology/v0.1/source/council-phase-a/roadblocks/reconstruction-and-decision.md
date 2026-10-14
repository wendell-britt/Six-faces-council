# Roadblocks — Reconstruction and Ontology Decision

**Date:** 2026-10-12

**Status:** Binding v0.1 ontology decision

**Scope:** The relationship among technical failure, blocked movement, metabolization, and “misaligned intention”

**Does not authorize:** BARS implementation changes, automatic psychological diagnosis, or compulsory processing

## Question resolved

When BARS calls an Emergent Roadblock “a manifestation of misaligned intention” while also using build errors, export mismatches, and missing directives as examples, is misaligned intention a metaphor, a diagnosis, or an automatically inferable cause?

## Reconstruction: what exists

The source material uses **roadblock** for three related but non-identical things.

1. **Observed obstruction.** A build error, export mismatch, missing directive, dependency failure, resource limit, inaccessible route, interpersonal constraint, or other condition prevents a specific action or route from proceeding under declared conditions.
2. **Operational metabolism.** The pre-commit ritual detects a failure, reflects on it, repairs or reroutes it, verifies the result, and preserves useful learning before code enters the shared branch.
3. **Mythic and transformational interpretation.** Yellow Brick Road language treats a blocker as possible raw material for a future brick. “Misaligned intention” appears at this layer as a meaning-making account of why movement and conditions do not presently fit.

The first is an observation. The second is a response pattern. The third is an interpretation. They may participate in one trace, but none is evidence enough to collapse the others.

## Reconstruction: where each claim operates

- **Technical and operational systems:** failure detection, reproduction, causal investigation, repair, verification, routing, and shared-field cleanliness.
- **Game systems:** a route, move, capability, quest, relationship, or action is constrained under stated conditions.
- **Personal experience:** the represented person may experience charge, friction, incapacity, refusal, uncertainty, or a mismatch worth interpreting.
- **Relational fields:** another agent may withhold consent, lack capacity, set a boundary, or report harm. That agent's reasons and inward meaning remain theirs.
- **Mythic framing:** the game may invite a player to treat a roadblock as material for learning or transformation without claiming that this is its sole meaning or required fate.

## Reconstruction: when the claims become available

1. A `RoadblockEvent` becomes recordable when evidence shows that a named action, route, capacity, or destination is constrained under declared conditions.
2. A `RoadblockClassification` becomes available after the observed scope is clear enough to classify provisionally. It may remain `unknown` or be multi-causal.
3. A `RoadblockCausalAccount` becomes available only as evidence supports candidate causes. Correlation, contributing condition, proximate cause, and root-cause claim remain distinct.
4. An `IntentionAlignmentHypothesis` becomes available only when a declared intention can be compared with a method, condition, or capacity relevant to the obstruction. It remains a correctable interpretation attributed to its author.
5. A `RoadblockResponse` records what an agent elects or is permitted to do next.
6. A `MetabolizationOutcome` becomes recordable only after the response produces a reusable change, learning, test, repair, artifact, or provenance record. Unresolved, rested, abandoned, and composted outcomes remain valid alternatives.

## Decision

### 1. A roadblock is first a scoped observation

A **RoadblockEvent** records that something is constrained. It does not by itself establish motive, emotional state, developmental level, hidden desire, resistance, personal defect, or misaligned intention.

Minimum fields are:

- blocked object or action;
- scope and conditions;
- symptom or reported obstruction;
- observation and reproduction evidence;
- detecting or reporting agent;
- time and lifecycle state;
- uncertainty, consequence, and urgency;
- links to candidate causes, interpretations, responses, and outcomes.

### 2. Classification is plural and correctable

A **RoadblockClassification** may include technical, dependency, resource, coordination, capability, environmental, relational, emotional/interpretive, safety/ethical, or unknown. These classes are not exclusive. Classification does not establish cause.

### 3. Causality requires evidence

A **RoadblockCausalAccount** distinguishes:

- observed correlation;
- contributing condition;
- proximate cause;
- root-cause hypothesis;
- verified cause within a declared test scope.

A technical defect may result from an incorrect assumption, an incompatible interface, insufficient capability, a changed environment, a missing resource, or many other causes while the governing intention remains aligned.

### 4. “Misaligned intention” is a hypothesis, not a default diagnosis

An **IntentionAlignmentHypothesis** asks whether a declared intention fits the selected method, present conditions, available capacity, permissions, or downstream consequences. The safe general claim is:

> A roadblock may reveal a mismatch among intention, method, conditions, and capacity; it does not prove misaligned intention.

The hypothesis must identify:

- whose declared intention is being interpreted;
- who authored the interpretation;
- the relevant method, conditions, or capacity;
- supporting and contradicting evidence;
- the distinction between a design intention, an action intention, and inferred hidden desire;
- confirmation, correction, rejection, and permitted-use status where a represented person is involved.

AI and council agents may propose this hypothesis. They may not silently install it as a person's belief or use refusal to confirm it.

### 5. Metabolism is one response family

A **RoadblockResponse** may repair, retry, test, request help, accommodate, change the environment, acquire capability, renegotiate, reroute, pause, rest, accept the constraint, leave unresolved, set down, abandon, or compost.

At the technical layer, **metabolize** means converting a failure into some combination of a repair, verified test, safer route, reusable learning, or provenance-bearing artifact. It does not require emotional processing.

At the experiential layer, metabolization is an offered transformational frame whose validity depends on the represented person's report. It is not required merely because a blocker exists.

### 6. Shared-field cleanliness is scoped governance

The BARS pre-commit ritual may require a named verification gate before a change enters a shared branch. That rule governs the proposed change and shared field; it does not establish a moral or psychological claim about the contributor. A rejected commit can be a fully successful detection event.

### 7. Unresolved blockers remain real

A blocker may remain unresolved indefinitely and may continue to prevent a particular route or quest from completing. Rest, refusal, accommodation, rerouting, abandonment, and composting do not mean the original blocker was repaired. Learning from it does not make it necessary or good.

## AI guardrails

An AI collaborator must not:

1. infer misaligned intention from a technical failure alone;
2. translate “the build failed” into “the person is blocked” without evidence and consent;
3. treat roadblock classification as causal proof;
4. convert correlation or narrative resonance into root cause;
5. use refusal, rest, or failure to metabolize as evidence of resistance;
6. require emotional disclosure before offering technical repair;
7. erase an external, structural, relational, accessibility, or safety constraint by reframing it as inner work;
8. claim that turning a blocker into learning repaired the original consequence;
9. infer another agent's intention, consent, or benevolence from compliance;
10. make shared-branch cleanliness a judgment of whole-person worth or capability.

## Relationship to prior decisions

- The Yellow Brick Road decision supplies `BlockerRecord` and the rule that no blocker creates a perpetual processing obligation. `RoadblockEvent` is the evidence-bearing specialization used when an obstruction is observed in operation or play.
- The Tension Representation decision prevents an interpretation of charge from becoming lived truth. The same separation applies to intention-alignment hypotheses.
- The completion decision allows a detection, failed attempt, or repair procedure to resolve while the larger quest remains incomplete.
- The derived-movement decision supplies the correction pattern: proposals remain versioned and correctable; actual outcomes require separate evidence.

## Result

The ontology keeps the generative BARS proposition that roadblocks can become material without treating every obstruction as a disguised psychological truth. The design opportunity is preserved; the causal claim is bounded.
