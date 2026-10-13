# Architect Decision — Orthogonal Lifecycle Claims

Definitions and occurrences must remain distinct: `EncounterDefinition` is not an `EncounterOccurrence`; a `MoveDefinition` is not a `MoveInvocation`; a `QuestDefinition` is not a `QuestInstance`; and an `ArcDefinition` is not an `ArcInstance`.

Each occurrence needs independent activity, ending, resolution, fulfillment, evidence, authority, consent, contestation, and resumability records. The common RPG nesting—arc, quest, encounter, move—is a graph rather than a rigid tree: encounters may advance several quests, quests may span encounters, and moves may cross boundaries.

No child state propagates upward unless a declared contract says it does.
