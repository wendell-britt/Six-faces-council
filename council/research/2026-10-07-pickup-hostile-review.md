# Board pickup: a hostile review

Wendell, 2026-10-07: "Let's do a hostile review for what assumptions we are making that will have something like
this happen again. We want root cause not just a quick patch. Is there something in how we're thinking about this
work that is off that will continue emerging problems like this in the future?"

## The short answer

Something is off: we are building a delivery system out of conversations. Every hop between your Save and the ledger on main is an
AI session that has to be woken, has to be the right session, has to hold the repo, has to pass a permission check,
has to not be restarted, and has to read a paragraph of prose correctly. Each failure so far broke a different hop,
and each fix added another paragraph. That pattern will keep producing new failures, because the number of hops and
the number of paragraphs only grow.

Your answers were never lost. All fifteen from 23:47 to 23:49 sat safely in the board's own store the whole time.
What failed was the chain we built to carry a copy of them somewhere else. We have spent two days guaranteeing the
delivery of a doorbell.

## What the record shows

Six separate breaks in about thirty-six hours, each at a different hop:

| When (UTC) | Hop that broke | What happened | Source |
|---|---|---|---|
| 10-06, before 20:20 | Page permission | A republish passed only `db`, dropping the connector grant; Send went dead | docs/pickup.md |
| 10-06, ~20:01 | Concurrency | Two board reads recorded the same six saves; the merge left conflict markers in main's board_data.json | docs/pickup.md, fixed in 2b06dea |
| 10-06, 20:36 | Authority | Your "yes" on the board was refused as approval for the grant; it needed you to type it in chat | thread "Trigger council hooks anywhere" |
| 10-06, 23:31 | Authority | The coordinator's auto mode refused to start a board read, because a routine firing is not you typing | project timeline, 23:31 |
| 10-06 23:49 to 10-07 13:02 | Session identity and environment | The routine fired a fresh session with no repo; it called `add_repo`, which restarts the container, killing the work, five times over thirteen hours, with no alarm | docs/pickup.md "The lost Send" |
| still open | Routing | You chose a fresh session per Send (`pickup-where`), which is the exact shape that lost the 23:49 Send; that routine still has no repo | `trig_01Q9mMcVwR4MCqHQzUHwcmiS` |

The leftovers, read from the routine list today (list_triggers, 2026-10-07 15:00):

- Three pickup routines are enabled. `trig_01L138vKTaN9MSJoFKRmaBNx` is live. `trig_01DpRsDM94Cnv2neyDVkBNMb` still
  points at the Flirtcraft coordinator. `trig_01Q9mMcVwR4MCqHQzUHwcmiS` has no repo and has never fired. Nothing gets
  retired; it gets superseded and left switched on.
- The live pickup routine shows no `last_run` at all, though it has fired several times. The platform does not track
  those firings, so nobody can see from the routine whether a Send arrived.
- The daily safety net (`trig_01F8fDdkjYEeMCfdozj6w3tt`) runs in a standing session that was at 331,329 tokens on
  10-05, past CLAUDE.md's own 200,000 handoff line. Its step 1b catches a missed save by firing the same pickup
  routine, so when the chain is broken the safety net breaks with it.

## The assumptions underneath

### 1. An agent session is a reliable transport

Moving a saved answer from the store into `board_data.json` is clerical and fully determined: same input, same output,
no judgment. We route it through the most fragile part we have, a chain of sessions that can be recycled, refused,
restarted or mis-routed. A step that needs no judgment should not depend on a judge being awake.

### 2. Prompts are a control plane

The routine's prompt is how we steer the system, and it is the worst place to keep configuration. Only the
conversation it posts into can edit it, so changing it means delete and recreate, and then hunt down every copy of
the id (the template's `PICKUP_TRIGGER`, the daily routine's step 1b, docs/pickup.md). Its rules are prose an agent
may or may not follow; 23:49 was a session that did not know the rule because the rule had not been written yet. Each
incident adds a sentence ("never call add_repo"), and the next incident will need a sentence nobody has thought of.

### 3. A session is a stable address

The design names specific sessions: the routine targets the coordinator by id, the daily routine targets one standing
session, the old routine still targets the Flirtcraft coordinator. Coordinators are recycled routinely, and when the
target is gone or the platform decides otherwise, the routine fires a fresh session that has nothing. Any design that
needs a particular session to be alive will break whenever sessions turn over, and they turn over all the time.

### 4. Your click carries your authority down the chain

You press Send, so it feels like you asked. The safety system reads it differently: by the time the request reaches
the coordinator, it is a routine talking, and a routine cannot grant itself the right to act for you. That refusal is
correct, and we keep meeting it (your board "yes" at 20:36, the coordinator at 23:31). The proposed fix, a standing
line in Project settings saying the routine may always start a board read, is a legitimate instruction from you, but
it is still a bet on how a classifier will read a sentence. The council's own rule makes this worse: the board is
where your word lives for design, but the platform only counts your word for permissions when you type it in chat.
Those two channels will keep colliding until the design stops needing permission-gated actions to record a save.

### 5. Exactly once, by good behaviour

There is no lock, no claim, no "done" marker and no timeout. Two board reads both recorded the same saves because
nothing stopped the second one. The 23:49 Send looped for thirteen hours because nothing noticed it never finished.
`pickup/last` records that a Send happened, never that a read claimed it or finished it. "A board read that starts
while another runs should wait for it" (docs/pickup.md) is a wish written as a rule.

### 6. A failure gets fixed by writing a rule

pickup.md is mostly an incident log now, and CLAUDE.md opens with one. Rules written in prose get dropped by
summaries (CLAUDE.md itself records that on 10-03), cost tokens on every read, and only work if the next session
reads and obeys them. Five rules for one button is a sign the button's design is wrong.

### 7. We find out how the platform behaves in production

"What the first firings showed" in pickup.md is a list of platform behaviours discovered by shipping: a routine made
in a thread fires into that thread, firing text arrives as a second message, only the target conversation can edit a
prompt, `add_repo` restarts the container. The 20:36 thread ended "your first Send is the real test". You are the
test harness. The council then recommended a design (`pickup-where` A, fresh session) on assumptions about the
platform nobody had checked, and it is the design that lost the 23:49 Send.

## What I'd redesign

One change of model, then four mechanical pieces.

**Pull, don't push.** The board's store becomes the record of your answers. Recording stops being a job someone has to
be woken for. Every council session (board read, pass, daily run, any thread touching rulings) starts by syncing the
store into main with one script, keyed by row id and `savedAt`, so running it twice changes nothing. A missed Send
then costs minutes of delay, never a lost answer or a debugging thread. Send stops being the delivery mechanism and
becomes what it should be: "I've ruled, start the work my answers open."

The four pieces:

1. **One sync script, idempotent.** Extend `board/unrecorded.py` into `board/pull.py`: read the saved store, write
   resolved entries and a ledger record for anything new, rebuild, push to main. Same input twice, same main. It is
   the first step in CLAUDE.md, not a step in a routine prompt. Recording runs on Sonnet; acting on the answers stays
   with the faces.
2. **A claim with an expiry.** `pickup/last` gets `claimedBy`, `claimedAt` and `doneAt`. A board read claims before it
   works and marks done after; a second read sees a live claim and stops. A claim older than an hour with no `doneAt`
   is stale and anyone may take it.
3. **An alarm that does not share the chain.** The daily check reports stale claims and unrecorded saves straight into
   the project chat in plain words, rather than firing the same routine. If the chain is down, you hear about it the
   next day instead of thirteen hours later by accident.
4. **One routine, no named sessions, nothing left switched on.** Keep only `trig_01L138vKTaN9MSJoFKRmaBNx`, whose job
   shrinks to "start a thread". Disable `trig_01DpRsDM94Cnv2neyDVkBNMb` and `trig_01Q9mMcVwR4MCqHQzUHwcmiS`. Move the
   daily run off the standing session to a short session per day, which also brings it back under the 200,000 line.

Two habits go with it:

- **A failure gets a mechanism before it gets a sentence.** Before adding a rule to pickup.md or CLAUDE.md, ask what
  would make the failure impossible or loud. Incidents go in a log nobody has to read every turn.
- **Check the platform before the council recommends.** A design question that depends on how routines, sessions or
  permissions behave gets one test firing, or a read of the platform docs, before it reaches the board as a
  recommendation.

## What this does not fix

- A routine firing into the coordinator will still sometimes be refused. With pull in place that delays work; it no
  longer strands answers.
- Your board answers still do not count as permission for actions the platform gates (connector grants, publishing
  with a new capability). Those stay chat-only, and the board should say so on any row that needs one.
- The coordinator can still be recycled mid-Send. The claim's expiry and the next session's sync cover it.
