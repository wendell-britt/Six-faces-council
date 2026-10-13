2026-10-13 (updated 23:20)
# Blender pipeline test plan (strand blender-pipeline-test)

## Next
J5 (clothing) is built: bars-engine draft #315. `content/ontology-game/cave/garments.py --all [--sheet]` cuts a robe
(wide sleeves, crossed collar, slits to the knee), a sash (on the body, and `sash-robe` over the robe) and a topknot for
each of the nine J4 figures in dusk, jade and hemp: 36 skinned GLBs, robe 109 to 119 KB, sash 20, topknot 28. J4's rig
gained two hem bones (`hemF`, `hemB`) that the robe hangs from; cave.js must compute them the same way (character.py
`pose`). Tests J5 (nothing through at 25 keys), J5b (unfitted robe fails) and J5c (swap under 1 ms in Chromium) pass,
and J4 and J4b still pass. Root-game reuse is in bars-engine tasks.md. Round 1 (`j5-look-01`, his notes 23:24): shoulders "peeking through on top", hems "held open against gravity". Round 2
(commit c555b144): the robe is laid over the shoulder tops and the test covers them; the hem flare went from 11 cm to 3 cm
and `hemB` follows the shin more; robe 117 to 125 KB; all five tests pass. Waiting on his look, board step `j5-look-02`
(list blender-cloud-test, step 10), pictures in `/mnt/project-files/3d-build/j5-round2-2026-10-13/`. On his yes, #315
goes ready and the next job wires figures and garments into `cave.js` together, in a fresh thread.

Earlier: J4 (character creator, robe set) is built: bars-engine draft #312. `content/ontology-game/cave/character.py`
`--build slight|average|broad --palette dusk|jade|hemp` (or `--all --sheet`) makes a faceless figure: the body map's
parts per build, the cave avatar's 16 joints, cave.js poseAvatar baked as "Walk" (1 s, 25 keys), and the robe set's
under-layer painted on (crossed collar left over right, tunic to mid-thigh, sash, cuffs, ankle ties, shoes). Nine GLBs
262 to 273 KB (line 300); tests J4 and J4b pass. Round 1 (`j4-look-01`, his notes 22:14): collars "broken", proportions "hitting uncanny valley". Round 2 (commit aaf9cf53): the collar
is one band cut exactly along its edges, over both shoulders and round the neck; the body is stylized (bigger head, plain trunk,
thicker limbs, mitten hands); 246 to 266 KB. His yes on round 2 (22:27, "Yes this is better"); `j4-look-02` ticked, #312 marked ready and merges itself. Pictures in
`/mnt/project-files/3d-build/j4-round2-2026-10-13/`. Next: J5 in a fresh thread. On his yes, #312
goes ready and J5 (clothing: long robe, sash, topknot as skinned garments on this rig, root-game's garment work first)
starts in a fresh thread. The figures reach the game with J5's garments, wired into `cave.js` together.

Earlier: J3 (picture to asset) is done: Wendell's yes on round 2 came in the thread, 2026-10-13 21:43 ("Oh that’s
PERFEXF"), and bars-engine #303 merged (6ff47a2, 2026-10-13 22:29). Board step
`j3-look-02` is ticked done (Your steps list `blender-cloud-test`, step 6), sheet
`/mnt/project-files/3d-build/j3-round2-2026-10-13/j3-round2-sheet.png`. Round 1 he ticked (`j3-look-01`), then gave
notes in the thread (2026-10-13 21:21): textures from the pictures, mushrooms and root "a little blobby", root "Not
readying as tendrils falling in a shape". Round 2: each piece carries its picture as a texture
(`picture(..., texture=True)`); one traced stem per mushroom under a smooth rimmed cap; the root's body is a braid of
four strands with tapering tendrils. Outline: mushrooms 0.822 (was 0.894), crystals 0.855, root 0.910 (was 0.819);
tests offline,bpy pass; chamber 1,482 KB of 3 MB. Next: J4 (character creator, robe set).
Crystals still have five shards to the picture's ten (P4 gap). The chamber objects reach the game when `chamber.py`
is wired into `cave.js`.

Earlier: J2 (adding objects) is built and merged: bars-engine #299 (2026-10-13). `cave/objects.py` gives `chamber.py` one `obj(...)` line per
object from Blendkit (CC0 Boulder 01, pinned by id), a picture (offering bowl, `pictures/offering_bowl.jpg`) or a script
(cushion). Each object passes the kill line, and a source that is not CC0 stops the build (tests J2, J2b). Next: J3 (picture to asset), which needs his pictures in the Drive inbox. The J3 vibe interview ran 2026-10-13 (thread "J3 concept pictures"); his answers and four ChatGPT prompts are in `/mnt/project-files/3d-build/j3-concepts/prompts.md`: wondrous with a sacred, uneasy undertone; per-charge shape, colour and growth (tightness violet gentle mushrooms, tension amber strange crystals, strength green ancient roots, numbness black and bare); a gold glow held in a crystal lamp; hi-bit pixel art. J3 starts when `j3-mushroom`, `j3-crystal` and `j3-root` are in Cave studio inbox. The chamber objects reach
the cave game when `chamber.py` is wired into `cave.js`.

Earlier: The stone is in the cave game: bars-engine draft PR #294, ledger `2026-10-13-cave-stone-textures.json`. Since then, from his
play notes: pieces grow out of the walls and roof by zone, spires are stochastic stalagmites and stalactites, roots hang from
the roof, each charge has its own cave shape (numbness is blackness), a lamp on the figure lights only what is near
(`carryLight` ready for spirits), and wood is a bush, grass and a root. 133 tests pass. Phone page:
https://claude.ai/artifact/23neJJJgywAygUqiJffGvc (version 7). Next: his play; #294 to ready once he has seen it. J2
(adding objects) starts after. The WAVE import and the Big Mind merge are their own thread (big-mind-cave sheet).

Part 1 is built: bars-engine `tools/blender-cloud/tests/`, PR #290 (merged 2026-10-13), ledger `2026-10-13-blender-pipeline-tests-built.json`.
R2 passed: the kit rebuilds byte for byte, so exact matching stands. One command runs everything:
`python3 tools/blender-cloud/tests/run.py --tier offline,bpy,net`; the summary goes to `$W/test-summary.md`.

Left open:
1. Blendkit tests ran 2026-10-13 in the new default environment (bars-engine draft PR #293): N4 up on all four hosts, N1, N2, A1 to A4, G4, G5, N5, V1 pass. Fixtures are pinned in `fixtures.json` (chair `chair` 5, table `table` 0, Wooden Chair `wooden chair` 0, Painted Wooden Chair 02 `wooden chair` 5, A2's bust `bust` 2, A3's 20-tile UDIM brick building `scan old brick building red small` 0). N5: 42 s, 1.51 GB peak, so the kill lines become 84 s and 3 GB (his to confirm). Still open: the E1 look at A2's preview (the 0.18 m bust is tiny beside the 1.8 m figure; the scale is by eye, `--scale`).
2. `bpt-licence-stop` and `bpt-no-restricted-flag` stood and are fixed in #290 (G2 and G2b pass). `bpt-root-curl`
   stood and is fixed in #289 (cave-studio strand, merged 2026-10-13): root_curl is one piece at 499 faces, `KNOWN` is
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

**Detail pass on the grown roots and mushrooms (2026-10-13, his "Start 4"), merged in bars-engine #300.**
`tools/blender-cloud/detail.py` grows the four pieces at their face budgets with no decimation. Cap rims stay sharp, and
each piece carries a grey shade and baked AO in COLOR_0. `cave.js` multiplies that shade into the colour and the glow, and
the clump is nine mushrooms spread wider. The kit is 398 KB, the page is 998 KB of 3 MB, and 303 cave tests pass. Phone
page version 12. Next: his play of the new caps. Previews are in `/mnt/project-files/3d-build/detail-pass-2026-10-13/`.

## Waiting on
Nothing from Wendell; he did step `blender-cloud-test-04` at 02:26. #291 merged 2026-10-13 02:10. The Blendkit tests need a cloud environment that allows api.blenderkit.com, assets.blenderkit.com and cdn.jsdelivr.net. The 12 October session reached Blendkit because it ran in his Default environment; project threads run on a built-in one with no settings. Step `blender-cloud-test-04` asks him to pick Default in Project settings. #290 (Part 1 tests) is a draft. #288 was replaced by bars-engine #295 (2026-10-13 04:00): the Part 2 plan merged with main and updated with the recipe result and J1, marked ready, merges itself once checks pass.
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
