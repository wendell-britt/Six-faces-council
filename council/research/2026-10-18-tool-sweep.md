# Tool sweep of the open strands, 2026-10-18

The first run of the tool ladder (docs/tool-scout.md) over the open strands in project memory and the callsheets. Each
row names what we build by hand, the tool that may do it, and the next move. Read from the callsheets, not from the
code; a row marked "inferred" was not checked in the repo it names. Nothing here changes a running round: each strand
picks its row up at its next `start`, where `next_round.py` prints the same tools.

| Strand | Built by hand now | Tool that may do it | Next move |
|---|---|---|---|
| J5 robe cloth (blender-pipeline-test) | A runtime cloth solver in `cloth.js`, then spring chains on the sleeves, tuned over thirteen rounds of jitter fixes | `blender-cloth-bake`: Blender's cloth solver baked over the walk clip into morph targets, played back with no solver in the game; `three-vrm-springbone` for sleeves if a live chain is still wanted | Next J5 round builds one baked robe beside the cloth.js robe and measures both with J5d; keep cloth.js only for motion that is not a fixed clip |
| Daemon bodies, gestures and let-gos (blender-frame-flesh-warp, big-mind-cave) | J4 rig and every pose and let-go keyed in code | `rigify` for the rig, `cmu-mocap` clips retargeted with the vendored blender-animation skill for walks and gestures; `mixamo` (gated, Adobe sign-in) for clips | Retarget one CMU walk and one gesture onto a daemon and compare with the keyed version; Mixamo only after his step |
| Spirit animal bases (spirit-generator) | Metaball bodies built from code, checked against photos since round 18 | `quaternius` and `blenderkit` animals as base meshes to reshape; `assetfurnace` from the reference photos (gated, docs/asset-generation.md) | Round 20 (basset hound, elephant) runs rung 3 first; whether a CC0 elephant or hound exists is unchecked |
| Spirit eyes and mouths (spirit-generator) | Eye and mouth geometry rebuilt by hand in rounds 3, 5 and 6 | Vendored blender-facial-shapekeys skill for expression shape keys | Use it when a round next touches faces |
| Cave chambers and materials (cave-studio, blender-pipeline-test J1) | Procedural stone textures | `poly-haven` and `ambientcg` CC0 rock, moss and ground materials and HDRIs; `blenderkit` already in use | Next chamber dressing pulls a CC0 rock set before writing a procedural one |
| Walking in the caves (the WAVE and cave-levels callsheets) | Click to walk and free walking written per level | `recast-navigation-js` navmesh pathfinding | The walkable skeleton thread checks it before writing movement |
| The Between 3D garden (relationship-creature) | Garden props built in code | `quaternius` and `kenney` CC0 nature packs, `poly-haven` | Round 3 dresses from a pack where a prop is generic |
| Chapter 1 demo and engine slice story layer (sprout) | Story and referee layer in sprout code (inferred; sprout not read here) | `inkjs` for branching story | The next engine-slice thread reads sprout and runs rung 3 before adding story code |

Strands with no row: board plumbing, morning menu, coaching, podcast and the council passes build our own process,
where no outside tool was found to fit; Root and the wave battle are game rules of our own.

Why this was missed: the council had a reach test for questions and no matching step for builds. Threads were briefed
to build a round, so they built it; the vendored Blender skills (bars-engine #374) sat beside threads that never
looked for them.
