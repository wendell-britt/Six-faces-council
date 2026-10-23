# Studio lot (the studio game)

## Next
Art direction done 2026-10-23 (thread "Set the studio boat art direction"): page https://claude.ai/artifact/85chXzRvLpPj7dumm6hi5z
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
- `ty-still-pick` (his look at the two stills).
Nothing from Wendell. Positions `ty-lens`, `ty-real-data`, `ty-host`, `ty-engine`, `ty-roster`, `ty-gates`, `ty-rigor`,
`ty-order`, `ty-genre-mix` stand unless he flips them. `ty-genre` is answered with a steer ("I'm thinking a mix of boat
and studio sim."), recorded in `council/ledger/2026-10-23-pull-230209.json`.

## Files
- Concept page: https://claude.ai/artifact/CDaX3PSvZ87d29SzBs1nMQ (source `/mnt/project-files/studio-tycoon/studio-lot.html`)
- Research: https://claude.ai/artifact/Jn1C9NzB7CQnN7PB2sr1yL
- Pass `studio-tycoon-2026-10-23`

## Archive
None yet.
