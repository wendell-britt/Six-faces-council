# Six-face pass 1 — what should exist in the engine slice

**Run 2026-10-16**, called by Wendell in chat: "I'd want to kick the tires on this first. We want the
biggest slice we can create that tests this but I think the plan needs to be thought through more.
The real contract is to use our process 6 game master analysis + ontology to decide what should
exist in the slice." The subject is the four-layer engine contract he named in the same session:
Twine-style narrative, on a Harvest Moon / Stardew daily chore loop, on a battle encounter
interface, with tabletop storytelling rules ported on as a board-game simulator whose systems can
affect the story. This is pass 1 on the subject. The `design-ontology` load profile `game_design`
is loaded for every face; daemons were not sent, to keep the session bounded.

## Scorecard

The previous pass on this environment (zo-environment 1, 2026-10-15) set two tests. **`zo-race-test`**
(Challenger, due 2026-10-17): not yet run. **`zo-quota-wiring`** (Architect, due 2026-10-17): not
yet run. Both stay open, and scheduled council work in this environment stays blocked behind them.
Wendell ruled in chat on 2026-10-16 ("Hell yeah. This makes sense."): `zo-division`, `zo-gates` and
`zo-guards` stand, and `zo-automations` was answered "Run the census and propose the list" — the
automation census is its own strand, not this one. New tests at the end.

## Anchor

Unchanged from the zo-environment pass — Wendell's steer of 2026-10-15 22:01Z: the work is *a
playable ontology for helping people install integral consciousness, somatic awareness and shadow
work through accessible story driven play*. Today he bound the engine question to it: "a narrative
game engine on top of a daily chore game engine on top of a battle encounter interface," with
tabletop rules as the board-game simulator that lets RPG systems affect the story.

## Casts (three coins, `council/iching/cast.py --seed 20261016`, so the record replays)

| Face | Hexagram | Changing lines | Becomes |
|---|---|---|---|
| Shaman | 57 Persuasion 巽 | 4, 5, 6 | 32 Endurance 恆 |
| Architect | 44 Serendipity 姤 | 6 | 28 Overload 大過 |
| Challenger | 38 Estrangement 睽 | — | — |
| Regent | 54 Home Field Advantage 歸妹 | — | — |
| Diplomat | 16 Anticipation 豫 | 4, 5 | 8 Alliance 比 |
| Sage | 42 Windfall 益 | 2, 3 | 9 Restraint 小畜 |

## The faces

## Shaman: 57 Persuasion, becoming 32 Endurance

Hexagram 57, Persuasion, changing into 32, Endurance: an effect is already happening that you have
not admitted to. What is moving underneath the "kick the tires" request is that the tires are the
game. Constitution 2 says the designer is also a player, and constitution 3 begins with authentic
pleasure — so the slice is not a test rig that precedes play; it is the first playable build, and
the felt standard is his enjoyment of his own day in it. The ontology names his counterweight
explicitly: he is rewarded by generation and integration more than reduction and closure, so the
slice's danger is scaffolding without enchantment — four engines wired correctly and nothing to
feel. The smallest meaningful loop exists to prevent exactly that. The slice must carry one felt
moment: labor spent in the day turns into a story consequence the game does not announce from a
dashboard. His 2026-09-09 lesson binds the passage: the player leaves with a move they can use, so
the slice's one passage should hand him something applicable outside the game, obliquely told
inside it. The body gets a vote, so the encounter carries a somatic beat, which the trust engine's
stress and shadow state already knows how to hold. Recommendation: the slice's acceptance test is
felt before it is mechanical — he plays one day and says whether the moment landed. Standing test:
nothing in the slice may say something is wrong with the player; the rules surface resolves stakes
and never diagnoses.

## Architect: 44 Serendipity, becoming 28 Overload

Hexagram 44, Serendipity, changing into 28, Overload: you are building on one piece of evidence,
and the risk it names is the risk in "biggest" — weight packed in the middle, thin at both ends,
the ridgepole sagging. What must be true in the machine, verified in the record today: the trust
reducer (`bars-engine .specify/specs/trust-encounter-loop/plan.md`) is pure, isolated and proven
completable by simulation; `world-state-provider` holds the pattern of session state above the
boundary that would otherwise kill it; `twine-authoring-ir` compiles passages with `quest_emit` and
`bar_emit` already in the IR; the walkable sprite slice and eight named cave chambers exist
(fr-scene-staging, fr-cave-studio). What has no spec anywhere: the day loop, the rules surface, and
the seam contracts between layers. The binary in "biggest slice" is false the same way "Claude or
Zo" was false: biggest does not mean most content, it means every seam exercised once. So the
slice's size is fixed by its topology, not its volume: one day cycle, one passage that fires on a
world predicate, one encounter on the trust reducer, one tabletop resolution, one sleep commit.
Content volume — a second NPC, a second day, art breadth — adds zero contract signal and is the
Overload reading made literal. A third position answers "demo or spec": the slice is the spec's
executable section. The spec kit carries the contract; the slice compiles from it; neither exists
alone. Recommendation: the spec kit names the four seam contracts as interfaces with owning types,
and the slice is the proof section that compiles against all four. Standing test: every claim in
this pass cites a file that exists.

## Challenger: 38 Estrangement, no changing lines

Hexagram 38, Estrangement: you reached a conclusion from a distance, and the figure fills its lines
with strange sightings — one of them a stranger who turns out to be kin. Flat claim: the tabletop
hub is a conclusion drawn from architecture, not from running code. Nothing has ever talked through
these seams at runtime, and the council is about to spec the seams before any two layers have met.
Three breaks, each checkable. First, the home: three board battles name sprout as the game's repo,
yet sprout is absent from `council/repos.yaml` and not cloned here — the council is designing for a
game it cannot currently open. Second, the decorative risk: a rules layer that resolves nothing the
story needs is furniture, and the slice is the cheapest place to catch that. Third, the scheduling
truth: the zo-guards keep scheduled work blocked until tomorrow's race test and quota wiring pass;
this pass and the spec are permitted local dev under `zo-division`, but the moment the slice build
becomes a scheduled loop, the gates bind. Falsification, two tests that only work together: the
slice's exit test is the sprout slice's own standard (mh3-card-in-playtest) — a playtester can say
why the edge changed without being told; and the substrate-removal test — if the slice plays
identically with the rules surface stubbed out, the substrate is not load-bearing and the slice has
failed. Verdict: support with conditions — the falsifiers are the definition of done, not
decoration.

## Regent: 54 Home Field Advantage, no changing lines

Hexagram 54, Home Field Advantage: you are following rules nobody told you — entering an
arrangement made before you arrived. That is literally this pass's position: the ontology and the
lifecycle decision were laid down while Sprout was already being built, and the slice must enter
that house on its terms. What must be preserved: the 2026-10-12 decision (unanimous, genre-portable
with tabletop as a named stress test) supplies the slice's state model — `EncounterDefinition` and
`EncounterOccurrence`, `MoveDefinition` and `MoveInvocation`, `QuestDefinition` and `QuestInstance`,
`CompletionContract`, and independent state axes instead of one overloaded `status`. The slice must
not invent vocabulary: anything the seams need that v0.1 lacks goes through `term_pass`, and the
2026-06-24 lesson stands — invented fields are face-saving, not design. Reserved to Wendell: repo
home, registration, money — so where the substrate lives is his, with the full list of options and
consequences on the board. Definition of done for this pass: the pass file, the ledger record with
casts, the board rows, and a chat reply that says what changed and names the rows. Phase gate: the
spec kit opens only after he rules on the substrate home, and the slice compiles only in the repo
he names. Standing test: every change of state in the slice's design has its decision-log entry —
the spec kit is where this pass's recommendations get theirs.

## Diplomat: 16 Anticipation, becoming 8 Alliance

Hexagram 16, Anticipation, changing into 8, Alliance: the good part has started and the event has
not, and preparation and pleasure are the same motion. Who is excluded by the slice as proposed:
nobody yet, because the first audience is Wendell himself — designer-as-player makes the onboarding
question `not_applicable` for v0, and that is a fact to record, not an omission to paper over. What
the community will accept, when they meet it: a slice that is watchable — a screen he can hand to
someone — which is the bridge between a contract test and a demo. The bridge that makes the layers
one household is the same as yesterday's: verified assets do the arriving, and the substrate fills
the hollows that already exist rather than digging new ones. Water on earth touches at every point
along the surface — so the seam contracts should be written as the thinnest interfaces that make
the four calls possible, not as a framework. Recommendation: reuse beats rebuild everywhere a
verified asset exists; the slice forks nothing, and the trust screen already rendering the reducer
is the proof the encounter seam can borrow its face. Standing test: the slice should be
explainable in one sentence to a stranger — one day, one choice, one consequence they can see.

## Sage: 42 Windfall, becoming 9 Restraint

Hexagram 42, Windfall, changing into 9 Restraint: more is arriving than you put in — one of the few
figures that says yes — and what it becomes is a small rule you never revisited holding all of it.
That is exact: the substrate-home question is the small unvisited rule, and it holds everything
downstream, so it goes to the board before the spec kit opens. The smallest coherent whole
resolves in this order. The Regent's gate stands first: he rules the home; the spec opens after.
The Architect's topology stands second: one of each seam, the slice as the spec's executable
section. The Challenger's falsifiers stand third and are the exit test, not decoration: the player
names what changed, and the substrate survives its own removal test. The Shaman's felt moment
stands fourth as the acceptance test: he plays one day and says whether it landed. The Diplomat's
reuse stands fifth as the build method: verified assets, thinnest interfaces, nothing forked.
Retained from every face; nothing dropped. The dissent is carried as conditions, not rejection:
three faces bound their support, and the conditions are recorded in the positions. Recommend, and
do not decide: the slice named below, the spec kit from `council/spec-kit/` in the repo he names,
and the board question answered first.

## Verdicts

| Face | Verdict on "what should exist in the biggest slice" |
|---|---|
| Shaman | One felt moment — labor becoming story without a dashboard — is the acceptance test. |
| Architect | Biggest = every seam once: one day, one passage, one encounter, one resolution, one commit. |
| Challenger | The falsifiers are the definition of done; sprout's absence from repos.yaml is a real break. |
| Regent | Ontology first-class objects are the state model; no invented vocabulary; home is his. |
| Diplomat | Reuse beats rebuild; thinnest interfaces; first audience is Wendell, and the slice stays watchable. |
| Sage | Home question first, then the spec kit; the slice is one of everything, bound by the lifecycle grammar. |

## Dissent check

The pass is not unanimous: no face opposed, but four of six set conditions (Shaman: the felt moment governs;
Architect: topology fixes size; Challenger: falsifiers are the definition of done; Regent: the home
gate precedes the spec). Conditions are recorded in the positions below, and the unanimity flag
does not apply.

## Outputs

### Positions (no ruling from Wendell needed; stand unless he flips them)

| id | faces | Position | Citation |
|---|---|---|---|
| `slice-contract` | architect, sage, challenger | The slice is one of each seam — one day cycle, one narrative passage fired by a world predicate, one encounter on the trust reducer, one tabletop resolution, one sleep commit. "Biggest" is topology: every seam once. Content volume adds no contract signal. | QUICKSTART counterweight "smallest meaningful loop"; Wendell's four-layer contract of 2026-10-16; trust-encounter-loop plan. Pass: `council/passes/6FACE_PASS_slice1_2026-10-16.md` |
| `slice-ontology-types` | regent, architect | The slice's state uses the 2026-10-12 decision's first-class objects — EncounterDefinition/Occurrence, MoveDefinition/MoveInvocation, QuestDefinition/QuestInstance, CompletionContract, independent state axes — and v0.1 vocabulary only. A term the seams need that v0.1 lacks goes through `term_pass`. | Unanimous ontology decision, `ontology/v0.1/source/council-phase-a/completion-boundaries/council-decision.md`; `faces.yaml` term_pass; the no-invented-fields lesson of 2026-06-24. Pass: same file |
| `slice-falsifier` | challenger, shaman | The slice passes when a playtester says what the rules resolution changed about the story without being told, and fails if it plays identically with the rules surface stubbed out. The felt acceptance test is Wendell playing one day. | The sprout slice exit test (board question `mh3-card-in-playtest`); constitution 5, "mechanics claim reality." Pass: same file |
| `slice-reuse` | diplomat, architect | The slice builds only on verified assets — trust reducer, walkable sprite slice, twine IR compiler, world-state-provider pattern — forks none of them, and writes the seam contracts as the thinnest interfaces that make the four calls possible. | Battles fr-scene-staging and fr-cave-studio; `trust-encounter-loop/plan.md` (deterministic-over-AI, contract-before-UI). Pass: same file |

### Question (passed the reach test)

**`slice-substrate-home`** (owner: Regent, with the Architect). Where does the engine slice and the
tabletop rules substrate live?

- **bars-engine.** Everything the slice needs is local and verified — the slice could compile
  today. Consequence: fastest tire-kicking; risk: Sprout's identity and the ontology-game content
  dilute inside a large repo with its own product surface.
- **sprout.** The battles name it as the game's home; the slice lands where the game lives.
  Consequence: no setup detour later; risk: sprout is not in `repos.yaml` and not cloned here, so
  setup and registration come before any code moves, and the council gains no local access until it
  is registered.
- **A new registered repo for the substrate, Sprout and bars-engine as first clients.** The
  contract gets a clean home the ontology governs from day one. Consequence: the cleanest long-term
  shape; risk: a new repo is standing infrastructure — money and maintenance are reserved to him,
  and the start is slowest.

*Why only he can answer:* repo home, repo registration and standing infrastructure are reserved to
him, and his rule requires the full list with consequences before infrastructure changes.
*Why not before:* the four-layer contract was first named in chat on 2026-10-16, no pass has ruled
on where an engine substrate lives, and sprout's absence from `repos.yaml` was only noticed today.

## Tests set for the next pass on this subject

1. **`slice-exit-test`** (Challenger, due when the slice is playable): both falsifiers run against
   a playable build — the player names what the resolution changed without being told; the slice
   does not play identically with the rules surface stubbed out. Pass: both hold. Fail: the
   substrate is decorative and the slice is rebuilt around a stake only the rules layer can resolve.
2. Carried, unchanged: **`zo-race-test`** and **`zo-quota-wiring`** (due 2026-10-17). Scheduled
   work stays blocked until they pass.

## Record block

- **Date:** 2026-10-16. **Called by:** Wendell, in chat.
- **Question:** the biggest slice that tests the four-layer engine contract, decided by the six
  game master analysis plus the ontology.
- **Verdicts:** Shaman: the felt moment is the acceptance test. Architect: biggest is topology —
  every seam once. Challenger: the falsifiers are the definition of done. Regent: the ontology's
  first-class objects are the state model; the home is his. Diplomat: reuse beats rebuild; thinnest
  interfaces. Sage: home question first, then the spec kit.
- **Board rows:** four positions (`slice-contract`, `slice-ontology-types`, `slice-falsifier`,
  `slice-reuse`), one question (`slice-substrate-home`).
- **Ruling:** pending.
