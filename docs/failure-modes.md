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
| 3 | Schedule | `.github/workflows/board-pull.yml`, cron every 15 min | GitHub Actions (free minutes on a public repo) | **GitHub drops most scheduled runs in this repo: the steward's hourly cron ran 52 times in 287 hours (median gap 5.6 h, longest 10.5 h); board-pull's 15-minute cron had not run once in the first hour.** GitHub also disables schedules after 60 days without activity | a run that never happens is silent; see "Root cause" |
| 4 | Fetch the store | `board/fetch_store.py fetch` → GET `/api/board/pull` | Vercel, Postgres, `BOARD_PULL_TOKEN` in both places | token missing or rotated on one side: 401 | red run, emailed |
| 5 | Record | `board/pull.py --push --no-room`, unchanged | GitHub (`GITHUB_TOKEN`, contents: write) | push race (retries, merge drivers); a branch rule that forbids pushes to main | red run |
| 6 | Pasted morning menu | `council/morning.py --menu --write` | bars-engine, `COUNCIL_MENU_TOKEN` | secret missing: warning, menu left unacknowledged, so step 9 goes red after 6 h | yellow, then red |
| 7 | Rebuild the board | `board/nonprofit/build.py`, push | GitHub | template line moved: build asserts | red run |
| 8 | Account and acknowledge | `fetch_store.py ack` → POST `/api/board/pull`, one call per status | Vercel, Postgres | a save neither on main nor passed over on purpose: left unacknowledged, step fails; fails after push: the next run finds them recorded and acks them | red run, self-healing; the summary's "Saves accounted" table names every save |
| 9 | Staleness | `board/staleness.py --hours 6` | Vercel, Postgres | any save unrecorded > 6 h | red run, emailed |
| 10 | Act on needs-work | `board/needs_work.py`, `AGENTS.md` | none: any agent (Claude, Codex, ChatGPT, API) or a person | nobody picks it up; the list keeps it | the Action's summary lists it |

No AI vendor and no token quota sits between a save and main. The pieces that remain are hosting (Vercel), the
database provider, and GitHub, each of which fails loudly except a schedule that stops firing.

## Root cause (2026-10-15, measured after the first runs)

The first read of the 20:09 stall named the cause as "an AI vendor's quota sits between a save and main" and moved
the trigger to GitHub Actions. Three problems followed in the first two hours: the steward could not import the new
contract test, run 2 acknowledged three saves and recorded one with no reason, and the 15-minute schedule did not
fire. Each one has the same cause as the stall.

**The design was checked against its own description, not against what its dependencies do.**

- The trigger. A Claude routine was replaced by a GitHub cron, and neither was measured. This repo's Actions
  history already showed the answer before the kit was written: the steward's hourly cron (`17 * * * *`) ran 52
  times between 2026-10-03 23:04 and 2026-10-15 22:18, which is 287 hours. The median gap was 5.6 hours, the 90th
  percentile 7.3 and the longest 10.5. GitHub drops scheduled runs under load and does not queue them. A 15-minute cron is a
  hope, not a schedule. The page's note ("The pull runs every 15 minutes, so this is late") repeats the same
  unmeasured claim.
- The alarm. `board/staleness.py` runs inside board-pull, so when the schedule does not fire, the alarm does not fire
  either. The stall at 20:09 was silent for the same reason: the routine that failed was also the step that would have
  reported it. The page's late note in bars-engine is the one alarm that lives outside the job.
- The ledger. Nothing tracked each save from arrival to main. The 20:09 Send asked for four picks main already held,
  and run 2 acknowledged two saves no one could name. `ack` now gives each save a status (below), which fixes the
  record but not the trigger.
- The gate. The patch was verified with `pytest` after installing jsonschema, and the repo merges on the steward's
  `unittest` run with only pyyaml. The landing session tested the command it was given instead of the gate that decides
  the merge (fixed in #174).

What follows from it:

1. A save starts its own pull. The save is the event, so the event should trigger the work: bars-engine calls
   GitHub's `workflow_dispatch` for board-pull when a save lands. The cron stays as a sweep for anything missed. This needs a
   GitHub credential in Vercel, which is Wendell's to create or refuse; the question is on the Council Board
   (`np-pull-trigger`).
2. The alarm lives where he saves, and measures what matters. The page warns from the oldest pending save's age, not
   from the last pull's age: with no pending saves, a long gap between pulls is not late. bars-engine already holds both numbers.
3. Claims in this file are measured. A figure here cites the run history or a test that checks it.

## Every acknowledged save is accounted for

Run 2 (2026-10-15 22:22) acknowledged three saves and recorded one, and nothing said what the other two were. Since
then `fetch_store.py ack` gives every pending save one status before anything is acknowledged, prints the table to
the run summary, and sends each status as its own acknowledgement, so `board_saves.record` in bars-engine reads, for
example, `six-faces-council@a491791 superseded`:

- `recorded`: main holds it. `superseded`: a newer save of the same document came in, and only the newest is judged.
- `nothing-to-record`: the newest save holds nothing pull.py records (an emptied answer, a removed pick).
- `held`: left unacknowledged on purpose (`--except`, or a freewrite or Tap the Vein for a session), so step 9 goes
  red after six hours if nobody does it.
- `unaccounted`: anything else. It stays unacknowledged and the step fails.

Run 2's two unexplained saves were acknowledged before this existed; their rows carry `six-faces-council@a491791`
with no status, and only a query on `board_saves` can say what they were.

## What is left

- A schedule GitHub has switched off produces no red run. The Action commits only when there are saves, so a quiet
  month could reach the 60-day limit. The check for it is outside GitHub: bars-engine's `/api/board/pull` records the
  time of the last pull, and the board page shows "last recorded on main" under the save bar, so a pull that has not
  happened is visible where he saves.
- Vercel and the Postgres provider are single vendors. Saves are rows with their full document, so a dump moves
  them; the store folder layout `pull.py` reads is provider-neutral.
