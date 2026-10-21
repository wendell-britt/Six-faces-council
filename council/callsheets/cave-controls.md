# Cave controls

Phone camera and touch controls for the cave (`content/ontology-game/cave/cave.js` in bars-engine). Wendell,
2026-10-21: "Ok the controls are pretty clunky still. Can we do some research on standard phone 3d game camera
manipulation in contexts similar to ours".

## 2026-10-21: research done

Findings page: https://claude.ai/artifact/BwBweZR865zrKckj9tCVMY (copy at
`/mnt/project-files/cave-controls/cave-controls.html`). Sources: Apple WWDC26 session 358 ("Make your game great with
touch"), Game Accessibility Guidelines, Xbox accessibility guideline 117, Unity Cinemachine deoccluder docs, reviews of
Sky, Genshin, Pocket Camp, Monument Valley.

Positions (stand unless he flips them; his look at the preview is the ruling, no board question):

- `ctl-split-thumbs`: left half walks with a floating stick, right half is a camera touchpad (relative), pinch zooms.
- `ctl-tap-rule`: under 10px and 500ms is a tap, anything else a drag; each pointer tracked on its own.
- `ctl-generous-taps`: hit areas at least 48px on screen around the elder, the daemon and objects; a tap walks there and
  opens the card; tap-to-walk keeps working with a ring marker; a Talk button (88px) bottom-right when near someone.
- `ctl-gentle-camera`: follow rate about half of today's 6; a hand turn holds for two seconds of walking before easing
  back; pitch eases to level; a ray pulls the camera in front of walls instead of the post-lerp clamp.
- `ctl-still-mode`: still mode for tired eyes (Ari's ask): no automatic camera movement, slower turning, bigger targets,
  on by default under `prefers-reduced-motion`; pairs with round 4's caption pace.

scout: rung 3. Rules 1, 3, 4, 5 and 7 tune the cave's own input code. For the camera, probe camera-controls 3.1.2
(yomotsu, MIT, about 12KB, three >=0.126, `colliderMeshes`, `setBoundary`, `interactiveArea`) against one added raycast
in our follow camera; keep whichever slides along walls better. nipplejs 1.0.4 is the stick fallback.

Faults found in cave.js on main: dead band 8 to 12px between tap and look (2502, 2513); hand turn and auto-follow fight
(2819, 2850); pitch never settles, `LOOK.settle` unused (898); one drag slot, a second finger overwrites (2496); fixed
116px stick (2132); only the element mesh is tappable, near misses walk (2520); `keepIn` after the lerp snaps at walls
(4589).

## Brief, 2026-10-21 02:10 UTC: controls round 1 (fresh Opus bars-engine thread)

Build the five positions above in `cave.js`, base on main. Thread "Elder card minimize and close" owns bars-engine #398
(the elder card) and round 4 comfort is on branch `claude/project-thread-r1hsuf`; read both diffs first and keep the
input changes clear of their card and caption code, or build on #398 if the elder's tap target needs it. Prove it
cheapest first: a Playwright touch script that checks tap vs drag, two fingers at once, and the camera distance near a
wall, before any video. Reply with a one-click preview link that opens in the cave (skip-ahead params to the elder
spot), on the Vercel preview of the pull request. End with what was not checked (real phone feel).

## 2026-10-21: round 1 built (bars-engine #411, draft, CI green)

Preview at the elder: https://bars-engine-git-claude-projec-9d09c6-wendells-projects-9c1b16dc.vercel.app/ontology-game/cave?go=elder
(`?go=cave`, `?go=home`, `&at=<place>` also work). All five positions are in `cave.js`; `content/ontology-game/cave/controls-probe.mjs`
reruns the touch checks in a few minutes (11 of 11 pass). The camera ray marches the tunnel's own `contain()`; camera-controls
was not probed. cave-test.mjs on main: 502 pass, 3 fail (camera inside while walking, 472 of 488; the hall check "camera comes
round behind the figure" and its follow-up). The branch's full run was cut short by the handoff.

Ruling, Wendell, 2026-10-21, on the hall check (a held diagonal leaves the figure about 45° off the camera's back): "Ah yes I
see the problem. The player should face in the direction of the stick".

## Brief, 2026-10-21 02:30 UTC: controls round 1b (fresh Opus bars-engine thread, owns #411, branch claude/project-thread-43i8fm)

1. Build the ruling on #411: the figure faces the way the stick points (as the camera saw it when the thumb went down), not the
   way it slid along a wall; in the hall and the centre the camera comes round behind that facing. Read home base's
   `R.stickFrame` (19 October) first; a frozen frame in the hall tried in round 1 flipped the camera half round on the ring
   (`wk.dir` flips when `along` goes negative), so the ring needs its own handling. Make the hall check pass without loosening it.
2. Run `controls-probe.mjs`, then the full `cave-test.mjs` in the background (about 30 minutes under swiftshader; deps:
   typescript@5, playwright, three@0.128.0 symlinked as node_modules), and compare with main's 502/3.
3. First fix a regression the branch's full run found (496 pass, 9 fail; main 502/3): home base's pinch. The test's first
   finger lands on the left half, so the floating stick takes it and the two fingers never pinch; the creature close-up
   checks after it fail with it. A second finger while the stick is floating should start a pinch (or the stick should
   float only once the finger moves). The camera-inside-while-walking failure on main now passes.
4. Reply with the `?go=` preview link, mark #411 ready, and say what was not checked (real phone feel).

## 2026-10-21: round 1b built (bars-engine #411, three new commits, CI green on d7a0a44; 59a63d5 pushed)

- The figure faces the stick, not the way it slid. In the hall and the centre the stick's forward is taken from the camera as
  the thumb goes down and held as a turn off the ring's way; the camera rides round with the ring by the same turn and eases
  behind the figure's facing. Up held still walks round the ring to the next door; no flip on a held diagonal. Tunnels keep
  the live view and the turn along the way. A hand look turns the held forward too.
- Pinch regression from round 1 fixed: a second finger while the stick's finger is still within its tap makes a pinch (home
  base and cave).
- Checks: `content/ontology-game/cave/hall-probe.mjs` (new, a few minutes) 6 of 6 on 59a63d5, including the unchanged hall
  check; controls-probe 11 of 11 on d7a0a44. A full cave-test run on d7a0a44 timed out walking the centre to its ways back
  (453 pass, no fails before it); 59a63d5 fixes that cause. The full run on 59a63d5 was started but cut by the handoff.

## Brief, 2026-10-21 03:20 UTC: controls round 1c (fresh Sonnet bars-engine thread, owns #411, branch claude/project-thread-43i8fm)

1. Run the full `cave-test.mjs` on #411's head in the background (deps: typescript@5, playwright, three@0.128.0 symlinked as
   node_modules in the repo root and cave/; build with `node scripts/build-ontology-game.mjs`). Compare with main's 502/3.
   A new failure on the hall, centre or a round room's walk goes to an Opus thread with the failing line.
2. If no new failure: reply with the preview link
   https://bars-engine-git-claude-projec-9d09c6-wendells-projects-9c1b16dc.vercel.app/ontology-game/cave?go=elder and mark #411
   ready. Not checked: real phone feel.
