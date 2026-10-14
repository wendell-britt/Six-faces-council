# Where Wendell's ideas are saved and tracked: audit, 2026-10-13

Asked by Wendell, 2026-10-13: "Where are we collecting my ideas and thoughts." He went on: "After we do a podcast I
need to injest my episodes and start building out my own writing corprus for 2.0 edition of Mastering Allyship or the
Allyship Game Masters's guide or any other infoproducts I'd want to create."

This is the session's reading of the record, not a ruling. Sources are the repos named under each row.

## Where an idea lands today

| Place | What it holds | Wendell's exact words? | Can a book pull from it? |
|---|---|---|---|
| Board `steer` and `steers_recorded` (six-faces-council) | 29 general steers, each with date and ledger record | Yes | No tag, no product, no search by theme |
| Quotes inside rules, passes and moves (six-faces-council) | About 35 dated quotes in 29 files, written as "Wendell, date: ..." | Yes | Found only by grep; sorted by whatever file held them |
| Board positions and resolved rows | 669 positions; his rulings, flips and overrules | Partly (the ruling, seldom the reasoning) | Decisions, not thinking |
| Memory files (`/areas`, `/topics`) | Compact [stated] lines per project, such as the Art of War adaptation | No, summaries | Good map of what he holds; unusable as prose |
| BARs and Sage Map (mtgoa-manuscript `BARs/`, memory `sage-map`) | 13 BARs with origin, source and verification; Sage Map fragments under the Rule of 20 | Mostly | The closest working corpus. `tracker.json` tracks are empty, and the repo's last commit was 2026-09-24 |
| `type: idea` notes (mtgoa-manuscript `specs/`) | One file, `IDEA_ALLYSHIP_AT_WORK`, with front matter and a review date | Yes | Right shape; used once |
| Episode transcripts and copy | Claude project files, `podcast/<episode>/` (not a git repo): transcript, copy, thumbnails, clips | Yes, but the host's lines are mixed with the guest's | Nothing reads them after the clips are cut |
| Outreach contacts (Council Board `contacts`) | Guest briefs. Today's frame for Dan Allison went here | Yes | Wrong place: it is Wendell's thinking, filed under a guest |
| `game-masters-guide` repo | A README and nothing else, though memory records the repo as the Guide's source of truth | n/a | Empty |
| `mtgoa-manuscript` repo | The book, plus 130 process files | n/a | Canon is `manuscript/ch1-9.md`; no 2.0 branch or folder |

## What the audit finds

1. The podcast move stops at the clips. `council/moves/podcast-episode.md` has six steps: read, copy, thumbnails,
   board picks, his steps, clips. No step turns what he said into anything he keeps. Episode 1 and 2 transcripts
   exist in project files and feed nothing.
2. His words are saved in six shapes. None is searchable beside the others, and none says which product a line is for.
3. The two repos that could hold a corpus are the wrong homes today. `six-faces-council` and `mtgoa-manuscript` are
   public, and a transcript holds guests' words. `game-masters-guide` is private and empty.
4. The closest working design is already his: a BAR has text, origin, source and verification, and the Sage Map stops
   at twenty fragments for a critique. Both stalled after September and neither reaches the podcast.
5. The board does not hold thinking. It holds questions, positions and steps. A thought belongs in the board only
   once it has become a claim a product needs.

## What is proposed

Rows `cp-unit`, `cp-home`, `cp-capture`, `cp-ingest`, `cp-slots` and `cp-backfill` on the Council Board, each a
position that stands unless he flips it. The strand's sheet is `council/callsheets/corpus.md`.
