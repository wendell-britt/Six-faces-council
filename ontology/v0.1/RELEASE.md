# Design ontology 0.1.0-alpha.1 release record

**Release status:** candidate; tag withheld

**Candidate verification date:** 2026-10-15

**Candidate base:** `7e43221` (merged PR 171)

## What is usable now

The repo-local package has a manifest, compact Quickstart, routed source corpus, design-ontology skill, Six Faces integration, six explicit read-only face agents, a shared response and authority contract, and thirteen adversarial fixtures covering FC-01 through FC-14.

It is suitable for ontology-guided fictional game design and council review when the operator supplies the selected manifest profile, bounded question, evidence scope, Player, reserved matters, and caller-side I Ching cast.

## Verified environment

- macOS host, zsh, Python 3.14
- clean Git worktree created from `origin/main`
- package validator: pass
- full test suite: 56 tests pass
- face-output contract voice lint: zero hard findings on the merged hardening content

The clean worktree found and validated the manifest, skill route, six agent definitions, contract, source links, YAML documents, compatibility aliases, historical-source precedence, and adversarial fixture coverage without relying on uncommitted files.

## Open release gate

Fresh Claude Code behavioral execution is not yet verified. The installed `claude` command returned `Not logged in · Please run /login` for each attempted face invocation. Therefore the two independent face-distinction runs, context-compaction behavior, and alpha tag are not claimed.

After Claude Code is authenticated, run the same bounded Roadblock Encounter through Shaman, Architect, Challenger, Regent, and Diplomat independently with caller-supplied casts, then give all five unedited reports to Sage. Repeat from a second fresh session. Preserve verdicts and dissent seeds, and confirm Sage recommends without deciding.

## Known gaps and non-goals

- Fixtures are machine-checkable semantic contracts; an authenticated model runner has not yet executed them.
- This alpha does not technically enforce permissions for real player data. Use fictional or synthetic material until product-level controls exist.
- Phase B active/reference/compost sorting is not authorized.
- This is not yet a reusable cross-project plugin or MCP server.
- Open authority questions remain provisional and follow the manifest's unresolved registry and reach test.

## Release rule

Tag only the exact commit for which the clean-session runs, package validator, full test suite, release record, and repository checks all pass. If behavior differs from this record, update it before tagging.
