# The morning menu

Wendell, 2026-10-09: "If I'm able to start the day with a free write and with the context of our operations backlog and
what emerges for me during the free write I can create a menu of things to add to the council board each day that are
aligned with my goal." The pass is `council/passes/6FACE_PASS_morning-menu1_2026-10-09.md`; the rulings are in
`council/ledger/2026-10-09-pull-181703.json`.

## A morning, end to end

1. He writes in Tap the Vein (`mm-where`) and seals the session. Only the lines he keeps leave it (`mm-raw`); the
   free write itself never does. bars-engine bridges each kept line to a Lens goal or suggests one.
2. The menu reaches the council (see "Reading the export" below), and a council session runs `council/morning.py
   --menu <file> --write` on main. The script gathers each source as its own category and bridges every item to a goal. Then the session
   commits, pushes and republishes the board.
3. He opens the board's Morning tab. Each category opens on its own (`mm-backlog-sources`). He picks up to seven items
   (`mm-menu-shape`), and can change any item's goal, or turn it into a new goal at a smaller time scale under one of
   his goals: the side quest that merges into the main quest. Then Send to Claude.
4. The board read records each pick through `board/pull.py` (store collection `picks`) as one row marked as his, and
   lists it under "needs work". The read starts one thread per pick (`mm-picks-become-threads`).

## Tap the Vein on the board

Wendell, 2026-10-14: "is there an ability to do a tap the vein on that board ? so that I can do the tap the vein
directly from the environemnt where I'll be using that information. The goal for tap the vein is to also pull bars like
we are doing from our podcasting episodes and creating robust context web that our projects and tasks can pull frmo".

The Morning tab's "Tap the Vein here" box runs the ritual on the board itself:

1. He writes. Until he seals, the free write is kept only in his browser (localStorage).
2. "Find my lines" splits the write into lines, and he marks the ones **To do**.
3. "Seal the menu" saves `morning/menu` exactly as a pasted menu is saved, with the To do lines as unaligned kept
   lines, and saves the free write at `morning/freewrite`. His To do lines appear in the "From your free write"
   category at once, where he picks a Lens goal for each and picks up to seven, then Send to Claude.
4. The board read runs `board/pull.py`, which lists `morning/menu` under needs work as before, and
   `morning/freewrite` while it exists. The read reads the free write once, writes two or three sentences summing it
   up, and pitches the lines worth keeping as BARs, each with the slot from game-masters-guide `corpus/products.yaml`
   it would go to. `python3 council/ttv_bars.py pitch <dir>/morning/freewrite.json --pitches <file> --summary "..."`
   turns them into board questions (keep in that slot, keep unplaced, or not a BAR) and refuses any line that is not
   in the free write word for word. When the free write carries `lensDomain` (the box offered an empty Lens domain's
   prompt, `lens-pitch-goals`), the read also pitches one to three year goals for that domain, each quoting a line of
   his: `python3 council/lens_goals.py pitch <dir>/morning/freewrite.json --pitches <file>`, with
   `[{"title", "line", "why"}]`. The read adds the rows with `board/sync_board.py --rows`, republishes, then
   deletes the doc (ArtifactData delete, collection `morning`, doc `freewrite`) and its local copy.
5. He answers the pitches on the Open tab and sends. The read that records them runs `python3 council/ttv_bars.py
   accepted --write`, which writes one BAR per kept pitch into wendell-britt/game-masters-guide `corpus/bars/` (tag
   `tap-the-vein`), and opens a pull request there. It also runs `python3 council/lens_goals.py kept --send`, which
   posts each kept goal to bars-engine's `POST /api/lenses/goals` as an active year goal (safe to run twice), then
   `python3 council/morning.py --write` so the Lenses panel shows it.

Wendell, 2026-10-14, after the first version sliced the page sentence by sentence: "I think the tap the being should
be read and summarized before bars are chosen. It a bit too raw for me to know what should be a bar and currently it
seems to just slice the page sentence by sentence. This is something where I'd want to use AI to summarize and make
pitches for where things should go."

Wendell ruled `ttv-raw-bars` on 2026-10-14: read it once for BARs, then delete it. His steer: "For now read it and
delete but this is the power of having a private server like in bars engine". This widens `mm-raw` for the board
box. A sealed free write sits in the board's store until the next board read deletes it. A private server for the
free write, as bars-engine has, is a later step.

bars-engine's Tap the Vein stays the home of tasks, charge and Lens goals; the board box is the front door he uses
where he picks his work (`ttv-board-home`).

## Tap the Vein first

Wendell, 2026-10-14: "So let's have it be that the first thing that happens in the morning when I open the board is tap
the vein. It checks to see if one's been done on bars-engine and if not forces one to be done in the board and then
ingests it into the board after completion. There should be a button that gives an option to skip but if it's skipped
for 2+ days it triggers a Wave or 321 session on the blocker that's stopping me from using it".

- Until today is handled, the board opens on the Morning tab with the Tap the Vein box open, and the other tabs are
  held. Today is handled when the last gather fetched today's sealed menu from bars-engine (`morning.sealed`, written
  by `council/morning.py`), a menu sealed or pasted on the board carries today's date, or the store's `ttv/<date>` says
  `done` (written at seal), `bars-engine` or `skipped`. The date is the browser's local date.
- The board asks bars-engine itself (Wendell overruled `ttv-bars-engine-trusted` on 2026-10-14: "I do think we need to
  be able to make an API call to bars-engine directly if this is the case"). While held, it calls bars-engine's
  `GET /api/tap-the-vein/status?date=<today>` through the viewer's Vercel connector (`web_fetch_vercel_url`). The route
  takes no token and answers only `{date, sealed, sealedAt}`; the menu stays behind the token. Sealed there saves
  `ttv/<date>` as `bars-engine` with `checked: true`, the board opens, `board/pull.py` lists it under needs work, and
  the read fetches that menu with `council/morning.py --fetch <date> --write`. Not sealed, or no answer, keeps the board
  held with "Check bars-engine again".
- Sealing on the board is ingested the way it already was: `morning/menu` and `morning/freewrite`, read by the next
  board read.
- "Skip today" saves `ttv/<date>` as `skipped`. When that makes two or more skips in a row (a done day breaks the run;
  a day the board was not opened does not), the board offers the WAVE room (`ttv-skip-wave`, his steer: "It should
  deposit me inside the WAVE room and we should move to have the WAVE room be able to metabolize context specific
  charges and send the results to the board"). "Go into the WAVE room" opens
  `https://bars-engine.vercel.app/ontology-game/cave/#wave=board&charge=<words>&skips=<n>&ref=tap-the-vein--<time>&date=<day>`
  in a new tab; "Work it here on the board instead" opens the board's blocker panel (`docs/blocker-panel.md`). The
  choice is saved on `ttv/<date>` as `wave` (`room`, `board` or `not-now`) with `waveRef`.
- The room side is the WAVE room thread's work: reading that hash to open the room with the charge, and sending the
  run back as a `blockers/<ref>` record with `engine: "wave-room"` (the contract in `docs/blocker-panel.md`, "Plugging
  in the WAVE room"). Until it does, the link opens the cave's front page.

## Everything you can do today

`lens-intake-align` (Lenses pass 1, 2026-10-14): "The full intake lists what you can do today; the board read gives
each item one line: the goal it serves, the board row it advances, or a pitched smaller goal. The reason is written,
not word overlap."

1. In the Tap the Vein box he lists everything he can do today, one per line, above the free write. The free write is
   optional now. Sealing saves the list with any To do lines as one menu at `morning/menu` (list items carry
   `source: can_do`); the free write is saved only when there is one.
2. The board read that finds `morning/menu` under needs work reads each item against his Lens goals
   (`morning.goals`), the open board rows and the free write, and writes one sentence on where it goes. It saves them
   as `[{"line", "why", and one of "goal": <goal id>, "row": <board row id>, "pitch": {"title", "parentId"} or
   {"title", "domain"}}]` and runs `python3 council/intake_align.py <dir>/morning/menu.json --aligns <file> --write`.
   The script refuses an item left out, reworded or aligned twice, a goal or row that does not exist, and a reason
   under four words. A pitch with a parent is one cadence smaller under that goal; without goals, it is a year goal in
   a domain. Each pitch becomes a question on the Open tab.
3. Then `python3 council/morning.py --write`, commit on main and republish. Each item on the Morning tab shows its
   written line, and he can still change its goal before he picks.
4. The read that records his answers runs `python3 council/lens_goals.py kept --send`, which sends kept intake
   pitches with their parent, so bars-engine files a smaller goal under it (bars-engine `POST /api/lenses/goals`,
   `parentId`).

## The loop, seed to fruit (pass ttv-loop 1)

Wendell, 2026-10-16: "once a taget's generted fromks tap the vein how does it get ingested? How does the council act on
the actions that I Want to do? How does the process help us grow up teh tasks (Which are essentially barSeeds) into
fruit." The pass is `council/passes/6FACE_PASS_ttv-loop1_2026-10-16.md`.

- **Ingested.** A commitment is a bars-engine task (`mm-where`). The board's intake gives each item one written line
  (`council/intake_align.py`): a Lens goal, a board row, a call sheet strand (`"strand": "<sheet>"`, work already
  happening, carrying the strand's `lens: <goal id>` line once he has kept one), a pitched smaller goal, or `"none": true`,
  no home yet. An item with no home has an alignment nobody can see yet, so it carries `"shadow"`, the question of an
  optional shadow quest that would bring it out (`ttv-no-home-yet`, overruled 2026-10-16). On the board served by
  bars-engine (/board/council), the seal writes each item to bars-engine as a task and the saved menu carries its
  `taskId`, so one id runs from the morning to its thread (`ttv-one-store`, bars-engine #341).
- **Acted on.** He picks; each pick becomes a board row and a thread (`mm-picks-become-threads`). An item that joins a
  strand goes to that strand's thread or call sheet as a next step rather than a new thread.
- **Grown.** A task becomes a BAR only when he keeps it as one (`ttv-task-not-bar`). It bears fruit when something
  happened outside (sent, merged, done with a link) and he marks it; a stage the council moves it to is not fruit.
  Letting it go needs no reason ("Just let it go" in bars-engine) and stops carrying and resurfacing (`ttv-fruit-is-his`).
- **Set aside.** A live task can rest in his seed library instead: out of the day, never carried or resurfaced, drawn
  back into a day only when he chooses, as the same task (`docs/seed-library.md`, the `sl-*` positions). On the board
  served by bars-engine, "Set aside" sits beside each sealed item; the Morning tab's closed Seed library panel lists
  what rests there.
- **Lenses emerge.** For a creator who skipped the intake, the council reads his saved bars-engine free writes for goals
  that return (`ttv-saved-read-scoped`, `ttv-lens-emerge`):
  1. `python3 council/lens_emerge.py fetch --out <scratch>/vein.json` reads `GET /api/tap-the-vein/history` (same token
     as the menu) into a scratch folder; it refuses a path inside the repo. bars-engine logs each read with no text.
  2. The read pitches at most five goals, each paraphrasing what he wrote on two or more mornings and citing only
     the dates; his words are never quoted, because the writing is raw (`ttv-lens-emerge`, overruled 2026-10-16).
     `pitch` refuses a gist that copies six or more of his words in a row:
     `python3 council/lens_emerge.py pitch <scratch>/vein.json --pitches p.json > rows.json`, then
     `board/sync_board.py --rows`. It deletes the scratch copy.
  3. He keeps or drops each on the Open tab; `python3 council/lens_goals.py kept --send` writes kept ones to bars-engine.
  4. Once a goal exists, a strand's call sheet gets a `lens: <goal id>` line only after he keeps that pairing. A strand
     with none keeps running.
- **The board's box** runs one phase at a time under a rail (what you can do, free write, keep your lines, seal), with
  bars-engine's line "No floor to clear · no streak to keep · stuckness is data, not failure" (`ttv-board-one-phase`).

## Lens goals on the Morning tab

`lens-board-reads-goals` (Lenses pass 1, 2026-10-14): the board reads his Lens goals every morning without needing a
sealed menu. `council/morning.py` reads bars-engine's `GET /api/lenses/goals` with the same `COUNCIL_MENU_TOKEN`
(or a saved copy with `--goals <file>`), and its goals win over the menu's goals list. The Morning tab shows them in
the "Your Lens goals" panel, one row per domain, with an empty domain shown as "No goals here yet". When the export
cannot be read, the panel says why and falls back to the goals in the sealed menu.

## The categories

| Key | Source |
|---|---|
| `menu` | The kept lines from Tap the Vein |
| `board` | Questions with no answer, and new positions that stand unless he flips them |
| `steps` | Undone steps on the Your steps tab due today or earlier (`--steps <dir>`, the store's `steps` collection saved with ArtifactData). Steps live only in the store, so nothing read them until 2026-10-13 |
| `due` | Deferred items due within a week (`council/due.py`) |
| `handoff` | Bold items under "Open on" in `council/HANDOFF.md`, minus those marked done, closed, recorded or picked |
| `prs` | Open pull requests in the council, bars-engine and the Game Master's guide (GitHub API, or `--prs <file>`) |
| `backlog` | bars-engine `.specify/backlog/BACKLOG.md` rows marked Ready (`--bars <checkout>`, default `../bars-engine`) |

Within a category, items with a goal come first and unaligned items last; none is hidden. A bridge is one of:
`named` (bars-engine or he named the goal), `existing` (shares two or more words with a goal), `new` (shares one word;
the suggestion is a goal one time scale smaller under that goal), or `unaligned`. The script's bridges come from
shared words, never a model, so they are suggestions he accepts or edits. A kept line he bridged at seal keeps his
goal; one he left unaligned stays unaligned until he picks a goal on the board.

## Reading the export from a council session

Checked 2026-10-09 from a council thread:
- The container cannot reach `bars-engine.vercel.app`: the proxy refuses the tunnel (403). The project runs on the
  built-in cloud environment, which has no network settings.
- The Vercel connector can reach it: `web_fetch_vercel_url` on `/api/health` returned 200. It sends a plain GET with
  no headers of its own.
- The export (bars-engine #267) is `GET /api/tap-the-vein/menu[?date=YYYY-MM-DD]` with `Authorization: Bearer
  <COUNCIL_MENU_TOKEN>`, for the one player `COUNCIL_MENU_PLAYER_ID` names: 503 without the token, 401 with a wrong
  one, 404 when no menu is sealed. The connector cannot send that header.

Wendell ruled `mm-menu-transport` on 2026-10-09 (ledger `2026-10-09-pull-185337`): the council fetches the menu
itself. The key lives in two places he sets once (Your steps list `morning-menu-key`), and never on the board or in
chat:
- **Vercel, bars-engine:** `COUNCIL_MENU_TOKEN` and `COUNCIL_MENU_PLAYER_ID`.
- **The council project's cloud environment:** the same `COUNCIL_MENU_TOKEN` as an environment variable, with
  `bars-engine.vercel.app` under Allowed domains. Sessions started after that run on it.

Then a council session runs `python3 council/morning.py --fetch YYYY-MM-DD --out <file> --write` on main. It sends
the key as a Bearer header, so the key stays out of the URL and Vercel's request logs, which is better than the
query-string fetch the ruling accepted. If the host is still out of reach, the script says so; the route also takes
`?token=` (bars-engine #267) for a fetch through the Vercel connector, which puts the key in that session's record.

**Fallback, any morning:** Tap the Vein's "Copy the sealed menu" button copies the JSON, and he pastes it in the
Morning tab's "Or paste this morning's menu" box. The page shows his kept lines at once and saves the text at
`morning/menu`; `board/pull.py` lists it under needs work, and the read runs `council/morning.py --menu
<dir>/morning/menu.json --write`.

## The export's shape

`docs/morning-menu.example.json` is a filled-in example with made-up goals.

```
{"version": 1, "sessionDate": "YYYY-MM-DD", "sealedAt": "<iso>",
 "goals": [{"id", "title", "domain", "cadence", "parentId"}],          (coming with the transport change)
 "items": [{"key", "text", "source": "task|kept_line", "status": "bridged|unaligned",
            "goal": null | {"id", "title", "domain", "cadence", "chain": [titles], "trace": "A → B → C"}}]}
```

The menu is frozen at seal. A suggestion he never accepted exports as unaligned, so every bridge in it is his. Until
the export carries `goals`, morning.py bridges backlog items to the goals his bridged items name. `morning.py` and the
board both refuse a menu that carries `rawEntry`.
