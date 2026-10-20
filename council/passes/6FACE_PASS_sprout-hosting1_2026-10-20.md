# Six faces, pass 1 on where sprout previews live (2026-10-20)

**Called by:** Wendell, in the thread for the Fixer spar (sprout #63), 2026-10-20 00:32 UTC.

**The question, in his words:** "yeah that makes sense now that you say it. I'm not quite ready for sprout to be
another vercel project, but that might be me being naive. Let's have the game masters weigh in on this for long-term
stability"

**Pass:** first on sprout hosting. It follows the Between hosting pass (`6FACE_PASS_between-hosting1_2026-10-17.md`),
which moved the Between off the artifact host and onto the web.

**Casts** (three coins, `cast.py --json`, kept in the ledger record):

| Face | Hexagram | Shows | Becomes |
|---|---|---|---|
| Shaman | 63 Arrived | This is finished, which is when it starts moving. | 5 |
| Architect | 52 Stillness | The move is to stop while the wanting is still running. | 15 |
| Challenger | 55 Fullness | This is at its peak and you are saving some of it. | 49 |
| Regent | 42 Windfall | More is arriving than you put in. | 25 |
| Diplomat | 61 Incubation | What is true here is still inside the shell. | 58 |
| Sage | 4 Fog | You are guessing where you could ask. | 46 |

No daemons were sent. The evidence is one worker's read of three repos and the Vercel team (below), and the record.

**Evidence, checked 2026-10-20:**

- sprout is a private repo with GitHub Pages off and no workflows. `tools/build-slice.mjs` writes `build/slice`, plain
  static files with relative imports and fetches; it needs an HTTP origin and nothing else. The script's own message
  says "static files, host them anywhere".
- Sprout previews have only ever run on his Mac: `council/callsheets/engine-slice.md` line 158, "the slice has no web
  host".
- The Vercel team "wendell's projects" holds seven projects (bars-engine, flirtcraft, friendcraft-manuacript,
  iching-quest, human-design-pwa, workspace, calrunian-fiction-dev). bars-engine previews have Vercel Authentication
  and password protection off, so they open on his phone. The team's plan was not readable from the connector.
- bars-engine already serves static game builds from `public/` (167 MB: oracle, card art, the Between, the inner
  garden) through rewrites in `next.config`. It uses `@vercel/blob` for uploads only; no route serves a build from Blob.
- The auto-mode safety check refused copying the 11 MB slice build into bars-engine `public/` twice.

## Scorecard

No earlier pass on this subject set tests. The Between hosting pass's own test (his iPhone opens the Between on
bars-engine) is outside this pass.

## Anchor

Every sprout pull request ships with one link he can tap on his phone and play (his standing rule, 2026-10-20:
"The more steps we add to test the less likely the test gets done"). Long term, Chapter 1's playable demo is what the
Kickstarter points at, and it is a sprout build.

## Shaman

**63 Arrived, becoming 5: you are ready and the ground is not.** The slice is built and playable; what is missing is
ground under it. The cast says not to read the waiting as failure.

**The felt read is his hesitation, and it deserves a hearing before a fix.** "I'm not quite ready" is a body signal,
and "might be me being naive" is him overriding it in the same breath. A second Vercel project can feel like the work
spreading out of the one place he trusts, bars-engine, where the WAVE, the caves and the Between already play.

**The Shaman leans toward keeping one home.** Option B (bars-engine serves sprout builds) keeps every playable game at
one address he already opens. The Shaman holds this lean lightly: it serves the feeling of one place, and a rewrite
gives that same feeling under option A.

## Architect

**52 Stillness, becoming 15: stop while the wanting is still running.** The pull is to build preview machinery. The
build is static, so the architecture question is small: which host gives a fresh link per pull request with the least
we maintain.

**scout: rung 3, a known tool does it.** Vercel's Git integration builds every pull request of a connected repo and
comments the preview link on it. Settings for sprout: framework "Other", build command `node tools/build-slice.mjs`,
output directory `build/slice`. Nothing is written in either repo.

**Option B is a hand-built copy of that tool (rung 5).** It needs a sprout workflow that builds each pull request and
uploads to Blob, a Blob token stored as a sprout secret, a bars-engine route that serves `/sprout/<pr>/...` with the
right content types, cleanup of old uploads, and a step that posts the link. Five parts we own, to reproduce what
Vercel does for free.

**One address either way.** A rewrite in bars-engine's `next.config` can send `bars-engine.vercel.app/chapter1/*` to
the sprout project's production URL, so the public demo lives under bars-engine's name whichever host builds it.

## Challenger

**55 Fullness, becoming 49: at the peak and saving some of it.** The council has the facts to settle most of this and
should not hold back a recommendation.

**Three options break.** Throwaway bars-engine preview branches put a second repo's 11 MB build into bars-engine's
history per pull request, run a full Next.js build to serve static files, leave branches to clean up, and were refused
twice by the safety check. GitHub Pages is off on a private repo, and Pages gives one site per repo, never one link per
pull request. Keeping it local breaks his one-link rule; that is how the Fixer spar got stuck.

**The fact that would organise the rest is unsaid.** He named the hesitation and not its cause. If it is cost or
account clutter, the record answers it: the team already has seven projects and a static build costs nothing to host.
If it is "one home for the game", the rewrite answers it. If it is something else, only he knows.

**Not checked:** the Vercel plan. If the team is on Hobby, Vercel's terms limit Hobby to non-commercial use, which
touches a Kickstarter demo whichever project hosts it, bars-engine included. That is a question for the Kickstarter
launch, flagged here and not asked.

## Regent

**42 Windfall, becoming 25: more is arriving than you put in.** Vercel already gives per-PR previews; the duty is to
take what is offered and stop paying for it by hand.

**The obligation is the web, not the bars-engine repo.** The Between hosting pass ruled on his words "This will
ultimately be hosted on the web" (`6FACE_PASS_between-hosting1_2026-10-17.md` line 142). bars-engine was the host
because the WAVE and the caves already worked there. The memory line "playable 3D spaces are hosted on
bars-engine.vercel.app; don't make Artifact pages game hosts" guards against the artifact host. A sprout project on the
same team, reached through bars-engine's address, keeps both halves.

**Authority:** adding a project to his Vercel team is his account, and he said he is not ready. That is his call, so it
goes to the board with a recommendation. **Done means** the first sprout pull request after his answer carries one link
that opens on his iPhone.

## Diplomat

**61 Incubation, becoming 58: the truth is still inside the shell.** The play is built and nobody can reach it yet. The exchange he
wants is the link itself.

**The link has to land where he already looks.** Under option A the Vercel bot comments the link on each sprout pull
request with no step from anyone, and the thread passes it on. Under option B a thread has to post it each time.

**One trap to close under option A.** New Vercel projects usually start with Vercel Authentication on for previews,
which would put a sign-in wall in front of him on his phone. bars-engine has it off. The new project should match, and
the first link gets opened in a phone-width browser that is not signed in before it reaches him.

## Verdicts

| Face | Throwaway bars-engine branches | GitHub Pages | Recommended host | Who decides |
|---|---|---|---|---|
| Shaman | no | no | B, held lightly | him |
| Architect | no | no | A | him |
| Challenger | no | no | A | him |
| Regent | no | no | A | him |
| Diplomat | no | no | A | him |
| Sage | no | no | A | him |

## Dissent check

Not unanimous. The Shaman leans to option B for the feeling of one home; the other faces recommend A and answer that
feeling with the bars-engine rewrite. All six agree that the throwaway-branch and Pages options are out, and that the
host is his call.

## Sage

**4 Fog, becoming 46: you are guessing where you could ask.** The council could guess why he is not ready. It should
ask instead, once, on the board, with the steer box open.

**What each face gave.** The Shaman named the hesitation as real and found the pull toward one home. The Architect
named the tool (Vercel's Git integration, rung 3) and showed B as a hand-built copy of it. The Challenger closed three
options and marked the unsaid cause. The Regent read the 10-17 ruling as "the web", not "the bars-engine repo". The
Diplomat placed the link and caught the sign-in wall. Nothing was dropped.

**The smallest whole:** sprout becomes its own Vercel project with previews open, and bars-engine rewrites a public
path to it for the demo. The Sage recommends it and does not decide it.

## Outputs

### Positions (stand unless he flips them)

- **sh-no-bars-branches:** No throwaway bars-engine branches carry sprout builds. Why: a second repo's build in
  bars-engine's history per pull request, a full Next.js build to serve static files, and two safety-check refusals.
- **sh-no-pages:** GitHub Pages is not the sprout host. Why: sprout is private with Pages off, and Pages gives one site
  per repo, never a link per pull request.
- **sh-web-not-repo:** The 10-17 hosting ruling means "on the web", and bars-engine's address is the public face. Why:
  the Between pass rests on his words "This will ultimately be hosted on the web" (line 142); bars-engine was chosen
  because the WAVE and caves worked there.
- **sh-demo-on-bars:** Chapter 1's public demo is reached at a bars-engine.vercel.app path whichever host builds it. Why:
  a `next.config` rewrite to another origin does it without copying files, and it keeps the Kickstarter link at the
  address the other games use.

### Question (passed the reach test)

- **sh-sprout-host** (owner: Regent). Where do sprout's per-pull-request previews live? Options: A. sprout as its own
  Vercel project on the same team (recommended); B. bars-engine serves sprout builds from Blob; C. keep previews on his
  Mac for now. Why only he can answer: he said he is not ready for another Vercel project, it is his account, and the
  record holds no reason for the hesitation. Why not asked before: sprout has had no web host since it started; the gap
  showed only when the Fixer spar needed a link.

## Tests (set 2026-10-20)

- **T1, by 2026-10-27:** the first sprout pull request after his answer carries one link that opens and plays on his
  iPhone, checked first in a phone-width browser that is not signed in to Vercel.
- **T2, at the next three sprout pull requests:** no sprout preview needs a change in bars-engine (option A) or a hand
  post of the link (option B, where it counts the posts).

## What this pass did not check

The Vercel plan and whether the team has a Blob store. Whether the built slice is 11 MB was taken from the
coordinator's note; the worker measured the source folders (slice 148 KB, traveler art 9.0 MB), not the build.
