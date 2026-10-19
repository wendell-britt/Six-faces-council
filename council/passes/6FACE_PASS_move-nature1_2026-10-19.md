# Six-face pass: what a move is (move-nature1), 2026-10-19

**Called by:** Wendell, board read 2026-10-19 (ledger `2026-10-19-pull-223918.json`), overruling `cc-move-sets-element`.
**His words:** "I don't know if move-engine is robust enough for this. We need to do an audit across surfaces because I
Think this is where most drift is happening. We're still figruing out what the fundamental nature of a move is in the
game. 5 channels X 3 satisfaction states sheng ke game master faces and daemons"
**Pass:** first on this subject. Evidence: `council/research/2026-10-19-move-audit.md` (bars-engine, sprout, council,
game-masters-guide). Ontology profile: game_design (QUICKSTART and the `emotional_alchemy` block of the yaml).

**Casts.** Shaman 4 Fog → 40 Thaw. Architect 35 Sunrise → 6 Divergence. Challenger 2 Bearing → 64 Almost. Regent 33
Retreat → 50 The Cauldron. Diplomat 32 Endurance → 6 Divergence. Sage 54 Home Field Advantage → 19 Spring.

## Scorecard

No earlier pass on this subject set tests. `crafting-charge1` set one that this pass answers: it assumed move and
element are one fact; the audit shows the record does not hold that (board `sf-ally-moves`).

## Anchor

A move is how a player carries a charge somewhere: the Emotional Alchemy grammar that every game in the library reads
(`ea-cap-which-waits`, 2026-10-14: "The move library is something all the games use").

## Shaman (Fog → Thaw)

**Fog says we have been guessing where we could ask.** Nine things answer to "move", and the player feels none of the
difference; they feel only that a move did or did not land. **The felt object is the cell.** A person in Anger,
dissatisfied, knows where they are; a move is what takes them to another cell or lets them stay and deepen. **Faces
and daemons are voices.** A daemon reaches for the same move every time because that is its habit; a face colours how
any move is offered. Making them axes of the move turns a person into a lookup table.

## Architect (Sunrise → Divergence)

**Divergence warns that going deeper and pushing forward at once cancel.** So the pass settles the kernel before any
code moves. **The kernel is the 5 × 3 grid.** Fifteen cells (channel × satisfaction state); a move is an edge between
cells, typed by relation: same channel (Transcend), sheng neighbour (Generative), ke target (Control). This is what
Wendell's own list names, and it is what `move-engine.ts` half-encodes: it gives the element pair but not the state
change, which four other files then guess at differently. **One table, read by every surface.** The fifteen named
moves become rows of a data file in this repo; bars-engine and sprout read it or carry a copy under a lockstep test,
as the transformation registry already does. Built only after his answers below, because the state change per family
is the open fact. **The check-in bug is fixed now** by sharing wuxing's tables with the client, not by a fifth copy.

## Challenger (Bearing → Almost)

**Almost: care where the crossing looks finished.** move-engine looks canonical because it is named and tidy; it is not
robust, since it says nothing about satisfaction and nine importers re-derive the rest. **Breakpoint:** the
same Control move lowers satisfaction in move-engine, holds it in the slice, and releases grip on the board. Any
build on top inherits whichever file it imported. **Falsification test:** play one charge through Anger dissatisfied →
Temper Action in the check-in, the slice and the ontology game; if the three end in different cells, the table is not
one fact. Today they do. **Root-fight is not drift:** answering fire with water is a reply (the restrainer answers),
a different relation, and it should be named so.

## Regent (Retreat → Cauldron)

**Retreat in good order keeps the vessel.** Nothing ships against an unsettled definition: `cc-move-sets-element`
stays overruled and the crafting ember stores the move and the element separately, rejecting nothing, until the
kernel is ruled. **Authority already given:** the Basic Moves and the fifteen are separate objects (owner decision
2026-10-10); Transcend raises satisfaction by two (`ss-shift-up`); ke acts by releasing grip (`ea13b-ke-release`);
daemons teach moves (`sf-moves-from-people`). These are positions, not questions. **Definition of done** for the move
table: one file, a test in each repo that fails when a copy differs, and the check-in reading it.

## Diplomat (Endurance → Divergence)

**Endurance: this exchange has happened before.** "Five moves" already means four things to a reader of sprout. Every
surface that shows a move to a player names its family in plain words. **Names hold across games.** Metal's gold is
"Wonder-Excitement" in his list of 2026-10-12, so code stops choosing between Wonder and Excitement. Earth's channel
is "Neutrality", never "Neutral", so it is not mistaken for the state.

## Verdicts

| Face | Kernel is the 5×3 grid | Ke and satisfaction | Faces and daemons |
|---|---|---|---|
| Shaman | yes | holds (release grip) | voices, not axes |
| Architect | yes | needs his ruling; leans holds | layers that pick edges |
| Challenger | yes, after the play test | holds; −1 breaks Temper Action's name | layers |
| Regent | yes | holds, per `ea13b` | layers; daemons teach |
| Diplomat | yes | no view | face = register |

**Dissent check.** Unanimous on the grid as kernel: a flag. The record leans on Wendell's own list, which the faces may
be reading too literally; question `mn-q-what-move-is` keeps the other reading (moves as character actions first)
open for him. The Architect alone holds out on ke until he rules.

## Sage (Home Field Advantage → Spring)

**We have been following rules nobody told us**, each surface inventing what a move does. The Shaman gave the cell
as the felt object, the Architect the one table, the Challenger the test and the reply relation, the Regent what is
already ruled, the Diplomat the names. Dropped: a full rename of bars-engine's five channel spellings (too wide for
this pass; it rides the table build). Dissent: the Architect's hold on ke. Wendell decides the three questions.

## Outputs

**Positions** (stand unless he flips them):
- `mn-basic-moves-apart`: owner decision 2026-10-10 (`wave-terminology/owner-decision.md`).
- `mn-transcend-plus-two`: `ss-shift-up`, move-engine `energyDelta +2`.
- `mn-ember-both`: replaces the overruled `cc-move-sets-element`; `sf-ally-moves`.
- `mn-checkin-fix`: a bug, `DailyCheckInQuest.tsx:13-18` against `wuxing.ts:28-45`.
- `mn-root-fight-reply`: sprout `root-fight/index.html:423`.
- `mn-gold-names`: `council/callsheets/somatic-ontology.md:19-24`.

**Questions** (passed the reach test; the record names the objects but not his preference):
- `mn-q-what-move-is` (Architect), `mn-q-ke-state` (Challenger), `mn-q-face-daemon` (Shaman).

**Tests set** (due 2026-10-26): after his answers, one table file exists, and the Temper Action play test ends in one
cell across the check-in, the slice and the ontology game.
