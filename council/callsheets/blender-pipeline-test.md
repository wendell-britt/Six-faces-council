2026-10-13 (updated 01:55)
# Blender pipeline test plan (strand blender-pipeline-test)

## Next
Part 1 is built: bars-engine `tools/blender-cloud/tests/`, draft PR #290, ledger `2026-10-13-blender-pipeline-tests-built.json`.
R2 passed: the kit rebuilds byte for byte, so exact matching stands. One command runs everything:
`python3 tools/blender-cloud/tests/run.py --tier offline,bpy,net`; the summary goes to `$W/test-summary.md`.

Left open:
1. Blendkit tests (G4, G5, N1, N2, A2 to A4, N5) skip, because this environment's network refuses Blendkit. The first
   session that reaches it runs `--tier net`, pins the chair, table and Painted Wooden Chair 02 query and index in
   `fixtures.json`, picks A2's multi-material asset, and records N5's time and memory.
2. `bpt-licence-stop` and `bpt-no-restricted-flag` stood and are fixed in #290 (G2 and G2b pass). `bpt-root-curl`
   stood: the cave-studio strand fixes root_curl's loose blob and face budget once #289 lands, then unmarks P3 and P5
   in `tests/test_bpy.py` (`KNOWN`).
3. Part 2's first job is done: the recipe and its token cost, bars-engine draft PR #291, ledger
   `2026-10-13-blender-recipe-token-cost.json`, results in `tools/blender-cloud/recipe_trial/RESULTS.md`. T1 passed, T3
   passed (8 of 10 both ways), T2 missed (recipe 0.69 of code, line 0.33). Board position `bpt-recipe-result`: the
   recipe is dropped and J1 on edits a committed Blender script, unless he flips it. The next thread (J1 textures)
   reads that row first; if he flipped it, J1 adds a texture line to `scene.yaml` instead. Fix in the builder either
   way: scatter keeps clear of what it is near, and glow is too strong (RESULTS.md). Wiring the chamber into
   `cave.js` waits for #289.

**Part 2, added 2026-10-13 from his second message:** whether Claude can change the cave from words and pictures, with
the fewest tokens. Claude edits a recipe (`cave/scene.yaml`) and a fixed script builds it; T1 to T3 measure the cost
against writing `bpy` code. Then five jobs, one thread each, in order: procedural textures, adding objects, picture to
model, a character creator themed on the robe set, and clothing as skinned swappable garments (his "biggest test").
Board positions `bpt-recipe`, `bpt-robe-theme`, `bpt-skinned-garments`, `bpt-order`. Part 1 merged in #287; Part 2 is in bars-engine #288 (draft). Part 2 starts after #285 merges. He let all four stand (2026-10-13 00:24); his steer on `bpt-skinned-garments`: "Use as much as we can from the root game for this as we’ve already done many garment tests there", so J5 begins by listing root-game's garment work and reusing it (spec.md, J5).

## Waiting on
Nothing from Wendell; `bpt-recipe-result` stands unless he flips it. #291 (recipe and token cost) is a draft. #290 (Part 1 tests) is a draft. #288 (Part 2, Markdown only) is a draft; mark it ready once he has seen it.
#285 merged; the picture-path tests run on main. His two tests are steps: N3 is `cave-studio-02`, and E3 goes on
Your steps when the build thread first republishes a page.

## Files
- bars-engine `tools/blender-cloud/` (README), `.specify/specs/blender-cloud-hardening/`, `.specify/specs/cave-studio/`,
  `content/ontology-game/cave/` and `content/ontology-game/body/`
- ledger `2026-10-12-blender-cloud-session.json`; call sheets cave-studio.md and studio.md

## Archive
- 2026-10-12 23:50, the brief for the plan thread: what the pipeline was, what had been tested by hand, what never had, and
  the six questions the plan had to answer. All six are answered in spec.md (tiers, exact or tolerance, the score trap,
  where the tests live and CI, fixtures). Full text in git history of this file.
