2026-10-13 (updated 00:10)
# Blender pipeline test plan (strand blender-pipeline-test)

## Next
The plan is written: bars-engine `.specify/specs/blender-pipeline-test/` (spec.md, plan.md, tasks.md), draft PR #287,
ledger `2026-10-13-blender-pipeline-test-plan.json`. No tests were built and nothing in the pipeline changed.

The next piece of work is one fresh thread that builds the tests, following plan.md's order:
1. Falsify first: R2, `build_kit.py` with picture dressing, run twice on #285's branch (or main, if #285 has merged).
   Byte for byte, or name the mesh that differs. Everything else goes ahead whatever it says.
2. Offline tier (G1, G2, G2b, G6, G7) and one step in `.github/workflows/frontend-check.yml`. G2 and G2b are known gaps:
   a sidecar with no `license` key crashes with a `KeyError` instead of a `STOP:` line, and `build_viewer.py
   --allow-restricted` lets a Royalty Free model into a page, against `cs-cc0-or-own`. Raise both on the board as
   positions (the record answers them); fixing them is a pipeline change.
3. `bpy` tier, contact sheet and `LOOKED.md`, network tier (N5 in the background), then the picture-path tests once #285 merges.
All tests go in a new `tools/blender-cloud/tests/`; the cave-studio strand owns `from_picture.py`, `build_kit.py` and `cave/`.

Read spec.md for the test table; this sheet does not repeat it.

**Part 2, added 2026-10-13 from his second message:** whether Claude can change the cave from words and pictures, with
the fewest tokens. Claude edits a recipe (`cave/scene.yaml`) and a fixed script builds it; T1 to T3 measure the cost
against writing `bpy` code. Then five jobs, one thread each, in order: procedural textures, adding objects, picture to
model, a character creator themed on the robe set, and clothing as skinned swappable garments (his "biggest test").
Board positions `bpt-recipe`, `bpt-robe-theme`, `bpt-skinned-garments`, `bpt-order`. Part 1 merged in #287; Part 2 is in bars-engine #288 (draft). Part 2 starts after #285 merges. He let all four stand (2026-10-13 00:24); his steer on `bpt-skinned-garments`: "Use as much as we can from the root game for this as we’ve already done many garment tests there", so J5 begins by listing root-game's garment work and reusing it (spec.md, J5).

## Waiting on
The plan needs nothing from Wendell. #287 merged (Part 1). #288 (Part 2, Markdown only) is a draft; mark it ready once he has seen it.
The picture-path tests wait for bars-engine #285 to merge. His two tests are steps: N3 is `cave-studio-02`, and E3 goes on
Your steps when the build thread first republishes a page.

## Files
- bars-engine `tools/blender-cloud/` (README), `.specify/specs/blender-cloud-hardening/`, `.specify/specs/cave-studio/`,
  `content/ontology-game/cave/` and `content/ontology-game/body/`
- ledger `2026-10-12-blender-cloud-session.json`; call sheets cave-studio.md and studio.md

## Archive
- 2026-10-12 23:50, the brief for the plan thread: what the pipeline was, what had been tested by hand, what never had, and
  the six questions the plan had to answer. All six are answered in spec.md (tiers, exact or tolerance, the score trap,
  where the tests live and CI, fixtures). Full text in git history of this file.
