2026-10-12 (updated 23:35)
# Cave studio (Blender in the cloud for the cave, battle fr-cave-studio)

## Next
Round 1 is recorded and the first piece is built: bars-engine draft PR #285 (branch `claude/project-thread-1loob1`).
- `tools/blender-cloud/from_picture.py` builds a model from one front-view picture: `lathe`, `inflate` or `crystals`,
  scores the outline match and renders it. `content/ontology-game/cave/build_kit.py` builds the chamber dressing from
  `cave/pictures/` (`DRESSING` table) into `cave-kit.glb` (84 KB); `cave.js` dresses every chamber; 126 of 126 cave checks pass.
- His first ChatGPT picture (Drive, Cave studio inbox, `cave-crystal-growth.png`) is the crystal cluster, 0.829 match.
  Outline-only scored 0.88 and looked like a blob: read the render, not just the number.
- Comparison page: https://claude.ai/artifact/568K2pwc7Lz5X9Kyftbzza (his crystal on top, three stand-ins below).
- He ticked `cave-studio-03` done with no note (board read 23:29), taken as trust. #285 marked ready; it merges
  itself once checks pass. Next session: more pieces from his pictures (one `DRESSING` row each, picture in
  `cave/pictures/`). Known gap to fix when it matters: crystal mode finds six crystals where his picture has about ten.
- The inbox also holds `taoist_swordsman_front_input.png` and `anime+character+3d+model (1).glb` from before round 1.
  Not used: a figure is not chamber dressing, and a finished model has no licence on record.

## Waiting on
His next picture in the Drive inbox. Nothing else.

## Files
- bars-engine `.specify/specs/cave-studio/` (request with round 1 and the licence answer, spec, plan, tasks);
  `tools/blender-cloud/` (from_picture.py, README); `content/ontology-game/cave/` (build_kit.py, pictures/, manifest.json)
- ledger `2026-10-12-feature-request-cave-studio-round-1.json`, pulls `2026-10-12-pull-222843.json`, `-222920.json`, `-223756.json`
- See cave-of-lessons.md and big-mind-cave.md (the two caves), studio.md (the pipeline they sit in).

## Archive
- Round 1 intake and the rebuild test (passed 2026-10-12) are in request.md.
