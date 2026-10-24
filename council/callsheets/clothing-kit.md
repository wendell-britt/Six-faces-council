# Clothing kit: robes and cultivation clothing

Strand opened 2026-10-24 by Wendell: "a formal run of the clothing pipeline ... research the approaches we've done and
the approaches to the type of clothing we are trying to make and to create a coherent path to developing robes and
cultivation clothing language that works in our environments and can be modified an expanded with primatives. The goal
here is to test our pipelines ability to solve game design asset problems using the skills in an iterative way".

## State
- Plan doc (review, research, path, nine-primitive language, rounds): https://claude.ai/artifact/Go9KtAbFQqzuUHS9i9p5bQ
- Worker notes: /mnt/project-files/clothing-kit/review-history.md (post-mortem of J5 r1-16, creator, Between, #435),
  research-games.md (Capcom RE Engine, thigh-driven skirt patent, VRM springbone, GoT wind, FFXIV, hanfu MD breakdown),
  research-games-2.md (Chinese/Japanese pass; may land after the opening thread ended; fold into the doc's research section).
- Kit: Shell, Tube, Bell, Panel, Wrap, Band, Lip, Drape, Tassel; slots Inner, Body, Outer, Waist, Ornament; each slot
  masks what it covers below. Skeleton owns the silhouette, physics only sways, folds drawn not simulated, clamp over realism.
- Robe layers (#433/#435, sprout #74): finish its open look; its round 2 (sit poke) folds into this strand's round 1.
  #435's figure-robe.js / wardrobe.js are the kit's starting code.
- Pipeline-test log: each round report records rounds to his yes, thread cost, ladder rung, what the art director caught
  first, and walls hit.

## Next: Round 0, art direction (fresh Opus thread)
Goal: look step `clothing-kit-look-01` on the board with stills inline (`examples`), no game code.
1. Read the plan doc and research-games-2.md; add the second pass to the doc's "Who solved this" section (Claude Docs
   update, doc id 7fea6c93-7650-4677-9abb-571b73d30753, body node dd6fcdb2-4101).
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
