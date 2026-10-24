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

## 2026-10-24: art direction round 1 done

- Page: https://claude.ai/artifact/HqbQ5Y1qfX2HxyrHCmeRub (source and files in /mnt/project-files/ship-art-direction/:
  ship-art-direction.html, stills/ with scripts and art-director-review.md, refs/ with credits.json, first-60-seconds.md).
- Still A (2D, SVG in Playwright): the fox spirit leads you across the clouds to a grown shell ship. Still B (3D, three.js
  0.160 + average-dusk.glb): through the hull's round door, a garden island, the spirit barn and a world ring. The CCGS art
  director recommends both in order. Known gaps: A's fox is the washed house sprite; B's ring reads as a quilt, bud small.
- Board: question `sd-still-pick`; positions `sd-dock-scrapped`, `sd-depth-rule` (rows/ship-art-2026-10-24.json).
- scout: rung 2, house tools reused (spirit boat sprites, Average Dusk, three.js, Playwright); no Cradle cloudship art
  exists online.

## Brief: Living ship build (TRIGGER: his yes on sd-still-pick)

One fresh Opus thread. Start from his pick and note. If A (both): build Still B first in three.js on bars-engine, as the
new /calrunia/arrive (the passport fold in guest.js and the arrive page's plumbing stay; drop the Kenney pirate ship,
the dock and vessel.js's grid panel as views). The island's size and light are inner energy (embers and fuel), spirits
aboard live on the island, new chambers bud from inner work; nothing is counted on screen (sd-depth-rule). Then Still A
as the 2D reveal at the end of Chapter 1 in sprout. Use the CCGS roles (art director, UX, systems designer) as a fixed
step: a still or render check before each push. Hosted preview link at the exact state in every reply. Also: write
sd-depth-rule into the design ontology (ontology/ change in the same round, via a council pull request).
bars-engine #399 stays a draft until this lands; then close it in favor of the new pull request.

## Next

1. SUPERSEDED 2026-10-24 (dock scrapped, see Brief: Living ship build). Was: his look at the dock on his iPhone (preview link in the bars-engine pull request). A note naming a change: a fresh Opus thread on bars-engine
   branch `claude/inner-vessel-build-vqaqgw`. Next build items, in order: fuel mined in the cave itself (crystal veins),
   the living ship's voice (the C part of his answer), Kenney Space Kit art for parts, a third-person view of the hull.
2. Tests due 2026-10-25 (destination count; paper card test only if he offers an evening), 2026-11-01 (G1 probe),
   2026-11-08 (five newcomers). Details at the end of the pass.

- 2026-10-21, from Ari's playtest of the Between (pass `between-ari1`, `council/passes/6FACE_PASS_between-ari1_2026-10-21.md`): Ari asked for a private space for spirits "like the barn in Stardew valley", loved "the gummy ship with a farm inside of it", and resonated with worlds rendered procedurally only as far as the player can see or travel. Stored here (`ba-barn-in-ship`, `ba-worlds-stored`): the barn lives inside each person's ship; the farm grows what spirits leave, with no yields or counts; procedural worlds belong to the ship's world after Chapter 1 and the engine question. Nothing built before his look at the dock.

## 2026-10-24: the dock is scrapped; art direction round (thread "Redo the ship dock art direction")

- His interview, round 1 (2026-10-24 01:56 UTC), recorded as rulings:
  - Look: "Toy pirate ship didn't match the vibes of the cave of lessons or the Between." The Kenney Pirate Kit dock goes.
  - Cabin: "The grid and gauge panel I didn't enjoy ... It was quite sophomoric and not particularly context aware."
    "We need a design language that consistently creates immersive experiences."
  - Stepping aboard: "either needs to be an inviting image like the current art direction for the council board as spirit
    boat OR it needs to be an explorable space like the cave of lessons. It need to bring people deeply and emotionally
    into the world and we keep making flat dashboard surfaces."
  - Principle he named: depth mechanics as part of our UI and game design principles. "The shadow of the diplomat is
    flatland ... it's also boomeritis and it's the shadow of integral green. Our job is to bring depth back into green.
    Depth and altitude as a way to pull them out of their flattened world via play."
  - Ship: a sky ship or a space ship. The references were No Man's Sky and the Kingdom Hearts gummy ship; "we landed on
    pirate ship which told me we didn't pull any reference images from this game inspirations".
  - View: walking around it in third person matters for learning 3D, and the story must play in both 2D and 3D, the way
    the asset pipeline works now.
- Next in this thread: interview round 2 (arrival from Chapter 1, the spirit barn, spirits aboard), then reference board
  with real images from No Man's Sky and the gummy ship, first 60 seconds, 1-2 mood stills. Code waits on his yes.
- Ontology check (2026-10-24): no rule for immersion, explorable space or depth; faces.yaml has no shadow fields. Nearest
  hooks: QUICKSTART principle 9 ("Mystery rewards inquiry") and the unpromoted source line where he chose "their imagery
  becoming explorable world material" (aesthetic-source-research-round-1.md:511-515). The dock pass loaded the default
  ontology and used neither for immersion. Verdict: not in the ontology. Proposed with the stills: a depth principle
  (every surface is an inviting image or an explorable space; depth and altitude as play against flatland).
- His interview, round 2 (2026-10-24 02:06 UTC), recorded as rulings:
  - Arrival: "spirit leads you to it and you see it from the outside".
  - Barn: "it's a world inside the ship that could potentially end up bigger than this ships this is not unlike the
    world ring in sprout. It represents the internal energy available for Taking action in friendcraft or flirtcraft of
    allyship".
  - Alive: "It grows new rooms as you do inner work. The spirits and people inside the world and the emergent story is
    what makes it feel alive".
  - References: "Will wights cradle cloud ships. The tardis, the south meditation ship from Star Wars expanded universe.
    Zonoma Sekot and the ship relationships between characters in Karen Lords best of all possible worlds" (plus No
    Man's Sky and the Kingdom Hearts gummy ship from round 1).

## 2026-10-24: living ship build, part 1 (Still B) done

- bars-engine #432 (draft, branch `claude/project-thread-qi3hnv`): Still B as the new `/calrunia/arrive`, three.js 0.160.
  World from the record in `content/calrunia/arrive/ship-world.js` (energy -> island size and light, spirits live on the
  island, embers -> chambers at the rim, vibeulons -> gold motes, cards on a board by the den). Tap to walk, the spirit
  greets you at the door and leads. Kenney ship, dock and the grid panel removed; cave's ship button walks here.
  Skip-ahead `?demo=1`, `?demo=grown`, `?at=island|den|bud`. #399 to be closed in favour of #432 once #432 lands.
- Council #381 (draft): sd-depth-rule written into the ontology as binding decision `depth_over_flatland`.
- Not checked: a real iPhone's frame rate; a real passport from Sprout's last link.

## Brief: Still A reveal in sprout (next, fresh Opus thread)

Build Still A (https://claude.ai/artifact/HqbQ5Y1qfX2HxyrHCmeRub; source and SVG script in
/mnt/project-files/ship-art-direction/stills/still-a.js) as the 2D reveal at the end of Chapter 1 in wendell-britt/sprout
(add_repo it; no CI). The player stands on the floating stone; the fox spirit walks out on air leaving lights; the grown shell
ship hangs in the clouds; the player taps to step after the fox across the lights to the round door, which opens to
Sprout's existing last link to bars-engine `/calrunia/arrive#p=...` (passport fragment). Fix the art director's gaps first:
the fox painted as a spirit (not the washed house sprite), the player standing still in wonder, a less regular whorl.
Nothing counted on screen (sd-depth-rule). CCGS art-director still check before each push. Hosted preview link with
`?beat=` skip-ahead to the reveal. Read docs/3d-math.md only if 3D is touched. After it lands, the owning thread also
watches bars-engine #432 to merge (it merges by itself when checks pass) and then closes #399.

## 2026-10-24: Still A reveal built (sprout #73)

- sprout #73 (draft, branch `claude/project-thread-xkvw0j`): Chapter 1 now ends on beat A9 `ch1.a9.the-ship`. Still A
  is a painted 2D cutscene: the player stands still on the stone, looking up; a fox made of light walks out onto the air
  leaving lights; three taps follow it to the round door, and the door opens onto `/calrunia/arrive#p=...` with the
  passport. The backdrop is painted by `tools/build-ship-reveal.mjs` (wide, plus a tall version for a phone) from
  `REVEAL_LAYOUT` in the page. The art director's gaps are fixed: the fox is painted as a spirit, the player stands
  still, the whorl is an uneven nautilus. A8's "ship at a dock" line is gone. `test-ch1-page` taps through to the
  arrival with a passport.
- Previews: reveal https://sprout-6rbb4w7wy-wendells-projects-9c1b16dc.vercel.app/ch1/?beat=ch1.a9.the-ship&arrive=https://bars-engine-git-claude-projec-dae56e-wendells-projects-9c1b16dc.vercel.app
  and inside https://bars-engine-git-claude-projec-dae56e-wendells-projects-9c1b16dc.vercel.app/calrunia/arrive?demo=1.
- bars-engine #432 checks are green. Council #381 has no checks. Both are still drafts and wait on his look.
- Board: question sd-ship-look-1 (rows file council/callsheets/rows/ship-reveal-2026-10-24.json).
- Not checked: frame rate on a real iPhone.
- TRIGGER: his answer on sd-ship-look-1. A or B: a Sonnet thread marks sprout #73, bars-engine #432 and council #381
  ready, lets them merge, then closes bars-engine #399 as replaced by #432. C: a fresh Opus thread starts the second
  round from his note. After the merges, the next art round is Still B's gaps (ring terrain, the floor light, the bud).
