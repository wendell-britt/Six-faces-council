2026-10-08
# Cutting session cost (advisor thread)

## Brief, 2026-10-21: a cost ledger he can see (Sonnet build, then Opus only if a design call comes up)
Wendell, 2026-10-21: "It’s no good that we can’t see our token costs for cloud sessions because how are we supposed to improve".
The platform already gives every cloud session's cost and token split (`get_session` usage: cost_usd, cache_read, cache_write, output, used_tokens); the 10-18 audit read 107 of them by hand. What is missing is a standing view.
1. `council/tools/cost_ledger.py`: takes `get_session` rows (JSONL, the shape of `usage-audit/sessions-2026-10-18.jsonl`) and writes a table per thread kind and per day: cost, end size, past-150k and past-200k counts, model. Test on the 10-18 rows (must reproduce $627.64, 63 of 107 past 200k).
2. A daily routine (beside the compost pass) that lists the project's sessions, pulls usage for those that ended, appends to a ledger file in project files and republishes one dashboard page (Dashboard artifact type) with the 10-25 targets drawn on it: under 20% of threads end past 200k, median end under 150k.
3. Agent Beacon was scouted for this and rejected (council toolbox `agent-beacon`): it records no tokens on cloud sessions.
Note: the opening load is still the biggest single cost (this thread opened past 110,000 tokens before any work); the ledger should show first-call size per thread so that cut can be measured.

## Next
- `board-read-slim`: built 2026-10-08 (`board/read.py`, steps in docs/pickup.md). The next real read measures it against 30 steps and $1.54.
- `plugins-trim`: once Wendell ticks it (Customize > Plugins, ten plugins), the next board read compares its opening size (first_request_input_tokens) with 102,416.
- Still to measure: what else fills the opening 102,000 tokens (CLAUDE.md files of attached repos, hook output, platform prompt) and how much of a thread is command output (the Jev trimmer signal).

## Waiting on
Wendell: tick `plugins-trim` (he chose remove-business, 2026-10-08).

## Files
- project files `usage-audit/sessions-2026-10-08.md`, `reviews/2026-10-08-jev.md`
- `board/read.py`, `docs/pickup.md`
- `threads-on-sonnet` is written into project memory for the coordinator.

## Archive
HANDOFF.md: "Open on 2026-10-08, cutting session cost (advisor thread)"
