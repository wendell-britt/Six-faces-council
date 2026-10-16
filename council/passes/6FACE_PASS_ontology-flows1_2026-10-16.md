# Six-face pass 1: the design ontology in the council's flows

**Run 2026-10-16**, called by Wendell in the project chat: "We've also added a game design ontology to the six faces repo that is designed to be used in continuing our game design work. I'd say its important for us to review that using the 6 faces and figure out how best to deftly use the information and processes there in our flows in a way that remains deft and token efficient". The subject is `ontology/` (0.1.0-alpha.2, provisional) and the flows: board reads and pulls, callsheets, round and chamber threads with their loop contracts, the daily compost pass, and the needs-work list. First pass on the subject.

The pass loaded the `default` profile (Quickstart) and an evidence pack, not a deeper profile, because the question is about routing, not a game mechanic. The five faces ran as the packaged read-only agents (`.claude/agents/`) under `ontology/v0.1/FACE_OUTPUT_CONTRACT.md`; each report below is condensed from the agent's own text. The caller wrote the Sage section from the five unedited reports rather than starting a sixth agent, to keep the pass inside its own token advice. Subagent tokens: 206,569 across five faces.

## Scorecard

No earlier pass on this subject; nothing to grade. Tests at the end.

## Anchor

The ontology guides the council while it designs and builds games (manifest `purpose`), and the north star is a playable Chapter 1 demo of *Mastering the Game of Allyship* built on it (`council/callsheets/chapter1-demo.md`). The question is where in the daily flows it earns its tokens.

## Measured before the pass

- Profile cost, manifest plus files at about four characters a token: `default` about 5k; `game_design` 29k; `council_deliberation` 29k; `aesthetic_excavation` 31k; `implementation_translation` 28k.
- Threads open at 102k to 140k tokens; 84% of spend is rereading (audits of 2026-10-04 and 2026-10-08).
- Already wired: CLAUDE.md, the six-faces skill (any pass on a game loads it), the design-ontology skill, six face agents with an output contract. Not wired: board reads, callsheets, loop contracts, compost pass, needs-work.

## Casts (three coins, `council/iching/cast.py --seed 20261016`, so the record replays)

| Face | Hexagram | Changing lines | Becomes |
|---|---|---|---|
| Shaman | 57 Persuasion 巽 | 4, 5, 6 | 32 Endurance 恆 |
| Architect | 44 Serendipity 姤 | 6 | 28 Overload 大過 |
| Challenger | 38 Estrangement 睽 | — | — |
| Regent | 54 Home Field Advantage 歸妹 | — | — |
| Diplomat | 16 Anticipation 豫 | 4, 5 | 8 Alliance 比 |
| Sage | 42 Windfall 益 | — | — |

# The faces

## Shaman (57 Persuasion → 32 Endurance) — subagent tokens 33,246

**Cast.** The ontology already shapes the flows in ways the record does not name: the compost pass already behaves like `CompostingDisposition`; round 11 of the loop already records a redirect as a correction, not a failure. "This exact exchange has happened before": the ontology should live in the motions that repeat (callsheet fields, the lint, the compost sentence), not in profiles every thread rereads.

**Observations.** In these flows Wendell is the player; board reads, callsheets, rounds and the compost pass are rituals he lives in daily (QUICKSTART 2, 13, 14). The compost pass already fits closely ("nothing depends on it"; lateness is evidence, not a reason alone). Not written down: dropping ends the obligation, nothing is owed back, reactivation needs a new decision. The loop's `max_ahead: 2` protects his rest; his silence never counts as his look. "Positions stand unless he flips it" is legitimate for build choices and must never reach reserved matters (consent, money, anything naming a person; FC-08). Inference: the shaman lesson of 2026-09-09 in `council/faces.yaml` ("if there IS a block we should assume self-sabotage, with the given choice to skip") sits in an unstated conflict with FC-01/FC-07 (a roadblock is not resistance or defect).

**Risks.** Profile loading in clerical flows (~29k tokens on threads already at 102-140k). Compost becoming a harvest owed (FC-12). Words that judge him ("stalled on Wendell", "he hasn't answered") turning rest into backlog; nothing deterministic catches this. Ontology vocabulary pasted as decoration with no field that changes a decision. Own overreach: sacralising clerical work, reading feelings into board silence.

**Recommendations.**
1. One `ontology:` line per callsheet and loop round: `none`, `default`, or a named profile, plus at most three object names. `none`/absent for board reads, needs-work, Nonprofit saves, art rounds; a profile only for mechanic strands. A thread loads only what its line names.
2. Compost `retired` sentence in the ontology's grammar: "Dropped on <date>: the obligation <x> ends; nothing is owed; bringing it back needs a new decision." Never "dropped because he didn't act". No Phase B sorting of the ontology itself.
3. A cheap deterministic check beside `council/tools/voice_lint.py`: bare TensionVector, WAVE outside Open Up, unnamespaced Epiphany values, and a short phrase list that turns rest into deficiency.
4. Keep the loop gate's rest: a redirect is a scoped correction; no look is no look, never approval, never a stall on the board.
5. Sage puts the shaman-lesson vs FC-01/FC-07 conflict through the reach test; only he changes `faces.yaml`; until then flows lead with the choice to skip.

**Standing test.** Recs 2-4 pass (they record what the designers learned). The lesson's "assume self-sabotage" as a default frame fails.

**Verdict.** support_with_conditions: light fields and checks in the repeating flows, no profile in clerical flows; compost, silence, redirects and unanswered rows are never written as deficiency.

**Evidence and authority.** Documents only (evidence pack, QUICKSTART, FACE_OUTPUT_CONTRACT, faces.yaml 26-79, compost-pass.md, spirit-generator.json). Judging-language risk inferred, no steps sampled. faces.yaml conflict: Wendell only. The field is a council position; the lint is the builder's.

**Dissent seed.** A flow that cannot hear Wendell's silence, rest or redirect as a complete answer will turn the ontology into one more way to measure him, however few tokens it costs.

## Architect (44 Serendipity → 28 Overload) — subagent tokens 41,120

**Cast.** "Building on one piece of evidence": the pack's map of what is not wired, spot-checked (INDEX.md, spirit-generator.json, compost-pass.md confirm it); token figures are chars/4 estimates. "Carrying more than what holds it up": do not put 5k-31k tokens of ontology into flows whose roof cannot hold them. Move the knowledge into small fields and free checks.

**Observations.** What exists: one load-profile map (`load_profiles`), one machine-readable list of retired/reserved terms (`compatibility`), the binding composting rule, prose callsheets, loop contracts with `builds/check/gate/budget/model`, board steps with a free-text `retired`. Board reads, needs-work and Nonprofit saves are clerical (Sonnet or no AI); strand and round threads design or build on Opus; compost runs daily on Sonnet. compost-pass.md's "Drop (compost)" covers three reasons: "nothing depends on it", "duplicates another step", "a later change made it moot"; by the ontology only the first is composting, the others are supersession or merge. INDEX.md says "WAVE room" throughout; whether the room is the Open Up practice's place is unchecked (observation, not finding).

**Risks.** False binary: load everywhere (5k resident tax reread every call, ~300k input over 60 calls) vs nowhere (drift and FC-12 collapses unchecked). Third option: typed pointers and deterministic checks, a profile only where design happens. A Drop for moot/duplicate steps takes composting's semantics and loses its `superseded_by` link. Backfilling old `retired` rows would be unauthorised Phase B sorting. A naive lint flagging "WAVE room" before the record is checked turns classification into a defect claim (FC-02). Own overreach: schema in every flow; every field needs a reader.

**Recommendations.**
1. Callsheet line: `ontology: <profile|none>; touches: [TypedObject...]; binding: [decision keys]`. Mechanic strands get `default` or `game_design`; art, podcast, plumbing get `none`. ~30 tokens a sheet.
2. Loop contract: optional per-round `ontology_profile`, checked by `next_round.py` against manifest keys.
3. Typed compost disposition on board steps: `composted | superseded_by:<id> | duplicate_of:<id> | done`; legacy rows `unclassified_legacy`, no backfill; a composted step returns only as a new step citing the old id. The binding rule goes into compost-pass.md as three sentences.
4. Deterministic `ontology/tools/term_lint.py` reading the manifest `compatibility` block; runs over board rows, callsheets, positions in CI and board-pull; warns, never fails; allowlist entries cite a ruling.
5. Board reads, needs-work, Nonprofit saves: no ontology load, lint only; a needs-work item that becomes a design question routes to its strand thread.

**Standing test.** No Architect standing test in faces.yaml; lens and `term_test` applied: profiles chosen from a field, not memory; the binary is false; `disposition` buys a mechanic (stops overdue pressure, return needs a new decision), a free "compost" sentence does not. Executable tests: every open sheet has a valid `ontology:` line; next_round rejects unknown profile; lint fixtures (bare TensionVector flagged, BARS321TensionVector deprecated, unnamespaced epiphany warns, "WAVE room" warns until a ruling); compost Drop without disposition fails.

**Verdict.** support_with_conditions, routing only: no profile in clerical flows; no backfill; lint warns not fails; any board step-shape change goes through the schema that owns steps (paired PRs if saves carry it).

**Evidence and authority.** Read manifest, QUICKSTART, contract, faces.yaml, compost-pass.md, spirit-generator.json, INDEX.md. Did not read the binding WAVE decision; the WAVE room question goes to the reach test against it first. Did not verify whether steps fall under board-save.schema.json. Everything else is advisory.

**Dissent seed.** Put the ontology into flows as typed fields and free deterministic checks, not as loaded context; a compost Drop that is really a supersession must not carry composting's name.

## Challenger (38 Estrangement, no changing lines) — subagent tokens 43,752

**Cast.** "You reached a conclusion from a distance"; small matters go well. The question assumes the ontology should run through every flow before any record shows it changing a single decision. The safe moves are small and placed where decisions are made.

**Observations.** The ontology already reaches every game-design pass through the six-faces and design-ontology skills; what is missing is wiring into clerical flows. Several of those have no model at all (`board-pull.yml` runs fetch, pull, build, ack, staleness with no AI), so prose wired there has no reader. A 29k load is paid again on every tool call. "WAVE room" in INDEX.md lines 8, 13, 16, 17 against the manifest's reserved WAVE: collision or valid use, unchecked. compost-pass "Drop (compost)" and `CompostingDisposition` are close but not the same. Most open game strands wait on his phone play.

**Risks.** (1) A boilerplate field filled with `default` that nobody reads: a noun with no verb under it. (2) Profile creep: art rounds loading `game_design` for "reads as an otter at 96 px", about 300k tokens of rereading over 11 rounds. (3) Agreeable language as cover: "composting is valid completion" could make a dropped step look principled when it is a missed decision; "do not return questions to Wendell" could hold back a real question (FC-08, FC-13). (4) A moving target: v0.1 alpha, Codex updates, copies of its terms drifting in many places. (5) Ontology wiring is meta-work that needs nothing from him while the real blocker is his play backlog; it runs beside that gate, never in place of it. (6) Own overreach: blocking a small, sound wiring because it is set to disagree.

**Recommendations.** 1. Load the ontology only at decision points (design passes, mechanic positions, new-strand briefs); not in board-pull, needs-work, saves or loop JSON. 2. `default` is the ceiling for round and chamber threads; deeper only when the round's `builds` names an ontology object. 3. One compost-pass sentence: a dropped step comes back only by a new explicit step. 4. No callsheet or loop field until T1 shows the ontology changed a decision. 5. Put the WAVE-room collision through the reach test before writing a lint.

**Falsification tests.** T1 (by 2026-10-23): replay three mechanic positions (`sg-romp-four-feet`, `sd-mana-to-stat`, `ps-polarity-poles`) through QUICKSTART only; fails if none would have changed, and then wiring stays at skill level. T2 (by 2026-10-20): term-lint dry run over callsheets and board rows; fails if false positives outnumber true collisions, and then no lint. T3 (by 2026-10-21): did any step retired since 2026-10-12 come back without a new step; fails if none did, and the sentence is decoration. T4 (by 2026-10-23): ontology tokens loaded against clauses cited in a week of threads; fails on any round-thread load with zero citations.

**Standing test.** Stripped of imagery, "use the ontology deftly in our flows" means loading 5k-29k tokens in case they change a decision; only measured cost holds that up today. Passes at design passes, where a face cites a clause and a position changes; fails as a field on clerical flows.

**Verdict.** support_with_conditions for recommendations 1-3; opposes wiring into no-AI and clerical flows until T1 and T4 show a changed decision.

**Evidence and authority.** Evidence pack, manifest (compatibility, load_profiles), QUICKSTART Composting, compost-pass.md, INDEX.md, spirit-generator.json. Costs are chars/4 estimates; collision observed as text only. WAVE term status is the owner's, after the reach test.

**Dissent seed.** Until a test shows the ontology changed a build decision, wiring it into a flow costs tokens on every call and buys nothing.

## Regent (54 Home Field Advantage, no changing lines) — subagent tokens 40,943

**Cast.** The one who arrives takes the junior place in a house whose rules are set. The ontology (provisional, release candidate) is the newcomer to working rules Wendell has already ruled on; it takes the junior place in how work moves. Within game-design meaning it holds binding decisions, and there the council is the newcomer. No changing lines: nothing is reversed.

**Observations.** The two rule sets cover different ground: repo rules govern process, the ontology governs what game objects mean plus evidence and consent limits; where they meet (session discipline) they agree. Both trace to Wendell, so a conflict is between two of his records and the council cannot settle it. Composting is the one real meeting point, and "Drop (compost)" merges composting with supersession (FC-12). RELEASE.md limits bind every flow: no Phase B sorting, no real player data. Retired and reserved terms exist only as prose; under `term_pass` only Wendell locks a term.

**Risks.** The ontology becoming a new gate that blocks `gate: auto` rounds, overruling his 2026-10-14 ruling against stalled work. ~24k extra tokens per profile on Sonnet clerical threads, against his Short sessions ruling. The daily pass composting ontology sources (Phase B by accident). Treating PermissionGrant language as protection for real data in board steps (mail, PayPal). Own overreach: procedure for its own sake.

**Recommendations.** 1. Precedence as a position: repo working rules govern process; the ontology's binding decisions govern meaning in game-design work; a real conflict goes through the reach test as a board row, neither wins silently. 2. Optional `ontology:` field on callsheets and loops; missing means load nothing; never a gate. 3. Split compost-pass Drop into compost (ends the obligation, no harvest owed, return needs a new decision) and superseded/duplicate; the pass never sorts `ontology/`. 4. A deterministic term check runs in CI. 5. No ontology wiring for needs-work and board reads.

**Phase gates.** G0 this pass, positions only. G1 (Sonnet, clerical): recs 2 and 3, tests pass, voice lint clean, no loop round blocked. G2: rec 4, catches a planted fixture and passes the current board. G3 (his ruling only): faces.yaml lessons, locking terms, constitution changes, Phase B, real player data. Stop conditions: a change adds a gate to an auto loop; a clerical flow needs more than `default`; a thread passes 200k; any move toward Phase B.

**Standing test.** Preserve his process rulings, binding decisions, provenance and the reserved list; binding are CLAUDE.md, manifest `binding_decisions`, RELEASE limits; only preferred are the new fields, script and wording split, which ship at G1-G2.

**Verdict.** support_with_conditions: no new gates, no Phase B, no real data treated as protected, G3 waits for him.

**Evidence and authority.** Evidence pack, faces.yaml (reserved list, term_pass), manifest, QUICKSTART, RELEASE.md, compost-pass.md, spirit-generator.json. Did not read terms.yaml or the composting decision file.

**Dissent seed.** The ontology is the newcomer in how the council works; any proposal that makes a flow wait on it, or makes a thread pay for it without declaring so, reverses the order Wendell already ruled.

## Diplomat (16 Anticipation → 8 Alliance) — subagent tokens 47,508

**Cast.** "The good part has started and the event has not": the ontology has arrived but the flows have not met it. Alliance warns that a newcomer to a union already formed finds the places taken; the ontology, written with Codex, arrives late to Claude-side flows with their own words (compost, retired, WAVE room, metabolize). The joining happens at the seam, in a small set of agreed words. Five-year-old doorway: "The ontology is a word book and a rule book for making games. Each job opens only the page it needs, and Wendell reads plain words."

**Observations.** Shared words already mean different objects: "Drop (compost)" leaves out "return needs a new decision" and "not archival or deletion"; "retired" is used three ways (board step, faces.yaml term state, manifest `bare_tension_vector: retired`); "WAVE room" against reserved WAVE; bars-engine's "Composting, not necromancy" is what QUICKSTART calls a `ProjectMeaningFrame`; bars-engine's "Roadblock Quest to metabolize" differs from QUICKSTART, where technical metabolization needs no emotional processing. Wendell reads rows, callsheet lines and art looks, not ontology objects. No defined route for a Claude-side correction to reach the ontology's owner.

**Risks.** Flattening (ontology names leaking into his rows, or the ontology softened until its distinctions go). Collision (silent revival of a composted step; "WAVE room" spreading). Evidence blur (friends' plays, his looks and AI readings recorded as one kind; FC-03, FC-05). Psychograph misuse (the Enneagram Five hypothesis cited back to him as a diagnosis). Phase B by the compost pass.

**Recommendations.** 1. One ontology line per callsheet (`profile=<none|default|game_design|implementation_translation>; objects=...`) set by the strand's first design thread; optional `ontology_profile` on loop rounds; visual art rounds stay `none`. 2. A small glossary mapping flow words to ontology words, in a later build stage; ontology names in fields and ledgers, his rows in his plain words. 3. Compost pass, two sentences, no profile load. 4. A deterministic term check run on rows and callsheets; WAVE room to the reach test first. 5. A route back to Codex: a Claude-side thread records a conflict as a reconciliation note or board position and never edits canon in place; rows that cite play name who reported it.

**Standing test.** Plumbing: yes for profile names and the check, not yet for "compost" (three meanings until a glossary). Reaching toward: only if ontology names stay out of his rows.

**Verdict.** support_with_conditions: a profile field, a glossary and a deterministic check; clerical flows do not load it; his reading surface does not change.

**Evidence and authority.** Evidence pack, manifest, QUICKSTART, contract, compost-pass.md, INDEX.md, spirit-generator.json, design-ontology skill, bars-engine CLAUDE.md. Wendell owns the constitution and any WAVE ruling; Codex-side owners hold the ontology text; the steward decides the fields.

**Dissent seed.** Translate at the seam: ontology names belong in fields and ledgers, never in what Wendell reads, and a clerical flow carries the rule as a sentence or a lint, not as a load.

# Verdicts

| Face | Verdict | Where the ontology loads | What clerical flows carry | Compost pass | Callsheet and loop field |
|---|---|---|---|---|---|
| Shaman | support with conditions | mechanic strands only | the term check, plus wording that never names his rest as a deficiency | ontology grammar, no harvest owed | yes, optional |
| Architect | support with conditions | from a field, never from memory | the term check | typed disposition: composted, superseded, duplicate | yes, optional, validated |
| Challenger | support with conditions (1-3); oppose clerical wiring | decision points only; `default` caps rounds | nothing | one sentence on coming back | not until T1 |
| Regent | support with conditions | process rules stay senior | nothing; the check in CI | split compost from supersession; never sort `ontology/` | yes, optional, never a gate |
| Diplomat | support with conditions | the line the strand sets | the check; his rows stay in plain words | two sentences | yes, optional |

## Dissent check

Not unanimous. Four faces support an optional callsheet and loop field now; the Challenger holds it until a test shows the ontology changed a decision. All five agree that clerical flows load no profile, so that agreement is a flag, not a proof: it rests on a token estimate, not on a measured week of threads (the Challenger's T4).

# Sage: 42 Windfall, lines 2 and 3 changing, becomes 9 Restraint

Windfall says more is arriving than was put in: Wendell and Codex built the ontology, and the council receives it whole, including binding decisions that already settle questions the flows keep half-asking (what composting is, what WAVE names). The duty attached is to move toward the good and correct the fault. Restraint, the hexagram it becomes, says one small rule holds everything; here that rule is the routing line, "load it where a decision is made; elsewhere carry it as a sentence, a field or a check".

**What each face gave, and what the Sage kept.**
- The Shaman gave the frame that these flows are rituals Wendell lives in, and the rule that silence, rest, a redirect or a dropped step is never written as his deficiency. Kept, and the term check carries the wording half of it.
- The Architect gave the third option to load-everywhere or load-nowhere: typed pointers and free checks. Kept as the spine. Its typed step disposition is set down for now, because steps are part of the board's save shape and a field there means paired pull requests with bars-engine; the compost-pass wording carries the distinction until T3 shows it is needed.
- The Challenger gave the tests and the warning that wiring is meta-work beside his play backlog. Kept: the field is optional, set only by a strand's first design thread, never backfilled, and T1 and T4 decide whether it lives.
- The Regent gave precedence (process rules govern process; binding decisions govern meaning; a real conflict goes to the board) and the stop conditions. Kept whole.
- The Diplomat gave the seam: ontology names in fields and ledgers, his rows in plain words, and a route back to Codex that never edits canon in place. Kept. The glossary is set down until a flow word actually confuses a reader.

**The two term questions went through the reach test and needed no one.**
- "WAVE room": the record answers it. The room runs the manual W.A.V.E. breath (Welcome, Acknowledge, Validate, Exhale), and walking no longer carries the breath (`council/callsheets/wave-room.md`, 2026-10-13). That is the Open Up breathing practice the binding decision reserves the word for. The name complies.
- The Shaman's lesson of 2026-09-09 in `council/faces.yaml` ("if there IS a block we should assume self-sabotage, with the given choice to skip"): the record reconciles it. His own lesson calls it an offer ("An offer is not a requirement"), and the roadblocks decision permits an `IntentionAlignmentHypothesis` offered against a declared intention, never asserted. Flows offer the frame with its skip and never record it as a finding. `faces.yaml` is untouched.

**T2 ran during the pass.** The term check over today's callsheets, docs and open board rows found one hit, "complete WAVE" in `oag-wave-ladder`, and it was a valid use (a finished breathing run). The rule was narrowed and the record is now clean: zero true collisions, so the Challenger's test reads as a fail on present value. The Sage keeps the check anyway, because it costs no tokens to run, catches what Codex updates or new rows could bring, and is cheaper to delete than any other piece here. T2 is re-graded on 2026-11-16: if it has caught nothing by then, it is composted. The Challenger's dissent stands on the record.

**The Sage does not decide.** Everything below stands as a position unless Wendell flips it.

# Outputs

## Positions (stand unless he flips them)

- `of-load-where-decided`: the ontology loads only where a design decision is made: a six-face pass on a game, mechanic or design tool, and a strand thread that designs a mechanic. Board reads, pulls, Nonprofit saves, needs-work and the compost pass load none of it. Citation: the five verdicts; the measured profile costs; CLAUDE.md Short sessions.
- `of-callsheet-line`: a strand that designs mechanics may carry one `ontology:` line naming one manifest profile (or `none`) and at most three objects; the strand's first design thread sets it; old sheets are not backfilled; a loop round may name an `ontology_profile`, checked by `next_round.py start`, and without one a round loads nothing. Citation: Architect, Diplomat, Regent, Shaman; the Challenger's condition becomes T1.
- `of-compost-split`: the compost pass splits Drop into composted (nothing depends on it; return only by a new step citing the old id) and superseded (a duplicate or a later change, naming what replaced it), never writes that a step was dropped because he did not act, and never sorts `ontology/`. Citation: QUICKSTART Composting; FC-12; RELEASE.md (Phase B not authorized).
- `of-term-check`: `ontology/tools/term_lint.py` checks callsheets, docs and open board rows for retired and reserved terms and deficiency wording; it warns, never blocks a save, and runs in the test suite. Citation: manifest `compatibility`; the binding WAVE decision; T2 above.
- `of-precedence`: the repo's working rules govern process; the ontology's binding decisions govern meaning in game-design work; a real conflict goes through the reach test as a board row and neither wins silently; Claude-side threads never edit ontology text, they write a position or a reconciliation note. Citation: Regent, Diplomat; manifest `authority`.
- `of-wave-room`: "WAVE room" is a valid name. Citation: `council/callsheets/wave-room.md`, 2026-10-13; manifest `compatibility.WAVE`.
- `of-sabotage-offer`: the 2026-09-09 self-sabotage lesson is used as an offered frame with its skip, never asserted or recorded as a finding. Citation: `council/faces.yaml` lesson text; roadblocks binding decision.

## Questions

No question reaches Wendell: the record answered both term questions.

## Built in this pass (reversible, one pull request)

- `docs/ontology-in-flows.md`: the routing table, one page.
- `ontology/tools/term_lint.py` and `tests/test_term_lint.py`.
- `docs/compost-pass.md`: the split.
- `council/loops/next_round.py` and `docs/loops.md`: the optional `ontology_profile`.
- `council/callsheets/INDEX.md`, CLAUDE.md and AGENTS.md: one pointer each.

## Tests (dated)

- **T1, by 2026-10-23**: replay `sg-romp-four-feet`, `sd-mana-to-stat` and `ps-polarity-poles` through the Quickstart only. Fails if none would have changed; then `of-callsheet-line` is composted and the ontology stays at skill level.
- **T2, re-graded 2026-11-16**: has the term check caught a true collision? Fails if not; then it is composted.
- **T3, by 2026-10-21**: did any step dropped since 2026-10-12 come back without a new step? If one did, the typed disposition field returns as a build (paired pull requests with bars-engine).
- **T4, by 2026-10-23**: in a week of threads, any round thread that loaded a profile and cited no clause of it fails the routing.
