# Plan: Deferred items come back on a spaced schedule, with new context

## Approach

The board already returns a deferred item when its date passes (six-faces-council #10 and #11). This
feature makes the return date grow each time the same item is deferred, and it has the council
re-weigh an item before it returns. The rule for the dates lives in two places, the board's script and
`council/due.py`, with a comment in each naming the other. The board computes the date it shows him, and
`due.py record` computes the same date when a session records it. The re-weigh is a short pass on one item,
written onto its row as `review`, so the board needs no new collection in its store.

The council weighed a scheduled session against the next board read for running the re-weigh. That choice
spends his account's usage, so it is question `sd-when` on the board rather than a decision here.

## Files touched

| File | Change |
|---|---|
| `council/due.py` | New. Lists due items with a context brief, shows the next spaced wait, records a deferral |
| `board/template.html` | The spaced option first in the Defer list; a "Since you deferred this" box on returned rows |
| `council/pipeline.yaml` | The `defer` block gains the spaced schedule and the re-weigh |
| `.claude/skills/six-faces/SKILL.md`, `council/portable/six-faces/SKILL.md` | A board read runs `due.py` first and re-weighs what is due |
| `council/passes/6FACE_PASS8_2026-10-03.md` | The pass |

## Order

1. The cheap test (spec, "How we will know it failed"). Done, passed, and it found the same-day fault.
2. `due.py`, then the board, then the rules.
3. After merge, on main: add `history` and `project` to the oracle drafts' resolved entry.

## What Wendell does, and when

He does nothing beyond the board. He answers question `sd-when`, and he can flip `sd-intervals` or `sd-ship`.
