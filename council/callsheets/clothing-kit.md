# Clothing kit: robes and cultivation clothing

Strand opened 2026-10-24 by Wendell: "a formal run of the clothing pipeline ... research the approaches we've done and
the approaches to the type of clothing we are trying to make and to create a coherent path to developing robes and
cultivation clothing language that works in our environments and can be modified an expanded with primatives. The goal
here is to test our pipelines ability to solve game design asset problems using the skills in an iterative way".

## State
- Plan doc (review, research, path, nine-primitive language, rounds): https://claude.ai/artifact/Go9KtAbFQqzuUHS9i9p5bQ
- Worker notes: /mnt/project-files/clothing-kit/review-history.md (post-mortem of J5 r1-16, creator, Between, #435),
  research-games.md (Capcom RE Engine, thigh-driven skirt patent, VRM springbone, GoT wind, FFXIV, hanfu MD breakdown),
  research-games-2.md (Japanese/Chinese pass: QualiArts thigh helper bone, SF6 anime physics, Shining Nikki sleeves; already in the doc).
- Kit: Shell, Tube, Bell, Panel, Wrap, Band, Lip, Drape, Tassel; slots Inner, Body, Outer, Waist, Ornament; each slot
  masks what it covers below. Skeleton owns the silhouette, physics only sways, folds drawn not simulated, clamp over realism.
- Robe layers (#433/#435, sprout #74): finish its open look; its round 2 (sit poke) folds into this strand's round 1.
  #435's figure-robe.js / wardrobe.js are the kit's starting code.
- Pipeline-test log: each round report records rounds to his yes, thread cost, ladder rung, what the art director caught
  first, and walls hit.

## Next: Round 0, art direction (fresh Opus thread)
Goal: look step `clothing-kit-look-01` on the board with stills inline (`examples`), no game code.
1. Read the plan doc (both research passes are in it; Claude Docs
   doc id 7fea6c93-7650-4677-9abb-571b73d30753, body node dd6fcdb2-4101).
2. Reference board: our own past robes (/mnt/project-files/3d-build/j5-round9*, arcade-robe-r5*, robe-layers-2026-10-24)
   plus outside references for hanfu, kimono/hakama, cultivation robes; what we take from each. Bulk image reading in a
   worker that returns a short verdict.
3. Stills: a kit sheet of the nine primitives and three composed outfits (novice, practitioner, elder) on Average Dusk
   (/mnt/project-files/3d-build/j4-characters-2026-10-13/average-dusk.glb), front, side, seated. Procedural three.js
   primitives rendered with Playwright is the cheap route (no Blender in most containers). Lighting: soft multi-directional.
4. CCGS art-director review of the stills against his notes (hem "painted on", sleeves "one piece", slit void), then
   fix and recheck.
5. Board: question `clothing-kit-look-01` (yes builds round 1 / yes with note / not yet), examples inline; land via
   board/sync_board.py on main.
scout: rung 3 for round 1 (three-vrm springbone math for Bell/Drape/Tassel chains); rung 2 for stills (#435 code, j4 GLB).
Rules to name: docs/3d-math.md rule 8 and garment page https://claude.ai/artifact/AvPdQRkPQwNcXEKfuxewAv; idle rule
(lt-idle-default); art direction before code; previews one click.

### Round 0 done (2026-10-24)
- Page: https://claude.ai/artifact/RhFdNzCGp6NUE5SPbhHdEt (source /mnt/project-files/clothing-kit/round0/look.html).
  Stills /mnt/project-files/clothing-kit/round0/stills-v2/ (kit, novice, practitioner, elder: front, mid-step, seated).
  Reference board /mnt/project-files/clothing-kit/round0/reference-board.md (8 Commons refs in refs/, our past robes kept/failed).
  Still generator /mnt/project-files/clothing-kit/round0/source/ (kit.js: the nine primitives fitted to the posed body,
  stage.js: outfits, sheet.html + shot.cjs: Playwright render; three r169 from npm). It solves drapes per pose for stills;
  it is NOT the round 1 rig, but its dials and the Bell chain-in-its-own-plane idea carry over.
- Board: question `clothing-kit-look-01` (stills inline), position `ck-open-at-belt` (his robe-layers-look-03 note:
  a long robe opens at the belt, front and back hang free; short robes keep hip slits). Rows
  `council/callsheets/rows/clothing-kit-r0-2026-10-24.json`.
- Art director: v1 fix first (6), v2 fix first small; reviews in round0/art-director-review-v1.md, -v2.md.
  Open gaps for round 1/2: hip junction under the belt on the walk; cuff Lip must be the sleeve edge, not a ring;
  Drape sleeves on a seated lap; kit tiles show grey shoulders; back views and motion unchecked.
- Pipeline-test log, round 0: one thread; ladder rung 2 (j4 GLB, own three.js), rung 3 not needed for stills; the art
  director caught shoulders, elbow crease, painted hem, outer/inner punch-through and seated slab before him; walls: no
  image generation, the walk clip only (sit posed by hand), the thread passed 150k by reading its own renders.
  Lesson: send every render look to a worker, not only the AD checks.

### Round 0b done (2026-10-24), from his "Not yet" on clothing-kit-look-01
His note: shoulders don't feel natural, seams will make boxy intersections, pieces show old artifacts.
- Page: https://claude.ai/artifact/U8VF9Jx5nmPvGFpCkp9V2B (source /mnt/project-files/clothing-kit/round0b/look.html).
  Generator round0b/source/ (README.txt; `node checks.cjs` = coverage, camera-ray skin/holes, thin/long triangles).
- Worker notes in round0b/: research-seams-shoulders.md (ranked: copy body skin weights, cut-on sleeve cap inside the
  shell, matched ring counts, averaged seam normals, clavicle + twist bone), skeleton-check.md (verdict PARTLY: no
  clavicle, max 2 influences, steep A-pose; base Walk clip flips a leg), past-fixes.md (25 past fixes, 9 missing in r0).
- Built: clavicles (28% share), shoulder weights blended to 3-4 bones, fit pose arms 45 deg out, garment copies body
  weights, cut-on sleeve cap, 48 matched divisions, body mask per outfit, cuff = sleeve edge, layer offsets.
- Independent AD (Sonnet, 3 passes, art-director-review-0b-independent.md): novice + practitioner ready; elder not
  (hairline seams back shoulders, waist step, padded shoulders, seated cuff loop). All: seated skirt slab, seated cuff
  hoops, knee into skirt mid-walk, trouser peek at practitioner front hem.
- Board: question clothing-kit-look-02 (examples inline), positions ck-cut-on-shoulder, ck-collarbone-rig,
  ck-mocap-walk. Rows council/callsheets/rows/clothing-kit-r0b-2026-10-24.json.
- Pipeline-test log, round 0b: one thread, 5 workers; rung 2 (own generator). The independent reviewer caught cuff
  rings, back lump and collar notch that the builder's self-review passed: always use a separate reviewer worker.

## Next: Round 1, the core kit (fresh Opus thread, on his yes to clothing-kit-look-02)
Carry round 0b's rig (clavicles, weights, fit pose) and the elder/seated gaps above. On a note: round 0c from
round0b/source/ with the same independent reviewer loop.

Per the plan doc's round 1: Shell, Tube, Bell, Band, Lip as one plain JS module in bars-engine (start from #435's
figure-robe.js / wardrobe.js), garment-contract.md, ray probe across walk, idle, sit, turn x 3 bodies, novice in the
Between mirror with a one-click preview. Fold in his note, ck-open-at-belt, and the round 0 gaps above. On a note
instead: round 0b from his note with the generator in round0/source/.
