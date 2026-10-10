# The studio pipeline: a six-faces pass

**Run 2026-10-10**, from Wendell's message in the Sprout Game project chat at 20:26 UTC. The project's coordinator
started the thread. This is the first pass on the subject. The report it produced is
`/mnt/project-files/studio/studio-pipeline.md`, and its sources are in `/mnt/project-files/studio/sources.md`.

**The ask, in his words:** "I'd like the 6 game masters to also do a research project on game design. Specifically
designing a game design pipeline from inception to production and marketing specifically how this intersects with
Keegan stages and other pipelines like film and TV, what the basic moves and roles are and which need to be defined and
scoped. Essentially we are creating a game studio of one person and AI agents and we need to create a meta-game around
it that is also the spirit of producing it. We are doing this as a project to study this week with a specific eye for
creating deft more token efficient gains for the other projects in our current pipeline and aligning them to best
practices. For instance if we WERE a game design studio we would be one that practices holacracy and the principles in
reinventing organizations and using learn startup modalities."

"Keegan" is read as Robert Kegan's stages of adult development.

**The board was pulled first:** main carried the 20:19 UTC pull (e4bdc31) and the Big Mind round 1 record (8168c5b).

**Inputs:** the usage audit of 2026-10-04; `council/pipeline.yaml` and `council/faces.yaml`; the byte sizes of the files
sessions are told to read first (measured in this session: root-game `HANDOFF.md` 122,828 bytes; the council's
`HANDOFF.md` 42,200 bytes with 33 `## Open` sections; the six-faces skill 21,371 bytes); one research subagent's source
list; five web searches by the thread to check the load-bearing claims; two daemon reports.

## Scorecard

No earlier pass on this subject set tests. Retro 1's standing test applies: the pass names its sources, and
`sources.md` marks which were checked.

## The anchor

A one-person studio with agents needs a pipeline from the first spark to the store page. It should cost fewer tokens
than today's open-ended threads, borrow only what transfers from team frameworks, and play as a game in its own right.

## The casts

Drawn with `council/iching/cast.py --json`, three coins each; the ledger carries them under `casts`. (A display run
was drawn first by mistake and discarded; the recorded run is the JSON one.)

| Agent | Hexagram | Becomes |
|---|---|---|
| Shaman | 1 Unbroken: *Every line here sends, and the return has nowhere to land.* | 13 Fellowship: *You are walking the same way and neither of you has said so.* |
| Architect | 24 Turning: *What came back is one line deep.* | 15 Understatement: *What you are underplaying had better be there.* |
| Challenger | 8 Alliance: *This is filling a hole you had before it started.* | no changing lines |
| Regent | 50 The Cauldron: *This is being transformed, and you are carrying it by the handles.* | 18 Stale Air: *This went off from being left alone.* |
| Diplomat | 10 Footing: *You are stepping onto ground that matters, and the play is what makes it safe.* | 25 Candour: *Your next move has no calculation in it, and that is the exposure.* |
| Sage | 38 Estrangement: *You reached a conclusion from a distance.* | 34 Vigour: *Force is available here and unaimed.* |
| daemon-player (for the Shaman) | 42 Windfall: *More is arriving than you put in.* | no changing lines |
| daemon-skeptic (for the Challenger) | 34 Vigour: *Force is available here and unaimed.* | 32 Endurance: *This exact exchange has happened before.* |

Daemon reports, both passing `check_report.py` (the Player's on its second try, after its headings were corrected):
`council/daemons/reports/2026-10-10-studio1-player`, `2026-10-10-studio1-skeptic`. Subagent tokens: research 71,102;
player 45,379; skeptic 36,555; total 153,036.

## Shaman

**Unbroken becomes Fellowship.** Every line sends and nothing lands: the studio has been all output, seven strands
moving at once, with the return (a playtest, a player, a reader) nowhere to land. Fellowship says the studio and its
players are walking the same way and nobody has said so. The meta-game should say so.

**The felt sense is a studio that wants to be played, not managed.** The Player daemon put it plainly: "I want running the
studio to be fun, and I want saying what I want to be a normal move at every stage, not only at intake." Its superpower
burns the charge while it is hot: when a feature raises a live "I want this", the next battle round runs then, in the same
session, and a second feature does not open beside it.

**The meta-game is already here** (Player daemon, citing `pipeline.yaml` and `faces.yaml`): the board as world map,
battles, levels for agents, the five moves and the deferral ladder. The Shaman backs one addition from the daemon: a
one-line receipt when a battle closes, naming the question answered, the face that moved it, any level change and the
session's cost. Cost becomes something he sees in play, not in an audit a week later.

**Risk.** Kegan's stages are the Shaman's ground, and the standing test applies: they must say what was learned,
never what is wrong with someone. The council never places Wendell, a tester or an agent at a stage.

## Architect

**Turning becomes Understatement.** What came back is one line deep. The studio is mostly built already; the Architect's
job is to show that and not to understate the four parts that are missing.

**The mapping holds, and it is a table, not a new system.** The council's stages (intake, spec, falsify, plan, build,
verify, ship, close) already run in film's order: development, pre-production, production, post, distribution. The
game industry's gates (concept, prototype, vertical slice, alpha, beta, launch) sit on the same line. The report's
table puts the three side by side with lean's question at each gate. Nothing in it needs a new file format.

**Four parts are missing, and each has a mechanism:**
1. *A gate per project with a kill line written first.* One card per project (gate number, the hypothesis, the kill
   line, a one-line purpose). Supercell's practice is the model: nine cancellations while Clash Royale was made, each
   toasted for what it taught (Paananen, BAFTA lecture, 2016).
2. *A cap on work in production.* The board knows every open strand; the cap is a count it can show.
3. *Call sheets.* Root's CLAUDE.md says "Read HANDOFF.md first", and that file is 122,828 bytes, about 30,000 tokens,
   carried on every call of every Root session. A call sheet is the film crew's one page for the day: what shoots,
   who, where, what must not change. The archive stays; the session reads the sheet.
4. *A Marketer role.* No role owns the hook, the devlog, the store page or the trailer.

**Holacracy's role card is the one structure worth taking.** Purpose, domain and accountabilities, kept apart from who
fills it. The report's role table lists nine roles. Two need definition: the Marketer, which is missing, and the Producer's
cap and receipt, which are new. The Clerk exists as a rule in CLAUDE.md and becomes a role when it gets a domain.

## Challenger

**Alliance, with no changing lines.** This is filling a hole that existed before it started: the frameworks are being
asked to fill a gap the board already fills. The Challenger tests every framework against that.

**The Skeptic's evidence goes mostly against transfer.** Anthropic measured multi-agent systems at "about 15x more tokens
than chats". Medium dropped holacracy as "a small but persistent tax on our effectiveness and our sense of connection".
Zappos lost 18% of its staff in the two buyout rounds after the 2015 memo (Fortune, 2016-01-14; checked). Critics of
teal say its claims "cannot be tested", and one review of lean startup found "practically no scientific evidence" for it (the
Skeptic took both from search summaries and did not open the pages). Nobody has published on Kegan's stages applied
to AI agents.

**Kept, each with a kill number** (Skeptic's Show Up, adopted):
- Lean's cheapest test, which is already `falsify`. Cut it if three falsify tests in a row are skipped before the
  build, or if none changes a design.
- The staged pipeline, one call sheet per stage. Collapse the stages if a staged feature costs more than 1.5 times a
  one-thread build of similar size.
- Holacracy's role card, with no meetings. Cut it if loading role cards adds more than 5,000 tokens to a session's floor.
- **Cut:** governance meetings (one human has no one to govern with), tension logs (the board holds tensions), Kegan
  checks per session (a label nobody can test), and a separate advice process (the reach test is one).
- **The judge is weekly spend.** If the next audit shows process threads above 20% of spend, trim again.

**The study is itself process.** This pass and its subagents used about 153,000 subagent tokens.
A study week that produces call sheets but no cheaper sessions has failed its own test.

## Regent

**The Cauldron becomes Stale Air.** The work is being transformed and carried by its handles. Stale Air says what went
bad was left alone, and here that means the handoffs. Root's handoff grew to 122 KB because nobody owned trimming it.

**What must be preserved.** The reserved list holds: money, consent and release, names, canonical prose, faces.yaml. A
store page, a public devlog post or a trailer is release, and a Steam page costs money. So the Marketer drafts, and
nothing is posted, bought or published without Wendell's answer on the board. Transcend and include holds too: a
killed project is retired with its reason and kept readable, and the HANDOFF archives stay where they are.

**Gates are definitions of done.** The report's seven gates (spark, hook, find the fun, slice, production, ship and
show, live and learn) each end with a greenlight row on the board: continue, pivot or kill, with the default standing
unless he flips it. The Regent owns the rule that the kill line is written before the work, not after.

**Ships when.** The call sheets are clerical and settled, so they run on Sonnet and need no question. The WIP cap and the
pilot change what gets built and are his to set.

## Diplomat

**Footing becomes Candour.** The ground matters, and the play is what makes it safe. Candour warns that a move with no
calculation is exposed.

**The missing eyes are the socialized ones.** In the table, the gates where makers fail are the ones that ask how
the work looks to someone else: the hook, the slice playtest and the launch. A studio of one person and agreeable agents has
nobody playing that role. The Diplomat backs two bridges: the Marketer role, which looks at the work as a stranger
would, and a playtester beyond Wendell when a slice is ready. Consent for testers is reserved, so naming them is his.

**Plain words for the roles.** Showrunner, Braintrust, Producer, Builder, Clerk, Researcher, Marketer and Playtester
are everyday studio words that a reader can check. "Lead link", "circle" and "tension" are holacracy's jargon and stay out.

**Marketing starts at the concept, gently.** Zukowski's advice is to put the Steam page up as soon as you share
anything, because wishlists don't age (Game World Observer, 2025). For Sprout, the Diplomat's lean is a hook test
first, one line and one capsule mock, shown to no one until he says.

## Sage

**Estrangement becomes Vigour.** The Sage reached its conclusion from a distance, from files and sources rather than
from play, and says so. Force is available and unaimed; the synthesis aims it at a single pilot.

**Synthesis.** The studio exists under council names. The board is the greenlight meeting, the faces are the Braintrust,
the pipeline's stages are the production schedule, and the battles are the meta-game. The week's work adds four parts:
a gate card per project with its kill line, a cap on strands in production, call sheets that replace long handoffs as
what a session reads, and a Marketer role. The frameworks contribute single rules, not meetings.

**What each face gave.** The Shaman gave the receipt and the rule that the studio should be played. The Architect gave the
mapping table, the four missing parts and the role card. The Challenger gave the kill numbers and the cuts. The Regent
gave gates as definitions of done and kept release reserved. The Diplomat gave the socialized gates and plain role names.
Nothing was dropped. The Player daemon's question about how agent levels rise was not carried forward; see positions.

**The pass was not unanimous.** The Challenger wanted no new artifacts at all and accepts gate cards only on the
pilot, with a kill number. The Diplomat wants the Marketer started now; the Regent holds that any posting waits for his answer.
They agree that the Marketer drafts and nothing goes out.

## Verdicts

| Face | Gate cards | WIP cap | Call sheets | Marketer role | Kegan as lens |
|---|---|---|---|---|---|
| Shaman | yes | yes | yes | yes | yes, never on a person |
| Architect | yes | yes | yes | yes | yes, as a table column |
| Challenger | pilot only, with a kill number | yes | yes, first | later | lens only, no checks |
| Regent | yes | yes | yes | yes, drafts only | yes |
| Diplomat | yes | yes | yes | yes, now | yes |

## Outputs

### Positions (stand unless flipped)

- **st-callsheets.** Root and the council get call sheets of 2-4 KB, read at session start in place of the full HANDOFF,
  which stays as the archive. Clerical work, run on Sonnet. Why it did not need him: the short-sessions rule (CLAUDE.md,
  2026-10-03) and the usage audit's first lever; it changes how sessions start, not what gets built.
- **st-gates-table.** The seven studio gates and the side-by-side table in the report become the studio's map.
  Each gate ends with a greenlight row (continue, pivot, kill), with the default standing unless he flips it. Source:
  `pipeline.yaml` stages and `ship` precedent.
- **st-kill-line-first.** A gate's kill line is written before its work starts. Source: the `falsify` gate ("the result
  that would stop the work") and the Challenger's lesson of 2026-10-03 (a test names the blocker it resolves).
- **st-kegan-lens.** Kegan's stages are a lens on what each gate asks, never a rating of Wendell, a tester or an
  agent, and there is no per-session check. Source: `faces.yaml` `standing`.
- **st-frameworks-cut.** No governance or tactical meetings, no tension log, and no separate advice process. The reach test is
  the advice process and the board holds tensions. Source: the Skeptic's report; the audit's 84% rereading figure.
- **st-roles.** The role table in the report stands. The Marketer and the Producer's cap and receipt are to be defined
  next, and the Clerk gets a domain. Source: the report; Clerk from the audit's Sonnet split.
- **st-marketer-drafts-only.** The Marketer drafts the hook, the devlog and the store copy. Nothing is posted, bought or
  published without his answer. Source: `reserved` (money, consent and release).
- **st-battle-receipt.** A closed battle gets a one-line receipt: the question answered, the face that moved it, any level change, and the session's
  cost read from the platform after the work. Source: the Player daemon; CLAUDE.md "Name the session's cost in its last report".
- **st-level-rule.** An agent's limit rises by his ruling on a board row that the record proposes, not by code alone.
  Source: the Diplomat's lesson of 2026-10-03 ("as a function of how much we trust the agent"); trust is his to grant.
- **st-judge-spend.** The week is judged by weekly spend per gate cleared, against the 4 October week. If process
  threads pass 20% of spend, trim. Source: the audit.

### Questions (passed the reach test)

- **st-wip** (Regent, Challenger). How many projects may be in production at once? Options: two (council lean), three, or no cap.
  Why only he can answer: it is a choice of priority among his projects, and the record holds no ruling on it. Why
  not before: no pass has looked at the studio as a whole.
- **st-pilot** (Architect, Sage). Which project runs the studio gates first? Options: the Big Mind cave (council lean:
  it is at intake now, so gates 0 to 2 cost little), the Skilled Helper encounters, or the Sprout slice. Why only he can
  answer: it is his preference among his projects, and it decides which strand gets the gate card first.
- **st-marketing-start** (Diplomat, Regent). When does Sprout's marketing start? Options: a hook test now, kept private
  (council lean); a hook test at the slice playtest; or after content lock. Why only he can answer: release is reserved,
  and a store page costs money.

## Tests set by this pass, due 2026-10-17

1. The next two Root sessions start at least 25,000 tokens smaller than the last Root session before the call sheet (read from the platform's meter), and open the archive no more than once each.
2. In the pilot, the gate cards change at least one decision. If they change none, drop them.
3. Weekly spend for 2026-10-09 to 2026-10-16 is below the 4 October week's $600-660 (list), with process threads under 20%.
