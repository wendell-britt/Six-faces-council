# Interview: personal development texts into a playable campaign

Wendell asked to be interviewed about a process that takes personal development texts or notes as input and
puts out a playable campaign (a series of quests and encounters) that, through play, builds the player's ability
to practice the text's techniques. These notes hold his answers so a later session can turn them into a spec.
Started 2026-10-07 in the project thread "Texts into game campaigns".

## His four steps, as he wrote them

> Step 1) pull the milestones lessons and beliefs from the text
> Step 2) translate these milestones into story including NPCs that will teach the players. Identify any holes in
> the techniques that need to be supplemented by the core game loop of sprout game
> Step 3) create daemon spirits that can be in the random encounters to teach the players the techniques
> Step 4) run players through the game and see if it teaches the techniques and milestones

## What the record already holds

- **bars-engine already tried step 1 on books.** `book-to-quest-library` turns personal development PDFs into a
  Quest Library ("reading books to become a better ally often becomes procrastination"). `library-quest-pipeline`
  records the yield: of 12 uploaded books, five were extracted with zero quests and *The Skilled Helper* gave zero
  quests. `book-cyoa-campaign` makes *Mastering the Game of Allyship* chapter 1 the reference adventure, with
  Wake Up, Clean Up, Grow Up, Show Up as the act structure and passage types (epiphany bridge, expository,
  storytelling, skill development).
- **Sprout keeps daemons and spirits apart.** Board row `ds-intersect` (fr-demo round 14, 2026-10-07): daemons are
  the player's own charges, spirits are the forest's. Befriending a spirit teaches the move that answers its paired
  daemon. Only Magic integrates a daemon or satisfies a spirit (`ds-strategies`). Daemons meet the player first in
  wild form on the strip, then at a story gate (`ds-two-meetings`). Pip and Captain Rue teach daemons in the
  watch house; Mother Ede teaches spirits at the gate (`ds-hunters-watch`, `ds-gate-teachers`).
- **Anastasia's campaign** is a coaching client's campaign in the coaching practice project. Its Zoom transcript was
  downloaded on 2026-10-07 (board read 1714, steps 1 and 2).
- **Council lesson:** ground a design in Wendell's named references and his own work (Root, the Allyship domains,
  *Mastering Allyship*) before inventing.

## Questions and answers

### Round 1 (2026-10-07)

1. **"Daemon spirits" in step 3.** Sprout now has daemons (the player's own charges) and spirits (the forest's).
   Does a text produce daemons, spirits, or a new kind that is both?
2. **The first text and who plays it.** Is the first run Anastasia's coaching transcript, played by Anastasia, or a
   published text (*Mastering the Game of Allyship*, say) played by many?

Answers (Wendell, 2026-10-07, in the thread):

> Texts should product spirits and daemons- they will probably be integrated as we keep developing
>
> The first text really should be one of the texts in the bars-engine attempt. Integral Life Practice and Skilled
> Helper are good first texts

- Step 3 makes both: a text yields spirits and daemons. He expects the two to merge as Sprout develops.
- The first text is *Integral Life Practice* or *The Skilled Helper*. Default taken: *The Skilled Helper* first,
  because its three stages and named micro-skills (tuning in, primary and advanced empathy, probing, summarizing,
  invitations to self-challenge) give step 4 something countable to test. Flip it and *Integral Life Practice* goes
  first.
- bars-engine already holds a step 1 draft of both: `.specify/specs/book-integration-analysis/diplomat-books.md`
  (*The Skilled Helper*, mapped to the Diplomat) and `shaman-books.md` (*Integral Life Practice*, mapped to the
  Shaman, including the 3-2-1 Shadow Process). `scripts/ingest-books-to-npc-constitutions.ts` makes the same
  pairing. `library-quest-pipeline` recorded zero quests for *The Skilled Helper*
  (262,000 words); `scripts/analyze-books-local.ts` later broadened the filter that had skipped the whole book.
  Wendell, round 2: drafts were created and never approved, so the quests are there.

### Round 2 (2026-10-07)

1. **Where the campaign lives.** Does each text become a region or arc inside Sprout's world (the village, the
   forest, its cast), or its own campaign that borrows only Sprout's loop?
2. **Helped or helping.** *The Skilled Helper* teaches someone to help another person. Does the player learn by
   being helped (an NPC walks them through the three stages), by helping (the player listens to and probes an NPC,
   daemon or spirit), or one then the other?

Answers (Wendell, 2026-10-07, in the thread):

> I believe they created quest drafts that didn't make it into approved but quests are there
>
> The campaign will live in sprout game world but we want to have the ability to create different game worlds for
> each book if we so choose.
>
> The player learns from helping

- Step 1 has raw material: bars-engine's unapproved quest drafts for *The Skilled Helper*. They live in the
  database, behind `src/actions/book-quest-review.ts`, and have not been read in this interview yet.
- The first campaign lives in Sprout's world. The process must also allow a separate world per book.
- The player learns by helping: the player is the helper, and someone in the world is the one helped.

### Round 3 (2026-10-07)

1. **Who comes for help.** Villagers, spirits, or both? Sprout's spirits already carry a need (Earth needs space,
   Water something returned, Fire the obstacle named), which reads like Egan's preferred picture.
2. **Daemons as the helper's own habits.** Egan's helper failures look like Sprout's daemons: the Fixer gives advice
   before the story is told, the Controller steers, the Skeptic interrogates instead of probing, the Victim takes
   on the other's distress. Is a daemon encounter in this campaign practice at catching one of those habits in
   yourself while you help?

Answers (Wendell, 2026-10-07, in the thread):

> Both spirits and villagers
>
> I think as a translation as Egan this holds, but we want to keep them separate so we can see how daemons connect
> to other texts

- Both villagers and spirits come to the player for help.
- The daemons-as-helper-habits mapping holds as a translation of Egan. The daemons stay their own set, kept apart
  from any one text, so the next text can be mapped onto the same daemons and the links compared. Reading taken:
  each text gets a translation table (this text's version of each daemon) and never redefines a daemon. Flip it if
  a text should be able to add a new daemon.

### Round 4 (2026-10-07)

1. **Milestones.** Sprout's story already runs on numbered milestones (1 to 6 in the demo). Does a text's milestone
   become one of Sprout's story milestones, or does it sit beside them as a separate track (a skill ladder for
   Egan's stages)?
2. **The test in step 4.** Who plays first: the council's daemon playtesters (simulated players, as in the Sprout
   demo rounds), real people, or one then the other? And what counts as proof it taught: the skill shown in the
   game, or shown in a real conversation afterwards?

Answers: waiting.
