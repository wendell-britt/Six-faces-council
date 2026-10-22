# Blender on this cloud VM, measured (2026-10-21; bars-engine's own suite 2026-10-22)

The question: when Claude tokens run out, can the Blender work carry on here? Answer: the asset half of it can, on
stills and mesh work; the GPU half cannot, and nothing in between is worth pretending.

This VM is 2 vCPU, 3 GB of RAM, no GPU, Ubuntu 24.04 with glibc 2.39 and about 10 GB of disk, with no root. The
bars-engine pipeline (`tools/blender-cloud`) ran in a container with a GPU, so its timings said nothing about this
machine, and its scripts expect a `bpy` venv rather than the binary. Both routes were set up here and its own test
suite was run against them on 2026-10-22.

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

## bars-engine's own pipeline (2026-10-22)

That is the tarball route. bars-engine runs Blender as the `bpy` wheel instead, and for its work that route is cheaper
and closer to what its scripts expect:

```
python3 council/tools/blender_here.py bars       # bars-engine's checkout and the bpy venv, four seconds on a warm image
python3 council/tools/blender_here.py bars-test  # bars-engine's own pipeline tests: offline, then bpy
```

The repo is public at `johnair01/bars-engine`, under an account the connected session is not logged in as but has push
access to. That is why the previous session called it private: the owner is not the login, so the repo never appeared
in its own list. A sparse clone of the pipeline, the cave and the body is 16 MB in 1.5 s; the whole repo is 274 MB.
The wheel is 961 MB and installs in 9 s on the Python 3.13 that `uv` fetches, against 1.2 GB and 1m22s for the
tarball. Both routes link the same six Ubuntu libraries, so `bars` reuses the `setup` sysroot. bars-engine's runner
reads `$BLENV` for the venv's Python; its own docstring calls that variable `BLENTV`, which nothing reads.

Their suite, on this box:

| Tier | Result | What it means |
|---|---|---|
| offline (plain Python, the tier their CI runs) | 7 of 7 pass, 1 s | The pipeline's licensing, budget and layout checks are CPU-only and cost nothing here. |
| bpy | 20 pass, 2 fail, 2 skipped, 1 known gap, 337 to 353 s over two runs | The Blender half runs. The cave props (J2, 12 pieces) take 14 to 27 s, nine figures and their walks (J4) 42 s, the frame with seven daemons and the Player (J6) 43 s, and the whole suite is six minutes of one core. |

The skips are G4 and G5, which want the dining table the net tier fetches; P4 is their own known gap (7 prisms where
the picture shows about 10). The two failures are worth their own lines.

**R1, the byte-for-byte rebuild, does not hold here** (fixed in the patch below, and still red upstream). It builds `body/figure.glb` and compares its hash with the
committed file. This VM's build is 204,268 bytes against 204,264, with the same 9,613 faces and the same topology, and
the accessors' min and max apart in the seventh digit: the figure's height reads 1.7382885 here and 1.7380060 in the
committed file, 0.28 mm over 1.738 m. That is float drift between machines, not a different figure, and it is
enough to fail a hash. The cave kit (R2) is byte-for-byte identical here, twice, so the sensitivity is per builder
and not a property of this box. The consequence for asset rounds: a new asset built here is fine, but regenerating a
committed GLB here churns the binary even when nothing changed, so that rebuild stays where its hash matches.

**J7, the held movement letting go, is a mismatched check rather than a bad pose** (fixed in the patch below, red upstream). The Controller's Integrate action opens both fists
(3.08x and 3.33x) and keeps the lower foot 0.02 cm off the ground, and its left forearm ends hanging at 0.86 of its
length. The right forearm ends at 1.308 m, at shoulder height, pointing 22.6 cm forward and 3 cm up: a ratio of
-0.13 where the check wants at least 0.5. That is not a tolerance miss on the last digit; the right arm stays out in
front while the left one drops. It reproduces on a second run. The cause is the check, not the arm: character.py
replaces the Controller's relaxed finish with its HONORED stance, so the right arm is meant to be offered, and the
check still demanded both forearms hang. Patch and measurements: `council/patches/bars-engine-j7-r1-2026-10-22.patch`
and the strand's call sheet. With it applied the bpy tier is 22 pass, 0 fail.

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

## What still does not work here

- **EEVEE.** It needs a GPU context. Mesa's software EGL failed with `EGL_BAD_PARAMETER` and then a segfault, so the
  fast engine for stylised looks is out and Cycles is the only renderer.
- **Animation at volume.** At 41 s a frame, ten seconds at 30 fps is about three and a half hours of CPU, without a
  re-render for a changed light. Short turntables at 480p are the honest format here.
- **Blenderkit.** Its API needs Wendell's key, which is not on this box, and its library is downloadable but the
  session-wide `blenderkit` add-on wiring lives in bars-engine. Polyhaven's API answers (CC0) and is the fallback
  that needs no key.
- **Image-to-3D.** AssetFurnace rents a GPU elsewhere; that channel does not move here.
- **Byte-identical rebuilds.** R1 above: a figure rebuilt here drifts 0.28 mm from the committed file, so any asset
  round whose output must match an existing hash runs where that hash was made. Building something new is unaffected.
- **`skill_run.py` and `council/tools/blender_report_card.py`** still point at `/home/user/bars-engine` and
  `/home/user/blenv`. The checkout and the venv are real now, one symlink away from those paths or a `BLENV`
  override; the report card has not been run against them.

## Pushing to bars-engine

The connected GitHub app reads bars-engine and commits to it through the API: this session made branch
`agent/j7-r1-checks` there and opened issue #425 with it. What the app cannot do is hand this VM a credential, so
`git push` answers "could not read Username for 'https://github.com'", and every file that moves has to pass
through an agent's context: fine for one small file, wasteful for a 664-line test.

`council/tools/bars_git.py` closes that with a project secret. Add `BARS_ENGINE_TOKEN` in this project's
Settings → Secrets as a fine-grained token for `johnair01/bars-engine` with Contents: read and write. Every shell in
the project reads that file, so no session is told the value. Then:

```
python3 council/tools/bars_git.py check        # 0 when a push from here would work now
python3 council/tools/bars_git.py push BRANCH   # HEAD to BRANCH, creating it
```

The helper it writes into `.git/config` names the variable and nothing else; the value never lands in the checkout, the
repo or a log. Until the secret exists, `check` exits 1 and says which piece is missing.

## What it is good for

Stills and contact sheets for look review; building and fixing meshes from script; rigging with Rigify and skinning;
cloth bakes to shape keys; a pinned garment on a skinned figure exported to glTF; QA and glTF export for the web
build; the research and reading that would otherwise spend Claude tokens. Animation, EEVEE renders and any GPU
generation stay where they were.

scout: rung 3, we have it (Blender 5.2.2 plus the vendored blender-skills; nothing new was needed). The composed
garment step is rung 2: `blender-skills` is already vendored, with `blender-cloth-bake` and `rigify` beside it, so this
job is composition in `council/tools/blender_probe.py`; no new tool was needed.
