2026-10-16
# Morning menu (Tap the Vein and Lenses)

ontology: default; touches: BAR, CompostingDisposition, PermissionGrant

## Next
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
library that can be drawn from"): set-aside items go to a library he draws from later. It needs a bars-engine status
or table plus a board surface, so it is a council pass or a design thread first. (3) Taking a shadow quest: today the
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
