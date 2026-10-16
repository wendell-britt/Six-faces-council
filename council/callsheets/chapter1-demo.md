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
| 3D cave | WAVE room, Big Mind cave, levels plan #307 | Walkable skeleton; book-to-cave path (the walkthrough ends in the cave, `ch1-where`) |

## Path to the demo
1. Step 1 of text-to-campaign on Chapter 1: `ch1/extract.yaml` (milestones, lessons, beliefs, the blockages a
   reader hits). Done 2026-10-14: sprout `campaigns/mtgoa-ch1/extract.yaml`, draft PR sprout #52.
2. Step 2: story and teaching NPCs, with Wake Up cards dealt as the player's hand. Done 2026-10-14: sprout
   `campaigns/mtgoa-ch1/story.md`, draft PR sprout #53 (stacked on #52). The Arcade track A1 to A8: Tam (farming),
   Yun (fighting), Ede (exploring); the player in the ally's seat with Pip; seven Wake Up cards; ends in the hollow,
   the 3D WAVE room.
3. Step 3: encounters and the guessing test. Done 2026-10-14: sprout `campaigns/mtgoa-ch1/encounters.yaml` and
   `guessing-test.md`, PR sprout #54 (stacked on #53, on #52). Blocks for A3, A4, A6, A8; Pip's warden and his no for
   good; the hollow spirit's urge-to-family map and naming presets on #51. Card match 12 of 18 (67%) against 85%:
   11 of 12 for players reading for meaning, the fixer plays "Which Fight Is Yours" nearly always. A4 and A8 swapped
   cards; A5's stance card is a keepsake.
4. Blender sprites for the Chapter 1 spirits and NPCs onto the page. Done 2026-10-14: sprout `prototype/ch1-arcade.html`,
   PR sprout #55 (stacked on #54), published for his phone at https://claude.ai/artifact/G4mj4M4zuUeHfWfQx4r6KE. Pip is
   a character-parts look; the warden is the Shellback round 2 Earth creature; the player's spirit is the ascended form
   of the charge's element. The end screen logs the card played at each moment, with a fixer check line for A6 and A8.
   A7's lines 2 to 6 are stand-ins from extract.yaml r3 to r7 until the manuscript's lines are wired.
5. His phone play. Done 2026-10-16 20:41 (step `chapter1-demo-play-01`, note recorded here). He played the Arcade
   once with no complaint about the page. Fixer check: he did NOT play "Which Fight Is Yours" at the hunters' choice
   (A6) or in the hollow (A8). Cards played: A2 What's Actually Scarce, A3 The Story the Lack Tells, A4 What's Going
   Unseen, A6 whole What's Actually Scarce (written: Which Fight Is Yours), A6 hunters What's Going Unseen (written:
   Who's at Risk), A8 hollow The Story the Lack Tells (written: What Doesn't Want Light). So the feared fixer repeat
   did not show, and the late cards did not match: 3 of 6 on his play (A2, A3, A4 match; A6 x2 and A8 miss), against
   12 of 18 on paper. One play is one player, so no card changes yet; his stance was "The one who makes the right move
   easy" and his spirit was fire, controller, named "I like having it handled before anyone asks." The page needed no
   fix. A6 and A8 cards are the open finding: a second playtest (another player, or him as a non-fixer) decides them.
6. A short video for the Kickstarter page. Plan: 60 to 90 seconds, phone-size screen capture of the published page in
   headless Chromium replaying his logged choices (Playwright, 390 px wide). Shots: arcade and Tam, Yun, Ede (10 s);
   dealt hand of Wake Up cards (8 s); Pip's hut and the warden (15 s); the hunters' choice (10 s); the hollow and the
   spirit made from his charge (15 s); end screen with the card log (10 s); title card with the book name and the
   Kickstarter ask (5 s). Captions on screen, no voice. Not started: it waits on his go, since a public video is
   outward-facing.

## Waiting on
- Nothing from Wendell. `ch1-where` answered 2026-10-14: Sprout ending in the cave, 2D or 3D character, all three loops.
- Positions `ch1-source`, `ch1-pipeline`, `ch1-deck-hand`, `ch1-npc-from-blockage` stand unless he flips them.

## Next thread brief
Step 6, the Kickstarter video, waits on Wendell's go. Step 5 is done (above). A6 and A8 card fit needs a second player
before any card changes. Sprout #52 to #55 are stacked and open; merge them in order when he says.
