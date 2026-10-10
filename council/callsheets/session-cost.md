2026-10-08
# Cutting session cost (advisor thread)

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
