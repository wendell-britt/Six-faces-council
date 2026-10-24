# Six-face pass: Gameplay Atlas into the design ontology, pass 1 (2026-10-24)

Called by the coordinator for Wendell. His words, 2026-10-24: "Need to study these mechanics and include them as elements of our design ontology. What's a coherent way to do this? Should we go after the 6 faces? As in how would each of the game masters make use of these mechanics?"

First pass on the subject; no tests to grade. Ontology loaded per docs/ontology-in-flows.md (mechanic-design pass): manifest, Quickstart, entity families, Emotional Alchemy, roadblocks, composting, hard invariants. The atlas itself was read by Sonnet workers; this thread read only their files.

Casts (`cast.py --json`, three coins): Shaman 16 Anticipation, becomes 58 Banter. Architect 10 Footing, becomes 6 Divergence. Challenger 19 Spring, no changing lines. Regent 24 Turning, becomes 42 Windfall. Diplomat 64 Almost, becomes 40 Thaw. Sage 45 Gathering, becomes 58 Banter.

## Anchor

The atlas is a field guide of 280 mechanics in 28 systems and 5 families (https://gameplayatlas.loopyhop.com/). We want its mechanics as named, reusable parts of our ontology, so a design thread can reach for "a timing window" or "a care cadence" and know at once what it claims and what our invariants require of it.

## The method (the answer to "what's a coherent way")

1. **Index, not copy.** The atlas states no licence, so we keep a factual index (names, systems, tags, example games, links) and write every description in our own words. `council/research/2026-10-24-gameplay-atlas/atlas-inventory.yaml`.
2. **Read each mechanic through the ontology's rule 5.** "Mechanics claim reality: what a game tracks, rewards, gates, remembers, permits, and changes." Each of the 280 gets its claim in those six verbs, the ontology objects it already instantiates, and a fit: covered, partial, gap or conflict. `crosswalk-a.yaml`, `crosswalk-b.yaml`. Result: 145 covered, 61 partial, 43 gap, 31 conflict.
3. **Then the six faces, on the gaps and conflicts only.** Running six faces over 280 mechanics would cost about 1,700 face-readings and say little the crosswalk does not. The faces earn their cost where the ontology is silent (the gaps) or where a common mechanic breaks one of our invariants (the conflicts). That is this pass.
4. **Land the vocabulary through Codex.** The ontology text is written with Codex (docs/ontology-in-flows.md, "Changes to the ontology itself"), so the additions go as a brief: `docs/codex/mechanic-vocabulary-brief.md`.
5. **Carry it into strands as a line, not a load.** Each strand gets its atlas shortlist in this folder (`shortlists` below); a strand's design thread reads its own shortlist when it designs, and nothing else loads the atlas.

## Six faces

**Shaman (16 Anticipation, becomes 58 Banter: "the exchange is already the whole of it").** The Shaman uses mechanics that hold felt time: the care cadence (farming-growth-care, farming-livestock-care), the rest that refills (survival-fatigue-rest), deliberate silence (narrative-deliberate-silence), on-beat breath (rhythm-cue-response). The Shaman's risk is the conflict list in part a: daily-contact streaks, overdue contracts and hidden debt turn a felt rhythm into a shame clock. Recommendation: keep **Tended Life** as the council's name for a care cadence whose neglect ends in a release (the seed, the letting-go vibeulon), never in blame; spirit-care already plays this way.

**Architect (10 Footing, becomes 6 Divergence: going deeper and pushing forward at once cancels).** The Architect uses the structural parts: **Meter** (merging the workers' ResourceMeter and Capacity Budget: a spendable stock with a ceiling, spend, refill and decay, shown as world state, never a number, per depth-over-flatland), **Timing Window**, **Trigger Chain**, **Loadout**, **Flow Network** (qi moving to vibeulon in Calrunia; power in the living ship) and **Combination with Lineage** (spirits merging, traits passed on with provenance). Risk, from the cast: building all twelve additions at once while also deepening the move ontology. Recommendation: the Codex brief adds the six structural parts as `DesignObject` types with required fields, and leaves move learning to the move ontology (council #364).

**Challenger (19 Spring, no changing lines: this is rising, and the window has an edge).** The Challenger tests the conflicts. Thirty-one atlas mechanics, as usually built, break an invariant: streak resets (rhythm-streak-multiplier), loss on death (progression-death-loses-training, inventory-death-retrieval), standing ladders read as a person's rank (progression-challenge-tiers, relationships-faction-reputation), secrets as leverage (relationships-secrets-leverage), disclosure under a timer (narrative-timed-response). Falsification test: for each conflict the crosswalk names a reshaped version (reset-free streaks, loss leaves a Seed, trust scoped to a domain); a reshaped version fails if a playtester can still lose standing for being away or for refusing. Recommendation: the ontology gains an **atlas reshaping table** as `AntiPattern` entries with their reshaped versions, so no thread rebuilds the shame clock by importing a familiar mechanic.

**Regent (24 Turning, becomes 42 Windfall: what came back is one line deep, and more arrives than you put in).** The Regent holds provenance and licence. The atlas states no licence and says its design levers are editorial analysis, so we keep names and links and our own words, and cite the atlas id on every mechanic we adopt. Definition of done for this subject: the index and crosswalk on main, the Codex brief written, each addition marked "council's word, may be cut" until Wendell or a term pass locks it, and `term_lint.py` clean. Non-negotiable: the atlas never becomes canon by being loaded; it becomes canon only through the brief.

**Diplomat (64 Almost, becomes 40 Thaw: nearly there, care at the last stride).** The Diplomat uses the two-person parts, which Chapter 1's second player and the Between need most: **Turns and Shared Pool** (allocation-snake-order, allocation-public-pick, cooperation-split-information, cooperation-complementary-abilities, narrative-perspective-handoff) and **Delegation** with scope, visibility and revocation. Bridge: the Portland community's allergy to AI means every addition must play without a model; all twelve do, since they are rules, not inference. Risk at the last stride: a bond number (relationships-bond-scenes, relationships-companion-approval) becomes "access is command"; keep trust scoped to a domain and revocable.

**Sage (45 Gathering, becomes 58 Banter: gathered, and may have forgotten why).** Why we came: playable Chapter 1, then the spar and the ship. Synthesis below.

## Verdicts

| Face | Method (index, crosswalk, faces on gaps) | Additions to brief | First strand |
|---|---|---|---|
| Shaman | yes | Tended Life, Release Residue, Delayed Return | spirit-care |
| Architect | yes | Meter, Timing Window, Trigger Chain, Loadout, Flow Network, Combination with Lineage | spar |
| Challenger | yes, faces on conflicts first | reshaping table (AntiPattern) | spar |
| Regent | yes, with licence rule | all, marked council's word | chapter1 |
| Diplomat | yes | Turns and Shared Pool, Delegation | chapter1 |
| Sage | yes | the above, plus Knowledge State and Practice Space | chapter1 |

Dissent: not unanimous on the first strand (spar, spirit-care, chapter1). The faces agree on the method, which is a flag: no face argued for running all six over every mechanic, and the Challenger's case for the conflicts first is the sharpest reason it holds.

## Sage

Kept from each face: the Shaman's care cadence and its release; the Architect's six structural parts as DesignObject types; the Challenger's reshaping table; the Regent's licence and provenance rule; the Diplomat's two-person parts and scoped trust. Dropped: AttentionState as an ontology addition (NPC alertness is a WorldAgent field, not a new object); "Practice Space" is kept as a candidate only, because the living ship's spirit barn has not reached its design round. First strand: Chapter 1, because it is the north star and the Kickstarter gate, and its open item (the second player for A6 and A8) is exactly the Turns and Shared Pool part; the spar takes the Meter, Loadout and Timing Window once the move ontology settles how element power works. Deferred: per-strand closer reads of each shortlist, done by each strand's next design thread.

## Outputs

Positions (stand unless Wendell flips them; all rest on his ask above and the record cited):
- `ga-method`: index, crosswalk by rule 5, six faces on gaps and conflicts only. Why: docs/ontology-in-flows.md loads cost per call; 280 x 6 face readings buys little the crosswalk lacks.
- `ga-index-not-copy`: atlas kept as a factual index with our own words, atlas id cited on adoption. Why: no licence stated on the site.
- `ga-codex-brief`: the additions reach the ontology only through `docs/codex/mechanic-vocabulary-brief.md`. Why: docs/ontology-in-flows.md, "Changes to the ontology itself".
- `ga-reshape-table`: the 31 conflicts enter the ontology as AntiPatterns with reshaped versions. Why: hard invariants, composting stop list.
- `ga-first-chapter1`: Chapter 1's second player is the first strand to use the atlas (Turns and Shared Pool). Why: Chapter 1 demo is the Kickstarter gate (team memory, 10-14).
- `ga-spar-waits-moves`: the spar's Meter, Loadout and Timing Window wait on the move ontology. Why: Wendell, 2026-10-21, spirit-generator callsheet: move learning waits on the move ontology.

Questions: none passed the reach test. Every choice above is answered by his ask, the ontology flow rules or the north star.

Limits (not checked): the crosswalk workers judged each mechanic from its name, system, tags and example games, not the atlas's full rule text, so a partial or gap may be a misread; each strand's closer read checks its own shortlist against the full entry. No playtest backs any claim here.

Tests for pass 2: (1) Codex lands the brief and `python3 -m unittest tests.test_design_ontology` passes. (2) The Chapter 1 second-player design names at least one atlas part by its ontology name. (3) No conflict mechanic enters a build without its reshaped version.
