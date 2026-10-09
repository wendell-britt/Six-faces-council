# The morning menu

Wendell, 2026-10-09: "If I'm able to start the day with a free write and with the context of our operations backlog and
what emerges for me during the free write I can create a menu of things to add to the council board each day that are
aligned with my goal." The pass is `council/passes/6FACE_PASS_morning-menu1_2026-10-09.md`; the rulings are in
`council/ledger/2026-10-09-pull-181703.json`.

## A morning, end to end

1. He writes in Tap the Vein (`mm-where`) and seals the session. Only the lines he keeps leave it (`mm-raw`); the
   free write itself never does. bars-engine bridges each kept line to a Lens goal or suggests one.
2. A council session fetches the export, saves it to a file, and runs `council/morning.py --menu <file> --write` on
   main. The script gathers each source as its own category and bridges every item to a goal. Then the session
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
shared words, never a model, so they are suggestions he accepts or edits. When bars-engine sends its own suggestion
for a kept line, that suggestion wins.

## Reading the export from a council session

Checked 2026-10-09 from a council thread:
- The container cannot reach `bars-engine.vercel.app`: the proxy refuses the tunnel (403). The project runs on the
  built-in cloud environment, which has no network settings.
- The Vercel connector can reach it: `web_fetch_vercel_url` on `/api/health` returned 200. It sends a plain GET with
  no headers of its own, so the export cannot use a Bearer header.
- `BARS_API_KEY` is set in Vercel (`/api/bar-registry` answers 401, not 503), but no council session holds its value.

So the export takes its token in the query string, and the fetch is one connector call:

    web_fetch_vercel_url  https://bars-engine.vercel.app/api/tap-the-vein/morning-menu?date=YYYY-MM-DD&token=<t>

The session writes the response's `text` to a file and passes that file to `--menu`. The Tap the Vein menu thread in
bars-engine builds the endpoint and decides where the token lives; this file follows what it builds.

## The export's shape

`docs/morning-menu.example.json` is a filled-in example with made-up goals.

```
{"version": 1, "date": "YYYY-MM-DD", "sealedAt": "<iso>" | null,
 "goals": [{"id", "title", "domain", "cadence": "year|quarter|month|week", "parentId", "status"}],
 "items": [{"id", "text", "goalId": "<id>" | null,
            "suggestion": null | {"kind": "existing|new", "goalId"?, "title"?, "cadence"?, "parentId"?},
            "accepted": true|false}]}
```

`goals` holds his active Lens goals; backlog items are bridged to them too. `morning.py` refuses a file that carries
`rawEntry`.
