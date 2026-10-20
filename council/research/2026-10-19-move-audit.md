# What a move is, across surfaces: audit of 2026-10-19

Asked by Wendell on the board, 2026-10-19, overruling `cc-move-sets-element` (ledger
`council/ledger/2026-10-19-pull-223918.json`): "I don't know if move-engine is robust enough for this. We need to do an
audit across surfaces because I Think this is where most drift is happening. We're still figruing out what the
fundamental nature of a move is in the game. 5 channels X 3 satisfaction states sheng ke game master faces and daemons".

Read-only sweep of bars-engine (main), sprout (main, dbcaaa0), Six-faces-council and game-masters-guide, three workers,
one per surface. The two cycle bugs below were checked by hand; the rest is the workers' file:line reading.

## The short answer

He is right that the drift is here. The word "move" names at least nine different objects across the four repos, and
nothing ties them together. The fifteen-move table in `move-engine.ts` agrees with standard sheng and ke and is the
best-built of them, but most code that needs a move does not read it.

| Object called a "move" | Count | Where |
|---|---|---|
| Canonical moves: Transcend, Generative (sheng), Control (ke) | 15 | bars-engine `src/lib/quest-grammar/move-engine.ts:27-57`; ontology yaml:251-256 (count only, no names) |
| Basic Moves: Wake, Open, Clean, Grow, Show | 5 | ontology owner decision 2026-10-10; daemons' work steps; `council/daily.yaml` |
| Within-channel progression: Wake, Clean, Grow, Show | 4 | ontology; bars-engine `primaryWaveStage`, nation moves, transformation registry |
| Clean-up move per channel (Burn it away, Let it flow...) | 5 | board `oag-clean-up-moves` |
| Class moves, one per gate | 8 per class | board `ea12-eight-moves` |
| Face moves | 3 per face, or 4 per face, or 8 per Kotter stage | bars-engine `lens-moves.ts`, `data/face-moves.json`, `gm-face-stage-moves.ts` |
| Vector move keys (metabolize, transcend, translate) | 30 | bars-engine `src/lib/alchemy/vector-move-families.ts` |
| Transformation moves (observe ... integrate) | 8 | bars-engine `src/lib/transformation-move-registry/registry.ts` |
| Sprout's own: push-hands gates, shadow moves, output-card moves, allyship moves, grid ids | 8, 5, 5, 4, 56 | sprout `root-fight/`, `prototype/`, `data/slice.json`, `data/grid.json` |

Six Fundamental Movements (GESTURES.md) are movements, not moves (`dg-six-movements`), and are kept apart.

## Bugs (wrong now, no design question)

1. **bars-engine daily check-in shows the wrong cycle.** `src/components/dashboard/DailyCheckInQuest.tsx:13-18` inlines
   its own tables "from wuxing.ts": SHENG `anger→joy` (sheng run backwards) and KE `anger→neutrality` (that is sheng).
   The server resolves the move with the canonical `wuxing.ts:28-45`, so the target the player sees differs from the
   one recorded. Rendered by DashboardHeader, so live.
2. **bars-engine `packages/bars-core` move-engine is a stale copy** (missing `getMoveFamily`); nothing in `src` imports
   it, and no lockstep test covers it.
3. **Example in `.agent/context/emotional-alchemy-ontology.md:77`** gives `fear:dissatisfied->anger:neutral` as a
   translate; fear→anger is neither sheng nor ke.

## Drift by axis

**Channels (5).** One mapping everywhere: Fear=Metal, Sadness=Water, Joy=Wood, Anger=Fire, Neutrality=Earth. Spelled
five ways in bars-engine (`'Fear'`, `'fear'`, `metal`, `METAL`, `"Metal|Fire…"`). Earth's channel is "Neutrality" in
code and "Neutral" in sprout `docs/design.md:294`, which collides with the satisfaction state "neutral".

**Satisfaction states (3).** dissatisfied / neutral / satisfied in code and on the board (`ss-three-states`); the
ontology yaml:234 has only satisfying / unsatisfying; the Between's garden.js:170 uses Charged / Steadied / Allied; the
schema and daemon spec use uppercase. Metal's satisfied name is "Excitement" (move-engine, alchemy-graph), "Wonder"
(emotional-alchemy/vector.ts:150) and "Wonder-Excitement" (his list, `council/callsheets/somatic-ontology.md:20`).

**Sheng.** Every live site agrees except the check-in bug.

**Ke direction.** move-engine, wuxing, sprout prototype and grid agree (controller → controlled: fire→metal). Sprout
`root-fight/index.html:150,423` answers a ke rally with the element that restrains the attacker (fire answered by
water): a reply relation, not a ke move, and nowhere named as different. Sprout `prototype/index.html` words it both
ways ("Fear restrains Anger" at 5107, "Anger restrains Fear" at 4683).

**What a move does to satisfaction.** The deepest drift, and an open design question:
- Transcend: one move dissatisfied→satisfied, +2 (move-engine, `ss-shift-up`), or two steps (vector-move-families
  splits it into metabolize + transcend; alchemy-graph calls the first step stabilize).
- Generative: +1 (move-engine, wuxing, prototype routing) or same altitude (alchemy-graph `growthPracticeEdgesFrom`,
  move-combinations spec).
- Control: −1 (move-engine, wuxing), same altitude (alchemy-graph growth edges, sprout slice `fight.js:37-40`),
  "holds or pulls back" (sprout prototype:4225), satisfied stays satisfied (ontology-game `game.jsx:2445`), or acts
  only "by releasing grip" (board `ea13b-ke-release`, stands).

**Does a move carry an element?** move-engine says yes (its pair). Board `sf-ally-moves` (stands, 2026-10-13): "Move
elements and spirit ally elements combine but aren't essentially aligned". `cc-move-sets-element` (element derived
from the move) was overruled.

**Faces.** `council/faces.yaml` ties no face to a move. bars-engine holds four maps that disagree: `lens-moves.ts`
(Challenger gets `water_fire`, a clean-up move), `branch-visibility.ts:316` FACE_MOVE_AFFINITY (Challenger: wake and
show only), `face-moves.json` (architect=metal, regent=earth) and `face-recommendation.ts:115` (architect on Joy and
Neutrality, regent on Anger). No face gets `metal_transcend` or `fire_metal`. Sprout's prototype gives each face 5
channels × 3 states of stems.

**Daemons.** Lists of 7 (game.jsx, garden.js), 8 (sprout daemons.json, canonical-operations.ts adds Fear and
Vulnerable Child, drops Emotional Body). Home elements in sprout `data/intake.json` (Protector=metal, Fixer=wood ...)
appear nowhere in the council record. At runtime bars-engine `daemons.ts:14` grants every daemon the same two Metal
moves; channel routing (spec FR10) is not built. Board `sf-moves-from-people` (stands): daemons teach moves.

**Open Up.** None of the fifteen names it; bars-engine's stage list has 4 stages in most places and 5 in
`quest-grammar/types.ts:129`; it means WAVE breathing (owner decision), Idea Storm (daemons), "what's been abandoned"
(daily.yaml) and Happy Apples (`oag-open-up-tools`).

## What runs

bars-engine: move-engine (9 importers), elements.ts, wuxing, alchemy-graph and vector-move-families (via charge
metabolism), lens-moves, DailyCheckInQuest, transformation registry, face-moves.json, the ontology-game build. Dead:
`move-expressions.ts`, `daemon-move-system/types.ts`, `packages/bars-core` copies. Sprout: `slice/*.js` with
`data/slice.json`, `daemons.json`, `intake.json` runs in `npm run slice`; `root-fight/` and `prototype/` are artifact
exports; `data/grid.json` feeds tools only. Sprout copies none of the fifteen names; it re-derives the cycles.

## Not checked

The live claude.ai artifacts sprout's exports came from; the game-masters-guide prose for Generative/Control route
meanings (free-flow pass:54 marks it unread); runtime behaviour beyond import tracing.
