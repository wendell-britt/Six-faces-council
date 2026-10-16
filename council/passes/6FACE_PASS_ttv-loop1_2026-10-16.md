# Tap the Vein as one loop, pass 1

**Date:** 2026-10-16. **Called by:** the coordinator, on Wendell's message that opened the thread "Tap the Vein: ingestion,
council action, lenses" (17:39 UTC). **Pass:** first on the loop as a whole; it follows morning menu 1 (2026-10-09) and
Lenses 1 (2026-10-14). **Ontology:** design-ontology skill, QUICKSTART plus the binding decisions bar_scope, composting,
privacy_consent_authority and roadblocks (docs/ontology-in-flows.md: a pass that designs a mechanic).

**The ask, in his words.** "ok I want to apply the game design ontology to the tap the vein flow. Specifically I Want
the version on the board to have the same ergonimic feeling as that on bars engine, but I also need the bars engine flow
to have the completeness of the board. Basically what we're trying to figure out once a taget's generted fromks tap the
vein how does it get ingested? How does the council act on the actions that I Want to do? How does the process help us
grow up teh tasks (Which are essentially barSeeds) into fruit. Right now the lens intersection is the place where things
have the biggest opportunity. The Lense intake would happen at character creation, but I haven't gone through that
process as the game's creator so for my needs I need a way for lenses to emerge through a council analysis of saved tap
the vein (with the idea that my freewrites would have the seeds of my long term goals) AND the ability to take actions
that I commit to for the day and align them with work that's aready happening and then align the work that's already
happening to lenses. because the creation of this game is itself a game this is also why I want to bring in the game
design ontology"

**Casts** (`council/iching/cast.py`, three-coin method): Shaman 49 Molting, becoming 17 Following; Architect 34 Vigour,
becoming 15 Understatement; Challenger 36 Nightfall, becoming 60 Measure; Regent 53 Emergence, unchanging; Diplomat 47
Drained, becoming 8 Alliance; Sage 40 Thaw, becoming 31 Mutuality.

**Scorecard.** Lenses 1 set tests for 2026-10-21 (his real domains on the Morning tab, one active goal, one item bridged
with a written reason); not due. Morning menu 1's test of 2026-10-16, one real morning end to end, has no ledger entry
after 2026-10-14. The Challenger reads that as an absence in the record, not proof that no morning ran.

**Anchor.** Every menu item bridges to a Lens goal, or the game masters suggest a smaller one (`mm-menu-shape`); now
also: lenses can emerge from his own writing, and the day's commitments meet the work already running.

## Design, in the ontology's terms

- **design_intent.** One loop from the morning write to the work: write, commit, the council takes it in, the work
  runs, the seed fruits or composts, and goals emerge from what keeps returning.
- **intrinsic_pleasure.** The designer's (constitution 2, 13): recognizing his own long thread in what he wrote, and
  seeing the day's moves land in work already moving. Generation and integration lead; the counterweight is good-enough
  completion and composting (Wendell's design center).
- **ontology_objects.** A commitment is a `TapTheVeinTask` in bars-engine (`mm-where`). It becomes a BAR only when he
  keeps it as one (bar_scope: capture creates lineage, not debt). A Lens goal is a `LensGoal`. Work already happening
  is a call sheet strand, a board row or a pull request. A pitched goal is a council proposal (AI inference is proposal
  only) until he keeps it.
- **mechanical_claims.** Tracked: commitments, their alignment line, their charge, and (new) recurring lines across
  saved free writes. Rewarded: no automatic reward. Gated: a goal exists only after his keep; a strand carries a lens only
  after his keep. Remembered: the date and words each pitch quotes. Permitted: "no home yet", composting with no reason,
  "not mine".
- **aqal_attention.** UL: his authored meaning of his own goals. UR: the commitments and the work done. LL: strands
  involve others (Jev and collaborators); tagging their work to his lens records his meaning only. LR: bars-engine as the
  one store, the board as front door, the council's scripts as checks.
- **agency_and_consent.** His 17:39 message is a present grant for one purpose: Lens goal pitches from saved free
  writes. Other purposes (BAR mining from the archive, board display, analytics, scheduled reads) are not granted.
- **evidence_and_unknowns.** Unknown: how many saved free writes exist (the council cannot reach the export from this
  session; the proxy's key was refused with 401). The first emergence run answers it (test T1).
- **provenance_effects.** Every pitch names its dates and quotes his words; every alignment line names its target.
- **risks_and_tests.** Below, per face, and the dated tests at the end.
- **implementation_translation.** Built in this pass: below under Outputs.
- **decision_or_open_authority.** Wendell holds goal meaning, fruit and consent scope; the positions below stand
  unless he flips them.

## The faces

### Shaman (49 Molting, becoming 17 Following: a skin is coming off, and the new one is soft)

**The old skin is the Lens intake at character creation, which he never went through; the new skin is lenses that come
out of his own writing.** Molting's third line warns against committing before a change has been spoken more than once,
so **a lens is named only after a theme comes back.** Following says to fall in with work already in motion: the council
follows the strands he is already working rather than pulling them toward goals, and **a lens can come from what he does
as well as what he writes.** **Fruit is his mark, never inferred:** maturity reaching `integrated` is a system trace, not
fruit (Evidence authority). **Risk:** reading old entries for goals turns unjudged writing into judged material; a pitch
must read "this kept coming back", never "this is your goal". **Copy:** an empty domain is open, not empty; a carried
task shows "let it go" beside "carry". **Dissent:** his saved bars-engine free writes were written under `mm-raw`'s
notice that only kept lines leave; the Shaman would ask him about the old entries before reading them.

### Architect (34 Vigour, becoming 15 Understatement: force is available here and unaimed)

**Most of the machinery exists and is not pointed at one object.** A commitment becomes a `TapTheVeinTask` in
bars-engine, but a can-do item on the board only gets an `intake_align.py` line and never reaches bars-engine.
**`TapTheVeinTask.status` packs five lifecycles into one field** (progress, carry, compost, campaign, quest), so turning
a task into a quest ends the task, which bar_scope §4 rules out for a BAR. **Third positions:** bars-engine is the one
store and the board writes through its API, as the Nonprofit Board's saves do; the free write is read where it lives and
only pitched goals with short quotes come back; a seed can take a form (an expression) while it stays active. **Next
builds:** the board's seal POSTs each item to bars-engine as a task with `source: "board"`, and the menu export carries
`taskId` and `barId` (`ttv-one-store`); an `AlignmentLink` record (task or BAR to goal, strand, row or PR, with a written
reason, proposed or accepted) so alignment is stored, not only shown; the status split (`ttv-axes`). **Dissent:** the
emergence read belongs on bars-engine's server with its own token, returning only pitches.

### Challenger (36 Nightfall, becoming 60 Measure: past what you can hold, and the edge unsaid)

**One commitment can exist as six unlinked records today:** a task, a board-store line, an alignment line, a corpus BAR, a
board row and a thread, with no shared id. **"Tasks are barSeeds that grow into fruit", stripped of the image, is a task
pipeline with stages; it is a CRM unless fruit is an outside event.** **Anti-patterns:** lenses pitched from his words and
then used to grade the council's own strands certify themselves (FC-02, FC-03); stage-climbing read as fruit (FC-05);
one ritual kept in two codebases drifting apart. **The measure:** read free writes transiently, never keep them; a task
links to a BAR only when he keeps it as one; "unaligned" is a real result; run the overdue real morning before building
more. Tests T1 to T4 below.

### Regent (53 Emergence, unchanging: this has stages, and you are trying to skip one)

**Two skips are possible:** aligning work to lenses before any goal exists, and reading saved free writes without a
scoped route. **Order:** (a) take in commitments by id and align each to work already happening, which works with zero
goals; (b) lens emergence from saved free writes; (c) align strands to lenses, which needs goals. **The read route:**
read-only and token-gated; each read logged in bars-engine with no text; the council's copy temporary; each pitch quotes
his line with its date; only kept pitches POST to `/api/lenses/goals`. **Fruit and compost:** fruit is the task's own
completion met and marked by him; compost is a disposition that needs no reason and stops carry and resurfacing.
**Gates:** G1 every pick carries a task id and an alignment line; G2 no `rawEntry` text in the repo, ledger or board
data; G3 one goal kept from a saved free write is active; G4 one strand carries a kept lens and unaligned strands keep
running; G5 one seed reaches fruit or compost through a recorded disposition. **Stop:** raw text outside bars-engine, a
goal written without his keep, a strand held for lacking a goal, compost requiring a reason.

### Diplomat (47 Drained, becoming 8 Alliance: the explaining continues and the basin is dry)

**The board's box keeps explaining:** ruling ids and pipeline prose sit inside the invitation. **bars-engine's feel comes
from three features:** one phase at a time, the rail, and one honest line ("No floor to clear · no streak to keep ·
stuckness is data, not failure"). **He arrives late to a union already forming:** the Lens slots assume character
creation, and with no goals every commit in bars-engine met "commit them as shadow quests", which makes an unaligned
task sound like a deficit. **Doorway:** "Write what's in you. Pick what you'll do today. The helpers suggest where each
one belongs. You say yes, no, or not now." **Overreach line:** cutting the board copy until the data-use notice
disappears; the notice moves behind "How your words are used", one click away, and stays.

### Sage (40 Thaw, becoming 31 Mutuality: the knot just loosened, and the window is short)

**The knot that loosened is the missing goals:** five faces agree the council can let goals emerge from what he already
wrote, without waiting for an intake he skipped, so long as every pitch quotes his words from more than one morning and
no pitch becomes a goal without his keep. **Retained:** the Diplomat's and Shaman's ergonomics (one phase at a time, the
ethic line, "no home yet"), built now; the Regent's order and gates, adopted as the order of builds; the Architect's
one-store, alignment-link and status-split designs, kept as the next builds in that order; the Challenger's finding of six unlinked
records and tests T1 to T4. **Set down for now:** the Architect's server-side emergence (the first runs read in a council
thread, as he asked for "a council analysis"; moving the read into bars-engine stays open once runs show what it needs);
the Shaman's per-entry consent tick. **Dissent kept:** the Shaman would ask before reading entries written under
`mm-raw`; the Architect would run emergence on bars-engine's server; the Challenger would build nothing more before the
overdue real morning. **The window is short:** he named the lens intersection as the biggest opportunity, so the slice
ships the emergence read, and the Challenger's T1 tests it on the first run. The Sage recommends and does not decide.

## Verdicts

| Face | A ingestion | B council action | C seed to fruit | D lenses | E ergonomics |
|---|---|---|---|---|---|
| Shaman | task stays a task | follow running strands | fruit is his mark | after a theme returns | rail, ethic line, open not empty |
| Architect | one store, by id | proposed links he accepts | split the status axes | read where it lives | rail; can-do list into bars-engine |
| Challenger | six records, one id | no self-grading | outside event only | transient read; T1 first | exports, not two runners |
| Regent | by id, gate G1 | order a, b, c | compost needs no reason | scoped, logged read | rail beside gate (a) |
| Diplomat | no home yet is normal | he keeps or corrects | his word | proposals with dates | one phase, fold the notice |
| Sage | synthesis | | | | |

**Dissent check:** not unanimous. Five faces support with conditions; the dissents are listed under the Sage.

## Outputs

**Built in this pass** (draft pull requests):
- bars-engine: `GET /api/tap-the-vein/history` (same token and player as the menu export): his past days, each free
  write verbatim and the seeds committed from it, with each seed's BAR maturity; every read logged with no text. The
  commit step's no-goals copy now says a task with no home yet is fine.
- council: `council/lens_emerge.py` (fetch to a scratch folder outside the repo, summary, pitch: at most five goals, each
  quoting his words from two or more mornings, in the row shape `lens_goals.py kept --send` already sends);
  `council/intake_align.py` takes `strand` (a call sheet, with its kept lens when it has one) and `none` (no home yet);
  the board's Tap the Vein box runs one phase at a time under a rail, with the ethic line and the "How your words are
  used" fold.

**Positions** (each stands unless he flips it on the board):
- `ttv-board-one-phase`: The board's Tap the Vein box runs one phase at a time under a rail (what you can do, free
  write, keep your lines, seal), with bars-engine's line "No floor to clear · no streak to keep · stuckness is data, not
  failure", and the notice on how your words are used one click away. Source: Diplomat and Shaman; your 17:39 ask for
  the board to feel like bars-engine.
- `ttv-no-home-yet`: A commitment with no Lens goal reads "no home yet, and that is fine", never "shadow quest"; the next
  read suggests a home and you keep, correct or leave it. Source: Diplomat; `lens-intake-align`.
- `ttv-align-to-work`: Each item on your intake can join work already happening (a call sheet strand), besides a goal, a
  board row or a pitched goal, and the strand's Lens goal rides along once you have kept one for it. Source: your 17:39
  words "align them with work that's aready happening"; Regent's order.
- `ttv-saved-read-scoped`: The council reads your saved bars-engine free writes only to pitch Lens goals, through a
  logged read, keeps no copy, and writes only the pitches you keep back to bars-engine. Other uses of the archive (BAR
  pitches, the board, a scheduled read) are not granted. Source: your 17:39 words "a council analysis of saved tap the
  vein"; your steer on `ttv-raw-bars`, "the power of having a private server like in bars engine". Shaman dissents.
- `ttv-lens-emerge`: A Lens goal is pitched only when it returns: each pitch quotes your words from at least two
  mornings, with their dates, at most five a run. Source: Shaman (Molting line 3); `lens-pitch-goals`.
- `ttv-fruit-is-his`: A seed bears fruit when an outside event happened (sent, merged, done with a link) and you mark
  it; a stage the council moves it to is not fruit. Composting needs no reason and stops carrying and resurfacing.
  Source: Shaman, Regent, Challenger; composting decision; Evidence authority.
- `ttv-task-not-bar`: A commitment becomes a BAR only when you keep it as one. Source: Challenger; bar_scope.
- `ttv-one-store`: Next build: the board's seal writes each item to bars-engine as a task, so every commitment has one
  id from the morning to its thread, and alignment is stored as links you accept. Source: Architect; Challenger's six
  unlinked records; `mm-where`.

**Questions:** none survived the reach test. Consent for the archive read is answered by his 17:39 message with the
`ttv-raw-bars` steer (Regent, Diplomat, Architect, Challenger cite it); the Shaman's ask stays as dissent on
`ttv-saved-read-scoped`, which he can flip.

**Tests, dated:**
- T1, 2026-10-18 (Challenger): the first emergence run reports how many saved free writes exist, and whether any pitch
  quotes two mornings. None found means drop the archive read and lean on strands.
- T2, 2026-10-21 (Challenger, with Lenses 1's tests): one real morning end to end; count how many records each
  commitment becomes and how many share an id. More than one id per commitment confirms `ttv-one-store`.
- T3, 2026-10-23 (Challenger): two invented strands, one plausible and one unrelated, go to the aligner; if the
  unrelated one gets a reasoned lens, strand-to-lens alignment is a rubber stamp and stops.
- T4, 2026-10-23 (Challenger): list his tasks carried two or more times with no blocker note, compost or decision; any
  found means a carry-or-decide step comes before more seed-to-fruit work.

Daemons: none sent. Face subagents: five, about 291,000 tokens together.
