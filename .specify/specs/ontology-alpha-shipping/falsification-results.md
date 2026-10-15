# Dogfood falsification results

**Date:** 2026-10-15

**Scope:** specification-level cheap test before implementation

## Scenario

The player uses only presets:

- destination: carry medicine across the salt flats;
- obstruction: the guide is exhausted;
- constrained action: cross before nightfall;
- optional intention interpretation: refused;
- route proposals: refused;
- ending: refusal;
- finding: unassessed;
- artifact: declined;
- persistence: none.

## Result

The specification represents the run without personal disclosure, psychological inference, accepted route, move invocation, artifact, persistence, quest completion, satisfaction, or transformation:

```yaml
ending_mode: refused
blocker_status: unassessed
move_result: not_invoked
movement_finding: unassessed
artifact_disposition: declined
persistence: none
```

The player still received the complete core encounter: a scoped fictional roadblock, two proposals they could evaluate, a clean refusal, and an accurately recorded ending. Refusal did not reduce craft, access, reward, or standing.

## Decision unlocked

The current ontology can produce an implementation-ready Roadblock Encounter contract while preserving refusal, completion, evidence, and privacy distinctions. PR 1 may proceed to review.

## What remains unverified

- no implementation exists yet;
- operation-boundary permission enforcement is untested;
- transient disposal and log minimization are untested;
- correction propagation is untested;
- route quality and accessibility have not been playtested;
- clean-session discovery has not been tested.

These limits belong to PR 2 and PR 3 gates. They are not silently counted as passing evidence.
