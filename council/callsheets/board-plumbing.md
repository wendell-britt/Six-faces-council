2026-10-07
# Board plumbing (pickup, pull, rows waiting)

## Next
- Check with `get_trigger trig_01L138vKTaN9MSJoFKRmaBNx` that the prompt says: pull, then act; never `add_repo`.
- Check the standing daily session carries step 1b for `trig_01F8fDdkjYEeMCfdozj6w3tt` (run pull.py, do not fire the pickup routine). That routine is switched off, not deleted (daily stopped 2026-10-08, `daily-stopped`).
- Read the store for answers saved after 2026-10-03T22:40Z, record them in a ledger record, republish.
- Small bug seen at board read 1714: the 17:12 Send did not rewrite `pickup/last`; nothing depends on that doc under pull.

## Waiting on
Wendell: a line in the project instructions pre-authorizing the board read thread. Board rows: `dy-model`, `dy-limit-wording` (#20), `dy-research-handoff`, `dy-2026-10-03-wake` (#21), `cost-quiet-wakes`, `cost-daily-script`, `cost-per-row`, `cost-short-rule` (#24). Pull requests #20, #21, #24 wait on his ruling; add `automerge` only when he says merge.
His Your steps tab: flirtcraft database steps 5 to 9 and the branch retire command.
Deferred: oracle drafts return 2026-11-03.

## Files
- `board/pull.py`, `docs/pickup.md`, `docs/incidents.md`, `council/due.py`
- `council/passes/6FACE_PASS10_2026-10-03.md`

## Archive
HANDOFF.md: "Open on 2026-10-03, when session_01BME8oqWjhm69ar2KZPiSDm handed off"; "Open on 2026-10-06, from the board pickup thread"; "Open on 2026-10-07, from the board read rerun (board read 2349)"; "Open on 2026-10-07, from the pickup hostile review"
