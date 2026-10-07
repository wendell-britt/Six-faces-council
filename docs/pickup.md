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

`trig_01L138vKTaN9MSJoFKRmaBNx` has no schedule; the Send button fires it, and it wakes the council project's
coordinator, which starts one board read thread. That thread pulls, then acts. A session the routine reaches that is
not the coordinator never calls `add_repo` (it restarts the container) and never does the board read itself.
Republish the board without `capabilities`, so the `mcp` grant carries forward.
