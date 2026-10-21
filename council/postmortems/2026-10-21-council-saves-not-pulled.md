# The Council Board's saves waited 22 hours for main, 20–21 October 2026

Wendell, 2026-10-21, with a screenshot of the Council Board: "173 saves have waited for main 22 h (the oldest). Main has
not recorded a pull from this board yet."

## What happened

Nothing was lost. bars-engine held every save in Postgres (`board=council`). main never pulled them, because
`.github/workflows/board-pull.yml` set `BOARD: nonprofit` and had no council pass. The 10-20 import moved the Council
Board to bars-engine and `council/callsheets/board-plumbing.md` listed "give board-pull.yml a council pass" as the
follow-up. That line was not done. The Nonprofit runs stayed green every 15 minutes, so nothing looked wrong.

The page's own warning was the only signal. It fires after six hours, and nobody saw it until he did.

## Why it was silent

- The workflow and the staleness check both answered for the Nonprofit Board only. A green run said nothing about the
  Council Board.
- The follow-up lived in a callsheet, not in a test or a check.

## What changed (council #343)

- board-pull.yml pulls the Council Board as well: fetch, `pull.py --push`, ack, staleness (all `BOARD=council`).
  The first run recorded 172 of 174 saves, including his `gs-care-is-the-cost` ruling.
- A step fetches the Tap the Vein menus he sealed in bars-engine (`ttv/<date>`, oldest first). pull.py leaves these
  for a session, so they would have kept the staleness check red.
- `board/fetch_store.py` held every sealed menu except the newest forever. Now only a date newer than `morning.sealed`
  is held.

## Separate: two-minute database blip

Between 16:53:36 and 16:55:31 UTC bars-engine logged 7 Prisma P1001 errors ("Can't reach database server",
`/api/board/pull` and `/login`), which failed two of my pull runs. It did not repeat. Cause unknown; if it recurs, look at
the Prisma Postgres dashboard for a paused database or a connection limit.

## What was not checked

The Prisma Postgres dashboard (not reachable from a session). Whether the 10-20 sealed menu's content was wanted: it is
fetched like any other, but only the newest date stays as `morning.sealed`.
