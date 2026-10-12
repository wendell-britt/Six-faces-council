2026-10-12
# Cave studio (Blender in the cloud for the cave, battle fr-cave-studio)

## Next
Round 1 is on the board: questions `cs-chatgpt-ai-art`, `cs-first-piece`, `cs-asset-kind` and eight standing positions
(`cs-*`). Two steps are on Your steps under "Cave studio" (Drive folder, optional Blendkit check, due 2026-10-19).
When he answers, record his turns under Round 1 in bars-engine `.specify/specs/cave-studio/request.md`, then build the first
piece (spec.md, plan.md, tasks.md beside it). The spec kit is written on bars-engine branch `claude/vibrant-tesla-3brtry` and
is committed once PR #281 merges. If it already merged, restart the branch from main and commit `.specify/specs/cave-studio/`.

## Waiting on
His three answers. The first piece waits on `cs-first-piece` only; ChatGPT art waits on `cs-chatgpt-ai-art` and `cs-asset-kind`.

## Files
- bars-engine `.specify/specs/cave-studio/` (request, spec, plan, tasks); `tools/blender-cloud/` (PR #281);
  `.specify/specs/blender-cloud-hardening/`
- ledger `2026-10-12-feature-request-cave-studio-round-1.json`
- Falsification test, passed 2026-10-12: `build_figure.py` and `build_kit.py` rebuild `figure.glb`, `cave-kit.glb` and
  `spots.json` byte for byte in the cloud (about 6 seconds).
- See cave-of-lessons.md and big-mind-cave.md (the two caves), studio.md (the pipeline they sit in).

## Archive
Nothing is archived yet.
