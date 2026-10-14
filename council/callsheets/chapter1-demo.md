2026-10-14
# Chapter 1 demo (the Kickstarter gate)

Wendell, 2026-10-14: "We'll be able to do a kickstarter for the Allyship game when we have a working demo of a
gamified chapter 1 which should use the game ontology I'm working on with codex AND the blender pipeline the story
skills and character and NPC generation based on player blockages."

## What the demo needs, and what exists

| Piece | Exists | Missing |
|---|---|---|
| Chapter 1 text | wendell-britt/mtgoa-manuscript `manuscript/ch1.md`, "The Infinite Arcade" (canon, `ch1-source`) | Not yet in this project's repos; the next thread adds it |
| Game ontology | `ontology/` here, v0.1 alpha, design-ontology skill | Nothing to start; updates from Codex land in the same folder |
| Story skills | text-to-campaign move; Skilled Helper Parts II and III in sprout (#38 to #48), 24 of 27 taught | Never run on Chapter 1 |
| NPCs from blockages | spirit generator, sprout #51 (charge makes spirit); WAVE room daemons, bars-engine | His phone play of #51 (`spirit-generator-01`) |
| Fights | spirit fights, sprout #50, build 3 in progress (`sf-stats-carry`) | His play of build 2 |
| Blender pipeline | cave assets J1 to J5, spirit Shellback round 2 (25 models and sprites) | Sprites wired into the Sprout page |
| Allyship Deck | 147 cards, bars-engine `public/allyship-deck/allyship-deck.json`, `/deck` | A place in play: `ch1-deck-hand` makes it the player's hand |
| 3D cave | WAVE room, Big Mind cave, levels plan #307 | Walkable skeleton; book-to-cave path (only if `ch1-where` says cave) |

## Path to the demo
1. Step 1 of text-to-campaign on Chapter 1: `ch1/extract.yaml` (milestones, lessons, beliefs, the blockages a
   reader hits). **Next move, starts now.**
2. Step 2: story and teaching NPCs, with Wake Up cards dealt as the player's hand.
3. Step 3: encounters and the guessing test; the player's own blockage becomes a spirit via #51.
4. Blender sprites for the Chapter 1 spirits and NPCs onto the page.
5. His phone play, then fixes; then a short video for the Kickstarter page.

## Waiting on
- `ch1-where` on the board (Sprout recommended). Step 1 does not depend on it.
- Positions `ch1-source`, `ch1-pipeline`, `ch1-deck-hand`, `ch1-npc-from-blockage` stand unless he flips them.

## Next thread brief
Add wendell-britt/mtgoa-manuscript (list_repos shows it, push allowed). Read `manuscript/ch1.md` and the Skilled
Helper's `extract.yaml` in sprout as the model. Write the Chapter 1 extract in sprout under `mtgoa-ch1/`, draft PR.
Load the design-ontology skill (game_design profile). Opus, one thread.
