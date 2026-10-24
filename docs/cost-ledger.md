# The cost ledger

Wendell, 2026-10-21: "It's no good that we can't see our token costs for cloud sessions because how are we supposed to improve".

The platform reports each cloud session's cost and token use (`get_session`: `usage.cost_usd`, `used_tokens`, `last_served_model`).
The ledger keeps those rows and shows them in one place.

- Dashboard: https://claude.ai/artifact/SzZM89iA46UJUAcF6utHkd (cost by thread kind and by day, with the 25 October targets).
- Ledger file: `/mnt/project-files/usage-audit/ledger.jsonl`, one `get_session` row per line, seeded with the 107 sessions of the
  18 October audit. A row is replaced when a later pull has a later `updated_at`.
- Script: `python3 council/tools/cost_ledger.py new-rows.jsonl --ledger /mnt/project-files/usage-audit/ledger.jsonl --flat <dir> --md <file>`.
  Test: `tests/test_cost_ledger.py` reproduces $627.64 and 63 of 107 past 200,000 tokens.
- Targets (council #272), checked on 25 October: under 20% of threads end past 200,000 tokens; median end under 150,000.
- Kinds come from the title (`kind()` in the script); the audit's own split differs by a few threads.

## The daily routine

Fires beside the compost pass and starts one Sonnet thread, which does these steps and stops:

1. `list_threads` (the hearthbot tool, `since` the newest `created_at` in the ledger minus two days, `limit` 100, following
   `next_cursor` until a page adds nothing in range; the pages are not in date order). `list_sessions` does not show project
   threads (2026-10-24: it listed nothing after 20 October), so it is not used. A thread's `session_id` is `cse_<x>`; its
   `get_session` id is `session_<x>`. Keep threads whose `last_activity_at` is later than the newest `updated_at` in the ledger.
2. `get_session` on each such thread that is not working, ten per message, in one Sonnet worker that writes each reply as one
   JSON line (keys as in the ledger; `usage` is `external_metadata.usage`, `used_tokens` and `max_tokens` are
   `external_metadata.context_usage`) to a new file. Copy ids from the listing by script, not by hand; a mistyped id returns
   "not found". A session still working is skipped; it is taken on a later day.
3. Run the script above with `--flat`.
4. Upload `kinds.json`, `days.json`, `targets.json` to the dashboard (Artifact `asset: true`, one call per file), then `update`
   each of `datasets/ledger_kinds`, `ledger_days`, `ledger_targets` with the new `url` and `updated.at`. Delete the old assets.
5. Reply in one line with the day's cost, the share past 200k and the median end, and no question.

Not measured: the platform gives no first-call size, so the dashboard's "median first call" stays blank unless a row carries
`first_request_input_tokens`. Prices are the platform's, not inferred.
