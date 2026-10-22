# Rotating COUNCIL_MENU_TOKEN

`COUNCIL_MENU_TOKEN` is the key the council sends to bars-engine for the morning menu, Lens goals, the Council Board
store (`/board/council`, `board/store_write.py`), the unchosen read and WAVE runs. bars-engine compares the key it
receives with its own copy (`src/lib/council/token.ts`), so all three copies below must hold the same value.

`BOARD_PULL_TOKEN` is a different key (the 15-minute board pull, `board/fetch_store.py`). Rotating one does not touch
the other.

## What went wrong on 2026-10-21 (so it does not again)

Every council call answered 401 from about 19:28 UTC. In the thread "Council menu token fix" Wendell rotated the key
three times before it held. Two faults stacked:

- **The key lived only on the clipboard.** Something else got copied over it between pastes, so Vercel ended up with a
  key nobody had. Fix: the key now lives in one private file on his Mac, `~/.council-menu-key`, and every paste comes
  from that file.
- **The Claude environment sends the key without the word `Bearer`.** Its network secret puts `Authorization: <key>`
  on each request, and bars-engine only read `Authorization: Bearer <key>`. So the keys matched and still got 401.
  bars-engine #424 (merged 2026-10-22) accepts both shapes.

The page that found both is `https://bars-engine.vercel.app/api/council/token-check` (bars-engine #422, #423). It shows
the length and an 8-character fingerprint of the server's key and of the key a caller sent, never the key itself, so
the output is safe to paste in chat.

## When to rotate

- A council call answers 401 from a fresh session and token-check shows the fingerprints differ, or
- the key has been seen somewhere it should not be (a chat, a log, a screenshot, a URL with `?token=` in a shared
  record), or
- once a year as housekeeping.

A thread that hits a 401 does not ask in chat: it runs the token-check line below first, then the coordinator opens one
rotation thread that walks him through this page.

## Step 0: make the key (Terminal on his Mac)

```
(cd ~ && umask 077 && openssl rand -hex 32 | tr -d '\n' > ~/.council-menu-key && pbcopy < ~/.council-menu-key && wc -c < ~/.council-menu-key)
```

Success: it prints `64`. The key is now in `~/.council-menu-key` (readable only by him) and on the clipboard. Never
paste it into a chat with Claude. Before each paste below, put it back on the clipboard with:

```
(cd ~ && pbcopy < ~/.council-menu-key)
```

## Step 1: Vercel, bars-engine (then redeploy)

1. Open https://vercel.com/wendells-projects-9c1b16dc/bars-engine/settings/environment-variables and search
   `COUNCIL_MENU_TOKEN`. There should be one row; it covers Production, Preview and Development.
2. **⋯** on that row, **Edit**, clear the value box, press **⌘V**, **Save**.
3. Open https://vercel.com/wendells-projects-9c1b16dc/bars-engine/deployments, **⋯** on the top **Production** row,
   **Redeploy** (untick "Use existing build cache" if offered), confirm.
4. When the new deployment shows **Ready** (3 to 5 minutes), check from Terminal:

```
(cd ~ && curl -s -H "Authorization: Bearer $(cat ~/.council-menu-key)" https://bars-engine.vercel.app/api/council/token-check; echo)
```

Success: `"match":true`. The Vercel connector cannot write production values, so this step is always his.

## Step 2: the council project's Claude cloud environment

1. Put the key on the clipboard (line above).
2. Project settings, Environment, the **Cloud environment** menu, the **gear** beside **Default**.
3. Under **Network secrets** (called **API credentials** in an older app), edit `COUNCIL_MENU_TOKEN` for
   `bars-engine.vercel.app`, clear it, **⌘V**, **Save**.

On 2026-10-22 threads already running picked up the new key within minutes, but test from a fresh session to be
sure.

## Step 3: GitHub Actions secret on Six-faces-council

1. Put the key on the clipboard (line above).
2. https://github.com/wendell-britt/Six-faces-council/settings/secrets/actions, the pencil beside `COUNCIL_MENU_TOKEN`,
   **⌘V**, **Update secret**.

The `board-pull` workflow reads it for the pasted and sealed menus and Lens goals.

Optional: if he runs bars-engine locally with the council routes, the same value goes in `~/bars-engine/.env.local` as
`COUNCIL_MENU_TOKEN=...`.

## Check it works (a Claude session started after step 2)

```
for p in "/api/board/session-writes?collection=steps" /api/tap-the-vein/menu /api/lenses/goals; do curl -s -o /dev/null -w "$p %{http_code}\n" "https://bars-engine.vercel.app$p"; done; curl -s https://bars-engine.vercel.app/api/council/token-check; echo
```

Success: 200 on each route (the menu may say 404 when no menu is sealed today; that also means the key was accepted).
If one says 401, read the token-check line: `authorization.valuePrint.fingerprint` is what the Claude environment sent,
`server.fingerprint` is Vercel's. Different fingerprints: redo step 2 (or step 1 if Wendell's Mac check fails too).
Same fingerprints and still 401: the sending shape changed again; look at `authorization.scheme` and
`src/lib/council/token.ts`.

For step 3, run the `board-pull` workflow by hand with a `menu_date`
(https://github.com/wendell-britt/Six-faces-council/actions/workflows/board-pull.yml, **Run workflow**): "No sealed
menu" (404) means the key was accepted; 401 means redo step 3.

## After a 200

The rotation thread tells the coordinator, which starts the work that waits on the key (see
`council/callsheets/board-plumbing.md`, `morning-menu.md` and the unchosen-read trigger in `docs/unchosen-read.md`).
