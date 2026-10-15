# Spec: Design ontology alpha shipping

## The ask

> “yes let's do that. Let's have the 6 game masters guide us through this process” — Wendell Britt, design-ontology project chat, 2026-10-14

**Who it is for:** Wendell and designers using the ontology with AI collaborators

**What they feel now, and what should change:** The ontology is rich and credible but still feels like something that must be explained from inside its history. It should become a bounded design encounter that can be entered, used, checked, and exited without oral context.

## Purpose

Ship a repo-local `0.1.0-alpha.1` whose usefulness and limits are demonstrated by one fictional consent-aware Roadblock Encounter, adversarial semantic fixtures, explicit six-face packages, and clean-session verification. Preserve unresolved questions as provisional; do not begin Phase B sorting.

## User stories

### Design one bounded feature

**As a game designer**, I want to give the ontology one concrete design problem, so I receive an implementation-ready brief without surrendering player meaning, consent, or evidence boundaries.

**Acceptance:** The Roadblock Encounter brief names its intended pleasure, smallest playable loop, ontology objects, mechanics, AQAL scope, evidence authority, consent/refusal routes, lifecycle, provenance, risks, tests, and implementation translation.

### Recognize ontology misuse

**As a package maintainer**, I want adversarial fixtures for known category errors, so fluent but unsafe outputs fail visibly.

**Acceptance:** Fixtures reject coercive disclosure, inference-as-belief, artifact-as-transformation, proposal-as-movement, completion conflation, access-as-command, type-as-level, retroactive-success claims, permission laundering through derivatives, and RPG-only assumptions.

### Use the council from a clean session

**As a new collaborator**, I want a fresh checkout to discover the ontology and six faces, so success does not depend on this chat or repository folklore.

**Acceptance:** A documented clean-session run loads the intended profile, respects canonical precedence, produces distinct face readings and a non-deciding Sage synthesis, and passes the validators.

## Design decisions

| Decision | Choice | Whose |
|---|---|---|
| Dogfood feature | Fictional consent-aware Roadblock Encounter | Six-face pass 1 synthesis, 2026-10-14 |
| Release evidence | Gates rather than percentage estimates | Challenger and Regent, pass 1 |
| Work shape | Three bounded PRs, one design-cycle spine | Regent–Diplomat synthesis, pass 1 |
| Sensitive data | No real player data in alpha verification | Privacy decision and Regent gate |
| Governance scope | No Phase B active/reference/compost sorting | Existing Phase A boundary and pass 1 |
| Alpha claim | Repo-local and provisional, not universal plugin or enforcement certification | `ontology/manifest.yaml` and shipping assessment |

## Contracts

The dogfood output uses the design-ontology skill contract:

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

Each face package adds cast, observations, face-specific deliverables, standing test, verdict, citations, and dissent. Sage names what it retained or dropped and never decides.

## Reserved items

Canonical prose, consent or release for real participants, money, and anything naming a person remain reserved. This strand requires none of them. It uses Wendell's quoted authorization only as provenance.

## How we will know it failed

- **The cheap test, run before building:** Produce the Roadblock Encounter brief from the current manifest, Quickstart, game-design profile, and six face definitions in `council/faces.yaml`. Check that a fictional refusal ends the encounter without fabricating quest completion, transformation, or consent, and that an optional artifact does not prove movement.
- **The result that stops the work:** The feature requires real personal disclosure, a face invents player or owner meaning, Sage decides, a clean reader cannot find the smallest loop, or the package cannot keep observation, inference, permission, finding, and completion distinct.

## Definition of done

- [ ] The dogfood Roadblock Encounter is usable as an implementation handoff.
- [ ] Observed failures are preserved and converted into package contracts.
- [ ] Six explicit face packages and their shared output schema exist.
- [ ] Adversarial fixtures and structural validators pass.
- [ ] A fresh checkout/session reproduces a conforming design run without this conversation.
- [ ] Installation, usage, tested environment, known gaps, and update instructions are current.
- [ ] The release example and failed versions remain available as provenance.
- [ ] No Phase B sorting or real-player-data workflow entered scope.
- [ ] The passing commit is tagged `0.1.0-alpha.1` only after every gate succeeds.
