2026-10-14
# Element settings (a cave-like land for each element)

Wendell, 2026-10-14: "we want to make a version of the cave for each element. The cave is primarily a metal setting. So
we'll need a fire setting, an earth setting (mountain?) a water setting (coral reef? Lagoon?) and a wood setting
(forest). ... the settings would be not unlike land in magic the gathering ... maybe we keep water as island". Design
thinking only. Nothing is built.

## Next
Wood first, in its own thread: write one paragraph describing the forest, run it through `rooms/room.py`
(room-from-text) and look at the renders beside the cave's. Wood is first because the forest has the most pieces
already (procgen roots and bushes, the BlenderKit greenery picks, the grass clump). The cave stays the only setting in
the Chapter 1 demo. Positions `el-*` on the board stand unless he flips them.

## The mapping

| Element | Land (Magic) | Setting | Interior |
|---|---|---|---|
| Metal | Swamp | The cave (built) | Chambers, crystal veins, wet stone |
| Fire | Mountain | Volcanic mountain | A caldera or lava tube |
| Earth | Plains | Open plain and standing stones | A barrow under the grass (a plain has no inside, so it needs one) |
| Water | Island | An island | A lagoon, with the reef under it |
| Wood | Forest | Old forest | A hollow under the roots |

Earth takes plains and fire takes mountain because he cannot have the mountain twice; this is the Magic mapping he
named. The game already colours Earth amber, Fire red-orange, Water blue, Wood green and Metal silver-grey
(`STEP_LOOK` in `cave.js`), so each land has a light before it has a model.

## Look and mood

- **Metal, the cave.** Wet dark stone, violet crystal veins, a carried light. Mood: held, clear, sharp edges. Done.
- **Fire, mountain.** Black basalt, glowing seams, ember drift, heat shimmer, a red-orange sky. Mood: urgent, bright,
  exposed. The shellback's fire form already has the basalt and lava seams to copy.
- **Earth, plains.** Wide low light, amber grass, standing stones, a barrow door. Mood: slow, steady, nowhere to hide,
  which is the opposite of the cave's fog. Needs the most care to still feel like a place with edges.
- **Water, island.** Shore, tide pools, shells, a lagoon of still blue with a reef below. Mood: soft, flowing, a held
  breath. The interior is the lagoon, entered by wading in; the reef is the floor of it.
- **Wood, forest.** Trunks, hanging roots, moss, mushrooms, grass, green dusk light through leaves. Mood: growing,
  patient, close. Wendell's 13 October rule stands here: roots and bushes and grass, never underground trees.

## What each reuses from the cave pipeline (bars-engine)

- **Cave studio** (`content/ontology-game/cave/` and the inbox, `cs-*`): his ChatGPT pictures become concept for each
  land; every piece is rebuilt from our own scripts or CC0 models, the same rule.
- **Procgen** (`tools/blender-cloud/procgen.py`, `grow.py`): roots, mushrooms and clusters carry the forest nearly as
  they are; the same growth code gives coral (water), crystal spires and stone clusters (earth, fire), and basalt
  columns. New growth rules, not new tooling.
- **Room-from-text** (`rooms/room.py`): each land's interior (lagoon, caldera, barrow, hollow) starts as a paragraph and
  a `room.json`, so the first look of every setting is cheap and Wendell can write or edit the description.
- **Fog of war** (`carryLight`, `STEP_LOOK` fog and light): the cave hides what is beyond the light. Each land keeps the
  idea with a different hider: smoke and ash (fire), tall grass and dusk (earth), sea mist (water), canopy and
  understory (wood). Nothing new in the code, a different table.
- **Per-charge caves** (`stoneOf`, one stone set per charge colour): becomes one ground set per land, then per charge
  inside it (a numb charge in the forest is mist under the trees).
- **Textures and kit** (`textures.py`, `build_kit.py`): new node textures per land (basalt, grass, sand and water,
  bark), baked the same way.
- **Characters** (J4, J5 garments, NPC warp): the same figure wears each land's weather. No new rig.

## How the settings tie to spirits and the Chapter 1 demo

- **Spirits.** The spirit generator already has five elements (Shellback in all five). A spirit's home setting is its
  element's land, so a wood spirit is met in the forest, which gives the generator's `sg-body-from` and the loot idea a
  place to live. Meridia (Earth) and Virelune (Wood) from `nation-elements` map to plains and forest directly.
- **Charge.** The charge's element chooses the land, with metal the default when it is not known. That is the per-charge
  cave generalised one step.
- **WAVE room.** The seven stretches (Welcome to Exhale) stay the walk in every land. Only the dressing and the light
  change, so one skeleton serves five lands and the hall of the six stays one place.
- **Chapter 1 demo (the Kickstarter gate).** The demo ends in the cave, so the cave stays the only setting for it. The
  other four are post-demo, and stretch goals worth naming on the Kickstarter page. Doing them first would spend the
  demo's time on breadth.

## Waiting on
Five positions on the board stand unless he flips them: `el-mapping`, `el-water-interior`, `el-skeleton`, `el-demo-scope`,
`el-first-setting`. No question reaches him.

## Files
- bars-engine `content/ontology-game/cave/DESIGN.md`, `LEVELS.md`, `rooms/README.md`, `cave.js`, `grow.py`
- See cave-levels.md, chapter1-demo.md, spirit-generator.md, blender-pipeline-test.md.
