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

## Where the rest lives

- The council's skill: `.claude/skills/six-faces/SKILL.md`. The pipeline: `council/pipeline.yaml`.
- Board data, ledger records and lessons are written on main only. Rows reach main through `board/sync_board.py`
  (see docs/merging.md), which also brings over anything the live page has that main lacks; a board-only pull request
  merges without the label (Wendell, 2026-10-04). `council/faces.yaml` changes only by his ruling.
- Deferred items: run `python3 council/due.py --ahead 7` at the start of every board read.
- Run `python3 council/tools/voice_lint.py` on anything he reads. Never alter his quoted words.
