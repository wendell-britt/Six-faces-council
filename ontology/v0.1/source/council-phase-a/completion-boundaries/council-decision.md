# Six–Game Master Council Decision — Encounter Ending and Scoped Completion

**Decision date:** 2026-10-12
**Status:** Unanimous ontology decision
**Scope:** Genre-portable, with tabletop and videogame RPGs as primary stress tests

> **Owner terminology correction — 2026-10-12:** Moves resolve, encounters end, quests complete, and arcs conclude. The council's earlier “quest fulfillment” and “quest termination” wording is superseded below.

## Decision

> **Moves resolve. Encounters end. Quests complete. Arcs conclude. None alone proves satisfaction, development, transformation, or worth.**

The word **completion** may be used only as a qualified, scope-bound claim. A completion claim must name the object, contract, criteria, evidence, authority, time, and contestation state.

## Scope-specific vocabulary

| Scope | Preferred transition | Meaning |
|---|---|---|
| Participant | exits, pauses, withdraws, refuses | This agent’s active participation changes |
| Session | ends or suspends | The current play period stops; its encounters may remain open |
| Encounter | ends or suspends | The bounded field of immediate participation stops or pauses |
| Move invocation | resolves, cancels, or is interrupted | The attempted procedure produces a result or ceases without one |
| Practice instance | completes procedurally or ends | Its declared practice steps were performed, or the container stopped |
| Quest | completes or receives another named disposition | It completes only when its declared conditions are met; otherwise it may remain incomplete, fail, expire, be declined, abandoned, superseded, or composted |
| Arc | concludes, remains open, branches, or is abandoned | A larger trajectory receives or does not receive an ending |
| Technical flow | reaches a destination or recoverable error | The interface does not strand the user silently |
| Transformation | is supported, unsupported, unclear, or contested | Appropriate evidence indicates whether a contextual change occurred |

`Resolved` does not mean successful. `Ended` does not mean resolved. `Completed` does not mean satisfying or transformative. `Concluded` does not mean favorable or exhaustive.

## First-class objects

- `EncounterDefinition` and `EncounterOccurrence`
- `MoveDefinition` and `MoveInvocation`
- `QuestDefinition` and `QuestInstance`
- `ArcDefinition` and `ArcInstance`
- `Session`
- `CompletionContract`
- `ParticipantExitRecord`
- `EncounterEndRecord`
- `MoveResolutionRecord`
- `QuestDispositionRecord`
- `ArcConclusionRecord`
- `CompletionClaim`
- `InterruptionRecord`
- `Checkpoint` and `ContinuationRecord`

## Independent state axes

Do not represent play with one overloaded `status` or `completed` field. Preserve at least:

- activity: available, active, suspended, ended;
- ending mode: resolved, rest, refusal, retreat, surrender, safety stop, timeout, interruption, disconnection, handoff, abandonment, supersession;
- resolution result: success, partial, failure, no effect, withdrawn, disputed, not applicable;
- objective judgment: unassessed, unfulfilled, fulfilled, disputed, not applicable;
- experiential finding: shift, no-shift, unclear, satisfying, unsatisfying, unreported;
- consent state;
- resumability and checkpoint;
- persistence and consequence;
- evidence, authority, provenance, and contestation.

No-shift is an experiential finding, not an ending mode. External interruption normally suspends an occurrence when resumption remains viable; it ends only when the current occurrence is explicitly closed.

## Composable encounter contracts

An encounter may carry one or more operative contract families:

- contest or instrumental;
- exploration, investigation, or inquiry;
- relational, negotiation, or allyship;
- practice, somatic, or transformational;
- ritual;
- creative, crafting, or authorial;
- recovery, downtime, or maintenance;
- governance or collective decision;
- training, rehearsal, or performance.

These are not exclusive genre labels. A boss negotiation may be simultaneously contest, relational, and inquiry-oriented. Contract families determine relevant criteria, evidence, authority, consent, and endings without predetermining the result.

## Completion contract

A `CompletionContract` records:

1. evaluated object and scope;
2. entry or trigger conditions;
3. required and optional conditions;
4. acceptable evidence and evidence authority;
5. adjudicating and contesting agents;
6. consent dependencies;
7. temporal scope and criteria version;
8. success, failure, refusal, retreat, interruption, expiration, and composting behavior;
9. pause, checkpoint, resumption, retry, and reopening rules;
10. child-to-parent propagation policy;
11. rewards, permissions, obligations, persistence, and consequences.

Criteria cannot be added retroactively to prevent exit or force a preferred emotional or narrative outcome.

## Authority

- Every participant may stop or pause their own participation.
- The player has primary authority over personal meaning, satisfaction, felt shift, and no-shift.
- Affected agents govern their consent and may attest relational impact.
- Rules and systems may establish recorded mechanical transitions.
- Game Masters may adjudicate fictional and procedural ambiguity within the agreed contract.
- Groups may recognize shared narrative conclusions without determining every member’s meaning.
- AI may propose interpretations or completion hypotheses but cannot establish consent or inward truth.

One participant’s exit does not necessarily end a shared encounter. Revoking consent blocks newly unauthorized participation or use; it does not automatically erase previously established fictional facts or consequences.

## Invariants

1. Encounter ending does not imply move resolution, quest completion, arc conclusion, or transformation.
2. Move resolution does not imply success.
3. A failed, expired, declined, abandoned, superseded, or composted quest is not thereby completed.
4. Child completion does not automatically complete a parent; parent conclusion does not imply every child completed.
5. Refusal, rest, retreat, witnessing, and no-shift cannot be relabeled as satisfaction of an unmet action gate.
6. A refusal or retreat may itself fulfill a contract explicitly about boundary-setting, survival, discernment, or release.
7. Failure describes an attempt or objective, never player worth.
8. Every ending leaves a legible next state and provenance.
9. Completion criteria cannot be retroactively tightened to force a story or transformation.
10. System evidence cannot establish inward meaning; inward satisfaction cannot establish external helpfulness.
11. The Game Master is also a player and retains boundaries, rest, and refusal.
12. WAVE names only the Open Up breathing practice and never a general completion process.

## Portable tests

- **Tabletop retreat:** escape resolves successfully, combat ends, and the rescue quest remains active or changes.
- **Videogame reload:** the abandoned branch retains provenance while canonical world state reverts; player knowledge and consent effects are not erased.
- **PbtA miss:** the move resolves and creates consequences without succeeding.
- **Relational refusal:** participation ends or branches without fabricating disclosure, consent, repair, or growth.
- **Emotional Alchemy no-shift:** the practice container ends and a Witness Note may be preserved while transformation and an action-attested Show Up quest remain unclaimed.
- **Roguelike death:** the run ends in failure while a metagame objective may advance.
- **Sandbox play:** a meaningful encounter may end without any quest or authored arc.
- **Multiplayer interruption:** one participant disconnects or exits while the shared encounter continues under its declared rules.

## Resolution of the previous conflict

A player may validly end an encounter through rest, refusal, witnessing, retreat, interruption, or no-shift while leaving a Show Up quest incomplete. This is not a contradiction because encounters end and quests complete.

Principle 14, “Composting is a valid completion,” means composting may validly complete an active obligation, review process, or lifecycle disposition. It does not retroactively complete the original quest unless that quest’s declared contract makes release or composting its completion condition.
