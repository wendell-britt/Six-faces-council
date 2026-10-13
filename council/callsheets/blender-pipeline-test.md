2026-10-12 (updated 23:50)
# Blender pipeline test plan (strand blender-pipeline-test)

## Next
One fresh thread, one piece of work: write the plan for testing the Blender pipeline. The output is a spec kit in bars-engine,
`.specify/specs/blender-pipeline-test/` (spec.md, plan.md, tasks.md), a draft pull request, and one ledger record. It is a plan only.
The thread builds no tests and changes nothing in the pipeline. Run `python3 council/strands.py` first: the cave-studio strand also
touches `tools/blender-cloud/`, so the plan adds files under a new `tools/blender-cloud/tests/` and leaves existing files alone.

**What the pipeline is on 2026-10-12, 23:50**
- Cloud tools on main (PR #281): `tools/blender-cloud/` with `blenderkit_fetch.py`, `prepare_asset.py`, `scene.py`, `build_viewer.py` and
  `viewer_template.html`. Setup and rules are in its README.
- The picture path, only on bars-engine PR #285 (branch `claude/project-thread-1loob1`, ready, not merged when this was written):
  `from_picture.py` (modes lathe, inflate and crystals, an outline-match score, a render), `content/ontology-game/cave/pictures/`
  and the `DRESSING` table in `build_kit.py`. Plan against main plus #285, and check whether #285 has merged.
- The cave builds: `content/ontology-game/body/build_figure.py`, `cave/build_kit.py`, `cave.js`, `cave-test.mjs` (126 checks at
  390 by 844) and `cave/manifest.json` with its size budgets.
- Two published pages: Cloud Walker https://claude.ai/artifact/SUZYu1w1P5b61Cn6pj7Vwg and the picture comparison page
  https://claude.ai/artifact/568K2pwc7Lz5X9Kyftbzza.

**What has been tested, by hand only** (evidence: ledger `2026-10-12-blender-cloud-session.json` and
`.specify/specs/blender-cloud-hardening/tasks.md`)
- `build_figure.py` and `build_kit.py` rebuild `figure.glb`, `cave-kit.glb` and `spots.json` byte for byte (about 6 seconds).
- The fetch script's `--selftest`; the key header goes only to the API host (checked with a fake value); a 403 prints the API's message.
- Draco decode and import for four CC0 glTFs. A synthetic two-tile UDIM image stops the run. A 617,708-triangle asset went to 25,000
  triangles and 7.3 MB, and the 12 MB size stop fires. A royalty_free sidecar stops `build_viewer.py`.
- The viewer loads in headless Chromium over http: 7 bones, 1,318 triangles, a 2.04 second WalkCycle, no console errors.
- The cave's 126 checks pass on #285.

**What has never been tested** (each is a candidate for the plan)
- Meshopt decoding, a multi-material asset beyond the one 11-texture chair, and a real asset with more than one UDIM tile.
- The fetch script without the sandbox proxy (his optional step `cave-studio-02` asks him to check from his machine).
- The walk cycle's numbers: nobody checked the bone rotations, only the pictures. No glTF validator has been run on any output.
- The published Cloud Walker page and the comparison page opened as private URLs. Neither can be opened from the cloud.
- Time and memory limits on a long run, and the network hosts the pipeline needs (api.blenderkit.com, assets.blenderkit.com,
  the npm registry for the decode step).
- Crystal mode finds six crystals where his picture has about ten (known gap, cave-studio sheet).

**What the plan has to answer**
1. For each test, what it proves and its kill line, as a number or an observable result. The Challenger owns the falsify stage.
2. Which tests run every time and offline (the three stop conditions, the licence gate, the manifest budgets, the byte-for-byte
   rebuilds), which need the network, which need a person's eyes, and which need Wendell.
3. Which outputs must match a stored file exactly and which need a tolerance (renders, scores).
4. The score trap. Outline-only scored 0.88 and looked like a blob; the crystal cluster scored 0.829 and looked right. A test cannot
   rest on the number alone, so say how the render gets looked at.
5. Where the tests live and how a cloud session runs them in one sitting and writes a short summary file. Weigh whether the repo's
   GitHub `check` job should run any of them: installing `bpy` there is heavy.
6. Fixtures. Pin each CC0 asset by its id in the sidecar JSON, since a search index can drift. Ids recorded this session: Chair (stool)
   `94eaeda7-5ef1-44a3-988e-4821002d8650`, Dining table `929d574b-02ed-4b48-ba5b-2ce3214a31d6`, Wooden Chair (617,708 triangles)
   `c8857203-ba76-4d34-9ee7-906293144d4e`. The Painted Wooden Chair 02 id is in its sidecar.

**Rules to carry**
- Questions for Wendell go to the board through the reach test, never to chat. A step only he can take goes on Your steps.
- Do not loosen the CC0 gate. His answer on `cs-cc0-or-own` is in bars-engine `.specify/specs/cave-studio/request.md`.
- Keep the thread short and end it with a call sheet update. A long test run goes in the background and writes a summary file.
- A test never writes a daemon's or a spirit's words, and a test never uses a photograph of a real person.

## Waiting on
The plan needs no answer from Wendell. The only dependency is order: if #285 merges first, plan against main.

## Files
- bars-engine `tools/blender-cloud/` (README), `.specify/specs/blender-cloud-hardening/`, `.specify/specs/cave-studio/`,
  `content/ontology-game/cave/` and `content/ontology-game/body/`
- ledger `2026-10-12-blender-cloud-session.json`; call sheets cave-studio.md and studio.md

## Archive
Nothing is archived yet.
