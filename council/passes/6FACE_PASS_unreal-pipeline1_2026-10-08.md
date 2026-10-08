# Unreal, Blender and Meshy for games from the ontology: a six-faces pass

**Run 2026-10-08**, called through the project coordinator on Wendell's message in the Sprout Game project at 19:56 UTC.
This is the first pass on the subject. The plan it shaped is in the project files at `unreal-pipeline/plan.md`.

**The ask, in his words:** "Also interested in exploring how to use unreal + blender + opus for creating other types of
games based on the ontology". He quoted a tweet (rewind02) giving the pipeline: Meshy makes the models, Blender cleans
them, Unreal is the game, Claude runs all three from one chat; "one full first build took about 4 hours and ~19% of a
weekly Max plan".

**Inputs:** the usage audit (`/mnt/project-files/usage-audit/audit-2026-10-04.md`) and connector audit (5 October); project
memory on the dungeon rule (3 October), the character look (4 October), the WAVE playtest steers and the daemons and
spirits pass; Sprout's CLAUDE.md (asset ids, licence audit); Root's CLAUDE.md; the CLAUDE.md short-sessions rule; Meshy's
docs, the Blender MCP setup page and uemcp's PyPI page. No daemons were sent: the problems were cost arithmetic and tool
lookup, done directly. `council/due.py --ahead 7` lists nothing due.

## Scorecard

No earlier pass on this subject set tests.

## The anchor

Find out what a Claude-driven 3D pipeline would take for Wendell, and plan it so the first build tests the pipeline on a
design the project already holds, at a cost the audit can defend.

## The casts

- shaman: 1 Unbroken (乾), changing to 57 Persuasion
- architect: 37 Household (家人), no changing lines
- challenger: 12 Stalemate (否), changing to 35 Sunrise
- regent: 55 Fullness (豐), no changing lines
- diplomat: 33 Retreat (遯), no changing lines
- sage: 22 Adornment (賁), changing to 21 Bite

## Shaman

**Unbroken, changing to Persuasion:** "Every line here sends, and the return has nowhere to land." The tweet is all
sending: generate, import, light, add a feature. The return is Wendell playing it.

**What moves underneath is appetite for a bigger canvas.** Sprout is bounded by the SNES profile; Root is the one break
and has cost weeks. A 3D world where the daemons and spirits stand in rooms is the felt pull. **The risk is a second
Root:** a fight game in 3D would pull straight into contact physics. **The recommendation is a game whose return lands
early:** walk into a room, meet a daemon, pass by the lesson. The Cave of Lessons does that.

## Architect

**Household:** "An arrangement has formed here without being discussed." The tweet's arrangement, one tool per job, is
sound; what it leaves undiscussed is where the design lives.

**The record keeps the design, the tools keep the assets.** The repo holds prompts, scripts, the manifest and
HANDOFF.md; the binary Unreal content stays on his machine until the slice is worth keeping. **Game data refers to asset
ids, never paths**, the rule Sprout already has, carried over as the manifest. **Pick the Unreal bridge with no compiled
plugin** (uemcp over Unreal's built-in Python remote execution), because a plugin is rebuilt per engine version. **The
machine reports its own GPU** in session 1; the tweet's "tell it your GPU" becomes a script, so no question goes to him.

## Challenger

**Stalemate, changing to Sunrise:** "You are seeking one game and wearing the face of the other." The tweet sells a
four-hour build; this project's rule is short sessions.

**What breaks is the single long session.** By the audit, 84% of spend is rereading; viewport screenshots grow the
context fast. Four hours in one session lands near the tweet's 19%, about $230 to $250 of his week at list prices
(the week is inferred at $1,200 to $1,300 from the audit's half-in-three-days). **Self-inflicted risk:** "add one feature
per prompt" in one chat. **Falsification tests:** session 1 proves each of the three bridges with one small action
before anything depends on it; the slice's total cost is read from the platform after each session, and if it passes
$200 the build stops and reports.

## Regent

**Fullness:** "This is at its peak and you are saving some of it." Hold some back: three rooms, not eight.

**Phase gates:** setup (his steps), session 1 (bridges proven), session 2 (one prop through the scripted pipeline with a
manifest entry), sessions 3 to 6 (props, rooms, character, encounter), then his playtest. **Definition of done for the
slice:** he walks through three rooms and passes one daemon by its lesson. **Non-negotiables:** money is his (reserved),
so the Meshy plan is a board question; the character look ruled 4 October holds; no third-party art is treated as
cleared; Root is not ported.

## Diplomat

**Retreat:** "Leaving is available, and the timing decides what you keep." Nothing here needs starting now; his setup
steps are the start, so he chooses the timing.

**The bridge is Meshy's paid licence:** models made on a paid plan are his privately, so this game's art starts cleaner
than Sprout's unconfirmed sources. **Onboarding path:** the steps are written for his operating system once the Meshy
plan is chosen, and land on the board's Your steps tab, not in chat.

## Sage

**Adornment, changing to Bite:** "You have dressed this, and the dressing is doing real work." The five game ideas are
dressing; the pipeline test underneath is the work. "An object is lodged in here, and nothing closes until you say it":
the game pick and the money are his.

**Contributions:** the Shaman chose the game by where the return lands; the Architect placed the design in the repo and
turned the GPU question into a script; the Challenger priced the tweet against the audit and set the stop; the Regent
cut the slice to three rooms; the Diplomat tied Meshy's licence to the licence audit. **Dissent:** the Shaman wanted the
push-hands arena listed first for its pull; it stays second because of contact physics. The pass was otherwise
unanimous, which is a flag: every face read the same audit, and none tested the tools on a real machine.

## Verdicts

| Face | Game pick | Meshy plan | Session shape |
|---|---|---|---|
| Shaman | Cave of Lessons | paid | short |
| Architect | Cave of Lessons | paid | short, scripted |
| Challenger | Cave of Lessons | Pro, one month | short, with a $200 stop |
| Regent | Cave of Lessons | his call | gated |
| Diplomat | Cave of Lessons | paid, for the licence | short |

## Outputs

### Positions (stand unless he flips them)

- `up-short-sessions`: the first build runs as about six Remote Control sessions, each ending in HANDOFF.md, not one
  four-hour session. Cited: CLAUDE.md short-sessions rule; usage audit.
- `up-gpu-by-script`: session 1 reads the machine's OS, GPU and memory and sets the graphics budget. Cited: a script can
  answer it, so the reach test fails.
- `up-repo`: a new repo, `wendell-britt/calrunia-3d`, holds design, prompts, scripts and the manifest; binary Unreal content
  stays local until the slice is kept. Cited: Sprout's asset-id rule.
- `up-cost-stop`: the slice stops and reports if its measured cost passes $200 at list prices. Cited: usage audit.

### Questions (passed the reach test)

- `up-game-pick` (Shaman, Regent): which game first. His preference; it changes everything built. Not asked before
  because this is the first pass on the subject.
- `up-meshy-plan` (Regent, Diplomat): which Meshy plan, if any. Money is reserved in `faces.yaml`.

### Tests, dated

- By the end of session 1: each of the three bridges has done one small action on his machine.
- By the end of the slice: its measured cost is recorded beside this pass's estimate of $90 to $210.
