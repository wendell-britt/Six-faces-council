# The podcast pipeline

The canonical way the six faces run any of Wendell's shows: Mastering the Game of Allyship (MTGOA), Flirtcraft and
Friendcraft. Wendell, 2026-10-21 (step `ttv-cmviclyuf0004`): "we want to make sure we have a canonical Podcast
pipeline that the 6 game masters know how to use and administrate". Board row `fcp-pipeline` (stands): the sister
shows run one pipeline, and only two steps belong to Friendcraft alone.

This file is the map. The detail lives in the files it names; change the detail there and keep this in step.

## What Wendell does and what the faces do

Wendell records, uploads, posts under his name, and picks. The faces draft, render, cut, queue and keep the books.
Nothing is published, scheduled, uploaded or sent to a guest by a session (reserved: anything that names a person,
consent and release, money). The one exception is a queue he approves on the board, which a timer publishes
(`pa-approval-publishes`). Every question for him goes through the reach test and onto the board, never into chat.

## The shows

| Show | Look | Host and feed | Notes |
|---|---|---|---|
| MTGOA | night violet, pink-to-gold, hexagon controller logo | Wendell's feed | the book's show; guests are allies, practitioners |
| Flirtcraft | same look, flirt red | Spotify for Creators, RSS to Apple (`pod-host`) | callsheet `flirtcraft.md` |
| Friendcraft | same look, friendcraft.app teal `#5fc2ba` | Spotify for Creators, RSS to Apple, video to YouTube (`fcp-host`) | cover B "Two friends" picked 2026-10-21 (`fcp-cover-pick`); two episode kinds alternating (`fcp-episode-shape`); crew in `THE_CREW.md` first as guests (`fcp-first-guests`); no release forms, a logged yes on the record is the release (`fcp-consent-on-record`) |

## The stages, in order

1. **Before recording: guest and shape.** Guests come from the Outreach tab of the board; Wendell sends every
   invitation (`podcast-outreach` move, `council/moves/podcast-outreach.md`). Friendcraft: the two episode kinds
   alternate, and the guest and Wendell agree before the call what they will make. The Diplomat owns the guest list
   and the Regent owns the consent line.
2. **Record.** Wendell, on Zoom. A Zoom VTT carries the speaker on each cue. Claude's cloud sessions cannot open
   zoom.us (`pod-zoom-phone`), so the transcript and video reach the thread from him. At the end of the episode he
   asks on the record whether there is anything the guest wants out (Friendcraft; a good habit for all three).
3. **The episode move, seven steps** (`council/moves/podcast-episode.md`): read the recording; draft title options,
   YouTube description with chapters and a two-line Spotify and Apple description; render thumbnails
   (`render_thumbnails.mjs`); put the title and thumbnail picks on the board and the description as a standing
   position; write his upload steps; pick and cut the clips (`cut_clips.sh`) with covers
   (`render_reel_covers.mjs`, `COVER_STANDARD.md`); mine the recording into BARs (`game-masters-guide`
   `corpus/`, rows as positions that stand).
4. **Posting.** Per episode, the posts go out on the marketing rhythm: the episode on day 0, a clip on days 2, 5 and
   9 (`episode-marketing-plan.md`). Two routes. The sitting: one computer session in Meta Business Suite from a
   posting pack (`ep02-posting-pack.md` is the pattern), X by hand (`pp-who-schedules`, `pa-x-api`). The queue: the
   session writes `council/podcast/queue/<episode>.json` and an approval row; his approve publishes Instagram and the
   Page on the timer (`council/podcast/publish/README.md`). Ep 3 of MTGOA is the first queue. The third route, Claude on his Desktop driving Meta Business Suite with his go on each post, is the one in use now (`council/podcast/desktop-posting.md`).
5. **Day-9 numbers.** Nine days after clip 1, each clip's views, saves and shares are read from the platforms' insights
   and noted in `council/callsheets/podcast.md` (Wendell, 2026-10-21, `podcast-ep1-clips-05`: "This is part of the now
   automated podcast pipeline"). Queue route: `publish.py numbers` already writes them into the queue file every Monday
   once `META_TOKEN` is set. Desktop route: the thread hands Claude on his Mac a read-only task (open Business Suite
   Insights, read each clip's numbers, change nothing, post nothing) and files what it reports. X numbers are read by
   hand on x.com. The thread that finishes an episode schedules this read for day 9; the one that reads it compares the
   clips (the marketing plan's test is whether a clip beats the episode link's reach). Ep 1 clips are the first read.
6. **Close.** Tick the episode's Your steps, put leftovers in `council/callsheets/podcast.md`, and record each of his
   answers the way a board answer is recorded.

## Friendcraft's two extra steps

- **Harvest.** After mining BARs, sort the guest's and Wendell's material into the friendcraft manuscript's six
  extract buckets (the manuscript repo's `podcast/PIPELINE.md` names them).
- **The guest checks each quote.** Before a quote enters the manuscript the guest sees it in context
  (`fcp-consent-on-record`; the manuscript's `podcast/CONSENT_AND_RELEASE.md`). Quote only what the recording holds.

## Who owns what

| Face | Owns in the pipeline |
|---|---|
| Shaman | the look: covers, thumbnails, titles that carry the hook |
| Architect | this file, the scripts, the queue and its schema, the Spotify/Apple/YouTube setup |
| Challenger | the check before it goes out: lengths, safe box, placeholders, claims about guests |
| Regent | consent and release, money, the reserved list |
| Diplomat | guests, invitations, outreach tab, the crew |
| Sage | the reach test, the BAR mine, what goes to the board |

## Running and administering it

- **Start an episode:** a thread reads this file, `council/moves/podcast-episode.md` and `council/callsheets/podcast.md`,
  pulls the board (`python3 board/pull.py <dir> --push`), and runs stage 3 from the transcript.
- **Gates that must pass before anything reaches him:** `python3 council/tools/voice_lint.py` on his reading; a
  thumbnail readable at phone size; covers inside the safe box (the renderer fails if not); `publish.py check` on a
  queue; no bracketed placeholder left in a caption.
- **Covers:** the Thumbnail Studio (https://claude.ai/artifact/RAiZ3keBiE6BvDD6YKA9S8) carries each show's thumbnail and
  clip-cover look (Friendcraft: Two friends). Clip covers follow `COVER_STANDARD.md`.
- **Changing the pipeline:** a stage Wendell rules on changes here and in the move file in one pull request, with the
  ruling quoted. `council/faces.yaml` changes only by his ruling.

## Open

- Friendcraft's square show cover file (3000 by 3000) for Spotify is not yet drawn in the Two friends look.
- Friendcraft's episode 1 has no guest yet (`fcp-first-guests` open); ep 1 needs its own `fcp-` rows once recorded.
- Meta publishing still waits on his `meta-publishing-setup` steps (publish README).
