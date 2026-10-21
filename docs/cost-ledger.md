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

1. `list_sessions` (limit 100, pages back until a session older than the newest `created_at` in the ledger, minus two days).
2. `get_session` on each session that is not working, in one message per ten ids, writing each reply as one JSON line to a new
   file. A session still working is skipped; it is taken on a later day.
3. Run the script above with `--flat`.
4. Upload `kinds.json`, `days.json`, `targets.json` to the dashboard (Artifact `asset: true`, one call per file), then `update`
   each of `datasets/ledger_kinds`, `ledger_days`, `ledger_targets` with the new `url` and `updated.at`. Delete the old assets.
5. Reply in one line with the day's cost, the share past 200k and the median end, and no question.

Not measured: the platform gives no first-call size, so the dashboard's "median first call" stays blank unless a row carries
`first_request_input_tokens`. Prices are the platform's, not inferred.
