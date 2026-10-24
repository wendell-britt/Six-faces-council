# Codex brief: a mechanic vocabulary from the Gameplay Atlas (2026-10-24)

Wendell, 2026-10-24: "Need to study these mechanics and include them as elements of our design ontology". Decided in council/passes/6FACE_PASS_gameplay-atlas1_2026-10-24.md (positions ga-*).

Inputs: council/research/2026-10-24-gameplay-atlas/ (atlas-inventory.yaml, crosswalk-a.yaml, crosswalk-b.yaml, gaps-a.md, gaps-b.md). The atlas states no licence: cite atlas ids, write all text in our own words.

Add to ontology/v0.1/source/design-ontology-v0.1.yaml (and the model doc), all marked provisional and "council's word, may be cut":

1. `DesignObject` types with required fields: Meter (ceiling, spend, refill, decay, world-state display), TimingWindow (span, what a miss changes; never a score of the person), TriggerChain (condition, effect, order), Loadout (bounded, player-authored; thresholds are never levels), FlowNetwork (conserved quantity, sources, sinks, rates), Combination (inputs, output, lineage kept as provenance), TurnsAndSharedPool (order, common stock, fairness repair), Delegation (scope, visibility, revocation), KnowledgeState (unknown, glimpsed, known, stale; mystery optional).
2. Care parts: TendedLife (cadence; neglect ends in release, never debt), DelayedReturn (no penalty for time away), ReleaseResidue (release act plus optional keepsake, tied to CompostRecord). PracticeSpace stays a candidate.
3. An `atlas_reshaping` table of AntiPatterns: each of the 31 conflict ids in the crosswalks, the invariant it breaks, and its reshaped version.
4. A `mechanic_sources` note: each type lists the atlas ids it covers.

Done when `python3 -m unittest tests.test_design_ontology`, `python3 ontology/tools/validate_package.py` and `python3 ontology/tools/term_lint.py` pass. Do not touch binding decisions; a conflict with one goes back as a board row.
