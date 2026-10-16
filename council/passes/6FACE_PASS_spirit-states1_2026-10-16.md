# Six-face pass: spirit states 1 (satisfied, neutral, dissatisfied)

2026-10-16. Called by the coordinator on Wendell's message that opened the thread "Spirit satisfaction states", 17:55 UTC:

> "For the Sprits and Allies that we're working on for WAVE and Sprout game we need to also introduce the Satisfied,
> Dissatisfied, and Neutral versions of it in whatever intake it's coming in as. The creatures should be darker and more
> feral in dissatisfaction. We'll need to think through design markers that show the state. Downwind there will need to
> be moves that allow a player to shift a spriti from satisfied to dissatisfied OR in allied or creature state able to
> take on moves from other elements. This isn't fully thought out, but was something in my brain that I wanted to see
> how the 6 game masters and design ontology would handle."

First pass on the subject. It is exploratory: it produces positions and one question, not art or code.

Ontology loaded (docs/ontology-in-flows.md, a pass on a mechanic): `ontology/v0.1/QUICKSTART.md`, with the `game_design`
profile read where the question touches it (the model's State, SatisfactionReport and TensionConfiguration, its evidence
table and rule 26). Every face got the same context. No face subagents and no daemons were sent: the record answered
each problem a daemon would have worked, so the pass's subagent token count is zero.

Casts (`cast.py`, three coins): Shaman 37 Household, becoming 63 Arrived; Architect 44 Serendipity, becoming 1 Unbroken;
Challenger 39 Impasse, becoming 13 Fellowship; Regent 57 Persuasion, becoming 59 Dispersal; Diplomat 15 Understatement,
becoming 37 Household; Sage 40 Thaw, unchanging. The ledger record `2026-10-16-spirit-states1.json` carries them.

## Scorecard

No earlier pass on spirit states. The tests this subject inherits: the spirit generator's check (`tools/check-spirit-gen.mjs`
on sprout #51: careful beats the masher, every fight won standing in 3 to 5 turns) and the art rule that a spirit reads at
the 96 px sprite (round 2, `sg-holo-stages`). Both still have to pass once states exist.

## Anchor

A spirit is a charge the player brought, and its look tells the player how that charge is doing: unsettled, steady or
settled. The player can move it, and a settled spirit can reach further.

## What the record already holds

- **A number.** Allies already carry satisfaction 1 to 10, doing Monster Rancher's loyalty job (`spirit-growth-by-training`).
  Spars that listen raise it and Fight alone lowers it (`sg-loop-trains`); an offered shard raises it (`sg-loot-offering`);
  an overcharged spirit joins at 1 and heeds only every other turn until 5 (`sg-overcharge`).
- **Three moods.** design.md gives every spirit three moods, named on the board as charged, steadied and allied
  (`demo-spirit-count`, `demo-daemon-count`). A daemon can be steadied by feeding it the generating stance or subdued by the
  controlling one (`enc-steady-rests`).
- **The canon's words.** Emotional Alchemy's channels run dissatisfied, neutral, satisfied
  (bars-engine `src/lib/quest-grammar/emotional-vector-resolver.ts`), and a charge cannot start satisfied (line 147). The
  fifteen moves are five Transcend (within a channel), five Generative and five Control (between channels), with energy +2,
  +1 and -1 (`move-engine.ts`).
- **Forms and families.** Gas, core, hologram, living creature, ally form (`sg-holo-stages`, rounds 1 to 11); the urge picks
  the family, one per daemon (`sg-body-from` A); living creatures stand on four feet (`sg-romp-four-feet`); each daemon holds
  one of the six movements (`council/daemons/GESTURES.md`, `dg-six-movements`).
- **Shadow and dissolving.** Polarity veils (above 0) or floods (below 0) a spirit (`ps-polarity`, bars-engine #326); a shadow
  spirit takes its element when fully revealed and only then can be dissolved (`sd-shadow-skip` steer, #327).
- **Moves across elements.** His steer on `sf-ally-moves`: "move sets should operate like pokemon where a spirit can learn
  moves from other channels but always has a signature move".

## Shaman

*The cast is hexagram 37, Household, becoming 63, Arrived.* "An arrangement has formed here without being discussed." The arrangement
is that a spirit's look has become, unannounced, a mirror of the player's charge. The changing line warns that a finished design
starts to decline, so the Shaman names the trouble before it comes.

**The feral spirit is a protector held past its time.** Wendell's premise is that daemons emerge to protect the vulnerable
child and later need renegotiating. A spirit's family is its daemon, so a dissatisfied spirit is that daemon's movement
stuck in its guard. The Shellback is the Protector's family, and its feral stance is the push braced and not landing. This
gives "darker and more feral" a meaning beyond a filter (position `ss-feral-stance`).

**The risk is a mirror that diagnoses.** If a player's own charge comes out snarling, the screen can say "your feeling is a
monster". Standing test: does the look say something is wrong with them, or something about what they have learned? The
copy names the spirit unsettled and says what it protects; it never says bad, corrupt or broken (`ss-feral-trade`).

**Only the player says they are satisfied.** In the cave, a spirit leaves satisfied only when the player names a gold state.
The charge number coming down is not enough, because a number moving is not the player's report (`ss-intake-start`).

## Architect

*The cast is hexagram 44, Serendipity, becoming 1, Unbroken.* "You are building on one piece of evidence." The temptation is to build a
new axis from one message. The record already holds a number, three moods and the canon's three words, so the Architect
builds on those and adds nothing that duplicates them.

**One number, three bands.** The three states are bands of the existing satisfaction 1 to 10, and the edge between
dissatisfied and neutral sits at 5, where `sg-overcharge` already changes behaviour (`ss-three-states`). The old moods map
onto them: charged, steadied, allied become dissatisfied, neutral, satisfied, and "allied" stays the bond's word. Is the
binary false? Yes: "mood or form" was never a choice, since each of the five forms can wear each of the three states.

**Two satisfactions share one word, and they stay apart.** The charge's emotional altitude (the TensionConfiguration, a
dissatisfied record) and the spirit's satisfaction (a relationship number) are different objects. The ontology forbids
folding satisfaction back into the configuration (model, rule 26), so the spirit's state never rewrites the charge's record.

**State owns a layer.** `sg-look-layers` gives each input one visual layer, so satisfaction gets its own and repaints none.
Built as a rig pose and material settings on the same model, three states cost no new models (`ss-markers`).

**The canon already draws the move map.** The five Generative and five Control moves join every pair of elements exactly
once. So the generating cycle reaches two elements and the controlling cycle the other two, and state can gate the reach
without anything invented: own element when dissatisfied, generating cycle at neutral, controlling cycle at satisfied
(`ss-cross-element`).

**Darker collides with veiled.** `ps-polarity` already gives a veiled spirit a dark aura. Dissatisfied darkness must be dense
and solid, veiled faint and fogged, flooding bright and too big, and a veiled spirit's state does not show (`ss-not-veiled`).

## Challenger

*The cast is hexagram 39, Impasse, becoming 13, Fellowship.* "The direct route is closed and you have asked nobody." The direct route,
taking his sentence about shifting "from satisfied to dissatisfied" as written, runs into a wall: the record cannot tell
whether he meant a move built to push a spirit down. Ask him, and only that.

**If feral is only worse, the state becomes a scoreboard.** Players will flee it and read every dark spirit as a grade on
themselves. So dissatisfied needs a real trade: its signature hits harder while it heeds less and reaches no other element
(`ss-feral-trade`). Monster Rancher's disobedient monster is still strong; that is the model.

**Anti-pattern: five forms times three states as fifteen models.** The cost would bury the art loop, which already runs one
family a round. Pose plus material settings on one rig is the only version the schedule holds.

**The art has to wait.** The spirit art strand is waiting on Wendell's look at version 14 (round 11, two rounds past his last
look), so a state art round cannot start under the loop contract until he looks. The design can land now; the art waits.

**Falsification tests** (each names the blocker it resolves):
1. *State squint test* (resolves: do the markers read?; unlocks building states into every family). One Shellback tortoise
   in one element, five forms by three states, fifteen 96 px sprites shuffled with the labels off. If Wendell or a player
   cannot sort at least 13 of 15, the markers fail and the next round strengthens the stance before anything else.
2. *Veil test* (resolves: does dissatisfied collide with perceptual shadow?; unlocks `ss-not-veiled`). A dissatisfied spirit
   beside one veiled at polarity 6 and one flooding at -6. Any pair confused, and the darkness rule changes.
3. *Feral trade test* (resolves: is dissatisfied a choice or only a penalty?; unlocks the numbers in `ss-feral-trade`). In
   `check-spirit-gen.mjs`, a feral-keeping policy beside the careful one: it should lose more fights than the careful policy
   but win some the masher loses. If it never wins one, the trade is a penalty.

## Regent

*The cast is hexagram 57, Persuasion, becoming 59, Dispersal.* "An effect is already happening that you have not admitted to." The
effect is that satisfaction has been changing a spirit's behaviour since `sg-overcharge` without ever changing its look.
The changing line says the rigid part, a single unchanging render per form, is what is coming apart.

**Obligations.** Living creatures stay on four feet and in a pose the family's rig can walk out of (`sg-romp-four-feet`,
bars-engine #325). No play-time AI art; the sprite stays rendered from the 3D model (`sg-assets-modular`). The signature move
is always kept (his `sf-ally-moves` steer). The charge's record is never rewritten (ontology). A veiled spirit cannot be
dissolved and does not show its state (`sd-shadow-skip` steer).

**The gate puts positions first.** Positions land now. The art is a round of the spirit loop (`council/loops/spirit-generator.json`) after his
look at version 14. The moves are a sprout build after the signature-move build the callsheet already queues, because
`ss-cross-element` sits on top of it. None of this goes ahead of the Chapter 1 demo's own work.

**The first build is done when** the squint test passes, `check-spirit-gen.mjs` still has careful beating the
masher and every fight won standing in 3 to 5 turns; a state change always shows its one line.

## Diplomat

*The cast is hexagram 15, Understatement, becoming 37, Household.* "What you are underplaying had better be there." The soft marker,
a gentle eye or a steadier glow, is fine only if the louder ones (stance, aura edge) are really carrying the state.

**No state rests on colour alone.** Each state shows on at least two markers that are not colour, so a colour-blind player and a 96 px
sprite both read it (`ss-markers`). Meridia's sun crest is already gold, so "gold means satisfied" would collide on every
Meridian spirit; the satisfied rim is brightness and smoothness, not a hue.

**Tell the player once, in plain words.** The first time any spirit crosses a band, one line says what moved it. After
that the look carries it. The words "dissatisfied", "neutral" and "satisfied" are the canon's and stay in the data; what the
player reads (unsettled, steady, settled) is the council's placeholder and his to set.

**The feral spirit stays welcome.** A player may keep one feral on purpose, and the game never nudges them out of it
(`ss-feral-trade`).

## Verdicts

| Face | Three states from the existing number? | Markers as a layer, two non-colour each? | Shift up through existing moves? | State gates cross-element reach? | Down-shift as a move? |
|---|---|---|---|---|---|
| Shaman | Yes, and the cave reads the player's report | Yes; stance carries the meaning | Yes | Yes | Lean B: no move riles a charge |
| Architect | Yes | Yes | Yes | Yes, by the canon's two cycles | Indifferent; A is buildable |
| Challenger | Yes | Yes, only as pose and material | Yes | Yes | Ask him (question) |
| Regent | Yes | Yes | Yes | Yes, after the signature build | A, wild and rival only |
| Diplomat | Yes | Yes, never colour alone | Yes | Yes | A or B; never C |

## Dissent check

Not unanimous. The pass splits on the downward shift: the Shaman leans against any move made to rile a spirit, the Regent
and Diplomat accept one on wild and rival spirits only, the Architect is indifferent, and the Challenger holds that only
Wendell can say what his sentence meant. That split is the board question `ss-push-down`. The five agree on the rest, which
is itself a warning: the agreement rests on the record already holding a number, the moods and the canon's moves, so if any of
those three is wrong (if, say, design.md's moods meant something other than these states), most of this pass falls with it.

## Sage

*The cast is hexagram 40, Thaw, unchanging.* "The knot just loosened, and the window is short." The knot was that satisfaction had a
number and a behaviour but no face; the pass gives it one while the spirit look strand is still building families.

The smallest coherent whole: **one number, read three ways, shown on its own layer, moved by moves the canon already has,
and opening the canon's two cycles as it rises.** From the Architect it keeps the single number and the cycle map, and the
split between the charge's record and the spirit's state. From the Shaman, the feral stance as a protector's held movement
and the rule that only the player's report makes a cave spirit satisfied. From the Challenger, the feral trade, the
pose-not-model cost rule and three tests. From the Regent, the gates and the four-feet and rig obligations. From the
Diplomat, the rule that no state rests on colour alone, and the one-line notice. It drops nothing whole; it drops the Architect's offer to rename the
moods outright, because renaming a design.md term is a ruling, so the pass maps them instead.

Dissent carried: the downward move (`ss-push-down`). Not decided here.

Recommended next move: when Wendell looks at the spirit page's version 14, the next round of the spirit loop builds the
state sheet for the Shellback tortoise in one element (five forms by three states, plus the veil test pair) and runs the
squint test, because the markers are the only part of this pass that could fail before any code exists. The moves wait for
the signature-move build already queued on sprout #51.

## Outputs

**Positions** (each stands unless he flips it; rows in `council/callsheets/rows/spirit-states-2026-10-16.json`):
`ss-three-states`, `ss-intake-start`, `ss-markers`, `ss-feral-stance`, `ss-not-veiled`, `ss-shift-up`, `ss-cross-element`,
`ss-feral-trade`. Each cites the record it rests on in its `why`.

**Questions** (passed the reach test):
- `ss-push-down`, owner Challenger. Options A (wild and rival spirits only, recommended), B (no move, play only), C (any
  spirit). Only he can answer because his sentence asks for exactly this shift and the record holds nothing on whether he
  meant a move. Not asked before because the states did not exist before this message.

**Reach test, questions that did not survive:**
- *Which intake did he mean?* Answered from the record: every intake the record has (generator, wild spirits, the cave), each
  starting from what it already records (`ss-intake-start`).
- *Are the old moods the same as these states?* Answered by mapping, citing `demo-spirit-count` and `demo-daemon-count`; he can flip it.
- *Which elements can a spirit learn from?* Answered by his `sf-ally-moves` steer and the canon's cycles (`ss-cross-element`).
- *What do the states look like?* Answered by his "darker and more feral" plus the family's held movement; the squint test
  checks it, and his look at the sheet steers it.

**Tests**, dated: the state squint test and the veil test with the state art round (after his look at version 14); the
feral trade test with the moves build on sprout. Next pass on the subject grades all three.
