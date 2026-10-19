2026-10-18
# Walkthrough build (the golden path)

Wendell, 2026-10-18: the game lacked a walkthrough test, a sprite that does everything from the title to a saved,
finished quest. Then, on the road's battle panel: "This part should open a final fantasy style battle system OR the 3d
battle system we've been working on k codex. ... This battle type for example just doesn't work and needs replacing."

## Where it stands
- Walkthrough build: sprout PR #58 (draft, branch claude/project-thread-99agas): title, creator, intake, the First
  ally quest, autosave and Continue. `npm run walkthrough` plays it, records build/walkthrough/walkthrough.mp4 and
  writes build/walkthrough/summary.md.
- Battle replacement: sprout #59 (draft, stacked on #58, branch claude/project-thread-i8uuuw). The strip's
  encounter opens the Super NES face-off from sprout #29 (Fight, Magic, Listen, Item; Master Yun's lesson the first
  time down the east road; the staff as gear per battle-fight-and-magic C). The W.A.V.E. panel is gone; wave.js stays
  only as the rules the face-off uses. The bot plays the face-off by its buttons (`data-cmd`).
- Board: `battle-road-opens-face-off` overruled 2026-10-19 (ledger council/ledger/2026-10-19-pull-223918.json): "I think we
  should develop the SNES face-off alongside the 3d Moonlit meridian. I want to see how they develop in parallel using the
  underlyin glogic, but a different UI". The road keeps the face-off; the Meridian now plays the same fight in 3D.
- Face-off in 3D: sprout #61 (draft, stacked on #59, branch claude/snes-face-off-un5nbg). `slice/spar.js` is the one spar
  both screens start; `npm run meridian` bundles slice/battle.js, spar.js and data/ into the Meridian's
  `web/dist/faceoff.js` (it stays buildless); `web/dist/clips.js` maps each command to a cultivator clip. Rerun the
  bundle after any rules change, or `npm run test:meridian` fails. test:meridian 16/16 (the 3D page, played by the WAVE
  policy, replays line for line through slice/battle.js), test:battle 113, walkthrough passes. `?foe=spirit` for the spirit.
  Not checked: a real phone; the Meridian's hosted Site is not redeployed.
- Phone build: https://claude.ai/artifact/ArJr2ii1LrquyXeoUi2AUy (multi-file, two publishes for the 255-file limit).

## Open
- His phone play of the face-off on the road.
- #29 is now carried by #59; close #29 once #59 merges. Merge #61 after #59 (retarget it to #58's branch or main then).
- His look at the 3D face-off side by side with the SNES one: serve `root-fight/moonlit-meridian/web/dist` (e.g.
  `python3 -m http.server` there) beside the slice's `?battle=daemon`.
- `npm run test:playtest` fails on #58's base too (tools/simulate-slice.mjs exits 1 when a farm-fight policy is
  stuck); not from this work.
- Next build after his look: integration (Mother Ede's first Skilled Helper talk as quest 2), then the settlement.

## Next: the spirit board's 2D sprites in the face-off (brief for the next thread)
Wendell, 2026-10-18 19:07, after the face-off landed: "Ok now we've got this let's start introducing the 2d sprites from
the spirit board. We have logic for veiled spirits and unveiled spirits and elemental version connected to various daemons".
- Stack on sprout #59 (branch claude/project-thread-i8uuuw), which this thread owns along with #58; keep
  `npm run walkthrough` at 8 of 8 and republish the phone build (https://claude.ai/artifact/ArJr2ii1LrquyXeoUi2AUy).
- The art: the spirit generator's sprites rendered from the Blender families (spirit-generator.md; bars-engine #318
  `tools/blender-cloud/content/spirits/`, page https://claude.ai/artifact/B9zYsNyxe6UVhRF3jcNP85 and its later
  versions; the Victim's Ballad on v28). Each daemon has a family (`sg-body-from` A: the urge picks the family).
- The logic to wire: the three states (`ss-three-states`, `ss-markers`), veiled and flooding (`ss-not-veiled`, perceptual
  shadow, bars-engine #326), the element versions, and the daemon to family map (`dmt-*`, `ds-*` positions).
- The hook: battle-ui.js already calls `drawSpiritArt(g, foe, x, y, scale, now)`, and main.js draws `record.battleAsset`
  when a record has one. Today daemons on the strip are a coloured block (main.js `drawDaemon`). Default: on the strip the
  foe is the encountered daemon's family spirit (wild, dissatisfied) in the worn element, veiled until Listen reveals it,
  drawn from packed sprite assets by asset id (CLAUDE.md: data names ids, never paths). Sprites go through the SNES
  profile check (15 colours per palette); remap colours first, never redraw without his approval.
- Any design question goes through the reach test onto the Council Board.
