# Gaps and conflicts, part a (Care & sustain, Develop & interact, Produce & manage)

143 mechanics: 76 covered, 44 partial, 3 gap, 20 conflict. Source: crosswalk-a.yaml. All names below are the council's word, may be cut.

## Candidate ontology additions

1. Flow Network (council's word, may be cut). A graph of conserved quantities moving from makers to users, with
   rates, splits, filters and byproducts. The ontology has Mechanic and Rule but nothing for a conserved flow.
   Needed by: automation-belt-routing, -flow-splitting, -fluid-routing, -item-filtering, -production-chain,
   -aerial-logistics, -byproduct-loop, -power-budget, commerce-dynamic-market, commerce-trade-route-programming.
   Fits calrunia (qi to vibeulon) and living-ship. Keep conservation visible as world state, not a gauge.

2. Capacity Budget (council's word, may be cut). A bounded stock with a refill and a spend, whose running out
   ends a trip or round and never marks a person as failed. Needed by: gathering-oxygen-gathering,
   automation-power-budget, ecology-habitat-capacity, incremental-allocate-progress-capacity, fishing-pond-production,
   survival-fatigue-rest.

3. Tended Living Thing (council's word, may be cut). A care cadence for a creature or plant, where neglect
   ends in a release path (the seed, the letting-go vibeulon) and never in debt or blame. Spirit-care already
   behaves this way, and the ontology has Seed and CompostRecord but no object for the cadence itself.
   Needed by: farming-growth-care, farming-livestock-care, gathering-renewable-forage-route,
   survival-fatigue-rest, ecology-animal-taming, fishing-pond-production.

4. Delayed Return (council's word, may be cut). An errand, trap or investment whose reward arrives later, with
   no penalty for how long the player is away. Needed by: incremental-limited-team-dispatch,
   fishing-passive-traps, farming-orchard-investment, automation-aerial-logistics.

5. Timed Window (council's word, may be cut). A short span in which an action lands, whose miss changes the
   item and nothing about the player. Needed by: cooking-heat-window, fishing-bite-window.

6. Inner Room (council's word, may be cut). A space that counts as a kind of room by practice done in it, not by
   item count. Needed by: building-room-requirements, building-structural-support, building-service-coverage.
   Fits living-ship and room-kit.

7. Release Residue (council's word, may be cut). A mechanic-level pairing of a release act with an optional keepsake
   (seed, parts, reset boost). CompostRecord and CompostResidue cover the governance, but no ontology object covers
   the in-play ritual. Needed by: gathering-salvage-dismantling, progression-prestige-reset,
   progression-successor-selection, automation-byproduct-loop.

8. Lineage Heritage (council's word, may be cut). Traits passed from one creature or run to the next, with
   provenance kept. Needed by: ecology-parent-trait-selection, ecology-plant-crossbreeding, progression-evolution-recipes.

## Conflicts and the invariant each breaks

- progression-challenge-tiers, relationships-faction-reputation: a tier or standing ladder reads as
  no_global_developmental_rank_for_person. Keep per line, per activity, chosen.
- progression-death-loses-training: a permanent loss on failure breaks recoverability ("No path has to be wasted").
- survival-competing-needs, farming-livestock-care, relationships-daily-contact, commerce-timed-contracts,
  commerce-debt-pressure, cooking-order-triage, incremental-offline-window: composted_work_cannot_remain_hidden_active_debt
  and the composting stop list (backlog pressure, overdue status, shame messaging). Keep as gifts and a release.
- survival-stress-crisis: player_authors_personal_inner_meaning, when the stress state is read as the player's.
- ecology-population-limits: culling a creature that is a relationship; letting go is the version that works.
- narrative-timed-response, narrative-conversation-intervention: pressure on disclosure; refusal and silence must stay valid.
- narrative-background-dialogue-access: type_is_not_level, sect choice does not establish altitude.
- relationships-gift-allocation: consent_is_not_inferred_from_..._acquisition.
- relationships-persuasion-checks: consent inferred from compliance (fine for NPCs only).
- relationships-secrets-leverage: disclosure_is_not_progression_currency.
- relationships-bond-scenes, relationships-companion-approval: access_is_not_command, and external approval does not prove
  inner transformation. A bond number should become domain-scoped trust.
