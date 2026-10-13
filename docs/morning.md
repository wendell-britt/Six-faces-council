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

## The categories

| Key | Source |
|---|---|
| `menu` | The kept lines from Tap the Vein |
| `board` | Questions with no answer, and new positions that stand unless he flips them |
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
