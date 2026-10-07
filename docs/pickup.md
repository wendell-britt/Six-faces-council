# Board pickup

Wendell, 2026-10-06, in the podcast thread: "What triggers you to check the board and how can we automate that?"
Nothing did. His podcast answers sat unread for 25 minutes, and the daily run of 2026-10-04 found 23 saves no session
had read. Board row `board-auto-pickup` set out the fix; this is how it works.

## The Send to Claude button

`board/template.html` shows a bar at the bottom of the board once anything is saved and not yet sent: a row saved and
not yet recorded, the context box, or a step ticked, noted or moved. Its button calls the Claude Code Remote
connector's `fire_trigger` as Wendell, on the pickup routine (`PICKUP_TRIGGER` in the template), with the list of rows,
and writes the same list to the store's `pickup/last` doc (`{sentAt, rows}`). The bar hides once everything saved is
older than the last send. Each failure code gets its own message; a view without the connector says to tell Claude in
chat instead.

The page declares two capabilities: `db` (its store) and `mcp` with server `Claude Code Remote`, tool `fire_trigger`.
A republish that omits `capabilities` keeps both. A republish that passes `capabilities` must pass both:

    {"db": {}, "mcp": {"servers": [{"server": "Claude Code Remote", "tools": ["fire_trigger"]}]}}

## The pickup routine

`trig_01L138vKTaN9MSJoFKRmaBNx`, "Council board: pick up Wendell's saves (council project)", has no schedule; only the
button and the daily run fire it. It wakes the coordinator of the 6 face game master council project
(`session_016Yw4J6vYgt5h3grAHh7NmK`), which starts one thread for a board read. It replaced
`trig_01DpRsDM94Cnv2neyDVkBNMb`, which woke the Flirtcraft project's coordinator, on 2026-10-06.

Wendell chose a fresh session per Send (`pickup-where`, board read 2004) so the pickup belongs to no project. A
routine made from a project cannot start fresh sessions (create_trigger refuses `create_new_session_on_fire` there),
so the council project's coordinator carries it. The standing daily session made the fresh-session routine
`trig_01Q9mMcVwR4MCqHQzUHwcmiS` outside a project; it goes into `PICKUP_TRIGGER` once its environment carries the
council repo and one test firing has worked. The daily routine's step 1b fires whatever `PICKUP_TRIGGER` names.

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

## The daily safety net

The daily routine (`trig_01F8fDdkjYEeMCfdozj6w3tt`) gets a step 1b: save the store, run `board/unrecorded.py`, and
if anything is unrecorded, fire the pickup routine and write `pickup/last` with `via: "daily"`. Only the standing
daily session can change that prompt; the thread asked it to, and it did, on 2026-10-06.

## The lost Send of 2026-10-06 23:49 (fixed 2026-10-07)

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
