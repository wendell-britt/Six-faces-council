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

## Open on 2026-10-06, from the Flirtcraft podcast thread (battle `fr-podcast-launch`)

- **Podcast page:** flirtcraft #9 merged (b5284f5). The player and the Listen on Spotify button go in by setting
  `embedUrl` and the Spotify `href` in flirtcraft `lib/podcast.ts` once Wendell pastes the episode link (step 5 of
  Your steps list `podcast-spotify`).
- **Episode 1 copy (`pod-ep1-from-audio`):** waits on step 2, Wendell attaching the audio in the Podcast page thread.
  Then draft the show description, title and notes, and put the title on the board as a question.
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
- **The fresh-session routine exists but is not in use:** the daily session made
  `trig_01Q9mMcVwR4MCqHQzUHwcmiS` (2026-10-06 23:30 UTC, outside any project). Its environment shows no repository,
  and the first daily routine failed the same way, so `PICKUP_TRIGGER` stays on `trig_01L138vKTaN9MSJoFKRmaBNx`,
  which Wendell's Send reached at 23:26. Once Wendell attaches wendell-britt/six-faces-council to that routine on its
  claude.ai page, fire it once with nothing unrecorded, then swap the id in `PICKUP_TRIGGER` and docs/pickup.md.
  The daily routine's step 1b now reads `PICKUP_TRIGGER`, so it follows the swap.
- **Work the answers begin:** `wave-acknowledge-turn` overruled (steer: a trigram move is the acknowledgement,
  welcoming is listening) for the WAVE thread; `oag-faces-names` chose plain words, steer: a popup page per face,
  for the ontology game thread.

## Open on 2026-10-06, from the Flirtcraft loop audit thread (battle `fr-orient-new-players`)

- **The pass:** flirtcraft `6FACE_PASS3_2026-10-06.md` and `council/ledger/2026-10-06-loop-pass1.json`, in flirtcraft
  #10. The readable page is https://claude.ai/artifact/1QydwJABFethDKW34vwBsR.
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
