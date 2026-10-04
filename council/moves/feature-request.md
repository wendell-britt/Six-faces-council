# The feature request move

A move the council runs together when a feature request comes up. It turns an ask into a well-scoped project and a
spec kit. It runs in chat with Wendell, and it updates the Council Board when it is done.

## The ask, in his words

Wendell, 2026-10-04, in the Sprout Game project thread that started this move:

> So this is a good opportunity to test out a feature request process.
>
> This should be a move the council does together when something like this pops up.

> This should be something we can run in chat that updates the board after we are done. It's a form of the 6
> unpacking questions and a developmental use of 321

> The output of a process like this should be a well scoped project and spec kit

**This move is the one place a council question reaches him in chat.** The board rule in CLAUDE.md still holds for
everything else. Inside a run of this move, the 2 step is a dialogue, so its questions go to him in the thread, one
round at a time, and each answer is recorded as a ruling. When the run closes, its positions, any question left open,
and the spec kit's link go to the board. A question that comes up outside a run still goes to the board.

## The grammar: Mastering Allyship's three questions

Every run answers these three, in his words of 2026-10-04:

1. **Who is being helped?** Name the person, by role: the player, Wendell as maker, a playtester, a future session.
   Usually more than one is helped, and the run says whose need leads.
2. **What satisfaction are they looking for?** For the inner experience, name it as one of the Emotional Alchemy gold
   states (wonder, poignance, bliss, triumph, peace; flirtcraft GRAMMAR.md, ruled 2026-09-14 for wonder). For the
   outer experience, list the benefits a person will notice.
3. **What altitudes does the help need to operate at?** Each face carries an altitude in `council/faces.yaml`: Shaman
   magenta, Challenger red, Regent amber, Architect orange, Diplomat green, Sage teal. The run names the altitudes the
   help must reach, which also names the faces that own the work.

## The shape: 3-2-1, used developmentally

3-2-1 is the shadow process in Mastering Allyship (mtgoa-manuscript `appendices/APPENDIX_E_321_SHADOW_PROCESS.md`):
face it in the third person, talk to it in the second, be it in the first. Here the figure is the work that wants to
exist. It runs ouroboros style: what the 1 step learns by testing becomes the next run's "what's life like now".
Which unpacking question goes in which step is the council's reading of his message, and it stands as a position.

### 3: Face it (third person, journalistic)

The council describes the wanted work in the third person, in as much detail as it can, before anyone talks to it.
The journalistic questions organise it: who, what, when, where, why, how. Two of the six unpacking questions belong
here, and the council answers them from the record with citations:

- **What are we trying to create or experience?**
- **What is life like now?** A summary of the current state of the work, with file paths.

The 3 step also gives the council's first answers to the three grammar questions, marked as the council's, for him to
correct in the 2 step. It is written before the 2 step opens, as `request.md` in the feature's spec folder.

### 2: Talk to it (second person, the dialogue)

This is the back and forth in chat, where the council and Wendell understand the needs of the work in depth and the
charge around it. Every face casts the I Ching at the start (`python3 council/iching/cast.py ... --json`), as in a
pass. Four unpacking questions belong here:

- **What will that get us?** For the inner experience, the Emotional Alchemy satisfaction. For the outer experience,
  a breakdown of the benefits to the player.
- **How does it feel to live here now?** The player's current satisfaction with the work as it stands, and Wendell's.
- **What would have to be true for someone to feel this way?** The Emotional Alchemy and daemon analysis. A face may
  send the daemons it needs (see "Daemons" in the skill) to answer it for the player.
- **What reservations do you have about the creation?** Which of the six self-sabotaging beliefs are at play. The
  table below lists how each might show up in production; the run names the ones it finds, with evidence.

Rules for the dialogue:

- One round at a time. A round asks at most three questions, each answerable in a word or a line, each with the
  council's recommended answer marked. Anything the record can answer is stated as a position, not asked.
- The council talks to the work as well as to Wendell. A face may write a short exchange with the work in the
  second person ("You want to be playable. What do you need first?") where that surfaces a need the record misses.
- Each answer of his is recorded in `request.md` under the round, quoted, as a ruling.
- The 2 step ends when the three grammar questions and the four unpacking questions each have an answer he has seen,
  and he says to go on, or a round finds nothing new.

### 1: Be it (first person, embodied through testing)

The council embodies the work by testing it, before building it. The last unpacking question belongs here:

- **What are a few aligned actions toward this goal?** Each face gives its analysis as a game master, and the actions
  are the decisions those six analyses support.

The 1 step writes the spec kit (`spec.md`, `plan.md`, `tasks.md` from `council/spec-kit/`), then runs the cheapest
test that could show the design is wrong: the `falsify` stage of `council/pipeline.yaml`. The test's result is written
into `request.md` as the next run's "what is life like now". From here the feature runs the pipeline's stages from
`plan` onward.

## The six self-sabotaging beliefs, in production

The six beliefs are Mastering Allyship's. The pairings with daemons come from the retired Appendix G
(`mtgoa-manuscript/specs/retired/APPENDIX_G_BELIEF_TO_SUPERPOWER_MAP.md`), which calls them starting points. Wendell's
examples of 2026-10-04 were offered as examples, not canon: *"Everything the parenthesis are examples of how self
sabotage might manifest in a production pipeline or organization and not "canon" we might need to brainstorm better
fit exponents of the self-sabotage"*. The production column below is the council's proposal, and it stands on the
board as a position until he flips it.

| Belief | His example | How it shows in a production pipeline (the council's) | Daemon most active | The aligned standard |
|---|---|---|---|---|
| I'm not ready | Busywork getting in the way of the major impacts | Prerequisite chasing: one more research note, spec or tool before anything playable exists. The work stays on paper. | Protector | Ready enough to put one playable scene in front of a person. |
| I'm not capable | The product needs a new feature | Reaching for a new engine, tool or feature instead of using what already works, or handing the crux to someone else. | Fixer | Capable enough to build the smallest version with what exists, and report honestly. |
| I'm not good enough | The product isn't good enough | Polish loops: holding work back for a finish no player would notice, or redoing it instead of testing it. | Controller | Good enough to show, honest enough to fix what the test finds. |
| I'm not worthy | The product isn't valuable | Not asking for the resource: skipping the playtest because a person's time feels unearned, or cutting the scope before it is tried. | Emotional Body | Worth a person's hour, because the hour is how it gets better. |
| I'm insignificant | We're making marginal gains | Changes too small to show or to measure, so nobody sees them and nobody learns from them; waiting for someone else to make the change that matters. | Victim | Significant enough to show Wendell this change today. |
| I don't belong | The users aren't going to accept what we have | Copying reference games or genre habits instead of the game's own teaching, or hiding the teaching so it will not be rejected. | Player (the child at the centre in Appendix G) | It belongs to the work's own purpose, whether or not the genre ratifies it. |

## What a run produces

1. `request.md` in `.specify/specs/<feature>/`, from `council/spec-kit/request.md`: the 3 step, every round of the
   2 step with his answers, and the 1 step's test result.
2. The spec kit beside it: `spec.md`, `plan.md`, `tasks.md`, with the pipeline's three council sections filled.
3. A ledger record in the home repo's `council/ledger/`, with the casts, his rulings, and any lesson for a face under
   `lessons_pending`.
4. Board rows, on main: a position for each point the run resolved (each with the citation for why it did not need
   him), a question for anything left open, and the `[wendell]` steps on the Your steps tab.
5. A pull request in the feature's repo with the spec kit.

## Where it sits

The move is the front door to the feature pipeline. It produces what the `intake`, `spec` and `falsify` stages ask
for, and the feature goes on from `plan`. `feature_request` in `council/pipeline.yaml` points here.

## Runs

| Date | Feature | Repo | Record |
|---|---|---|---|
| 2026-10-04 | Scene staging: a scene script becomes a playable, animated slice | wendell-britt/sprout | `.specify/specs/scene-staging/request.md` |
