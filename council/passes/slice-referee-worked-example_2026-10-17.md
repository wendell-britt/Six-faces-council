# The referee, worked through two scenes (battle roll and story roll)

**2026-10-17**, a short answer thread, not a pass. Wendell answered `q-slice-referee-clear` B at 20:03 UTC (ledger
`council/ledger/2026-10-17-pull-200544.json`): *"The roleplaying referee itself operates on multiple levels depending
on the system. Battle mechanics and non battle skill mechanics. In this case the uncertainty would be around solving
story encounters and faction relationships"*. The ontology QUICKSTART is the only ontology loaded. Every number
below is a placeholder; none changes the game. Battle figures come from the pass 2 simulation
(`council/passes/slice2-sim/chart.mjs`, sprout main). Story figures are invented for this example, in the same
shape.

## What he said, in the referee's terms

He is right that a tabletop referee works on levels. A tabletop book has combat rules, skill rules and social rules,
and one way of running all of them. The slice's referee has the same split:

- **One procedure** that every uncertain action runs through (five steps, below). This is the referee.
- **A rule set per kind of scene** that answers step 2 of the procedure. The battle rule set is the five-element chart.
  The story rule set is "does what you brought meet what they need" (the trust loop's reading of a need). A
  faction rule set is a standing that the other two move.

The referee decides one question: *did this attempt land, and what is written down about it*. It never writes the
story and never says how the player feels.

## The five steps (the same every time)

1. **Who is trying what, against whom.** The player's move and the other side.
2. **Fit.** The scene's rule set says how well the move meets what the other side needs. Battle: the chart. Story:
   the need the player has listened to.
3. **Odds, then one roll.** The player sees the odds before choosing. One roll against them.
4. **Result.** Lands, or misses. A miss costs the beat and a little, and never leaves the player without a safe move
   (the trust loop's "Show Up Honestly", the fight's Listen).
5. **One logbook line.** What was tried, the fit, the odds, the roll, the result, and what moved. Nothing else
   changes the world.

## Scene 1: a battle roll (the Earth spirit in the ring)

The player has restrained the Earth spirit with a controlling stance (the fight takes 8 off its Demand), then offers
fertilizer. The simulation of every stance line gives the offering odds:

| What the player did | Offering odds | Turns |
|---|---|---|
| Restrain, then feed | 95% (the cap) | 5 |
| Control, control (only damage) | 75% | 2 |

1. Player tries the offering, against the Earth spirit.
2. Fit: the chart says the controlling stance hit and the feeding stance fed. The spirit has been fed.
3. Odds 95%. The roll comes up 41. Under 95.
4. Lands: the spirit becomes an ally.
5. Logbook line:
   `day 3 | offering | Earth spirit | restrained then fed | odds 95 | roll 41 | lands | ally: yes | fed: yes`

If the player had only damaged it, the odds are 75%, the roll may still land, and the line says `fed: no`. That
difference is the whole point of the logbook: the fight's result is the same ally, and the world's memory is not.

## Scene 2: a story roll and a faction (the Tender at the gate)

The next morning a neighbor from a placeholder faction, the **Tenders**, stands at the farm gate. The scene is in the
game because a logbook line from yesterday made it: the Tenders saw an offering with `fed: no`. Nobody scripted
"morning of day 4". The scene's rule says *when a line has `offering` and `fed: no`, Mara comes to the gate*.

Mara carries a hidden need, one of the five elements, as the trust loop does for its NPCs. The player holds three
cards of different channels. The loop's own rules supply the shape: the need is hidden until the player **Attunes**
(listening spends the beat), a card of the matching channel meets it, a wrong card is a misread, and "Show Up
Honestly" is always on the table and never negative. The odds table below is invented in the battle's shape (a right
fit starts at 75%, listening first adds 20, the cap is 95%, a misread starts at 40%).

**The player listens first, then answers.**

1. Player tries to answer Mara, a Tender.
2. Fit: the player Attunes (costs the beat) and learns she needs Earth: to be told what happened to the field,
   plainly. The player plays the Earth card ("Tell it plainly"). A match.
3. Odds: 75 for the match, plus 20 for listening first, is 95. The roll comes up 88. Under 95.
4. Lands: Mara's trust rises 3 to 5.
5. Logbook line:
   `day 4 | talk | Mara of the Tenders | need Earth, listened | card: tell it plainly | odds 95 | roll 88 | lands | trust 3→5 | Tenders standing +1`

**The player skips the listening and guesses.**

1. Same.
2. No Attune. The player plays a Fire card ("Offer a hand"). Mara needs Earth. A misread.
3. Odds 40. The roll comes up 55. Over 40.
4. Misses: Mara's trust drops 3 to 2 and the player's beat is spent. Show Up Honestly stays available. Only repeated
   misreads can rupture her, as in the trust loop.
5. Logbook line:
   `day 4 | talk | Mara of the Tenders | need Earth, not listened | card: offer a hand | odds 40 | roll 55 | misses | trust 3→2 | Tenders standing 0`

### What a faction is

A faction is a standing number the referee keeps for a group, moved only by logbook lines that name a member of that
group. Nothing else moves it. Mara's line above moved the Tenders by +1. Standing opens and closes doors the way a
logbook line does: when the Tenders reach +2, a scene can fire at their gathering ("the Tenders ask you to the
compost circle"). A standing never rolls by itself. It is the running total of rolls the referee already wrote down.

### What the story gets

The story layer reads two records only: the logbook (what happened) and the standings (what the groups think of you).
A scene's door is a condition on those, e.g. `Tenders standing ≥ 2` or `the last offering was fed: no`. The twine
passage text stays unwritten; the engine proves the door opens. Pass 2's test `slice-referee-off`
becomes concrete: switch the referee off and no line for Mara is written, so Mara never arrives, the standing never
moves, and the compost-circle door never opens.

## The same referee, two rule sets

| | Battle | Story |
|---|---|---|
| Step 1 | offering against the Earth spirit | answer Mara |
| Step 2: fit | the five-element chart | Attune, then match the need |
| Step 3 | 95% (restrained then fed) | 95% (listened, matching card) |
| Step 4: a miss | beat spent, Listen stays | beat spent, Show Up Honestly stays |
| Step 5: the line | `offering … fed: yes` | `talk … trust 3→5, Tenders +1` |
| Who computes settledness | the game, for the spirit | the game, for Mara's trust; never for the player |

The player's own state is never rolled or named. If a scene's spirit is made of the player's feeling, as in the daemon
meeting, the player says whether it is settled, and the referee writes that down as their answer.

## What this example leaves open

- The numbers (95, 75, 40, 20) are placeholders in one shape. The real ones come from the bots in feasibility test 5,
  and they are his to rule.
- Mara and the Tenders are invented to carry the example. A real faction list is a content question that waits until
  the engine runs.
- The trust loop keeps its own cards and reducer in bars-engine. The slice borrows its shape (hidden need, Attune,
  never-negative basic move, rupture by misreads only) and writes its own small version in sprout.
