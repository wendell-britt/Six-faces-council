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
so the council project's coordinator carries it until a fresh-session routine is made outside a project, from a
plain Claude Code session or the routines page. Its environment must carry the council repo.

The page lost its `mcp` grant once, through a republish that passed `capabilities` with only `db`; the button then
showed "This view cannot reach Claude". Wendell said yes to restoring it on 2026-10-06 (`pickup-send-permission`); the
publish with the grant still needs his approval in the session that makes it. Once restored, republish without
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
