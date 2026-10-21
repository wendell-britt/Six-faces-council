# Inner vessel: a ship for inner space and the world it travels

ontology: default; touches: BAR, MovementFinding, CompostingDisposition

## 2026-10-18: pass inner-vessel1 done

- Ask: Wendell, 2026-10-18 23:26 UTC, Gummi Ship plus No Man's Sky plus Galactic Starcruiser, a customizable vehicle
  for inner space, and an inner world grown from daemon work, 321 and WAVE.
- Pass: `council/passes/6FACE_PASS_inner-vessel1_2026-10-18.md`. Research, grounding and scout:
  `council/research/2026-10-18-inner-vessel/`. Board rows: `council/callsheets/rows/inner-vessel-2026-10-18.json`.
- Shape the council backs: the WAVE room carried inside a small hull; a sample ship that flies from minute one; any
  finished route (worked, preset, symbolic, fictional) gives one ember; the move sets element, intensity sets look,
  the player picks the kind. Ten bounds in the Sage's list. Dissent kept: Challenger defers the vehicle; Architect,
  Shaman and Regent wanted practice to set the kind.
- Positions (stand unless flipped): `iv-look-only`, `iv-element-by-move`, `iv-kind-chosen`, `iv-no-bonus`,
  `iv-daemon-not-part`, `iv-no-private-decay`, `iv-no-mirror`, `iv-lineage`, `iv-cave-only`, `iv-private-line`,
  `iv-cc0`, `iv-starcruiser`.
- Questions on the board: `iv-q-what-ship`, `iv-q-between-only`, `iv-q-demo-order`.

## Gates (Regent)

- G0 scope: scout lines (below), the component-to-binding table, the ember slice merged (bars-engine #379 and the hearth).
- G1 probe: pure data model and tests (Architect's V1 to V7, with V3 and V4 rewritten for `iv-kind-chosen`).
- G2 preview: voice_lint clean, a paper ship sheet that plays whole, iPhone-size WebKit. The name question comes back here.
- G3: `bh-device-gate` on his iPhone. G4: his look on the board.
- Stop if a stat grows with intensity or volume, a daemon becomes a target, a part needs disclosure, a record is put to
  a new purpose, an asset is not CC0 or ours, or an element land is built before the demo.

## Scout lines

- scout: 5 snap grid and fit rule, ~150 lines of TypeScript drawn with pixi.js (in bars-engine). No library search spent yet.
- scout: 4 part art, Kenney Space Kit, CC0, https://kenney-assets.itch.io/space-kit (confirm format; add to toolbox.yaml when used).
- scout: 2 route map, @xyflow/react (in bars-engine).
- scout: 2 places, the cave as built; element lands wait for after the demo.
- scout: 5 component table, a typed table in code, no Prisma model.

## 2026-10-19: his answers, and the dock build

- Answers (`council/ledger/2026-10-19-pull-223918.json`): `iv-q-demo-order` B (a WAVE-room dock in the demo),
  `iv-q-between-only` A (lift it for the private ship), `iv-q-what-ship` B with his steer: "Honestly a mix of all three
  is what I'm looking for. Probably B that extends to A (from the 3rd person aesthetic) and the story of whatever game
  emerges (probably the single player version) is the living ship you have a relationship with."
- Overruled: `iv-no-mirror` (charge is a fuel gauge, mined from environments like No Man's Sky; spirit energy powers the
  ship), `iv-no-bonus` (the bonus carries over), `iv-cave-only` (places are reached from the ship; the ship does not
  travel to them), `iv-starcruiser` (the model is *Spacecruiser Inquiry* by A. H. Almaas; Galactic Starcruiser stays only
  as a model for an immersive voyage event). Steer kept on `iv-daemon-not-part` (stands): an ally daemon can make parts.
- Open tension: `cc-move-sets-element` is overruled pending a move audit across surfaces, while `iv-element-by-move`
  stands. The dock uses the worked charge's own element and leaves the move out until the audit lands.
- Built: bars-engine `content/ontology-game/cave/vessel.js` (model, store `oag.vessel.v1`, dock panel) and
  `vessel-test.mjs` (11 checks, plain node). The WAVE room has a "The ship" button; a charge worked through the whole
  W.A.V.E. gives one ember (a 3-2-1 one when worked by 3-2-1, with the bonus as fuel); an ally daemon makes one part;
  ending a visit to the hall or the Big Mind cave mines fuel; spirits aboard raise the tank and add fuel on each run.
- Positions taken for the build (board rows `iv-fuel-economy`, `iv-demo-ungated`, `iv-ally-part-once`,
  `iv-bonus-as-fuel`, `iv-element-until-audit` in `rows/inner-vessel-2026-10-19.json`; stand unless he flips them): start 3, tank 6 plus each aboard spirit's stage, waking a
  part costs 1, a visit mines 2, the bonus gives 2; built places are charted from the start so nothing on the demo path
  waits on fuel; fuel is spent on waking parts and, after the demo, on charting element lands.
- scout: 5 hull grid and fit rule, hand-built in vessel.js (a 3x3 grid in DOM; pixi.js not needed at this size).
- scout: 5 fuel gauge, a counter and a cap in vessel.js; no library fits a single number.
- Not checked yet: the dock on his iPhone (G3); the Kenney Space Kit art (parts are labelled cells for now).

## Next

1. His look at the dock on his iPhone (preview link in the bars-engine pull request). A note naming a change: a fresh Opus thread on bars-engine
   branch `claude/inner-vessel-build-vqaqgw`. Next build items, in order: fuel mined in the cave itself (crystal veins),
   the living ship's voice (the C part of his answer), Kenney Space Kit art for parts, a third-person view of the hull.
2. Tests due 2026-10-25 (destination count; paper card test only if he offers an evening), 2026-11-01 (G1 probe),
   2026-11-08 (five newcomers). Details at the end of the pass.

- 2026-10-21, from Ari's playtest of the Between (pass `between-ari1`, `council/passes/6FACE_PASS_between-ari1_2026-10-21.md`): Ari asked for a private space for spirits "like the barn in Stardew valley", loved "the gummy ship with a farm inside of it", and resonated with worlds rendered procedurally only as far as the player can see or travel. Stored here (`ba-barn-in-ship`, `ba-worlds-stored`): the barn lives inside each person's ship; the farm grows what spirits leave, with no yields or counts; procedural worlds belong to the ship's world after Chapter 1 and the engine question. Nothing built before his look at the dock.
