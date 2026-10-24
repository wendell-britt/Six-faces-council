# Studio lot (the studio game)

## Next
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
