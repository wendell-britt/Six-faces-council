# The Cave of Lessons: a 3-2-1 the player feels in the scene

**Run 2026-10-10**, started by the project coordinator from Wendell's note in the cave thread (10 October, 23:14 UTC). This
is the fourth council pass on the cave; the third is `6FACE_PASS_3d-build3_2026-10-09.md`. The build is
johnair01/bars-engine PR #265. The brief is HANDOFF.md, "Open on 2026-10-10, a real 3-2-1 inside the Cave of Lessons"
(commit 7444e21).

**The ask, in his words.** "So we need to actually have an in game interface of the 321. At the very least pulling in
the version from bars engine with the chat interface OR we design an encounter that simulates the felt sense of doing a
321 in the game". The floor he named, the chat port of `Clean321Flow.tsx`, is being built now in the "Cave 3-2-1 chat
port" thread. This pass weighs the other path and puts the choice on the board.

**Inputs:** the cave's DESIGN.md, section "No skip at a daemon, and the 3-2-1 (board of 10 October, 02:01)", and
`cave.js` lines 1197 to 1222 (today's three boxes); bars-engine `src/components/clean321/Clean321Flow.tsx` (the
canonical chat: Face it, Talk to it with a voice switcher, Be it, a charge reading before and after);
`.specify/specs/clean-up-technique-system/321-shadow-process.json`; the Big Mind cave rows (`bm-*`) and Wendell's
overrule of `bm-phone-first`; `st-which-three` and its steer; `enc-inner-moves`. The board was pulled first (ledger
`2026-10-10-pull-231712.json`). `council/due.py` was not run; this is a pass, not a board read.

**Casts** (`python3 council/iching/cast.py --json`, three coins; the record is in the ledger):

| Agent | Hexagram | Shows |
|---|---|---|
| Shaman | 11 Mingling | This is working, and you should know why. |
| Architect | 35 Sunrise, changing to 38 Estrangement | This is becoming visible faster than you planned. |
| Challenger | 58 Banter, changing to 38 Estrangement | The exchange is already the whole of it. |
| Regent | 34 Vigour, changing to 19 Spring | Force is available here and unaimed. |
| Diplomat | 4 Fog, changing to 38 Estrangement | You are guessing where you could ask. |
| Sage | 47 Drained | The explaining continues and the basin is dry. |
| Emotional Body daemon (for the Shaman) | 7 Muster, changing to 32 Endurance | What would organise this is a fact you have not said. |
| Skeptic daemon (for the Challenger) | 40 Thaw, changing to 35 Sunrise | The knot just loosened, and the window is short. |

**Daemons:** two, on the middle model, both reports passed `check_report.py --research` and are saved as
`council/daemons/reports/2026-10-10-3d-build-321-*`. 44,069 subagent tokens. The faces could not spot-check the links:
the proxy refused nature.com. Every figure taken from a daemon is marked as the daemon's.

## Scorecard (tests set by pass 3)

- **By 2026-10-16, the avatar walks and breathes on his phone, and the breath never holds a step.** Passes in the
  browser test (53 checks at 390 by 844, commit 1237515); his phone play is still open.
- **By 2026-10-16, a block opens a side passage and returns to the exact step, two deep.** Passes in the browser test.
- **The five-person labyrinth test.** Retired: Wendell overruled `cave-labyrinth-test` ("I don't really understand the
  purpose of this"). This pass sets no test that needs other players.

## Anchor

The Cave of Lessons is the ontology game played inside the body. Since 10 October a daemon in the way has no skip: "If
a daemon pops up then it needs to be worked with. We can pivot to a 321 discussion with the part until it feels
satisfied." Unchanged. This pass asks what that discussion looks like in the scene.

## What the record already answers

**The player writes every line.** `Clean321Flow` keeps one thread the player writes, the daemon's answers included; its
composer for the block's voice says "Answer as the block…". The cave adds no model (bars-engine CLAUDE.md, dual-track:
the non-AI version is first-class). So a figure in the scene can move, but it never speaks words the system wrote.

**A felt 3-2-1 has drifted once already.** bars-engine's `321-shadow-process.json` is called "a structured felt-sense
discharge", and its Three, Two and One are breath counts: "The first breath: you feel the weight", "imagine the weight
leaving", "what arrives in the space it leaves?". It never says it, you or I. The shift from it to you to I is what
makes it the 3-2-1, and that file shows how easily a felt version loses it.

**Both caves are one project.** Wendell on `st-which-three`: "cave of lessons and big mind cave are both part of the
same project- they are just forked". The Big Mind cave is "a fork of cave of lessons that adds chambers between cave
hallways with a voice blocking the path" (his overrule of `bm-phone-first`). A daemon met in its own place, worked by
voice, is that chamber. Whatever the 3-2-1 becomes here, the fork reuses it.

**Two daemon questions are answered by the record.** The Emotional Body asked whether the breath follows the player:
the cave breathes on its own clock, and the hold ring hands it to the player when they choose (DESIGN.md,
`cave-breath-in-the-cave`). It asked how the daemon speaks: in text, in the pane (`cave.js` line 1203).

## Shaman

**Mingling:** "This is working, and you should know why." Heaven sends its force up and earth comes down to receive it,
and the exchange runs both ways. That is the 3-2-1: the daemon and the player trading places. The tradition warns at once
that flat ground turns to slope, and the slope here is the step into "I".

**The Shaman wants each pronoun to be a place.** From the Emotional Body daemon: "It" stands far, with the camera back
and the daemon dim. "You" stands two steps from it at eye level. "I" moves the camera behind the daemon's eyes. Its
source is Gendlin's first step of focusing, "DO NOT GO INSIDE IT", "Let there be a little space between you and that"
(the daemon's quote, not spot-checked). Distance is the felt part the three boxes leave out.

**The Shaman makes "I" a round trip.** The daemon cites a body-swap study in which alternating between one's own body
and the other's mattered (its quote: "the process of alternating between their own and the Freud body is important").
So the player steps into the daemon's place, speaks as it, and steps back to their own place to hear it. The step back
is also the way out if the "I" floods.

**The Shaman's standing test passes:** the daemon is someone the player has met, not a fault in them.

## Architect

**Sunrise, changing to Estrangement:** "This is becoming visible faster than you planned." The chat port is landing
tonight, and the encounter is already half built in it. The changing line warns about a conclusion reached from a
distance, so the Architect reads the binary from close up.

**The Architect finds the third position.** His "OR" is two halves of one build. The chat holds the words; the scene
holds the distance. Run the ported chat in the pane, as it is being built, and let the scene move on the chat's own
steps: Face it puts the camera back behind the avatar with the daemon far off; Talk to it brings the avatar face to face,
and the voice switcher swings the camera from over the player's shoulder to over the daemon's; Be it walks the avatar
into the daemon's place and turns the camera to look back down the passage the player came in by. Nothing new is
written, and the chat port stays the single source of the words.

**The Architect keeps it in the cave's own pieces.** The camera already follows the avatar (`cave-avatar-self`), the
daemon already has a figure and a place on the wall (`c3d-daemon-body`, `moveDaemon`), and the breath already runs. The
staging is camera targets and an avatar path tied to three chat steps. The Big Mind fork takes it as its chamber.

## Challenger

**Banter, changing to Estrangement:** "The exchange is already the whole of it." The practice is the words passing
between the player and the daemon. Anything the scene adds that the player does not write is a show.

**The Challenger names the failure: the cutscene.** From the Skeptic daemon: if the figure answers on its own, the player
watches instead of practising, someone has to write the daemon's lines, and that someone is the system. The daemon
cites Slater's 2019 study, in which talking to oneself by swapping bodies beat a scripted counsellor (86% against 48%
reporting change after a week, its figures, with the authors' own caution that "most of the effects we found were not
overwhelmingly supported in terms of probability"). The Challenger keeps the direction and none of the precision.

**The Challenger holds the wordless version suspect.** A felt encounter with no writing is the drift
`321-shadow-process.json` already shows: breaths in place of voices. It may still be worth playing, but it is not the
3-2-1 unless the player speaks as the daemon.

**The Challenger names the blocker a test resolves:** whether the staging earns its build over the chat alone. After the
staged version is built, Wendell works one daemon each way on his phone. The page keeps four numbers for him, on his
device only: the charge before and after, seconds, and how many "Be it" lines open with "I". The staging stays if the
charge drops at least as far and he writes no less. This is his own play, which he does anyway, not a panel.

## Regent

**Vigour, changing to Spring:** "Force is available here and unaimed." The cave has a working chat landing tonight and
two more ideas pulling at it. The becoming gives the window an edge: aim the force at one build at a time.

**The Regent sets the order.** The chat port ships first, untouched by this pass; it is the floor he named. The scene
work waits for his answer on the board. Whichever he picks, the Big Mind fork reuses it, so it is not a second build.

**The Regent holds three non-negotiables from the record.** No skip at a daemon (`cave-daemon-wall`, overruled 10
October 02:01). A way back to "it" at every step is a pause, not a skip: the daemon still stands, and the round is not
done. The written words stay on the page and leave nothing on a server (DESIGN.md, choice; the chat port's brief).

## Diplomat

**Fog, changing to Estrangement:** "You are guessing where you could ask." Two kinds of guessing. The council would be
guessing to pick between the chat and the encounter for him, so it asks, on the board. A player who has to guess
where to stand, or how to get out of the daemon's place, is in fog while the feeling is live.

**The Diplomat makes every move obvious and reversible.** Each step names where the player is standing in one line
("You are looking at it from across the chamber", "You are face to face", "You are standing where it stood"). A "Step
back" button returns to the far place at any step and keeps the words. The calm switch stays on screen through the 3-2-1.

**The Diplomat protects the player at the deepest door.** For the Damaged Self, the Big Mind cave already asks first
(`bmc-safety`: continue, rest, go back up). The same check-in comes before "Be it" when the daemon in the way is the
Damaged Self.

## Sage

**Drained:** "The explaining continues and the basin is dry." Words spoken now land badly; the reading counsels
persistence held privately. The chat is enough to be worked with tonight, and more argument does not fill the basin.

**The Sage names each face's part.** The Shaman made each pronoun a place and the "I" a round trip. The Architect found
the third position: the chat runs in the pane and the scene stages its steps. The Challenger named the cutscene and the
drift to breaths, and set a test on his own play that resolves whether the staging earns its build. The Regent put the
chat first and kept no-skip and the words local. The Diplomat named where the player stands and gave the way back and
the check-in. The Sage dropped the Emotional Body's hand-on-body charge reading, because the chat's own slider already
does that job and a second one splits it.

**The dissent is real.** The Shaman leans to the scene doing more than the chat, closer to a wordless walk, because
writing invites the meaning before the feeling (the Emotional Body: "the meaning arrives before the feeling does").
The Challenger leans to the chat alone until the staging shows it adds something. The Architect and Diplomat take the
staged chat. Which the cave is, chat, staged chat, or a felt walk without writing, is his. The pass was not unanimous.
The Sage does not decide.

## Verdicts

| Face | Form | Who writes | The "I" step | Order |
|---|---|---|---|---|
| Shaman | Staged, leaning wordless | The player | A round trip into its place and back | After the chat |
| Architect | Staged chat | The player, in the chat | Camera looks back from its place | After the chat |
| Challenger | Chat until the test shows more | The player, every line | Must be said as "I" | Chat first |
| Regent | His call | The player | No skip; a pause is allowed | Chat first |
| Diplomat | Staged chat | The player | Check-in before it for the Damaged Self | After the chat |
| Sage | Synthesis | Synthesis | Synthesis | Synthesis |

## Outputs

### Positions (stand unless he flips them)

- `cave-321-player-writes`: in any form, the player writes every line of the 3-2-1, the daemon's answers included. The
  daemon's figure may move but never speaks words the cave wrote. Why: `Clean321Flow`'s thread ("Answer as the
  block…"), the non-AI first rule in bars-engine's CLAUDE.md, and the Skeptic's finding that a scripted answer is the
  weaker arm.
- `cave-321-pronoun-places`: if the scene stages the 3-2-1, each pronoun is a place. Face it from across the chamber;
  Talk to it face to face, with the camera swinging shoulders as the voice switches; Be it from where the daemon
  stood, looking back, then a step back to one's own place. A "Step back" to the far place is always there and is a
  pause, not a skip. Why: the Emotional Body's report (Gendlin's "a little space"), and `cave-daemon-wall`.
- `cave-321-not-breath-count`: the cave does not use bars-engine's `321-shadow-process.json`. Its Three, Two and One
  are breath counts and never say it, you or I. Why: the shift of voice is the practice; that file is a felt-sense
  breath practice under the 3-2-1's name.
- `cave-321-damaged-self-ask`: before "Be it" with the Damaged Self, the cave asks first: continue, rest, or go back up.
  Why: `bmc-safety`, already standing for the fork.
- `cave-321-one-build`: the 3-2-1 chamber is built once and shared with the Big Mind cave. Why: his steer on
  `st-which-three` and his overrule of `bm-phone-first` ("chambers between cave hallways with a voice blocking the
  path").

### Questions (passed the reach test)

- `cave-321-form` (Architect, Shaman, Challenger): what should working a daemon feel like in the cave? A, the chat only,
  as being built now. B, the chat inside a staged scene: the same thread he writes, while the camera and figure move from
  across the chamber, to face to face, to standing in its place (recommended). C, a felt walk without writing: the
  player moves from it to you to I with the breath and the figure, and the chat is offered after for words. Why only he
  can answer: his own note gives both halves joined by "OR", the faces split three ways, and the record holds no ruling
  on how much the cave should carry without words. It decides what gets built after the chat port. Why not before: until
  23:14 on 10 October the 3-2-1 was three boxes, and nobody had asked for it to be felt in the scene.

### Tests, dated

- By 2026-10-17, if B or C is chosen: Wendell works one daemon in the chat and one in the staged version on his phone.
  The page keeps, on his device only, the charge before and after, seconds, and how many "Be it" lines begin with "I".
  The staging stays if the charge drops at least as far and he writes no less. It resolves whether the staging earns its
  build over the chat.
- After the chat port merges: its browser test still passes with the staged camera added, at 390 by 844.

## Sources (from the daemons; not spot-checked, the proxy refused them)

- Emotional Body: [Focusing, six steps](https://focusing.org/sixsteps);
  [Slater et al. 2019, Scientific Reports](https://www.nature.com/articles/s41598-019-46877-3);
  [Proteus effect, Stanford VHIL](https://vhil.stanford.edu/publications/avatars-and-agents/proteus-effect-self-transformations-virtual-reality);
  [two-chair work, Frontiers in Psychology 2025](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1692630/full)
  (the daemon read only the search result).
- Skeptic: [Slater et al. 2019](https://www.nature.com/articles/s41598-019-46877-3);
  [University of Barcelona, Freud avatar](https://www.ub.edu/web/ub/en/menu_eines/noticies/2015/10/015.html);
  [Game Informer, Hellblade's psychosis expert](https://www.gameinformer.com/b/features/archive/2017/04/17/three-big-takeaways-from-hellblade-s-psychosis-expert.aspx).
