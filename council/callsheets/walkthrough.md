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
