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
5. His phone play, then fixes; then a short video for the Kickstarter page.

## Waiting on
- Nothing from Wendell. `ch1-where` answered 2026-10-14: Sprout ending in the cave, 2D or 3D character, all three loops.
- Positions `ch1-source`, `ch1-pipeline`, `ch1-deck-hand`, `ch1-npc-from-blockage` stand unless he flips them.

## Next thread brief
Step 5 is his phone play. Put one step on the board's Your steps tab: open https://claude.ai/artifact/G4mj4M4zuUeHfWfQx4r6KE
on his phone, play once as a fixer would (reach for the big moves at Pip's hut), then tap "Copy this" on the end
screen and paste the log into the step's note. Say it takes about ten minutes. Own sprout #52 to #55 (stacked; watch
any still open and drop each watch once it merges). When his note arrives: read the fixer check line (did he play
"Which Fight Is Yours" at the hunters' choice and in the hollow?), fix what the play shows in `prototype/ch1-arcade.html`
and republish the same artifact link, then plan the short Kickstarter video. Lean: he is near his weekly limit.

## His play (2026-10-16 20:41, board read)
Step `chapter1-demo-play-01` done with the log. He played What's Actually Scarce at A2 and A6 whole, The Story the Lack Tells at A3 and A8, What's Going Unseen at A4 and A6 hunters. The cards written for the fixer at A6 (Which Fight Is Yours, Who's at Risk) and A8 (What Doesn't Want Light) were not the ones he played, so the fixer check misses at all three spots. Stance: The one who makes the right move easy. Spirit: fire, controller, named "I like having it handled before anyone asks". Pip line: "The night you knocked, I nearly left. Then you came back with water. That one counted." No complaint in the note.
Next thread (fresh, Sonnet): own sprout #52 to #55. Read what the play shows: he did not reach for the big moves at the hunters' choice or the hollow, so either the fixer cards are not the ones a fixer reaches for or the log shows his own read. Recommended: rework the A6 and A8 fixer cards and blocks from his choices (his three plays are the data), rerun the guessing test, republish https://claude.ai/artifact/G4mj4M4zuUeHfWfQx4r6KE, then plan the Kickstarter video. Not the Big Mind centre play; that waits on its own step.
