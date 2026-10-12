2026-10-12 (19:50)
# Coaching pipeline (lead generation for masteringallyship.com/coaching)

## Next
Wendell answered both picks on 2026-10-10 (board read 2234): `lg-first-pipe` = guesting, `lg-keep-step` = daemons-list.
- First pipe: guesting on other shows. Built 2026-10-12: 14 shows on the Outreach tab's Guesting list, all
  Identified, each row holding its pitch and tagged link (`utm_source=guest&utm_campaign=<show>`). The full list,
  sources and what was dropped are in `/mnt/project-files/lead-gen-research/guest-pitches-2026-10-12.md`. The
  Daily Evolver has been silent since March 2024 and is off the list. Your steps `coaching-pipeline-04` (due
  2026-10-19) asks Wendell to send the first three: Coaches Rising, The Embodiment Podcast, Buddhist Geeks (after
  Vince records on 16 Oct). The letter and the live session wait.
- Keep step: the coaching page's centre now offers the Meet Your Daemons series by email (bars-engine draft PR, branch
  `claude/project-thread-lr11l2`). It adds a `daemons` list (Resend topic "meet your daemons"); the address is stored
  on FunnelSignup with intent `daemons`, source `coaching`. This is the one exception to `cg-browser-only`: what the
  visitor carried in still stays in the tab. Nothing is sent yet. The series goes out only after Wendell edits the
  seven emails, and no sequence automation exists for it.
- PR #273 merged 2026-10-12 16:43 UTC, and Wendell ticked the Web Analytics step, but Vercel's API still answered
  "Web Analytics not found" at 16:44 UTC. The first Monday read checks that first; if it still fails, the step goes
  back on his list with what Vercel shows. Each
  Monday a session reads Web Analytics by `utmSource` (Vercel MCP `aggregate_pageviews`, project bars-engine) and
  Calendly bookings by utm, and writes a Results line per pipe in the plan file. Tests fall due 2026-10-20 and
  2026-11-07 (see the pass). The podcast strand adds the tagged walk link to MTGOA show notes and captions
  (`lg-podcast-link`).

## Waiting on
Wendell: sending the first three guest pitches (step 04), the Web Analytics switch, PR #273 review, the daemons opt-in PR review, and his edit of the Meet Your Daemons
series (the file named in the pass is not in the project folder now).

## Files
- `council/passes/6FACE_PASS_leadgen1_2026-10-10.md`, `council/ledger/2026-10-10-leadgen1.json`
- `/mnt/project-files/lead-gen-research/coaching-pipeline-plan.md` (the one live plan), `elevenlabs-zeely-for-coaches.md`
- bars-engine PR #273 (`src/lib/coaching/source-tags.ts`)
- bars-engine daemons opt-in: `src/app/coaching/ForestWalk.tsx` (`#daemons`), `src/actions/leads.ts`
  (`captureDaemonsSeries`), `src/lib/esp/list-contract.ts` (`daemons`)

## Archive
Nothing is archived yet.
