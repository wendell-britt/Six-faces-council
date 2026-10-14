# Lenses on the board, pass 1

**Date:** 2026-10-14. **Called by:** the coordinator, on Wendell's message in the thread "Tap the vein on the board"
(18:08 UTC). **Pass:** first on Lens integration; it follows morning menu 1 (2026-10-09).

**The ask, in his words.** "Well also need the full tap the vein process where I intake all the things off the top of
my mind that I can do today and then we check alignment with the current board items. The lenses integration is
probably the biggest bottleneck as our current system doesn't really use lenses"

**Casts** (`council/iching/cast.py`, three-coin method): Shaman 57 Persuasion; Architect 34 Vigour, becoming 38
Estrangement; Challenger 37 Household, becoming 57 Persuasion; Regent 51 Shock, becoming 30 Burning; Diplomat 7
Muster, becoming 29 Depths; Sage 2 Bearing, becoming 22 Adornment.

**Scorecard.** Morning menu 1 set one test for 2026-10-16: one real morning end to end, and the Lenses intake closed
after two domains and reopened with both saved. Not yet run. The intake fixes it tests shipped in bars-engine
`ded88fb` (save each lens as it locks, one lens a morning, edit a single goal).

**Anchor.** Every item on the morning menu bridges to a Lens goal, and the game masters suggest a smaller goal where
none fits (`mm-menu-shape`).

## What the record shows

- **He has no Lens goals.** The export read on 2026-10-14 (`GET /api/tap-the-vein/menu`, his menu sealed 2026-10-13)
  returned `"goals": []`. `loadActiveLensGoals` reads `LensGoal` rows with status `active`
  (`src/lib/tap-the-vein/menu-data.ts:20`), and a domain locked in the intake saves as `active`
  (`src/actions/lens-goals.ts`, `saveYearLensDomain`). So no domain has been locked in.
- **Every board item is unaligned for that reason.** Each item in `board_data.json` `morning.categories` carries the
  bridge `"why": "no Lens goals were read this morning"`.
- **The board only sees goals through a sealed bars-engine menu.** The export returns 404 when no menu is sealed
  there (`docs/morning.md`), and goals ride inside that response. Since #126 he seals on the board, so even a filled
  year frame would not reach the board on a morning he skips bars-engine.
- **The intake itself is built.** Five domains (relationships, career, money, health, allyship;
  `src/lib/lenses/domains.ts`), a ten-minute free write each, up to five kept year goals, then the descent to
  quarter, month and week. His steer on `ya-domains`: "The lenses domains haven't been formalized".

## The faces

### Shaman (57 Persuasion: an effect is already happening that you have not admitted to)

**The effect already happening is that the board runs his mornings without his goals present.** Each morning
item is weighed against nothing, so the menu reads as a to-do list rather than a path. **The free write is where his
goals already speak.** His 18:08 message asks the game masters to read the free write and pitch where each line belongs; the
same reading can pitch year goals, so the intake becomes part of the morning he already keeps instead of an hour
apart. **Risk:** a goal pitched by a model and kept in a hurry is a borrowed goal. The pitch quotes his own line, and
he keeps it in his words.

### Architect (34 Vigour, becoming 38 Estrangement: force is available here and unaimed)

**The machine has force and no aim: goals live in bars-engine and the board reaches them only by way of a sealed
menu.** Three structural pieces aim it. **(1) A goals export,** `GET /api/lenses/goals` with the same council token,
independent of any menu, so `council/morning.py` reads goals every morning. **(2) A Lenses panel on the Morning
tab:** the five domains, his goals under each, an empty domain shown as empty. **(3) Goal pitches:** when a domain is
empty, the board's Tap the Vein box offers that domain's prompt; the read pitches year goals from the sealed free
write exactly as `council/ttv_bars.py` pitches BARs, and each one he keeps is written to bars-engine through
`POST /api/lenses/goals`. bars-engine stays the home of Lens goals (`mm-where`); the board is the front door
(`docs/morning.md`). **Third position:** neither "lenses only in bars-engine" nor "copy goals into the council repo";
the board reads and writes through bars-engine.

### Challenger (37 Household, becoming 57 Persuasion: an arrangement has formed without being discussed)

**The arrangement nobody discussed is that the bottleneck was taken for code when it is data.** The intake was
rebuilt on 2026-10-09 to take one domain a morning, and no domain has been locked. Building three new pieces before
one goal exists repeats that. **Falsification test:** if he locks one domain in the existing intake and the board
still shows nothing aligned, the export is the bottleneck; if he does not lock one in a week, the intake's home is
the problem, and the board pitch is the fix. **Anti-pattern:** word-overlap bridges (`council/morning.py` `bridge`)
on an empty goal list. They will mislead once goals exist too; the read should bridge with a written reason, the way
his ruling asks for BAR pitches.

### Regent (51 Shock, becoming 30 Burning: it went off, and it will go off again)

**Non-negotiables.** Goals are written only to bars-engine, and only the pitches he keeps (`mm-where`, `mm-raw`).
The sealed free write is deleted after the read, as for BARs (`ttv-raw-bars`). The token never reaches the board or
a step. **Phase gates.** Gate 1: the goals export answers and the Lenses panel shows his real domains, empty or not.
Gate 2: one kept pitch appears as an active `LensGoal` and on the panel the next morning. Gate 3: the full intake
bridges each item to a goal and to the board rows it advances. **Done** means a morning where every menu item names
a goal or a pitched smaller goal.

### Diplomat (7 Muster, becoming 29 Depths: what would organise this is a fact you have not said)

**The fact that would organise this is his year goals, and only he can say them.** The bridge for him is the
morning he already keeps: "Today's prompt is Health, because it is empty" asks less than a separate hour-long page.
**Copy:** the panel says "No goals here yet" under an empty domain, never "incomplete". **Onboarding path:** one
domain a morning, five mornings to a year frame, any morning skippable. **For the full intake:** each item he lists
gets one line back, "serves *goal*" or "advances *board row*" or "no home yet: pitch a smaller goal", so the check
reads as help, not a grade.

### Sage (2 Bearing, becoming 22 Adornment: the whole weight of this is yours, unasked)

**Synthesis.** The Shaman, Architect and Diplomat agree the board should both show and fill his Lens goals, and the
Architect gives the shape. The Challenger dissents on order: it wants one goal locked before any build. The two
reconcile: build 1 (goals export and panel) is small and proves the Challenger's test either way, and the goal
pitch (build 2) waits on what that test shows only if he has locked a domain by then. **Order:** build 1, then build 2
(goal pitches from the free write), then build 3 (the full intake with alignment), because the alignment check needs
goals to align to. **Dropped:** the Regent's write-path gate wording folds into build 2. **Deferred:** formalizing the
domains; bars-engine's five stand until he names others (his steer on `ya-domains`). **Dissent flag:** not unanimous;
the Challenger dissents on order.

## Verdicts

| Face | Board shows goals | Board pitches goals | Build order |
|---|---|---|---|
| Shaman | yes | yes, quoting his line | pitch early |
| Architect | yes, own export | yes, via bars-engine | export, panel, pitch, intake |
| Challenger | yes | after one goal exists | his one domain first |
| Regent | yes | yes, kept only | gated 1, 2, 3 |
| Diplomat | yes | yes, one domain a morning | panel first |
| Sage | synthesis | | export and panel, pitch, intake |

## Outputs

**Positions** (each stands unless he flips it on the board):

- `lens-board-reads-goals`: The board reads your Lens goals every morning through a goals export from bars-engine,
  without needing a sealed bars-engine menu, and shows them on the Morning tab under each domain, with empty domains
  shown as empty. Source: the export returned no goals on 2026-10-14, and goals reach the board today only inside a
  sealed bars-engine menu.
- `lens-pitch-goals`: When a domain has no goals, the board's Tap the Vein box offers that domain's prompt. The board
  read pitches year goals from what you wrote, quoting your line, and each pitch you keep is written to bars-engine
  as an active goal. Source: your 18:08 ruling to summarize and pitch; `mm-where` keeps bars-engine as home.
- `lens-intake-align`: The full intake lists what you can do today; the board read gives each item one line: the goal
  it serves, the board row it advances, or a pitched smaller goal. The reason is written, not word overlap. Source:
  your 18:08 message; `mm-menu-shape`.
- `lens-order`: Build order is the goals export and panel first, goal pitches second, the full intake third, because
  the alignment check needs goals to align to. Source: this pass; Challenger's dissent kept.
- `lens-domains-stand`: bars-engine's five domains (relationships, career, money, health, allyship) stay until you
  name others. Source: your steer on `ya-domains`.

**Questions:** none survived the reach test. Where to fill goals and what to build were answered by his 18:08 ruling,
`mm-where` and #126; the domains question is deferred to his steer.

**Step for him** (optional, speeds the Challenger's test): lock in one domain at
https://bars-engine.vercel.app/lenses/onboarding. Ten minutes; it saves as you lock it.

**Tests, dated 2026-10-21:** the Morning tab shows his real domains; at least one active Lens goal exists; one board
morning item bridges to a goal with a written reason.
