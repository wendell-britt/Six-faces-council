# A morning menu: Tap the Vein and the Lenses intake in the council's day

**Run 2026-10-09**, from Wendell's message in the project chat at 17:58 UTC. This is the first pass on the subject.

**The ask, in his words.** "I also want to start integrating the tap-the-vein and Lenses work from bars-engine into
our flow. If I'm able to start the day with a free write and with the context of our operations backlog and what
emerges for me during the free write I can create a menu of things to add to the council board each day that are
aligned with my goal. This would require the Lenses Intake to be more robust and usable for me."

**Anchor:** each morning he writes, sees his goals and the open work side by side, and picks the day's items. The
picks reach the board without a chat question, and every pick names the goal it serves.

**Inputs:** bars-engine at `64627db` (the Tap the Vein and Lenses code below, specs `tap-the-vein-tier-2`,
`lens-integration-refactor`, `quest-lineage-alignment`); this repo's `council/HANDOFF.md`, `council/daily.yaml`,
`docs/pickup.md` and the board. No daemons were sent: the problems were reading code and the record.
`council/due.py --ahead 7` lists nothing due.

## What exists in bars-engine

**Tap the Vein** (`/tap-the-vein`, `src/actions/tap-the-vein.ts`) is a daily ritual in six steps: open, free write,
brainstorm, commit, work, seal (`TapTheVeinRunner.tsx:46`). The free write is saved whole with its word count
(`TapTheVeinDailySession.rawEntry`). The brainstorm turns it into a list of lines he marks raw, play or composted,
and the list is kept (`brainstormCandidates`). Commit turns a line into a task, and a task attaches to a week goal
from the Lenses (`lensGoalId`, with a lineage snapshot). Work tracks charge, blockers and notes per task. Carrying a
task to tomorrow is always his explicit move. No model runs anywhere in it.

**The Lenses intake** (`/lenses/onboarding`) builds a year frame over five domains: relationships, career, money,
health and allyship (`src/lib/lenses/domains.ts`). Each domain is a ten-minute timed free write; each line becomes an
option (at most ten), and he keeps up to five as year goals. The descent (`/lenses/descent`) then breaks a year goal
into quarter, month and week goals. Goals are `LensGoal` rows with a parent chain, so a week task can be traced up to
its year goal. The Observatory (`/observatory`) shows the lens levels.

## The gaps, for his use

1. **Nothing crosses between the two systems.** Tap the Vein lives in the bars-engine database; the council lives in
   this repo and the board. No morning output reaches the board, and the council's open work never reaches the free
   write.
2. **The intake saves only at the end.** The client holds all five domains in memory and calls `saveYearLensFrame`
   once (`LensesOnboardingClient.tsx:183`). A closed tab partway through loses the work, and the page asks for about
   an hour in one sitting (`src/app/lenses/page.tsx`).
3. **A goal cannot be edited on its own.** Goals change only by re-running the intake or the descent, which upsert
   the whole set (`src/actions/lens-goals.ts`).
4. **There is no menu.** Tap the Vein's commit step makes tasks for the day; nothing gathers his kept lines and the
   open work into one list he picks from.
5. **The operations backlog has no single reader.** The council's open work is spread over `council/HANDOFF.md`, the
   board rows that wait on him, `council/due.py`, open pull requests in three repos, and bars-engine's
   `.specify/backlog/BACKLOG.md`.
6. **The record does not show whether his year frame is filled in.** The first build reads his Lenses goals and says
   so.

## The casts

| Face | Hexagram | Shows |
|---|---|---|
| Shaman | 51 Shock, changing to 22 Adornment | It went off, and it will go off again. |
| Architect | 10 Footing, changing to 1 Unbroken | You are stepping onto ground that matters, and the play is what makes it safe. |
| Challenger | 24 Turning, changing to 2 Bearing | What came back is one line deep. |
| Regent | 63 Arrived | This is finished, which is when it starts moving. |
| Diplomat | 36 Nightfall | You are keeping a light covered, and it is still lit. |
| Sage | 41 Spending | This has a price and you have yet to name it. |

## Shaman

**Shock, changing to Adornment:** "It went off, and it will go off again." The free write goes off every morning,
and what it raises is the day's real material. **What the Player wants is to write first and be handed nothing
until the writing is done,** so the backlog appears after the free write, never beside the blank page. The intake's
hour is the wrong size for a morning; one domain a morning, as that morning's prompt, fits the ritual he already
keeps (`mm-intake-one-a-morning`).

## Architect

**Footing, changing to Unbroken:** "You are stepping onto ground that matters, and the play is what makes it safe."
The ground is already laid: kept lines, week goals and the lineage chain all exist. **Build only the two missing
pieces:** a reader that gathers the operations backlog into one list (`council/morning.py`, `mm-backlog-sources`),
and the bridge that brings his kept lines and goals to the board. Where the bridge sits is his preference
(`mm-where`). The intake saves each domain as it is locked in (`mm-intake-saves-each-lens`), and a single goal can be
edited from the Observatory (`mm-goal-edit`).

## Challenger

**Turning, changing to Bearing:** "What came back is one line deep." A menu of thirty items is the backlog again
under a new name. **Cap it at seven, and make every item name its goal;** an item that serves no goal stays on the
menu marked unaligned, last, because hiding it is how drift goes unseen (`quest-lineage-alignment`'s shadow quest,
`mm-menu-shape`). The test is whether he picks from it on a real morning in under ten minutes.

## Regent

**Arrived:** "This is finished, which is when it starts moving." A pick is already his ruling. **Each pick becomes
one board row marked as his, and the next board read starts one thread per pick** (`mm-picks-become-threads`). No
pick turns into a chat question, and the daily session stays stopped (`daily-stopped`); the morning replaces its
wake move with his own choice.

## Diplomat

**Nightfall:** "You are keeping a light covered, and it is still lit." The free write is the covered light. **Who
reads the raw free write is his consent to give,** and consent is on the reserved list in `faces.yaml`. The
community's allergy to AI (bars-engine `CLAUDE.md`) points to a ritual that runs with no model in it, where only the
lines he keeps leave the page. That choice goes to him (`mm-raw`).

## Sage

**Spending:** "This has a price and you have yet to name it." The price is a bridge between two systems. The record
answers the menu's shape, its sources, what a pick becomes, and the intake's two fixes. **Two questions are his:**
where he writes in the morning, which decides what gets built (`mm-where`), and who may read the free write, which
is consent (`mm-raw`). **Dissent:** the Shaman would hide the backlog until the free write ends; the Architect would
show his goals from the start so the writing can aim at them. The menu shows goals after the writing, as the Shaman
asks, and the dissent is recorded. The pass was otherwise unanimous, which is a flag: no face tried the ritual on a
real morning.

## Outputs

### Positions (stand unless he flips them)

- `mm-backlog-sources`: the operations backlog the menu reads is HANDOFF.md's open items, the board rows that wait on
  him, `due.py`, open pull requests in the three repos, and bars-engine BACKLOG rows marked Ready, gathered by one
  script, `council/morning.py`.
- `mm-menu-shape`: at most seven items, his kept lines first and backlog items after; each names the Lens goal it
  serves, and an item with no goal is marked unaligned and shown last.
- `mm-picks-become-threads`: each pick becomes one board row marked as his pick, and the next board read starts one
  thread per pick.
- `mm-intake-saves-each-lens`: the intake saves each domain as he locks it in, so a closed tab loses nothing.
- `mm-intake-one-a-morning`: the intake can run one domain per morning as that morning's free-write prompt.
- `mm-goal-edit`: a single goal can be renamed, parked or retired from the Observatory.

### Questions (passed the reach test)

- `mm-where` (Shaman, Architect): where he writes each morning. His preference; it decides whether the bridge is
  built in bars-engine or on the board. Not asked before: this is the first pass on the subject.
- `mm-raw` (Diplomat, Shaman): who may read the raw free write. Consent, which is reserved. Not asked before for
  the same reason.

### Tests, dated

- By 2026-10-16: one real morning runs end to end, and at least one pick becomes a thread.
- By 2026-10-16: closing the intake after two domains and reopening it shows both domains saved.
