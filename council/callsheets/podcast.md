2026-10-09
# Podcasts and outreach (MTGOA, Flirtcraft)

## Next
- 2026-10-16: Wendell answered `pa-x-api` = X by hand (council lean). The timer builds Instagram and the Page only; X is posted on x.com or its own schedule button in the same sitting.
- 2026-10-16, pass `podcast-pipeline2` (`council/passes/6FACE_PASS_podcast-pipeline2_2026-10-16.md`): BUILD BRIEF for the next thread. Build `.github/workflows/publish-queue.yml` + `podcast/publish/` script: every 15 min read approved `podcast/queue/<ep>.json`, publish due posts to Instagram (REELS container, resumable upload of the clip from a GitHub release asset `pod-epNN`, `cover_url` = raw.githubusercontent URL of the cover JPEG, `share_to_feed`) and the Page (`/video_reels` start/upload/finish), write post ids back, open a board step on failure (`pa-failure-step`), read insights on Mondays (`pa-numbers-auto`). Secret `META_TOKEN` (system user token, Wendell's steps `meta-publishing-setup` 01-03); IG user id and Page id come from the token via `/me/accounts`. Add the queue-approval board row shape (each post whole, covers as images) and the move's one exception line. Gate: dry run (container FINISHED, unpublished) before episode 3. Open: app must go Live, which needs a privacy policy URL (check masteringallyship.com / bars-engine; add a page if missing, then a step for him to paste it). Captions risk: API has no auto-captions switch; first live Reel checks it. X waits on `pa-x-api`. Waits on Wendell's three setup steps for the live parts; the workflow, queue format and dry-run harness can be built now.
- 2026-10-16: Wendell answered `pp-who-schedules` = sitting (Meta Business Suite) and let all six pp- positions stand. No MBS connector exists in Claude's directory and threads have no browser tools, so the sitting runs from a posting pack: Your steps `podcast-pipeline` 02 (check IG + FB Page in MBS) and 03 (schedule ep 2's five posts, pack with every caption in the step). ep 2 clip dates moved to 17/19/21/24/27 Oct. Claude scheduling via Meta's publishing API is a later build only if he asks (needs a Meta developer app, a token, public file hosting, and our own scheduler).
- 2026-10-16, pass `podcast-pipeline1` (`council/passes/6FACE_PASS_podcast-pipeline1_2026-10-16.md`): posting is the bottleneck. Waiting on `pp-who-schedules` (Metricool queue vs one computer sitting vs as now); episode 2's remaining clips are the pilot. Once he answers: for Metricool, suggest the connector and build the queue for ep 2; for the sitting, write a posting pack and one computer step. Zoom-to-Movies step is on `podcast-pipeline`. Tests: 2026-10-26 ep 2 fully out or scheduled; ep 3 at four touches or fewer.
- Ep 2 (Tom Hurlburt): Your steps `podcast-ep2-youtube` after `pod2-title`/`pod2-thumb-pick` (aging parents title and thumbnail A picked). Ep 2 clips post Oct 9, 12, 16, 19 (`podcast-ep2-clips`); captions carry `[episode link]`.
- Ep 1: Spotify link (step 5 of `podcast-spotify`) goes into flirtcraft `lib/podcast.ts` `embedUrl` and the Spotify `href`. Clips: `podcast-ep1-clips`, `flirtcraft-ep1-clips`; captions wait on `pod1-isaac-handle` and the link.
- Recut episode 1 longer per `pod-clip-length` (new thread).
- Clip covers follow `council/podcast/COVER_STANDARD.md` (safe box x 80-900, y 310-1500) in the render script and the Thumbnail Studio. Ep 1 (Isaac) covers re-rendered 2026-10-12 to `~/Downloads/podcast/ep01-clips/` (old ones in `old-covers/`); ep 2 and Flirtcraft ep 1 covers predate it.
- Outreach: Wendell sends invitations (Marina and Dustin Muñoz de Martínez, Adam, WMHCA gala counselors). Research-first group needs step 2 before pitching. Dated checks by 2026-10-15: a saved chase shows on the contact; weekday morning brief lists chases; board opens no slower on his phone.
- Vault needs the four fear-gold strings (GRAMMAR.md 12g) or decks.json regeneration brings excitement back.

## Waiting on
Wendell: `pod2-title`, `pod2-thumb-pick`, the Spotify link, `pod1-isaac-handle`. Not covered: finding relationship-coaching guests.

## Files
- `council/moves/podcast-episode.md`, `council/moves/podcast-outreach.md`, `council/ledger/2026-10-08-outreach-tab-build.json`
- MTGOA files `podcast/` (`outreach/invitations-2026-10-09.md`, `episode-marketing-plan.md`); `/mnt/project-files/podcast/`

- From the unfinished-work pass (2026-10-14, `uw-podcast-ticks`): tick what shipped in bars-engine `.specify/specs/mtgoa-podcast/tasks.md` (the hub shipped 2026-09-30 as `cc4d4f35f`) and mark the question and guest forms, and their models, as not built.

## Archive
HANDOFF.md: "Open on 2026-10-07, from the MTGOA podcast episode 2 thread (battle `fr-mtgoa-podcast-ep2`)"; "Open on 2026-10-06, from the Flirtcraft podcast thread (battle `fr-podcast-launch`)"; "Open on 2026-10-08, from the outreach-on-board pass" (twice); "Open on 2026-10-09, from the MTGOA podcast invitations thread"
