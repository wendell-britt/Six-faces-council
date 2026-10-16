2026-10-07
# Board plumbing (pickup, pull, rows waiting)

## Next
- `np-pull-alarm-age` is merged (bars-engine #336). Wendell answered `np-pull-trigger` with token (chat, 2026-10-16):
  bars-engine dispatches board-pull after each save (PR in bars-engine; docs/failure-modes.md has the line). Waiting on
  Wendell: create a fine-grained GitHub token for Six-faces-council (Actions read and write only) and set it in Vercel
  as `BOARD_DISPATCH_TOKEN`. Until then saves fall back to the cron and the page alarm. Open follow-up: the option
  promised the page says so when the token has expired; not built.
- `board-home` (Wendell, chat, 2026-10-16): bars-engine becomes the one home of the Council Board. Spec kit at
  bars-engine `.specify/specs/board-home/`. Built 2026-10-16 (bars-engine commit eb41f7eb on main):
  (1) DONE — `/board/council` serves `board/council-board.html` from main behind the owner sign-in; serving logic
  shared with `/board` in `src/app/board/serve.ts` (5-minute cache, wrap, owner gate; redirect `returnTo=/board/council`).
  (2) DONE — shim is `boardShim(board, returnTo)`; the council page's store calls are identical to the nonprofit
  page's (same collections: steer, steps, blockers, contacts, shows, lists, pickup, morning, ttv, picks plus
  positions/questions/terms/causes; same two mcp calls: `fire_trigger` on Claude Code Remote, `web_fetch_vercel_url`
  on Vercel), so no new capability was needed — the Send button shows the page's own not-granted message on
  bars-engine, as on /board. (3) DONE — confirmed: `BOARDS` already has `'council'` in `src/lib/board/save.ts` and
  `fixtures/board-saves/board-save.schema.json` (contract tests pass); `/api/board/pull` takes `board` as a parameter;
  `board/fetch_store.py` takes `BOARD` as an env var. Follow-up: the board-pull Action runs with `BOARD: nonprofit`;
  it needs a council pass (or a second job) once the page is live. (4) LEFT — move the artifact's saved store into
  Postgres once, so no save is lost: needs ArtifactData from a Claude session signed in to the owning organization.
  (5) LEFT, ordered after 4 — point AGENTS.md, CLAUDE.md, docs/pickup.md and the pickup routine at the new page and
  store (pointing them over before the store is moved would read an empty Postgres). (6) LEFT — retire the artifact
  after a few clean days. One owner only by design (`BOARD_OWNER_PLAYER_ID`); other people editing the board is a
  separate ask.
  Follow-up in bars-engine #338 (draft, on main's board-home): the council page's Send bar is patched at serve time (button
  hidden, "saved and waiting for the board pull", as board/nonprofit/build.py does), `/api/board/pull` rejects a `board`
  other than nonprofit or council, tests for both. Another session landed steps 1-3 first; #338 was merged onto it.
- Stopgap until then: the Council Board artifact (https://claude.ai/artifact/DxyShVS8tmvJym4HAsgnho) needs one republish
  from a session signed in to its organization (Wendell, 10 am 2026-10-16), since main has rows the live page lacks.
- Write-race remediation (2026-10-16, from zo-environment pass 1 + two absorbed collisions the same day):
  (1) fetch before you record, push immediately after — DONE: the standing line is in `council-sync.sh` output
  (home commit 4463914, reaches every repo at its next session start); (2) rulings stay append-only ledger files, and
  `board_data.json` row-moves ride in the same commit as the ruling's ledger record, so a rebase resolves a ruling
  atomically; (3) no lock service.
  Both 2026-10-16 collisions (zo-environment pass push vs steward PR #178; chat-ruling recording vs PR #181) were
  absorbed by fetch, rebase, row-union, rebuild at about two minutes each. The hook line goes in with the
  board-home build thread; np-pull-trigger (push per save) raises collision frequency and makes the discipline
  load-bearing rather than optional. The line is in (home, 4463914).
- `board-home` build thread (2026-10-16, bars-engine eb41f7eb on main): steps 1-3 are done.
  (1) `/board/council` serves `board/council-board.html` behind the owner sign-in — shared serving in
  `src/app/board/serve.ts` (5-minute page cache, wrap, `isBoardOwner`), shim parameterized as
  `boardShim(board, returnTo)`; the council page's store calls are identical to the nonprofit page's, so
  no new shim capability was needed (the Send button's `fire_trigger` stays ungranted on bars-engine and
  the page handles it gracefully). Spec kit cut from council/spec-kit/ into
  bars-engine `.specify/specs/board-home/`. (2) `/api/board/pull` and `board/fetch_store.py` confirmed
  board-aware (`board=council`; fetch_store takes the `BOARD` env). 29 board tests pass in bars-engine.
  (3) council-sync home-copy check now ignores URL case — the case-sensitive compare made the home repo
  revert its own shared files from remote main and ate the first discipline-line edit.
  Left, in order, for a Claude session signed in to the owning organization (needs ArtifactData):
  move the artifact's saved store into Postgres as `board=council` (no save lost), then point
  AGENTS.md, CLAUDE.md, docs/pickup.md and the pickup routine at `/board/council` + Postgres,
  then retire the artifact after a few clean days. Follow-up when the migration lands: give
  board-pull.yml a council pass (fetch/pull/ack with `BOARD=council`); the current run is nonprofit-only.
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
- Session note (2026-10-16, board-home build thread): `council-sync.sh` ran in the home clone and pulled remote main
  over uncommitted shared-file edits — the home-copy check compared `origin` (`Six-faces-council`) case-sensitively
  against `council/source.txt` (`six-faces-council`). Fixed in the same commit (4463914): the comparison now ignores
  case. If a shared-file edit vanishes at session start, this was why.
