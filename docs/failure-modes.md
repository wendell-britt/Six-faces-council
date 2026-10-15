# From "I save an answer" to "it's on main": failure modes

Written 2026-10-15 after the Nonprofit Board's Send stalled. The run `trig_013Qmc7KZJNNDXAiLbuncGva` fired at
20:09:44 UTC (session `cse_01Dw9RF7MbLEDvfL8ANSqqNn`) and stayed pending when the account ran out of tokens. The
board's own record of that Send (`pickup/last` in the artifact store, written 20:09:48) names five rows:
`morning/menu` and four `picks/menu-task:*`. The four picks were already on main (ledger
`council/ledger/2026-10-15-pull-195357.json`, pushed 19:55), so the Send asked for work that was done. The one save
truly stranded is `morning/menu` (saved 19:52:17), which `pull.py` never records itself: it hands it to a session to
run `council/morning.py`, and no session came. Recovery is in docs/incidents.md.

## Until 2026-10-15: the claude.ai chain

| # | Step | What it runs on | Vendor or quota it depends on | How it failed, or could | Visible? |
|---|------|-----------------|-------------------------------|-------------------------|----------|
| 1 | Open the board | claude.ai artifact page | Anthropic (claude.ai up, signed in to the nonprofit's org) | outage; wrong org | yes |
| 2 | Save an answer | `claude.use("db")`, the artifact store | Anthropic artifact runtime | store unavailable: banner "This view cannot save" | yes |
| 3 | Press Send | `mcp` capability, Claude Code Remote connector, `fire_trigger` | Anthropic connector auth, page permission grant, org policy | needs_reauth, not_granted, blocked_by_policy | yes, a message per code |
| 4 | The routine starts a session | Claude Code Remote routine `trig_013Q…` | **Anthropic token quota of this account** | **2026-10-15 20:09: run stays pending; nothing tells anyone** | **no**: `fire_trigger` returned, the page wrote `pickup/last`, and the bar went dark |
| 5 | Session saves the store | ArtifactData tool | Anthropic (Claude-only tool) | session never starts (step 4) | no |
| 6 | `pull.py --push` | Python + git in the session | GitHub via Claude Code's GitHub app | auth lapse, push race (handled by retries) | in the session only |
| 7 | Pasted morning menu | `morning.py --menu`, `COUNCIL_MENU_TOKEN` | an AI session to run it; bars-engine for goals | **this is the save stranded on 2026-10-15** | no |
| 8 | Republish the board | Artifact tool | Anthropic (Claude-only); this org has no GitHub connector, so the page itself can never write GitHub | session never starts | stale page |
| 9 | Safety net | the council's daily routine pulls the Council Board | Anthropic quota again, and it never read the Nonprofit Board's store | same quota, wrong board | no |
| 10 | Act on needs-work | a Claude thread | Anthropic quota | stalls with step 4 | no |

Every path from step 3 to main went through one Anthropic account's quota, and the one failure that happened was the
silent one.

## From 2026-10-16: bars-engine and a GitHub Action

| # | Step | What it runs on | Vendor or quota it depends on | How it fails | Visible? |
|---|------|-----------------|-------------------------------|--------------|----------|
| 1 | Open https://bars-engine.vercel.app/board | Next.js route, sign-in cookie, single owner (`BOARD_OWNER_PLAYER_ID`) | Vercel hosting; GitHub raw for the page (cached 5 min, last good copy kept in memory) | Vercel down; raw.githubusercontent.com down with a cold cache: 503 page | yes |
| 2 | Save an answer | POST `/api/board/saves`, checked against `schema/board-save.schema.json`, row in `BoardSave` | Vercel functions; the Postgres provider behind `DATABASE_URL` | 4xx/5xx: the control shows "Not saved" and the answer stays on screen | yes |
| 3 | Schedule | `.github/workflows/board-pull.yml`, every 15 min | GitHub Actions (free minutes on a public repo) | cron delayed under load; **GitHub disables schedules in a public repo after 60 days without activity** | a run that never happens is silent; see "What is left" |
| 4 | Fetch the store | `board/fetch_store.py fetch` → GET `/api/board/pull` | Vercel, Postgres, `BOARD_PULL_TOKEN` in both places | token missing or rotated on one side: 401 | red run, emailed |
| 5 | Record | `board/pull.py --push --no-room`, unchanged | GitHub (`GITHUB_TOKEN`, contents: write) | push race (retries, merge drivers); a branch rule that forbids pushes to main | red run |
| 6 | Pasted morning menu | `council/morning.py --menu --write` | bars-engine, `COUNCIL_MENU_TOKEN` | secret missing: warning, menu left unacknowledged, so step 9 goes red after 6 h | yellow, then red |
| 7 | Rebuild the board | `board/nonprofit/build.py`, push | GitHub | template line moved: build asserts | red run |
| 8 | Acknowledge | `fetch_store.py ack` → POST `/api/board/pull` | Vercel, Postgres | fails after push: saves stay unacknowledged; the next run finds them recorded and acks them | red run, self-healing |
| 9 | Staleness | `board/staleness.py --hours 6` | Vercel, Postgres | any save unrecorded > 6 h | red run, emailed |
| 10 | Act on needs-work | `board/needs_work.py`, `AGENTS.md` | none: any agent (Claude, Codex, ChatGPT, API) or a person | nobody picks it up; the list keeps it | the Action's summary lists it |

No AI vendor and no token quota sits between a save and main. The pieces that remain are hosting (Vercel), the
database provider, and GitHub, each of which fails loudly except a schedule that stops firing.

## What is left

- A schedule GitHub has switched off produces no red run. The Action commits only when there are saves, so a quiet
  month could reach the 60-day limit. The check for it is outside GitHub: bars-engine's `/api/board/pull` records the
  time of the last pull, and the board page shows "last recorded on main" under the save bar, so a pull that has not
  happened is visible where he saves.
- Vercel and the Postgres provider are single vendors. Saves are rows with their full document, so a dump moves
  them; the store folder layout `pull.py` reads is provider-neutral.
