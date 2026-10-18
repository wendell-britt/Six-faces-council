# Working rules for any agent: six-faces-council

This file is for any coding agent (Codex, Claude, or another) and for people. It carries the same rules as
`CLAUDE.md`, which Claude loads on every turn. `tests/test_agents_md.py` keeps them in step: every section of
`CLAUDE.md` has a section of the same name here, and the board rules below are word for word the same. Where
`CLAUDE.md` names a Claude-only tool, the section here says what any agent does instead.

## Questions go to the board, never to chat

- Every question for Wendell goes on the Council Board, https://claude.ai/artifact/DxyShVS8tmvJym4HAsgnho, as a
  row in `board/board_data.json` on main, rebuilt and republished. Run the reach test first (`reach_test` in
  `council/faces.yaml`). A question the record can answer becomes a position that stands unless he flips it.
- A chat reply says what changed and names the new board rows with the link. It ends without a question.
- A question that comes up mid-build, outside a pass, is still a council question. Put it through the reach test
  and onto the board like any other.
- The board process supersedes any repo rule that puts the ask in the reply (Wendell, 2026-10-03: "This process
  also superseded friendcraft so we need to change that rule there too"). friendcraft's CLAUDE.md now says the same
  (friendcraft-manuacript #27).
- An answer he gives in chat counts as a ruling. Record it the way a board answer is recorded. A chat answer does not
  make the next question a chat question.


## The Nonprofit Board's saves

- The Nonprofit Board is served by bars-engine at https://bars-engine.vercel.app/board behind Wendell's own sign-in,
  and every save goes to Postgres through bars-engine's API (POST /api/board/saves). Its rows are the `np-` rows of
  `board/board_data.json` on main; bars-engine reads `board/nonprofit/nonprofit-board.html` from main, so a row that
  lands on main is on the board without a republish.
- Saves reach main through `.github/workflows/board-pull.yml` every 15 minutes, with no AI involved:
  `board/fetch_store.py fetch`, `board/pull.py --push --no-room`, `council/morning.py` for a pasted menu,
  `board/nonprofit/build.py`, `board/fetch_store.py ack`, then `board/staleness.py`, which fails the run when a save
  has waited more than six hours. Anyone with `BOARD_PULL_TOKEN` can run the same lines by hand.
- A save follows `schema/board-save.schema.json`. A change to the save shape changes the schema, the fixtures in
  `tests/fixtures/board-saves` and bars-engine's copy of both in one pair of pull requests; `tests/test_save_contract.py`
  and bars-engine's `board-save-contract.test.ts` must both pass.
- What his answers still ask for is the needs-work list: `python3 board/needs_work.py`. Finish an item with the change it
  asks for and one entry for its key in `council/needs-work-done.json`, in the same pull request. A needs-work item
  that turns into a question for him goes through the reach test and onto the board like any other question.
- Why it works this way, and what each step depends on: `docs/failure-modes.md`.

## Short sessions

`CLAUDE.md` holds the full rule and Wendell's words. For any agent:

- One session does one piece of work: a board read, a pass, a feature, or one needs-work item.
- End at a natural boundary. Record the work in the repo (and on the board when it is a ruling), put anything left open
  in `council/callsheets/<strand>.md` and `council/callsheets/INDEX.md`, and stop.
- Pull requests merge by themselves once ready and green (`docs/merging.md`); only a `council/faces.yaml` change or a
  daily branch waits for his label. Do not open a second pull request for work an open one covers.
- Long jobs run in the background and write a short summary file; read it once when the job ends.
- Hand off before the context passes 150,000 tokens. Every call rereads the whole context, so batch independent
  calls and keep bulk reading (images, logs, searches) out of the main session.
  A PostToolUse hook (`.claude/settings.json`, `council/tools/context_size.py --hook`) now adds the handoff order to every tool result once the context passes the line, so the check no longer depends on remembering it (2026-10-18; the 63 of 107 threads past the old line ran as few long turns, median 2 replies, with no user message to prompt a stop).
- Name the session's cost in its last report if your platform shows it.

## Check for a tool before building

- Before building anything new (a round, a model, a rig, an animation, a solver, a game system), climb the tool ladder
  in `docs/tool-scout.md` and stop at the first rung that holds: does it need to exist, do we have it, does a known
  tool do it (`python3 council/tools/scout.py <job>`, reading `council/toolbox.yaml`), does an unknown one (one worker
  search, keepers added to the toolbox). Build by hand only after that, and record the rung in a `scout:` line
  (Wendell, 2026-10-18: "Essentially a hack of ponytail but for asset pipeline and 3d production").

## Where the rest lives

- The council's method: `.claude/skills/six-faces/SKILL.md` (plain Markdown; any agent can read it). The pipeline:
  `council/pipeline.yaml`. The faces and the reach test: `council/faces.yaml`.
- The game-design ontology: `ontology/manifest.yaml`. Which flow loads what: `docs/ontology-in-flows.md`.
- Board data, ledger records and lessons are written on main only, through `board/pull.py` (saves) and
  `board/sync_board.py` (rows; `docs/merging.md`). `council/faces.yaml` changes only by his ruling.
- Deferred items: `python3 council/due.py --ahead 7`.
- Run `python3 council/tools/voice_lint.py` on anything he reads. Never alter his quoted words.
- Tests: `python3 -m pytest -q tests`.
