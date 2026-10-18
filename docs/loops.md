# Rounds that start themselves

Wendell, 2026-10-14, on the loop engineering thread: "I do a lot of prompting for the next move instead of that next
move being already acted upon", then "Yes I agree with this. What would we need to do to implement". He stays the
grader, but his look stops being what starts the next round. Piloted on the spirit look art loop.

## The four pieces

1. **A next-round contract per strand**: `council/loops/<strand>.json`, beside the callsheet. Each round says what it
   builds, how it is checked, its gate and its budget. An optional `ontology_profile` names the one manifest profile
   the round loads (docs/ontology-in-flows.md); without it the round loads none. Gates: `auto`, or `eyes`, `money`, `accounts` (needs him).
   Statuses: `done`, `running`, `next`, `queued`, `held`.
2. **Continuation**: when a round ends, its thread runs `python3 council/loops/next_round.py finish <strand> <n>`
   and pushes the change. If the tool then says a round may start, the thread names that round in its last reply
   and in its send_message handoff, and the coordinator starts it at once (the handoff rule in CLAUDE.md). The
   new thread runs `next_round.py start <strand> <n>` first.
   A contract's `every_round` list names what every round delivers whatever it builds (the spirit loop: the models in
   the page's 3D viewer, since round 13 shipped without them and that is where Wendell reviews). `start` prints the
   list, and `finish` refuses without `--delivered`.
3. **His look is a veto with a leash**: a round starts itself only when it is at most `max_ahead` (2) rounds past
   his last look. His look is recorded with `next_round.py look <strand> <n> --verdict keep-going|redirect|stop
   --words "<his words>"`. A redirect rewrites the next round's `builds` before it starts (or the running round
   folds it in); `stop` holds every queued round.
4. **Labels**: every look appends one line to `council/loops/labels/<strand>.jsonl`: the render, his verdict, his
   words unaltered. These are the examples a model grader can later learn his calls from.

`python3 council/loops/next_round.py` with no arguments says, per strand, what may start now and why not.

## Positions on the board

`loop-ahead-two` (two rounds ahead of his last look) and `loop-auto-gate` (auto only where no money or accounts
are involved, and never a `council/faces.yaml` change) stand unless he flips them.

## When a round needs art that does not exist

Wendell, 2026-10-14, steer on `loop-ahead-two` (board read 18:46, ledger `2026-10-14-pull-184616.json`): "If art is
needed and there isn’t any art available we should generate a prompt OR a design intake to get clear on what asset
should be made". A round that needs reference art (a concept, a face, a material) and finds none does not stall or
wait for him. It writes an image prompt, or a short design intake when the asset itself is unclear, to
`council/loops/prompts/<strand>-r<n>.md`, builds the round from the prompt's own description, and names the prompt in
the callsheet so the art can be made and dropped in the cave studio inbox for a later round. The round's `check` stays the
same.

