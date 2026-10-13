2026-10-06
# WAVE battle (sprout, battle fr-demo)

## Next
- Wendell, 2026-10-13, after the water-and-fire note: "Yeah we need to rethink this battle logic in general. It's pretty clunky and unintuitive we may need to go through a whole brainstorm intake around it so we can understand how spirits generated from wrong answers turn into fun and meaningful battle encounters. This one's not meeting the mark". Next is a brainstorm intake on the battle as a whole, in a fresh thread, before any patch. The water-controls-fire fix below waits for it and is folded into the redesign.
- Wendell's ruling, 2026-10-13 (Skilled Helper thread, on the Lamp-keeper's tap-through): "Water controls fire not the other way around". Board position `wave-water-controls-fire`: the right answer to a strike becomes a move whose element controls the strike's (River Fill answers fire, Earth Yield answers water, Flame Follow answers Heaven), replacing the next-gate answer of `wave-trigram-moves`. Change it in sprout `slice/battle.js` and `campaigns/skilled-helper/part-two/tools/prototype.template.html` (`NEXT` and the answer check), rebuild both tap-throughs, and settle how an Earth foe is met when no straight gate controls earth.
Round 12 read 2026-10-07 01:07: all seven positions stood, `wave-teacher` = A, Master Yun. In a new thread: the WAVE build on sprout #25 with Yun's taught fight, the straight four first, corner unlocks from spirits, English move names (Sky Lift, Earth Yield, River Fill, Flame Follow, Wind Draw, Lake Gather, Thunder Split, Mountain Stand) and visible qi; trigram lore into design.md as Proposed; rerun the bot test with the straight four only. Sprout #26 is closed. Round 10 built in #26 (`slice/wave.js`, `npm run test:wave`); Welcome's cost against carried HP is the first balance check, after his `?road` playtest.
Exhale: `wave-exhale-ends` was overruled with a steer (a coup de grace, or an "express" move); the WAVE thread reworks Exhale and brings it back as a new position.

## Waiting on
Nothing in fr-demo waits on Wendell. Separate: his context note, 23:26 UTC: "I want to make sure the work from the morning brief is coming into the council board as well". The section says nothing in the three repos named a morning brief; Morning brief routine `trig_01KkW95XDC3xrnYxmBLbjmX2` later reads the board's contacts.

## Files
- `/mnt/project-files/demo/wave-acknowledge-research.md`, `/mnt/project-files/demo/wave-teaching-pass.md`
- ledger `2026-10-06-board-read-2002.json`, `2026-10-06-board-read-2330.json`, `2026-10-06-demo-round8-research.json`, `round9`, `2026-10-06-demo-round10-build.json`, `2026-10-06-demo-round11-pass.json`, `2026-10-07-demo-round12-chat.json`, `2026-10-07-board-read-0107.json`

## Archive
HANDOFF.md: "Open on 2026-10-06, from board read 2002"; "Open on 2026-10-06, from board read 2330"; "Open on 2026-10-06, from the WAVE teaching pass (`fr-demo` round 11)"
