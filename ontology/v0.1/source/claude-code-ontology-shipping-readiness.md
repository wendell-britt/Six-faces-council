# Claude Code Shipping Readiness — Design Ontology v0.1

**Assessment date:** 2026-10-12
**Target:** A repo-local Claude Code package that can teach agents the ontology, route work through it, run the six Game Master lenses, preserve provenance, and detect major misuse
**Assessment:** The ontology is **usable as supplied context now**, but is **not yet a dependable installable package**.

## Executive assessment

There are three different meanings of “shippable”:

| Target | Current readiness | Meaning |
|---|---:|---|
| Manual context handoff | **85%** | A person can point Claude at the brief, philosophy, model, YAML, and decisions and get useful work now |
| Repo-local Claude Code alpha | **55%** | The corpus is strong, but it lacks a compact loader, task routing, dedicated six-face agent definitions, and executable checks |
| Reusable cross-project package/plugin | **30%** | No manifest, installation path, release bundle, compatibility contract, or automated evaluation suite exists yet |

These percentages measure packaging and reliability, not philosophical completeness. The ontology can ship provisionally while later authority questions remain open, provided those questions are represented as unresolved rather than silently answered.

## What is already strong

### Canonical content

- provisional fifteen-principle constitution with preserved eight-principle lineage;
- designer psychograph and intended near-neighbor audience hypothesis;
- AQAL, Emotional Alchemy, Octalysis, somatics, BAR lifecycle, and provenance framing;
- entity, relationship, evidence, confidence, lifecycle, and invariant models;
- explicit separation of personal meaning, observable behavior, relational evidence, and systemic consequence;
- resolved terminology for Basic Moves, WAVE, within-channel progression, and the fifteen-move grammar;
- resolved encounter/completion, tension-representation, derived-movement, and Yellow Brick Road boundaries;
- six-face ingestion and cross-environment comparison records;
- machine-readable YAML that parses successfully.

### Existing Claude Code substrate in BARS

The BARS repository already has:

- a project `CLAUDE.md` and `AGENTS.md`;
- `.agents/skills/` with reusable workflows and reference skills;
- `.claude/settings.json` and a SessionStart hook configuration;
- established spec, verification, and provenance workflows;
- local Emotional Alchemy and Game Master context files.

This means the ontology does not need a new agent platform. It needs a disciplined adapter into the existing one.

## What prevents dependable shipping

### 1. No compact canonical entry point — blocking

The core package is spread across more than 149 KB of major documents before the individual council records are loaded. A coding agent should not ingest all of this on every request.

Needed:

- a short always-loaded router stating the constitutional rules, hard invariants, canonical vocabulary, and when to load deeper references;
- a manifest naming current, historical, superseded, unresolved, and implementation-only sources;
- task-specific retrieval paths.

### 2. The ontology is not yet a Claude Code skill — blocking

Needed repo-local structure:

```text
.claude/skills/design-ontology/
  SKILL.md
  references/
    constitution.md
    vocabulary.md
    evidence-authority.md
    emotional-alchemy.md
    lifecycle.md
    adaptive-systems.md
    decisions/
```

The skill should load only when a task involves game design, ontology decisions, AI adaptation, player modeling, Emotional Alchemy, council deliberation, or interpretation of BARS mechanics.

### 3. No executable ontology manifest — blocking

The YAML is a useful vocabulary seed, but it is not yet a release manifest. It needs:

- schema version;
- package version;
- source authority and status;
- supersession and compatibility aliases;
- unresolved-decision registry;
- required references per task class;
- validation rules;
- changelog and migration notes.

### 4. Six-face records are not six Claude Code agents — blocking for council use

The council has intellectual content but no project-level `.claude/agents/` definitions binding each face to:

- its bounded lens and predictable losses;
- required ontology skill preload;
- evidence obligations;
- forbidden authority claims;
- output schema;
- handoff to Sage synthesis;
- rule that convergence is not empirical truth.

The orchestrator itself also needs a defined deliberation protocol: parallel independent readings, preserved disagreement, synthesis, decision jurisdiction, and escalation only for irreducible owner authority.

### 5. No comprehension or regression suite — blocking

The reconciliation already contains good test prompts, but they are prose. They need fixtures and expected assertions covering at least:

- face namespace separation;
- Basic Moves/WAVE/within-channel/fifteen-move separation;
- player satisfaction versus external helpfulness;
- moves resolve / encounters end / quests complete / arcs conclude;
- Tension Map versus TransformationTrace;
- proposal versus actual movement;
- Yellow Brick Road recoverability without self-sealing claims;
- type is not level;
- access is not command;
- no silent conversion of AI inference into player belief;
- correction and provenance propagation.

### 6. Canonical and historical material are intermingled — high priority

Older council records correctly preserve superseded language as provenance. Without retrieval rules, Claude may quote those records as current canon. The shipping package needs positive source selection, not merely warnings inside long documents.

### 7. Open authority questions are not machine-routable — high priority

Unresolved questions may remain in v0.1, but each needs:

- stable id;
- current status;
- sources in tension;
- what agents may do provisionally;
- what they must not assume;
- decision authority;
- tests or evidence that could advance it.

### 8. Existing Claude integration needs cleanup — medium priority

The BARS `CLAUDE.md` is already approximately at the recommended upper size boundary. The ontology should be loaded on demand rather than pasted into it.

The repository contains a script intended to mirror `.agents/skills/` into `.claude/skills/`, but the inspected `.claude/settings.json` SessionStart entry currently invokes a different setup script. Before relying on skill discovery, the installation path must be verified end to end.

### 9. Privacy rules are doctrine, not enforcement — medium priority for design work; blocking for player-data workflows

Claude can follow the privacy distinctions as instructions, but instructions alone do not enforce collection, persistence, sharing, or model-use boundaries. Any workflow touching actual player data needs technical permission gates, redaction behavior, and lineage-aware deletion outside the ontology prompt.

## Minimum viable Claude Code v0.1

A shippable repo-local alpha requires these deliverables:

1. **Ontology manifest** — current sources, statuses, versions, aliases, unresolved questions.
2. **Design ontology skill** — compact loader plus routed reference files.
3. **Six face agent definitions** — bounded lenses with a shared output contract.
4. **Council orchestrator skill** — independent deliberation, synthesis, disagreement preservation, and authority routing.
5. **Validation script** — schema, link, duplicate-id, supersession, and forbidden-term checks.
6. **Comprehension fixtures** — representative prompts with machine-checkable assertions.
7. **BARS adapter** — maps existing terms and files to ontology concepts without rewriting implementation history.
8. **Installation verification** — start Claude Code in a clean session and prove the correct skill and agents are discoverable.
9. **Release notes** — known gaps, provisional decisions, non-goals, and migration boundaries.

## Recommended three-pass path

### Pass 1 — Package the knowledge

- freeze the current ontology as `0.1.0-alpha.1`;
- create manifest and changelog;
- split the large corpus into routed reference modules;
- create the design-ontology skill and a concise project-memory pointer;
- label historical records so retrieval cannot mistake them for current canon.

**Exit condition:** One Claude session can load the ontology intentionally and accurately restate its current boundaries without reading the entire history.

### Pass 2 — Make the council executable

- define the six face agents;
- define their shared response schema;
- create the council orchestration skill;
- encode decision jurisdiction and the no-unnecessary-escalation rule;
- preserve minority reports and source citations.

**Exit condition:** The same design problem can be deliberated twice with recognizable face distinctions, preserved disagreement, and a synthesis that does not invent owner beliefs.

### Pass 3 — Verify and release

- turn comprehension tests into fixtures;
- add validators for YAML, links, ids, aliases, supersession, and terminology;
- run clean-session and context-compaction tests;
- test at least one real design task and one adversarial ambiguity task;
- produce installation and update instructions.

**Exit condition:** A clean Claude Code checkout can install, discover, use, and test the ontology without relying on this conversation.

## Not required before alpha shipping

- resolving every remaining philosophical or governance question;
- migrating BARS runtime schemas;
- implementing every privacy permission in product code when no real player data is used;
- reducing the full ontology to active/reference/compost governance sets;
- turning the ontology into an MCP server;
- publishing a cross-project plugin.

## Release recommendation

The next milestone should be **repo-local `0.1.0-alpha.1`**, not a universal plugin. The existing corpus is mature enough to package, and packaging it now will expose ambiguities through actual use. A plugin becomes appropriate after the repo-local skill, six agents, and evaluation fixtures survive at least one ontology-guided design cycle and one revision cycle.

## Claude Code packaging basis

This recommendation follows the current Claude Code extension model:

- [`CLAUDE.md` provides persistent project context](https://code.claude.com/docs/en/memory);
- [skills provide on-demand knowledge and reusable workflows](https://code.claude.com/docs/en/skills);
- [subagents provide isolated specialist contexts](https://code.claude.com/docs/en/sub-agents);
- [hooks provide deterministic lifecycle enforcement](https://code.claude.com/docs/en/hooks);
- [plugins are the later packaging layer for reuse across repositories](https://code.claude.com/docs/en/features-overview).
