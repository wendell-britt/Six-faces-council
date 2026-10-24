2026-10-16
# Morning menu (Tap the Vein and Lenses)

ontology: default; touches: BAR, CompostingDisposition, PermissionGrant

## Next
2026-10-22, thread "Morning menu catch-up": key answers 200. bar_read ran on the five 10-21 sealed lines (join 3, work-today 1, defer 1), on main. Annastasia's campaign has no call sheet to be its home; the Between spark was already replanted on bars-engine (carry answered "not needed"). Steps menu-key-match-01..03 ticked. NEXT: the weekly unchosen-read routine (see Unchosen lines below) once bars-engine branch claude/project-thread-klpz41 has merged.
2026-10-20, thread "Morning lists, first real read": #314 merged. The 10-20 morning is gathered on main (no sealed
lines: the menu key still answers 401) and the faces read today's slate of 16 list items: work-today 3 (send Annastasia
the draft, #311, #308), join 2, defer 7, let-go-offered 4. Positions tb-lists-are-bars, tb-slate, tb-pick-carries-read
stand on the board (v486). Found and fixed on this thread's pull request: board/sync_board.py merged a stale live page's
morning entry by entry, which is where main's duplicated 10-14 categories came from (now the later gather wins whole,
tests/test_sync_board_morning.py), and morning.py's backlog links lost the dot in `.specify` and 404'd. NEXT: none
for this strand until the menu key works; then the Sonnet board read in the 10-19 entry below reads sealed lines too.
Checked in headless Chromium on main's build: the Morning tab shows seven categories and 16 read cards, each with a Pick button,
no page errors. Not checked: a pick saved from /board/council (it loads behind his sign-in only).

2026-10-20, thread "Morning lists into the faces' flow" (branch claude/morning-lists-flow-ark0q6, draft PR on
Six-faces-council): the orphaned Morning tab lists (waiting on you, steps, due, handoff, open PRs, bars-engine backlog)
are now BARs (tb-lists-are-bars). `python3 council/bar_read.py --slate` names up to 3 items per list each morning
(tb-slate: never-read first, then deferrals due on the seed library's 3/7/14/30/60/90 ladder, `list_reads` in
board_data.json); a face fills each read with the same rules as a sealed line (kernel, missing, gathered with sources,
now also `spec:<bars-engine path>`, factors apart, call) and `bar_read.py --reads reads.json --write` checks and files it.
A sealed line with no home can now meet a read list item (opponent kind `item`); a list item can meet a sealed line
(`line`). The Morning tab shows list reads under "The council's read" with a Pick button, and a one-line read in each
category. A pick carries the read into its thread brief (board/pull.py `read_brief`, tb-pick-carries-read).
morning.py keeps each item's last read across gathers. Tests: tests/test_list_reads.py (fixtures in
tests/fixtures/bar-read/). scout: rung 2, we have it (bar_read.py, morning.py, pull.py extended).
NEXT, fresh thread that owns the PR: (1) drive CI green and let it merge; (2) on main, gather a fresh morning
(`council/morning.py --prs <file from the GitHub tools> --bars ../bars-engine --write`; main's `morning` is from 10-14
with duplicated categories, the fresh gather replaces it), run `--slate`, have a worker write the faces' reads, run
`bar_read.py --reads reads.json --write`, land with board/sync_board.py and republish; (3) put positions tb-lists-are-bars,
tb-slate, tb-pick-carries-read on the board as standing positions; (4) confirm on /board/council that the cards show
and a pick saves. Not checked: the page in a browser (the script parses; no screenshot taken).

2026-10-19, thread "work today or defer": the ttv-bars 1 build is done on sample data. `council/bar_read.py` checks one
read per sealed line against every tb-* rule and writes it beside the line's alignment in `board_data.json` `intake`;
the Morning tab shows each read as a face-off card under the Tap the Vein box ("The council's read", work-today cards
first). bars-engine's history export now carries each task's `blockedAt` and `notes` count (johnair01/bars-engine #404);
the Six-faces-council pull request on branch claude/project-thread-a871l9 holds the script, the card and
`tests/test_bar_read.py` (sample: `tests/fixtures/bar-read/`, five lines, five checked reads). NEXT, a Sonnet board read
once the menu key works (morning-menu `menu-key-match`): fetch the menu and history, write reads.json for the real sealed
lines, run `python3 council/bar_read.py <menu> --reads reads.json --history <history> --write`, commit on main and
republish. Tests F1 (10-26, he takes at least half the calls) and F2 (10-31, council work wins at most four in five) run
from there. Not built: a tap on the card itself (the tap stays in Tap the Vein, tb-call-is-advice).

2026-10-19, thread "Tap the Vein on the board": one UI is done. bars-engine #403 (/tap-the-vein/embed) merged; Six-faces-council
#312 frames it on /board/council and merges after. Position `ttv-one-ui` is on the board. Pass ttv-bars 1
(`council/passes/6FACE_PASS_ttv-bars1_2026-10-19.md`, ledger `2026-10-19-ttv-bars1.json`) answered his second ask with six
positions and no question: `tb-sealed-is-bar` (sealing is the keeping; updates `ttv-task-not-bar`), `tb-face-unpacks`,
`tb-context-first`, `tb-face-off`, `tb-call-is-advice`, `tb-loss-not-avoidance`. NEXT, fresh Opus thread, the build on sample
data (the menu key is still 401): (1) bars-engine history export adds each task's notes count and `blockedAt`; (2)
`council/bar_read.py` checks one read per sealed line (line word for word, taskId, barId, face, kernel, home from
`intake_align.py`, missing from [next step, home, input, capacity, blocker], gathered with sources, workable, opponent from
the same strand/row/goal else `needs_work.py` else the next callsheet entry, factors signal/ready/unlocks/waiting shown
apart, call work-today/defer/join/let-go-offered, why) and writes them to `board_data.json` `intake`; (3) the Morning tab
shows each read as a face-off card under the Tap the Vein frame; (4) a test in `tests/`. Done when a pasted five-line
sample menu gives five checked reads on the board. Tests F1 (10-26, he takes at least half the calls) and F2 (10-31,
council work wins at most four in five).

2026-10-16, thread "spaced resurfacing" (branch claude/project-thread-9rf0rk in both repos; bars-engine #345,
Six-faces-council #197): board read 2031 overruled `sl-no-pressure` ("We need a mechanics to pull in tasks that are
resting and use spaced repetition to get it back into the board"). Built: a resting seed comes back 3, 7, 14, 30, 60,
then every 90 days, shown three days, at most three a day; Keep resting or passing it by climbs a rung; silence never
composts it. Tap the Vein shows "Back from the seed library" with Draw, Keep resting and Let go; the board's Morning
tab shows today's at the top, linking there. Positions `sl-resurface-ladder` and `sl-resurface-not-a-draw` are on the
board. `docs/seed-library.md` rule 1 is rewritten. Still open: SL1 on 2026-10-30 now also counts keeps and the rung
each draw came from; Keep resting from the board itself waits on SL1 (a save-schema change in both repos).

2026-10-16, thread "seed library board" (this repo's and bars-engine's branch claude/seed-library-board-4vdnzv): the
board's surface is built. The Morning tab has a closed Seed library panel that `council/morning.py` reads from
`GET /api/tap-the-vein/seed-library` (`--seeds` for a saved copy), and "Set aside" beside each sealed item with a task
id, saved as `seeds/<taskId>`, which bars-engine's save route turns into the same rest as the card's button. It works
on /board/council (bars-engine); on the claude.ai page the button links there. bars-engine #342 and Six-faces-council
#192 merged. Still open: test SL1 on 2026-10-30; the first `morning.py --write` after bars-engine deploys fills the panel.

2026-10-16, thread "seed library" (bars-engine branch claude/seed-library-g3qu9x, this repo's branch of the same name,
stacked on #191): Next item (2) below is built in bars-engine. A live task can be set aside as `resting`, drawn back into
today as the same task, or let go from the library with no reason; the council reads it through
`GET /api/tap-the-vein/seed-library`. Design and rules: `docs/seed-library.md`; positions `sl-resting-not-compost`,
`sl-no-pressure`, `sl-draw-same-task`, `sl-board-reads-library`. Still open: the board's surface (a seed library panel on the
Morning tab read by `council/morning.py` from the export, and "Set aside" beside each intake item, written to bars-engine),
a fresh Opus thread that owns bars-engine #342 and Six-faces-council #192 and stacks on #341 and #342 until they merge;
test SL1 on 2026-10-30.

2026-10-16, thread "lens emergence" (bars-engine #341, this repo's branch claude/lens-emergence-ittf5k): board read 1759
flipped two positions and added one. Done here: `lens_emerge.py` pitches paraphrase each morning and cite only its date,
refusing a gist that copies six of his words in a row (`ttv-lens-emerge`); `intake_align.py` gives every no-home-yet
item an optional shadow quest, the question that would bring out its hidden alignment (`ttv-no-home-yet`); and
`ttv-one-store` is bars-engine #341 (the council seal on /board/council writes each item as a task, the menu carries
`taskId` and `barId`). Still open, in order: (1) T1, due 10-18: the key is refused (401 on menu and lens goals,
`/api/tap-the-vein/history` still deploying at 18:00 UTC); Your steps list `menu-key-match` asks him to put one new key in
Vercel, the cloud environment and the GitHub secret. Once he ticks it, a fresh thread runs `lens_emerge.py fetch`,
pitches at most five goals with `pitch`, lands the rows with `board/sync_board.py --rows` and deletes the scratch copy.
(2) The seed library (`ttv-fruit-is-his` stands with his addition, "We should also be able to defer those into a seed
library that can be drawn from"): built in bars-engine by the "seed library" thread above; the board surface is next. (3) Taking a shadow quest: today the
board only shows the question. Making it a bars-engine shadow quest on the item's task (QLA already mints shadow quests)
is the follow-up once #341 merges.

2026-10-16, pass ttv-loop 1 (`council/passes/6FACE_PASS_ttv-loop1_2026-10-16.md`, eight `ttv-*` positions, no
questions): built on draft PRs, bars-engine `GET /api/tap-the-vein/history` and optional compost reason, council
`council/lens_emerge.py`, strand and no-home-yet alignments in `intake_align.py`, and the board box as a four-phase
stepper. Next, in order, each its own thread: (1) once the bars-engine PR deploys, the first emergence run (test T1 by
10-18: `lens_emerge.py fetch`, read, pitch, rows to the board; the token was refused from the 10-16 thread's container,
so check `COUNCIL_MENU_TOKEN` reaches it); (2) `ttv-one-store`: the board's seal writes each item to bars-engine as a
task and the menu export carries `taskId` and `barId`; (3) the Architect's `AlignmentLink` record and status split
(`ttv-axes`), after T2 (10-21) counts records per commitment. Tests T3 and T4 due 10-23.
2026-10-14, Lenses build (3) `lens-intake-align` is up: the board's Tap the Vein box takes "Everything you can do today", one per line, and `council/intake_align.py` writes the board read's one-line reason per item (goal, board row, or pitched smaller goal; docs/morning.md "Everything you can do today"). bars-engine `POST /api/lenses/goals` takes `parentId` for smaller goals. The Lenses chain is built; next is his first real intake, tested by 2026-10-21. 2026-10-14, Lenses build (2) `lens-pitch-goals` is up: bars-engine #320 (`POST /api/lenses/goals`, year goals, safe to send twice) and this repo's `council/lens_goals.py` plus the Tap the Vein box offering one empty domain's prompt (saved as `lensDomain` on the free write; docs/morning.md steps 4 and 5). #319 merged. Next is build (3) `lens-intake-align`, its own thread: the full intake, each item bridged with a written reason to a goal, a board row, or a pitched smaller goal. 2026-10-14, Lenses build (1) is up as bars-engine #319 (`GET /api/lenses/goals`) and Six-faces-council #133 (morning.py reads it, Lenses panel on the Morning tab); once both merge and bars-engine deploys, a board read runs `python3 council/morning.py --write` on main and republishes. Builds (2) and (3) are next. 2026-10-14, Lenses pass 1 (`council/passes/6FACE_PASS_lenses1_2026-10-14.md`, five positions, no questions): he has no active Lens goals (the export returned `goals: []`), so every board item is unaligned. Build in order, each its own thread: (1) bars-engine `GET /api/lenses/goals` (same council token, no sealed menu needed), `council/morning.py` reads it, and the Morning tab shows a Lenses panel per domain, empty ones as "No goals here yet" (`lens-board-reads-goals`); (2) an empty domain's prompt in the board's Tap the Vein box, goal pitches from the sealed free write like `council/ttv_bars.py`, kept ones written by `POST /api/lenses/goals` as active goals (`lens-pitch-goals`); (3) the full intake, each item bridged with a written reason to a goal, a board row, or a pitched smaller goal (`lens-intake-align`). Test by 2026-10-21. Earlier: 2026-10-14, Tap the Vein on the board (#126, #129): the board box seals a menu and saves the free write; the board read summarizes it and pitches BARs as board questions (`council/ttv_bars.py`). Two pieces Wendell named next, each its own fresh thread on Opus (new design): (a) the full Tap the Vein intake on the board, where he lists everything off the top of his mind he can do today and each item is checked for alignment against the open board items (`council/morning.py` already gathers those as categories); (b) Lenses: "The lenses integration is probably the biggest bottleneck as our current system doesn't really use lenses". The board's goals come only from bars-engine's menu export, so a session should first find what Lens data exists for him (`/api/tap-the-vein/menu` returns `goals`) and run a council pass on how the board uses it.

Three fresh threads: (1) bars-engine Lenses intake (Sonnet): save each domain as locked in (`saveYearLensFrame`, `LensesOnboardingClient.tsx:183`; `LensWorkshopDraft` exists), run one domain a morning as Tap the Vein's free-write prompt, rename/park/retire a goal from the Observatory. (2) bars-engine Tap the Vein menu (Opus): kept lines become menu items bridged to a Lens goal; only kept lines leave the session (`mm-raw`); menu exported for the council. (3) council `council/morning.py` and the board view: gather the backlog as separate categories; first find how a council session reads thread 2's export (network policy and a token).

## Waiting on
No answer owed. Ruled 18:21: `mm-where` = Tap the Vein, `mm-raw` = only kept lines leave the free write; six positions stand. Test by 2026-10-16: one real morning end to end, and a pick becomes a thread (thread 1: close after two domains, reopen, both saved).
`mm-backlog-sources`: "Keep them as separate categories people can explore so they aren't just one long list"
`mm-menu-shape`: "All items need a bridge to lens goals and game masters suggest ways to align to lens goals or suggest adding lens goals a smaller time scales to integrate (side quests merging into main quest)"

## Files
- `council/passes/6FACE_PASS_morning-menu1_2026-10-09.md`; ledger `2026-10-09-pull-181703.json`; `council/morning.py` (to build)

## Archive
HANDOFF.md: "Open on 2026-10-09, morning menu (Tap the Vein and Lenses)"

## Unchosen lines, 2026-10-21 (pass unchosen1)

Wendell asked for something to do with the ideas the intake does not take, to see patterns in what is not chosen.
Pass `council/passes/6FACE_PASS_unchosen1_2026-10-21.md` mapped six drop points and set seven `uc-*` positions and one
question, `uc-who-reads` (may the council read the unchosen lines; recommended weekly, in place, no copy kept).
First build: bars-engine #414, a read-only "Not chosen" section in Tap the Vein (`?view=unchosen`), no schema change.

Next, in order: (1) when #414 merges, his look at /tap-the-vein?view=unchosen; (2) "Draw into today" on a raw or
unpicked line; (3) a store for the council's misses (declined menu suggestions, unpicked face-off cards,
`uc-council-misses`); (4) if he answers `uc-who-reads` B or C, a weekly read in `council/bar_read.py`'s style. Test UC1 on 2026-11-04.

**Weekly read built, 2026-10-21.** He answered `uc-who-reads` B (pull 17:16 UTC). bars-engine branch
`claude/project-thread-klpz41`: table `ttv_unchosen_pitches`, GET/POST `/api/tap-the-vein/unchosen`, pitches in the Not
chosen view (preview `?view=unchosen&sample=1`). Council: `council/unchosen_read.py`, `docs/unchosen-read.md`. Per his
steer on `uc-pattern-returns`, a returning word gets a new pitch and the old one is composted beside it. Blocked on
`COUNCIL_MENU_TOKEN` (401 on 10-21). TRIGGER: the token answers 200 and the bars-engine pull request has merged ->
create a weekly routine (Mondays, one Sonnet thread per docs/unchosen-read.md, no chat line beyond the count), and run
the first read. His look at the sample preview may steer the pitch card.

## Tap the Vein day rolls at 4am (note, 2026-10-24)

His note on the Tap the Vein blocker (blockers/tap-the-vein--mvm206os): "Make a note to have the tap the vein timer not reset at midnight." Position `ttv-day-rolls-late` stands: the day rolls at 4am local. Not built: `ttvToday` in board/template.html (a local `toLocaleDateString('en-CA')`) and the `date` bars-engine's `/api/tap-the-vein/status` and the seal use must both take a "day" that is the local date minus 4 hours, and the skip run (`ttvSkipRun`) follows from it. Do it as one pair of pull requests with a test in each repo; a Sonnet thread can take it.

## Board look examples (2026-10-24)

A question's `examples` list ({title, src, href, note}; src is https or data:image) shows as pictures and links on its row; `build_board.py` warns on a bad one. `lt-mirror-look-03` was answered "None yet" for lack of pictures, so it is asked again as `lt-mirror-look-03b` with the five mirror stills and both links. TRIGGER: his pick on `lt-mirror-look-03b` (callsheet relationship-creature.md, line "Next. TRIGGER" now reads 03b). Rule for any look question from now on: put the thing to judge in `examples`.
