# Studio lot (the studio game)

## Next
Face ships round 3, Taoist cultivation in space, done 2026-10-24 (thread "Pivot ships to Taoist space style"). His
pivot (03:26): "I do think the FTL ship design and the spacecraft should be where we send this. The aesthetic polarity
is Taoist cultivation in space Star Wars meets Avatar the last airbender but with 5 elements". His 04:02 steers overruled
boat-grid-spiritfarer (space, no buoyancy), boat-grid-axes (grows below as well as above) and boat-grid-deck-unlock
(starship names). Made in `/mnt/project-files/studio-tycoon/taoist-ships/`: `art-direction.md` (keep list, face to
element table), `refs/` (28 images + README + contact sheet: Luofu, Star Wars interiors, ATLA airships, Su Song clock
tower, Wu Xing), `ships-tao.js` (round 2 API and mechanics kept), stills `still-{1..4,hangar}-v3.png`, `compare-*.png`,
`art-director-review-v3.md` (fixes applied: no sails or raised ends, a deck below the vein on every ship, 118px+ open
span with a glowing crate). Page https://claude.ai/artifact/3nMqrD3GVb1UpUMiexuY9W (source `face-ships-tao.html`).
Ships: Gourd Star (wood), Ember Comet (fire), Jade Palace (earth), Clockwork Orrery (metal); Tide Lotus and Taiji Star
locked at the Air Temple moorings. Rows `council/callsheets/rows/tao-ships-2026-10-24.json` on main: positions
`boat-grid-tao-space`, `-five-elements`, `-grows-both-ways`, `-star-names`; question `boat-grid-carry-tao` (carry the
look to the living ship and Calrunia?). Look step `boat-grid-look-3` (list `studio-lot-boat`, n 8) on both stores;
`boat-grid-look-2` ticked as answered by his pivot. Open art notes: Jade Palace lacks symmetric tiers; Gourd Star is
small in the hangar. #429 untouched (head c315bb5).

Brief: Face ships build now ports `taoist-ships/ships-tao.js`, not `ftl-ship/ships.js`; otherwise as below, starts
after his yes on `boat-grid-look-3` (a note starts round 4 from his note plus the open art notes). Lanterns are qi pearls
by element; names per boat-grid-star-names.

Earlier, Face ships round 2 done 2026-10-24 (thread "Face ships, round 2"). Renderer v2 `ships.js` (v1 kept as
`ships-v1.js`) applies `art-director-review-v1.md`: cottages with open deck between them and ladders in the gaps,
per-face outlines (Shaman arched reed, Challenger raked and jagged with ram, spars and ring, Regent gables mirrored
about a bell tower, Architect truss roof, pipes, stacks, crane, galleon hull), energy as lanterns along the vein in
the hold with light threads to rooms and an "asks / holds" tag (no panel), Everdoor, signs with vines, portholes,
role hats and sashes on crew (64px x scale, min 56), spirits min 50px, needy room pulses and speaks above its roof,
hangar on a dusk pier with rimmed ink silhouettes, tap a cottage to move a lantern (`FaceShips.tap`). Six real
Spiritfarer frames added to `refs/` (`spiritfarer-sheet.jpg`). Stills `still-{1,2,3,4,hangar}-v2.png`; recheck
`art-director-review-v2.md`: show it to him, open notes for round 3 (vary room widths and offset decks, a 100-140px
open span for the mid-trip walker, more portholes and lit windows on Regent and Architect). Page with the four ships
moving, the hangar, refs beside our earlier boats and a table per face: https://claude.ai/artifact/PP8w2152LsMZ4Yz9ZE4GJk
(source `face-ships.html` in `/mnt/project-files/studio-tycoon/ftl-ship/`). Positions on main (rows
`council/callsheets/rows/boat-face-2026-10-24.json`): `boat-grid-face-ships` (replaces `tw-walkable-decks`),
`boat-grid-energy-is-power`, `boat-grid-deck-unlock`, `boat-grid-axes-faces` (amends `boat-grid-axes`). Look step
`boat-grid-look-2` (list `studio-lot-boat`, n 7) on both stores. #429 untouched.

Brief: Face ships build (fresh Opus thread after his yes on `boat-grid-look-2`, per hx-looks-gate not before; a note
instead starts round 3 from his note plus the v2 open notes; owns bars-engine #429, branch
`claude/project-thread-227mft`, head c315bb5). Keep list, checked by the art director before his look: a crew member
mid-trip across open deck in every frame, work seen live, eye pulled by movement and need, the Lantern deck's style.
(1) Port `ships.js` (plain canvas 2D) as the boat's renderer in `public/studio/`; `world.ts` stays the data side.
(2) Ship = faces earned: Chapter 1 is the Hearth Canoe; a deck appears when its unlock line (boat-grid-deck-unlock)
is met, read from loops and callsheets. (3) Spirits from INDEX strands sit in the room of their face and step
(boat-grid-axes-faces), crew errands from strands touched in the last day, the needy room from open board letters.
(4) Lanterns: each running strand spends lanterns from the vein; tapping a cottage moves one (boat-grid-energy-is-power);
store the choice through the board's own save via src/lib/board/shim.ts. (5) Tap a bubble or spirit: the steer card
(round 4 letters content); Tap the vein is a hold move. (6) Forty-six strands: queue spirits on the open deck in front
of a full cottage; check on a phone. (7) Leave the needy cottage's table for brief "Looks aboard the boat". (8) Preview
link at `?strand=<one with a letter>` as look step `boat-grid-look-3`.

Face ships (FTL) round 1, 2026-10-24 (thread "Mock the face-driven ships"). His steer on `tw-walkable-decks` (02:57,
overruled): split the difference between the current render and Spiritfarer, toward FTL: "Different ship design as a
function of which of the game master faces is running the game"; Chapter 1 ship designed from shamanic feel and
emotional alchemy; unlock a two-deck ship (Shaman + Challenger), then Regent, then Architect, "Each reflecting the style
and concern of that level of development as well as the complicity afforded and the emotional energy cost" (read as
complexity afforded). His note at 03:01 on the grid ship: "more accurate from a mechanics POV but has lost the style.
Did we use art direction when changing to the grid style?" It did not; this round runs art direction first (reply
posted in the thread). Made so far, all in `/mnt/project-files/studio-tycoon/ftl-ship/`: `refs/` (8 real FTL images +
README), `ships.js` (canvas renderer, Lantern-deck dusk style, FTL tile rooms + doors + emotional-energy power bar),
`still.html` (`?view=1|2|3|4|hangar`), stills `still-1-v1.png`, `still-2-v1.png`, `still-4-v1.png`,
`still-hangar-v1.png`, and the CCGS art-director review `art-director-review-v1.md` (a worker was writing it at
handoff; if missing, rerun that review first). Design in v1: one deck per face, stacked by altitude (Shaman at the keel),
decks taper upward, rooms stern to bow in pipeline order. Shaman deck = the five Basic Moves (Wake, Hearth = Open Up and
the reactor where the vein rises, Cauldron = Clean Up, Garden = Grow Up, Porch = Show Up), 1 pip each. Challenger
(Lookout, Ring, Forge, Breach bay with live fires), 2 pips each. Regent (Ledger, Bell, Charter, Stores), 2 each.
Architect (Drafting, Engine = second reactor, Drone bay, Pipeworks), 2-3 each. Reactor 6/9/12/16: Chapter 1 has 2 spare
pips (room to rest); every later ship asks more than it holds, so the player chooses where feeling goes. Hull silhouette
per face (woven spiral canoe, angular ram, symmetric cupola, truss + crane). Hangar is FTL's ship select, ships 2-4
locked with unlock lines. No board rows or look step yet; #429 untouched.

Brief "Face ships, round 2" done 2026-10-24, recorded above.

Superseded by the face ships above: Grid ship 2026-10-24 (thread "Build the walkable ship"). His note on `tw-ship-look-1` (02:51): right direction, lean more
on Spiritfarer, and "If the boat is a coordinate grid the x axis is the step in the pipeline and the y axis is almost
like depth within that step of the pipeline (perhaps even unlockable depths as a function of the game master face at
play in the design ontology and game design space)". The grid changed the look a lot, so a moving mock went up first
instead of the build: https://claude.ai/artifact/KU5qyuYmdmCPWHZD2uRuag (source `grid-scene.js`, `grid-ship.html`,
stills in `/mnt/project-files/studio-tycoon/grid-ship/`). Seven stacks along a Spiritfarer barge, one story per face in
altitude order (Shaman lowest, Sage top), unearned stories as blueprint cells, ladders between every pair of stacks,
crew carrying crates down, along the deck and up. Positions `boat-grid-axes` (replaces `tw-deck-map`),
`boat-grid-unlock`, `boat-grid-spiritfarer` (rows `council/callsheets/rows/boat-grid-2026-10-24.json`). Look step
`boat-grid-look-1` (list `studio-lot-boat`, n 6) on both stores. Boat rows now use the `boat-grid-` prefix, since `tw-`
ids also exist on the Work/DBT strand. #429 untouched (head c315bb5). The brief "Walkable ship build" below is replaced
by this one.

Superseded by brief "Face ships build" above: Grid ship build (fresh Opus thread after his yes on `boat-grid-look-1`; per hx-looks-gate not before; owns
bars-engine #429, branch `claude/project-thread-227mft`, head c315bb5). Keep list, checked by the art director before his
look: a crew member visible mid-trip (on a ladder) in every frame, work seen live, eye pulled by movement and need.
(1) Port `grid-scene.js` (plain canvas 2D) as the boat's renderer in `public/studio/`; keep `world.ts` as the data side
with a `STAGES` table (stage from loop or callsheet, fallback the hold) and a `FACES` table from `council/faces.yaml`
altitudes. (2) Stack height per stage = the faces at play on that stage's strands: a face counts once a board row on a
strand in that stage lists it in `faces` (boat-grid-unlock); unearned stories stay blueprint. (3) Spirits from INDEX
strands sit in the cabin of their stage at the highest story earned; crew errands from strands touched in the last day,
routes cell to ladder to deck to ladder to cell; the waiting cabin from open board letters. (4) Tap a bubble or spirit:
the steer card (round 4 letters content) POSTs the board's own save via src/lib/board/shim.ts; Tap the vein is a hold
move. (5) Forty-six strands over seven stacks: queue spirits on the deck in front of a full cabin; check on a phone.
(6) Leave the waiting cabin's table for brief "Looks aboard the boat". (7) Preview link at `?strand=<one with a
letter>` as look step `boat-grid-look-2`.

Superseded 2026-10-24 by the grid ship above: Walkable tall ship 2026-10-24 (thread "Art direct the walkable tall ship"). His steers at 02:24 overruled `lb-keep-the-deck`
("I want a tall ship crosssectikn where agents walk between rooms in the cross section. Perhaps the tall ship is 3
dimensional but represented in 2d (monument valley style)") and `lb-stage-pennants` ("I don't understand the pennants").
Made: moving mock page https://claude.ai/artifact/9W13HHYCqpNQcKyDqbDMb3 (source, `scene.js` renderer, stills, refs and
`art-director-review.md` in `/mnt/project-files/studio-tycoon/walkable-ship/`): the ship cut open lengthwise in one fixed
axonometric view, four decks (top: wheel, bell, Everdoor; stage deck: seven stages stern to bow; workshop deck: six
departments; hold: the vein), an open corridor per deck, five open stairways, cabins with no front wall, 11 crew carrying
stage-tinted crates with dashed route lines, follow camera turning between the waiting cabin and a moving crate.
Reference board of 8 images, side by side with the flat boat and the sealed ship, and the brief-master prompt that should
have run. Positions `tw-walkable-decks` (replaces `lb-keep-the-deck`), `tw-deck-map`, `tw-no-pennants`, `tw-follow-camera`
(rows `council/callsheets/rows/walkable-ship-2026-10-24.json`, on main; the artifact board shows them at its next
republish). Look step `tw-ship-look-1` (list `studio-lot-boat`, n 5) on both stores. `lb-boat-look-1` is answered by his
steers. The brief "Living boat build" below is retired.

Brief: Walkable ship build (fresh Opus thread after his yes on `tw-ship-look-1`; owns bars-engine #429, branch
`claude/project-thread-227mft`, head c315bb5). Keep list, checked by the art director before his look: a crew member
visible mid-trip in every frame, work seen live, eye pulled by movement and need. (1) Port `scene.js` as the boat's
renderer in `public/studio/` (it is plain canvas 2D, no Phaser needed; keep `world.ts` as the data side): spirits from
INDEX strands placed in the cabin of their stage (a `STAGES` table, stage from loop or callsheet, fallback the hold),
crew errands from strands touched in the last day, the waiting cabin from open board letters. (2) Tap a bubble or
spirit: the steer card (round 4 letters content) POSTs the board's own save via src/lib/board/shim.ts; Tap the vein is
a hold move. (3) Art-director open notes: tie each walker to its strand's colour, a work prop per busy cabin, the follow
camera prefers a walker mid-stair. (4) Forty-six strands must fit seven cabins: stack or queue spirits, check on a
phone. (5) Preview link at `?strand=<one with a letter>` as look step `tw-ship-look-2`.

Brief: Looks aboard the boat (waits on the boat build above; brief only, no code before it). Wendell, 2026-10-24: "we
also need a place on the council board and in th spirit game design game where we can preview and test any assets that
are waiting for my eyes". The board half is built: the Your eyes tab on the Council Board (council PR from thread
"Gather looks waiting for Wendell"), which reads every open look step (`look: true`, or an id with look, try, play or
squint), one card per strand, newest first, with a still (`still`), a title (`lookTitle`), one Open it link and a yes
or note that ticks the step and saves his words as its note. The boat half: a look is a spirit at the rail holding up
what it made. (1) Each open look step becomes a lantern or a crate on the waiting cabin's table, carrying its still as a
painted card; its spirit (the strand) waits beside it, so how many looks wait is seen as how full the cabin is, never as
a count. (2) Tapping the card opens the step's `href` (the hosted preview) in a new tab; coming back, the spirit asks
"yes, or what feels off?" in the steer card, and the answer writes the same `done` + `note` patch the board tab writes,
through src/lib/board/shim.ts, so both views close the same step. (3) Older looks on the same strand sit face down
under the newest. (4) Art direction first, per the keep list: a still of the cabin with three waiting looks, for his
look, before code. Data source is the steps store only; no new collection.

Retired 2026-10-24 by his steers above: Living boat 2026-10-24 (thread "Bring back the living boat"). His note on `ts-ship-look-1` rejected the tall ship: "the
tall ship is not an improvement from the platform style ... Fully the wrong direction" and "The biggest thing is that
agents can be seen traveling between rooms anymore that was the most compelling part of the first design. Being able
to see the work happening seemingly in real time and zooming into what was pulling attention based on its movement and
needs". The brief "Tall ship, round C" below is retired. Made: page https://claude.ai/artifact/UAcTBNbgfFT7XYNXRQCPM7
(source and still in `/mnt/project-files/studio-tycoon/living-boat/`: a mock drawn over a screenshot of the c315bb5
preview, `still-scene.html` rebuilds it). Positions `lb-keep-the-deck` (replaces `ts-stage-rooms`, `ts-walk-bow-ward`,
`ts-depts-below`), `lb-stage-pennants`, `lb-depth-in-place` (rows `council/callsheets/rows/living-boat-2026-10-24.json`).
Look step `lb-boat-look-1` (list `studio-lot-boat`, n 4). The `bw-*` rulings and `ts-tap-opens-card`, `ts-steer-is-save`,
`ts-fanout`, `ts-device-tiers` still stand.

Lesson (rule for every rework of something he has looked at): before changing a layout, write a keep list from his
looks (what he called good, in his words) into the brief, and the art-director check lays the new still beside the old
one and asks "does the keep list survive?", not only "is it readable?". The tall ship rounds skipped references
(no cutaway or crowd-sim images were pulled), never ran the brief through brief-master, and judged the still on labels
and sizes. The cross-section walled seven rooms apart, so crew could not travel; motion, the thing that told him work
was happening, disappeared. Depth is fine where movement stays visible (a hall opening in place), not as sealed rooms.

Brief: Living boat build (fresh Opus thread after his yes on `lb-boat-look-1`; owns bars-engine #429, branch
`claude/project-thread-227mft`, head c315bb5). Keep list: one deck, crew walking hall to hall, eye pulled by motion and
need. (1) Crew traffic: each running strand (callsheet touched in the last day or a loop round open) gets a crew member
who walks between its hall and the next with a crate showing its stage number; idle crew rest at doors. (2) Seven stage
pennants on the light string, stern to bow, current stage lit (a `STAGES` table in `world.ts`, stage from loop or
callsheet, fallback none). (3) Camera drifts toward the nearest bell or moving crate when the player is idle. (4) Tap a
bubble or spirit: the steer card (round 4 letters content: wax seals, Not tonight, Say something else, Tap the vein)
POSTs the board's own save via src/lib/board/shim.ts; Tap the vein is a boat move per his bw overrule. (5) Open hall
fades its front wall in place; traffic keeps passing. Prove with a still from the running build beside the mock, then
a preview link at `?strand=<one with a letter>` as look step `lb-boat-look-2`.

Tall ship (retired 2026-10-24 by his note above):
Tall ship, round B done 2026-10-24 (thread "Tall ship, round B"). Still v2 fixed per the review (one hull with depth,
one label per room, big tailed bubbles, one spirit-generator spirit per room at 108px, departments as lower-deck
portholes): `/mnt/project-files/studio-tycoon/tall-ship/still-tall-ship-v2.png`, source `still-scene-v2.html` (reads
`spirits.png` beside it). CCGS art-director recheck `art-director-review-v2.md`: ship it for his look; open notes are
pixel spirits on a vector ship (pick one style), Production/Release spirits only stand, sizes vary ~1.5x, no drawn
mapping of seven stages over six departments. Hosted page with the still and the steer design:
https://claude.ai/artifact/GM4aktqN5uvuu3bfhbmgzb (source `tall-ship.html` there). Look step `ts-ship-look-1` (list
`studio-lot-boat`, n 3) on both boards. Positions (rows `council/callsheets/rows/tall-ship-b-2026-10-24.json`, on both
boards): `ts-stage-rooms`, `ts-walk-bow-ward`, `ts-depts-below`, `ts-tap-opens-card`, `ts-steer-is-save`, `ts-fanout`,
`ts-device-tiers`. No questions: the reach test left none the record could not answer. #429 untouched (head c315bb5).

Brief: Tall ship, round C (fresh Opus thread; waits on his note on `ts-ship-look-1` per hx-looks-gate; owns bars-engine
#429, branch `claude/project-thread-227mft`). (1) Take his note. (2) Rebuild `world.ts` and `public/studio/boat.js` on
the tall-ship layout: seven stage rooms stern to bow (a `STAGES` table; each strand's room from its loop/callsheet
stage, fallback the hold), department workshops on the lower deck as crew homes (keep the hall map of round 3 as
`deptOf`), the wheel on the stern where the player stands. Pick one art style for spirits and ship (art-director note 1).
(3) Tap a bubble, spirit or the player's line opens the strand card (round 4 letters content); a steer POSTs the board's
own save via src/lib/board/shim.ts. (4) Device badge per `ts-device-tiers` (pointer/width guess, tap to correct,
localStorage). (5) Preview link opened at `?strand=<one with a letter>` as look step `ts-ship-look-2`. Fan-out builds
(`ts-fanout`: board-pull firing the Board Send routine, a SessionStart hook listing new steers) are a separate
board-plumbing thread, not this one.

Rulings from his 2026-10-24 02:03 saves, to build from (round C brief, add-on):
- `bw-strand-fade` = A: a strand fades and leaves a seed. `bw-first-move` = "Answer letters".
- `bw-crew-are-hands` stands, his steer: "Crew should be about what and how. Spirits are about why. The goal of the game is to leverage emotional charge into effective leveraged action. The goal for players is to make more deft decisions with the most effective use of resources and the purpose is to integrate the inner and outworks motivations toward making jaw droppingly excellent work with AI"
- `bw-board-keeps-the-rest` OVERRULED, his steer: "Tap the vein needs to be a move one can do on the boat. This is how the boat mines emotional energy. This is where vibeluons come in in a big way"
- `bw-spirit-is-strand` OVERRULED, his steer: "Spirit is the emotional energy and magic fueling the work"
- Also stand: `ty-boat-departments`, `bw-talk-is-save`, `bw-lines-from-record`, `bw-answer-is-care`, and the seven `ts-*` rows.

Tall ship, round A 2026-10-24 (thread "Rework boat as a tall ship", from his note on `ty-boat-look-2`: click a spirit's
or player's message to open its card and steer; the skiff is overdone and too long, use a cross-section of a larger
tall ship, keep the vibe, rooms correspond to the pipeline, maybe oriented along it; a steer updates the repo and sends
a hook to every surface, including coding environments; the boat knows phone vs a computer that can reach the council).
Made: still v1 `/mnt/project-files/studio-tycoon/tall-ship/still-tall-ship-v1.png` (scene source `still-scene.html`
beside it, rendered by Playwright from the round 2 sprites). Layout idea: stern to bow = the seven CCGS stages
(Concept in the captain's cabin under the wheel where he steers, Systems Design chart room, Technical Setup carpenter's
shop, Pre-Production model shop lit as "here", Production workshop deck, Polish sail loft, Release forecastle facing
the live-site island); a strand's spirit walks bow-ward as its stage passes; departments are workshops below; hold =
corpus/compost. The art-director review (`art-director-review-v1.md` beside it) says fix first. Not shown to him yet.
Found: the save path already fires board-pull at once (bars-engine `src/app/api/board/saves/route.ts` calls
`dispatchBoardPull()` for record kinds), so "steer writes the repo" exists; missing is the fan-out after main changes.

Brief: Tall ship, round B (fresh Opus thread; owns bars-engine #429, branch `claude/project-thread-227mft`, head c315bb5).
(1) Fix the still per the review (one vessel with depth, one label per room, big tailed bubbles, one distinct spirit
per room at one scale), recheck with the CCGS art-director role, then put it up as a look step with board positions
`ts-stage-rooms` (stern-to-bow = stages), `ts-walk-bow-ward`, `ts-depts-below`. (2) Write the steer design as one
page: tap a bubble opens the strand/letter card (round 4 letters brief above is the card's content); a steer is the
board's own save (no schema change); fan-out plan after board-pull lands on main: bars-engine reads main (live
already), artifact board republish step, Board Send routine trig_01L138vKTaN9MSJoFKRmaBNx so the owning cloud thread
picks it up, desktop sessions pull main at SessionStart; device tiers (phone: read, open, steer, defer; signed-in
computer: also hand to crew; his Mac: actions that need local tools queue for a thread with Remote Control). Position
rows for each; questions only what the record cannot answer. (3) Layout rebuild in Phaser on #429 waits on his yes to
the fixed still.

Boat moves, design answer 2026-10-24 (thread "Map board moves onto the spirit boat"): page
https://claude.ai/artifact/Q9BL7o2wJMAPSoQU6cyyAr (source `/mnt/project-files/studio-tycoon/boat-moves/boat-moves.html`),
rows `council/callsheets/rows/boat-moves-2026-10-24.json` on both boards. The boat writes nothing today (only
localStorage `studioBoat.*`; it reads INDEX.md and loops, no questions, positions or steps). Positions `bw-spirit-is-strand`,
`bw-crew-are-hands`, `bw-talk-is-save`, `bw-lines-from-record`, `bw-answer-is-care`, `bw-board-keeps-the-rest`.
Questions `bw-first-move` (A letters first, recommended; B crew onto spirit per ty-order) and `bw-strand-fade`.

Brief: Boat round 4, letters (fresh Opus thread after round 3; owns #429 or its successor; read `bw-first-move` first and
build the crew move instead if he picks B). (1) deck.ts also loads open questions and positions from board_data.json on
main, each tied to its strand (by `pass` or callsheet name; unmatched rows go to the wheelhouse). (2) A spirit with a
letter shows it at the bell; one wax seal per option, "Not tonight" (defer), and "say something else" (steer, saved as
typed). Positions are the rule over the door: nod (stands), change it plus words (overrule), take it down (retire).
(3) The spirit says back what it heard, then the page POSTs the board's own save shape to /api/board/saves (reuse the
board shim, src/lib/board/shim.ts; no schema change). Lines come from the row text, no live model. (4) Test: a save
from the boat matches tests/fixtures/board-saves. Preview link opened at `?strand=<one with a letter>` on the board as a
look step.

Round 3 split 2026-10-24 (thread "Group the boat into departments"): #429 `check` is green on 10fd9e3 (step 1 done). His
note on `ty-boat-look-1` is recorded as position `ty-boat-departments`. The thread passed the context line before
building, so the build is the brief below.

Brief: Boat round 3: departments (fresh Opus thread, owns bars-engine #429, branch `claude/project-thread-227mft`).
Replace 46 houses with six department halls (rooms inside halls, wings inside some halls). Plan, already decided:
- `world.ts`: a `DEPARTMENTS` table (hall, CCGS lead, wings) and `hallOf(strand)` with fallback `hold` (the cargo
  hold, so a new strand still shows). World gains `halls: {id, name, x, w, bells, look, wings: {name, x0, x1}[]}`;
  rooms keep the House fields plus `hall`, `wing?`, x absolute, tier 0/1 for the hall's two storeys. ROOM_W about 118,
  hall pad 24, gap 40. Halls with no bell and no scaffold go stern of the wheelhouse; the rest bow-ward, fewest bells
  first, so bells are at the bow. Tests: every current INDEX strand has a hall; bells at the bow; wings contiguous.
- Map (49 names, 46 in INDEX today): Art Studio (art-director): spirit-generator, cave-studio, calrunia-creator; wing
  Blender workshop: blender-frame-flesh-warp, blender-pipeline-test, jev-asset, game-demo. Design Room (game-designer):
  chapter1-demo, walkthrough, engine-slice, skilled-helper, steps-hand, move-nature, root, studio-lot, studio; wing
  Spirit nursery: inner-creatures, spirit-dissolve, perceptual-shadow, spirit-care, wave-battle. Map Room
  (level-designer): calrunia-world, inner-vessel, relationship-creature; wing Caves: cave-of-lessons, cave-levels,
  cave-controls, big-mind-cave, spirits-in-caves, wave-room, element-settings. Story Room (narrative-director):
  story-pipeline, corpus, friendcraft, somatic-ontology, ontology-flows; wing Healing practice: shame-coaching,
  work-dbt. Post Office (community-manager): podcast, flirtcraft, email-pipeline, virtual-launch, artist-corps; wing
  Coaching business: coaching-pipeline, coaching-site. Engine Room (producer): board-plumbing, session-cost,
  process-retro, morning-menu.
- `boat.js`: drop the gallery and ladders (the player stays on deck). `drawHall` = one two-storey building with the
  hall's name on a painted sign, one window per room showing its state (lit, dim with vines, letter glow), wings as
  a gabled annex in their own wall colour; one bell on the hall when any room waits. `drawRoom` = a small cutaway room
  (strand hue, lamp, boards for scaffold, vines, letter on the table) with the spirit or tortoise inside. Tapping a
  hall walks to its door and fades the front wall (one hall open at a time, closes when you walk away); tapping a room
  knocks as before. Intro: ring the first bell hall, then on waking open it and knock its first waiting room.
  `?strand=` opens the hall first. Crew stand at their hall's door, spread by index.
- Also from the art-director review: a night multiply layer (glows on a separate layer above it), letter text in
  plain words (strip parentheticals, URLs, PR numbers, code spans), then the move (crew card onto a waiting spirit).
- Look step `ty-boat-look-2` opening `<preview>/board/studio?intro=1`, plus a still of a closed and an open hall.

Earlier: Round 2 done 2026-10-24 (thread "Polish the studio boat, round 2", bars-engine #429 commit 10fd9e3). Look step
`ty-boat-look-1` (list `studio-lot-boat`) is on both boards, opening the branch preview
https://bars-engine-git-claude-projec-a0a10d-wendells-projects-9c1b16dc.vercel.app/board/studio?intro=1 . Built: waiting
spirits from the spirit generator's pixel renders (`public/studio/sprites/spirits.png`, 18 bases x 5 elements, one stable
creature per strand), crew coats recoloured from the walk frames and walking only while they move (hammer at scaffolds),
tall islands with a lighthouse, the ship's log on a lectern by the wheelhouse (`worldOf().log`, tested), a quilted sleeper
in a wider hammock (MAST_W 300), three bells instead of 17, hull sunk in the water, additive glows, letters over a dim
scrim. CCGS art-director review of round 1: `/mnt/project-files/studio-tycoon/rebuild-1/art-director-review.md`; stills of
round 2: `/mnt/project-files/studio-tycoon/rebuild-2/`. Not checked: a real phone; fonts (stills were taken without
Google Fonts); the crew still stand in one row in front of the working houses when idle.

Brief: Boat round 3 (fresh Opus thread, owns #429, waits on his note on `ty-boat-look-1` per hx-looks-gate). (1) Confirm the
#429 `check` job is green on 10fd9e3 (4a0e14f failed on one lint error, likely the `const S = this` that 10fd9e3
removes); if not, fix the lint and push. (2) Take his note. Then the review's open items: break the two storeys of wall-to-wall houses into fewer, gapped houses
(review fix 1, a layout change in `world.ts`), a night multiply layer, letter text in plain words instead of the
callsheet line, and spread idle crew. Then the move: a crew card dragged onto a waiting spirit sends its brief.

Earlier: Rebuilt 2026-10-24 (thread "Rebuild the studio boat", bars-engine #429 commit 4a0e14f): `/board/studio` is now the
Lantern deck in Phaser 3 from still A. Code: `src/lib/studio/world.ts` (strand to house look and place, tested in
`world.test.ts`), `src/lib/studio/page.ts` (shell, Phaser 3.80.1 from jsDelivr), `public/studio/boat.js` (the game),
`public/studio/sprites/` (from mood-stills/sprites). 46 strands as houses on two rows (deck and gallery, ladders):
resting under vines with a sleeping tortoise at the stern, wheelhouse and hammock midship, scaffold/lit-and-smoking
houses with crew carrying crates, bell houses with a fox and a letter at the bow; the done strand walks through the
Everdoor; seven stages as islands and a sea chart in the wheelhouse. First 60 seconds as on the page (hammock, bell,
tap to wake, walk to the bow, letter with two wax seals, pull-back). The red seal is local to his phone for the day;
the board stays the record. Params `?skip=1`, `?intro=1`, `?strand=<name>`, `?sky=dawn|day|dusk|night`.
Stills from the running build: `/mnt/project-files/studio-tycoon/rebuild-1/` (deck-dusk, letter-night, pull-back).

Brief: Boat round 2 (next, fresh Opus thread, owns #429 on `claude/project-thread-227mft`). (1) Get the Vercel
preview URL for 4a0e14f from the PR and put a look step on the board (`ty-boat-look-1`) opening
`<preview>/board/studio?intro=1`. (2) CCGS art-director check of the three stills against
https://claude.ai/artifact/85chXzRvLpPj7dumm6hi5z, as an Agent worker. Known gaps: crew all share one pose and run in
place (need a walk cycle), every waiting spirit is the same fox (use the spirit-generator spirits, tinted by element),
islands barely show behind the houses, no ship's log yet, the hammock pose is the side sprite turned 84 degrees, 17
bells crowd the bow. (3) After his look, the move (a staff card onto a waiting spirit sends its brief).

Earlier: Art direction done 2026-10-23 (thread "Set the studio boat art direction"): page https://claude.ai/artifact/85chXzRvLpPj7dumm6hi5z
(reference board, first 60 seconds, data-to-world map, two stills). Files `/mnt/project-files/studio-tycoon/mood-stills/`
(still-a.png side view on canvas, still-b.png three.js 0.160 pixelated, sprites/ from bars-engine public/between/m GLBs,
art-director-review.md). Per his 23:52 ask, the CCGS art-director role (fetched from the CCGS repo) reviewed and fixed
the stills; it recommends A (Spiritfarer side view). Board question `ty-still-pick` (A recommended). Render scripts were
in a scratch dir and are lost with the container; rebuild from the review if needed.

Brief: Boat rebuild (waits on ty-still-pick yes). One Opus thread on bars-engine #429: Phaser 3 side-view deck from the
chosen still, every strand a house with its four looks, player walks the deck, data only as world state, first 60 seconds
as on the page. Use the CCGS roles for the work (game-designer for the loop, art-director checks each still against the
page, gameplay-programmer builds). Prove with a still from the running build before any feature. Hosted preview link.

Built 2026-10-23: the read-only boat deck at bars-engine `/board/studio` (bars-engine #429, draft, branch
`claude/project-thread-227mft`). Open strands from INDEX.md ride as spirits (bow waiting on Wendell, midship moving,
stern resting, Everdoor done; fading toward 21 days untouched), loop strands show rounds past his last look, a crew row
of the Claude-Code-Game-Studios roster with Opus/Sonnet wages, and the Chapter 1 gate bar (advice: Pre-Production, no
gate passed). Preview deployments open without the bars-engine sign-in; production stays owner-only.

Rejected 2026-10-23 23:40 by Wendell: "Visually it doesn't feel like a game. The boat doesn't feel like a space and
it's all check lists and dashboard ... It's meant to be immersive." What missed: the brief listed data surfaces (a deck
of passengers, a crew row, a gate bar), and the thread built them as UI. There was no art direction, no reference
board and no player-POV spec, and the tool-scout "cheapest rung" was used to justify plain shapes when the cheapest
proof of a game is a mood still. The check was "does the data render", never "does a player call this a game".
Asset list: `/mnt/project-files/studio-tycoon/boat-world-assets.md`.

Brief: Boat art direction (next). One Opus thread, before any code: (1) a reference board from Spiritfarer, A Short
Hike, Unpacking, Cultist Simulator and Animal Crossing, as an Artifact page of stills with what we take from each;
(2) a player-POV spec of the first 60 seconds (where you stand, what you see, the first thing you do), with no
lists on screen and data shown only as world state; (3) one or two mood stills of the deck as a place, built from
Kenney/Quaternius shapes plus our spirit-generator spirits and Average Dusk, for his look. Code waits on his yes to a
still. Then the rebuild goes on #429 in Phaser 3 (`ty-engine`), and the move (a staff card onto a waiting spirit sends
its brief) after that. Rule for every game brief from here: art direction, a POV spec and a look at a still come
before the build.

## Waiting on
- His look at the rebuilt deck (step `ty-boat-look-1`, put up by the round 2 thread). `ty-still-pick` answered A.
Nothing from Wendell. Positions `ty-lens`, `ty-real-data`, `ty-host`, `ty-engine`, `ty-roster`, `ty-gates`, `ty-rigor`,
`ty-order`, `ty-genre-mix` stand unless he flips them. `ty-genre` is answered with a steer ("I'm thinking a mix of boat
and studio sim."), recorded in `council/ledger/2026-10-23-pull-230209.json`.

## Files
- Concept page: https://claude.ai/artifact/CDaX3PSvZ87d29SzBs1nMQ (source `/mnt/project-files/studio-tycoon/studio-lot.html`)
- Research: https://claude.ai/artifact/Jn1C9NzB7CQnN7PB2sr1yL
- Pass `studio-tycoon-2026-10-23`

## Archive
None yet.
