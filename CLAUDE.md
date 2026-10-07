# Working rules: six-faces-council

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

## Short sessions

Wendell, 2026-10-03: "Ok this is important and maybe one of the rules that will save us the most. I know Claude’s
projects does short conversational threads and then archives if we can achieve that level of discipline OR use
projects more effectively between that and Jev we can save a lot of tokens"

- One session does one piece of work: a board read, a pass, or a feature. Every tool call rereads the whole
  session, so a long session pays for its past on every step (pass ten measured $0.14 a call at 679,000 tokens).
- End at a natural boundary. Record the work in the repo and on the board, put anything left open in
  `council/HANDOFF.md`, and stop. The next piece of work starts in a new thread that reads this file,
  HANDOFF.md and the board.
- Drop a pull request watch once the pull request merges. Pull requests merge by themselves once they are ready and
  their checks pass (docs/merging.md, Wendell, 2026-10-06); only a `council/faces.yaml` change or a daily branch
  waits for his label.
- Name the session's cost in its last report, read from the platform after the work, never mid-turn.
- Hand off before the context passes about 200,000 tokens, even mid-feature. The 4 October usage audit found
  84% of spend was rereading context (`/mnt/project-files/usage-audit/audit-2026-10-04.md`). An art review
  gets one thread per round.
- Long jobs (Root renders, batches, test loops, sprite rebuilds) run in the background and write a short summary
  file. The thread reads that summary once when the job ends. It does not check in on the job while it runs.
- Clerical work runs on Sonnet when the model can be chosen: recording board answers, landing rows, merges,
  steward work, packaging, and rebuilds once the design is settled. Root's solver work, council passes, new
  design and first story drafts stay on Opus. Fable runs only when Wendell asks for it by name. Sonnet saves
  about a quarter, not half, because rereading context costs the same on both models.

## Where the rest lives

- The council's skill: `.claude/skills/six-faces/SKILL.md`. The pipeline: `council/pipeline.yaml`.
- Before acting on any ruling, pull the board: save its store with ArtifactData and run `python3 board/pull.py
  <dir> --push`. Saved answers reach main this way, from any session, safe to run twice; the Send button only asks
  for the work to start (Wendell, `pickup-pull-model`, 2026-10-07; docs/pickup.md).
- Board data, ledger records and lessons are written on main only. Rows reach main through `board/sync_board.py`
  (see docs/merging.md), which also brings over anything the live page has that main lacks; a board-only pull request
  merges without the label (Wendell, 2026-10-04). `council/faces.yaml` changes only by his ruling.
- Deferred items: run `python3 council/due.py --ahead 7` at the start of every board read.
- Run `python3 council/tools/voice_lint.py` on anything he reads. Never alter his quoted words.
