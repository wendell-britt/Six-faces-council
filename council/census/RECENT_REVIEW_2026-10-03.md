# The council's review of the recent branches, 2026-10-03

Wendell ruled at board read 14 that the council reviews each recent unmerged branch and proposes merge or retire. The
Diplomat sent two Fixer daemons on the small model, one per repo. The Diplomat then checked each merge with git's own
merge test against main as it stands tonight. Two daemon claims did not hold, and the corrections are marked.

## flirtcraft

| Branch | What it holds | Merge test against main | Proposal |
|---|---|---|---|
| `claude/front-door-fold` | The storefront: hero on the front page, about, pricing, privacy and terms pages, the founder section Wendell ratified on 2026-09-11, a footer and analytics | **Conflicts** in `lib/useEntitlement.ts` and `package.json`, because main changed both for sign-in and billing | Bring it onto current main as a new strand, keep main's newer sign-in and billing code, and show Wendell a preview before it goes live |
| `claude/storefront` | The same commit as `front-door-fold` | Same | Retire with the line above |
| `claude/founder-panel` | Contained in `front-door-fold` | Same | Retire with the line above |
| `claude/front-door-seo` | A lighter front door with robots and sitemap files, plus 9 commits the fold lacks, among them a hostile review and its seven defects | **Conflicts** in `package.json` | Fold its unique commits into the same strand, then retire it. *Correction: the Fixer called it superseded; it holds 9 commits of its own.* |
| `claude/heycatch-analysis-roadmap-hs6mwa` | 54 commits on the oracle's binds: `lib/binds.json`, new grammar rulings, a spec and a research note | Merges cleanly | Merge after its own checks pass on a preview |

## friendcraft-manuacript

| Branch | What it holds | Merge test against main | Touches the book? | Proposal |
|---|---|---|---|---|
| `claude/friendcraft-manuscript-preproduction-pm7drz` | A hosted version of the exchange, so a friend outside the organization can open it; undeployed, with deployment steps in its README | Merges cleanly | No | Merge |
| `claude/new-session-y0181b` | 33 commits of flirtcraft oracle prose rewrites, 64 reference card images, translation analysis and prose tools | **Conflicts** in the house-voice skill, `tools/voice_lint.py` and the hexagrams spec, because main has newer versions | No | Port the oracle rewrites and images onto current main as a new strand, keeping main's newer voice kit, then retire the branch. *Correction: the Fixer said nothing would be overwritten; three files conflict.* |

## The casts

- Fixer for flirtcraft: hexagram 60, Measure, no changing lines.
- Fixer for friendcraft: hexagram 47, Drained, becoming 29, Depths.
