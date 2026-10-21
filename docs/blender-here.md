# Blender on this cloud VM, measured (2026-10-21)

The question: when Claude tokens run out, can the Blender work carry on here? Answer: the asset half of it can, on
stills and mesh work; the GPU half cannot, and nothing in between is worth pretending.

This VM is 2 vCPU, 3 GB of RAM, no GPU, Ubuntu 24.04 with glibc 2.39 and about 10 GB of disk, with no root. The
bars-engine pipeline (`tools/blender-cloud`) ran in a container with a GPU, so its timings say nothing about this
machine. Every number below was measured here, on 2026-10-21.

## Setup, in one command

```
python3 council/tools/blender_here.py setup
python3 council/tools/blender_here.py probe
```

`setup` downloads Blender 5.2.2 LTS (the version the council's skills are built for), unpacks it, and finds whatever
shared libraries the binary is missing by asking `ldd`. On this image there are six (libxrender1, libxfixes3, libxi6,
libxkbcommon0, libsm6, libice6); their Ubuntu packages are downloaded and unpacked into
`~/blender-here/sysroot`, which `LD_LIBRARY_PATH` then points at. None of this needs root or touches the system's own
files. It also clones the 22 blender-skills at the version the toolbox lists. From an empty folder: 1m22s and 1.2 GB
on 2026-10-21, the download taking most of it (the same run took 45 seconds that morning on a faster link), all under
`~/blender-here` (`BLENDER_HERE_ROOT` moves it). The repo holds the scripts; the install lives under the home folder.
Each session starts from an empty home folder, so this is the first minute of every asset session.

`probe` runs `council/tools/blender_probe.py` inside Blender plus the upstream skill test suite, prints the numbers
below as JSON, writes them to `~/blender-here/measure.json` and exits non-zero on a failed step. Run it again after a
restore: this VM's home folder is not promised to survive, and 45 seconds buys it back.

## What the numbers say

| Step | Measured | What it means |
|---|---|---|
| Blender | 5.2.2 LTS, bundled Python 3.13.13 | The same major version as the council's `bpy` work; the pip `bpy` wheel wants Python 3.13 and this image has 3.12, so the tarball is the route here. |
| Cycles still, 480x270, 32 spp, denoised | 7.0 s, 109 KB PNG | A contact-sheet tile every seven seconds. |
| Cycles still, 1280x720, 48 spp, denoised, one lit character | 41 s, 799 KB PNG, 1.13 GB peak RSS | Look-review stills are affordable; see the memory line below before running two at once. |
| glTF export, web preset | 1.1 s, 418 KB for 29,460 tris, one skin, `EXT_meshopt_compression` | The export path the game uses works, meshopt included. |
| Rigify, basic human metarig, fitted | 159 bone metarig to 706 bone rig in 5 s; 307 KB rig GLB | The rig work J4 needed is here. |
| Auto-skin (bone heat), 14,732 verts | 3.3 s, 35 groups, 0 unweighted verts, 4 influences max | Skinning a generated or imported body is a few seconds. |
| Cloth bake, 441-vert sheet, 30 frames | 0.1 s, falls 3.07 m | Robe and sleeve cloth bakes at this size are free; the J5 rounds were 20x20 grids and up. |
| Asset QA (game profile) | ran, and failed my crude probe body: 2 coplanar tri pairs, 98.6% UV overlap, lowest point below ground | The QA gate finds real faults, so it is worth running even when nothing looks wrong. |
| blender-skills suite | 47 passed, 0 failed, 3 skipped (they need a GPU), 19 s | The vendored skills run on this Blender version, unchanged. |
| Composed garment job: figure, auto-skinned, pinned panel, cloth, glTF | 0.7 s of sim after build, 625-vert panel, 95 KB GLB, 466 MB peak RSS, 0 points through the body over 24 keys, hem still moving 77 mm at key 24 | A job shaped like a J5 round fits on this box comfortably. The sim window is the limit: 24 keys is too short for this panel to hang. |
| `probe` end to end | 40 s, seven steps | Cheap enough to run at the start of a session. |

Memory is the real ceiling: 1.13 GB peak for a 720p still on a 3 GB box, 466 MB for the composed garment job. One
Blender at a time, and a scene over roughly 1.5 GB will swap or die.

## The measurement trap the garment step found

The first version of the composed step read the garment's evaluated vertices in its own local space and got a clean
pass: 0 points through the body, a 0.05 m hem drop. Both numbers were meaningless, because the panel is rotated 90
degrees about X, so a local reading measures a panel lying flat at the origin while the screen shows one hanging off a
figure. Reading through `matrix_world` turned the same scene into 2.02 m of slide on an unpinned panel and 0 points
through, and the pin then held it. A probe that reports a pass on the wrong coordinate space is worse than no probe:
it certifies work nobody did. Check any Blender number against `matrix_world` before trusting it.

## What does not work here

- **EEVEE.** It needs a GPU context. Mesa's software EGL failed with `EGL_BAD_PARAMETER` and then a segfault, so the
  fast engine for stylised looks is out and Cycles is the only renderer.
- **Animation at volume.** At 41 s a frame, ten seconds at 30 fps is about three and a half hours of CPU, without a
  re-render for a changed light. Short turntables at 480p are the honest format here.
- **Blenderkit.** Its API needs Wendell's key, which is not on this box, and its library is downloadable but the
  session-wide `blenderkit` add-on wiring lives in bars-engine. Polyhaven's API answers (CC0) and is the fallback
  that needs no key.
- **Image-to-3D.** AssetFurnace rents a GPU elsewhere; that channel does not move here.
- **The game's own assets.** This clone has no `.blend`, `.glb` or `.fbx`, and bars-engine and sprout are not checked
  out. The rigs, the garments and the cave live there, so a J5 round cannot run here yet. Unblock: bars-engine
  connected to this account's GitHub integration (read access is enough for the source) or a checkout in the VM. A J5
  run needs `content/ontology-game/cave/character.py`, `garments.py` and `cloth.js`, the body and stance data they
  read, and `tools/blender-cloud/tests` for the J4/J5 checks. The composed step above is the same shape built from
  primitives, and it runs in under a second, so the missing piece is the checkout.
- **bars-engine's `tools/blender-cloud`** itself: `skill_run.py` and `council/tools/blender_report_card.py` point at
  `/home/user/bars-engine` and a `blenv` Python that this VM does not have. The skills run directly here instead,
  which is how the numbers above were taken.

## What it is good for

Stills and contact sheets for look review; building and fixing meshes from script; rigging with Rigify and skinning;
cloth bakes to shape keys; a pinned garment on a skinned figure exported to glTF; QA and glTF export for the web
build; the research and reading that would otherwise spend Claude tokens. Animation, EEVEE renders and any GPU
generation stay where they were.

scout: rung 3, we have it (Blender 5.2.2 plus the vendored blender-skills; nothing new was needed). The composed
garment step is rung 2: `blender-skills` is already vendored, with `blender-cloth-bake` and `rigify` beside it, so this
job is composition in `council/tools/blender_probe.py`; no new tool was needed.
