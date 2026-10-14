# Blender: frame, flesh, warp (parametric creatures and NPCs)

## Next
- Source: a tweet Wendell shared 2026-10-14 (skeleton first, then flesh, then warp; headless Blender practice). Its numbers (benchmark scores, who built it) are unverified; the practice is sound on its own and was checked against our scripts.
- Position (stands unless he flips it): build the NPC generator for the Chapter 1 demo on the humanoid rig we already have, and add the warp as a numbers table applied last. Do not start with the spirit generator, which is sprite art and has no rig.
- Build, in a fresh thread on Opus, in bars-engine (not on #318's branch, which round 8 is using):
  1. `content/ontology-game/cave/census.py`: loads any GLB, asserts the mesh census (non-manifold edges, loose verts, degenerate faces, size within a stated box). Humanoid figures must pass it; kit-bashed spirits and the chamber only report.
  2. A `WARP` table beside `BUILDS` in `cave/character.py` (limb ratio, head size, spine curve, stoop, one joint collapsed), each row named for a blockage, applied after the fused body and before the weights are painted. The blockage list comes from the ontology; ask the board (`reach_test` first) only if the record cannot map a blockage to a row.
  3. A 12-figure sheet from one frame, each figure one number away, to look at before anything else.

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
- Rig the spirits skeleton first. They are static meshes rendered to a 96 px sprite; a rig buys nothing until the 3D game wants them walking (`sg-assets-modular` says one rig per family with sockets, which is later).
- Banning `bpy.ops` outright. Our metaball bodies (`blob`, `shellback.py`) convert through `bpy.ops.object.convert`, and 68 calls work headless on 5.2.2. Move to bmesh only where a run fails or a mesh needs measuring.
- Printing numbers (overhang, hole size, wall). Not printing anything.
- The Blender MCP servers. We run scripts in a pinned venv; the tweet's own warning about unguarded code applies.
- EXACT booleans, `gpu.init()` offscreen sheets: no booleans in these scripts, and Cycles CPU works.

## Waiting on
- Nothing from Wendell. Start the build when a thread is free; it does not touch #318.
