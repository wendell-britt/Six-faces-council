# A Final Fantasy battle with emotional alchemy as its magic: a six-faces pass (fr-demo round 13)

The pass ran on 2026-10-07, called by Wendell in the thread "Master Yun's taught fight" at 14:49 UTC, after he played
sprout #27 (the taught fight, draft, stacked on #25) as demo v2. This is the council's thirteenth round on fr-demo.
Round 12 on the board holds `wave-move-names` and `wave-qi-made-visible`, and both stood at board read 0107, so this
pass is round 13. Nothing here is built. Sprout #27 stays a draft until this round is read.

## The ask, in his words

"Ok we're failing to understand my meaning.

So we want a battle screen in the style of final fantasy snes games where the player sprite is facing off against the spirit.
I'm struggle whether to have just a regular attack system with weapons and have the wuxing emotional alchemy be the magic system and have the player learn the moves from various characters. It's still a bit too much to understand for new people

And the user interface is a bit much.

We haven't used subagents with the council board and I think this would be a good use of them. Understanding the player and going through a full 6 game master analysis of how to make the game more like a final fantasy game and how to turn emotional alchemy into a magic system that grows over time

What stats to spirits have and how are they developed. My intuition says monster rancher can be used for inspiration"

The council reads four subjects in it: (a) the face-off screen and a lighter interface, (b) a weapon attack beside
emotional alchemy as magic, (c) a magic system that grows and is learned from characters, and (d) spirit stats and
their growth, with Monster Rancher as the model.

## Casts

Each face cast by the three-coin method (`council/iching/cast.py`, 2026-10-07).

- Shaman: 19 Spring, becoming 38 Estrangement.
- Architect: 44 Serendipity, becoming 1 Unbroken.
- Challenger: 33 Retreat, becoming 12 Stalemate.
- Regent: 8 Alliance, becoming 2 Bearing.
- Diplomat: 31 Mutuality, becoming 37 Household.
- Sage: 51 Shock, becoming 3 Sprouting.
- Daemons, each cast by its face: Player (Diplomat) 61 Incubation, becoming 27 Feeding; Emotional Body (Shaman) 47
  Drained, becoming 40 Thaw; Controller (Architect, research, on Sonnet) 48 The Well, becoming 57 Persuasion; Skeptic
  (Challenger) 62 Overstep, becoming 51 Shock.

## Scorecard

Round 11 set three tests.

1. **A cold phone player finishes the taught fight and says what Welcome does.** Not run. Wendell's own play is the
   first read, and he is the warmest player the game has. He found it "still a bit too much to understand for new
   people", so the council expects this test to fail on the current screen and does not spend a stranger on it.
2. **That player Welcomes unprompted in the first real charge.** Not run, for the same reason.
3. **The bot rerun with rung 1 only.** Passed. Full WAVE beat answer spam on HP left in 5 of 5 blocks (14.0 against
   10.0 to 11.9).

The bots passed again and the person did not. Round 11 named this gap and built a teacher for it, and the teacher
alone did not close it. The screen still asks a new player to read stances, gates and a hold bar at once.

## Anchor

A random charge on the strip is a daemon carrying a belief and wearing a feeling, and the battle is the player doing
WAVE to it. The player leaves knowing a move they can use on a real charge.

The anchor stands unchanged, because Wendell has not changed it. His steer bears on its middle clause. If the battle
gains a plain Fight command, the battle is no longer only WAVE: WAVE becomes the magic inside a Final Fantasy battle.
That rewording belongs to his answer on `battle-fight-and-magic`, below.

## What the record already holds

- **The spirit fight's Decided rules.** design.md, "Decided: the spirit fight": spirits are not humanoid, stances act
  as elements the way bending does in Avatar, attacks do damage, and damage subdues and never kills. A Fight command
  that does damage fits these rules; a weapon is new.
- **Push hands is the world's magic.** design.md: each village teaches one nation's push-hands style as its magic, the
  Well lends mana that belongs to the forest, and Master Yun says once at the dojo that mana is borrowed.
- **Growth rules.** Practiced gate levels are permanent and rise only by practice (five levels). The grid's branches
  unlock moves, and no node touches a gate or tool level. Forest ranks 5 to 7 are conferred by the five refiners.
  Inner demons' spoils pay for grid nodes. "Skill is bought only with skillful play."
- **Spirits grow by sparring, never by work.** design.md, "Decided: allies": "Spirits do not grow by working. The
  player levels them, by sparring with them in the ring or fighting other spirits in the forest." Each ally saves an
  id, element, level, satisfaction, mode and a present flag.
- **Monster Rancher is already in the record.** Settlement bouts follow its host organizations, cups and invitations
  (Decided), and design.md cites Monster Rancher 2's six grades, E to S.
- **The board's WAVE rows that stood.** Using a move is acknowledging (`wave-trigram-moves`), Welcome is listening
  (`wave-welcome-listen`), Validate is holding and Exhale is letting go (`wave-seize-validate`), the Witness Book
  (`wave-record`), the integration ladder of loot, then a move, then a companion (`wave-integrate-ladder`), the
  taught fight (`wave-taught-fight`), the straight four first (`wave-straight-first`), corners learned from spirits
  (`wave-corners-from-spirits`), the round 12 English names (`wave-move-names`) and qi made visible
  (`wave-qi-made-visible`). Master Yun teaches (`wave-teacher`, answered A).
- **The build lags the board.** Sprout #27 still labels its buttons by image and verb ("Heaven, rise / Ward off"),
  which `wave-buttons-image-first` showed before Wendell overruled it. The round 12 names never reached the screen.
- **Placeholder stats.** Every daemon in `data/daemons.json` has `maxHp: 16` and `demand: 8`, so no two differ.

## The six faces

### Shaman

**The Shaman drew hexagram 19, Spring, becoming 38, Estrangement.** Spring shows something rising with an edge on the
window, and Estrangement shows a conclusion reached from a distance. The council reached its battle from a distance:
twelve rounds of bots and rows, and Wendell's first line today says the council missed his meaning.

**The Shaman observes** that Wendell has pointed at familiar games the whole time. He overruled `wave-naming` because
it "strays too far from what makes pokemon work", and today he names Final Fantasy. Each time, the council answered
with a deeper custom system. The felt need under his words is a battle a new player already knows how to hold, so the
alchemy can be the new part.

**The Shaman sent the Emotional Body** on one problem: how emotional alchemy becomes a magic that is felt, not coded.
The report passed `check_report.py`. The Shaman uses two of its moves. Each teacher names the feeling a move meets
before teaching its form ("this is how you meet anger"), and the Witness Book page keeps the teacher's line beside the
move. The Shaman stops the daemon in four places. Its new line that mana is "borrowed through the feelings in your
body" rewrites a Decided story item (the Well lends it). Its cave-trial choices and its Act III channel fights change
Decided story. Its garden verbs as spells collide with offerings, which are garden verbs by a Decided rule. Its own
overreach line names the last stop: a system so deep the player has to journal to use it.

**The Shaman answers the daemon's two questions from the record.** The channels, streams and garden verbs already map
to one frame by element in design.md's channel table and village list, so the player learns them as one. Act 0 reads
the channel from play, and nothing in this ask needs that moved.

**The Shaman sees a risk** in a Fight command. Pushing until the charge breaks is the settlement's habit, and the game
exists to teach the other habit. A Fight that is as good as listening teaches the wrong move.

**The Shaman recommends** that Fight exist and that it visibly cost the player: Fight always lands, and the spirit's
push always lands back. Only a magic answer sends the push into emptiness. Only a magic answer can be held, and only
holding writes the Witness Book page. The standing test passes: nothing here says something is wrong with the
player.

### Architect

**The Architect drew hexagram 44, Serendipity, becoming 1, Unbroken.** Serendipity warns of building on one piece of
evidence, and Unbroken shows every line sending with nowhere for the return to land. One playtest by the designer is
the evidence, and the screen as built sends stances, gates and a bar with no single place for the player's eye to
rest. The Architect weighs every structure below against that one read and marks what a stranger must still confirm.

**The Architect observes** that a Final Fantasy battle on the Super NES is one shape: enemies on the left, the party on
the right facing them, and one window across the bottom with a short command list beside each fighter's name, HP and
MP. Enemy HP shows no number. A message line at the top says what just happened. The shape is known to the player
before the game teaches anything, which is the point.

**The Architect proposes this structure.** The command list holds at most four commands: Fight, Magic, Listen and
Item. Magic opens a submenu of learned moves, each with its mana cost. Listen is Welcome, and it works the way Final
Fantasy's Libra or Scan works: it shows what the foe is. Hold and Let go are not commands; after a right magic answer,
the window offers Hold in place of the list, and the glow bar appears only then. The stance leaves the main screen.
The player stands in their channel's stance by default, and "Change stance" sits inside Magic once Master Yun has
taught it. The data stays by id: commands in `data/slice.json` under `wave`, each move's teacher in
`data/wave-moves.json`, and a stat block on each record in `data/daemons.json` and `data/spirits.json`.

**The Architect sent the Controller** on spirit stats, as research on the middle model. The report passed
`check_report.py --research`. The Architect uses its five stats (renamed below), its damage shape (Fight scales with
Power; a magic answer takes the type chart's 1.3 or 0.7, which the code already holds as `over` and `resist`), its
point that a wild daemon's stats come from the charge the player brings (already `wave-spirit-from-charge`), and its
turn question. The Architect stops it in three places. "Drills as chores" breaks the Decided rule that spirits do not
grow by working. "Bond" duplicates satisfaction, which design.md already saves per ally. Its overreach line names the
third: tuning toward a stat set with no downside and delaying the playtest.

**The Architect spot-checked the Controller's links** and could not open them. The network proxy blocks all four
domains (Monster Rancher guide, LegendCup, the Final Fantasy wiki and Wikipedia), and the daemon flagged its second
source as unopened. No figure from those pages enters a position as fact. Monster Rancher 2's six stats appear here as
the daemon's claim, and design.md separately cites the game's grades.

**The Architect answers the turn question.** The battle stays turn-based, one action each, with the spirit's wind-up
shown before the player chooses, as the build does now. Active Time Battle adds a clock to a screen that is already
too much on a phone, and design.md keeps complexity down.

**The Architect sees a risk** in a stat block shown in battle. Final Fantasy shows the party's HP and MP and nothing of
the enemy's numbers. The spirit's stats belong on its Witness Book page and an ally's status screen, out of the fight.

### Challenger

**The Challenger drew hexagram 33, Retreat, becoming 12, Stalemate.** Retreat says leaving is available and the timing
decides what the player keeps; Stalemate says "you are seeking one game and wearing the face of the other." The risk
in this round is exactly that: a Final Fantasy screen drawn over the same push-hands quiz. The retreat worth making is
from WAVE as the whole battle to WAVE as the magic, and the timing matters because the build is a draft.

**The Challenger names the anti-pattern:** borrowing Final Fantasy's layout without its rhythm. The rhythm is pick one
command, watch one result, read one line. A screen with Final Fantasy's window and eight buttons inside it fails the
ask.

**The Challenger sent the Skeptic** on one problem: whether a weapon attack beside the alchemy keeps the lesson. The
report failed `check_report.py` twice, because its sources are local files with no links. The skill allows one
return, so the report was not saved through `save_report`; it sits beside the others as
`2026-10-07-sprout-demo-13-skeptic-FAILED-CHECK.md`. The Challenger weighs it anyway, as the skill allows. The
Challenger uses its three-policy bot test and its demand for a falsification sentence written before the build. The
Challenger stops it where it quotes Wendell as saying "test that split hard": he did not say it, and a search of the
board, the ledger and the demo folder finds the phrase nowhere. Its question "what does Wendell mean by split" is
answered by his own words: a regular attack with weapons, and the alchemy as the magic system. Its question whether
Fight costs mana is answered below: Fight is free, because Final Fantasy's lesson is that Fight always works.

**The Challenger sets the falsification test** for the Fight command, naming the decision it unlocks. Three bot
policies play rung 1 spirits: full WAVE through Magic, answer spam, and Fight spam. Fight spam must finish every fight,
because Fight always works. Fight is too strong, and its damage is cut before a stranger plays, if Fight spam ends with
HP left within 10% of full WAVE in 3 or more of 5 blocks. Then a cold player plays the new screen. If that player uses
only Fight through the first three real charges and cannot say what Listen does, the menu order or Fight's cost
changes before step 2 (the five demo spirits). The 10% and the three charges are the council's numbers, placeholders.

**The Challenger dissents on the stat names tied to elements.** "Speed is Wood" survives only by its phrasing. The
Challenger accepts the tie only if it buys a mechanic, and the Architect's answer below makes it a growth rate.

**The Challenger carries its lessons.** Before limiting a move, ask what it expresses: Fight expresses the
settlement's way, and its limit is that it cannot listen, which is a meaning, not a balance cap. A test names the
blocker it resolves: the bot test resolves whether Fight may ship, and the stranger test resolves the menu order.

### Regent

**The Regent drew hexagram 8, Alliance, becoming 2, Bearing.** Alliance shows a hole being filled that existed before
the work began; Bearing says the whole weight is carried unasked. The hole is a battle a new player can hold, and it
existed before WAVE. The weight the council carried unasked is the choice of what the battle is, which is Wendell's.

**The Regent sets the phase gate.** Sprout #27 stays a draft. The new screen, the four-command window, what stays
hidden and the Magic menu do not depend on the weapon answer, so they build now, beside the question (the Regent's
lesson: work that serves the gate runs beside it). The Fight command itself waits on `battle-fight-and-magic`. Step 2,
the five demo spirits, waits on the stat block, since each spirit's numbers come from it.

**The Regent sets non-negotiables.** Damage subdues and never kills. Mana is borrowed from the forest through the Well.
Spirits never grow by working. No weapon is sold in the demo, because skill is bought only with skillful play. The
round 12 names replace the image-and-verb labels on every button. Each teacher says a move's purpose before its rule.

**The Regent sets the definition of done for the screen.** One window, at most four commands, one message line, the
player's HP and mana, and no spirit numbers. A cold player's first real fight shows three commands.

**The Regent marks what is Proposed.** The stat names, the tie of stats to elements and every number are council drafts. Nothing
enters design.md until Wendell lets it stand.

### Diplomat

**The Diplomat drew hexagram 31, Mutuality, becoming 37, Household.** Mutuality says the movement arrived because the
council stopped; Household says an arrangement formed without being discussed. The council stopped defending its
screen, and the household was already there: Final Fantasy's party, where each person who joins brings their magic.

**The Diplomat sent the Player daemon** on one problem: what a new player wants from the battle. The report passed
`check_report.py` after two returns. The first answered last round's problem; the second lacked a heading and links,
and said Final Fantasy IV's first battles offer only Fight and Run. The resend corrected that: Rosa brings White Magic
and Rydia brings Black Magic. The Diplomat uses its core point, that a new player wants to make one move, see it work,
and hear what it means only after trusting the system, and its cut list: hide the corner gates, the hold timing, the Witness Book and
the stance choice at first.

**The Diplomat stops the daemon at its question,** whether the first real spirit should accept only Welcome. The record
answers it: the taught fight (`wave-taught-fight`) already opens one input per beat and cannot be lost. A real fight
with one working button is a quiz. The first real fight offers three commands that all do something visible.

**The Diplomat sets copy principles.** Commands use Final Fantasy's own words: Fight, Magic, Item, and Listen for the
one that is ours. Every move shows its round 12 English name and glyph and nothing else on the button. The message
line shows one sentence at a time in the reader's word ("Sky Lift. Its push rises past you."). The Chinese name lives
on the Witness Book page (the Diplomat's pending lesson: putting the foreign name second is not translation).

**The Diplomat sets the onboarding path,** which is Final Fantasy's: magic arrives with people. Master Yun teaches
Listen and the first two moves at the dojo, and the rest of the straight four as the player practices. The tame charge
at the strip edge teaches Hold and Let go. Spirits teach the corner four. In Act II each village's refiner brings that
village's style, the way Rosa and Rydia bring theirs. An integrated daemon brings its gift move.

### Sage

**The Sage drew hexagram 51, Shock, becoming 3, Sprouting.** Shock comes twice: round 11 heard "too much", and today
the same shock comes again. Sprouting says this is early, the mess is not a verdict, and the counsel is to appoint
helpers and decline any journey. Wendell appointed the helpers by asking for subagents. The journey to decline is a
bigger system; the smallest screen comes first.

The Sage's synthesis is below, after the verdicts.

## Verdicts

| Face | Face-off screen | Fight plus Magic | Hidden at first | Magic from teachers | Five stats | Growth by sparring | Turn-based |
|---|---|---|---|---|---|---|---|
| Shaman | Yes | Yes, if Fight cannot listen (leans to B otherwise) | Yes | Yes, feeling first | Yes | Yes, satisfaction from listening | Yes |
| Architect | Yes, one window | Yes | Yes, stance inside Magic | Yes | Yes, as growth rates | Yes | Yes |
| Challenger | Yes, rhythm not layout | Only if the bot test passes | Yes | Yes | Dissents on tying stats to elements, accepts it as growth rate | Yes | Yes |
| Regent | Yes, definition of done | Wendell's call | Yes | Yes, purpose first | Proposed only | Yes, never by work | Yes |
| Diplomat | Yes | Yes | Yes, three commands first | Yes, as Final Fantasy's party | Yes, plain names | Yes | Yes |
| Sage | Synthesis | Synthesis | Synthesis | Synthesis | Synthesis | Synthesis | Synthesis |

## Dissent check

The pass was not unanimous. The Challenger accepts Fight only if the three-policy bot test passes, and the Shaman
leans to a magic-only battle unless Fight is visibly unable to listen. The Challenger dissented on tying stats to
elements, and withdrew the dissent when the tie became a growth rate. The Regent holds that weapon or no weapon is
Wendell's call and gives no verdict on it. The faces agree on the screen, the menu and the hidden list, because his
steer and Final Fantasy's own shape answer those.

## Sage: synthesis

The Shaman gave the reason the council missed his meaning, the felt-first teaching from the Emotional Body, and the
rule that Fight always lands but never listens. The Architect gave the four-command window, Listen as Libra, the stance
moved inside Magic, the stat block and its damage shape from the Controller, and the turn-based answer. The Challenger
gave the falsification test, caught the Skeptic's invented quote, and forced the tie of stats to elements to buy a mechanic. The
Regent gave the phase gate, so the screen builds now and only Fight waits, and the non-negotiables. The Diplomat gave
Final Fantasy's words, the party as the way magic arrives, and stopped the Player daemon's one-button fight.

The Sage dropped the Emotional Body's lore line, cave choices and garden-verb spells, the Controller's chores and
Bond, and the Skeptic's quote, each for the reason its face gave. The dissent on Fight goes to Wendell as the one
question. The Sage does not decide it.

## How the four subjects come out

**(a) The screen.** The spirit stands on the left and the traveler's sprite on the right, facing it. One window runs
along the bottom: the command list on the left, the traveler's name, HP and mana on the right. A message line at the
top says one sentence. The spirit's wind-up shows as its weather over it. Nothing else appears.

**(b) Fight and magic.** The council recommends a Fight command beside emotional alchemy as Magic. Fight always lands
and costs nothing, and the spirit's push always lands back. A right Magic answer sends the push into emptiness, can be
held to write the Witness Book page, and is the only way to integrate a daemon. WAVE survives as the order the Magic
menu teaches: Listen, answer, Hold, Let go. Whether Fight uses a weapon is Wendell's call, on the board.

**(c) A magic that grows.** Teachers give moves, practice levels them, the grid's branches open deeper moves, and
integrated daemons give gift moves. The table below sets the order.

| When | Who | What the player learns | How it grows |
|---|---|---|---|
| Act I, milestone 2 (dojo) | Master Yun | Listen, Sky Lift, Earth Yield | Gate level by practice, 1 to 5 |
| Act I, dojo bounties | Master Yun | River Fill, Flame Follow, Change stance | Gate level by practice |
| Strip edge (taught fight) | Master Yun | Hold and Let go | Timing window widens with level |
| The strip | Spirits that strike with a corner weather | Wind Draw, Lake Gather, Thunder Split, Mountain Stand | Learned by holding that spirit |
| The strip and the ring | Integrated daemons | Each daemon's gift move | The integration ladder |
| Act II | Each village's refiner | That village's style as a stance, felt move first | Forest rank keys open that stream on the grid |
| Act II and III | The grid | Branch moves, one arm per subtype | Points from rank and Root level, spoils of inner demons |

**(d) Spirit stats.** Every spirit and daemon carries five stats in Final Fantasy's words: HP, Power, Guard, Magic and
Speed. Its element is its type on the chart. Each element grows one stat fastest, which is how the cycle shows in a
stat block: Earth in HP, Fire in Power, Metal in Guard, Water in Magic, Wood in Speed. Allies grow the way Monster
Rancher monsters do, by how the player trains them, inside design.md's Decided rule that they grow by sparring and
never by work.

## Outputs

### Positions (each stands unless Wendell flips it)

1. **`battle-face-off-screen`.** The battle looks like a Super NES Final Fantasy battle: the spirit on the left, the
   traveler's sprite on the right facing it, one window along the bottom, a message line at the top. The window shows
   the command list and the traveler's HP and mana. The spirit shows no numbers; its look and its push text show how
   charged it is. Why it did not need Wendell: his words ask for it, and design.md's SNES profile already sets the
   screen.
2. **`battle-four-commands`.** The command list holds at most four commands: Fight, Magic, Listen and Item. Listen is
   Welcome and works like Final Fantasy's Libra: the first shows the spirit's stance and feeling, the second its coming
   weather. Hold appears in place of the list only after a right Magic answer. If Wendell answers B on
   `battle-fight-and-magic`, Fight leaves the list. Why: his "the user interface is a bit much", Final Fantasy's own
   menu, and `wave-welcome-listen` and `wave-seize-validate`, which keep their rules.
3. **`battle-hidden-first`.** A new player's first real fight shows three commands (Fight, Magic, Listen) and two
   moves under Magic. Hidden at first: the stance choice (the traveler stands in their channel's stance until Master
   Yun teaches Change stance, which then sits inside Magic), the corner gates, the hold bar until a right answer opens
   it, the Witness Book (opened after the fight), and the Chinese names (Witness Book only). This replaces the on-screen
   stance row in `wave-straight-first`; the order of what is taught stands. Why: his steer, and the Player daemon's cut
   list; the first spirit is not a one-button fight, because `wave-taught-fight` already teaches one input at a time.
4. **`battle-turns`.** The battle stays turn-based, one action each, with the spirit's wind-up shown before the
   traveler chooses. No Active Time Battle in the demo. Why: the Controller's question, answered by the phone screen
   and design.md's rule to keep complexity down; the build already works this way.
5. **`magic-is-the-alchemy`.** The Magic menu holds emotional alchemy. Each entry is a move by its round 12 English
   name, costs mana the Well lends, and answers the spirit's weather. A right answer sends the push into emptiness and
   lands on the type chart; holding writes the Witness Book page; letting go releases or integrates. WAVE is the order
   the menu teaches: Listen, answer, Hold, Let go. Why: his words ("the wuxing emotional alchemy be the magic system"),
   and every WAVE row that stood.
6. **`magic-from-teachers`.** Moves arrive with people, as magic arrives with party members in Final Fantasy IV.
   Master Yun teaches Listen and the straight four, then Hold and Let go at the strip edge; spirits teach the corner
   four; each village's refiner teaches that village's style as a stance in Act II; integrated daemons give gift moves.
   Each teacher names the feeling a move meets before its rule. Why: his "learn the moves from various characters",
   `wave-teacher` (Yun), `wave-corners-from-spirits`, design.md's villages, and `wave-integrate-ladder`.
7. **`magic-grows`.** The magic grows four ways, all earned in play. Practice raises a move's level, 1 to 5, and a
   higher level shows a larger qi effect. Forest ranks give the keys that open a village's stream on the grid. Grid
   branches unlock deeper moves, paid by points and inner demons' spoils. Integration deepens a daemon's gift. Nothing
   is bought. Why: design.md's Decided growth rules (gate levels, ranks, grid branches unlock moves, skill bought only
   with skillful play) and `wave-qi-made-visible`.
8. **`spirit-five-stats`.** Every spirit and daemon has five stats: HP, Power (how hard its push lands), Guard (how
   much Fight it shrugs off), Magic (how strong its weather is and how well it resists Magic) and Speed (who acts first).
   Its element is its type. Each element grows one stat fastest: Earth HP, Fire Power, Metal Guard, Water Magic, Wood
   Speed. A wild daemon's level comes from the charge the traveler brings, or from the table in story mode. Stats show
   on the Witness Book page and an ally's status screen, never in the fight. Names and numbers are council drafts.
   Why: his question, the Controller's report, `wave-spirit-from-charge`, and design.md's pillar that everything
   teaches the cycle.
9. **`spirit-growth-by-training`.** Allies grow as Monster Rancher monsters do, by how the traveler trains them, inside
   design.md's rules. Sparring in the ring is the drill: each spar trains one stat the traveler picks, and fighting
   other spirits in the forest raises level. Work never raises a stat. Satisfaction does the job of Monster Rancher's
   loyalty: sparring that listens (Listen and Hold) raises it, sparring by Fight alone lowers it. There is no lifespan
   and no death; a neglected ally steps back, as design.md already says. Why: his "monster rancher can be used for
   inspiration", design.md's Decided allies rules, and its saved fields (level, satisfaction).

### Question (passed the reach test)

**`battle-fight-and-magic`: Should the battle have a plain Fight command beside the alchemy?** The Regent owns it, with
the Challenger.

- A. Fight with a hunter's staff, and the alchemy as Magic (recommended). The traveler gets one staff at the strip
  and no weapon is sold in the demo. Fight always lands and costs nothing, and the spirit's push lands back; only Magic
  listens, holds and integrates. The battle reads as Final Fantasy from the first turn. It ships only if the
  three-policy bot test passes, and the anchor's "the battle is the player doing WAVE" becomes "the magic is WAVE".
- B. Magic only, in Final Fantasy's menu. No Fight; the first command is Sky Lift, taught by Yun, which always lands.
  Every action stays alchemy and the anchor stands as written. A new player has no plain button to lean on while
  learning.
- C. Fight with weapons as gear, as Final Fantasy has: swords and staves with stats, bought and found. Most like
  Final Fantasy, and the most to build. Bought weapons would lapse at the exile like settlement talismans, to keep
  "skill is bought only with skillful play", and they compete with talismans as the loadout.

Why only he can answer: he names it as his own struggle, it decides what the battle is, and a weapon adds a rule
beside design.md's Decided spirit fight, where stances act as elements. The record holds the rules around it but not his
preference. Why it was not asked before: the steer to make the battle a Final Fantasy battle with a regular attack is
new today. The answer decides whether the Fight command, a staff sprite and the three-policy bot test get built.

## Tests set for the next pass (set 2026-10-07)

1. **Three-policy bot test.** Full WAVE through Magic, answer spam and Fight spam on rung 1 spirits. Fight is cut if it
   ends within 10% of full WAVE's HP left in 3 or more of 5 blocks. Due with the build of Fight, if Wendell answers A
   or C. It resolves whether Fight may ship.
2. **Wendell's read of the new screen.** He plays it on his phone and says whether it reads as a Final Fantasy battle
   and whether the interface is still too much. Due at his next play after the screen is built. It resolves whether a
   stranger should play it yet.
3. **A cold phone player on the new screen.** That player finishes the taught fight without outside help, says what
   Listen does, and uses Magic unprompted in the first real charge. Due at the first stranger playtest after test 2
   passes. It resolves the menu order and Fight's cost, before step 2.

Subagent tokens: 199,803 (Player 43,630; Emotional Body 58,217; Controller 29,173; Skeptic 68,783).
