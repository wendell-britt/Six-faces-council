# Gaps, part b: Combine & allocate, Control & respond (137 mechanics)

Counts: see the verdict; fit values live in crosswalk-b.yaml. Names below are the council's word, may be cut.

## Candidate additions

1. **ResourceMeter** (council's word, may be cut). A named spendable amount with a ceiling, a spend rule, a refill rule (rest, node, time) and a decay rule. Its display on a play surface must be world state (light, size), never a number (depth_over_flatland). Ids: combat-stamina-budget, combat-action-points, exploration-climbing-rest-route, exploration-air-action-refill, projectiles-heat-pacing, projectiles-spread-recovery, driving-drift-boost, inventory-light-reserve, inventory-weight-budget, defense-tower-upgrade-budget, defense-ammunition-supply, combat-posture-break.
2. **TimingWindow** (council's word, may be cut). An interval in which one action resolves differently, with a record of the attempt that is not a score of the person. Ids: combat-timed-parry, combat-invulnerable-dodge, projectiles-active-reload, driving-start-charge, stealth-knockout-window, command-interrupt-action, rhythm-onbeat-actions, rhythm-hidden-beats.
3. **TriggerRule / EffectChain**. A condition-effect pair that fires in an order, including reactions and cascades. Ids: deckbuilding-trigger-order, combat-surface-reactions, defense-trap-sequence, matching-gravity-cascade, combat-overwatch, stealth-synchronized-actions, combat-part-destruction.
4. **Loadout**. A chosen, bounded, cycling or thresholded set of moves, members or items, authored by the player. Ids: combat-combat-deck-cycle, deckbuilding-opening-hand-control, deckbuilding-reward-choice, deckbuilding-rule-changing-passives, inventory-equipment-budget, command-prebattle-formation, command-trait-thresholds. Thresholds on traits must never become levels (type_is_not_level).
5. **TurnStructure and SharedPool**. Who acts or picks when, from what common stock, with fairness repair. Ids: command-initiative-order, allocation-public-pick, allocation-snake-order, allocation-worker-placement, allocation-shared-stock, allocation-follow-phase, allocation-area-majority, allocation-route-denial. Matters for the second player in chapter1 and for between.
6. **Foreknowledge / KnowledgeState**. What the system shows before commitment, and how known a place or thing is (unknown, glimpsed, known, stale). Ids: combat-intent-preview, stealth-peeking, exploration-earned-map, command-scout-current-vision, inventory-identification. Must let mystery stay optional.
7. **Combination (recipe)**. Several things merge into one of a next tier, with lineage of inputs. Ids: matching-merge-three-upgrade, matching-combine-power-pieces. Fits spirits combining and a ship growing rooms.
8. **AttentionState (WorldAgent)**. Alertness of an NPC or world agent. Ids: exploration-stealth-awareness. NPC-only.
9. **Delegation / standing order**. Ids: defense-target-priority, command-workers-or-soldiers; needs scope, visibility, revocation.

Smaller partials: per-claim confidence for deduction (puzzles-scene-deduction); a distinct word for "windup" because Charge already means something else (projectiles-charged-release).

## Conflicts and the invariant each breaks

- rhythm-streak-multiplier: a reset on a miss is a progress penalty; engagement is not meaning. Keep streaks reset-free.
- defense-early-wave-call, allocation-public-goal-race: speed as worth; keep optional, no penalty for waiting.
- projectiles-graze-reward: danger as currency; keep it cosmetic.
- inventory-durability, inventory-death-retrieval: composted_work_cannot_remain_hidden_active_debt, silence_is_not_automatic_composting; a timer on loss becomes backlog pressure. Version: repair optional, loss leaves a Seed, no overdue.
- stealth-disguise-access: access_is_not_command, and consent_is_not_inferred; NPC and fiction only.
- stealth-security-network: surveillance of the player or real persons breaks consent and the permission purposes rule; NPC-only, no data collection.
- stealth-body-concealment, stealth-staged-accidents: deniable harm and deception, fine in fiction against NPCs, never a real person.
- combat-friendly-fire: harm to an ally by misplay; allow only with repair available and no blame.
