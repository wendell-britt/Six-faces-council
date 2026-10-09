# The Cave of Lessons: an avatar, a labyrinth, the breath, and branches from blocks

**Run 2026-10-09**, from Wendell's day-3 playtest notes (project thread, 19:40 UTC), started by the project
coordinator. This is the third pass on the 3D cave; the first two are `6FACE_PASS_unreal-pipeline1_2026-10-08.md` and
`6FACE_PASS_3d-build2_2026-10-09.md`. The build is johnair01/bars-engine PR #265; its
`content/ontology-game/cave/DESIGN.md` (commit ebe6d5b) lists these four notes as not yet built.

**The ask, in his words.** "I want to explore how we can integrate the wave breathing more. Right now we're in 1st
person and I think I want to have a player avatar." "Also the cave going straight doesn't vibe with me right now. I
think a labrynthine expereince will make things feel more immersive." "we also need to introduce the branching paths
that emerge from blockages in the wave patterns". The rest of his notes (no face at the doorway, one answer per page,
an object for each element) were built the same night in ebe6d5b and are not part of this pass.

**Inputs:** the cave's DESIGN.md; the ontology game's passes 1 and 3 (`content/ontology-game/6FACE_PASS1_2026-10-06.md`,
`6FACE_PASS3_2026-10-07.md`), which hold his workflow sketch of 7 October and the W.A.V.E. as a breathed ladder whose
steps can be blocked; `game.jsx` (the W.A.V.E. practice text, line 806, and the block stack, line 1733); the WAVE
teaching pass (project files `demo/wave-teaching-pass.md`); the board's earlier labyrinth ruling `pr-labyrinth-scale`.
`council/due.py --ahead 7` was not run; this is a pass, not a board read.

**Casts** (`python3 council/iching/cast.py`, three coins):

| Agent | Hexagram | Shows |
|---|---|---|
| Shaman | 29 Depths, changing to 20 Witnessing | The bottom of this has another bottom under it. |
| Architect | 15 Understatement | What you are underplaying had better be there. |
| Challenger | 6 Divergence, changing to 14 Noon | You are going deeper and pushing forward at once, and the two cancel. |
| Regent | 5 Hosting, changing to 9 Restraint | You are ready and the ground is not. |
| Diplomat | 54 Home Field Advantage, changing to 34 Vigour | You are following rules nobody told you. |
| Sage | 31 Mutuality, changing to 49 Molting | The movement here arrived because you stopped. |
| Player daemon (for the Shaman) | 59 Dispersal, changing to 47 Drained | What you were holding rigid is coming apart. |
| Skeptic daemon (for the Challenger) | 12 Stalemate, changing to 33 Retreat | You are seeking one game and wearing the face of the other. |
| Emotional Body daemon (for the Diplomat) | 47 Drained, changing to 38 Estrangement | The explaining continues and the basin is dry. |

**Daemons:** three, on the middle model, each report passed `check_report.py` (two with `--research`). About 77,600
subagent tokens. The faces could not spot-check the research links from this container: the proxy refused Wikipedia and
PubMed. Every figure taken from a daemon is marked as the daemon's.

## Scorecard (tests set by pass 2)

- **By the end of day 2, chamber one loads under 3 MB and walks on his phone.** Passes in part. The kit is 17 KB and the
  browser test walks it at 390 by 844 (22 checks on day 3, 27 after ebe6d5b). Frame rate on his own phone is not
  measured yet; day 5 owns it.
- **By the end of the week, he has walked three chambers and passed one daemon, with the cost recorded.** Open; the
  week ends 2026-10-15.

## Anchor

The Cave of Lessons is the ontology game played inside the body: the player goes in where the charge is and works it
as a walk, and leaves with the scan saved. Unchanged. This pass asks what the walk is made of.

## What the record already answers

**His sketch already joins the W.A.V.E. to the block work.** Pass 3 read it off his photograph: "Initial resistance
goes into WAVE. WAVE has two ways out. 'Awareness of resistance to a move' leads down to '(WAVE) Resistance', which has
three numbered steps [...] After the steps comes Release, and from Release a line marked 'Return to original block'
goes back into WAVE. A WAVE that completes goes to 'Exhale to finish'." The cave built the block steps (sensation,
element, daemon, gate, release) as the main walk and left the W.A.V.E. out. "Branching paths that emerge from
blockages in the wave patterns" is the sketch's own shape drawn as a map: the W.A.V.E. is the path, a blocked step is
the branch, and Release is the way back.

**The game already has the way back.** `game.jsx` keeps a block stack ("A stack because a block can come up inside
block work", line 1733), and the browser test checks the trail two blocks deep (pass 3 scorecard). The map keeps the
detour (line 2032). A branch in the cave is that stack drawn as a passage.

**The breath is an offer, never a lock.** Pass 1, the Shaman: "each step lasts one guided breath. The continue button
appears when the exhale ends. That is an offer of pace, never a lock, because an offer is not a requirement (lesson,
9 September)." A block is never assumed: "We shouldn't assume a block, but if there IS a block we should assume
self-sabotage, with the given choice to skip" (Wendell, 9 September, quoted in pass 1).

## Shaman

**Depths, changing to Witnessing:** "The bottom of this has another bottom under it." A block inside a block is pit
past pit, and the counsel is water: the same move in every hollow. The becoming is the tower, the place you watch from
that is itself in view, which is what a player avatar is: the player sees themselves inside their own body.

**The Shaman wants the avatar to be the player, not a hero.** The Player daemon asked for "a small someone to walk with
me, who is me and not a hero." **The Shaman recommends** a small faceless figure in the daemons' own body language
(fused rounded shapes, `c3d-daemon-body`), wearing the charge the player named at the doorway: narrow and drawn in for
tightness, fogged for numbness, bright for strength. As the W.A.V.E. climbs, the figure loosens. The camera follows
close behind and a little above. The Shaman keeps the Player daemon's "let the avatar breathe back": its chest and the
nearest wall swell together.

**The Shaman's standing test passes:** nothing in the avatar says something is wrong with the player. A block shows on
the wall, not on the figure.

## Architect

**Understatement:** "What you are underplaying had better be there." The height is under the floor already: the block
stack, the five places and the kit exist. **The Architect proposes the structure.** The W.A.V.E. is the spine: one
winding stretch per step, Welcome, then Acknowledge, Allow, Accept, Appreciate, then Validate, then Exhale at the way
out. Each stretch is one breath long at a walk. On any stretch the player can say the step will not go further; the
wall there opens a side passage, and that passage is the five-place chamber as built (sensation, element, daemon, gate,
release). Release walks back to the exact footprint on the spine. A block inside the side passage opens a passage off
it, and the stack carries the way back through both.

**The Architect keeps the build in one script.** `build_kit.py` gains a few path pieces (a bend, a switchback, a side
door), and the page lays the spine from a short table of stretches, one per W.A.V.E. step. The layout is a seeded
pattern, so one scan always gives the same cave. The asset budget barely moves; the avatar is generated geometry, which
the Player daemon put at under about 50 KB (its estimate).

## Challenger

**Divergence, changing to Noon:** "You are going deeper and pushing forward at once, and the two cancel." The two words
in his notes pull apart. A labyrinth, in the old sense, has one winding route and no wrong turns, and a maze has choices
and dead ends (the Skeptic's sources, below). Branching from blocks is maze-like; a winding walk is labyrinth-like.

**The Challenger names the fork.** It is not unicursal against maze in the abstract. It is whether the player ever
chooses a turn when nothing is blocked. If they do, the walk competes with the practice for attention, and a person
carrying a charge on a phone gets lost while the feeling is live. The Skeptic: "choice in the walk competes with the
choices in the practice." That is his preference, so it goes to the board (`cave-labyrinth-form`).

**The Challenger sets the failure test** (the Skeptic's thresholds, which are its choices): five people on phones walk
one chamber with no instruction. The labyrinth fails if anyone pauses more than 10 seconds to ask where to go, if the
winding adds more than about a fifth to the time before the first breath step, if the frame rate drops below 30 on a
mid-range phone, or if a player coming back from a branch cannot say which step they resumed.

## Regent

**Hosting, changing to Restraint:** "You are ready and the ground is not." The build is ready to wind; the ground under
it is two choices only he can make. **The Regent sets the gate:** day 4 keeps to what does not wait on him (the avatar
and the cave's breath), and the spine and the labyrinth wait for `cave-spine` and `cave-labyrinth-form`. The becoming
names the small rule holding everything: the breath never locks. **The Regent holds it as non-negotiable:** no step
waits for a correct breath, and no breath is scored.

**The Regent records two non-negotiables from the record.** A block is offered, never assumed, and every block offers a
skip (9 September). The map keeps every detour (`game.jsx` line 2032), so a blocked step stays marked on the saved
scan. That answers the Emotional Body's second question.

## Diplomat

**Home Field Advantage, changing to Vigour:** "You are following rules nobody told you." A player who has to guess that
the cave waits on their breath is following an unspoken rule. **The Diplomat sets the breath as the cave's, not the
player's chore.** From the Emotional Body daemon: the cave breathes on its own by default, walls easing and light
warming at about five and a half breaths a minute (its figure; it cites resonance breathing near six with personal rates
from 4.5 to 7). The avatar walks on the inhale and settles on the exhale. A hold-to-inhale ring is offered for a player
who wants to lead, and then the cave follows their rhythm. That answers the Player daemon's question from the record: the
breath is an offer (pass 1), so the clock runs on its own and the thumb is optional.

**The Diplomat protects the dysregulated player.** The Emotional Body daemon cites a review finding that "certain
breathing exercises can in fact intensify anxiety". So a calm switch is always on screen: the cave stills its sound and light, the ring
goes away, and tapping the floor grounds the player with eyes open. Haptics are off by default.

**The Diplomat marks a block as company.** A blocked step stays dim, a lantern waits there, and the daemon of the side
passage is met as a guest, as the daemon canon says (enlist, never fight).

## Sage

**Mutuality, changing to Molting:** "The movement here arrived because you stopped." That is the block: the branch opens
only where the player stops. The Shaman gave the avatar as the player seen from outside, and the breath that loosens
it. The Architect gave the spine and branch, read from his own sketch, and kept it in one script. The Challenger named
the real fork in the labyrinth and the test that shows it failed. The Regent held the breath unlocked and kept the
detour on the map. The Diplomat put the breath in the cave, not on the player, and the calm switch. The Sage dropped the
Player daemon's mapping of the four A's onto the five places, because the spine makes the places the branch.

**The dissent is real.** The Shaman would let the winding open into side caves that hold nothing required, for wonder; the
Challenger would keep every turn on the spine until the phone test passes. The Architect reads the sketch as settling
the spine; the Regent holds that moving the five places off the main walk changes what he played and liked ("Choosing
all 6 faces when you're in teh cave is very cool"), so it goes to him. The pass was not unanimous. The Sage does not
decide.

## Verdicts

| Face | Avatar | Breath | Block branch | Spine | Labyrinth form |
|---|---|---|---|---|---|
| Shaman | Faceless figure wearing the charge | Cave breathes, avatar breathes back | Yes | W.A.V.E. spine | Winding, with optional side caves |
| Architect | Yes, generated, about 50 KB | Yes | Yes, the stack as a passage | W.A.V.E. spine, from his sketch | Winding, seeded |
| Challenger | Yes | Yes, never scored | Yes, main path lit | Either, if tested | Winding only, no free turns |
| Regent | Yes | Never a lock | Yes, with a skip | His call | His call |
| Diplomat | Yes | Cave's by default, ring optional, calm switch | Yes, a lantern | W.A.V.E. spine, the gate kept | Winding |
| Sage | Synthesis | Synthesis | Synthesis | Synthesis | Synthesis |

## Outputs

### Positions (stand unless he flips them)

- `cave-avatar-self`: the player sees a small faceless figure, built like the daemons, wearing the charge they named,
  from close behind and a little above. Holding a thumb anywhere walks it toward the next glowing place; a drag looks
  around. It loosens as the W.A.V.E. climbs and breathes with the cave. Why: his "I want to have a player avatar", the
  daemons' body (`c3d-daemon-body`) and one-finger walk (`c3d-one-finger`).
- `cave-breath-in-the-cave`: the cave breathes on its own at an easy pace (its walls, its light, and the fire, tree, crystal, pool or boulder the player raised); the avatar
  walks on the inhale and settles on the exhale. A hold-to-inhale ring is offered, not required, and a calm switch is
  always on screen. No breath is scored and no step waits on one. Why: pass 1's "an offer of pace, never a lock".
- `cave-block-branch`: on any W.A.V.E. step the player can say it will not go further. The wall there opens a side
  passage with the block work; Release walks back to the exact footprint, a block inside it branches again, the main
  path stays lit, and a lantern marks the spot. Every block offers a skip. Why: his sketch, the block stack in
  `game.jsx`, and his ruling of 9 September.
- `cave-detour-kept`: a blocked step stays marked on the saved scan. Why: the map keeps the detour (`game.jsx` 2032).
- `cave-labyrinth-test`: the labyrinth is phone-tested with five people before he is asked to walk it, against the
  Challenger's thresholds above.

### Questions (passed the reach test)

- `cave-spine` (Architect, Regent): what is the main walk? A, the W.A.V.E. breathed as the winding path, with the five
  places as the branch a block opens (his sketch; recommended). B, the five places stay the walk, and a W.A.V.E. breath
  is taken at each, with blocks branching from any breath. C, the W.A.V.E. first, and the five places always follow
  at the end, so every walk meets the daemon and the six stones. Why only he can answer: the sketch says A, and his
  day-3 delight in the six stones says the gate matters on every walk; which of his two words wins is his. Why not
  before: the breath was not in the cave until his note of 19:40.
- `cave-labyrinth-form` (Challenger, Shaman): what kind of labyrinth? A, one winding path with no free turns, branching
  only at blocks (recommended). B, a winding path with side caves to wander that hold nothing required. C, a true maze
  with choices and dead ends. Why only he can answer: "labyrinthine" carries both meanings, and the feel he wants is his
  preference; it changes the path generator. Why not before: the cave was a straight passage until his note.

### Tests, dated

- By 2026-10-16: the avatar walks and breathes on his phone, and the breath never holds a step (browser test).
- By 2026-10-16: a block on one W.A.V.E. step opens a side passage and returns to the exact step, two deep, in the browser
  test.
- After the labyrinth is built: the five-person phone test above passes before he is asked to walk it.

## Sources (from the daemons; not spot-checked, the proxy refused them)

- Skeptic: [Labyrinth walking, Wikipedia](https://en.wikipedia.org/wiki/Labyrinth_walking);
  [Labyrinths, The Bus](https://thebus.substack.com/p/labyrinths);
  [Adaptive Visual Navigation Assistant in 3D RPGs, arXiv](https://arxiv.org/pdf/2508.18539);
  [Overgrown design process](https://go424.itch.io/overgrown/devlog/879873/overgrown-design-process).
- Emotional Body: [Steffen et al. 2017, resonance breathing](https://pubmed.ncbi.nlm.nih.gov/28890890/);
  [breathing guidance in game-based relaxation, 2021](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8695492/);
  [interoception and anxiety, Frontiers in Psychology 2024](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1412928/pdf).
- Player: [Flower, Wikipedia](https://en.wikipedia.org/wiki/Flower_(video_game)).
