2026-10-07
# Board plumbing (pickup, pull, rows waiting)

## Next
- `np-pull-alarm-age` is merged (bars-engine #336). Wendell answered `np-pull-trigger` with token (chat, 2026-10-16):
  bars-engine dispatches board-pull after each save (PR in bars-engine; docs/failure-modes.md has the line). Waiting on
  Wendell: create a fine-grained GitHub token for Six-faces-council (Actions read and write only) and set it in Vercel
  as `BOARD_DISPATCH_TOKEN`. Until then saves fall back to the cron and the page alarm. Open follow-up: the option
  promised the page says so when the token has expired; not built.
- `board-home` (Wendell, chat, 2026-10-16): bars-engine becomes the one home of the Council Board. Build in a fresh thread:
  (1) bars-engine route `/board/council` (or a `board` parameter on `/board`) serving `board/council-board.html` from
  main behind the owner sign-in, like src/app/board/route.ts; (2) extend the page shim for whatever the council page
  calls beyond the nonprofit page's store calls (check `pickup` and every collection it reads); (3) confirm
  /api/board/pull and `board/fetch_store.py` handle `board=council` and its documents; (4) move the artifact's saved
  store into Postgres once, so no save is lost (read it with ArtifactData from the owning organization); (5) point
  AGENTS.md, CLAUDE.md, docs/pickup.md and the pickup routine at the new page and store; (6) retire the artifact after
  a few clean days. One owner only by design (`BOARD_OWNER_PLAYER_ID`); other people editing the board is a separate ask.
- Stopgap until then: the Council Board artifact (https://claude.ai/artifact/DxyShVS8tmvJym4HAsgnho) needs one republish
  from a session signed in to its organization (Wendell, 10 am 2026-10-16), since main has rows the live page lacks.
- Write-race remediation (2026-10-16, from zo-environment pass 1 + two absorbed collisions the same day):
  (1) fetch before you record, push immediately after — one standing line in `council-sync.sh` output reaches every
  council repo at session start; (2) rulings stay append-only ledger files, and `board_data.json` row-moves ride in
  the same commit as the ruling's ledger record, so a rebase resolves a ruling atomically; (3) no lock service.
  Both 2026-10-16 collisions (zo-environment pass push vs steward PR #178; chat-ruling recording vs PR #181) were
  absorbed by fetch, rebase, row-union, rebuild at about two minutes each. The hook line goes in with the
  board-home build thread; np-pull-trigger (push per save) raises collision frequency and makes the discipline
  load-bearing rather than optional.
- Step notes (2026-10-12, #87): a board read now lists six collections, steps included. The coordinator updates the pickup routine prompt to name `steps` (docs/pickup.md has the text). Act on the 8 needs-work items in council/ledger/2026-10-12-pull-170058.json: copy-paste terminal instructions as a rule for every step (morning-menu-key-02), gs-1 step-by-step with file location, two links on flirtcraft-own-database-06, an unblocking process for virtual-launch-restart-01.
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
