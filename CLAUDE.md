# Working rules: six-faces-council

Any other agent reads `AGENTS.md`, which carries these rules; `tests/test_agents_md.py` keeps the two in step.

This file is loaded on every turn, so the council's rules survive a long session being summarized. Before
2026-10-03 the board rule below reached a session only through the session-start hook and the skill. In one long
session, a summary dropped it and kept friendcraft's "the ask, stated as a question", and five questions reached
Wendell in chat. His words: "These questions shouldn't be showing up here".

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

Wendell, 2026-10-03: "Ok this is important and maybe one of the rules that will save us the most. I know Claude’s
projects does short conversational threads and then archives if we can achieve that level of discipline OR use
projects more effectively between that and Jev we can save a lot of tokens"

- One session does one piece of work: a board read, a pass, or a feature. Every tool call rereads the whole
  session, so a long session pays for its past on every step (pass ten measured $0.14 a call at 679,000 tokens).
- End at a natural boundary. Record the work in the repo and on the board, put anything left open in
  `council/callsheets/<strand>.md` (and `INDEX.md`), appending to `council/HANDOFF.md` only as the archive, and stop.
  The next piece of work starts in a new thread that reads this file, `council/callsheets/INDEX.md`, the one sheet
  for its strand and the board (Wendell, `st-callsheets`, 2026-10-10).
- A handoff starts the next thread; it does not wait for Wendell. When a thread stops with work left (the next art
  round, the rest of a feature), it writes the brief to its callsheet, sends the coordinator a message asking it to
  start the next thread now (naming the brief and any pull request the new thread owns), drops its own pull request
  watches, and resolves itself. The coordinator starts that thread without asking (Wendell, 2026-10-14: "A major
  issue is we aren't picking up work automatically and closing threads when they are done").
- Strands with a next-round contract (`council/loops/<strand>.json`, docs/loops.md; spirit-generator is the pilot)
  continue without asking: a finished round runs `python3 council/loops/next_round.py finish <strand> <n>`, and when
  the tool says the next round may start (gate auto, at most two rounds past his last look) the handoff names it and
  the coordinator starts it. Record each look of his with `next_round.py look`, which also writes the labels file.
- Drop a pull request watch once the pull request merges. Pull requests merge by themselves once they are ready and
  their checks pass (docs/merging.md, Wendell, 2026-10-06); only a `council/faces.yaml` change or a daily branch
  waits for his label.
- Name the session's cost in its last report, read from the platform after the work, never mid-turn.
- Hand off before the context passes 150,000 tokens, even mid-feature. Check with `python3
  council/tools/context_size.py` at each milestone; do not guess. The 18 October audit measured 90% of spend as the
  context carried forward (65% rereading, 25% writing it to cache), up from 84% on 4 October, and threads that
  ran past 200,000 tokens were 63 of 107 and $504 of $628 (`/mnt/project-files/usage-audit/audit-2026-10-18.md`).
  An art review gets one thread per round.
  A PostToolUse hook (`.claude/settings.json`, `council/tools/context_size.py --hook`) now adds the handoff order to every tool result once the context passes the line, so the check no longer depends on remembering it (2026-10-18; the 63 of 107 threads past the old line ran as few long turns, median 2 replies, with no user message to prompt a stop).
- Every call rereads everything above it, so a call saved is a reread saved: batch independent tool calls into one
  step, and send work that reads many files, images or logs (render checks, searches, CI logs) to an Agent worker
  that returns a short verdict, so the reading never enters the thread.
- Long jobs (Root renders, batches, test loops, sprite rebuilds) run in the background and write a short summary
  file. The thread reads that summary once when the job ends. It does not check in on the job while it runs.
- Clerical work runs on Sonnet when the model can be chosen: recording board answers, landing rows, merges,
  steward work, packaging, and rebuilds once the design is settled. Root's solver work, council passes, new
  design and first story drafts stay on Opus. Fable runs only when Wendell asks for it by name. Sonnet saves
  about a quarter, not half, because rereading context costs the same on both models.

## Check for a tool before building

- Before building anything new (a round, a model, a rig, an animation, a solver, a game system), climb the tool ladder
  in `docs/tool-scout.md` and stop at the first rung that holds: does it need to exist, do we have it, does a known
  tool do it (`python3 council/tools/scout.py <job>`, reading `council/toolbox.yaml`), does an unknown one (one worker
  search, keepers added to the toolbox). Build by hand only after that, and record the rung in a `scout:` line
  (Wendell, 2026-10-18: "Essentially a hack of ponytail but for asset pipeline and 3d production").
- A build proves itself the cheapest way first (a probe number before a still, a still before a sheet or video),
  leaves a check the next round can rerun, and ends its report with what was not checked (docs/tool-scout.md,
  "Building it small").

## Where the rest lives

- The council's skill: `.claude/skills/six-faces/SKILL.md`. The pipeline: `council/pipeline.yaml`.
- The game-design ontology: `ontology/manifest.yaml`. For game design or game building, load
  `.claude/skills/design-ontology/SKILL.md`; do not load the complete provenance archive by default. Clerical
  flows load none of it: `docs/ontology-in-flows.md` says which flow loads what.
- Before acting on any ruling, pull the board: save its store with ArtifactData and run `python3 board/pull.py
  <dir> --push`. Saved answers reach main this way, from any session, safe to run twice; the Send button only asks
  for the work to start (Wendell, `pickup-pull-model`, 2026-10-07; docs/pickup.md).
- Board data, ledger records and lessons are written on main only. Rows reach main through `board/sync_board.py`
  (see docs/merging.md), which also brings over anything the live page has that main lacks; a board-only pull request
  merges without the label (Wendell, 2026-10-04). `council/faces.yaml` changes only by his ruling.
- Deferred items: run `python3 council/due.py --ahead 7` at the start of every board read.
- Run `python3 council/tools/voice_lint.py` on anything he reads. Never alter his quoted words.
