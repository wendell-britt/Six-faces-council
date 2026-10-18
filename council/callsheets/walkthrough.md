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
- Board: position `battle-road-opens-face-off` (face-off, not the 3D Moonlit Meridian fight) stands unless he flips it.
- Phone build: https://claude.ai/artifact/ArJr2ii1LrquyXeoUi2AUy (multi-file, two publishes for the 255-file limit).

## Open
- His phone play of the face-off on the road.
- #29 is now carried by #59; close #29 once #59 merges.
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
