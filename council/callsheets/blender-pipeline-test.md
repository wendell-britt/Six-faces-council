2026-10-13 (updated 02:45)
# Blender pipeline test plan (strand blender-pipeline-test)

## Next
J1 is built: bars-engine draft PR #292, ledger `2026-10-13-blender-j1-textures.json`. Wet stone (walls), dry stone (floor,
gate stones) and crystal vein (spires, crystal bed), baked to six 512 px JPEGs; chamber.glb 465 KB. The frame-rate line
can't be judged in the cloud (software WebGL misses it even untextured), so `bpt-j1-frame-rate` puts it on his phone
play after #289 wires the chamber in. Next job: J2, adding objects, in a new thread.

Part 1 is built: bars-engine `tools/blender-cloud/tests/`, PR #290 (merged 2026-10-13), ledger `2026-10-13-blender-pipeline-tests-built.json`.
R2 passed: the kit rebuilds byte for byte, so exact matching stands. One command runs everything:
`python3 tools/blender-cloud/tests/run.py --tier offline,bpy,net`; the summary goes to `$W/test-summary.md`.

Left open:
1. Blendkit tests (G4, G5, N1, N2, A2 to A4, N5) skip, because this environment's network refuses Blendkit. The first
   session that reaches it runs `--tier net`, pins the chair, table and Painted Wooden Chair 02 query and index in
   `fixtures.json`, picks A2's multi-material asset, and records N5's time and memory.
2. `bpt-licence-stop` and `bpt-no-restricted-flag` stood and are fixed in #290 (G2 and G2b pass). `bpt-root-curl`
   stood and is fixed in #289 (cave-studio strand, 2026-10-13): root_curl is one piece at 499 faces, `KNOWN` is
   empty, P3 and P5 pass.
3. Part 2's first job is done: the recipe and its token cost, bars-engine draft PR #291, ledger
   `2026-10-13-blender-recipe-token-cost.json`, results in `tools/blender-cloud/recipe_trial/RESULTS.md`. T1 passed, T3
   passed (8 of 10 both ways), T2 missed (recipe 0.69 of code, line 0.33). He let `bpt-recipe-result` stand (board read
   0145): the recipe is dropped. The chamber is `content/ontology-game/cave/chamber.py` (#291), one `place(...)` line
   per piece; J1 textures and every later job edit that script. The recipe and its builder sit in
   `tools/blender-cloud/recipe_trial/` as the record. Wiring the chamber into `cave.js` waits for #289.

**Part 2, added 2026-10-13 from his second message:** whether Claude can change the cave from words and pictures, with
the fewest tokens. Claude edits a recipe (`cave/scene.yaml`) and a fixed script builds it; T1 to T3 measure the cost
against writing `bpy` code. Then five jobs, one thread each, in order: procedural textures, adding objects, picture to
model, a character creator themed on the robe set, and clothing as skinned swappable garments (his "biggest test").
Board positions `bpt-recipe`, `bpt-robe-theme`, `bpt-skinned-garments`, `bpt-order`. Part 1 merged in #287; Part 2 is in bars-engine #288 (draft). Part 2 starts after #285 merges. He let all four stand (2026-10-13 00:24); his steer on `bpt-skinned-garments`: "Use as much as we can from the root game for this as we’ve already done many garment tests there", so J5 begins by listing root-game's garment work and reusing it (spec.md, J5).

## Waiting on
Wendell has one step, `blender-cloud-test-04`. #291 merged 2026-10-13 02:10. The Blendkit tests need a cloud environment that allows api.blenderkit.com, assets.blenderkit.com and cdn.jsdelivr.net. The 12 October session reached Blendkit because it ran in his Default environment; project threads run on a built-in one with no settings. Step `blender-cloud-test-04` asks him to pick Default in Project settings. #290 (Part 1 tests) is a draft. #288 (Part 2, Markdown only) is a draft; mark it ready once he has seen it.
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
