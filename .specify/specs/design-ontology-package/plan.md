# Plan: Design ontology package

## Approach

Preserve the exported ontology unchanged beneath a versioned source directory. Put a small manifest, Quickstart, and skill in front of it so Claude Code loads only the material required for the current task. Connect that skill to the existing council workflow instead of duplicating the six faces.

## Files touched

| File | Change |
|---|---|
| `ontology/manifest.yaml` | Package version, authority, task profiles, compatibility, validation |
| `ontology/v0.1/QUICKSTART.md` | Compact current ontology |
| `ontology/v0.1/source/` | Preserved exported corpus |
| `.claude/skills/design-ontology/SKILL.md` | On-demand Claude Code adapter |
| `.claude/skills/six-faces/SKILL.md` | Game-design integration |
| `CLAUDE.md` and `README.md` | Discovery pointers |
| `tests/test_design_ontology.py` | Package and semantic checks |

## Order

1. Copy the corpus without rewriting its provenance.
2. Add manifest and compact current view.
3. Add the ontology skill and connect the council.
4. Add and run validation.
5. Commit, push, and open the pull request.

## What Wendell does, and when

Nothing. Wendell already selected the repository and purpose.
