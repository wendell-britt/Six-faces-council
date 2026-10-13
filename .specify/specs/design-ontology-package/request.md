# Request: Package the design ontology in Six-faces-council

## The ask

> “the ontology should live in the Six-faces-council repo as the ontology is going to be used by this orchestrator for building and desinging games.”
>
> Wendell, chat, 2026-10-12.

## 3: Face it

The design ontology exists as a complete provisional corpus outside the orchestrator repository. The council already has a Claude Code skill, bounded faces, a feature pipeline, and provenance practices, but it cannot reliably retrieve the ontology during game-design work.

The work helps Wendell as designer first, the council as Game Master orchestrator second, and players of games built through the system third. The desired inner satisfaction is coherence and uncanny precision; the external benefit is that design decisions preserve the same vocabulary, authority boundaries, and aesthetics across sessions.

## 2: Talk to it

No new owner question is required. Wendell selected the repository and purpose. Existing ontology decisions determine the package boundaries. The historical corpus should remain available, but the orchestrator needs a compact current entry point so history does not colonize context.

## 1: Be it

Package the complete source corpus, add a manifest and Quickstart, add an on-demand Claude Code skill, connect the six-face skill to it for game-design passes, and add validation that fails when current sources or integration points are missing.

### Cheap falsification test

A clean reader given only the manifest and Quickstart must be able to distinguish the Basic Moves from WAVE, an intended route from an enacted transformation, encounter ending from quest completion, and recoverability from infallibility. The validator checks those distinctions and every manifest path.
