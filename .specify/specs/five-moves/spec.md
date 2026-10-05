# Spec: The daily session takes up work on its own, by the five moves

## The ask

> "It should be able to check in it's own and eventually find work to do that pushes the needle even if I'm
> unavailable"
>
> Wendell, board steer on `sd-when`, 2026-10-03.

> "We can always do research as "something new" [...] Wake up to new opportunities or work / Open up- find out
> what's been abandoned in the larger work corpus / Clean up remove tech debt literally organizing things / Grow
> up- increase out throughout or quality capacity- operating from higher levels / Show up- ship finished work"
>
> Wendell, board steer on `sd-autonomy-pass`, 2026-10-03.

**Who it is for:** Wendell, on the days he does not open a session.

**What he feels now, and what should change:** Work moves only when he is present. The daily session already
runs for deferrals. It should also move one piece of work forward each day, inside limits he has ruled on.

## Purpose

After the re-weigh, each daily run takes up one of Wendell's five moves, finishes one change under it, puts one
row on the board, and stops.

## Design decisions

| Decision | Choice | Whose |
|---|---|---|
| The moves | Wake up, Open up, Clean up, Grow up, Show up, as he defined each | Wendell, the steer on `sd-autonomy-pass` |
| Which move | One per run, in his order, as a daily rotation | Council, position `fm-rotation` |
| Nothing found | The run does research instead | Wendell: "We can always do research as "something new"" |
| What a move may do | Wake up writes a research note with quoted sources. Open up lists abandoned work it found. Clean up and Grow up change code or files on a strand branch, with a pull request. Show up brings finished work to mergeable and names it on the board | Council, position `fm-limits`, from his definitions |
| Never | Merge into main, act on the reserved list, change another session's rows or branches, retire or delete anything, or work on a project with a deferral waiting | Council, position `fm-limits`, from the pipeline's ship stage, `reserved` in faces.yaml and the council lesson of 2026-10-03 |
| Board rows | By level: level one is one row per run, and he rules each level change on the record of rows that stood and tokens used | Wendell, overrule of `fm-one-row`: "This is essentially a level progression. More skillful agents get more capacity and resource"; the numbers in position `fm-levels` are the council's |
| Repos | The council's home repo only, for now | Wendell, `fm-repos`, board read 25 |
| When the build starts | After six-faces-council #16 merges | Council, position `fm-after-16`, from the Challenger's dissent |

## Contracts

Each run writes `council/ledger/<date>-daily.json`: the move, what it found, what it finished, the branch and
pull request if any, and the board row it added. The board row is a position or a finding in the existing
shapes. Nothing new is added to the board's store.

## Reserved items

The reserved list in `council/faces.yaml` is outside every move. Work in bars-engine is a question for Wendell
because another person owns that repo.

## How we will know it failed

- **The cheap test, run before the pass:** check whether each move has real work waiting today. **It passed.**
  Every move has some (pass nine, evidence E1).
- **The result that stops the work:** after two weeks of runs, more of the session's rows flipped or ignored
  than stood would mean the session is not finding work that pushes the needle.

## Definition of done

- [x] Wendell rules on `fm-rotation`, `fm-limits`, `fm-one-row`, `fm-after-16` and `fm-repos` (board read 25).
- [x] Wendell rules on `fm-levels` (stands, board read 26).
- [x] #16 merges (4de3aa8).
- [x] The daily routine's instructions gain the move step, and `plan.md` and `tasks.md` are written (board read 27, 0fa2fea).
- [ ] The first run of each move is read and recorded here.
