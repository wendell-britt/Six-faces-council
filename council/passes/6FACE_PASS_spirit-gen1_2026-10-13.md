# Six-face pass: the spirit generator, intake 1

2026-10-13. Called by the coordinator on Wendell's chat in the thread "Type-chart fight: the Fixer" (sprout #50), 23:33 UTC:

> "Ok so a mismatched ally gets defeated too quickly. I do think this is where pokemon stats balance the game out and
> moves are bonuses on stats.
>
> We will need to develop a spirit generator à la monster rancher and contexts for spirits to train and grow stronger
> by getting better at the overall game loop"

The first half is built (`sf-stats-carry`, sprout #50). This pass takes the second half. It is the first pass on the
subject, under the board position `sf-generator-next`.

Casts (`cast.py --json`, three coins): Shaman 16 Anticipation; Architect 35 Sunrise, becoming 42 Windfall; Challenger
12 Stalemate; Regent 54 Home Field Advantage, becoming 17 Following; Diplomat 33 Retreat, becoming 53 Emergence; Sage
55 Fullness, becoming 14 Noon. The ledger record `2026-10-13-spirit-gen1.json` carries them.

## Scorecard

No earlier pass on the generator. The test this subject inherits is `sf-stats-carry`'s: every ally wins standing in 3
to 5 turns. It passed on sprout #50 by a scripted run. A generated spirit has to keep passing it.

## Anchor

A spirit is born from something the player really brings, and it grows stronger as the player gets better at the
game's whole loop. Monster Rancher is the model he named.

## What the record already holds

- **Stats.** `spirit-five-stats` and `sf-stats-carry`: HP, power, guard, magic and speed; a spirit's element grows its
  matching stat twice as fast; moves are bonuses on stats.
- **Where spirits come from.** `wave-spirit-from-charge`: in prompted and integrated modes the daemon is made from the
  charge the player brings (feeling, strength, urge, the belief of the block), and story mode keeps a table.
  `wave-integrate-ladder`: loot, then a move, then a companion. His chat ruling of 2026-10-13 on the WAVE space: spirits only after
  the whole W.A.V.E. `demo-spirit-count`: 25 species (five elements, five regions, three moods), five in the demo.
- **Growth.** `spirit-growth-by-training`: Monster Rancher's model; sparring in the ring trains a stat the player picks,
  fights in the forest raise level, satisfaction does loyalty's job, no lifespan and no death. `sf-ally-moves`: a level
  per fight won standing, moves at levels 1, 3 and 5. `sf-moves-from-people`: the villages teach their styles.
  Settlement bouts follow Monster Rancher's host organisations, cups and invitations (design.md, Decided, as quoted in
  pass sprout-demo13). design.md cites Monster Rancher 2's grades, E to S.
- **The rule his ask may change.** design.md, "Decided: allies", as pass sprout-demo13 quotes it: "Spirits do not grow
  by working. The player levels them, by sparring with them in the ring or fighting other spirits in the forest."
- **His ruling on outer work.** Board read of 2026-10-06 (ledger `2026-10-06-board-read-saved-answers.json`): "real
  work action is the highest killed play avaiable", with three modes of play, the third "where you can actually have
  players metabolize their outer work into ingame success".

This session could not open sprout's design.md itself; the quotations above come from the council's own passes and
ledger. The next build thread reads design.md before it builds.

## The six faces

### Shaman

16, Anticipation: the good part has started and the event has not. A spirit should arrive the way thunder comes up out
of the ground, as the player's own charge returned to them as a creature.

**The charge is the disc.** In Monster Rancher you put any CD in the shrine and the game reads it into a monster, and
the delight is that your own CD becomes a creature nobody else has. Here the player brings the charge
they worked through the whole W.A.V.E. The record already makes the daemon from that charge
(`wave-spirit-from-charge`), and the integration ladder already turns a met daemon into a companion. The generator is
the moment the integrated daemon steps over as a spirit, shaped by the same charge.

**The same charge gives the same spirit.** Monster Rancher's discs are deterministic, which is why players trade them.
A feeling, a strength and an urge that are the same give the same spirit, so a player who brings the same block twice
meets an old friend.

### Architect

35, Sunrise, becoming 42, Windfall: this is becoming visible faster than planned, and more is arriving than was put in.
The structure is mostly in the record already, so the Architect assembles it and adds only the seams.

**The generator reads four fields.** The feeling sets its element (`wave-offered-feeling`); the region where it was met
sets the species among the 25; the strength (a little, a lot, too much) sets the starting stat total; the urge sets
which two stats lead, the way a Monster Rancher breed shows its top two or three stats. The belief line becomes the
words the spirit says when it joins. A spirit's matching stat grows twice as fast, as `sf-stats-carry` has it. Each
stat shows a grade, E to S, on the status screen and never in the fight. Story mode draws the same fields from a table.

**Five places to train.** The ring (a spar trains one stat the player picks), the forest (wild fights raise level), the
settlement bouts and cups (rank and invitations), journeys to the villages (Monster Rancher's errantry: the ally learns
that village's move), and, if he says so on the board, the outer world.

**Getting better at the loop is what trains.** A spar or a fight is a run of the loop, and each step played well adds to
one stat: listening before answering adds speed, the right answer on the chart adds power, holding adds guard, letting
go adds HP, and an integration adds magic. Fight alone still trains, less, and lowers satisfaction, as
`spirit-growth-by-training` says. Numbers are placeholders.

### Challenger

12, Stalemate: you are seeking one game and wearing the face of the other. The risk is a generator that looks like Monster
Rancher and plays like a stat sheet.

**The test that could prove it wrong.** A scripted run of ten spars: a careful player (listens, answers on the chart,
holds, lets go) against a Fight-masher, on the same spirit. If the masher's spirit ends as strong, "getting better at
the loop" is not what trains, and the design failed. Second check: two different charges must give spirits that differ
in their two leading stats, and the same charge must give the same spirit twice. Third: a generated spirit still wins
standing in 3 to 5 turns against Ama Rell's Fixer. All three run as a script at phone width before he plays.

**What would show it false in play.** If his phone play finds he cannot tell why his spirit got stronger, the link from
play to growth is invisible. Each spar ends with one line naming the stat that rose and the step that raised it.

### Regent

54, Home Field Advantage, becoming 17, Following: following rules nobody told you. There is a Decided rule this ask
walks into, and he has not been told.

**The fork is real and only he can settle it.** design.md says spirits never grow by working. His new words ask for
growth from "getting better at the overall game loop", and his ruling of 2026-10-06 says real work action is the
highest skilled play and names a mode where outer work becomes in-game success. Read one way, the Decided rule stands
and the loop means the ring and the fights. Read the other way, outer-world action is part of the loop. The record holds
both, and which one wins changes what gets built. It goes on the board as `sg-work-grows`.

**What stands either way.** In-game chores, if the settlement ever has them, do not train a spirit. That keeps "skill is
bought only with skillful play", which no option here touches.

### Diplomat

33, Retreat, becoming 53, Emergence: leaving is available, and the stages cannot be skipped. Build the smallest stage
first.

**One slice, on the page he already plays.** The fight page on sprout #50 keeps placeholder allies today. The first
build replaces them: he enters a charge (feeling, strength, urge) or picks one from the table, meets the spirit it
makes with its status screen and grades, spars it three times in the ring, then takes it into the Fixer fight. The
other training places wait until the ring has been played.

**A stranger needs one sentence.** The five-year-old sentence for the screen: "Your feeling made this spirit. Train it by playing well."

### Sage

55, Fullness, becoming 14, Noon: everything is visible at once, and noon is when the light starts down. Most of this was
already decided; the pass gathers it and asks one question.

**Contributions.** The Shaman's charge-as-disc and same-charge-same-spirit are kept as `sg-charge-disc`. The
Architect's four fields, grades and five places are kept, split into `sg-charge-disc` and `sg-loop-trains`. The
Challenger's three checks and the one-line spar result are kept in `sg-first-slice`. The Regent's fork is the one
question. The Diplomat's slice is `sg-first-slice`. Nothing was dropped. No daemons were sent; the record answered every
problem a face raised.

**Nobody dissented on the positions.** On the question the Regent
would hold the rule (B) and the other four would widen it to outer-world action (A). A unanimous pass on the positions is a flag: every position here assembles rulings already on
the board, so the risk is that the council read its own record back. The Challenger's scripted test is the check
against that.

## Verdicts

| Face | sg-charge-disc | sg-loop-trains | sg-first-slice | sg-work-grows |
|---|---|---|---|---|
| Shaman | yes | yes | yes | A |
| Architect | yes | yes | yes | A |
| Challenger | yes | yes, if the test passes | yes | A |
| Regent | yes | yes | yes | B |
| Diplomat | yes | yes | yes | A |
| Sage | does not rule | does not rule | does not rule | does not rule |

## Outputs

### Positions (each stands unless Wendell flips it)

1. **`sg-charge-disc`.** The charge is the disc. A spirit is born when a daemon you met through the whole W.A.V.E. joins
   you, and it is made from that charge: the feeling sets its element, where you met it sets its species among the 25,
   the strength sets its starting stats, and the urge sets its two leading stats. The same charge always makes the same
   spirit. Each stat shows a grade from E to S on its status screen. Story mode draws from a table. Why it did not need
   Wendell: his "à la monster rancher", `wave-spirit-from-charge`, `wave-integrate-ladder`, `demo-spirit-count`,
   `spirit-five-stats`, and design.md's Monster Rancher 2 grades.
2. **`sg-loop-trains`.** Spirits train in the ring, the forest, the settlement bouts and on journeys to the villages, and
   playing the loop well is what makes them stronger. In a spar or a fight each step played well adds to one stat:
   listening first adds speed, the right answer adds power, holding adds guard, letting go adds HP, and an integration
   adds magic. Fight alone trains less and lowers satisfaction. Each spar ends with a line naming what rose and why.
   Why: his "grow stronger by getting better at the overall game loop", `spirit-growth-by-training`, `sf-ally-moves`,
   `sf-moves-from-people`, and design.md's bouts and cups.
3. **`sg-first-slice`.** The first build replaces the placeholder allies on the Fixer fight page (sprout #50): enter or
   pick a charge, meet the spirit it makes, spar it three times, then fight. It ships only if a script shows a careful
   player's spirit ends stronger than a Fight-masher's after ten spars, that different charges lead with different
   stats and the same charge repeats, and that a generated spirit still wins standing in 3 to 5 turns. Why: the
   short-sessions rule, `sf-generator-next`, and the Challenger's test.

### Question (passed the reach test)

**`sg-work-grows`: Does real-world action make your spirits stronger, or only play in the ring and fights?** The Regent
owns it, with the Architect. Options and consequences are on the board row. Why only he can answer: design.md's Decided
rule and his own ruling of 2026-10-06 point different ways, and his new words fit both. Why it was not asked before: no
build until now let a spirit grow from anything but a fight.

## Tests set

- T1 (by the build thread, before his play): the three scripted checks in `sg-first-slice`.
- T2 (his phone play of the slice): he can say why his spirit got stronger after three spars.
