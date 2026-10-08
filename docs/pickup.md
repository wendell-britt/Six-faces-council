# Board pickup

Wendell, 2026-10-06, in the podcast thread: "What triggers you to check the board and how can we automate that?"
Nothing did. His podcast answers sat unread for 25 minutes, and the daily run of 2026-10-04 found 23 saves no session
had read. Board row `board-auto-pickup` set out the fix; this is how it works.

## Pull, not push (2026-10-07)

Wendell chose `pickup-pull-model` A after the hostile review (council/research/2026-10-07-pickup-hostile-review.md).
The board's store is the record of his answers. `board/pull.py` copies every save main lacks into `board_data.json`
and a ledger record, rebuilds, and pushes to main. It takes no judgment, runs the same twice, and any session with
the repo can run it: the board read a Send starts, the daily run, and any session about to act on a ruling (CLAUDE.md,
the session-start hook, the skill). A Send that never arrives now costs a delay until the next session pulls; it
cannot strand an answer. What pull.py lists under `needs work` (a question's pick, an overrule, a steer) is what the
session acts on.

Two runs at once are safe: resolved entries join by id through the board merge driver, and the ledger file is named
after the newest save it records, so two runs that see the same saves write the same file. That replaces the
"a board read that starts while another runs should wait" rule, now in docs/incidents.md.

The routines after the change: `trig_01L138vKTaN9MSJoFKRmaBNx` stays as the Send target, and its prompt shrinks to
"start a board read thread; it pulls, then acts". `trig_01DpRsDM94Cnv2neyDVkBNMb` (the Flirtcraft coordinator) and
`trig_01Q9mMcVwR4MCqHQzUHwcmiS` (fresh session, no repo) are switched off, which reverses `pickup-where`. The daily
routine's step 1b runs pull.py itself instead of firing the pickup routine, so the safety net no longer depends on the
chain it backs up. The push design's history and its incidents are in docs/incidents.md (retro 1).

## A board read in five steps (2026-10-08, board-read-slim)

The 00:25 board read took 30 steps and $1.54 because every step rereads a session that opens at about 102,000 tokens.
`board/read.py` folds the plumbing into one command, so a read is:

1. One message with five parallel ArtifactData `list` calls (positions, questions, terms, causes, steer), one
   `out_dir`. The store lands in files; it is never read into the conversation, and the page is never read.
2. `python3 board/read.py <dir>`: pull.py with `--push`, `council/due.py --ahead 7`, and a last line that says
   whether to republish. Add `--dry` to report without writing.
3. If it says REPUBLISH, one Artifact call on `board/council-board.html`, no capabilities. When every save was
   already recorded there is nothing to republish.
4. Act on the `needs work` list, one thread per piece of work.
5. One reply. No question in it.

unrelated histories" on the 2026-10-08 trial.

Reads that stop (2026-10-08): a read is never resumed. It is idempotent, so a stopped one is replaced by one fresh
thread, and only after `python3 board/unrecorded.py` shows rows main still lacks. It runs in a thread from
`start_thread_session`, never in an Agent worker of the coordinator. The reason is in docs/incidents.md.

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

`trig_01L138vKTaN9MSJoFKRmaBNx` has no schedule; the Send button fires it. A board read always runs in a thread that
the council project's coordinator starts, and that thread pulls, then acts. Republish the board without
`capabilities`, so the `mcp` grant carries forward.

### Where a Send lands (2026-10-07, 20:37 Send)

The routine is bound to the coordinator (`persistent_session_id`), but a Send does not reliably wake it. At 20:37 UTC
the button's `fire_trigger` started a new session titled "⚡ Council board: pick up Wendell's saves (council project)"
(origin `force_run_trigger`) while the binding pointed at the live coordinator. The same happened once on 2026-10-06.
So plan for every Send landing in a fresh session that has no `start_thread_session` tool.

What broke was the fallback. The prompt told that session to find the coordinator and `send_message` it. Coordinators
are recycled and get a new session id each time (`session_016Yw4J6vYgt5h3grAHh7NmK`, then
`session_0141631xFabQPhsk4de2UWtb`), so a search by title finds old ones too. It picked the archived "Game master
agents system" session, the send failed as inactive, and the fresh session posted a failure line in the project chat.

That failure line is what got the board read started: the coordinator is woken by every project-chat post, and it
started board read 2037 a minute later. A project-chat post is the one route from a routine session that reaches
whichever session is coordinator now, so the fallback is that post, on purpose:

- A routine session with no `start_thread_session` tool never searches for the coordinator, never calls
  `send_message` or `add_repo`, and does no board read. It posts one line in the project chat with `post_message`:
  "Board Send at <time UTC>: <rows from the payload>. Starting a board read." Then it ends its turn.
- The coordinator treats that line like the routine firing into itself: it starts one board read thread on that
  post, with no further project-chat line.
- Nothing names a coordinator session id, so a recycled coordinator needs no change here. Rebinding the routine after
  a recycle still helps on the Sends that do reach it directly.

The routine prompt that carries this, set by the coordinator (only the conversation a routine posts into can edit it):

    This is a Council Board pickup. Wendell saved answers on the Council Board
    (https://claude.ai/artifact/DxyShVS8tmvJym4HAsgnho) and pressed Send to Claude. A second message names the
    rows; do not wait for it.

    If you have the start_thread_session tool, you are the coordinator of the "6 face game master council" project.
    Start one thread now for a board read, with no project-chat line beyond the thread's own. Brief it to work in
    repo wendell-britt/six-faces-council on main and follow its CLAUDE.md: save the board's store with ArtifactData
    (positions, questions, terms, causes, steer) into one folder, run python3 board/pull.py <folder>
    --push, republish board/council-board.html without passing capabilities, and act on the "needs work" list
    pull.py prints (ask you for a thread for each new piece of work). pull.py is safe to run twice. If pull.py
    records nothing, the thread says so in one line and resolves itself.

    If you do not have start_thread_session, you are a session this routine started, and the coordinator will hear
    you only through the project chat. Do not look for the coordinator, and do not call send_message, add_repo or
    any repo or board tool. Call mcp__hearthbot__post_message once with one line: "Board Send at <time UTC>:
    <the rows named in the second message, or 'rows in pickup/last'>. Starting a board read." Then end your turn
    with no other message. Nothing is lost if this fails: the next council session's pull records the saves.
