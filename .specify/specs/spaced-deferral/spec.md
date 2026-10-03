# Spec: Deferred items come back on a spaced schedule, with new context

## The ask

> "We want to use spaced repetition so that tasks that are deferred come back and the council can weigh in
> on them in new context."
>
> Wendell, in chat, 2026-10-03, after ruling that deferral is a council lesson.

**Who it is for:** Wendell, reading the Council Board on his phone, and every session that reads the board for him.

**What he feels now, and what should change:** He defers work he cannot take up yet, as with the oracle drafts
("I've been out of the practice too long"). An item that comes back bare asks him to rebuild the context he
set down. An item should come back with the council's reading of what changed while it waited, and an item
he keeps deferring should come back less often.

## Purpose

Each deferral of the same item waits longer than the one before, the way spaced repetition schedules grow.
When a deferred item's date passes, the council gathers what changed in its project while it waited,
re-weighs it with fresh casts, and writes that onto the row. Then the item returns to the Open tab with
the council's reading beside it.

## User stories

### A deferral I keep making waits longer

**As Wendell**, I want the Defer button to offer a spaced return date that grows each time I defer the same
item, so low-priority work stops coming back every week.
**Acceptance:** the first option in the Defer list reads "bring back in 1 hour (spaced)" for an item never
deferred, "bring back in 6 hours (spaced)" for one deferred for an hour, and "bring back in 1 month (spaced)"
for the oracle drafts, which waited 31 days the first time.

### An item comes back with what changed

**As Wendell**, I want a returning item to show what changed while it waited and what the council now
recommends, so I can decide without rebuilding the context.
**Acceptance:** a returned row shows a box headed "Since you deferred this" with how many times I deferred
it, my last steer in my words, what changed with its source, each face's line under its cast, and the
council's recommendation. If nothing changed, the box says so in one line.

## Design decisions

| Decision | Choice | Whose |
|---|---|---|
| Spaced repetition | Each deferral of an item waits longer than the last | Wendell, the ask |
| The numbers | A ladder: 1 hour, 6 hours, 1 day, 3 days, 1 week, 2 weeks, 1 month. Week, month and "when I ask" stay on the list | Wendell, in chat, 2026-10-03: "The spaced repetition of deferrals should start with 1 hr to 6 hours to 24 hours to 3 days to a week to 2 weeks to a month". It replaced version one, below |
| Which rung | The first rung longer than the item's last wait, so a wait he set by hand counts. After a one-week deferral the next spaced one is 2 weeks; the oracle drafts waited 31 days, so theirs is a month | The session's reading of his ladder, not his words |
| Past the top | Stays at a month | The session's reading. His ladder ends at a month and says nothing after it |
| No retirement after N deferrals | The schedule keeps growing and never retires an item by itself | Council. A cap would be a number inferred on his behalf (faces.yaml council lesson of 2026-08-22). The Challenger's dissent is recorded in pass eight |
| New context | `council/due.py` reads, for the item's project: the changes that landed on its main branch, the council's ledger records, and the lessons ruled, all since the moment he deferred | Council |
| Since when | The exact time he pressed Defer (`saved_at`), compared with the time each ledger record was committed. A lesson carries only a date, so a same-day lesson is marked "same day" | Council, from the cheap test below |
| The re-weigh | Each face casts and writes one line on what changed, and the council recommends one of: take it up, defer again, retire, or reshape the question | Council, under the reach test and the iching-cast-first position |
| Who re-weighs, and when | A weekly scheduled session, and also any session that reads the board | Wendell, question `sd-when`, 2026-10-03: "On its own" |
| How far ahead | Each run prepares items due now or within the coming 7 days, so they arrive with the reading done. A reading can be up to 6 days old when he sees it | Wendell, in chat, 2026-10-03: "Yes they should prepare items due in the coming week" |
| Rungs shorter than a week | An item deferred for an hour, 6 hours, a day or 3 days can come back before any Monday run reaches it. It waits on the Open tab with the "not re-weighed yet" note until a session reads the board | Open: put to Wendell in chat, 2026-10-03 |
| History | Every deferral of an item stays in its `history`, also after he takes it up | Wendell, the deferral lesson ("we are also collecting data about priority") |

## Contracts

**A deferral on the board's store** (written by the board): `{deferred: true, until: "spaced"|"week"|"month"|"ask",
hours: <number, spaced only>, steer, savedAt}`.

`until` is a UTC time (`2026-10-03T20:00:00Z`); the first deferrals were recorded as a date alone, which counts
as midnight UTC. Each history entry carries `hours`; the first carried `days`.

**A recorded deferral** (`resolved.<kind>.<id>` in `board/board_data.json`, written by `due.py record` on main):

```json
{"decision": "deferred", "until": "2026-12-04T10:00:00Z", "project": "friendcraft-manuacript",
 "label": "Deferred 1 month, until 2026-12-04T10:00:00Z", "recorded": "2026-11-04", "record": "<ledger file>",
 "history": [{"recorded": "2026-10-03", "saved_at": "2026-10-03T18:08:52Z", "until": "2026-11-03", "days": 31, "steer": "..."},
             {"recorded": "2026-11-04", "saved_at": "2026-11-04T10:00:00Z", "until": "2026-12-04T10:00:00Z", "hours": 720, "steer": "..."}]}
```

When he later takes the item up, the new resolved entry keeps `history`.

**A re-weigh** (`review` on the question or position row in `board_data.json`, written on main):

```json
{"date": "2026-11-03", "changed": ["<what changed, with its source>"],
 "faces": [{"face": "Challenger", "cast": "2 Bearing", "line": "<one sentence>"}],
 "recommend": "take it up | defer again | retire | reshape: <one sentence>"}
```

`due.py record` clears `review` when he answers the returned item.

## Version one, and what it got wrong

The first version, merged in #13, set the numbers itself: 7 days for the first spaced deferral, then twice the
last wait. Wendell replaced them the same day with his ladder. What version one got wrong is the scale. It
treated deferral as a matter of weeks and months, for projects, and his ladder starts at an hour, so a deferral
can also mean "not right now". Version one's dates were whole days; his ladder needs hours, so `until` became a
UTC time.

## Reserved items

Nothing here touches money, prose, a person's name or consent. The weekly session is a question
because it spends his account's usage.

## How we will know it failed

- **The risk:** the re-weigh is ceremony. The council finds nothing useful in what changed, and the box on
  the row repeats the old reasoning in new words.
- **The cheap test, run before building the board:** run the context gatherer on a real item as if it had been
  deferred on 2026-10-02 and were due today. The item was the flirtcraft deploy alert (position
  `fc-silent-failure`), proposed on 2026-10-02 and never started. Pass mark, stated in chat before the run: the
  brief turns up at least one change a face could use to change its verdict.
- **The result that stops the work:** a brief with nothing a face could use, or one buried in noise.

## Result of the test, 2026-10-03

**It passed.** The brief listed 8 changes that landed in flirtcraft after 2026-10-02. Two of them would change
a face's verdict on the deploy alert. The storefront is live (board read 16), so a deploy that fails without
anyone hearing now keeps a fix from reaching a live store. Production builds also apply database migrations
now (`fc-migrate-on-deploy`), which gives a build a new way to fail. Both raise the alert's priority. A failed
deploy leaves the last good one serving, so the site itself stays up.

**The test also found a fault, and the fault is fixed.** Run on the oracle drafts, the brief listed two
records from earlier on 2026-10-03, before he deferred them, because it compared dates. It now compares the
time he pressed Defer with the time each record was committed, and it leaves out the deferral's own record.
Lessons carry only a date, so a lesson from the same day is marked "same day".

## Definition of done

- [x] The cheap test passes, and its result is recorded here.
- [x] `council/due.py` lists due items with their brief, shows the next spaced wait, and records a deferral.
- [x] The board offers the spaced option first, with its number of days, and a returned row shows the review or
  says the council has not re-weighed it yet. Checked by rendering a test board in a headless browser.
- [x] `council/pipeline.yaml` and both skills say a session runs `due.py` at every board read and re-weighs each
  due item before it reaches him.
- [x] Ships as board position `sd-ship`. It stood at board read 21, and the PR merged.
- [x] The weekly session is scheduled: "Council: re-weigh due deferrals", every day at 15:45 UTC (Mondays until board read 24).
- [ ] The first real re-weigh, the oracle drafts on 2026-11-03, is recorded here.
