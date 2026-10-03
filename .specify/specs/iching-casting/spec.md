# Spec: Every agent casts the I Ching

## The ask

> "Ok next piece is that all agents should be casting the I Ching and using its wisdom to inform their
> decisions (not unlike flirtcraft)"
>
> Wendell, in chat, 2026-10-03.

**Who it is for:** Wendell, through every pass in every council repo, and every face and daemon in it.

## Purpose

Before an agent argues or works a problem, it casts one hexagram. It names the hexagram and its two
trigrams, and says in one or two sentences how the hexagram's image bears on its decision. The cast and
what it informed go into the pass and the ledger.

## Design decisions

| Decision | Choice | Whose |
|---|---|---|
| Who casts | Every agent: each of the six faces, and each daemon a face sends | Wendell ("all agents") |
| How a cast is drawn | One hexagram drawn evenly from the 64, as flirtcraft's draw does, with a cryptographic random source | Wendell ("not unlike flirtcraft"); the council read flirtcraft's draw |
| What the cast carries | Number, Chinese name, pinyin, lines, and the two trigrams with their traditional names and qualities, from `council/iching/hexagrams.yaml` | Council. The table was read from flirtcraft's `lib/decks.json` and checked line by line against the trigrams |
| Flirtcraft's card readings | Not copied. Wendell ruled on 2026-09-09 that the subscription sells the cards, and the council's repo is public. Whether to bring them in is a board question | Wendell's ruling; board |
| Daemons | The face casts for each daemon it sends and passes the cast in, so daemons stay read-only | Council, from pass six's capability position |
| Inform, not decide | A cast shapes how an agent frames and weighs its argument. The evidence the agent cites still has to hold | Wendell ("inform their decisions") |

## Reserved items

Nothing here is reserved.

## How we will know it failed

- **The risk:** the reading is decoration, a sentence bolted onto an argument that would have been the same
  under any hexagram.
- **The cheap test, run before building further:** one daemon, the Protector serving the Challenger, works
  one real open problem (the deploy alert from flirtcraft pass one) three times, under three different
  casts. Its reports leave out the hexagram's number and name. A separate judge receives the three reports
  shuffled and the three casts, and matches each report to its cast.
- **Pass mark, set before the run:** the judge matches all three correctly. The chance of doing that by
  luck is one in six.
- **The result that stops the work:** any mismatch, which would mean the cast does not change what the
  agent does.

## Result of the test, 2026-10-03

**It passed against the pass mark set before the run.** The casts were hexagram 1 (The Creative), 18 (Work
on What Has Been Spoiled) and 5 (Waiting). The judge matched all three reports to their casts.

**One tightening was made before judging, and it made the test harder.** Each report's opening section on
the cast gave its hexagram away, and one named its trigrams against its instructions. The judge received
the reports with that section removed, so a match had to come from the work itself.

**The limits, recorded with the pass.** The judge rated its confidence medium to low and said two of the
three could have been swapped. All three reports reached much the same five moves. The cast changed how the
daemon framed and weighed the problem more than what it proposed. The clearest change came under Waiting:
that daemon held the build back until the channel that reaches Wendell is known. One test with a one in six
chance of passing by luck is a start, not proof, so the next three passes record their casts and the
Challenger grades whether any cast changed an output.

## Definition of done

- [x] The test passes, and its result is recorded here.
- [x] `council/iching/hexagrams.yaml` and `cast.py`, synced to every council repo and installed by `install.py`.
- [x] The skill's pass shape: every face casts first, and casts for each daemon it sends.
- [x] Each daemon report opens with a section on its cast, and `check_report.py` requires it.
- [ ] Ships as a board position that merges on the next board read unless Wendell flips it.
