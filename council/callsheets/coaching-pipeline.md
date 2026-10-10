2026-10-10 (22:45)
# Coaching pipeline (lead generation for masteringallyship.com/coaching)

## Next
Wendell answered both picks on 2026-10-10 (board read 2234): `lg-first-pipe` = guesting, `lg-keep-step` = daemons-list.
- First pipe: guesting on other shows. Claude builds the guest-show list on the Outreach tab (`lg-guest-shows`) and
  drafts pitches for Wendell to send. The letter and the live session wait.
- Keep step: the coaching page's centre now offers the Meet Your Daemons series by email (bars-engine draft PR, branch
  `claude/project-thread-lr11l2`). It adds a `daemons` list (Resend topic "meet your daemons"); the address is stored
  on FunnelSignup with intent `daemons`, source `coaching`. This is the one exception to `cg-browser-only`: what the
  visitor carried in still stays in the tab. Nothing is sent yet. The series goes out only after Wendell edits the
  seven emails, and no sequence automation exists for it.
- Still open: Vercel Web Analytics switch and PR #273 (Your steps list `coaching-pipeline`, due 2026-10-13). Each
  Monday a session reads Web Analytics by `utmSource` (Vercel MCP `aggregate_pageviews`, project bars-engine) and
  Calendly bookings by utm, and writes a Results line per pipe in the plan file. Tests fall due 2026-10-20 and
  2026-11-07 (see the pass). The podcast strand adds the tagged walk link to MTGOA show notes and captions
  (`lg-podcast-link`).

## Waiting on
Wendell: the Web Analytics switch, PR #273 review, the daemons opt-in PR review, and his edit of the Meet Your Daemons
series (the file named in the pass is not in the project folder now).

## Files
- `council/passes/6FACE_PASS_leadgen1_2026-10-10.md`, `council/ledger/2026-10-10-leadgen1.json`
- `/mnt/project-files/lead-gen-research/coaching-pipeline-plan.md` (the one live plan), `elevenlabs-zeely-for-coaches.md`
- bars-engine PR #273 (`src/lib/coaching/source-tags.ts`)
- bars-engine daemons opt-in: `src/app/coaching/ForestWalk.tsx` (`#daemons`), `src/actions/leads.ts`
  (`captureDaemonsSeries`), `src/lib/esp/list-contract.ts` (`daemons`)

## Archive
Nothing is archived yet.
