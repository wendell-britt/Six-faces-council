2026-10-18
ontology: none; touches: the cave demo's controls, title screen and first-time teaching (bars-engine content/ontology-game)
# Game demo: the walker and the in-game walkthrough

Wendell, 2026-10-18: "The big change is I want to pull the average dusk walker into the game. And I want to create a more
ergonomic demo so it looks like a game and gives players a walkthrough introduction to the features but from inside the
game itself". Default taken: "the game" is the 3D cave game on bars-engine.vercel.app (/ontology-game/cave and Big Mind).

## Built
- **Walker in the game** (bars-engine #381, merged 2026-10-18): Average Dusk, rigged with Rigify by
  script and walking CMU mocap 35_01 (#378's `rig_mocap/run.py`), exported by `rig_mocap/export_walker.py` (two bones a
  vertex) and baked by `bake_daemons.py --walker` to `cave/player/walker.glb` (125 KB, 6,328 triangles, 35 joints). cave.js
  `wearWalker` puts it over the player's stand-in in the cave, the WAVE room and Big Mind; the stand-in's joints keep
  moving unseen, so gait tests and footfalls still hold; with no network the stand-in stays. The clip turns once per two
  steps of the game's walk clock; standing holds the clip's passing pose and breathes. cave-test checks it is worn and
  the clip turns. Foot slide measured (FK on walker.glb): the clip steps 1.34 game units at 1.7 steps a second, so at
  the game's 2.5 the legs cover 3.4 units a second against the walk's 7; playback alone would need 5.2 steps a second
  (scurrying), so it was left. 7 is a jog for this figure: the fix is a CMU jog clip, or blending one in above a walk.
  Not checked: which foot lands on the footfall sound, and the charge looks (tightness narrow, numbness fogged) on the new body.
- scout: 2, our own rig_mocap (#378) and the daemon body format; rung 4 (one worker search) found no plain three.js
  tutorial library; nipplejs, animouse and three-mesh-bvh noted, none needed for the walker.
- **PR 1, title as a game screen** (bars-engine #382, ready, waiting on Wendell's play of the preview
  https://bars-engine-git-claude-projec-f3ad4b-wendells-projects-9c1b16dc.vercel.app/ontology-game/cave ): the cave mouth
  in 3D (kit arch, tunnel, spires, caps) with the walker standing in it, breathing, its light at the chest; Continue
  (`oag.last.v1`, written by the room, the cave and the Big Mind door; else a Big Mind save with a voice met), Begin
  (body map then the WAVE room), a link straight into the cave, and a gear: Sound (Big Mind's mouth sound obeys it),
  Still motion (follows the device until set; cave's reducedMotion follows it), Show the walkthrough again (clears
  `oag.tutorial.v1`). cave-test 393/0 with seven new title checks, bigmind-test 520/0. scout: 2, all on the page already.
  Not checked: a real phone's frame rate, Continue into Big Mind on a real save, screen-reader order.

- **PR 2, The Arrival** (bars-engine #383, draft, stacked on #382; retarget to main once #382 merges; preview
  https://bars-engine-git-claude-projec-0326eb-wendells-projects-9c1b16dc.vercel.app/ontology-game/cave ): a new player's first
  WAVE room opens with its page tucked away; the chest light floats to each lesson with one glyph and no words (walk, look,
  tap the floor on a spot in view, sit on the rug, the nearer door, with an edge arrow when it is out of view); each goes for
  good once done, in any order; "I know this" (fixed at the bottom) skips one; ids kept in `oag.tutorial.v1`. The round-1
  walking paragraph is gone. From the board the page stays up and lessons wait for Look around. cave-test Arrival block 16/16
  (full run before the last fixes: 400 passed, the 4 fails all in the Arrival block, since fixed); shadow and board-wave
  tests pass except their servers not serving walker.glb (from #381, not this PR). scout: 2, the room's own controls.
  Not checked: a real phone, screen-reader reading of the glyph labels.
  Next for PR 2: Wendell plays #382 then #383; merge #382, retarget #383 to main, mark ready. The cave's lessons (run,
  glowing marks, word stones) were not in PR 2; fold them into PR 3 with Big Mind's glyphs, reusing `ROOM_LESSONS`'
  pattern and `learn()`. Small fix owed: shadow-test and board-wave-test servers should serve `cave/player/walker.glb`.
- **PR 3, the cave's lessons and Big Mind's** (bars-engine #384, draft, stacked on #383; retarget to main once #382 and #383
  merge; preview https://bars-engine-git-claude-projec-4f6b0d-wendells-projects-9c1b16dc.vercel.app/ontology-game/cave ): one
  shared `teacher()` in cave.js (the light, the glyph by its control or by the light, "I know this"), exported on the kit. The
  cave teaches a word stone (tap the pane) and a glowing mark (the prompt by the right thumb, the light floating out to the
  mark); walk and look only if the room has not taught them. Big Mind's first hallway teaches the walk, Run, Self and the way
  back; Spirits and Trust get a glyph the first time their buttons show. The mouth keeps the crisis line and "Nothing is sent
  anywhere" as words; its rules list, the hallway's walking line and the cave pane's rules line are gone. `learnTutorial`
  merges every write, so two open places never undo each other's lessons. Shadow and board-wave test servers serve
  walker.glb. cave-test 413/0, bigmind-test 533/1 then the fixed block 20/20, shadow 54/0, board-wave 20/0. scout: 2.
  Positions taken: "sit out any question" left the mouth (every ask has its own decline); what leaves the device stayed as words.
  Not checked: the Spirits glyph in a browser, a real phone, screen-reader reading of the glyph labels.
  Next for PR 3: Wendell plays #382, #383, #384 in order; merge each, retargeting the next to main. Then PR 4 below.
- **PR 4, the charge dial and kept cards** (bars-engine #385, draft, stacked on #384; retarget to main once #382 to #384 merge;
  preview https://bars-engine-git-claude-projec-2978c9-wendells-projects-9c1b16dc.vercel.app/ontology-game/cave ): every 0 to 10
  reading in the cave, the WAVE room and Big Mind (3-2-1 charge, Allow's size and brightness, Big Mind's charge polls) is a drawn
  dial, `dial()` in cave.js on the kit: a ring from calm green to full coral, drag or tap, the number in its middle, the range
  input kept inside unseen so keys, screen readers and test fills still work. The Big Mind mouth's kept list is a card per voice
  (daemon-coloured edge, Forget on the card), spirits a card of chips; Delete everything asks again on the page. `alert()` is
  gone: `notice()` puts a line at the foot of the screen (role status, or alert for a failure). cave-test 418/0, bigmind-test
  541/0, shadow 54/0, board-wave 20/0; both main tests now fail on any browser dialog. scout: 2, the page's own range inputs
  under an SVG. Left as they are: game.jsx's 1 to 10 block-size slider and its record-erase confirm (the 2D game).
  Not checked: a real phone's thumb on the dial, screen-reader reading of the dial.
  Next for PR 4: Wendell plays #382 to #385 in order; merge each, retargeting the next to main. That ends the walkthrough's
  four PRs; T1 and T2 are tested at his first play.

## Next: the walkthrough, taught by doing (design settled here; build on Opus, then Sonnet for the later PRs)
What a new player meets today (worker map, 2026-10-18): an HTML title page, a WAVE room whose first page is one overlay
sentence about the stick, and a Big Mind mouth that is a rules list. Drag-look, run, prompts by the thumb, word panes,
the Self, Spirits and Trust buttons are never taught. Nothing is taught in the world.

Positions taken (they stand unless he flips them):
- `gd-lantern-guide`: the guide is the player's own light, the glow already at the figure's chest. It leaves the chest,
  floats ahead to the next control to learn, waits there, and goes on once the player does it. It never lists rules.
- `gd-teach-by-doing`: each lesson is one in-world glyph (stick, key, finger) beside what it teaches, shown until the player
  does it once, then gone for good. Order, each where first needed: walk (stick, keys or hold), look (drag), tap the floor,
  run, stop at a glowing mark (the prompt by the thumb), open a word stone (the pane), sit on the rug, the two doors.
  Big Mind adds Self, Spirits and Trust as one-time glyphs beside each button the first time it shows.
- `gd-skip-and-replay`: a small "I know this" skips a lesson; settings replays the walkthrough. Saved in
  `oag.tutorial.v1` as the lessons done, no words.
- `gd-title-as-game`: the title becomes the cave mouth in 3D with the walker standing in it, "Begin" and "Continue"
  (Continue reads `oag.bigmind.v1`, then the last place played), and a settings gear (sound, reduced motion, replay walkthrough).
- `gd-mouth-in-world`: Big Mind's mouth keeps its crisis line as text, always (never cut); the rest of its rules list
  moves into the lantern's lessons in the first hallway.
- `gd-web-bits`: the 0 to 10 sliders become a drawn charge dial and the keep list becomes cards; `alert()` goes.
- Daemons are sparred, never fought (`dmt-trainer` A); the non-AI play is first class; keyboard, reduced motion and
  14 px type hold on every new screen.

PR order, one at a time, each with a playable link (bars-engine.vercel.app preview) and its own test checks:
1. Title as a game screen with Continue and settings. Built: bars-engine #382.
2. The Arrival: the lantern guide and the WAVE room lessons, saved in `oag.tutorial.v1`, replacing the round-1 sentence. Built: bars-engine #383.
3. Big Mind first-use glyphs for Self, Spirits, Trust, run, and the mouth rewrite. Built: bars-engine #384.
4. Sliders to a dial, keep list to cards, no `alert()`. Built: bars-engine #385.
Tests at his first play: T1 a new player reaches the WAVE room rug without reading a paragraph; T2 nothing he already
did is taught twice.

## Next: PR 5, screen space (brief for the next thread, 2026-10-19)
Wendell, 2026-10-19, after playing: "Ok the buttons are taking up too much space on the screen. Is there a way to create menus so
that we can more intelligently use space. Also they are randomly placed and players are telling me they don't quite know what
everything or anything means. The camera is acting funky in the wave room and the character needs to actually be able to sit on
the seat as opposed to walking through it / Biggest problem is still that the input screens are too big and one can see the
action underneath. We could maybe solve this with camera movement but also breaking the screens up so their data isn't one
semitransparent block"

Build on Opus, stacked on bars-engine #385 (the new thread owns #382 to #385 too; they still wait on his "go", merge in order).
Defaults taken (positions, stand unless he flips them on the board):
- One Menu button in a fixed corner gathers the scattered controls (Breath ring, Calm, Sit down, Spirits, Self, Trust, the
  gear), each a glyph with its word beside it. On screen stay only the walk stick and the one action the moment calls for.
- Input screens become a solid bottom sheet, no taller than about half the screen, one step or question per card with Next
  and Back, never one long translucent block. While a sheet is open the camera frames the figure in the top half.
- WAVE room: find what "funky" is first (probe stills of the camera on the walk to the rug, sitting, and the doors; his words
  only), then fix it. The figure walks to the seat, turns and sits on it at the seat's height; the seat blocks walking through.
Run the tool-scout ladder first (a known three.js or web bottom-sheet/menu pattern, rung 3). Each piece gets cave-test checks
and a playable preview link. Not done in this thread: nothing of PR 5 is built yet.
