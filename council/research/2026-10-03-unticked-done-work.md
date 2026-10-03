# Unticked boxes on work that has shipped

Daily run, 2026-10-03, move Wake up. His words: "Wake up to new opportunities or work".

## What I looked at

Every unticked box (`- [ ]`) in `.specify/specs/`, every `open` field in this week's ledger records, the open
pull requests and the open issues of wendell-britt/six-faces-council. There are no open issues. The two open
pull requests (#18 and #20) belong to other sessions, so this run left them alone.

## What I found

There are twelve unticked boxes. Nine of them describe work the record shows as done. Three are still open.

### Nine boxes the record shows as done

| Spec file | Box | What the record says |
|---|---|---|
| `five-moves/spec.md:60` | "Wendell rules on `fm-levels`." | `board_data.json`, resolved `fm-levels`: `"decision": "stands"`, record `council/ledger/2026-10-03-board-read-26.json` |
| `five-moves/spec.md:61` | "#16 merges." | Commit 4de3aa8: "Merge pull request #16 from wendell-britt/claude/project-thread-gposog" |
| `five-moves/spec.md:62` | "The daily routine's instructions gain the move step, and `plan.md` and `tasks.md` are written." | Commit 0fa2fea: "Board read 27: #19 merged by Wendell; the daily routine gains the move step". Both `plan.md` and `tasks.md` are in the spec folder. |
| `five-moves/tasks.md:17` | "Fire the routine once and read what it did." | `council/ledger/2026-10-03-first-daily-run-blocked.json`: `"fired_by": "hand, to check the loop"`, with what it made and what blocked it |
| `spaced-deferral/tasks.md:21` | "Board position `sd-ship`: merges on the next board read unless flipped." | Resolved `sd-ship`: `"decision": "stands"`, record `board-read-22.json`. The spec's own box says: "Ships as board position `sd-ship`. It stood at board read 21, and the PR merged." |
| `spaced-deferral/tasks.md:22` | "After merge, on main: the oracle drafts' resolved entry gains `history` and `project`." | Resolved `fcm-oracle-drafts` carries `"project": "friendcraft-manuacript"` and a `history` list with one deferral, saved at 2026-10-03T18:08:52Z |
| `spaced-deferral/tasks.md:23` | "Ledger record written; this file ticked." | The ledger half is done (`2026-10-03-board-read-22.json` records `sd-ship`). The ticking half is this finding. |
| `daemon-subagents/spec.md:152` | "Ships as a board position that merges on the next board read unless he flips it." | Resolved `daemons-ship`: `"decision": "stands"`, record `board-read-10.json`. Commit d473fa5: "Daemon subagents (merged on Wendell's board read 10: daemons-ship stands)" |
| `iching-casting/spec.md:68` | "Ships as a board position that merges on the next board read unless Wendell flips it." | Resolved `iching-ship`: `"decision": "stands"`, record `board-read-11.json`. Commit 1b10b0f: "I Ching casting by the three-coin method (merged on Wendell's board read 11: iching-ship stands)" |

`daemon-subagents/spec.md:51-54` holds four more unticked boxes, but they belong to the first definition of done,
which "failed on 2026-10-02". Version two, below it, ticks the same four. Those boxes are history, so this note
does not count them.

### Three boxes that are still open

- `spaced-deferral/spec.md:134`: "The first real re-weigh, the oracle drafts on 2026-11-03, is recorded here."
  It is due on 2026-11-03. `due.py --all` lists it as waiting, deferred once, and today's run had nothing due.
- `five-moves/spec.md:63`: "The first run of each move is read and recorded here." Today's run is the first
  Wake up that finished. The other four moves have not run yet.
- `five-moves/tasks.md:21`: "Ledger record written; this file ticked." It waits on the box above it.

### One open ledger item that has already been taken up

`council/ledger/2026-10-03-board-read-22.json` keeps an `open` note: "Finding work that pushes the needle while
he is unavailable is a larger feature than the weekly re-weigh." Pass nine, the five moves, took that up, and
the daily routine now runs it. The note was never closed.

## Why it matters

A session that reads `tasks.md` to find work will see nine jobs that are already done. The five-moves spec
counts "Open up" as finding "what's been abandoned in the larger work corpus", and stale boxes make finished
work look abandoned. That is the failure the record is meant to prevent.

## What would finish it

Tick the nine boxes, each with the record it rests on, and add one line to the board-read-22 ledger record saying
pass nine took up its open note. That is Clean up work, the move he named for tech debt, so the council
proposes it for the next Clean up run, not done today. It changes no code and needs nothing from Wendell.

## Leads not followed

Every source was in the repo, so this run needed no outside site.
