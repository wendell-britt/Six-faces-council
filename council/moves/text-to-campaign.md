# The text-to-campaign move

A move the council runs to turn one section of a personal development text into playable content in Sprout's world.
It runs Wendell's four steps, one section at a time, with a model drafting each step, Wendell validating on the
Council Board, and the author approving when reachable. It is built to spend as few tokens as the work allows.

## The ask, in his words

Wendell, 2026-10-07, in the project thread "Texts into game campaigns", the four steps:

> Step 1) pull the milestones lessons and beliefs from the text
> Step 2) translate these milestones into story including NPCs that will teach the players. Identify any holes in
> the techniques that need to be supplemented by the core game loop of sprout game
> Step 3) create daemon spirits that can be in the random encounters to teach the players the techniques
> Step 4) run players through the game and see if it teaches the techniques and milestones

Later that day, in the thread that designed this move:

> Ok next I want to figure out how we can leverage the 6 game master council to steward the texts to content
> pipeline in a deft and token efficient way

The interview that settled the process is `council/interviews/text-to-campaign.md`. The pass that designed this move
is `council/passes/6FACE_PASS_text-to-campaign1_2026-10-07.md`. Its first run is the introduction of *The Skilled
Helper* (interview round 8).

## Where it comes from

Nothing here is new machinery. Each part reuses something already in the record:

| Part of the move | Source |
|---|---|
| One section at a time | bars-engine `book-quest-targeted-extraction`: a table of contents and section-tagged chunks, so analysis pays only for the sections it needs. The whole-book run of `library-quest-pipeline` gave *The Skilled Helper* zero quests. |
| A model drafts, a person approves | bars-engine `book-quest-draft-review` (draft, then approved) and interview round 7b |
| A named steward per adaptation, credit on every surface | bars-engine `book-cyoa-stewardship` |
| Owning faces and a gate per step | `council/pipeline.yaml` stages |
| One step per session | CLAUDE.md, short sessions |
| Daemon playtesters | Sprout's demo rounds (`council/passes/6FACE_PASS_sprout-demo13_2026-10-07.md`) |
| Daemons shared, spirits per text, blocks from the emotional alchemy canon | interview rounds 3, 4 and 6 |

## The unit of work

**The unit is one section of one text.** A section is a chapter, or a smaller part of one when the chapter is long. The first is
*The Skilled Helper*'s introduction. Each section runs steps 1 to 4. A later section reads the files the earlier ones
left (the teacher, the translation table) and adds to them; it never starts over.

## The files a section leaves

Each step writes one file, and the next step reads that file instead of the book or the earlier thread. The files
live with the campaign, in Sprout, under `campaigns/<text>/<section>/`.

1. `extract.yaml`: milestones, lessons, the author's beliefs, the beliefs the author wants readers to take on, and
   the named techniques. Each item cites its page and paraphrases; none quotes more than a line (round 8).
2. `story.md`: the teacher NPC (an existing character first, round 7), who comes for help (villagers and spirits,
   round 3), the milestone track beside Sprout's (round 4), the holes Sprout's loop fills (round 5), and every asset
   the section adds or changes, including any new place (round 9).
3. `encounters.yaml`: the text's translation table onto the shared daemons, with a new daemon only when none fits
   or as a subclass (round 4); the text's spirits; the blocking beliefs, taken from the emotional alchemy canon and
   never from the text (round 6).
4. `playtest.md`: who played, which techniques were used in the game, and the BARs that prove them outside it
   (rounds 5 and 6).

## The four steps

Each step is its own thread. Each has one owning face that drafts and one checking face that reads the draft
against its standing test. The other four faces stay out of it; the full council meets once, when the section
closes.

| Step | Owner | Checker | Model | Reads | Writes |
|---|---|---|---|---|---|
| 1. Extract | Architect | Shaman | Sonnet | the section's text | `extract.yaml` |
| 2. Story | Shaman | Diplomat | Opus | `extract.yaml`, Sprout's design record | `story.md` |
| 3. Encounters | Architect | Challenger | Opus for a text's first section, Sonnet after | `extract.yaml`, `story.md`, the daemon canon | `encounters.yaml` |
| 4. Test | Challenger | Regent | daemon playtesters on the smallest model; Wendell and his testers | the built content | `playtest.md` |
| Close | Sage, with all six | | Opus | the four files and the board | the pass and a ledger record |

The model column follows CLAUDE.md: reading and recording on Sonnet, new design and first story drafts on Opus,
daemons on the smallest model.

What each checker asks:

- **Shaman on step 1:** are the beliefs the author's own, and are blocks left out (round 6)?
- **Diplomat on step 2:** does the teacher speak in the game's words and not the author's (round 8), and would a
  player who has never read the book follow it?
- **Challenger on step 3:** does every daemon in the table stay the shared daemon, with the text's variety inside
  it (`lesson-challenger-shared-frame`)?
- **Regent on step 4:** did the test count technique used in the game and a BAR outside it, both (round 5)?

## How Wendell validates

**Each step's file reaches him as a board position that stands unless he flips it.** This is the board's own rule
for council output, and it is round 7b's "the model writes I validate" done where he already looks. The
bars-engine drafts for *The Skilled Helper* waited in an admin page nobody opened, and were never approved (round 2).

**The next step does not wait for him.** Design work is not gated (`lesson-challenger-gate-release`). Every step
thread pulls the board first (CLAUDE.md), so a flip on step 1 reaches step 2 before it builds on it, and a flip
after that is a change to the next file, not a restart.

**What does wait for him:** anyone outside his own testing playing the content, and anything that names the author
or the book on a player's screen (`reserved` in `council/faces.yaml`). Those are board questions.

**The author approves when reachable** (round 7b). The section's close puts the four files and the playtest in
front of the author as one package, which is also the licensing pitch.

## What keeps it cheap

- **The book is read once per section**, at step 1. Every later step reads files a few pages long.
- **A step thread reads this file, its input files and the board**, and nothing else. It does not read the
  interview or another step's thread.
- **Two faces per step, six per section.** The full pass runs once, at the close.
- **Later sections reuse.** The teacher and the translation table carry forward, so step 3 drops to Sonnet after
  the first section.
- **Each step thread names its cost** in its last report (CLAUDE.md). There is no budget number until the first
  section is measured; the close proposes one on the board.

## Copyright

The campaign is game content built from Wendell's notes and applications of a text (round 8). In every file:
paraphrase, never quote more than a line, and keep the author's name and the title to a credit line. Before
anything is sold or published, a lawyer looks at it. This is the council's reading, not legal advice.
