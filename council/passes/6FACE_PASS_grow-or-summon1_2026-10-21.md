# Growing a spirit or summoning a new one

**Run 2026-10-21**, started by the project coordinator from Wendell's message in the cave controls thread. Pass
`grow-or-summon1`. Rows: `council/callsheets/rows/grow-or-summon-2026-10-21.json` (six `gs-*` positions, no question).
The sibling thread "Sitting and door energy spirits" builds the sitting and the door's gas spirits; this pass sets the
rule it builds to. No casts were drawn this pass; no daemons sent.

**The ask, in his words** (2026-10-21 15:02 UTC):

> Now we've created the spirits the blobs that emerge from the door need to be the energy gas energy spirits and then
> sitting gross them into creatures and allies.
>
> We need a difference between harvesting energy to grow an existing spirit or summoning a new one altogether

## What the record already answers

- **What makes a spirit.** `sg-charge-disc`: a spirit is born from a charge worked through the whole W.A.V.E., and the
  same charge always makes the same spirit. `dp-bm-door-cave`: only charges worked through the whole W.A.V.E. go through
  a door as spirits.
- **What grows one.** `sg-holo-stages`: gas, core, hologram. The cave counts sittings per spirit and derives the stage
  from the count (`spirit-store.js`, `stageOf`; spirits-in-caves slices 2 to 4a). `sg-loop-trains`: stats come from
  playing well.
- **Who picks.** `bms-sit-whom`: you pick each time who to sit with. `bms-spirits-after`: you choose whether a charge's
  spirits are kept or let go.
- **Energy.** `cw-qi-meter-scales`: qi is a meter practice fills, and the vibeulon is condensed qi. Inner vessel
  (overruled `iv-no-mirror`): charge is fuel mined from environments, and spirit energy powers the ship.
- **Limits.** `sg-overcharge`: more charge than you can hold makes an unruly spirit. The loadout walks three at most.
  `sc-ruling-mortal`: every spirit you have needs tending, or it fades.

## The faces

- **Shaman.** The two acts must feel different in the body. Growing is feeding: motes leave you and go into a spirit
  already sitting with you, and it swells. Summoning is calling: the motes gather into a new cloud that comes out
  through the door. A new spirit asks for a new charge, because a spirit is a charge given a body.
- **Architect.** One store, two writes. Grow adds to an existing spirit's sittings (and qi, once qi exists in the cave).
  Summon adds one new entry at stage gas. A charge whose disc a spirit already carries can only grow that spirit
  (`sg-charge-disc`), so the store never holds two spirits from one charge.
- **Challenger.** A menu at the end of every sitting is friction. Default to the obvious choice and let one tap change
  it. Harvesting must never kill anything: daemons are never fought, and a wild gas you drain would be a fight by
  another name. (Dissent kept: the Challenger wanted no choice at all, the game deciding by match. The Diplomat's point
  below carried.)
- **Regent.** Summoning carries a cost, and the cost is care, not a price: each new spirit is one more to tend
  (`sc-ruling-mortal`). Show the count at the choice. No vibeulon price, since the record keeps vibeulons for releasing a
  spirit (`sc-offer-release`) and condensing qi.
- **Diplomat.** The player owns the choice (`bms-sit-whom`, `bms-spirits-after`). A player who wants many small spirits
  and one who wants one deep ally are both playing well.
- **Sage.** Reach test: every candidate question went back to its face with the record. Who picks: `bms-sit-whom`. Can
  qi alone summon: no, `sg-charge-disc`. Does summoning cost vibeulons: the record spends them elsewhere and treats care
  as the weight of a spirit; a position he can flip. Nothing is left that only he can answer, so no question goes to the
  board. Not unanimous: the Challenger's dissent is recorded.

## Positions (stand unless he flips them)

1. **`gs-two-acts`.** Summoning makes a new spirit; growing feeds one you already have. Summoning takes a charge
   worked through the whole W.A.V.E. that none of your spirits carries yet; the new spirit comes out through the door as
   a gas cloud. Growing takes energy only, and never makes a new spirit.
2. **`gs-harvest-is-qi`.** Harvested energy is qi. You harvest it by sitting, by practice, and from the places you go;
   it fills the qi meter or flows straight into a spirit you choose. It adds to that spirit's sittings, which move it
   from gas to core to hologram to creature to ally.
3. **`gs-door-gas`.** The blobs that come out of the door are your newly summoned spirits at the gas stage, one per
   charge worked through. Sitting with one grows it, as with any of your spirits.
4. **`gs-same-charge-grows`.** A W.A.V.E. on a charge one of your spirits already carries grows that spirit; it never
   makes a second. A new charge in a family you already have offers both at the end of the sitting: "Feed Fear" with
   the spirit you have, or "Call a new one". The likelier choice is lit; one tap changes it.
5. **`gs-show-the-flow`.** The difference is seen. Grow: motes stream from you into the spirit sitting with you, and it
   swells. Summon: motes gather into a new cloud that drifts out through the door. Reduced motion fades instead.
6. **`gs-care-is-the-cost`.** Summoning has no vibeulon or qi price. Its cost is care: the summon choice says how many
   spirits you tend. Harvesting never harms a wild spirit.

## Test

Cave test, after the sibling's build: a sitting with a spirit you have adds to its sittings and adds no store entry;
a W.A.V.E. on a new charge adds exactly one entry, at gas, seen leaving the door; a repeated charge adds none.

## Recommended next move

The sibling thread "Sitting and door energy spirits" builds positions 3 to 5 with the sit fix, in the same bars-engine
pull request, and adds the test above. Position 2's meter waits on qi reaching the cave (passport field owned by the
vessel), so until then a harvest is a sitting.
