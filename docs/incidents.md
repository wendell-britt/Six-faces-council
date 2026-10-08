# Incidents

Process rules that a mechanism replaced, kept here with their dates and reasons so they stay readable and no session
pays to reread them. Wendell, `proc-rule-retire` A (2026-10-07): the retro may retire a rule as a board position that
stands unless he flips it, and the rule moves here. No working-rules file points sessions at this one.

## Board pickup, the push design (2026-10-06 to 2026-10-07)

Retired by retro 1 (`retro1-retire-pickup-history`, council/passes/6FACE_RETRO1_2026-10-07.md). The pull model
(`pickup-pull-model` A, docs/pickup.md) replaced every rule below: a lost Send now only delays an answer. The six
breaks these sections describe are tabled in council/research/2026-10-07-pickup-hostile-review.md. Moved verbatim
from docs/pickup.md.

### The pickup routine

`trig_01L138vKTaN9MSJoFKRmaBNx`, "Council board: pick up Wendell's saves (council project)", has no schedule; only the
button and the daily run fire it. It wakes the coordinator of the 6 face game master council project
(`session_016Yw4J6vYgt5h3grAHh7NmK`), which starts one thread for a board read. It replaced
`trig_01DpRsDM94Cnv2neyDVkBNMb`, which woke the Flirtcraft project's coordinator, on 2026-10-06.

Wendell chose a fresh session per Send (`pickup-where`, board read 2004) so the pickup belongs to no project. A
routine made from a project cannot start fresh sessions (create_trigger refuses `create_new_session_on_fire` there),
so the council project's coordinator carries it. The standing daily session made the fresh-session routine
`trig_01Q9mMcVwR4MCqHQzUHwcmiS` outside a project, with no repo attached; it was switched off on 2026-10-07 when
the pickup moved to pull, and never went into `PICKUP_TRIGGER`.

The page lost its `mcp` grant once, through a republish that passed `capabilities` with only `db`; the button then
showed "This view cannot reach Claude". Wendell restored it on 2026-10-06 (`pickup-send-permission`, then in chat at 23:23
UTC, because the publish with a connector grant needs his word in the session that makes it). Republish without
`capabilities`.

What the first firings showed, 2026-10-06:
- A routine made in a project thread with no target fires into that thread. One made with the coordinator as its
  target fired once into a fresh session with no repository (it stalled asking to add one), then into the coordinator
  itself. The prompt covers both: a fresh session finds the coordinator by its title with `list_sessions` and passes
  the message on.
- The firing at 20:01 UTC reached the coordinator, which started a Board read thread.
- A firing's `text` arrives as a second message after the prompt, so the prompt must not wait for it. The rows are in
  `pickup/last` too.
- Only the conversation a routine posts into can change its prompt. To change this one, delete it and create a new
  one from a project thread, then put the new id in `PICKUP_TRIGGER` and in the daily routine's step 1b.
- That firing's board read ran while another thread was doing one, and both recorded the same six saves. Their
  merge put conflict markers into main's `board_data.json` (fixed in 2b06dea). A board read that starts while
  another runs should wait for it and then read only what is still unrecorded.
- When the coordinator is replaced, check that this routine still reaches it (`get_trigger`, `last_run`).

### The daily safety net

The daily routine (`trig_01F8fDdkjYEeMCfdozj6w3tt`) gets a step 1b: save the store, run `board/unrecorded.py`, and
if anything is unrecorded, fire the pickup routine and write `pickup/last` with `via: "daily"`. Only the standing
daily session can change that prompt; the thread asked it to, and it did, on 2026-10-06.

### The lost Send of 2026-10-06 23:49 (fixed 2026-10-07)

The 23:49 Send fired the pickup routine into a fresh session (`session_01Q7kmX3qFH2GW6KRBpRwsTN`, origin
`force_run_trigger`) rather than the coordinator. That session had no repository, so it called `add_repo`, and adding a
repository restarts the container, which killed the board read it had started as a worker. It went round that loop for
five container epochs until 13:02 the next day and recorded nothing. Board read 2349 (2026-10-07) recorded the fifteen
saves. Two rules follow:

- A session the routine reaches that is not the coordinator never calls `add_repo` and never does the board read
  itself. It finds the coordinator and passes the message on, or starts a thread, since threads carry the project's
  repositories. The routine's prompt says so once the coordinator updates it (only the conversation the routine posts
  into can change its prompt).
- A board read always runs in a thread, never in a worker of the session the routine fired.

The other failure that night, at 23:31, was the coordinator's auto mode refusing to start a thread on a routine
firing, because a firing is not Wendell typing. A standing line in the project's instructions that the pickup routine
may always start a board read thread removes that refusal; Wendell adds it in Project settings.

### The stalled reads of 2026-10-07 22:31 to 2026-10-08 11:48 (fixed 2026-10-08)

The 22:31 Send's board read was stopped by container restarts four times and paused at 11:48 with six saves unconfirmed
(wave-exhale-ends, wave-offer-opens, wave-urges-all, wave-welcome-cost, steer/general, steps/oag-body-map-02). Every
retry paid the opening load again (about 120,000 to 140,000 tokens). All six were already on main (ledger
`2026-10-06-board-read-2330`), so the retries recorded nothing new.

What the record shows: the project chat has no thread card for that read, and `list_thread_sessions` has no thread for
it between 21:22 and 23:54, while every read that finished that night has a card ("Board read 2106", "2354"). The read
ran as a worker inside the coordinator's own session, which is the case the 23:49 rule above forbids. A worker dies
when its parent's container is replaced, and nothing was saved between steps, so each death meant a restart from the
opening load. The coordinator then "resumed" it, paying again.

Another leak sat beside it: a thread that has finished is woken by a webhook for any pull request it still watches
(the Ontology game steers thread was restarted at 23:48 by a merge on bars-engine #264, rereading 363,000 cached tokens
to answer with no_reply_needed).

Rules that follow:

- A board read runs in a thread started with `start_thread_session`, on Sonnet. Never in an `Agent` worker, never in
  the coordinator's or a routine session's own turns. If no thread card appeared, the read did not run as one.
- A stopped read is never resumed. The read is idempotent (`board/read.py` records only what main lacks), so the
  coordinator starts one fresh thread, once. If that thread also stops, the coordinator posts one line and waits for
  the next Send, since the next session's pull records the saves anyway.
- Before starting a retry, check main for the rows named in the message (`python3 board/unrecorded.py`). If they are
  recorded there is nothing to retry; say so and stop. That check costs one cheap call, not a read.
- A thread unsubscribes from a pull request the moment it merges (CLAUDE.md, short sessions).
