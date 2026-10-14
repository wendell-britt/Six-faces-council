# Unfinished work from twenty sessions: what to pick up, what to retire

**Run 2026-10-14**, called by Wendell in the project thread "Unfinished work from your last 20 sessions" (23:09 UTC).
This is the first council pass on the subject.

**The ask, in his words.**

> Let’s have this ingested and weighed in on  by the game masters

**The subject is a list.** A thread searched his last twenty Claude Code session logs (2026-09-14 to 2026-10-14) for three
kinds of unfinished work: work he deferred, problems Claude raised outside the task, and tasks dropped when the
topic changed. It checked each against current code and ranked eleven as still open. The list is
`/mnt/project-files/unfinished-work-2026-10-14.md`. His earlier words in the same thread:

> Show me the list first. For each one I pick, give me a new-session card I can start with one click.

**Board read.** The board was read at 23:20 UTC (live version 1792018774-06a8), with the store's `lists` and `steps`
collections. `python3 council/due.py --ahead 7` reported nothing deferred and due. No daemons were sent: every item
is a routing call against the record, and none needed legwork beyond what the thread had already done. The ontology
skill was not loaded, because this pass designs no game.

**The anchor holds.** Unfinished work should either reach a thread that finishes it, reach Wendell as a step only he can take,
or be retired with its reason. Nothing should sit in a chat log where no session will find it.

**Casts** (`council/iching/cast.py`, three coins):

| Face | Hexagram | Becomes |
|---|---|---|
| Shaman | 36 Nightfall | 3 Sprouting |
| Architect | 37 Household | 63 Arrived |
| Challenger | 51 Shock | 7 Muster |
| Regent | 39 Impasse | 63 Arrived |
| Diplomat | 54 Home Field Advantage | 41 Spending |
| Sage | 29 Depths | 44 Serendipity |

## The board corrects the list

The list was built from logs and code. It never read the board, and the board already holds three of its items.

- **Flirtcraft's database (list item 5) is done.** The steps list "Give flirtcraft its own database" has eight of
  nine steps ticked, including step 9, "Ask for a sign-in link with your own email." Only step 7, creating the
  tables by hand, is unticked. The board ruled on 2026-10-02 that production builds migrate (`fc-migrate-on-deploy`),
  so step 7 is probably moot.
- **Anastasia's campaign (list item 2) is on Your steps.** The list "Anastasia's campaign: get her yes and her
  links, then create the page" has three open steps, due 2026-10-11 and 2026-10-12. The draft is written. The work
  waits on her consent and her links.
- **Sprout (list item 9) is not stalled.** The thread checked a local copy last pulled on 2026-10-03.
  wendell-britt/sprout has commits through 2026-10-13, and `docs/design.md` line 354 settles the tile-day as the
  pricing unit.

## Shaman: 36 Nightfall, becoming 3 Sprouting

**The cast.** Nightfall shows a light kept covered and still lit; Sprouting says this is early, and the mess is not a
verdict. The list reads like an accusation, eleven items not done. Most of it is work that was covered by newer work,
and a covered light is not a dead one.

**What is moving underneath.** Two items carry a person. Anastasia's campaign names her father's death, her
mother's cancer and the flood. Consent and release are reserved, so the council builds nothing more and asks
Wendell nothing new. Her steps already wait on Your steps. The second is the Emotional Alchemy move library. Its
last exchange (2026-09-16) ended with five rulings "written and waiting for your yes" and the line *"So the 6 moves
you earn are the 6 places you've been faking it. That's the whole game, actually."* That is a live idea, not a
chore. Retiring it would be the wrong burial.

**The Shaman recommends.** Anastasia stays exactly where it is. The move library reaches Wendell as one question, because
whether it waits or comes back is a call about what he loves working on.

## Architect: 37 Household, becoming 63 Arrived

**The cast.** Household says an arrangement formed without being discussed; Arrived says work is finished, and
that is when it starts moving. Several items are finished work whose record never caught up: the podcast hub
shipped on 2026-09-30 while every task in `.specify/specs/mtgoa-podcast/tasks.md` is still unticked.

**What must be true in the machine.**
- **Three items are plain fixes, and none needs a spec.** The image limit (`src/app/api/assets/upload/route.ts`,
  line 31 declares 5 MB and line 109 enforces the 10 MB PDF limit for every type), the 2,021 duplicate
  "cert-cyoa-slides (follow-up)" rows at the end of bars-engine's `BACKLOG.md`, and the two deferral paragraphs in
  this repo's `.claude/skills/six-faces/SKILL.md` (lines 103 and 125). `scope` in `council/pipeline.yaml` keeps
  fixes out of the feature pipeline.
- **Two items belong to strands that already have call sheets.** The Jev pieces (JEVI on main's backlog, the stale
  count in `jev-asset-recount`) belong to `jev-asset`. The podcast spec's ticks belong to `podcast`. Starting a new
  strand for either would collide with the owner.
- **Flirtcraft's step 7.** The daily compost pass already keeps, drops or takes over open steps. It should drop step
  7 if a production build created the tables, which step 9's working sign-in suggests.

**The Architect recommends.** Three fixes each get a short thread of their own, two notes go to existing call
sheets, and the feature pipeline gets nothing new.

## Challenger: 51 Shock, becoming 7 Muster

**The cast.** Shock says it went off and will go off again; Muster says what would organise this is a fact not yet
said. The fact is that the sweep got three of eleven wrong because it never read the board. It will go off again the
next time a session sweeps logs.

**What breaks.**
- **The November 10 reminder.** The 2026-09-15 session said the reminder "won't send" without `EMAIL_POSTAL_ADDRESS`
  and needs `CRON_SECRET` before the job is allowed to run. No later session mentions either, and the Vercel
  connector refused to list the variables (403), so nobody knows. The partial backfill of 2026-09-15 already put 66
  character-sheet readers into Resend, so the reminder needs only the two variables. The topics backfill (one-shot
  command from #248) is for the succession and nonprofit lists, which no deadline holds.
- **The upload limit is a cost leak, not a crisis.** An image of up to 10 MB lands in Blob storage where 5 MB was
  meant. The fix is one line and a test.
- **Falsification test for the corrected list.** A sweep that reaches Wendell should name, for each item, the board
  row or steps list it checked. If a later sweep reports an item the board already holds, this pass's position
  `uw-board-before-sweep` failed.

**The Challenger recommends.** The two Vercel checks go on Your steps with a date well before November 10. The sweep rule
becomes a position.

## Regent: 39 Impasse, becoming 63 Arrived

**The cast.** Impasse says the direct route is closed and nobody was asked; turn back and come again with others.
Arrived says the work is finished. Both readings point at the move library: it stalled because the rulings never
reached the board, which is the one place he rules.

**Obligations.**
- **A legal obligation.** List email needs a postal address. That outranks every other item here, and only
  Wendell can enter it.
- **The cap of three.** `st-cap-games-only` counts game projects only: the Big Mind cave, Root, the Sprout slice and
  the Cave of Lessons. The Emotional Alchemy card game is a game, and its 72 class moves would be a fourth project.
  The council cannot add it to the cap or defer it on its own; both are his priority calls. The question goes to
  the board with deferral as an option.
- **Pushhands.** His words on 2026-10-01, in the mocap session: *"I do want fixes for the obvious problems the
  inspector finds. If this is taken care of in a later task I will defer to then"*. Claude answered that no later
  task covers it, because the project's constitution keeps analysis, visualization and repair apart. The record
  answers the preference: he wants fixes, and the first release excludes them. That makes repair a later project of
  its own, spec'd after the first release, and not a question. The footage check at about 2.0 s is his eyes only,
  so it is a step.

**Done has a definition.** Every item ends as a thread, a step, a question, or a retirement with its reason.

## Diplomat: 54 Home Field Advantage, becoming 41 Spending

**The cast.** Home Field Advantage says you are following rules nobody told you. Spending says this has a price you
have yet to name. The thread wrote its list without the board's rules, so the list that reached him in chat
carried three wrong items. The price is his trust in the next list.

**The Diplomat builds three bridges.**
- **Correct the list where he read it.** The corrections go beside the original entries in the shared file, not in
  place of them, so the first version stays readable.
- **His ask was session cards for the items he picks.** On the board, a position he lets stand is a pick. Once he
  presses Send, each standing fix gets its card.
- **One plain line per step.** The email steps say where in Vercel to go, what to enter and how to know it worked,
  and the secret is generated on his device.

## Sage: 29 Depths, becoming 44 Serendipity

**The cast.** Depths says the bottom has another bottom; Serendipity warns against building on one piece of
evidence. The list was one piece of evidence, and the board was the second bottom under it.

**Synthesis.**
- **The Shaman** kept the move library alive and held Anastasia's campaign inside the reserved line.
- **The Architect** sorted the work into three fixes, two call-sheet notes and one compost-pass drop.
- **The Challenger** found the deadline that matters and the failure mode of the sweep itself.
- **The Regent** named the legal obligation, applied the cap of three to the move library, and answered pushhands
  from the record.
- **The Diplomat** turned "pick" into the board's own action and kept the first list readable.
- **Dropped:** nothing. The Shaman's wish to bring the move library back now is carried as an option, not adopted.

**The dissent is real.** The pass was not unanimous. The Shaman wants the move library brought back now; the Regent holds that
the cap of three makes it a deferral unless Wendell names what gives way. That split is the one question.

## Verdicts

| Face | Email list (1) | Upload limit (3) | Move library (4) | Jev, podcast spec (6, 10) | Pushhands (7) | Dupes, skill (8, 11) | Sprout (9) |
|---|---|---|---|---|---|---|---|
| Shaman | steps | fix | bring back now | call sheets | step | fix | retire |
| Architect | steps | fix | his call | call sheets | later project | fix | retire |
| Challenger | steps, first | fix | his call | call sheets | step | fix | retire |
| Regent | steps, first | fix | defer unless he names a trade | call sheets | later project, step | fix | retire |
| Diplomat | steps | fix | his call | call sheets | step | fix | retire |

## Outputs

### Positions (stand unless he flips them)

| id | Faces | Position | Why it did not need him |
|---|---|---|---|
| `uw-list-corrected` | diplomat, challenger | Three items on the list were wrong: Flirtcraft's database is done, Anastasia's campaign is already on Your steps, and Sprout is active. The corrections sit beside the originals in the shared file. | The board's steps and the sprout repo's commits answer it. |
| `uw-board-before-sweep` | challenger, regent | A session that sweeps logs for unfinished work reads the board's rows and Your steps before it ranks anything, and names the row or list it checked for each item. | The sweep failed on three of eleven items for this reason. |
| `uw-email-steps` | regent, challenger | The November 10 reminder's two Vercel settings and the topics backfill go on Your steps, due 2026-10-24 and 2026-10-31. | His own setup list from 2026-09-15 names the three steps; only he can enter them. |
| `uw-upload-limit` | architect, challenger | bars-engine's upload route caps images at 5 MB and PDFs at 10 MB, with a test. It is a fix and merges when its checks pass. | Line 31 states the intended limit. A fix stays out of the pipeline (`scope`). |
| `uw-backlog-dupes` | architect | The 2,021 duplicate "cert-cyoa-slides (follow-up)" rows at the end of bars-engine's `BACKLOG.md` collapse to the one row they repeat. Git keeps the old file. | The seed ignores the section, so nothing a reader sees changes. |
| `uw-skill-dedupe` | regent, architect | The two deferral paragraphs in `.claude/skills/six-faces/SKILL.md` become one, keeping every rule both carry. | A skill edit, not `faces.yaml`; it syncs to every repo. |
| `uw-jev-to-sheet` | architect, sage | JEVI lands on main's backlog by itself, and `jev-asset-recount` gets the corrected count (four known drifts, one live) beside its original wording. Both go to the `jev-asset` call sheet. | `jev-images-backlog` and `jev-asset-recount` already stood; this carries them out. |
| `uw-podcast-ticks` | diplomat, architect | The podcast strand ticks what shipped in `mtgoa-podcast/tasks.md` and marks the question and guest forms as not built. | The hub shipped on 2026-09-30 (`cc4d4f35f`). |
| `uw-pushhands-repair-later` | regent, architect | Pushhands repair becomes its own project after the first release. Nothing is built for it before the footage check. | His words ask for fixes, and the constitution keeps repair out of the first release. |
| `uw-sprout-current` | challenger | List item 9 is retired. Sprout's open decisions of 2026-10-03 were taken up in later work. | `docs/design.md` line 354 and commits through 2026-10-13. |
| `uw-anastasia-as-is` | shaman, regent | Anastasia's campaign gets no new work from the council. Its three steps stay on Your steps. | Consent and release are reserved, and the steps already exist. |
| `uw-flirtcraft-step7` | architect | The compost pass drops Flirtcraft's step 7 once it confirms production created the tables. | `fc-migrate-on-deploy` (yes) and step 9 ticked. |

### Question (passed the reach test)

**`uw-ea-library`** (owner: Regent, with the Shaman). The Emotional Alchemy move library has had five rulings
(EA-11, EA-12, EA-13a, EA-13b, EA-13c) waiting since 2026-09-16, then two interview answers, a spec, research and the
72 class moves. Bring it back, defer it, or fold it into the cave work?

- **Bring the five rulings to the board now.** Five rows appear for him to flip, and the library becomes a fourth
  game project beside the cap of three unless he names one that waits.
- **Defer for a month (recommended).** Nothing moves until 2026-11-14, and the spaced deferral brings it back with
  what changed.
- **Fold the class moves into the cave.** The Big Mind cave's chambers and daemons take up the idea that a class
  move is a key at the place a player has been faking it. The card game's own spec stays where it is.

*Why only he can answer:* the cap of three is his ruling, and whether this game outranks one in the cap is his
priority. *Why not before:* it was raised in chat on 2026-09-16, before the board was his one place to rule.

### Steps only Wendell can take (published to Your steps)

List `email-list-nov10`, "The November 10 reminder: two settings in Vercel, then the topics backfill":
1. Check `EMAIL_POSTAL_ADDRESS` in bars-engine's Production environment, and add it if missing. Due 2026-10-24.
2. Check `CRON_SECRET` the same way, and add a generated one if missing. Due 2026-10-24.
3. Run the one-shot topics backfill from Terminal. Due 2026-10-31.

List `pushhands-footage`, "Pushhands: the hand check at 2.0 seconds":
1. Watch the footage at about 2.0 seconds and say whether A's right hand touches B's left hand. Due 2026-10-28.

## Record block

- **Date:** 2026-10-14. **Called by:** Wendell, thread "Unfinished work from your last 20 sessions".
- **Question:** "Let’s have this ingested and weighed in on  by the game masters"
- **Verdicts:** Shaman: bring the library back, keep Anastasia as is. Architect: three fixes, two call sheets.
  Challenger: the reminder first; the sweep must read the board. Regent: the address is a legal duty; the library
  waits on his trade. Diplomat: correct the list beside the original; a standing position is a pick.
- **Board rows:** twelve positions (`uw-*`), one question (`uw-ea-library`), two steps lists.
- **Ruling:** pending.
