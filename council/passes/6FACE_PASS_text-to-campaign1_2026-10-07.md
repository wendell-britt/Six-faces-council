# Stewarding the texts-to-campaign pipeline: a six-faces pass

**Run 2026-10-07**, called by Wendell in the project thread at 19:29 UTC. This is the first pass on the pipeline; the
interview that came before it (`council/interviews/text-to-campaign.md`, #51) was its intake.

**The ask, in his words:** "Ok next I want to figure out how we can leverage the 6 game master council to steward the
texts to content pipeline in a deft and token efficient way"

**The board was pulled first** (`board/pull.py`): every saved answer was already recorded. `council/due.py --ahead 7`
lists nothing due.

**Inputs:** the interview's nine rounds; retro 1 (`council/passes/6FACE_RETRO1_2026-10-07.md`), above all
`lesson-architect-sources` and `lesson-challenger-gate-release`; CLAUDE.md's short-sessions rule; `council/pipeline.yaml`;
and five bars-engine specs that already tried this on books: `book-to-quest-library`, `library-quest-pipeline`,
`book-quest-targeted-extraction`, `book-quest-draft-review` and `book-cyoa-stewardship`, with
`book-integration-analysis/diplomat-books.md`, a whole-book summary of *The Skilled Helper* from March.

## Scorecard

No earlier pass on this subject set tests. Retro 1's first test applies to every pass from now on: no design without
the sources it should have named. This pass names its sources in the move's table, and invents only the four step
files.

## The anchor

A model drafts each step of turning a text into Sprout content, Wendell validates on the board, the author approves
when reachable (interview, round 7b). The council's job is to make each step cheap to run and cheap for him to check.

## The casts

Drawn with `council/iching/cast.py`, three coins each; the ledger carries them under `casts`.

| Face | Hexagram | Becomes |
|---|---|---|
| Shaman | 53 Emergence: *This has stages, and you are trying to skip one.* | 39 Impasse: *The direct route is closed and you have asked nobody.* |
| Architect | 61 Incubation: *What is true here is still inside the shell.* | no changing lines |
| Challenger | 46 Ascent: *This is growing at a rate you cannot see day to day.* | 18 Stale Air: *This went off from being left alone.* |
| Regent | 46 Ascent | no changing lines |
| Diplomat | 18 Stale Air | no changing lines |
| Sage | 34 Vigour: *Force is available here and unaimed.* | 40 Thaw: *The knot just loosened, and the window is short.* |

No daemons were sent. The record answered every problem the faces raised, and a pass about saving tokens should spend
none it does not need.

## Shaman

**The cast is Emergence, becoming Impasse.** A tree takes hold at the rate its roots allow, and the direct route is
closed to someone who asks nobody. The pipeline has stages that cannot be skipped, and the one most easily skipped is
Wendell's own application of the text.

**Round 8 sets what the content is made of:** "as though the content were developed based off of my notes of the text
and my own applications of the text". A model can draft notes on the text. It cannot draft his applications; only he
holds them. If step 1 runs on the text alone, the content is the model's reading of Egan, and the claim round 8 rests
on gets thinner.

**The felt sense of a step is in its checker.** The Shaman checks step 1 for one point: that the beliefs in the file
are the author's, and the blocks are left to the emotional alchemy canon (round 6).

**Recommendation:** ask him once how his applications enter step 1. Everything else in the move can stand.

## Architect

**The cast is Incubation, unchanging.** What is true is still inside the shell: bars-engine already built most of
this pipeline, and it failed in a way that says what to change.

**The sources, in the order retro 1 set.** His own systems first:

- `library-quest-pipeline` ran *The Skilled Helper* as one 262,000-word job and got zero quests.
- `book-quest-targeted-extraction` was the fix: a table of contents, section-tagged chunks, and analysis paid only for
  the sections it needs. Its stated purpose is "Reduce token waste".
- `book-quest-draft-review` made every model output a draft an admin approves.
- `book-cyoa-stewardship` names a steward per adaptation and credit on every player-facing surface.
- `council/pipeline.yaml` gives each stage one or two owning faces and a gate.
- Sprout's demo rounds already run daemon playtesters.

No game was named for this, so the third source, invention, covers only the four step files.

**The design: one section, four steps, four files.** The unit is one section of one text. Each step writes a short
file and the next step reads that file, never the book or the thread before it. The book is read once per section.
The move is `council/moves/text-to-campaign.md`.

**The token arithmetic comes from CLAUDE.md.** Its audit found 84% of spend was rereading context, and pass ten measured $0.14 a call
at 679,000 tokens. A step thread that reads the move, one or two short files and the board starts small and stays
small. The council does not put a number on it before the first section runs (council lesson: no number inferred on
his behalf).

**Recommendation:** the move as written, with the files kept in Sprout beside the campaign.

## Challenger

**The cast is Ascent, becoming Stale Air.** Growth too gradual to see from one day to the next, turning stale from
being left alone. Both halves describe the bars-engine drafts: generated in March, never approved, still in the
database (round 2).

**What breaks.** Validation by standing position means a flip can arrive after a later step has built on the file it
flips. The Challenger proposed that step 3 wait until step 1 has stood through one board read.

**What the record says about that proposal.** `lesson-challenger-gate-release` stands: gate a release on a test, never
the design work before it. The Challenger withdraws the gate and keeps the risk: every step thread pulls the board
first, so a flip reaches the next step before it builds. A flip after that changes the next file; nothing restarts.

**The test that could show the move is wrong:** slice one runs four step threads, each reading only the move, its
input files and the board, and each names its cost. If a step has to go back to the book or to an earlier thread to do
its work, the files are missing something and the move is wrong.

**The checker's job on step 3** is retro 1's shared frame: every daemon in the translation table stays the shared
daemon, with *The Skilled Helper*'s variety inside it. The Fixer gives advice before the story is told (round 3) is a
reading of the Fixer, not a new daemon.

## Regent

**The cast is Ascent, unchanging.** Steady increments; nothing to force.

**The non-negotiables, all from the record.** Paraphrase, never quote more than a line, and keep the author's name and
the title to a credit line (round 8). Anything that names the author on a player's screen, and anyone outside his own
testing playing the content, waits for his answer on the board (`reserved` in `council/faces.yaml`). Blocks come from
the emotional alchemy canon, never the text (round 6).

**Definition of done for a section:** four files, each a standing position on the board, and a playtest where a
technique was used in the game and proven outside it with a BAR (round 5).

**Who validates a BAR in slice one.** Round 6 says the coach validates in a coaching container. Slice one is played by
the daemon playtesters, Wendell and his testers (round 4), so Wendell validates as the coach. The open question from
the interview, who validates outside a coaching container, changes nothing until someone outside his testing plays,
and waits until then.

## Diplomat

**The cast is Stale Air, unchanging.** What spoiled was left alone, and the Diplomat's reading is where it was left:
an admin page at `/admin/books/[id]/quests` that he had no reason to open.

**The bridge is the board.** Each step's file reaches him as a position on the page he already reads, in the board's
plain shape: what the step made, and what flipping it would change. He validates by reading and flipping, not by
opening a fourth tool.

**The Diplomat checks step 2** for the two readers round 8 and the community note in bars-engine's CLAUDE.md care about:
the teacher speaks in the game's own words, and a player who never read Egan can follow the help they are giving.

**The author's package.** When an author can be reached, the close sends one package (the four files and the
playtest), which round 7b makes the licensing pitch. The bars-engine stewardship spec already sets credit fields
(title, steward credit, optional link) for it.

## Sage

**The cast is Vigour, becoming Thaw.** Force is available and unaimed, and the knot has just loosened. The interview
gave the pipeline its whole shape in one afternoon; this pass aims it at one section.

**Contributions kept.** From the Shaman, his applications as the input only he holds, which becomes the one question.
From the Architect, the move, the order of sources and the section as the unit. From the Challenger, the test that
would show the move wrong, and the risk of late flips, answered by the board pull. From the Regent, the
non-negotiables, the definition of done, and slice one's BAR validator. From the Diplomat, the board as the review
surface and the author's package.

**Dropped:** the Challenger's gate on step 3, withdrawn under `lesson-challenger-gate-release`.

**Dissent:** the Challenger still rates the risk of late flips higher than the Architect does. Both are recorded, and
slice one's costs will show which was right.

## Verdicts

| Face | The move as written | Two faces per step | Validation by standing position | Files in Sprout | Ask about his applications |
|---|---|---|---|---|---|
| Shaman | yes | yes | yes | yes | yes, the one question |
| Architect | yes | yes | yes | yes | yes |
| Challenger | yes | yes | yes, gate withdrawn, risk kept | yes | yes |
| Regent | yes | yes | yes, release still waits | yes | yes |
| Diplomat | yes | yes | yes, on the board, not an admin page | yes | yes |

**Dissent check:** unanimous on every column, which is a flag. The flag is answered in part: each column cites the
record, and the one real split (how likely a late flip is) is recorded above and is what slice one measures.

## Outputs

### Positions (stand unless Wendell flips them)

- **`ttc-move`**: the council stewards the pipeline with `council/moves/text-to-campaign.md`. Citation: the interview's
  summary, and the sources table in the move.
- **`ttc-section-unit`**: one section of one text is the unit, starting with *The Skilled Helper*'s introduction.
  Citation: round 8; `book-quest-targeted-extraction`; `library-quest-pipeline`'s zero quests from the whole book.
- **`ttc-two-faces`**: each step has one owning face and one checking face, and the full council meets once per
  section, at the close. Citation: `council/pipeline.yaml` stage owners; CLAUDE.md, short sessions.
- **`ttc-model-by-step`**: extraction on Sonnet, story and a text's first translation table on Opus, playtesters on
  the smallest model. Citation: CLAUDE.md, the model split.
- **`ttc-validate-by-position`**: each step's file is a board position that stands unless he flips it, and the next
  step does not wait. Release and anything naming the author wait for his answer. Citation: round 7b;
  `lesson-challenger-gate-release`; `reserved` in `faces.yaml`; the unapproved March drafts (round 2).
- **`ttc-files-in-sprout`**: the move lives in the council's home, and the section files and the spec live in Sprout,
  under `campaigns/<text>/<section>/`. Citation: rounds 2 and 4; the podcast move's precedent of a move at home and
  the product beside it. This answers the interview's open question on the spec's home.
- **`ttc-slice-bar-validator`**: in slice one Wendell validates BARs as the coach; who validates outside a coaching
  container waits until someone outside his testing plays. Citation: rounds 4 and 6.

### Questions

- **`ttc-applications`** (Shaman): how his own applications of the text enter step 1. Options:
  - **A. The model drafts from the introduction's text, and he adds his applications as a steer on step 1's
    position (recommended).** One read of the text, his words added where he already validates.
  - **B. He writes or dictates notes on the introduction first, and step 1 works from them only.** The content is
    most clearly his, and step 1 waits on him.
  - **C. The model drafts from the text alone, with no applications.** Cheapest, and the round 8 basis is thinnest.

  Why only he can answer: his applications are a fact only he holds, and the answer sets step 1's input. Why not asked
  before: the interview settled who writes (round 7b) but not what the writing is made from.

## Tests set for the next pass on this subject (set 2026-10-07)

1. **The files carry the work.** In slice one no step thread opens the book except step 1, and none reads another
   step's thread.
2. **Every step names its cost.** The close has four costs, one per step, and proposes a budget from them.
3. **The test counts both.** Step 4 shows at least one *Skilled Helper* technique used in the game and one BAR he
   validated.
4. **Flips are lessons.** Every flip on a step position becomes a line in the move, quoted, with its source.
