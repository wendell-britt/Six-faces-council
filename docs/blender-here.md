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
files. It also clones the 22 blender-skills at the version the toolbox lists. From an empty folder: 45 seconds, 1.3 GB, all under `~/blender-here`
(`BLENDER_HERE_ROOT` moves it). The repo holds the scripts, never the install.

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
| `probe` end to end | 36 s | Cheap enough to run at the start of a session. |

Memory is the real ceiling: 1.13 GB peak for a 720p still on a 3 GB box. One Blender at a time, and a scene over
roughly 1.5 GB will swap or die.

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
  out. The rigs and the cave live there, so a look pass on them needs another clone first.
- **bars-engine's `tools/blender-cloud`** itself: `skill_run.py` and `council/tools/blender_report_card.py` point at
  `/home/user/bars-engine` and a `blenv` Python that this VM does not have. The skills run directly here instead,
  which is how the numbers above were taken.

## What it is good for

Stills and contact sheets for look review; building and fixing meshes from script; rigging with Rigify and skinning;
cloth bakes to shape keys; QA and glTF export for the web build; the research and reading that would otherwise spend
Claude tokens. Animation, EEVEE renders and any GPU generation stay where they were.

scout: rung 3, we have it (Blender 5.2.2 plus the vendored blender-skills; nothing new was needed).
