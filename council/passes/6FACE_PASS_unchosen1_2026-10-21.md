# What Tap the Vein does with the lines he does not choose

**Run 2026-10-21**, started by the project coordinator from Wendell's message. Pass `unchosen1`, the first on the
subject. Rows: `council/callsheets/rows/unchosen-2026-10-21.json` (seven `uc-*` positions, one question). Ontology loaded
(QUICKSTART, Composting); this pass designs a mechanic. No daemons sent.

**Casts** (`council/iching/cast.py`): the Shaman drew 63, Arrived, with no changing lines. The Architect drew 58,
Banter, becoming 42, Windfall. The Challenger drew 29, Depths, becoming 43, Unsaid. The Regent drew 59, Dispersal,
becoming 44, Serendipity. The Diplomat drew 32, Endurance, becoming 39, Impasse. The Sage drew 60, Measure.

**The ask, in his words** (2026-10-21 16:51 UTC):

> so for the tap the vein inside of bars-engine we need something to do with the ideas that aren't taken during the
> intake so we can see emergent patterns around what's NOT been chosen. These are parts of the pipeline in ways I don't
> quite understand yet, but i know its emotional energy and idea energy that isn't being pulled into our flows of yet

The anchor, in one sentence: the council keeps what the morning did not pick, and shows what keeps coming back in it,
without turning it into a duty.

## Where the intake drops ideas today

A worker read the intake in bars-engine (main, 2026-10-21). Six places lose or ignore what he did not choose:

1. **Raw and composted brainstorm lines** are saved in `TapTheVeinDailySession.brainstormCandidates` (text and fate
   only) and nothing reads them again: the menu skips them (`src/lib/tap-the-vein/menu.ts:405`) and the history API
   does not select the column.
2. **Play lines past the daily task cap** stay play candidates and are never committed (`TapTheVeinRunner.tsx:163`).
3. **Lines past the menu's seven** never reach the sealed menu or the council (`menu.ts:424`).
4. **The faces' suggestions he declines** are never stored: "Leave unaligned" keeps only `lensGoalId: null`
   (`src/actions/tap-the-vein-menu.ts:124`), and the export drops the suggestion (`menu.ts:454`).
5. **Face-off cards he does not pick** on the board: only picks are written (`board/council-board.html`, `picks/<id>`).
6. **The free write itself** is kept as `rawEntry`; what it holds beyond the lines he named is out of reach by his
   ruling `mm-raw`.

Kept on purpose already: composted tasks with their reason, and resting tasks in the seed library.

## What the record already answers

- **Who reads his writing.** `mm-raw` (2026-10-09, "kept"): only lines he keeps reach the council. `ttv-raw-bars`
  (2026-10-14, read then delete), with his steer: "For now read it and delete but this is the power of having a private
  server like in bars engine". `ttv-saved-read-scoped`: the council reads saved free writes only to pitch Lens goals.
- **What a pattern is.** `ttv-lens-emerge`: something is pitched only when it returns, quoting his words from at least
  two mornings with their dates.
- **No pressure.** `sl-no-pressure`: the seed library opens only when he opens it, shows no count, and nothing comes
  back unasked. `ttv-fruit-is-his`: letting go needs no reason.
- **Losing is not avoiding.** `tb-loss-not-avoidance`: a line that keeps losing is read as missing conditions.
- **Composting.** Ontology QUICKSTART, Composting: composting ends an obligation; "Compost may nourish future growth,
  but it does not owe the garden a harvest"; later reuse needs its own decision.
- **Spirits and qi.** `sg-charge-disc`: a spirit is born from a charge worked through the whole W.A.V.E.
  `cw-qi-meter-scales`: qi is filled by practice. `gs-harvest-is-qi`: harvested energy is qi.

## The faces

- **Shaman** (63, Arrived: what is finished has one way left to move). The morning feels finished at the seal, and
  what it left out is where it starts moving again. An unchosen line is still his charge, unspent. It should be seen
  the way he wrote it, in his words, with the day, and never in a summary of him.
- **Architect** (58 becoming 42: the exchange is the whole of it, and more arrives than went in). Rung 2 of the tool
  ladder holds: the lines are already saved in bars-engine, so the first build only reads them. One pure function
  sorts a session's lines into chosen and unchosen (a task's original text, or a sealed menu line, is chosen; anything
  else is not), and a second counts which words return across mornings. No schema change. Drop points 2 and 3 are
  covered by the same read, because those lines are still in the candidates as play. Points 4 and 5 are the council's
  own offers and need a write; that is a second build.
- **Challenger** (29 becoming 43: the pit has another pit, and one sentence is unsaid). Two failures to guard. First,
  the pile turning into a backlog that stares at him; so no count, closed by default, no reminders. Second, a word
  count passing for meaning: "garden" coming back on four mornings says it returns, not what it wants. The view says
  "keeps coming back" and never "you keep avoiding". The unsaid sentence: the council's declined suggestions are a
  different pile from his unchosen lines. They measure the council's aim, not his energy, and should not be mixed in.
- **Regent** (59 becoming 44: rigidity disperses; building on one piece of evidence). Consent is reserved
  (`faces.yaml`). His rulings let bars-engine keep his lines and let the council read only kept lines. Showing him his
  own lines inside bars-engine, with no model reading them, is inside both rulings. A council or model reading the
  unchosen pile is not, and only he can widen it. Composted lines stay composted: they can show as residue in a
  pattern, and nothing in this view draws them back.
- **Diplomat** (32 becoming 39: a motion that repeats; turn back and come again with others). The view must work with
  no AI at all, because the non-AI path is first class (bars-engine `CLAUDE.md`). His hand stays on every move: a line
  goes back into a day only when he draws it. The links he named (qi, compost, spirit seeds) fit loosely. The daily
  compost pass sorts board steps, not his lines. Qi is filled by practice, so an unchosen line is not spent qi. A
  pattern can become a spirit only the way any charge does, by his taking it through the W.A.V.E.
- **Sage** (60, Measure). Reach test: each candidate question went back to its face with the record. Where to keep
  the lines: the record answers (`mm-raw`, his steer on `ttv-raw-bars`: bars-engine). What a pattern is:
  `ttv-lens-emerge`. Pressure: `sl-no-pressure`. Composted lines: the ontology's Composting rule. Links to qi and
  spirits: `sg-charge-disc`, `cw-qi-meter-scales`. One question is left that the record cannot answer and only he can:
  may the council read the unchosen pile, which his `mm-raw` ruling keeps from it? It changes what gets built next.
  The pass was not unanimous on one point: the Challenger wanted the council's declined suggestions kept out of the
  view entirely; the Architect wanted them on the same page in a second section. The positions follow the Challenger
  and keep them in a separate store; the dissent is recorded.

## Verdicts

| Face | Keep the lines | Where | Patterns | Council's misses | Links |
|---|---|---|---|---|---|
| Shaman | yes, his words and day | bars-engine | by return | separate | his to make |
| Architect | yes | bars-engine, read only | words by mornings | second build, same page | none forced |
| Challenger | yes, no count | bars-engine | "keeps coming back" | separate store | none forced |
| Regent | yes | bars-engine; model reading is his call | by return | separate | composted stays |
| Diplomat | yes | bars-engine, no AI needed | by return | separate | W.A.V.E. by his hand |

## Positions (stand unless he flips them)

1. **`uc-keep-unchosen`.** Every brainstorm line he named and did not choose is kept in bars-engine with its morning
   and what happened to it: left raw, composted, or marked play and not picked (including lines past the day's cap or
   the menu's seven). Nothing is deleted. Today is not judged until the next morning.
2. **`uc-not-chosen-view`.** Tap the Vein gets a "Not chosen" section under the seed library, and on the opening and
   sealed screens. It opens only when he opens it and shows no count while closed. It lists past mornings' unchosen
   lines in his words, newest first.
3. **`uc-pattern-returns`.** A pattern is a word that comes back on two or more mornings, counted by mornings, at most
   five shown. Tapping one shows every line it came from with its date. It reads "keeps coming back", never avoidance.
4. **`uc-no-duty`.** An unchosen line owes nothing: no reminders, no resurfacing, never a task unless he makes it one.
   Composted lines show muted as residue and are not offered back.
5. **`uc-council-misses`.** The faces' suggestions he declines and the face-off cards he does not pick are the
   council's misses, not his unchosen energy. A later build stores them apart, so the council can measure its own aim.
6. **`uc-links-by-hand`.** Nothing is converted to qi, vibeulons or spirits. A pattern becomes a spirit only the way
   any charge does, when he takes it through the W.A.V.E. The daily compost pass keeps to board steps.
7. **`uc-first-build`.** First build: the read-only "Not chosen" view in bars-engine, from data already saved, with a
   test. Next build: "Draw into today" on a raw or unpicked line, then the council's misses store.

## Question (passed the reach test)

**`uc-who-reads`.** May the council read your unchosen lines to find patterns? The Regent owns it, with the Diplomat.

- **A. Only you, in bars-engine.** The view counts words with no model. The council never sees the pile.
- **B. The council reads them once a week, in place (recommended).** A board read reads the pile in bars-engine, keeps
  no copy, and writes back at most five patterns, each quoting your lines from two or more mornings with dates. The
  no-AI view works either way.
- **C. Only lines you mark.** Each unchosen line gets a "show the council" tick; only ticked lines are read.

Why only he can answer: who reads his private writing is consent, reserved to him in `faces.yaml`, and his `mm-raw`
ruling keeps unchosen lines from the council. Why not asked before: until today the unchosen pile had no use; `mm-raw`
was about the free write reaching the council, before the brainstorm kept lines it ignored.

## Test

UC1, 2026-11-04: open "Not chosen" after two weeks of mornings. It holds every raw, composted and unpicked line from
those mornings and none he chose; each pattern names at least two dates; nothing in it changed his day.

## Recommended next move

The first build is in bars-engine (pull request on branch `claude/project-thread-82q0y7`): `src/lib/tap-the-vein/unchosen.ts`
with its test, the action `getUnchosen`, and `src/app/tap-the-vein/Unchosen.tsx`. Not checked: real data, since the view
reads his sessions behind his sign-in.
