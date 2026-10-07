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

Answers (Wendell, 2026-10-07, in the thread):

> Texts can propose daemons of their own. We want to only do this if they don't fit into the existing structure OR as
> a subclass of daemon
>
> Parallel milestones but the idea of milestones is the same as sprout is essentially me writing the emotional
> alchemy text through game design
>
> Council daemon playtesters, me, and any other play testers I bring in for feedback
>
> Specifically if I can get authors to donate their books the authors can be play testers as well

- A text may propose a daemon only when a habit fits none of the existing daemons, or as a subclass of one. The
  translation table comes first; a new daemon is the exception and must say why no existing one fits.
- A text's milestones run as a parallel track beside Sprout's story milestones. They are the same kind of thing:
  Sprout is Wendell's emotional alchemy text written as game design. So Sprout is this process's first worked
  example, run on his own text, and its design record is a reference for steps 1 to 3.
- Playtesters: the council's daemon playtesters, Wendell, and anyone he brings in.
- Authors who donate their books can playtest their own campaign. That ties the process to permission from the
  author for each text it uses beyond private testing (inferred; not yet asked).
- Still open from round 4: what counts as proof that a campaign taught the technique.

### Round 5 (2026-10-07)

1. **Proof.** What tells you a campaign taught the technique: the author recognising their technique in play, the
   player doing it in a real conversation afterwards, a check inside the game, or a mix?
2. **Holes (step 2).** Is a hole a skill the text assumes but never teaches? Egan, for one, assumes the helper can
   manage their own reactions while listening. Sprout's core loop would fill that with emotional alchemy.

Answers (Wendell, 2026-10-07, in the thread):

> A campaign taught the technique of they are able to use it in the game context AND d they are able Tod
> demonstrate mastery by using the techniques in the outer world and proving it (merit badge style)
>
> 10) yes. Emotional alchemy and removing inner blocks is the fundamental technique that I believe is the reason
> many people don't out personal development books into practice

- Proof needs both: the player uses the technique in the game, and then shows mastery in the outer world with
  proof, merit badge style. In-game success alone does not count.
- Sprout's merit badges today come only from in-game counters (`pr-merit-from-practice`). An outer-world badge
  is new and needs a way to verify it.
- A hole is a skill the text assumes and never teaches. The main hole in most texts is emotional alchemy and
  removing inner blocks, which Wendell believes is why people don't put personal development books into practice.
  Sprout's core loop fills it. This is the process's thesis: every campaign carries the text's techniques plus the
  emotional alchemy needed to actually use them.

### Round 6 (2026-10-07)

1. **Who verifies an outer-world badge?** The player's own word with a written reflection (a BAR in bars-engine),
   a witness such as the person they helped, or a reviewer such as the author or a coach?
2. **"Beliefs" in step 1.** Are they the author's beliefs the player comes to hold (Egan's "the client is in the
   driver's seat"), or the limiting beliefs that block practice, which would become daemons and inner blocks? Or
   both, sorted into two lists?

Answers (Wendell, 2026-10-07, in the thread):

> I do think a BAR artifact is really good proof. A player in the game can collect these artifacts as well. If done
> in a coaching container the coach validates the BARs
>
> We're pulling out the authors beliefs and the beliefs they want the readers to install by reading the text. The
> blocking beliefs will all be the self-sabotage beliefs of mastering allyship and other emotional alchemy based
> texts (like flirtcraft)

- Outer-world proof is a BAR. Players collect their BARs in the game. In a coaching container the coach validates
  each BAR; outside one, the BAR stands on the player's word (inferred; not yet asked who validates outside
  coaching).
- Step 1 pulls the author's beliefs and the beliefs the author wants readers to take on. It does not pull blocking
  beliefs from the text.
- Blocking beliefs come from one shared source: the self-sabotage beliefs of *Mastering Allyship* and other
  emotional alchemy texts such as flirtcraft. bars-engine already carries a list in its quest grammar
  (`src/lib/quest-grammar/emotional-alchemy.ts`, the shadow voices: not ready, not worthy, not good enough, not
  capable, insignificant, don't belong; unpacking question Q6). So the text supplies the technique and the beliefs
  to install, and the emotional alchemy canon supplies the blocks, the same way it supplies the daemons.

### Round 7 (2026-10-07)

1. **Teachers (step 2).** Does each text get its own teacher NPC who carries the author's voice (an Egan-like
   mentor), or do Sprout's existing cast (Pip, Captain Rue, Mother Ede) teach the text's track?
2. **Who runs the steps.** Does a model draft each step and you review it (like bars-engine's book quest review),
   or are some steps done by hand? The community's allergy to AI and bars-engine's non-AI track may bear on which.

Answers (Wendell, 2026-10-07, in the thread):

> Teacher NPC that carries the voice. If there is an existing character that can hold that voice prioritize that.
>
> What do you mean by carry out the step?

- Each text gets a teacher NPC who carries the author's voice. An existing character who can hold that voice comes
  first; a new character only when none can.
- Question 2 was unclear. Restated in round 7b.

### Round 7b (2026-10-07)

2. **Who does the work of each step, restated.** For *The Skilled Helper*, someone has to read the book and write
   the list of milestones, lessons and beliefs (step 1), draft the story and the teacher's lines (step 2), and write
   the daemon translation table and the spirits (step 3). For each, who writes the first draft (a model, Wendell,
   or the author), and who checks it before it goes into the game?

Answers (Wendell, 2026-10-07, in the thread):

> The model writes I validate and if we have access to the writer (which we won't especially for public domain and
> free texts which this is designed to ingest) we can get their final approval. The final approval is a way to pitch
> to authors deals for licensing

- A model writes every step's first draft. Wendell validates it.
- When the author can be reached, the author gives final approval. Usually they can't be: the process is designed
  to ingest public domain and free texts.
- Author approval doubles as the pitch for a licensing deal.
- Tension to resolve: the two first texts, *The Skilled Helper* and *Integral Life Practice*, are in copyright,
  and the process is designed for public domain and free texts.

### Round 8 (2026-10-07)

1. **The first text and copyright.** Does *The Skilled Helper* run as a private test until there is a licensing
   deal, or should the first campaign anyone else plays come from a public domain text?
2. **The first test's size.** Is the first run a thin slice (one milestone, one teacher, one spirit, one daemon's
   translation, one BAR badge), played through step 4 before the rest of the book is translated?

Answers: waiting.
