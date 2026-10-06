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
- **Cover art (`pod-art-ma`):** three drafts done 2026-10-06, question `pod-cover-pick` on the board (round 3).
  Files: `/mnt/project-files/podcast/covers/` (3000x3000 JPEGs, plus `covers.html` and `render.js` that drew them;
  render with Playwright at deviceScaleFactor 3).
  Recolored to flirt red (#ff5a5f to #d4003a) the same day; first versions in `covers/v1-mastering-allyship-colors/`.
  Board read 2002 (2026-10-06): Wendell steered pod-art-ma toward "one strong color change so people can
  differentiate it from MTGOA"; `pod-art-recolor` stands, so the cover thread redraws the three in a new color, then
  updates `pod-cover-pick`'s options before he picks. The look came from bars-engine (johnair01/bars-engine, public):
  `public/mastering-allyship/cover-front.png` and `src/styles/bars-tokens.css`. Once he picks, add the file to the
  `podcast-spotify` steps.
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
