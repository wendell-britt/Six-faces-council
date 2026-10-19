# Six-face pass: sealed tasks read as BARs, pass 1

**Date:** the pass ran on 2026-10-19. **Called by:** Wendell, in the project chat at 23:38 UTC, routed to the thread "Tap the Vein on the board".
**Pass:** ttv-bars 1, the first on this subject. It follows ttv-loop 1 (`council/passes/6FACE_PASS_ttv-loop1_2026-10-16.md`) and the seed library passes.
**Ontology:** QUICKSTART, with its BAR scope, composting, roadblocks and disclosure sections (`ontology/manifest.yaml`, profile `default`; the
deeper `game_design` files were not loaded). **Daemons:** none sent. **Subagents:** none.

**The question, in his words:**

> We also need a way for the tasks generated in that board to be read and interpreted by the 6 game masters faces. Essentially the tasks
> should be able to be unpacked into language the council can use to prioritize the task and give advice on if it should be worked that day
> or deferred.
>
> this is essentially a head to head battle mechanic of prioriities. The tasks that emerge in teh free-write are what by subconcious says is
> relevant, the tasks being worked by the Council are ones that have more ergonimics to be worked on because they are context aware. I need
> the information from my subconcious to be context aware
>
> the interface structure I beleive is bars itself. When a council member is able to see a player produces bar and unpack it or gather more
> context until it's able to be worked. Then we are nearing what I'm looking for.

**Casts** (`council/iching/cast.py --json`, three coins):

| Face | Hexagram | Changing lines | Becomes |
|---|---|---|---|
| Shaman | 8 Alliance: "This is filling a hole you had before it started." | 3 | 39 Impasse: "The direct route is closed and you have asked nobody." |
| Architect | 64 Almost: "You are nearly there, and the last stride is where it gets wet." | 2, 5 | 12 Stalemate: "You are seeking one game and wearing the face of the other." |
| Challenger | 32 Endurance: "This exact exchange has happened before." | 6 | 50 The Cauldron: "This is being transformed, and you are carrying it by the handles." |
| Regent | 61 Incubation: "What is true here is still inside the shell." | 5 | 41 Spending: "This has a price and you have yet to name it." |
| Diplomat | 16 Anticipation: "The good part has started and the event has not." | none | none |
| Sage | 26 Reserves: "You have been storing this and never named the day." | 5 | 9 Restraint: "A small rule you never revisited is holding all of this." |

## Scorecard

ttv-loop 1 set four tests. T1 (the first emergence run, due 10-18) has not run: `COUNCIL_MENU_TOKEN` is still refused with a 401, and the
thread "Menu key retest" owns it. T2 (records per commitment, due 10-21) and T3 and T4 (due 10-23) are not yet due. The seed library's SL1
is due 10-30. None can be graded today. Every test in this pass names the open blocker it resolves (Challenger lesson, 2026-10-03).

## Anchor

Each task he seals in Tap the Vein reaches the council as something a face can read, unpack and fill with context until it can be worked,
and then it meets the council's own work for today in a face-off whose result is advice: work it today, or defer it.

## What exists

- **The task.** bars-engine `TapTheVeinTask` holds his words (`originalText`), an optional Lens goal, `status`, `carryCount`, `chargeLevel`
  and `chargeNote` (his own read, "never inferred"), `blockedAt`, a soft `barId` ("so a task can be tuned / charged / 3·2·1'd / grown like any
  BAR"), and a running log, `TapTheVeinTaskNote`, of kind context, blocker, unblock or charge (`prisma/schema.prisma:922`).
- **What the council can read.** The menu export carries each item's `taskId` and `barId` (`src/lib/tap-the-vein/board-seal.ts`). The history
  export carries `chargeLevel` and `carryCount` (`src/app/api/tap-the-vein/history/route.ts`). Neither carries the notes. Both are behind the
  key that returns 401 today; `council/morning.py` also takes a pasted menu.
- **Where an item already goes.** `council/intake_align.py` gives each item one line: a Lens goal, a board row, a strand (work already
  happening, `ttv-align-to-work`), a pitched smaller goal, or no home yet with an optional shadow quest (`ttv-no-home-yet`).
- **Where a deferral goes.** The seed library: a resting task comes back on the 3, 7, 14, 30, 60, then 90 day ladder (`sl-resurface-ladder`).
- **What the council holds for today.** `board/needs_work.py`, the Next entry of each callsheet in `council/callsheets/INDEX.md`, and pull
  requests waiting on him.
- **A standing position in the way.** `ttv-task-not-bar` (stood 2026-10-16): "A commitment becomes a BAR only when you keep it as one."

**scout:** rung 2, we have it. The read reuses `intake_align.py`'s alignment and checks, the history export's charge and carry counts, the seed
library's ladder for a deferral, and the board's battle rows for the face-off. Rung 3 holds for one piece: the face-off's factors follow
utility AI's considerations (the vendored `ai-behavior-trees-utility-ai` skill), each scored and shown on its own, never summed into one number
(the Challenger's reason below). Nothing here is built by hand from nothing.

## Shaman

**The Shaman cast Alliance, becoming Impasse.** The cast says this fills a hole that was there before it started, and that the direct route is closed and
nobody was asked. The hole is plain in his message: the free write speaks and nothing on the council's side listens to it in its own terms.

**The free write is the subconscious speaking, so the read listens before it ranks.** He named it: "The tasks that emerge in teh free-write
are what by subconcious says is relevant." A face that reads a line only for how workable it is will always find it less workable than work
the council has been carrying for days. The face's first job is to say what the line is reaching for, in one sentence, before it says
anything about readiness.

**The standing test holds the read to what has been learned, never what is wrong with him.** "Does it say something is wrong with them, or
something about what I have learned?" A line that loses a face-off three mornings running is information about conditions: no next step,
no home, a missing input. It never means he is avoiding it. The ontology says the same of roadblocks: a blocker "does not prove misaligned
intention", and a face "must not psychologize a technical defect, infer hidden desire, or treat refusal as confirmation."

**Charge is his word, and a long charge note buys nothing.** `chargeLevel` is "his own read, never inferred." The ontology's disclosure rule:
"Intimate disclosure is not progression currency." A line he wrote three words about stands on the same footing as one he wrote a paragraph
about.

**Risk:** the read becomes the council talking over the free write. **Recommendation:** each read opens with the kernel in his terms and keeps
his line word for word above it.

## Architect

**The Architect cast Almost, becoming Stalemate.** It reads as nearly there, wet at the last stride, seeking one game while wearing the face of the other. Every
part already exists. The last stride is the join, and the stalemate is a read that looks like a face-off but is scored in only the council's game.

**The third position on ttv-task-not-bar: sealing is the keeping.** The standing position says a commitment becomes a BAR only when he keeps
it as one. His message today names the interface as "bars itself", where "a council member is able to see a player produces bar and unpack
it." Both hold if the seal is the act of keeping. Under `mm-raw` only kept lines leave the free write, so every sealed line is one he chose
and captured, which is what the ontology's BAR scope requires ("explicitly captured as a reusable kernel"). The task stays the obligation
and the BAR is its kernel, kept apart as the ontology keeps a BAR from its `BARExpression`: today's task is one expression; resting in the
seed library or joining a strand is another. What still holds from the old position: a BAR creates lineage, not a duty to build it.

**The read is one record per sealed line, written on the board, never in his task.** Fields: `line` (word for word), `taskId`, `barId`,
`face` (the face whose lens the line most needs), `kernel` (one sentence), `home` (the `intake_align.py` alignment), `missing` (what stops it
being worked today, from a fixed list: next step, home, input, capacity, blocker), `gathered` (each missing piece the face found in the
record, with its source), `workable` (true once nothing is missing, or what is still missing), `opponent`, `factors`, `call`, `why`. The
council never writes into `TapTheVeinTaskNote`: that log is his, and collection, derivation and adaptation are separate permission purposes in
the ontology. Whatever the council gathers lives with the read.

**Gathering means the record, and only the record.** A face fills a missing piece from board rows, callsheets, open pull requests, Lens goals
and the history export. Anything the record cannot fill stays missing and is shown as missing. It becomes a question for him only through the
reach test, on the board.

**The face-off pairs each line with one piece of council work competing for the same hours.** The opponent is the council's best candidate
for today in the same area (the same strand, row or goal first; else the top of `needs_work.py`; else the next callsheet entry). Factors,
each shown on its own: *signal* (he wrote it today; `carryCount`; his `chargeLevel`), *ready* (missing pieces left), *unlocks* (items it
removes, bars-engine's "generative dependencies"), *waiting* (days the council's item has sat, or a seed's rung). The call is one of: work
today, defer to the seed library, join the strand (the line becomes part of the council's item, "side quests merging into main quest" from
`mm-menu-shape`), or let it go, which is only ever offered.

**Build, one fresh thread:** the history export adds `notes` count and `blockedAt` per task (bars-engine); `council/bar_read.py` checks the
reads the way `intake_align.py` checks alignments and writes them to `board_data.json` `intake`; the Morning tab shows each read as a face-off
card under its item.

## Challenger

**The Challenger cast Endurance, becoming The Cauldron.** This exchange has happened before, and this time it is being transformed and carried by the handles.
It has happened before: ttv-loop 1 ranked council work against free-write lines through `intake_align.py`, and every unaligned line came out
"no home yet". The handles are the context.

**The self-inflicted loss: the council writes its own work's context, so its work always looks ready.** He said it: the council's tasks
"have more ergonimics to be worked on because they are context aware." A face-off scored on readiness alone is decided before it starts.
So the free-write line gets its context gathered first, and the face-off happens only after. That is the literal sense of "I need the
information from my subconcious to be context aware."

**One priority number is the first anti-pattern.** Summing the factors hides which side won on what. Each factor is shown, and the call names the one
that decided it.

**Treating a loss as a sentence is the second.** A line that loses is never composted, deferred or hidden on its own. Deferring is his tap in Tap
the Vein; the council's call is advice, and the Sage never decides (`sage_rule` in `council/faces.yaml`).

**Falsification tests.** F1 resolves whether the call is useful at all, and unlocks the build of the board card past its first version. F2
resolves whether the equal-footing rule works, and unlocks the decision to widen what a face may gather.

## Regent

**The Regent cast Incubation, becoming Spending.** What is true is still inside the shell, and it has a price not yet named. The price is a line the
council marks "defer" that he needed to work today. The shell is that this pass designs before one real morning has run through it.

**Non-negotiables.** His line is quoted word for word (as `intake_align.py` already enforces). The call is advice; he taps the outcome in
Tap the Vein. Nothing the council writes enters his private task or its notes. Composting is his alone and ends the obligation
(`CompostingDisposition`); a deferral is a rest, never compost (`sl-resting-not-compost`). Every deferral is kept, because "the pattern of what
he puts off is data about priority" (board read 20, 2026-10-03).

**Phase gates.** (1) The read: every sealed line gets one, checked by the script. (2) The face-off: only on lines whose read says workable,
or says plainly what is still missing. (3) The card goes on the Morning tab. (4) F1 runs on his first real morning. Gate 4 waits on the menu key; until
then the pasted-menu route and sample data carry the build.

**The build thread is done when** a pasted sample menu of five lines produces five reads and five face-offs that pass the
checker, the board shows them, and a test in `tests/` covers the checker.

## Diplomat

**The Diplomat cast Anticipation, with no changing lines.** The good part has started and the event has not. The good part, one Tap the Vein, starts with bars-engine
#403 and Six-faces-council #312; the event is his first morning where a face answers his free write.

**The bridge is one screen.** He asked for one UI because two "differ enough as to confuse me an annoy me." The read must not become a third
surface. It sits on the Morning tab under the Tap the Vein frame, one card per line: his line, the face's kernel, what was missing and what was
found, the opponent, and the call. The tap that acts on it stays inside Tap the Vein.

**Copy principles.** The kernel and the call are each one sentence he can act on without asking a follow-up. The card names the face that
read it. A missing piece is written as what would make it workable ("needs a first step"), never as a fault.

**Onboarding starts on good news.** The first card he sees is the one the face called "work today", so the feature opens on its good news.

## Sage

**The Sage cast Reserves, becoming Restraint.** It reads as stored and never given a day; a small rule never revisited holds it all. The small rule is
`ttv-task-not-bar`, and the day is the seal.

**Synthesis.** Reading his sealed line as a BAR (Architect, from his own words) lets a face unpack it. Gathering its context before the
face-off (Challenger) is what makes the subconscious context aware, which is his ask. Listening for the kernel first and never reading a loss
as avoidance (Shaman) keeps it his. The gates and the privacy line (Regent) keep the council's work off his private task. One card on the
Morning tab (Diplomat) keeps one UI. Nothing was dropped.

**The dissent is about sequencing.** The Challenger holds that the build should wait for F1 on a real morning; the Regent and Architect hold that the pasted-menu route
lets it be built and checked now. The pass records both; the build thread runs on sample data and F1 runs on the first real morning.

**The pass was not unanimous** on sequencing, and it was unanimous on the design. A unanimous design is a flag: no face argued that the
council should not read his free write at all. `ttv-raw-bars` (read once, then delete) and `mm-raw` (only kept lines leave) are the record
that answers it, so the flag is noted and not raised.

## Verdicts

| Face | Sealed task read as a BAR | Context gathered before the face-off | Call is advice only | Build now on sample data |
|---|---|---|---|---|
| Shaman | yes, kernel first in his terms | yes | yes | yes |
| Architect | yes, sealing is the keeping | yes, from the record only | yes | yes |
| Challenger | yes | yes, the core rule | yes | no, F1 first |
| Regent | yes | yes | yes, non-negotiable | yes, gated |
| Diplomat | yes | yes | yes | yes |
| Sage | recommends | recommends | recommends | records the split |

## Positions

Each stands unless he flips it on the board.

1. **`ttv-one-ui`** (Diplomat, Architect, from the thread "Tap the Vein on the board"): the board shows bars-engine's own Tap the Vein in its
   Morning tab, never a copy of it. Cited: his words, "They differ enough as to confuse me an annoy me"; bars-engine #403 and
   Six-faces-council #312.
2. **`tb-sealed-is-bar`** (Architect, Challenger): a line you seal in Tap the Vein is a BAR the council can read; today's task is one
   expression of it, and the BAR creates no duty to build. Updates `ttv-task-not-bar`. Cited: his words, "the interface structure I beleive
   is bars itself"; `mm-raw`; the ontology's BAR scope.
3. **`tb-face-unpacks`** (Architect, Shaman): one face reads each sealed line: the kernel in one sentence, where it belongs, what stops it
   being worked today, and what it found in the record. The read lives on the board, never in your task or its notes. Cited: his words,
   "unpack it or gather more context until it's able to be worked"; the ontology's permission purposes.
4. **`tb-context-first`** (Challenger, Shaman): a free-write line gets its context gathered before it meets council work, so it is judged on
   what it is and not on what the council happens to know. Cited: his words, "I need the information from my subconcious to be context aware."
5. **`tb-face-off`** (Architect, Challenger): each read line meets the one piece of council work competing for the same hours; the factors
   (signal, ready, unlocks, waiting) are shown one by one, never summed, and the call names the one that decided it. Cited: his words, "a head
   to head battle mechanic of prioriities"; the utility AI considerations pattern.
6. **`tb-call-is-advice`** (Regent, Diplomat): the call is work today, defer to the seed library, join the strand, or (only offered) let it
   go; you tap the outcome in Tap the Vein, and a line is never deferred or composted for you. Cited: the Sage rule in `council/faces.yaml`,
   `sl-resurface-ladder` (Draw, Keep resting and Let go are your taps), `sl-resting-not-compost`, the ontology's composting rule.
7. **`tb-loss-not-avoidance`** (Shaman): a line that keeps losing is read as missing conditions, never as avoidance, and a longer charge note
   does not help it win. Cited: the Shaman's standing test; the ontology's roadblock and disclosure rules.

## Questions

None survived the reach test. Each candidate and its citation:

- *May the council read sealed lines?* Answered: `mm-raw` (only kept lines leave) and `ttv-raw-bars` (read, then delete).
- *Who decides work or defer?* Answered: the Sage never decides (`sage_rule`), and Draw, Keep resting and Let go are his taps (`sl-resurface-ladder`).
- *May the council add notes to his tasks?* Not needed: the read lives on the board (`tb-face-unpacks`), so nothing asks for that consent.
- *Does a tie go to the free write or to council work?* Answered by his words, "I need the information from my subconcious to be context
  aware": a tie shows both and names the free-write line first. Held as part of `tb-face-off`; he can flip it.

## Tests

- **F1, due 2026-10-26, or his first real morning after the menu key works if later.** On a morning of three or more sealed lines, he takes the
  council's call on at least half. Resolves: whether the call is useful. If it fails, the face-off is cut back to the read alone.
- **F2, due 2026-10-31.** Across his first five read mornings, council work wins no more than four face-offs in five. Resolves: whether
  gathering context first gives the free write equal footing. If council work wins more, the faces may gather from more of the record.

## Landing

Pass file: this one. Ledger: `council/ledger/2026-10-19-ttv-bars1.json`. Board: the seven positions above. Next: a fresh thread builds
`council/bar_read.py`, the history export's extra fields and the Morning tab card on sample data (morning-menu callsheet, Next).
