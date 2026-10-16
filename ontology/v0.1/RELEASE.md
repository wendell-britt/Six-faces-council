# Design ontology 0.1.0-alpha.1 release record

**Release status:** verified candidate; ready to tag after repository checks

**Candidate verification date:** 2026-10-15

**Verification base:** `7024722` (clean worktree from `origin/main`)

## What is usable now

The repo-local package has a manifest, compact Quickstart, routed source corpus, design-ontology skill, Six Faces integration, six explicit read-only face agents, a shared response and authority contract, and thirteen adversarial fixtures covering FC-01 through FC-14.

It is suitable for ontology-guided fictional game design and council review when the operator supplies the selected manifest profile, bounded question, evidence scope, Player, reserved matters, and caller-side I Ching cast.

## Verified environment

- macOS host, zsh, Python 3.14
- clean Git worktree created from `origin/main`
- package validator: pass
- complete repository suite in the CI-declared dependency environment: 84 tests pass, 1 skipped, 24 subtests pass
- face-output contract voice lint: zero hard findings on the merged hardening content
- two authenticated, non-persistent Claude Code councils: pass
- clean-council semantic validator: pass

The clean worktree found and validated the manifest, skill route, six agent definitions, contract, source links, YAML documents, compatibility aliases, historical-source precedence, and adversarial fixture coverage without relying on uncommitted files.

## Behavioral verification

Two independent councils ran from the clean worktree with fresh, non-persistent Claude Code sessions. Each round independently invoked Shaman, Architect, Challenger, Regent, and Diplomat with caller-supplied casts, then passed their unedited reports to Sage.

Both rounds preserved their casts and required headings, produced recognizable face distinctions, covered every scenario-relevant forbidden collapse, retained dissent, and gave bounded verdicts. Both Sage reports accounted for every face, applied the reach test, marked convergence as a flag rather than proof, and recommended without deciding. Raw reports are preserved in `council/passes/ontology-alpha-clean-councils-2026-10-15.json` and checked by `ontology/tools/validate_clean_councils.py`.

## Known gaps and non-goals

- The clean runs tested the Roadblock Encounter rather than executing every adversarial fixture through a live model.
- Forced context compaction was not tested because non-persistent print mode exposes no deterministic compaction trigger; this remains a post-alpha durability test.
- This alpha does not technically enforce permissions for real player data. Use fictional or synthetic material until product-level controls exist.
- Phase B active/reference/compost sorting is not authorized.
- This is not yet a reusable cross-project plugin or MCP server.
- Open authority questions remain provisional and follow the manifest's unresolved registry and reach test.

## Release rule

Tag only the exact commit for which the clean-session runs, package validator, full test suite, release record, and repository checks all pass. If behavior differs from this record, update it before tagging.
