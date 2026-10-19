# Running /better before work: what the test showed (2026-10-19)

Wendell asked what, aside from tokens, would stop us running the /better prompt two or three times on his
natural-language messages before work starts. We ran it twice, on Sonnet, in fresh workers, on that same message.

| Pass | Words in the brief | What it added |
| --- | --- | --- |
| His message | 45 | Research how this fits our flows; what stops 2 or 3 runs |
| 1 | 453 | A sample of 15 to 20 past messages, an A/B test, a drift diff, a stopping rule, cost per placement |
| 2 | about 850 | Pre-registration, two independent coders with agreement scores, 4 to 6 matched-pair rebuilds, blind judges, a base-rate gate |

Each pass found one good idea: pass 1 a stopping rule and a drift check, pass 2 "measure how often short messages
start bad threads first; if rarely, stop". Each pass also roughly doubled the scope, and by pass 2 his words were gone
from the brief.

What stops repeated passes, beyond the rewrite's own tokens:

1. Scope compounds. "Deeper, not bigger" holds for one pass at best; the second deepens the first pass's additions.
   This collides with the brief rule (add no deliverables he never named) and with the tool ladder (extra variants are
   not scope).
2. His voice is replaced. A rewritten brief no longer carries his words, which breaks "never alter his quoted words"
   and makes later threads work from Claude's reading of him.
3. It grades itself. A second pass judges the first with the same model and no outside evidence; the outside check
   in question (4) only exists once work runs.
4. The pause becomes a chat question. The gist waits for a go-ahead in chat; our questions go to the board, and auto
   pickup must not stall.
5. The real cost is downstream. A brief twice as big makes a longer thread, and carried context is 90% of spend
   (usage audit 2026-10-18). The rewrite itself costs cents.

What we adopted: `.claude/skills/better/SKILL.md`, one pass at the start of build, design and research threads, his
words kept on top, answers (2) and (4) kept whole, answer (1) filtered by rung 1 of the tool ladder, any pause sent to
the board.

Not checked: whether one pass improves thread outcomes. That needs a few real threads run with it; count his
corrections in their first replies against threads run without it.
