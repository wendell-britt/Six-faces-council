# Handoff

The council works in short sessions (Wendell, 2026-10-03, board read 29). A session does one piece of work, records it
in the repo and on the board, writes anything left open here, and ends. The next session starts by reading
CLAUDE.md, this file and the board.

## Open on 2026-10-03, when session_01BME8oqWjhm69ar2KZPiSDm handed off

- **The board** (https://claude.ai/artifact/DxyShVS8tmvJym4HAsgnho) waits on Wendell for: `dy-model`,
  `dy-limit-wording` (#20), `dy-research-handoff`, `dy-2026-10-03-wake` (#21), `cost-quiet-wakes`,
  `cost-daily-script`, `cost-per-row`, `cost-short-rule` (#24). `cost-jev` is retired: Jev is TypeSafe's Jev, and another session's `jev-` rows and
  its trial spec (`jev-spec-first`, bars-engine) carry that work. Wendell named Jev beside short sessions as a way to
  save tokens; once the trial reports, the short-sessions rule can say where Jev takes judging work off the large model. Read the store for answers saved
  after 2026-10-03T22:40Z, record them in a ledger record, and republish.
- **Pull requests:** #20, #21 and #24 wait only on Wendell's ruling and the steward. Merge none; add the
  `automerge` label only when he says to merge.
- **The daily session:** routine `trig_01F8fDdkjYEeMCfdozj6w3tt` wakes the standing session
  `session_011mcRZ4vDnnis99dnptvdmu` at 15:45 UTC. 2026-10-04 is the first scheduled wake; check whether it reached
  the standing session (a hand-fired run started a fresh session instead). Record each run's cost from its result
  event with `council/daily.py usage`, never from get_session mid-turn.
- **Your steps tab:** research sites (`council-research-network`), the flirtcraft database, and the branch retire
  command are unticked.
- **Deferred:** the oracle drafts come back 2026-11-03 (`council/due.py`).
- **Costs measured so far:** pass ten, `council/passes/6FACE_PASS10_2026-10-03.md`.

## Open on 2026-10-05, from the standing daily session

- **The standing session is past the short-sessions limit.** `session_011mcRZ4vDnnis99dnptvdmu` read 331,329 tokens
  of context at the start of today's run (get_session, 15:46 UTC). CLAUDE.md now says to hand off before about
  200,000. Wendell chose one standing session (`dy-access`, board read 28) because a fresh routine session had no
  repo access; the short-sessions rule came later. A board read should weigh the two: the routine could fire a
  fresh session once the repo is attached to it, or the standing session could be replaced by a new one.
  Nothing has been changed; the routine still wakes this session.

## Open on 2026-10-06, from the Friendcraft next-steps thread (friendcraft pass 8)

- **Three pieces of work, each its own thread.** Wendell's board answers (friendcraft
  `council/ledger/2026-10-06-friendcraft-manuacript-pass8-board-read.json`) set them:
  `fcm-p8b-redesign` (Friendcraft's design pass: work like flirtcraft, BARs for friendship development, rethink the
  basic moves with emotional alchemy; start with a six-face pass), `fcm-p8b-interview` (the council interviews him
  about his own stories for Part 0, one story per thread), and `fcm-p8b-outline` (re-derive the book outline from
  `canon/` as a proposal). They stand unless he flips them on the board.
- **Waiting on him:** `fcm-p8b-exchange-where` (today's exchange at flirtcraft.app/friend now, wait for the
  redesign, or its own address).
- **Lessons pending** for the Challenger and the Shaman are in that ledger record, for `collect_lessons.py`.
- friendcraft-manuacript #28 holds the pass, the ledger records and the decision-log entry (rulings 14 and 39
  closed).

## Open on 2026-10-07, from the MTGOA podcast episode 2 thread (battle `fr-mtgoa-podcast-ep2`)

- **The podcast episode move** merged in #47: `council/moves/podcast-episode.md` and
  `council/podcast/render_thumbnails.mjs`. Every episode of either show runs it.
- **Episode 2 with Tom Hurlburt** waits on `pod2-title` and `pod2-thumb-pick`. The copy and the drafts are in the MTGOA
  project files under `podcast/ep02-tom-hurlburt/`. If he picks "Put us in it", redraw his pick with a still from the
  video as `photo` in `spec.json`. Then Your steps list `podcast-ep2-youtube` takes it to YouTube.
- **Picked (board read of 2026-10-07):** the aging parents title and thumbnail A; the description stands.
- **Episode marketing** (2026-10-07): the plan is in the MTGOA project files at `podcast/episode-marketing-plan.md`
  and the move's new step 6. Episode 1's three clips (Isaac Holze) were recut on 2026-10-07 to 50, 70 and 52
  seconds with no words on screen (`pod-clip-no-words`) and sit in `~/Downloads/podcast/ep01-clips/` on Wendell's
  Mac under the old names, with `captions.md`; the short versions are in `_claude_work/ep01-clips-short/`. The same
  captions are in
  `podcast/ep01-isaac-holze/clips-and-captions.md`. Your steps list `podcast-ep1-clips` posts them. Waiting on
  `pod1-isaac-handle`. Episode 2's clips need step 6 once it is on YouTube; `Downloads/02-how-would-you-like-to-feel.mp4`
  (53 s) looks like one already cut.
- **Episode 2 clips** (2026-10-07): moments are in `/mnt/project-files/podcast/ep02-tom-hurlburt/clip-moments.md`, and board question `pod2-clip-moments` recommends A, B, C, D. Next thread: read his answer, cut the picks from `~/Downloads/GMT20260925-170846_Recording_640x360.mp4` per step 6 of the podcast move (9:16, words on screen, chapters stripped), write `clips-and-captions.md`, and make a Your steps list on the day 0/2/5/9 rhythm. The move doc still says "10 to 60 seconds"; bring it in line with `pod-clip-length`. The episode's YouTube link is not on record yet.
- **Clip length** (2026-10-07): `pod-clip-length` stands unless flipped: one or two clips of 60 to 90 seconds per
  episode, one or two of 30 to 60, none under 30. Research in the MTGOA project files at
  `podcast/reels-research-2026-10-07.md`. Next, in a new thread: recut episode 1 longer from
  `~/Downloads/GMT20260916-192430_Recording_640x360.mp4` (only 640x360; ask whether a full-size recording exists)
  and its VTT, with moments proposed on the board per step 6 of the move. Clip 1 is due to post on 2026-10-08.
- **Leftover on his Mac:** `~/Downloads/podcast/_claude_work/` holds four wav files and a png from finding the clips.
  Deleting needs his permission in a session; he can bin the folder himself.

## Open on 2026-10-06, from the Flirtcraft podcast thread (battle `fr-podcast-launch`)

- **Podcast page:** flirtcraft #9 merged (b5284f5). The player and the Listen on Spotify button go in by setting
  `embedUrl` and the Spotify `href` in flirtcraft `lib/podcast.ts` once Wendell pastes the episode link (step 5 of
  Your steps list `podcast-spotify`).
- **Episode 1 copy (done 2026-10-07):** show description, title and notes are in `/mnt/project-files/podcast/episode-1.md`;
  Wendell uploaded and published the episode (step 4 ticked). Step 5, the Spotify link, is still open. The
  Podcast Thumbnail Studio is at https://claude.ai/artifact/RAiZ3keBiE6BvDD6YKA9S8 (`pod-thumb-studio`).
- **Book harvest (2026-10-07, battle `fr-book` round 2):** flirtcraft #12 (draft) adds `book/podcast/episode-01.md`
  (20 ideas, conflicts with the app) and `book/podcast/README.md` (the recipe for the next episode). Questions
  `book-golds-satisfactions` and `book-permission-remedy` wait on Wendell; `fc-fear-rung-wonder` is a small decks.json
  fix to build once it stands. Mark #12 ready once he has seen it; it merges by itself after that.
- **Cover art (done):** Wendell picked cover B, Two signals, at 20:02 on 2026-10-06, in the flirt red (#ff5a5f to
  #d4003a) his `pod-art-ma` steer asked for. The final file is `/mnt/project-files/podcast/covers/flirtcraft-podcast-cover.jpg`
  (3000x3000), and step 4 of Your steps list `podcast-spotify` names it. The other drafts, `covers.html` and
  `render.js` stay beside it; the first versions in Mastering Allyship's colors are in `covers/v1-mastering-allyship-colors/`.
- **Board pickup (`board-auto-pickup`):** built on 2026-10-06; docs/pickup.md has how it works. The board's Send to
  Claude button fires routine `trig_01DpRsDM94Cnv2neyDVkBNMb`, which wakes the coordinator to start a board-read
  thread; its first firing did, at 20:01 UTC. The daily routine has step 1b, the safety net. Open: the routine
  names the coordinator's session, so when the coordinator is replaced, check it still arrives.

## Open on 2026-10-06, from board read 2002

- **WAVE battle (`fr-demo` round 7):** Wendell overruled `wave-acknowledge` and asked for research: the battle must
  feel turn based, and the system should generate a spirit that matches the charge the player is feeling.
  `wave-ack-research` stands; the WAVE thread does the research and brings Acknowledge back as a new position.
  `wave-offered-feeling` and `wave-integrate-ladder` stood. Lesson pending for the Architect in
  `council/ledger/2026-10-06-board-read-2002.json`.
  Done 2026-10-06 (round 8, `council/ledger/2026-10-06-demo-round8-research.json`, research in
  `/mnt/project-files/demo/wave-acknowledge-research.md`): positions `wave-spirit-from-charge` and
  `wave-acknowledge-turn` are on the board and stand unless he flips them. Then the WAVE build goes on sprout #24's
  branch: Welcome asks feeling and strength, then the urge; the daemon's next push is shown; Acknowledge always lands,
  with an extra turn when it catches a wind-up.
  Round 9 (`council/ledger/2026-10-06-demo-round9.json`): `wave-spirit-from-charge` stood, `wave-acknowledge-turn`
  was overruled for Root's trigrams. New positions `wave-trigram-moves`, `wave-welcome-listen` and
  `wave-seize-validate` stand unless he flips them; the build then takes Root's rules from sprout
  `root-fight/index.html`. All three stood at board read 2038 (ef6c341), so the WAVE build can start in a new
  thread on sprout #24's branch.
  Round 10 (`council/ledger/2026-10-06-demo-round10-build.json`): the WAVE battle is built in sprout #26 (sprout #24
  had merged, so it is a new branch, `claude/project-thread-eb8lu4`). Rules in `slice/wave.js`, tests in
  `npm run test:wave`. The build's own choices are positions `wave-offer-opens`, `wave-exhale-ends`, `wave-urges-all`
  and `wave-welcome-cost`, standing unless he flips them. Next: his playtest of `?road`; Welcome's cost against
  carried HP is the first balance check.

## Open on 2026-10-06, from the board pickup thread

- **Send works again** (2026-10-06 23:24 UTC, on Wendell's word in chat): the board declares `db` and `mcp`
  (Claude Code Remote, `fire_trigger`). Republish without `capabilities` so the grant carries forward.
  `PICKUP_TRIGGER` is `trig_01L138vKTaN9MSJoFKRmaBNx`, which wakes the council project's coordinator.
- **Closed 2026-10-07:** the fresh-session routine `trig_01Q9mMcVwR4MCqHQzUHwcmiS` is switched off and the pickup
  moved to pull (see "from the pickup hostile review" below). No repo needs attaching and no id needs swapping.
- **Work the answers begin:** `wave-acknowledge-turn` overruled (steer: a trigram move is the acknowledgement,
  welcoming is listening) for the WAVE thread; `oag-faces-names` chose plain words, steer: a popup page per face,
  for the ontology game thread.

## Open on 2026-10-06, from the Flirtcraft loop audit thread (battle `fr-orient-new-players`)

- **The pass:** flirtcraft `6FACE_PASS3_2026-10-06.md` and `council/ledger/2026-10-06-loop-pass1.json`, merged in
  flirtcraft #10 (2026-10-07). Board read 2349 recorded every row: all seven positions stood, both questions took A.
  The audit thread is closed; the build below is a new thread. The readable page is https://claude.ai/artifact/1QydwJABFethDKW34vwBsR.
- **On the board:** seven positions (`loop-fix-labels`, `loop-draw-means-drawn`, `loop-one-move`, `loop-posture-once`,
  `orient-bridge`, `orient-on-your-own`, `orient-reflection-to-wall`) stand unless he flips them; two questions wait on
  him (`orient-first-paid-run`, `orient-terms`).
- **Next, once they stand:** one flirtcraft pull request for the fixes (rail labels, draw first, 16 internal cards,
  one named move, posture once); `orient-bridge` starts the pipeline with a spec kit inside flirtcraft. It is not tied
  to the sprout demo: Wendell ruled in chat, "The wave battle thread really shouldn't be in this project"
  (flirtcraft `council/ledger/2026-10-06-loop-pass1-ruling.json`, Regent lesson pending). Test 1 (a cold reader names
  their one move at the commit screen) runs with the next stranger who plays flirtcraft.
- **Not started:** the book outline Wendell named after the audit. It is its own thread.

## Open on 2026-10-06, from board read 2330

- **WAVE battle (`fr-demo` round 10):** `wave-offer-opens`, `wave-urges-all` and `wave-welcome-cost` stood.
  `wave-exhale-ends` was overruled with a steer: an Exhale can end a fight as a coup de grace, or offer an "express"
  move, a way to express the emotional energy being worked with. The WAVE thread reworks Exhale in sprout #26
  (`slice/wave.js`) and brings it back as a new position. Lessons pending for the Challenger and the Regent in
  `council/ledger/2026-10-06-board-read-2330.json`.
- **Morning brief to the board:** Wendell's context note, 23:26 UTC: "I want to make sure the work from the morning
  brief is coming into the council board as well". Nothing in the three repos names a morning brief, so the next
  session that takes this finds where that brief is produced and routes its items to the board through the reach test.

## Open on 2026-10-06, from the Flirtcraft book outline thread (battle `fr-book`)

- **Outline drafted:** flirtcraft `book/OUTLINE.md` (flirtcraft #11, docs only, marked ready), page
  https://claude.ai/artifact/Gojd8ok8fbtDqcJoysmwCr. Seven parts, twenty-seven chapters, built on one rep, crafts in
  the order of service. Drafted from the record, not a full six-face pass. Prose stays Wendell's.
- **On the board:** question `book-oracle-in-print` waits on him; positions `book-spine-one-rep`,
  `book-crafts-service-order`, `book-binds-after-crafts`, `book-part-zero-stories` and `book-plain-first` stand
  unless he flips them.
- **Next, each its own thread:** the Part 0 interview (one story per thread, as `fcm-p8b-interview`), once he
  answers or lets the positions stand.
- **For the app, not the book:** GRAMMAR.md §12g renamed fear's gold to wonder; `lib/decks.json` still says
  excitement in both fear cultivate rungs.

## Open on 2026-10-06, from the WAVE teaching pass (`fr-demo` round 11)

- **On the board:** question `wave-teacher` (A Master Yun recommended, B Captain Rue, C Cael) waits on Wendell;
  positions `wave-taught-fight`, `wave-straight-first`, `wave-corners-from-spirits`, `wave-gates-in-the-world`
  (a story draft, Proposed) and `wave-buttons-image-first` stand unless he flips them. Pass:
  `/mnt/project-files/demo/wave-teaching-pass.md`; ledger `council/ledger/2026-10-06-demo-round11-pass.json`.
- **Next:** after the read, the WAVE build on sprout #25 (draft) adds the taught fight, the gate ladder, the corner
  unlocks and the image-first buttons, then reruns the bot test with the straight four only. Sprout #26 is closed.
- **Round 12 (chat steer, 2026-10-07 00:00):** `wave-buttons-image-first` overruled ("translate work so that the moves
  mean something to America players"). Positions `wave-move-names` (Sky Lift, Earth Yield, River Fill, Flame Follow,
  Wind Draw, Lake Gather, Thunder Split, Mountain Stand) and `wave-qi-made-visible` (neigong turned outward, bending
  feel) stand unless he flips them. Ledger `council/ledger/2026-10-07-demo-round12-chat.json`.
- **Rounds 11 and 12 read (2026-10-07 01:07):** all seven positions stood and `wave-teacher` is A, Master Yun
  (`council/ledger/2026-10-07-board-read-0107.json`). Nothing in fr-demo waits on Wendell. Next, in a new thread: the
  WAVE build on sprout #25 with Yun's taught fight, the straight four first, corner unlocks from spirits, the English
  move names and visible qi; the trigram lore goes into design.md as Proposed.

## Open on 2026-10-07, from the board read rerun (board read 2349)

- **Recorded:** the fifteen saves of 2026-10-06 23:47 to 23:49 that the lost Send left (fr-orient-new-players: two
  questions, seven positions; fr-book: one question, five positions), all on the recommended options
  (`council/ledger/2026-10-07-board-read-2349.json`). Next for the book: the Part 0 interview, one story per thread.
  Next for orient: the first paid run shows all seven screens, terms as subtitles under a plain sentence.
- **Pickup routine:** the coordinator was asked to update its prompt so a fresh session never calls `add_repo`
  (docs/pickup.md, "The lost Send"). Check with `get_trigger trig_01L138vKTaN9MSJoFKRmaBNx` that the prompt carries
  that paragraph. Waiting on Wendell: a line in the project instructions pre-authorizing the board read thread.

## Open on 2026-10-07, from the pickup hostile review

- **Pull is built** (six-faces-council #46): `board/pull.py <store folder> --push` records every save main lacks and
  is safe to run twice. CLAUDE.md, the session-start hook and the skill point every session at it. Run against the
  store after board read 1714, it found nothing new, so it agrees with what that read recorded.
- **Dropped from the review's plan, on purpose:** the claim with an expiry. Two pulls at once write the same resolved
  entries and the same ledger file, so there is nothing to lock. The separate alarm is also dropped: the daily run
  now records saves itself, so a broken Send chain no longer takes the safety net with it.
- **Switched off:** `trig_01DpRsDM94Cnv2neyDVkBNMb` and `trig_01Q9mMcVwR4MCqHQzUHwcmiS` (17:17 UTC).
- **Waiting on the sessions that own the prompts:** the coordinator was sent the new prompt for
  `trig_01L138vKTaN9MSJoFKRmaBNx` (pull, then act; never add_repo), and the standing daily session the new step 1b
  for `trig_01F8fDdkjYEeMCfdozj6w3tt` (run pull.py, do not fire the pickup routine). Check both with `get_trigger`.
- **Small bug seen at board read 1714:** the 17:12 Send fired the routine but did not rewrite `pickup/last` (it still
  held the 00:45 rows), so the Send bar may not hide. Under pull nothing depends on that doc.

## Open on 2026-10-07, from the process improvement thread (pass 13)

- **Pass 13** (`council/passes/6FACE_PASS13_2026-10-07.md`) asked how to use the process to improve the process. Its
  answer is a retro pass: the six faces read the council's own record (overrules, steers, deferrals, incidents,
  unfolded lessons) on the daily session's Grow up day. Positions `proc-retro-pass`, `proc-first-retro-by-hand`,
  `proc-fold-lessons`, `proc-record-face` and `proc-scorecard-always` stand unless he flips them; `proc-rule-retire`
  went to him.
- **Read at 18:15 UTC:** all five positions stood and `proc-rule-retire` was answered A (retire as a position, rule
  moves to an incident log). `retro` in `council/pipeline.yaml` holds the rules. `proc-record-face` is done: pull.py
  copies faces and pass onto resolved entries, and every existing resolved row that still has its row was backfilled.
  The overrules by face, counting each face on a row: Challenger 17, Architect 15, Shaman 11, Regent 9, Diplomat 6,
  Sage 4.
- **Next:** the first retro runs by hand in its own thread, on the 32 overrules, the 9
  pending lessons and the 6 pickup incidents.

## Open on 2026-10-07, from retro 1

- **Retro 1** (`council/passes/6FACE_RETRO1_2026-10-07.md`, ledger `council/ledger/2026-10-07-retro1.json`) found three
  repeating patterns in the 32 overrules: the Architect's designs not playing like the game he named (or missing the
  answer already in his own work), one-to-one rules where he wanted a shared frame with variety inside, and gates in
  front of design work. The third recurred after its lessons were folded on 2026-10-03. The retro rhythm holds.
- **On the board, standing unless he flips them:** `retro1-rhythm-holds`, `lesson-architect-sources`,
  `lesson-challenger-shared-frame`, `lesson-challenger-gate-release`, `lesson-regent-purpose-first`,
  `lesson-diplomat-plain-names`, `lesson-sage-evidence-readings`, `retro1-lessons-closed`,
  `retro1-retire-pickup-history`. **Next:** the board read after he answers folds each standing lesson into
  `faces.yaml` (his ruling is the board answer), with his quoted words and the source rows.
- **Not reached:** `collect_lessons.py` could not read friendcraft-manuacript, flirtcraft, root-game or
  emotional-first-aid from that session (GitHub 403 through the proxy). Their pending lessons (friendcraft Challenger
  and Shaman, flirtcraft Regent) wait for a session that can read those repos. The script now names unread repos.
- **Retired:** the push design's history moved from `docs/pickup.md` to `docs/incidents.md`. The four rule files are at
  588 lines; retro 1's test 4 holds them there.

## Open on 2026-10-07, from the texts-into-campaigns interview

- **The interview is done.** `council/interviews/text-to-campaign.md` holds Wendell's answers and a summary of the
  process. The next piece of work, in a new thread, is the spec, starting with the thin slice: *The Skilled
  Helper*'s introduction or first chapter, run through steps 1 to 4 in Sprout's world.
- **Unasked:** who validates an outer-world BAR outside a coaching container; what the spec's home repo is (Sprout
  or bars-engine).

## Open on 2026-10-07, from texts-to-campaigns pass 1

- **The steward move is written:** `council/moves/text-to-campaign.md`, from
  `council/passes/6FACE_PASS_text-to-campaign1_2026-10-07.md` (ledger `council/ledger/2026-10-07-text-to-campaign-pass1.json`).
  One section at a time, each of the four steps its own thread with one drafting face and one checking face, one file
  per step, all six at the section's close.
- **On the board, standing unless he flips them:** `ttc-move`, `ttc-section-unit`, `ttc-two-faces`,
  `ttc-model-by-step`, `ttc-validate-by-position`, `ttc-files-in-sprout` (answers the spec's home: Sprout),
  `ttc-slice-bar-validator` (answers the outside-coaching validator for slice one; the general case waits).
- **Waiting on him:** `ttc-applications`, how his own applications of the text enter step 1.
- **Next:** once he answers, a new thread runs step 1 on *The Skilled Helper*'s introduction, on Sonnet, and writes
  `extract.yaml` in Sprout. It needs the introduction's text: the copy uploaded to bars-engine if a session can reach
  it, or pages he attaches.

## Open on 2026-10-07, from the ontology game steers thread

- **Applied:** his board answers on `oag-ea-practice`, `oag-main-order`, `oag-daemon-step` (overruled) and `oag-record`
  (A), in bars-engine #264, a draft that stacks on #263 and targets its branch. The positions the build added stand
  unless he flips them: `oag-open-up-tools`, `oag-open-up-marks`, `oag-wave-first`, `oag-dig-deeper`.
- **Merged 2026-10-07 23:50 UTC** on his word ("ok let's merge both of those"): #264 into #263's branch, then #263
  into main, with the 21:06 steers (`oag-clean-up-moves`). Pass 3's test 10 (he plays one blocked step against his
  sketch) is still open on his steps list.
