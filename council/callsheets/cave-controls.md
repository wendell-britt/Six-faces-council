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
