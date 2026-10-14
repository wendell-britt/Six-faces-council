# Blender: frame, flesh, warp (parametric creatures and NPCs)

## Next
- Source: a tweet Wendell shared 2026-10-14 (skeleton first, then flesh, then warp; headless Blender practice). Its numbers (benchmark scores, who built it) are unverified; the practice is sound on its own and was checked against our scripts.
- Ruling (Wendell, 2026-10-14 22:15, overruling the first draft): "Overrule the rigging spirit skeletons first. What it buys is a good operational foundation and we ARE going to be using the rigs in the cave forms of these sprites emerging." Spirits are rigged skeleton first, and the rigs go into the cave forms.
- Position (stands unless he flips it): one frame, flesh, warp recipe for both strands. The NPC generator for the Chapter 1 demo builds on the humanoid rig we already have, with the warp as a numbers table applied last. The spirits get the same treatment, starting with the Shellback families, whose rig is built before any further look rounds.
- Build, in a fresh thread on Opus, in bars-engine (not on #318's branch, which round 8 is using):
  0. Spirit rig first: a per-family frame (joint table, parent map, weights, one Walk and one Idle), the fused flesh skinned to it, the existing element, nation and base layers as the warp. Not on #318's branch while round 8 runs; it lands as its own module that #318 later imports. The cave forms use these rigs, so the sprite is rendered from the rigged model posed at its sprite angle.
  1. `content/ontology-game/cave/census.py`: loads any GLB, asserts the mesh census (non-manifold edges, loose verts, degenerate faces, size within a stated box). Humanoid figures must pass it; kit-bashed spirits and the chamber only report.
  2. A `WARP` table beside `BUILDS` in `cave/character.py` (limb ratio, head size, spine curve, stoop, one joint collapsed), each row named for a blockage, applied after the fused body and before the weights are painted. The blockage list comes from the ontology; ask the board (`reach_test` first) only if the record cannot map a blockage to a row.
  3. A 12-figure sheet from one frame, each figure one number away, to look at before anything else.

## Built (2026-10-14, bars-engine #325)
- Item 0, the spirit rig: `tools/blender-cloud/content/spirits/rig.py`. A joint table per base and stage (tortoise,
  armadillo, pangolin, fox; creature on four legs, ally form on two, gas, core and hologram on one float bone), the
  cave avatar's joint names, the fused body, cloth and tail weighted per vertex, every other piece on the bone it sits
  on, the aura on the root, Walk (one second) and Idle (two seconds). rig_scene(base, stage) is what shellback.py calls
  before export once #318 lands; until then it rigs an exported GLB. Sheets and four rigged GLBs:
  /mnt/project-files/3d-build/spirit-rig-2026-10-14/.
- Scale declared (`SIZE` in rig.py) and baked in, 1 unit = 1 m: tortoise creature 1.2 m long, armadillo 1.0, pangolin
  0.9, fox 0.75 nose to rump; ally forms 1.4 to 1.5 m tall; gas, core and hologram at their creature's scale.
- Item 1, the census: `content/ontology-game/cave/census.py`, plain Python. J4, J5 and the body map figure pass (closed,
  0 degenerate); spirits and the chamber report. Tests C1 (offline) and S1 (bpy, skips until shellback.py is on main).
- Position (stands unless he flips it): the WARP rows in item 2 are named for the seven daemons (Controller, Damaged
  Self, Emotional Body, Fixer, Protector, Skeptic, Victim), since the record already maps a blockage to a daemon and a
  daemon to a spirit family (sg-body-from, ch1-npc-from-blockage). No board question needed.

## Next thread (Opus, fresh): items 2 and 3
- Brief: add `WARP` beside `BUILDS` in bars-engine `content/ontology-game/cave/character.py`, one row per daemon (limb
  ratio, head size, spine curve, stoop, one joint collapsed), applied after the fused body and before the weights;
  every warped figure must pass `census.py --kind humanoid` and J4's walk check. Then the 12-figure sheet from one
  frame, each one number away, to /mnt/project-files/3d-build/. Own bars-engine #325 until it merges (drop the watch
  then), and Six-faces-council #150.

## What we already follow
- Version pinned: `bpy==5.2.2` on Python 3.13 (tools/blender-cloud/README.md). Matches the tweet's current LTS.
- Scale convention: GLB exports 1 unit = 1 m; characters are 1.75 m. Cameras and dims in the cave scripts agree.
- Frame, then flesh: `cave/character.py` starts from the body map's parts with a joint table (`J`), a parent map, fuses the surface, then weights each vertex by nearest part. That is frame and flesh. `BUILDS` is a small warp (three widths).
- Parametric and seeded: `procgen.py` has same seed, same mesh asserts (roots, mushrooms). `character.py` checks the walk's joints per figure.
- Render for a contact sheet, judge by eye: `LOOKED.md`, the sheets in every thread. Cycles on CPU because the cloud has no GPU (the tweet's offscreen EEVEE route needs one).

## Which would fix problems we have had
- Census on outputs. Ran trimesh over exports on 2026-10-14 (vertices merged): the J4 figure is clean (0 non-manifold edges, a volume, 4 degenerate faces). The spirits are 130 to 190 separate parts and 7,000 to 9,000 non-manifold edges each, and the generated chamber GLB has 19,000 and 438 degenerate faces. For sprites that is fine; for a 3D game, solid-looking pieces that are open shells will break any boolean, physics collider or print. Nothing asserts any of it today.
- Scale declared once. The spirits export at about 4 m long (tortoise creature 3.9 m) because they were framed for a sprite camera, and nothing says so. A 3D game would meet them at four times a person.
- Warp as numbers. Spirit variants today are 3 bases by flags and module globals (`SHELL_SQUASH`, `HEAD`, `NECK`) and one process per base. The parametric NPC need is the same shape as the humanoid.
- `--python-exit-code 1`: our scripts run under the bpy wheel, so a traceback already fails the run. It matters only if a build ever shells out to the Blender binary.

## Which do not fit
- (Withdrawn by his ruling: not rigging the spirits first.)
- Banning `bpy.ops` outright. Our metaball bodies (`blob`, `shellback.py`) convert through `bpy.ops.object.convert`, and 68 calls work headless on 5.2.2. Move to bmesh only where a run fails or a mesh needs measuring.
- Printing numbers (overhang, hole size, wall). Not printing anything.
- The Blender MCP servers. We run scripts in a pinned venv; the tweet's own warning about unguarded code applies.
- EXACT booleans, `gpu.init()` offscreen sheets: no booleans in these scripts, and Cycles CPU works.

## Waiting on
- Nothing from Wendell. Items 2 and 3 start in a fresh thread (above).
