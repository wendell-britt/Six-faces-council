# Spec: Design ontology package

## The ask

> “the ontology should live in the Six-faces-council repo as the ontology is going to be used by this orchestrator for building and desinging games.”
>
> Wendell, chat, 2026-10-12.

**Who it is for:** Wendell and the Six Faces council while designing and building games.

**What should change:** The council moves from relying on conversation history and cross-repo discovery to a versioned, intentionally loaded ontology package.

## Purpose

Make the provisional design ontology a first-class dependency of the Six Faces game-design orchestrator without forcing its complete research history into every Claude Code turn.

## User stories

### Design with the ontology

**As the council**, I want a task-routed ontology skill so game-design work uses current terms, authority rules, and evidence boundaries.

**Acceptance:** A Claude Code session can find the ontology from project instructions, load a compact current view, and follow deeper references appropriate to the task.

### Preserve the excavation

**As Wendell**, I want the full source and council history retained so later revisions can show how the ontology evolved.

**Acceptance:** The copied corpus is complete and historical records are explicitly prevented from silently overruling current decisions.

## Design decisions

| Decision | Choice | Whose |
|---|---|---|
| Repository | `wendell-britt/Six-faces-council` | Wendell, chat, 2026-10-12 |
| Loading | Compact Quickstart plus task profiles; archive on demand | Ontology context-cost principle and Claude Code skill model |
| History | Preserve the complete output corpus under the version | Constitutional lineage and provenance invariants |
| Council use | Six-face game-design passes load the ontology skill | Wendell's stated orchestrator purpose |
| Release | `0.1.0-alpha.1`, explicitly provisional | Shipping-readiness assessment |

## Contracts

- `ontology/manifest.yaml` is the package router and authority manifest.
- `ontology/v0.1/QUICKSTART.md` is the compact common context.
- `ontology/v0.1/source/` preserves the complete exported corpus.
- `.claude/skills/design-ontology/SKILL.md` is the Claude Code entry point.
- `tests/test_design_ontology.py` validates the package and orchestrator integration.

## Reserved items

No new reserved decision. The work copies and operationalizes rulings Wendell already made; it does not change `council/faces.yaml`.

## How we will know it failed

- **Cheap test:** validate every manifest path and the canonical distinctions in the Quickstart.
- **Stop condition:** the package requires loading the full archive for an ordinary game-design task, or a test cannot distinguish current canon from historical language.

## Definition of done

- [x] Complete ontology source corpus is in the repository.
- [x] Manifest, Quickstart, and Claude Code skill are present.
- [x] The six-face skill invokes the ontology for game design and building.
- [x] Automated tests pass.
- [x] Branch is pushed and pull request #93 is attached.
