2026-10-11
# WAVE room (the cave's home)

## Next
Build the room's first slice in a fresh thread (`wave-room-first-slice`, Opus), in bars-engine on the cave's branch
(`claude/project-thread-ottswt`, PR #265; the cave is not on main yet). Brief, all settled:
- One scene in `content/ontology-game/cave/`, built from the cave kit: a seat facing a door, the faceless figure on the
  seat, the cave's breath, Calm switch and "Step back". Reached two ways (`wave-room-cave-link` = both): from the body map
  on its own, and from the cave's daemon stop by a new "Take it home" choice beside the staged 3-2-1, which leaves a
  lantern at the spot, brings the charge in with its feeling known, and returns to the lantern when the room is done.
- The flow is a table of steps, as `STRETCHES` is: Welcome (door opens on an out-breath, a grey shape comes in), Witness
  (where and texture), Acknowledge (a name the player writes and an element, "I don't know" offered), Allow, Accept,
  Appreciate with Not now, Validate, then the fork. Step words come from `WAVE_STEPS` in `game.jsx` (lines 1092-1108).
- The fork asks "What do you actually want right now?" (`wave-room-goal` = now; nothing stored), then where the charge
  pushes the next move: toward it or away (`wave-room-validate-first`).
- Stays: the cave's staged 3-2-1 chat, aimed at the goal, ending with one next move the player writes
  (`wave-room-stay-move`). Goes: the door opens on the exhale, the charge leaves at its own pace, a named light in its
  colour stays on the threshold for the sitting (`wave-room-release`). Then "Is anything still here that says it
  belongs?" restarts at Welcome with a new charge (`wave-room-parts-restart`). After three rounds in a sitting, offer to
  rest it by the door with a lantern (`wave-room-stop`).
- The player writes every line; words stay on the page. Extend `cave-test.mjs` at 390 by 844 for both branches, the
  restart, the rest offer and the lantern round trip.
- For the 10-18 test, after each branch the page asks "Did it leave, or did you get rid of it?" and keeps the answer and
  round count on his device only.

## Waiting on
Nothing on the board. Settled 2026-10-11 21:54 Send (ledger `2026-10-11-pull-212941.json`): `wave-room-cave-link` =
both, by lantern; `wave-room-goal` = ask in the moment. All eight `wave-room-*` positions stood. His phone play of the
slice by 2026-10-18 gates the daemon and alchemy extensions.

## Files
- `council/passes/6FACE_PASS_wave-room1_2026-10-11.md`, ledger `2026-10-11-wave-room1-pass.json`
- `council/daemons/reports/2026-10-11-wave-room1-*`
- See cave-of-lessons.md (the cave it belongs to) and wave-battle.md (the same WAVE as Sprout's fight).
