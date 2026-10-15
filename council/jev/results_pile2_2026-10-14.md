# Jev asset trial: second pile with a code map

Run 2026-10-14, once, on 48 new doc rows from seven bars-engine docs the model had not seen (`BAR_FORGE_API`, `BOOKS_CONTEXT_API`, `BUILD_RELIABILITY`, `DB_STRATEGY`, `PRISMA_MIGRATE_STRATEGY`, `DEVELOPER_ONBOARDING`, `OPENAI_API_USAGE`). Source: bars-engine main at 1885d16. Pile and labels (`pile2_rows_*.json`, `pile2_labels_*.json`) were pushed in commit 8551d94 before the model ran and were not edited after. The run brief gave the fixed code map (`src/`, `prisma/schema.prisma` and migrations, `scripts/`, `backend/`, `package.json`, `public/`, plus `.github/`, `.husky/`, `openapi/` when a line points there) and withheld the labels. Answers: `run_pile2_answers_2026-10-14.json`.

## Result

Scored rows are the 43 with a clear label: 8 positives (doc and code disagree) and 35 agreeing rows. Five rows are borderline and are reported apart.

| Measure | Result | 95% interval |
|---|---|---|
| Catches | 8 of 8 | true rate plausibly 63% to 100% |
| False flags on agreeing rows | 0 of 35 | plausibly 0% to 10% |
| Cannot tell | 0 of 48 | |

The first trial's mark (catch all positives, at most 1 false flag in 17) is met here too, on a pile 2.5 times larger. The code map fixed the earlier failure: the model searched every listed place and no row came back "cannot tell" for want of looking.

Catches: B2-017 (404 on `/quests`: an empty book returns 200), B2-022 (`verify:build-reliability` runs four checks, not two), B2-026 (no `strand:consult:build-reliability` script), B2-035 (onboarding says `db push` is fine for local use; the script now exits with an error), B2-040/042/045/046 (`OPENAI_API_USAGE`: "2 call sites" is 16+ files, `generateQuestCore` and `QUEST_GEN_MODEL`/`QUEST_GEN_AI_ENABLED` do not exist).

## Script baseline (same 43 rows)

`constant_baseline.py`, unchanged: catches 3 of 8 (B2-042, 045, 046), false flags 8 of 35. The model caught five the script missed (B2-017, 022, 026, 035, 040); the script flagged nothing the model caught that the model had missed. Same caveat as before: the script is crude.

## Borderline rows (5, not in the counts)

| Row | My label | Model | Note |
|---|---|---|---|
| B2-008 | disagrees | agrees | Doc says the OpenAPI file lists three game-master routes. The yaml does; no route exists in `src/`. Model read the line as being about the yaml. |
| B2-024 | disagrees | agrees | Pre-commit runs `check`, which includes lint; doc omits lint. Minor. |
| B2-038 | disagrees | agrees | Same drift, in the onboarding doc. |
| B2-027 | agrees | agrees | Preview builds skip migrate deploy. |
| B2-034 | cannot tell | disagrees | "Node v18+": no `engines` field, CI uses Node 22, and the model says Next 16.1.5 needs Node 20 or later. That requirement is from Next's published docs and is not checked in this repo. Likely a real drift I labelled too softly. |

The model's answers on B2-008, 024 and 038 are defensible, so I would not count them as misses. If Wendell flips B2-034 to disagrees, catches become 9 of 9.

## How sure these numbers can be

- Counts are small. 8 of 8 only says the catch rate is plausibly 63% or higher; 0 of 35 says the false-flag rate is plausibly under 10%.
- I chose the docs and wrote the labels from the same code the model read, so the labels are not independent of the method. A doc line I misread would show as a model miss or a false flag against me. Wendell checking the borderline readings is the independent look.
- I picked docs likely to hold checkable claims (APIs, scripts, env vars). The rows are easier than prose about design intent, so this says nothing about those. The pile also has a higher rate of drift (11 of 48 labelled disagree) than the earlier pile.
- No row from the first trial was reused. The model ran once; no prompt change after seeing results.
- Not tested: docs where the code is hard to find, long behavioural claims, and rows with no drift in a doc that is mostly right.

## Recommended next move

Treat the trial as earning its place on this evidence and put it in front of real docs: run the same brief with the code map over one whole doc that nobody has labelled (start with `docs/OPENAI_API_USAGE.md`, where the model found four drifts), and give Wendell the flags as a fix list, not a score. Four of the doc drifts found here are small edits (`BUILD_RELIABILITY`, `DEVELOPER_ONBOARDING`, `OPENAI_API_USAGE`, `BOOKS_CONTEXT_API`) and could go to bars-engine as a doc-fix PR. Board position `jev-pile2-result` carries this.
