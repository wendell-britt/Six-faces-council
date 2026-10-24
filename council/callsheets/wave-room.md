2026-10-14 (updated 21:50)
# WAVE room (the cave's home)

## Next
2026-10-13: pinch to zoom and a tap-a-creature close-up are built for the room, bars-engine PR #302 (branch
`claude/project-thread-wvicrp`), cave-test 315 pass, 331 with the Big Mind fold. Zooming out past the step's view widens the lens
so all three creatures fit on an upright phone (choice). The close-up card shows name, element, texture, where, step, charge,
feelings about it, goal and next move, with "Work with this one" and "Back to the room" (choice). Phone page
https://claude.ai/artifact/23neJJJgywAygUqiJffGvc version 14 carries it with the Big Mind fold. Next: his play of the pinch and
close-up.

The second slice is built: bars-engine PR #277 (branch `claude/project-thread-ncihch`, stacked on #276), 263 checks green. It
carries all seven of Wendell's 22:59 changes: Talk to it switches voice by itself (room and cave), the door slides into the wall,
Allow grows the creature with size and brightness sliders, a glow and sparks that dull as it is worked, up to three creatures
with a "Working with" picker and a fourth waiting at the door, and feelings about feelings as named rings on the creature they
are about. The cave fork took the narrower reading (3-2-1 switching, sliders and glow at the daemon; the whole room flow is not
run in place in the cave); it stands unless he flips it. The cave's DESIGN.md has "The WAVE room, second slice". Next: his play
of the second slice, then fixes from his notes in a fresh thread.

## Built: the board's way into the room (2026-10-14)
- His steer on `ttv-skip-wave`: "yes, but I want it to be as interactive as possible. We want to move toward using the game
  to build the game. It should deposit me inside the WAVE room and we should move to have the WAVE room be able to metabolize
  context specific charges and send the results to the board in this case."
- bars-engine #324 (draft, branch `claude/project-thread-h6nfj1`, stacked on #317 with #316 merged in): `cave/board-wave.js`
  reads `#wave=board&charge=&skips=&ref=&date=` and opens the room from the board. Welcome names the charge words and asks
  the charge 0 to 10; Acknowledge asks what is in the way of it; the quiet room asks how today's Tap the Vein ends (the
  panel's five endings) and the charge left; the way out is "Back to the board". Every page saves the run (blocker record,
  `engine: "wave-room"`) to `POST /api/council/wave-runs` under his sign-in; a signed-out run waits in the browser.
  New table `wave_room_runs`. board-wave-test 20 of 20.
- Six-faces-council: `council/wave_runs.py`, run by `board/pull.py`, fetches the runs with `COUNCIL_MENU_TOKEN` into the
  store's `blockers/`, so they land as `council/blockers/<ref>.json`. Board side (the link) is #147.
- Choices that stand unless he flips them: the charge as eleven buttons; one ending per sitting; Tomorrow moves the date a day;
  a run belongs to the signed-in player and the council reads only his.
- Merge order: #310, #313, #317, then #324 (it retargets to main). #147 merges after the bars-engine routes deploy.
- Next: the room as the board's blocker button for any overdue step, not only Tap the Vein (the panel's "Work through
  what's in the way" opens the room with the step's words), then running the WAVE inside the walkable test room
  (`rooms/walk-room.js`).

## Rulings folded in (Wendell, 2026-10-13, from `somatic-ontology.md`)
- `sb-no-pass-at-daemon`: a 3-2-1 skipped in the cave is picked up in the WAVE room. The room is where the journey begins: the player
  lets spirits in there, or starts a cave journey from there. The cave never makes the player finish a 3-2-1 at the daemon; the room
  holds the skipped one until they come back. Build is not started; this is the call-sheet record only.
- `sb-one-at-a-time`: up to 3 daemons at a time, turn based like Final Fantasy combat. This matches the second slice (three creatures,
  "Working with" picker). The fourth waiting at the door is a cap on the party, not one-at-a-time; any line elsewhere that assumes one
  daemon at a time is superseded.


2026-10-13: the room is walkable (tap the floor), wears the J1 stone, and has two doors behind the seat: Big Mind and the
six game masters. bars-engine #313; see big-mind-cave.md.

## Chat ruling (Wendell, 2026-10-13)
- Wendell, 2026-10-13 22:29 (in the cave branch seams thread): "Cave is breaking here and if you sit down
  without going through the whole wave process a spirit is auto created. It should only emerge once it’s been engaged
  with". A spirit emerges only after the whole W.A.V.E.; standing up partway leaves none. This flips the sit-anywhere
  design's "standing up partway leaves a spirit". Built in the cave by bars-engine #310; in the room, only a charge worked
  through to the end goes through a door as a spirit (the walkable room build, stacked on #309).
- Wendell, 2026-10-13 23:26 (in the cave branch seams thread), after "In the 6 faces room the walking is quite slow":
  "Ah yes. Ok we should disambiguate the walk speed to breath. We have that built into the manual wave experience so we
  don’t need that anymore". Walking no longer keeps one stretch to a breath. Every cave and level walks at one steady
  speed, and the breath lives in the manual W.A.V.E. Built in bars-engine #310 (WALK_SPEED 4 units a second).
- Wendell, 2026-10-13, in the WAVE room thread: the room needs "free walking controls", "a rug or a seat players can sit
  on when they are communing with spirits", and a camera that tilts up and down. Built in bars-engine #313: a walking
  stick and the arrow keys, a rug with a cushion that offers Sit down, and a drag that tilts the camera.

- Wendell, 2026-10-14 00:42 (in the cave branch seams thread): "Ok I think we’ve reached the maturity where we don’t have
  to have the walking happening on rails. It’s causing more trouble than it’s work and we need to test the ergonomics of
  Freeform navigation in preparation of introducing running. The gates for the 6 game master room are too small. They
  should be doors." Not built yet; it is the next piece of work (below).
- Wendell, 2026-10-14 00:39, on doors and the stick: the room now follows five phone-game rules (the stick is never taken
  away; prompts by the right thumb; a zone shows sooner than it hides; one prompt at a time; full pages only from a tap).
  They are in bars-engine `content/ontology-game/cave/DESIGN.md` and apply to every room and cave that gets free walking.

## Built: free walking everywhere and the hall's doors (2026-10-14)
- bars-engine #317 (branch `claude/project-thread-re36zv`, draft) carries #313 with #310 merged in and takes walking off
  the rails in the caves, the hall of the six, the face tunnels and the centre: the stick and the keys, stops as prompts by
  the right thumb whose page opens from a tap, the way past the next stop still shut on the main path and in passages, free
  in the levels. The hall's arches are doors 3.2 wide and 5 tall. Choices (stand unless he flips them): walkable width, prompt
  distances, door size, Sit down moved to the bottom right. DESIGN.md "Free walking everywhere, and the hall's doors".
- cave-test 376 pass, 1 fail: the idle breathing threshold (shoulders 0.010 against > 0.01), which passed on the two
  earlier runs of the branch.
- After his play the same day ("Camera controls are clunky in the game master space and the walking is rather slow", then
  "The center is impassible and we want to be able to have click to walk for when we're testing on the computer"): the
  camera follows the figure, the walk is 7 units a second, the middle of the hall and the centre is open floor (the six stones
  block), and a click on the floor walks there. DESIGN.md "The camera follows the figure, and the walk is quicker" and "The
  open middle, and click to walk". cave-test 385 of 385. He said "perfect. Looking good".
- The phone page https://claude.ai/artifact/23neJJJgywAygUqiJffGvc version 32 carries it.
- Next: running, on the same stick, in a fresh thread. Merge order: #310, #313, #317.

## Handoff that started it (from the WAVE room walk thread, 2026-10-14)
- Where it stands: bars-engine #313 (branch `claude/project-thread-o1ntdv`, carries #309) has free walking in the WAVE
  room only: `freeWalk`, the stick, keys, tilt, the rug, door prompts (`doorZone`, `doorCard`). The caves and the levels
  (hall of the six, face tunnels, centre) still walk on rails (`walkStep`; #310 made it a steady `WALK_SPEED`).
- The work: replace the rails with the room's stick-and-keys walking in the tunnels and the hall, keeping the figure
  inside the tube (`tube.contain`), markers and doors as prompts by the right thumb (DESIGN.md rules), and make the hall's
  gates full-size doors (`roundRoute` door(), `portal_arch` scaled `h*0.75`). Running comes after.
- Merge order: #310 first, then #309/#313; the hint() conflict keeps #309's two lines plus `avatar.userData.stepIdx = 0`.
- The phone page (https://claude.ai/artifact/23neJJJgywAygUqiJffGvc) is built from #313 merged with #310; see the
  cave-phone-page-build memory.
- His third ask, a room generated from a ChatGPT room description with BlenderKit and our own asset pipeline, is its own
  strand (Blender pipeline), not this one.

## Waiting on
The board's blocker panel (docs/blocker-panel.md, 2026-10-12) runs an overdue step through a light WAVE and saves
`blockers/` records; the room can take it over by writing the same record with `engine: "wave-room"`.
His phone play of the room by 2026-10-18 still gates the daemon and alchemy extensions. PR #276 (first slice) is open into the
cave branch. The board has no open rows for the room.

## Files
- `council/passes/6FACE_PASS_wave-room1_2026-10-11.md`, ledger `2026-10-11-wave-room1-pass.json`
- `council/daemons/reports/2026-10-11-wave-room1-*`
- See cave-of-lessons.md (the cave it belongs to) and wave-battle.md (the same WAVE as Sprout's fight).

## 2026-10-24: gas spirits landed (bars-engine #436)

Wendell's screenshot showed the live WAVE room at Witness with a plain grey blob. Cause: the gas-spirit stack (#412 the
worn figure sits, #413 the door's charge is a gas spirit, #419 every charge comes in as a gas and takes form by the work)
was never merged. #436 is #419's head with main merged in (passport purse, ship ember and the `?go=` skip-ahead kept on
both sides) and a `&tour=0` preview key that skips the walkthrough. Merging #436 marks #412, #413 and #419 merged.

- Look step `wave-gas-look-01` (list `wave-gas`) on both boards, preview `/ontology-game/cave?go=home&tour=0`.
- TRIGGER his yes -> mark #436 ready; it merges itself once green. A note -> new round on #436's branch
  (`claude/project-thread-5zrl9b`).
- #434 (one seat for the caves and the WAVE room) touches the same sitting code as #412; whichever lands second merges.
- Checked on the preview: the charge at Witness is `stage gas, 150 motes`, no blob. Not checked: a real phone.
- Cave test (not in CI) in this container: #436 434 pass, main 432 pass; both fail the same three checks (walk swing
  range, a breath-timed button, "walking onto the rug offers Sit down") and stop at the same timeout before the
  door-spirit block, so those failures are main's, not #436's.

## Brief 6, handoff 1 (2026-10-24, thread "Rig the spirits, Shellback first")
Stopped at the 150k line after reading, before any code (the thread opened at ~100k). No commits in bars-engine; branch
`claude/project-thread-9uem3k` is cut from main d462d7e (#436 merged) and is empty. The brief itself is in
/mnt/project-files/door-spirits/handoff-2.md, "Brief 6". What the reading found, so the next thread need not reread it:
- scout: rung 2 is really rung 1. bars-engine `tools/blender-cloud/content/spirits/rig.py` (663 lines, #325) already rigs
  the Shellback tortoise creature and ascended from shellback.py's GLB: joint table, weights, Walk (24 keys, one cycle a
  second) and Idle (48 keys), baked to 1 unit = 1 m. Usage line at its top; an earlier run's output is in
  /mnt/project-files/3d-build/spirit-rig-2026-10-14/ (glb/, poses/, report.json). Source GLBs: .../spirit-shellback-2026-10-14/glb.
  Rigify is not needed for the Shellback; keep it for families rig.py lacks.
- The cave today: spirit-forms.js `parseStage` reads bake_spirits.py's unskinned files (16-bit positions, one primitive per
  material with its look in extras, z-up converted, Y0 0.35). cave.js `parseBody`/`bodyRig` (line ~1312) already read
  bake_daemons.py's skinned format: `_SKIN` attribute (two joints, first weight, band byte), joints [name, parent, pos, quat]
  in node extras, clips as {fps, length, travel, channels} via `keysOf`; `keyAt` (~1560) samples a channel; the walker
  (`wearWalker`) plays walk/run by speed with `travel`.
- Plan: (1) `blender_here.py setup`, run rig.py on shellback creature (and ascended), export. (2) Extend bake_spirits.py with
  the creature/ally rig: keep the per-material primitives and their looks, add `_SKIN` and the joints plus "walk" and "idle"
  keys in node extras the way bake_daemons.py writes them (stay under LATE_BUDGET_BYTES 160 KB). (3) spirit-forms.js
  `buildStage`: when the file has joints, build one THREE.Skeleton and a SkinnedMesh per part. (4) cave.js `walkForm`
  (~5388): replace the coded bob/roll/squash with the walk clip, phase by distance over `travel`, idle when stopped; keep the
  lowest-point-on-floor offset and the turn. (5) Probe first: creature mesh lowest world y within 0.03 of 0 across a walk
  (cave-test.mjs door-spirit block), then a still, then a sheet. Preview `/ontology-game/cave#go=home&grown=7&tour=0`.
