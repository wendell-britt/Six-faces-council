2026-10-07
# Board plumbing (pickup, pull, rows waiting)

## Next
- `np-pull-alarm-age` is merged (bars-engine #336). Wendell answered `np-pull-trigger` with token (chat, 2026-10-16):
  bars-engine dispatches board-pull after each save (PR in bars-engine; docs/failure-modes.md has the line). Waiting on
  Wendell: create a fine-grained GitHub token for Six-faces-council (Actions read and write only) and set it in Vercel
  as `BOARD_DISPATCH_TOKEN`. Until then saves fall back to the cron and the page alarm. Open follow-up: the option
  promised the page says so when the token has expired; not built.
- `board-home` (Wendell, 2026-10-16, board row `board-home`, decision "bars-engine"): first half built in bars-engine #338
  (draft; Wendell merges after the Vercel check): `/board/council` serves `board/council-board.html` from main behind
  the owner sign-in, shim board constant `council`, Send bar patched at serve time (a save starts its own board-pull),
  `/api/board/pull` validates `board`. The council page's store calls all fit the existing save contract, so schema and
  fixtures did not change. Left, each in a fresh thread:
  - Pull the council board on main: `.github/workflows/board-pull.yml` has `BOARD: nonprofit` only, so council saves
    are not recorded until it runs the same steps with `BOARD=council` (a matrix or a second job), and
    `board/pull.py` with the council board's room flag (it runs `--no-room` for the nonprofit). Also build.py for the
    council page is not needed (board/build_board.py already writes it). Then check `board/staleness.py` per board.
  - Move the artifact's saved store into Postgres once, so no save is lost: needs a session signed in to the artifact's
    organization (`/login` there); read each collection with ArtifactData, POST each doc to `/api/board/saves`
    (`board: council`) or insert `BoardSave` rows with the original times, marked recorded where main holds them.
  - Republish the artifact (stopgap) from that same session; main has rows the live page lacks.
  - Point AGENTS.md, CLAUDE.md, docs/pickup.md and the pickup routine at https://bars-engine.vercel.app/board/council
    and the Postgres store (`fetch_store.py` with `BOARD=council`).
  - Retire the artifact only after `/board/council` has run clean for a few days. One owner only by design
    (`BOARD_OWNER_PLAYER_ID`); other people editing the board is a separate ask.
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
