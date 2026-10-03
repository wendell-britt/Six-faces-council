# Plan: The daily session takes up work on its own, by the five moves

## Approach

The daily routine already re-weighs deferred items. A second step follows it: `council/daily.py` prints the
level, today's move and the limits from `council/daily.yaml`, the run does the move, and `daily.py record`
writes what it did. The move rotates in Wendell's order by the number of runs recorded. Token use is read
afterwards from the session record by a session that holds the claude-code-remote tools, because a run may
not hold them itself.

## Files touched

| File | Change |
|---|---|
| `council/daily.yaml` | New. The moves in his words, the repos, the level and its history, the limits |
| `council/daily.py` | New. The plan, `record` and `usage` |
| `council/pipeline.yaml` | A `five_moves` block |
| `.claude/skills/six-faces/SKILL.md` | The board-read step for daily runs |
| The daily routine's instructions | A move step after the re-weigh, changed after the merge |

## Order

1. `daily.py` and its settings, tested on scratch data: the rotation, a level-up proposal after five rows
   stood, an overrule proposal, and a refusal of more rows than the level allows.
2. The rules and the skill.
3. After this merges, the routine's instructions gain the move step, and one run is fired to check it end to
   end.

## What Wendell does, and when

He lets position `fm-build` stand or flips it on the board. At the board read where it stands, the session adds
the `automerge` label, which `docs/merging.md` allows only when he says to merge.
