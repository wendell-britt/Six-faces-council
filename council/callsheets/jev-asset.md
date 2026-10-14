# jev-asset

State 2026-10-14. Wendell ruled `jev-asset-piles` = admin-first: label the 20 admin rows, size the teaching pile
afterwards. Steer: the labelling must not be a spreadsheet to him.

- Done: Claude read the doc line and code for all 20 `asset-admin` rows (bars-engine main, 2026-10-14).
  16 are labelled in `council/jev/admin_labels.json` (15 agrees, 1 disagrees: AS-011, the 5/10 MB upload limit).
  The statement list itself is bars-engine branch `claude/inspiring-bhabha-f752d0`, `council/jev/asset_statements.json`.
- Answered 2026-10-14 (recorded in `admin_labels.json`): AS-029 agrees, AS-032 disagrees, AS-064 agrees, AS-024 cannot-tell (his steer: five move icons now, doc predates Open Up). Scoring pile freeze: 19 rows. Was open: 4 rows are board questions `jev-lab-as-024`, `jev-lab-as-029`, `jev-lab-as-032`, `jev-lab-as-064`
  (one tap each, Claude's reading shown). Position `jev-admin-16-labelled` says the 16 stand unless he flips one.
- Frozen 2026-10-14: scoring pile = 19 rows in `council/jev/scoring_pile_2026-10-14.json` (17 agrees, 2 disagrees: AS-011, AS-032;
  AS-024 left out as cannot-tell). Not edited after this.
- Mark fixed 2026-10-14 in `council/jev/mark_2026-10-14.md` (both 2 positives caught, at most 1 false flag of 17). Not edited after.
- Teaching pile sized 2026-10-14: Wendell ruled `jev-teaching-pile` = 30 (board read 2235). The 30 rows are labelled in
  `council/jev/teaching_pile_2026-10-14.json` (18 agrees, 12 disagrees), drawn from the 158 sprite-pre-august and card-art-deprecated
  rows. All 9 known-drift tags in those 158 are in it. Board positions `jev-teaching-30-labelled` and `jev-teaching-playbook-readings`
  say the labels stand unless he flips one; the second explains the 4 layer-name rows (disagree) against the 3 folder-path rows (agree)
  that the brief lumped as drift (c). Not part of the score; no mark applies.
- Run 2026-10-14 (results in `council/jev/results_2026-10-14.md`): practice 27 of 30 match the labels (misses AS-182, AS-100, AS-101: the model never searched bars-engine `backend/`).
  Scoring pile: catches 2 of 2, false flags 1 of 17 (AS-002), mark passed. The constant-extraction script (`council/jev/constant_baseline.py`, written for the run) caught 0 of 2 and flagged 3 agreeing rows.
  Board positions `jev-trial-result` and `jev-next-pile-with-code-map` stand unless flipped.
- Superseded 2026-10-14: second pile run (see below).
- (old) Next: write a second pile of new, unseen doc rows labelled before the run, with a fixed code map in the run brief (src/, prisma/schema.prisma, scripts/, backend/, package.json, public/); then run the model once. Wendell may flip AS-002 to disagrees; apply it before any rerun of the stats, never to the frozen file.
- Stale doc: the move-icon line (AS-024) says 4 icons; the ontology has 5 since Open Up. Only that row was affected, and it is already out.
  The doc itself in bars-engine `.specify/specs/asset-register-design-system/spec.md` line 68 still needs the fix.

- Second pile run 2026-10-14 (results `council/jev/results_pile2_2026-10-14.md`): 48 new rows from 7 unseen docs, labelled in commit 8551d94 before the run, fixed code map in the brief. Catches 8 of 8, false flags 0 of 35 (43 clear rows), 5 borderline rows apart (B2-008, 024, 027, 034, 038). Script baseline 3 of 8, 8 false flags. Board positions `jev-pile2-result` and `jev-pile2-borderline` stand unless flipped.
- Next: run the model with the code map over one whole unlabelled doc (`docs/OPENAI_API_USAGE.md` first) and hand Wendell the flags as a fix list; the doc fixes found (BUILD_RELIABILITY, DEVELOPER_ONBOARDING, OPENAI_API_USAGE, BOOKS_CONTEXT_API) can go to bars-engine as one doc-fix PR. The AS-002 / spec.md line-68 fixes from before are still open.
