# Six-faces council

This repo is the home of Wendell's council of six Game Master faces: Shaman, Architect, Challenger,
Regent, Diplomat and Sage. Each face argues a question from one developmental altitude, the Sage
synthesises without deciding, and Wendell rules on a board.

## What lives here

- `council/faces.yaml` holds the six lenses, their term tests, and the lessons each face has learned
  from Wendell's rulings, in his words.
- `.claude/skills/six-faces/SKILL.md` tells a Claude Code session how to run a pass or a term pass.
- `council/portable/` is a copy of the skill for places with no repo, such as an ordinary Claude chat.
  `python3 council/package_skill.py` zips it for upload to a claude.ai account.
- `council/hooks/council-sync.sh` runs when a session opens in any council repo. It pulls the
  definition file, the skill, the voice lint and itself from here, and tells the session which copy
  it has.
- `council/tools/voice_lint.py` is the house voice lint, shared with every council repo.
- `board/` builds the board Wendell rules on: https://claude.ai/artifact/DxyShVS8tmvJym4HAsgnho
- `council/ledger/` holds the records of decisions about the council itself. Records about a
  project stay in that project's repo.

## Adding a repo

From this repo, run `python3 council/install.py <path to the other repo>`. It copies the shared
files, registers the session-start hook, and adds the repo to `council/repos.yaml`. Commit the new
files in the other repo and merge them. From then on, a change made here reaches that repo at its
next session start.

## Rules that keep it in one piece

- Lessons and lens changes are written here and nowhere else. A lesson recorded in another repo goes
  under `lessons_pending` in that repo's ledger record, and `python3 council/collect_lessons.py`
  finds it.
- Ledgers, term registries and glossaries never sync. They stay in the repo whose decision they
  record. `python3 council/stats.py --remote` counts all of them over GitHub.
- The council never edits `faces.yaml` on its own authority. Only a ruling by Wendell adds a lesson.

The design history, the first four passes and the research behind the faces are in
johnair01/bars-engine, under `.specify/specs/six-faces-council-agents/`, where the council started.
