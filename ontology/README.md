# Wendell's Design Ontology

This directory is the canonical home of the design ontology used by the Six Faces council when it designs and builds games.

Start with:

1. [`manifest.yaml`](manifest.yaml) for version, authority, source status, compatibility, and task-specific load profiles;
2. [`v0.1/QUICKSTART.md`](v0.1/QUICKSTART.md) for compact current context;
3. [the Claude Code skill](../.claude/skills/design-ontology/SKILL.md) for the application workflow.

`v0.1/source/` preserves the complete exported research, philosophy, formal model, council ingestion, crosswalks, decisions, and process log. It is provenance, not default context. Load it through the manifest so historical or superseded language does not silently replace current decisions.

Version `0.1.0-alpha.1` is provisional. It can guide real game-design work while remaining corrigible through evidence, council deliberation, play, and Wendell's rulings.

## Install and verify

This alpha is repo-local: check out the repository at the release commit and run commands from its root. No global plugin installation is required.

```sh
python3 ontology/tools/validate_package.py
python3 -m unittest discover -s tests -p 'test_*.py'
```

For a design task, select a load profile in `manifest.yaml`, read the Quickstart, and invoke the relevant face agent with a caller-supplied I Ching cast. Produce a cast with `python3 council/iching/cast.py shaman`, replacing `shaman` with the selected face. The face agents are deliberately read-only and have no shell capability.

## Update and compatibility

Pull or check out a newer tagged release, rerun both verification commands, and review the manifest's `compatibility`, `binding_decisions`, and `historical_material` rules before accepting changed behavior. Historical detail never outranks a current or binding manifest route.

See [`v0.1/RELEASE.md`](v0.1/RELEASE.md) for the tested environment, release gate, and known gaps.
