# The daily compost pass

Wendell, 2026-10-12: "ok can we do a daily pass through the open items for me and see if they are still needed for
our various goals? This is an important composting step and a big opportunitty for the game masters. As context
increased and changes we should be able to take things from my board and act on them if it's the more deft and
aligned path"

The find that started it: that evening the Guide sync list was retired because nothing depended on it. Other steps go
stale the same way, and nobody looks at them until he trips over one.

## When it runs

A routine fires each morning at 6:47 Pacific into the project's coordinator, which starts one thread for the pass on
Sonnet. The pass is one session and ends when its reply is posted (short sessions, CLAUDE.md).

## The pass

1. Save the store: one message with ArtifactData `list` calls on `steps`, `lists`, `questions`, `positions`, `terms`,
   `causes` and `steer` of https://claude.ai/artifact/DxyShVS8tmvJym4HAsgnho, all into one `out_dir`, limit 1000.
2. `python3 board/read.py <dir>` first, so any saved answer is recorded before steps are judged.
3. `python3 council/compost.py <dir>` prints every open step with its list's why and source.
4. For each open step, decide one of three, checking the record (callsheets, PRs, mail, Vercel) rather than
   guessing:
   - **Keep.** It still serves a live goal and only he can do it. If it lacks full context or a place to find each
     item, rewrite it so it has them (Wendell's rule of 2026-10-12). If a piece is missing, it becomes a find-it
     step: what to find, why it matters, and what the game masters do if it is not found.
   - **Drop (compost).** Nothing depends on it any more, it duplicates another step, or a later change made it moot.
     Set `retired` to one sentence that says "Dropped on <date> by the daily pass" and why, keeping any link he
     might still want.
   - **Take over.** Claude can do it, or check it, with the tools a session has. Do it in this thread when the work
     is small; otherwise start the work (a thread, a PR) and rewrite the step so what is left for him is only what
     needs his accounts, money or eyes. Rewrite or tick the step to match.
5. Apply every change in one ArtifactData `batch` on `steps`, pinned with each step's version. Steps render live, so
   no republish is needed for step changes.
6. Moving a due date is his; the pass never moves one. A step that is late is evidence for the decision, not a
   reason on its own to drop it.
7. One reply in the thread: what was dropped, taken over and rewritten, with counts and a line each. No question.
   A question that comes up goes through the reach test and onto the board. Then resolve the thread.

## Standing checks the pass carries

- `coaching-pipeline-03`: ask Vercel's analytics API (Vercel connector, `count_pageviews`, project bars-engine,
  team slug wendells-projects-9c1b16dc, since and until both set) whether visits are counted. Tick the step when they
  are. If it still answers "not found" on 2026-10-14, turn it into a find-it step.
- `paypal-funding-01`: search his mail for PayPal or Libsyn failed-payment notices newer than the last pass, and
  tick the step once Libsyn shows paid.
- `morning-menu-key-03`: once bars-engine PR 283 is merged and deployed, drop the Terminal line from the step.

## First pass, 2026-10-12

Dropped: `hd-1` and `hd-2` (the phone-to-Mac bridge; project threads reach his Mac directly now),
`replies-owed-20261008-2` (the same failed Libsyn payment as `paypal-funding-01`), `replies-owed-20261009-1` (its
own text said nobody was waiting on him). Taken over: the analytics check in `coaching-pipeline-03`. Rewritten with
current evidence: `paypal-funding-01` (still failing on 11 October) and `morning-menu-key-03` (why the Copy id
button was missing: PR 283 is not live). Kept as they were: 35 steps; 38 steps across 11 lists stay open. The Open tab had no rows.
