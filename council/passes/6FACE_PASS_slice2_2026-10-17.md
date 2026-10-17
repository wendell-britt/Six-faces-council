# Six-face pass 2 — the engine slice after Wendell's board answers

**Run 2026-10-17**, started by the coordinator on Wendell's board answers of 06:22–06:26 UTC (ledger
`council/ledger/2026-10-17-pull-062632.json`). This is pass 2 on the engine slice. Pass 1 is
`council/passes/6FACE_PASS_slice1_2026-10-16.md`. The subject's home is sprout (Wendell, 2026-10-16).
The `design-ontology` light profile (QUICKSTART) is loaded for every face. The Architect sent the
Controller and the Challenger sent the Skeptic, both on research.

His words, which set the three subjects of this pass:

- On `pos-slice-rules`, overruled: *"We need to explain this to the degree is makes sense to me before we move
  forward. This sounds like mumbo jumbo"*
- On `q-slice-typechart-inferred`, steer: *"We’ll need to do deeper research on this. Let’s let the 6 game masters
  go after this but with the pokemon type system as a model and how the pokemon moves use the pokemon stats to
  balance the game"*
- On `pos-slice-encounter`, overruled: *"We may need to think through this more. It feels like there is a gap
  we’re skipping over to keep it coherent with work we’ve already done. Let’s have the 6 game masters explore how
  to actually bridge this gap rather than papering over it"*
- On `pos-slice-passage`, overruled: *"These are the main things we need feasibility testing on. If we get this
  engine going then generating content will be a breeze"*
- `q-slice-playtest-order` answered B (build the engine slice first, one combined playtest after);
  `q-slice-heart-pool` answered C (keep the pool, revisit after the first live playtest); `pos-slice-day` stands.

## Scorecard

Pass 1 set three tests. **`zo-race-test`** and **`zo-quota-wiring`** (due 2026-10-17) have not run; scheduled work
stays blocked behind them, and this pass is local work. **`slice-falsifier`** (the referee switched off) cannot run
yet, because no shared referee exists. Pass 1's positions on the rules, the passage and the encounter were all
overruled. All three failed the same way: each used the ontology's record names in place of saying what a player
would see. That is the lesson this pass carries.

## Anchor

Unchanged: *a playable ontology for helping people install integral consciousness, somatic awareness and shadow
work through accessible story driven play*, on his four layers (story on a daily chore loop on a battle encounter,
with tabletop rules that can change the story).

## Casts (three coins, `council/iching/cast.py --seed 20261017`)

| Face | Hexagram | Changing lines | Becomes |
|---|---|---|---|
| Shaman | 47 Drained 困 | — | — |
| Architect | 26 Reserves 大畜 | 3, 6 | 19 Spring 臨 |
| Challenger | 36 Nightfall 明夷 | 1, 2, 3 | 7 Muster 師 |
| Regent | 34 Vigour 大壯 | 2, 6 | 30 Burning 離 |
| Diplomat | 60 Measure 節 | 4, 6 | 10 Footing 履 |
| Sage | 37 Household 家人 | 3, 5 | 27 Feeding 頤 |

## The plain explanation (delivered first, in the thread)

The rules position, as sent to Wendell on 2026-10-17 before this pass went further: each part of the slice does
its own math (`slice/fight.js` takes 8 off for a controlling stance, `slice/offering.js` rolls its own odds,
`slice/wave.js` has a third set of numbers). A tabletop game has one rulebook: every uncertain action runs the same
steps, and the GM writes down what happened. The engine slice needs one **referee** that every part of the game asks,
and that keeps a **logbook** the story can read. A scene fires on a logbook line ("you beat this spirit down without
ever feeding it"). The falsifier is to switch the referee off: if the game plays the same, the rules layer was
decoration. "EncounterOccurrence" and "MoveInvocation" are the ontology's names for a logbook line per encounter and
per move.

## The faces

## Shaman: 47 Drained

**The reading bears on the overrules directly.** Drained says the explaining continues and the basin is dry, and that
words spoken now land badly. Pass 1 spoke in record names to a designer who plays, and he heard mumbo jumbo. **The
felt standard is unchanged:** he plays one day and says whether labor turned into story without a dashboard. **The
Shaman's concern on the type chart is what the fight teaches the body.** Feeding a spirit with the stance that
generates it is the cycle's nourishing half; a chart that makes the same element hurt (the builder's guess, 3 damage)
teaches that meeting like with like is an attack. **The Shaman's concern on the bridge is who owns satisfaction.**
In the daemon meeting (`dmt-two-axes`, `dmt-spirit-from-answers`) the spirit is built from the player's own feeling,
and the player says whether it is settled. In Sprout's negotiation fight satisfaction is a number the game computes
from feeding. Constitution 10 holds: the game may not name the player's inward state for them. **Standing test:**
nothing in the engine may compute a player's satisfaction; it may compute a creature's.

## Architect: 26 Reserves, becoming 19 Spring

**The reading names the store.** Reserves is force held under a mountain, and Spring says now is when to spend it.
The council has stored three encounter engines and a type chart's shape without naming the day the numbers get
stats. **The Controller's research (report `council/daemons/reports/`, pass slice2) found what Pokémon's chart is:**
an 18 by 18 attacker-by-defender table, mostly neutral (about 204 of 324 cells), with 2x, ½x and 0x cells, dual types
multiplying, and a same-type bonus of 1.5. **The chart sets ratios; stats and moves create the choices.** Damage
combines move power, the attacker's attack stat over the defender's defense stat, level, the same-type bonus, the
chart multiplier and a random roll (0.85 to 1.00). Each move since Gen IV carries its own category (physical or
special), so one creature can be strong one way and soft another. The formula's exact shape is from memory; the
Bulbapedia page returned 403 to the research, so it is marked unverified.

**What must be true in the machine, from a simulation run today.** A brute-force run of every stance sequence up to
six turns against the Earth spirit with the current placeholders (script kept with the pass:
`council/passes/slice2-sim/chart.mjs`, run against sprout main) gives:

| Line | Offering odds (fertilize) | Turns |
|---|---|---|
| Controls, controls | 75% | 2 |
| Same element four times | 75% | 4 |
| Generated-by five times | 75% | 5 |
| Generating stance six times | 79% | 6 |
| One control, then feeding | 95% (the cap) | 5 |

**The chart barely discriminates.** Any line that only damages reaches 75%, and dozens of lines reach the 95% cap.
The two guessed relations never appear in a best line and change nothing that matters. **The open question is not
what "same" and "generated-by" should deal; the fight has no stats, so the chart alone has to carry every choice, and
its numbers saturate.** **The Architect's recommendation, from the Controller's moves:** keep the cycle as the
table (it is design.md canon) and give it Pokémon's other half. Each stance gets a power; each spirit gets an attack
and a resist stat from its **family** (the daemon it belongs to, as the spirit loop already builds families); its
element is its type; its strength (little, a lot, too much, already in `wave.js`) is its level; the bonded
ally's element gives the same-type bonus. Listen (Ting) and feeding are the status moves. The chart becomes ratios:
controls 2, same 1, generated-by ½, controlled-by turns back on the player. **This runs in simulation first, not in
the game.** Sprout's rules reserve balance to him.

## Challenger: 36 Nightfall, becoming 7 Muster

**The reading:** a light kept covered and still lit, becoming the unsaid fact that would organise the force. **The
unsaid fact is what the player knows when they pick a stance.** **The Skeptic's research** found Pokémon's balance
was repaired by addition, never by nerfing: Gen I Psychic was unchecked until Dark and Steel arrived in Gen II, and
Fairy arrived in Gen VI to check Dragon. A five-part cycle gives every element equal allies and enemies, as Magic's
colour pie does, and in an odd cycle the best reply to a known element is always the same stance. **Flat claim:** in a
pure cycle, stats only create choices if stances differ in cost or risk. **The simulation confirms it for the slice:**
once Listen has shown the spirit's element, the fight is a one-step lookup, and the numbers cap out. **Two breaks the pass 1
encounter position skipped:** sprout holds two charts that disagree (`fight.js` uses flat damage per relation;
`wave.js` uses multipliers, `restrainBonus` 1.5 and `hitMult`), and the slice's Earth spirit belongs to no family,
while every spirit since the daemon meeting does. **Falsification tests:** (1) a bot that always plays the
controlling stance must win the ally less often than a bot that restrains then feeds, under any chart model the
engine adopts; (2) two spirit families with the same element must call for different best lines, or the stats are
decoration; (3) the referee switched off must change the logbook. **Verdict:** support the stats model, conditioned on
the three tests running before any number reaches the game.

## Regent: 34 Vigour, becoming 30 Burning

**The reading:** force available and unaimed, like a ram catching its horns in a hedge; then the same true sentence
repeated until it consumes its subject. Pass 1 repeated the ontology's names until they consumed the meaning. **What
must be preserved:** design.md's three decided relations (controlling hits hard, generating feeds, being controlled
hurts), the daemon meeting's rulings (daemons are never fought, you spar their spirits; satisfaction and veil are two
measures; the player says which), the trust loop's no-dead-end rule (bars-engine
`.specify/specs/trust-encounter-loop/spec.md`: a basic move is always available and never negative), and sprout's
CLAUDE.md (no rule, balance or story change without him). **Reserved to him:** the chart's numbers once the
simulation has data, and whether the plain explanation makes enough sense to build on, which he named as his gate.
**Definition of done for the engine slice, in plain words:** one referee, one logbook, one scene that fires from a
logbook line, one day that closes with sleep, the Sprout fight and the ring offering both asking the referee, and the
three falsifiers green. **Standing test:** every row this pass sends him says what a player would see before it says
a record name.

## Diplomat: 60 Measure, becoming 10 Footing

**The reading:** past what you can hold, with the edge unsaid; then stepping onto ground that matters, where the
quality of the step keeps it safe. **The edge pass 1 failed to state is the reader.** Every row from now on is written
for Wendell as a player first. **The bridge, in the household's terms:** the four encounters already built are one
encounter in four costumes, and reuse beats rebuild:

| | Sprout spirit fight | Sprout WAVE fight | bars-engine trust loop | Daemon meeting (council #240) |
|---|---|---|---|---|
| What is hidden | the spirit's need ("space") | the spirit's stance, then its next gate | the NPC's live need | nothing: the player's answers build the spirit |
| The listening move | Listen (Ting), costs the turn | Welcome, the push lands in full | Attune, spends the beat | the approach check-in |
| The right answer | a stance by the five-element cycle | a gate by the trigram cycle | a card that meets the need | sparring the family's spirits |
| What falls | HP and Demand | the charge | shadows, dissolved by trust | — |
| What rises | satisfaction (computed) | seize, borrowing | trust | settled or not (the player says) |
| How it ends well | offering, then ally | integrate or release, Witness Book page | convert, ally, four domains | ally stands honored, vouches once |
| How it ends badly | player HP 0, start over | the push lands | rupture, only by misreads | none; walking on is an answer |

**What bridges them without forcing one engine:** every encounter has a spirit (element, family, strength, veil or
flood), a move list checked against it by a chart, something that falls and something that rises, a listening move
that costs tempo, and endings that include walking away. The referee resolves each move the same way and writes the
same logbook line; each engine supplies only its chart and its move list. No code moves between repos. **Standing
test:** the bridge can be said to a stranger in one sentence: *every encounter is a spirit you listen to, answer, and
either befriend or leave, and the game writes down what happened.*

## Sage: 37 Household, becoming 27 Feeding

**The reading:** an arrangement formed without being discussed; positions held properly inside produce order
outside; then look at what each part feeds on. The household here is four encounters that grew up apart, and what
feeds them is the logbook. **The Sage orders the smallest coherent whole.** The Diplomat's bridge stands first: one
encounter grammar, four costumes, one referee and one logbook. The Shaman's line stands inside it: the engine
computes a creature's settledness and asks the player for theirs. The Architect's stats model stands second, in
simulation only. The Challenger's three falsifiers are its exit test. The Regent's gate stands last and first: the
referee is built only once he says the plain explanation makes sense. **Kept from every face; nothing dropped.**
**Dissent:** the Challenger supports the stats model only on its tests; the Shaman doubts the guessed "same element
hurts" relation on what it teaches. Both are carried as conditions. The Sage recommends and does not decide.

## Verdicts

| Face | Rules, explained | Type chart | Encounter bridge | Feasibility first |
|---|---|---|---|---|
| Shaman | Speak as a player | Same element should not teach harm | Player's satisfaction is asked, never computed | Felt test after the engine runs |
| Architect | One referee, one logbook | Pokémon's other half: stats, power, same-type bonus | Family = stats, element = type, strength = level | Simulation before game |
| Challenger | Falsifier: referee off | Chart saturates; one-step lookup | Two charts in sprout; Earth spirit has no family | Three falsifiers are the exit |
| Regent | His gate: it makes sense | Numbers are his once data exists | Preserve design.md, daemon meeting, no-dead-end | Done = referee, logbook, scene, day, two callers |
| Diplomat | Rows written for a player | — | Four costumes, one grammar | Reuse beats rebuild |
| Sage | Gate first | Simulate, then ask | Bridge stands first | Build order as above |

## Dissent check

The pass was not unanimous: no face opposed, and the Challenger and the Shaman set conditions, recorded in the positions.

## Outputs

### Positions (stand unless he flips them)

| id | faces | Position |
|---|---|---|
| `pos-slice-bridge` | diplomat, architect, shaman, regent | The four encounters already built (Sprout's spirit fight, Sprout's WAVE fight, bars-engine's trust loop, the daemon meeting) are one encounter in four costumes. Each has a spirit, a move list checked against it by a chart, something that falls, something that rises, a listening move that costs a turn, and endings that include walking away. The engine slice builds that shared shape once, as the referee and its logbook; each engine keeps its own chart and moves, and no code moves between repos. Where the spirit is made of the player's own feeling, the player says whether it is settled; the game only computes a creature's settledness. |
| `pos-slice-chart-stats` | architect, challenger, shaman | Pokémon's lesson for Sprout is that the chart sets ratios and stats make the choices. Today the fight has no stats, and a simulation of every line shows the chart barely matters: any damage-only line reaches 75% offering odds, many reach the 95% cap, and the two guessed relations never appear in a best line. The six model the fight on Pokémon in simulation only: stance power; spirit attack and resist from its family; element as type; strength as level; the bonded ally's element as the same-type bonus; ratios of 2, 1, ½ and turn-back. The question on the two guessed relations comes back to you with the simulation's numbers. |
| `pos-slice-feasibility` | challenger, architect, regent | Engine feasibility comes before content: (1) the referee, which the spirit fight and the ring offering both ask, keeping one logbook; (2) one placeholder scene that fires from a logbook line and not from a script; (3) one day that closes with sleep and writes the day's page; (4) the Sprout fight writing the same logbook line shape bars-engine's trust loop can write; (5) the chart-and-stats model run by bots. It passes when the always-control bot does worse than restrain-then-feed, two families of one element need different best lines, and switching the referee off changes the logbook. Then one combined playtest (your answer B). |

### Questions (passed the reach test)

| id | owner | Question |
|---|---|---|
| `q-slice-referee-clear` | regent, diplomat | Does the plain explanation (one referee every part of the game asks, keeping one logbook the story reads) make enough sense to build on? Only he can say whether it makes sense to him, and he made that the gate. |

## Tests set by this pass

- **`slice-bots-chart`** (Challenger, due 2026-10-24): the three falsifiers above run green in sprout.
- **`slice-referee-off`** (Architect, due 2026-10-24): the referee switched off changes the logbook and the scene.
- **`slice-plain-rows`** (Diplomat, standing): every engine-slice row names what a player sees before a record name.

## Lessons pending (ledger, for `faces.yaml` at the next review)

- Regent and Architect, from `pos-slice-rules`: *"We need to explain this to the degree is makes sense to me before we
  move forward. This sounds like mumbo jumbo"*. Lesson: a position is written as what the player would see; record
  names come after, as a gloss.
- Architect, Challenger, Regent, Diplomat, from `pos-slice-encounter`: *"It feels like there is a gap we’re skipping
  over to keep it coherent with work we’ve already done"*. Lesson: "the engines do different jobs" was a way to avoid
  the bridge; line the existing engines up side by side before calling them separate.
- Diplomat and Architect, from `pos-slice-passage`: *"These are the main things we need feasibility testing on"*.
  Lesson: when the layers are untested, the passage seam is a feasibility test, not a later content task.
