# Six-face pass: battle intake 1, how spirits from wrong answers become fights worth having

**Date:** 2026-10-13. **Called by:** Wendell, in the Skilled Helper thread: "Yeah we need to rethink this battle logic
in general. It's pretty clunky and unintuitive we may need to go through a whole brainstorm intake around it so we can
understand how spirits generated from wrong answers turn into fun and meaningful battle encounters. This one's not
meeting the mark". **Subject:** the spirit fight in the Skilled Helper tap-throughs (sprout
`campaigns/skilled-helper/part-two/tools/prototype.template.html`, the fight section, and `slice/wave.js`). This is the
first pass of the intake. Inputs: board position `wave-water-controls-fire` and draft sprout #49.

**Casts** (three coins, `council/iching/cast.py`):

| Agent | Hexagram | Becomes |
| --- | --- | --- |
| Shaman | 25 Candour, lines 1, 3, 5, 6 | 62 Overstep |
| Architect | 54 Home Field Advantage, line 1 | 40 Thaw |
| Challenger | 33 Retreat, line 3 | 12 Stalemate |
| Regent | 21 Bite, lines 1, 2 | 64 Almost |
| Diplomat | 53 Emergence, lines 1, 2, 3, 5 | 41 Spending |
| Sage | 25 Candour, lines 5, 6 | 51 Shock |
| Daemon: Player (for the Diplomat) | 36 Nightfall, line 2 | 11 Mingling |
| Daemon: Skeptic (for the Challenger) | 45 Gathering, lines 1, 2, 4 | 60 Measure |

**Daemons.** Two ran. Both reports passed `check_report.py` (the Player's on its second try, for two headings) and are
saved in `council/daemons/reports/2026-10-13-battle-intake1-*.md`. Two of the Player's research links were spot-checked
and load. Subagent tokens: about 158,000 (Player 97,697 over two runs, Skeptic 60,117).

## Scorecard

Pass 3 on the Pruner's fights set F1 (a cold player), F2 (a mana run) and F3 (his phone play of a fight). F3 is the
only one that ran, and it failed: his verdict above. F1 and F2 are retired with the fight they measured.

## Anchor

A mistake in a talk is the player's own urge, walking out into the world. Meeting it is offered and never forced, and
only listening brings a charge home (pass 3, unchanged). Added by this pass from his words: the meeting has to be fun,
and it has to mean something about the talk it came from.

## Shaman (magenta)

**Candour, becoming Overstep, says the fight is doing slightly too much.** The Shaman reads the record and finds the
original wish buried. Wendell's first steer on daemon battles (`enc-inner-moves`, 2026-10-06) was "more like pokemon
battles where the moves do HP to the daemon and each of the moves is an inner move the player can do to get the
emotional alchemy effects in themselves". Today no move in the fight is an inner move a player could do on themselves.
River Fill and Earth Yield are names for elements, and Hold and Let go are timing.

**The Shaman recommends the fight be the urge met from inside.** The spirit is the urge that spoke the wrong line. The
four WAVE moves are the moves, because each is something a person can do with an urge: Welcome it, Acknowledge it by
naming its feeling, Validate the need under it, and Exhale it. When it is metabolised, the player says the line they
missed in the talk, and that is the finishing blow.

## Architect (orange)

**Home Field Advantage, becoming Thaw, says the fight follows rules nobody told the player.** The fight stands on
ground laid by three other builds. Sprout #29 gave it a role-playing menu (Fight, Magic, Listen, Item, HP, mana,
levels, speed, guard). Root gave it push hands (eight gates, weathers, stances, the seize). The WAVE build gave it
Welcome, Validate and Exhale, under two names each. Each layer answered a real ruling, and no layer was taken out when
the next arrived.

**The Architect sets the structure every option keeps.** A charge stores the words of the wrong line and the need the
talk shows in brackets (Ama Rell's: "She did not want it named a burden. She wanted room."). That text already exists
in `encounters.yaml`, and the fight opens with it. A fight shows the spirit's next push in words before the player
picks, at most four choices on screen, one tap a turn, three to five turns.

## Challenger (red)

**Retreat, becoming Stalemate, says leave early, while there is still something to keep.** The Challenger sent the
Skeptic to count. It found about 25 concepts in one fight, most of them taught nowhere on the battle screen, and every
action named twice across the two files. Three findings are faults in the build today, whatever the redesign: the
fight never shows the wrong line, an Earth foe's plan reads "It means to bury you" while it strikes other weathers, and
a stance change costs no turn.

**The Challenger names the anti-pattern: the answer key.** Under the trigram rule, and under #49's fix, one move is
right and the rest let the push land. That is a quiz with a cycle the player cannot see. The Player daemon warned of
the same fault from the other side: skill cards with one right answer stop being Egan's model, which allows more than
one good line. Pokémon's chart has no wrong move, only stronger and weaker ones, which is what Wendell asked for in
`wave-acknowledge` ("strays too far from what makes pokemon work").

**Falsification test B1:** five phone players who have not seen the cycle each play one fight; it fails if fewer than
four finish without a retry, or if fewer than four can say afterwards what the spirit needed.

## Regent (amber)

**Bite, becoming Almost, says something is lodged here and nothing closes until it is named.** What is lodged is the
question of what the fight is for. The Regent's non-negotiables are Wendell's rulings that survive any redesign:
fights are offered and never forced, and declining costs nothing (`p2n-stakes` C); taking a fight costs HP and mana
(`pf-costs-hp-and-mana`); Fight rests a foe and only listening clears a charge (`pf-fight-rests`); water controls fire
(`wave-water-controls-fire`).

**The Regent decides #49.** The Lamp-keeper's track is waiting on Wendell's phone play, and its fights still show fire
answering water, the rule he just ruled wrong. #49 fixes that on the same stack, with tests passing. It stays the
interim rule until the redesign replaces the fight; the ruling carries into whatever chart comes next. Definition of
done for the intake: his answers to the two questions below, then one spirit built in the new shape, played by him.

## Diplomat (green)

**Emergence, becoming Spending, says this has stages, and the pass is trying to skip one.** The stage being skipped is
his play. The Diplomat will not ask him to read a design; he will play one fight. The Player daemon's picture is the
one to build toward: "The spirit says its line back, the Player taps a skill card, and the spirit says what it needed.
A fight of about ninety seconds, ending on a spoken want."

**The Diplomat sets the copy rule.** One name for each action, on screen and in code. The spirit's push is written in
words, not weathers. The element shows as the feeling it carries ("Fire, anger"), as the Skeptic asked.

## Sage (teal)

**Candour, becoming Shock, says act straight and expect it to go off a second time.** The Sage expects the first
build of the new fight to miss too, and the intake is set up so that missing costs one spirit, not a track.

**Synthesis.** The Shaman restored the first wish: moves that are inner moves. The Architect named the three stacked
layers and kept the talk's words as the fight's material. The Challenger named the answer key as the anti-pattern and
set B1. The Regent held the rulings and decided #49. The Diplomat put the player's ninety seconds first. Dropped: the
Player daemon's skill cards as the whole fight (the Shaman's version keeps them as the finisher instead), and the
Skeptic's stance chips (stances may not survive).

## Verdicts

| Face | Line comes back | Moves are inner moves | Type chart, no answer key | Trigrams leave the spirit fight | #49 as interim |
| --- | --- | --- | --- | --- | --- |
| Shaman | Yes | Yes (recommends) | Yes | Yes | Yes |
| Architect | Yes (sets it) | Yes | Yes | Yes, kept in Root | Yes |
| Challenger | Yes | Yes | Yes (asked for it) | Yes | Yes |
| Regent | Yes | His call | His call | His call | Yes (decides it) |
| Diplomat | Yes | Yes | Yes | Lean yes | Yes |

## Dissent check

Not unanimous. The Regent will not take a side on what the fight is for or on the trigrams, because Wendell asked for
the trigrams himself (`wave-trigram-moves`: "The merging of root and the mechanics of spirit battle has the solution I
think I'm looking for"). Pulling them out of the spirit fight reverses that steer, so it goes to him. The Player daemon
and the Shaman differ on whether the helping skill is the whole fight or its last blow.

## Outputs

### Positions (each stands unless Wendell flips it)

1. **`bi-three-layers`.** The fight is clunky because three systems are stacked in it (the role-playing menu, Root's
   push hands and WAVE), each from a real ruling, none removed when the next came, about 25 concepts in one fight, and
   the talk that made the spirit plays no part. Why it did not need him: the Skeptic's count of the built code.
2. **`bi-line-comes-back`.** Whatever shape wins, the spirit opens by speaking the wrong line the player picked, and
   the need the talk showed in brackets is what the spirit is carrying. Why: `encounters.yaml` already holds both, and
   his ask was how spirits from wrong answers become meaningful.
3. **`bi-one-tap`.** One tap a turn, at most four choices on screen, the spirit's next push in words before the
   player picks, three to five turns, one name for each action. Why: `wave-acknowledge-turn` already took Slay the
   Spire's shown intent, and the Skeptic found every action named twice.
4. **`bi-49-interim`.** Sprout #49 (water answers fire) rides on the Lamp-keeper rekey stack as the interim rule, so
   his next phone play does not show the rule he ruled wrong. Its Earth default stands with it: until the traveler has
   a move that controls earth, an Earth foe strikes only with weathers the first four moves can meet, and says so. The
   redesign replaces the code and keeps the ruling. Why: `wave-water-controls-fire` and his pending Lamp-keeper play.
5. **`bi-one-spirit-first`.** After his answers, one fresh thread builds the chosen shape for one spirit, Ama Rell's
   Fixer at P1, as its own phone page; he plays it before any track's fights change, and B1 runs on it. Why: the
   Diplomat's stage, and the short-sessions rule.

### Questions

1. **`bi-what-for`** (Shaman, Regent). What is a spirit fight for?
   - **A. Meet the urge, then say the line (recommended).** The spirit is your urge speaking the wrong line. The
     moves are Welcome, Acknowledge, Validate and Exhale, done on the urge. When it is met, you say the line you
     missed, and that ends the fight. It teaches emotional alchemy in the fight and the book in the finish.
   - **B. The rematch.** The spirit is the talk again. Your moves are the helping skills as cards, and the fight ends
     when the spirit says what it needed. It teaches the book only.
   - **C. Push hands, trimmed.** Keep the trigram answers with water controlling fire, and cut the menu, mana and the
     seize, so a turn is read the strike and pick one of four moves. It keeps Root's art and teaches the cycle.
   - Why only he can answer: it decides what the fight teaches, and A and B take the trigram moves out of the spirit
     fight (they stay in Root and the dojo), which reverses his `wave-trigram-moves` steer. Why not asked before: each
     earlier ruling fixed one layer; nobody asked what the whole fight is for until he called it clunky.
2. **`bi-chart`** (Challenger, Architect). How does the five-element chart decide a turn?
   - **A. Type chart (recommended).** Every move works. A move made from the element that controls the spirit's
     feeling lands double (water on fire); one that feeds it lands half. No wrong move, only stronger and weaker.
   - **B. Answer key.** Only the controlling move lands; any other lets the push land, as #49 builds it.
   - **C. Colour only.** The element names the feeling the spirit carries and changes nothing in the numbers.
   - Why only he can answer: it sets how hard the fight is and whether the elements are taught by reward or by
     failure. Why not asked before: the answer key arrived with the trigram moves and was never put to him as a choice.

### Reach test, on every question the pass raised

- The Player daemon's "Should a wrong card still cost HP?": answered by `p2n-stakes` C ("Taking it costs HP and mana")
  and `pf-costs-hp-and-mana`. The spirit's push costs HP on any turn it is not met. It does not leave the pass.
- The Skeptic's "Is a stance change meant to cost no turn?": a build fact, folded into `bi-one-tap`; stances may not
  survive `bi-what-for`. It does not leave the pass.
- The Skeptic's "Is the befriend path held back on purpose?": `pf-fight-rests` lists the endings; the redesign
  rebuilds them from `bi-what-for`. It does not leave the pass.
- `bi-what-for` and `bi-chart` passed: each needs his preference and changes what gets built.

### Tests

- **B1** (Challenger), by the first build: five cold phone players, one fight each; fails under four of five finishing
  without a retry or under four of five saying what the spirit needed.
- **B2** (Diplomat), on his play of Ama Rell's Fixer: does he say it was fun, and can he say what it meant.
