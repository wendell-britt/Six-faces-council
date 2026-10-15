# Six-face pass: design ontology alpha 2, the fictional Roadblock Encounter

Wendell authorized the alpha-shipping process with the six Game Masters on 2026-10-14. Pass one selected a fictional, consent-aware Roadblock Encounter as the first dogfood feature. This second pass designs and falsifies that encounter under the current `game_design` load profile.

**Casts** (`cast.py --json`): Shaman 53 Emergence, lines 2, 3 and 4, becomes 6 Divergence. Architect 9 Restraint, lines 1 and 2, becomes 53 Emergence. Challenger 58 Banter, lines 2, 5 and 6, becomes 21 Bite. Regent 40 Thaw, no changing lines. Diplomat 34 Vigour, line 4, becomes 11 Mingling. Sage 53 Emergence, no changing lines.

## Scorecard

Pass one's Stage 0 tests are met at specification level. The dogfood feature is consequential enough to exercise roadblock, evidence, completion, disclosure, and privacy boundaries; small enough to implement as a deterministic local state machine; and uses only version-controlled fictional fixtures. Phase B, real player data, clinical use, production analytics, model improvement, unrestricted export, and BARS runtime migration remain excluded.

The implementation, clean-session, and semantic-fixture gates remain ungraded.

## Anchor

Create a small fictional encounter in which a traveler meets an obstruction on the way to a chosen destination, tests or declines one route, and leaves with their own account of what happened. The feature should demonstrate that the ontology can produce a useful, implementation-ready design without collecting real personal material or converting play into claims about a player's inner state.

## Shaman

**Emergence becomes Divergence.** The player first needs a hospitable ledge, not an interpretation. Pressing into exposed ground turns movement into defense; an imperfect branch that holds, such as a symbolic answer, temporary route, or rest, is enough. Divergence means the encounter must hold disagreement among destination, route, conditions, and the system's reading without forcing reconciliation.

**The pleasure is gentle symbolic precision.** A fictional obstruction becomes several playable possibilities while the player retains the right to say “none of those.” Begin with presets and symbolic distance. Ask what the obstruction prevents under stated conditions, never what it secretly means. Let the player reject every path, set the work down, or witness the fork. The player chooses the finding word.

**The standing test remains binding.** Refusal, silence, divergence, and no-shift cannot become resistance or evidence that something is wrong with the player.

## Architect

**Restraint becomes Emergence.** Hold the clouds without claiming rain. Dependable capability grows from a deliberately small loop: no psychograph, hidden adaptation, quest system, longitudinal player model, or required LLM.

**The design uses independent axes.** A deterministic state reducer separates encounter state, move result, movement finding, artifact disposition, and persistence. `MOVE_RESOLVED` does not imply shift. `ENCOUNTER_ENDED` does not imply quest completion or satisfaction. The artifact remains optional and proves only that an artifact was made.

**The smallest loop has four beats.** Choose a fictional destination. State the scoped obstruction. Review two sourced route proposals plus rest, refuse, and leave unresolved. Resolve one fictional action if selected, choose or decline a finding, end the encounter, and separately accept or decline the optional card.

## Challenger

**Banter becomes Bite.** The player must be able to challenge the system, change the frame, or laugh off a poor interpretation without losing progress. Reassuring consent language is insufficient; evidence and permission boundaries must bite as executable gates.

**Eight tests guard the slice.** Observation must not become psychology. Optional interpretation must remain optional at equal craft. Transient processing must not enable persistence or later purposes. Rejected hypotheses must stop affecting play. Rest, refusal, interruption, and suspension must not fabricate resolution or transformation. Useful clues must not mark the blocker repaired. The trace must contain only fictional fixture data and permitted operational events. Generated world material must not launder source restrictions.

**Stop conditions are concrete.** Stop if refusal reduces quality, interpretation appears without invitation, classification becomes causal proof, rejected inference remains active, an ending implies personal change, or any undisclosed persistence occurs.

## Regent

**Thaw has no changing lines.** The feature should loosen obligation around a blocker, not create duties to explain, transform, finish, save, or agree. Remove unnecessary complexity and let the player leave cleanly.

**Authority is scoped.** The designer authors fictional scenarios and rules. The player governs optional interpretation, correction, persistence, visibility, and continuation. Fixture facts establish only fictional conditions; selections establish choices; performance establishes observable play. None proves motive, satisfaction, development, or transformation.

**Permission sits at operation boundaries.** Transient processing is disclosed. Persistence, personalization, visibility, export, analytics, and model improvement are separate and default off; publication and model improvement are prohibited in this slice. Every derivative inherits the active PermissionEnvelope. Administrative access creates no new purpose.

**The encounter may end cleanly.** Resolution, rest, refusal, retreat, safety stop, timeout, interruption, and suspension are distinct endings. A parent quest changes only under its own contract. Resumption requires a new situated check of any saved permission.

## Diplomat

**Vigour becomes Mingling.** Strength no longer has to ram the hedge. Agency appears as the player's ability to choose the terms of contact with obstacle, helper, and world, then leave with one usable next relation.

**The invitation says what it does.** The player does not have to explain why, disclose anything personal, or defeat the obstruction. They choose real-distance fiction through preset, symbolic, concise, self-authored in-world, drawn, arranged, gestured, or nonverbal routes. A visible Rest / Change / End control remains available throughout.

**Every route has the same quality floor.** A player who shares nothing intimate, says nothing aloud, rejects interpretation, and exits after one choice still receives one accurately scoped roadblock, one authorized response or refusal, one evidence cue, and an equally crafted optional Route Card.

**Witnesses remain bounded.** A witness may report observable action or their own experience, never the player's motive or inward truth. Silent witness, factual reflection, offered options, and joining the move require distinct situated permission.

## Verdicts

| Face | Deterministic fictional slice | Optional interpretation | Equal-quality refusal | Persistence default off | Poetic skin |
|---|---|---|---|---|---|
| Shaman | yes | yes | required | yes | important to felt invitation |
| Architect | yes | yes, not needed for core | required state axis | required | replaceable layer |
| Challenger | yes | only after gate tests | required or stop | required or stop | must not soften enforcement |
| Regent | yes | separately granted | required | required | subordinate to authority truth |
| Diplomat | yes | player-controlled | defining quality test | required | useful if all routes remain legible |

**The dissent check finds a real split.** The pass is not unanimous about how much poetic presentation belongs in the alpha. Shaman and Diplomat see symbolic distance as part of the invitation; Architect, Challenger, and Regent treat it as a replaceable layer that must not obscure testability or authority. Sage preserves both by specifying a functional, deterministic core with an optional provisional skin. No coined product name becomes ontology canon in this pass.

## Sage

**Emergence has no changing lines.** The feature advances by stages the ground can hold. The alpha should not skip from a rich specification to a release claim.

**The synthesis keeps every face.** Shaman provides the hospitable fictional distance and non-diagnostic felt rule. Architect provides the state machine and independent axes. Challenger supplies falsification and stop conditions. Regent supplies authority, permissions, and lifecycle truth. Diplomat supplies the invitation, expressive equality, witness boundary, and life-use bridge. Nothing is dropped.

The specification passes the cheap design-level falsification: a preset-only refusal ends the encounter truthfully, produces no quest-completion or transformation claim, requires no interpretation or personal disclosure, and persists nothing. This supports implementation; it does not prove the implementation will comply.

## Outputs

**Positions:**

- **dogfood-functional-core.** Implement a deterministic fictional Roadblock Encounter whose lifecycle, findings, artifact, and persistence axes validate independently.
- **dogfood-quality-floor.** Preset, symbolic, concise, nonverbal, refusal, rest, and unassessed routes receive the same core craft and access.
- **dogfood-permission-boundaries.** Transient processing is the only default; all other purposes are independent and off, with publication and model improvement prohibited.
- **dogfood-provisional-skin.** The poetic setting and names remain replaceable design copy; the alpha tests the ontology contract, not the permanence of a theme.

**Questions:** none. The reach test finds no owner-only fact required to implement a fictional, non-sensitive local slice. Canonical prose, real consent/release, money, and personal naming remain untouched.

## Tests before PR 1 may merge

1. Preset-only refusal ends with `ending_mode=refused`, `movement_finding=refusal|unassessed`, no move result, no artifact obligation, and no persistence.
2. Selecting a route and then reporting `no_shift` preserves proposal, move result, and finding as distinct records.
3. Correcting an obstruction invalidates unused descendants and generates replacements from the correction.
4. No-save completion leaves no recoverable fictional input or descendant outside the explicit test trace.
5. The same schema supports fantasy, science-fiction, and everyday-folktale fixtures without RPG-only character progression.
