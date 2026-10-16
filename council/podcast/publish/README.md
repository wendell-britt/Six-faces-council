# Publishing podcast posts through Meta's API

Pass `podcast-pipeline2` (`council/passes/6FACE_PASS_podcast-pipeline2_2026-10-16.md`). Claude prepares each episode's
posts as a queue. Wendell approves the whole queue once on the board, and a timer publishes each post on its day to
Instagram and the Facebook Page. Episode 2 goes out through the sitting he picked; episode 3 is the first queue
(`pa-pilot-ep3`).

## Queue, script and timer

- `council/podcast/queue/<episode>.json` holds the posts, in the shape of `schema/publish-queue.schema.json`: each
  post's time (with an offset), kind (`reel` or `image`), networks, one caption per network, the clip (an asset of the
  release `pod-<episode>` on this repo) and the cover JPEG (in `council/podcast/queue/covers/<episode>/`).
- `publish.py` does the work. `check` and `plan` need no token and no network; `run`, `numbers`, `accounts` and
  `container-test` read `META_TOKEN`.
- `.github/workflows/publish-queue.yml` runs `publish.py run` every fifteen minutes and `numbers` on Mondays, commits
  the post ids back into the queue, and opens an issue assigned to Wendell for a post that fails or misses its window.
  With no `META_TOKEN` it runs only `plan`.

## How a session prepares an episode's queue

1. Cut the clips and render the covers as the podcast move says (`council/moves/podcast-episode.md`). Covers must be
   JPEG, 9:16, 8 MB or less.
2. Upload the clips as assets of a release on this repo: `gh release create pod-ep03 <clips> --title "Episode 3 clips"`.
   The repo is public, so the clips are public from then on. Keep guests' family and health details out of them.
3. Commit the covers to `council/podcast/queue/covers/<episode>/` and write `council/podcast/queue/<episode>.json`.
   Fill every `[episode link]` before approval; `check` refuses a caption that still holds a bracketed placeholder.
4. `python3 council/podcast/publish/publish.py check`, then `plan --now <a time after the first post>` to see every
   call a live run would make.
5. `python3 council/podcast/publish/publish.py approval-row council/podcast/queue/<episode>.json --write` puts the
   approval question on the board with every post shown whole. Land it on main, rebuild and republish the board.

The covers must be on main before he approves, or the board shows broken images and Meta cannot fetch them.

## Approval

A queue publishes only when its `approval_row` is answered `approve` and the row's `queue_sha` equals the queue's hash
now (`pa-approval-publishes`). The hash covers `episode` and `posts`, so editing any post after approval stops the
whole queue until a new row (`pq-<episode>-2`) is approved. `state` and `numbers` are the workflow's and do not change
the hash.

## What the timer will not do

- Post twice. It saves the queue just before each publishing call. A run that fails at that call, or dies there, is
  marked failed and never retried, because the post may have gone out. Failures before that call (container,
  upload) retry up to three times, then open an issue.
- Post late. A post more than six hours past its time is marked missed and opens an issue.
- Print the token. `plan` shows `access_token=***`.

## The gate before episode 3

After Wendell's setup steps (`meta-publishing-setup` 01 to 03 on Your steps): run the workflow by hand with mode
`accounts`, which names the Page and the Instagram account the token reaches. Then upload one of episode 2's clips
to a release (`pod-ep02`), commit its cover, and run mode `container-test` with
`clip = release:pod-ep02/<clip>.mp4` and `cover = <repo path>`. It passes when the container reaches `FINISHED`. It is
never published and expires after 24 hours.

## Open

- The app must be switched to Live, which needs a privacy policy URL. Whether masteringallyship.com or bars-engine
  has one was not checked from this container (its network does not reach either site).
- Instagram's auto captions: the API has no switch for them (`pod-clip-no-words`). The first live Reel checks whether
  they appear.
- `pa-failure-step` asks for a step on his Your steps list. The steps live in the board's store, which a GitHub
  workflow cannot write, so the timer opens a GitHub issue assigned to him instead (GitHub emails him). The next
  board read can turn an open issue into a step.
- The Graph API version defaults to `v24.0`; set the repo variable `META_GRAPH_VERSION` if Meta has retired it.
- X waits on `pa-x-api`.
