# Six-face pass: podcast pipeline 2, Claude scheduling posts through Meta's publishing API

Wendell asked on 2026-10-16 at 17:42 UTC in the Mastering the Game of Allyship project, quoting the thread's last reply:
"Claude could later schedule posts itself through Meta's own publishing API. That's a separate build, not a switch to
flip: it needs a Meta developer app, a login token, the clips at a public link, and Claude running the schedule." His
words: "let's create a plan for getting this set up including costs etc". This is the second pass on the pipeline. Pass
one is `6FACE_PASS_podcast-pipeline1_2026-10-16.md`.

**Board read.** The board pull of 17:34 UTC recorded his answers: `pp-who-schedules` = the one computer sitting, and all
six `pp-` positions stand. Your steps `podcast-pipeline` 02 and 03 (check Meta Business Suite, then episode 2's
sitting) went up at 17:52 UTC.

**Casts** (`council/iching/cast.py --json`, in the ledger): Shaman 42 Windfall, lines 4 and 6, becomes 17 Following.
Architect 9 Restraint, lines 2, 3 and 4, becomes 25 Candour. Challenger 52 Stillness, no changing lines. Regent 18 Stale
Air, lines 3 to 6, becomes 47 Drained. Diplomat 6 Divergence, no changing lines. Sage 44 Serendipity, lines 1 and 2,
becomes 13 Fellowship.

**Daemons.** None were sent. The research is Meta's, X's and Vercel's own pages, read in this session and cited below.

## Scorecard

Pass one's tests are not yet due: episode 2 fully out or scheduled by 2026-10-26, and episode 3 at four touches or
fewer. This pass adds no reason to move them. Episode 2 still goes out through the sitting he picked.

## Anchor

Claude prepares each episode's posts and Wendell approves the whole queue once. From then on, a timer Claude built
publishes each post on its day, with no phone and no sitting. Publishing stays his act, and the approval is where he
performs it.

## What Meta's pages say

- **Instagram Reels** publish through a container with `media_type=REELS`. It takes `cover_url` (a public JPEG of 8 MB
  or less, 9:16, which overrides the frame offset), `share_to_feed`, `caption` (2,200 characters) and up to three
  `collaborators`. The video can be a public URL, or a resumable upload of a local file "only for apps that have
  implemented Facebook Login for Business". Instagram has no scheduling field, so the app publishes at the hour itself.
  The limit is 100 API posts in 24 hours (the page also says 50 in one place).
  Source: https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media and
  …/content-publishing.
- **Facebook Page Reels** publish through `/{page-id}/video_reels` in three phases, with `video_state` set to
  `SCHEDULED` and a publish time "greater than 10 minutes from the current time and within 29 days". They need
  `pages_show_list`, `pages_read_engagement` and `pages_manage_posts`, a 3 to 90 second 9:16 video, and a Page, not a
  personal profile. The limit is 30 posts in 24 hours. Source: https://developers.facebook.com/docs/video-api/guides/reels-publishing.
- **Access.** Standard Access is enough for an app that serves only accounts its owner manages; Advanced Access, with
  App Review and business verification, is for other people's accounts. A user token lasts 60 days and can be
  refreshed. Source: adaptlypost.com's summary of Meta's scope rules, unchecked against Meta's own page.
- **X** dropped its free tier for new developers. Pay-per-use started on 2026-02-06, at $0.015 a post, or $0.20 for a
  post with a link; the page gives two dates for that price, and no media upload price. Source:
  https://postproxy.dev/blog/x-api-pricing-2026, unchecked against X's own page.
- **Vercel Blob** is free on Hobby up to 1 GB stored and 10 GB transferred a month, and on Pro storage is $0.023 a GB-month.
  Source: https://vercel.com/docs/storage/vercel-blob/usage-and-pricing. The plan below does not need it.

## Shaman

**Windfall becomes Following.** More is arriving than he put in: the clips, the covers and the captions already exist
for every episode. The work now is inside what pass one opened, and the timer follows his yes instead of his
remembering.

**The felt read is relief, with one exposure moved earlier.** Approving five posts at once is the same act of courage as
the sitting, without the forty minutes of uploading. The Shaman guards the approval: it must show each post
whole, cover and words, so his yes is a real yes and not a click on a list.

## Architect

**Restraint becomes Candour.** A small rule is holding all of this: Instagram has no scheduling field. So something has
to wake at the hour and publish. The council already runs one such timer, `board-pull.yml`, every fifteen minutes on
GitHub Actions, free because the repo is public.

**The machine, with no paid host.**

1. *Kit.* When an episode's clips are cut, Claude stages them from his Mac and uploads them as assets of a GitHub
   release on the council repo (`pod-ep03`). The covers go in the repo beside the queue, so each has a plain public URL.
2. *Queue.* Claude writes `podcast/queue/<episode>.json`: for each post, the time, the networks, each network's
   caption, the clip asset and the cover.
3. *Approval.* The queue goes on the board as one question, with every post shown whole and the covers as images. His
   approval is the publishing act.
4. *Publish.* A new workflow, `publish-queue.yml`, runs every fifteen minutes. It reads approved queues, takes each post
   that is due, uploads the clip to Meta by resumable upload (no public video link needed), sets the cover from its
   repo URL, publishes to Instagram and to the Page, and writes the post ids back into the queue.
5. *Numbers.* Each Monday the same workflow reads each post's plays, saves and shares from the insights endpoints into
   the episode's results. This replaces his "note the numbers" step.

**The token never passes through Claude.** Wendell makes a system user token in Meta Business Suite's business
settings, set never to expire, and pastes it into the council repo's GitHub Actions secrets himself. Only the workflow
reads it. A step never holds it.

## Challenger

**Stillness, no changing lines.** The move is to stop while the wanting is still running. Episode 2's sitting has not
happened yet, and no clip numbers exist. The Challenger would run the sitting once before building, so the build knows
what the sitting cost.

**What breaks.**

- *Captions.* His rule is no words burned in, with Instagram's auto captions on (`pod-clip-no-words`). The publishing
  API has no captions switch. If an API-published Reel shows no auto captions, the rule and the build collide. The pilot checks
  this first.
- *Development mode.* A Meta app still in development mode may publish posts that only the app's own people can see.
  The app has to go Live, and Live needs a privacy policy link.
- *Covers.* `cover_url` takes a JPEG. The covers exist as JPEGs (`covers/*.jpg`), and the renderer must keep making
  them.
- *Silent failure.* Flirtcraft's deploys failed for three weeks unheard (`fc-silent-failure`). A post that fails to
  publish must open a step on his list the same hour.

**Falsification tests**, each naming the blocker it resolves. The upload works: a container for one of episode 2's clips
reaches `FINISHED` without being published. The captions: the first live Reel shows auto captions. The approval works:
episode 3's queue publishes every post on its day with no touch from him after the approval.

## Regent

**Stale Air becomes Drained.** Something left alone goes off. A token that lapses, an app left in development mode, or
a queue nobody reads after approval would each stall this without anyone noticing. The definition of done names who looks at what.

**Obligations.** Posting under his name and money are reserved (`reserved` in `council/faces.yaml`). His approval of each
queue is the act that publishes. Nothing goes out without it, and a change to an approved post sends it back for
approval. The token lives only in GitHub's secret store. The move's line "never publishes, schedules, uploads or posts
anything" gets one exception, written into `council/moves/podcast-episode.md`: approved queues publish through
`publish-queue.yml`.

**The Regent defines done for the build.** The dry-run test passes (a container reaches `FINISHED`). One live post publishes
and shows to a logged-out viewer. A forced failure opens a step. The Monday numbers land once.

## Diplomat

**Divergence, no changing lines.** The cast warns that going deeper and pushing forward at once cancel each other out. The build should
not also redesign the episode move. It takes the move as pass one left it and replaces only the posting.

**The bridge to guests.** A collaborator tag (`collaborators`) puts a Reel on a guest's profile once they accept. Isaac
was tag-only by his ruling (`pod1-isaac-handle`), and Tom has no accounts, so no guest is invited by default. The queue
carries a guest's handle only when he names it.

## Sage

**Serendipity becomes Fellowship.** The cast warns that the plan rests on one piece of evidence: Meta's own pages, read
today and not yet run against his accounts. The becoming says that he and the council are already walking the same way.
His ask was to set it up, and the plan sets it up in an order where the first step is also the first test.

**What each face gave.** The Shaman made the approval show each post whole. The Architect found that the existing
fifteen-minute timer and resumable upload remove any paid host. The Challenger set three tests and named the captions
collision. The Regent kept approval as the publishing act, kept the token in GitHub's secret store, and defined done. The
Diplomat kept the build from redesigning the move and left guests untagged by default.

**The pass was not unanimous.** The Challenger would wait for episode 2's sitting before building. The Sage records it and does not
resolve it: his ask was to set it up, and the setup steps take him under an hour, by the council's estimate. Building
alongside the sitting serves the gate in front of it (the Regent's lesson of 2026-10-03).

## Costs

| Item | Cost | Source |
|---|---|---|
| Meta developer account, app and API calls | $0 | Meta's pages above; the limits are 100 Instagram and 30 Page Reels a day |
| Video hosting | $0: GitHub release assets on the public council repo, sent to Meta by resumable upload | council design |
| The timer | $0: GitHub Actions is free on a public repo, as `board-pull.yml` runs now | |
| X, if added | about $0.20 a post with a link, so about $1 an episode for five posts, plus an unlisted media price | postproxy.dev, unchecked |
| Claude's build | one build thread, its cost named in its last report | CLAUDE.md, short sessions |
| Claude per episode | building the queue, measured on episode 3 rather than guessed | faces.yaml, no number inferred |
| His time | about 45 minutes once for setup, then a few minutes per episode to approve | council estimate, not his |

## Positions (stand unless he flips them)

- `pa-github-timer`: posts publish from a new GitHub Actions workflow on the council repo every fifteen minutes,
  beside `board-pull.yml`, with no paid scheduler and no paid host.
- `pa-approval-publishes`: his approval of an episode's queue on the board is the publishing act; nothing goes out
  without it, and a changed post goes back for approval.
- `pa-token-in-secrets`: the Meta token is a system user token he makes and pastes into GitHub's secret store; it never
  appears in chat, a step or a file.
- `pa-pilot-ep3`: episode 2 goes out through the sitting he picked; episode 3 is the first queue, after the dry-run
  test passes.
- `pa-numbers-auto`: once posting runs, the workflow reads each post's numbers every Monday, and his "note the
  numbers" step is retired.
- `pa-failure-step`: a post that fails to publish puts a step on his list within the hour, saying what failed.

## Question (passed the reach test)

`pa-x-api`, owner Challenger with the Regent: **Should X posts go out by the same timer?** The council recommends
keeping X by hand until the clips' numbers show X brings anyone.

- Keep X by hand (council lean: Challenger, Regent). It costs nothing, and you post on x.com or use its scheduler.
- Add X to the timer. It costs about $0.20 a post with a link, by postproxy.dev's figures, which is about $1 an episode,
  bought as X credits. The workflow posts X on the same day as Instagram.

Why only he can answer: it is money and posting under his name. Why not asked before: pass one kept X out of Meta
Business Suite, and nothing had priced X's API until today.

## Tests (dated)

- Before episode 3: one of episode 2's clips reaches a `FINISHED` container without being published.
- Episode 3's first Reel: it shows auto captions, and a logged-out viewer can see it.
- Episode 3: every queued post publishes on its day with no touch from him after the approval.
