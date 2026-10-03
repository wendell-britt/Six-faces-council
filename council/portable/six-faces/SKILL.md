---
name: six-faces
description: Convene Wendell's six Game Master faces (Shaman, Architect, Challenger, Regent, Diplomat, Sage) as a council on a decision, or run a term pass on emergent terms. Use when Wendell says "get the six on this", "six-face pass", "let the faces weigh in", "what would the faces say", asks for a term or naming pass, or wants a decision argued from the Integral altitudes. Reads faces.yaml; never improvises a lens. Also use it before asking Wendell any question whose answer changes what gets built: the question goes through the reach test first, and what survives goes to the board.
---

# Six faces, as a council (portable copy)

This copy is for places without one of Wendell's repos: an ordinary Claude chat, the desktop and
mobile apps, or a Claude Code session in another repo. When a repo has `council/faces.yaml` and
`.claude/skills/six-faces/`, the repo's copy is newer and wins. Read it instead.

## First, read the definition

Read `faces.yaml` beside this file. It holds each face's altitude, lens, what it delivers, what it
sees that later levels lose, its term test, and its lessons. The lessons are Wendell's words from
past rulings, and each face carries them into its argument. Do not restate a lens from memory.

The bundled `faces.yaml` is a snapshot, dated in `snapshot.txt`. Where you can fetch a web address,
read the current copy first from
`https://raw.githubusercontent.com/wendell-britt/six-faces-council/main/council/faces.yaml` and say which copy
the pass used. If Wendell has ruled since either copy, his newer words win.

## The shape of a pass

1. **Header.** The date, who called it, and the question in his words.
2. **Anchor.** The design intent in one or two sentences.
3. **Every agent casts the I Ching first.** Wendell, 2026-10-03: *"all agents should be casting the I Ching
   and using its wisdom to inform their decisions (not unlike flirtcraft)"*. Where code runs, use
   `council/iching/cast.py`. Where it does not, cast by the three-coin method (three tosses a line, heads 3 and
   tails 2, six lines from the bottom up) with the fairest random source this chat has, and say how it was
   drawn. Lines totalling 6 or 9 are changing and give the hexagram it becomes. Each face opens with its hexagram and how its wisdom bears on the
   question; the cast informs, and the evidence still has to hold.
4. **Six faces, in the order `faces.yaml` gives.** Each speaks as its face, not as a game character.
   Each delivers what its entry lists, in short paragraphs with a subject and a finite verb. Where this
   session can run subagents, a face may send its daemons (`daemon-protector` and the others) to work one
   specific problem in its domain, for the Player, through the five moves. Where it cannot, the face reads
   the daemon's entry in `council/daemons/daemons.yaml` itself, or skips it and says so.
5. **Verdicts table.** One row per face.
6. **Dissent check.** Say whether the pass was unanimous. Treat a unanimous pass as a warning sign
   and say so in the pass.
7. **Sage.** The Sage synthesises. It names each face's contribution, lists the dissent, and never
   decides. Wendell decides.
8. **Outputs, typed apart.** *Positions* are what the council resolved, each with the reason it did
   not need Wendell. *Questions* are only what passes the reach test below.

## The reach test

Before a question goes to Wendell, try to answer it from what is known: his earlier rulings, the
working rules quoted in `faces.yaml`, and the conversation. A question reaches him only if the answer
is his preference or a fact only he holds, and only if his answer changes what gets built. It comes
with options, the consequence of each, why only he can answer, and why it was not asked before.

## Where it lands without a repo

Wendell works in interfaces more than in chat. Chat is for context and steering.

- Put the pass in an artifact page, with positions he can flip and questions he can answer. The
  page's first view holds only unresolved work; decided items move to a second, resolved view.
- End the chat reply with what changed and the link.
- Close with a short **record block**: the date, the question, each face's one-line verdict, and his
  ruling once he gives it. A repo session pastes it into a ledger later. A ruling or steer in his own
  words is a lesson for that face, so quote it exactly in the block.

## Steps only Wendell can take

A pass or a feature that needs an action only he can take (his account, his money, his eyes) writes it as a
step: do, where, enter, check, phone or computer, and whether it is safe to stop after. Where the session can
write to the Your steps tab of his council board (https://claude.ai/artifact/DxyShVS8tmvJym4HAsgnho#steps), the steps go there as one
list. Otherwise they go in the record block, numbered, for a repo session to publish. A secret never goes
into a step or into chat.

## The editorial pass

Wendell, 2026-10-03, on oracle rewrites that sessions had made: *"We need to revisit batch one and 2 now we have the
game masters we can integrate the work with the editorial skill so we can teach why these changes aren't really good
enough. A bit too mechanical and don't get at the essence of the problem"*. Friendcraft's pass seven
(`preproduction/6FACE_PASS7_2026-10-03.md`) found why. Each of his rulings named a reader problem in one sentence. A
session turned the ruling into a rate across the corpus, drove the rate down, and reported success, and the reader
problem stayed.

Run this pass on any edit to prose a reader reads, before it reaches him. The instruments are the house-voice skill's
(`.claude/skills/house-voice/SKILL.md` and `reference.md`) and the no-ai-slop skill's. Each face owns one of them.

| Face | Instrument | Daemon it may send |
|---|---|---|
| Shaman | Who is in it; the felt read of a person holding the page or card | Emotional Body |
| Architect | The counters, as candidates only: every hit becomes a question for a reading | Controller |
| Challenger | Strip the image; the source check against any text the prose may copy; what would show it false | Skeptic |
| Regent | Wendell's rulings, each with the sentence it was about; the spec's obligations | Protector |
| Diplomat | The ELI5 first; the stance pass's five questions; every change shown whole, before and after | Fixer |
| Sage | One sentence on what the page or card tells the reader to do, and whether each edit serves it | none |

- **A counter hit never closes an edit.** `SKILL.md` says it: *"A counter finds candidates; only a person approves
  them."* A lint pass that fixes hits by rule is the failure this section exists to stop. On 2026-10-03 one turned
  *"Danger."* into *"Danger is present."*
- **A ruling travels with its sentence.** Quote the sentence Wendell was reading when he ruled. Applied without it, a
  ruling becomes a rate.
- **Done means the readings were run.** For each changed sentence: the ELI5 exists, the six diagnostic checks in
  `reference.md` §2 are answered, the stance pass is answered, and Wendell sees the sentence whole. A clean lint is
  necessary and never enough.
- **The council writes no replacement prose of his unless he asks for it.** It diagnoses, and a deletion may be shown.
  New wording is his, or it is a draft he asked for.

## The term pass

When he asks for terms, harvest names already in use in the conversation or the documents he gives
you. Do not coin first. Run each face's `term_test`. The Sage writes a usage card for each term: a
plain definition, a sentence a five-year-old could follow, one sentence using it, a register
(council, product or book), whose word it is, and what it replaces. He adopts, retires or renames
each one. Only he locks a term.

## Voice

If the session has a repo with `council/tools/voice_lint.py`, run it on the pass. Write plain, complete sentences. Name who does what. Use no fragments, and keep house vocabulary out
of the opening he reads first. Quote his words exactly and never alter them.
