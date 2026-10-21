# story-pipeline

State 2026-10-21. Wendell's board step `ttv-cmvicm0aj` asked the six game masters to study how RPGs and the Pokémon
and Stardew clones produce story, and to leave a repeatable pipeline that keeps story moving beside asset creation.
The pipeline is written and Chapter 1 has a pack; the Challenger's reading and a playtest are still owed.

- Studied 2026-10-21: twelve findings from Stardew's production record, Temtem's narrative designer, Disco Elysium's
  per-task documents and its 428-card choice, Spiritfarer and Hades, plus the tool landscape. The findings, what each
  one changes, and every URL read sit in `council/story/PIPELINE.md`. The short version: teams write task-level specs
  rather than one bible, they hand art descriptions and guidelines across instead of tracking a shared asset list, and
  a four-way choice can become hundreds of lines. That last number is why reactive lines get counted before anyone
  writes them.
- Built 2026-10-21: `council/story/PIPELINE.md` (six stages, owner and checker per stage, the beat fields, the reserved
  lines) and `council/story/check.py`, which reads a pack against the faces, the move table, the toolbox and the world
  registry. `tests/test_story_pack.py` holds a fixture pack and one case for each rule the check refuses.
  `python3 council/story/check.py` prints `no packs yet` until the first pack lands.
- Toolbox 2026-10-21, rung 3 then 4 of the ladder: `inkjs` was already listed and stays the only runtime a three.js
  game would run. Added `yarn-spinner` (available for its CSV export), `articy-draft` and `arcweave` (gated, for the
  day several writers share a chapter), and `twine-tweego` and `godot-dialogic` (rejected, with reasons).
- First pack, written 2026-10-21 by a Freebuff session on main (stage 2, the Shaman's seat):
  `council/story/packs/calrunia/chapter1/beats.yaml`, eight beats A1 to A8, 25 assets, all six faces, places taken
  from route `chapter1` in `calrunia/world.yaml`. `python3 council/story/check.py` prints
  `ok calrunia-chapter1-arcade: 8 beats, 25 assets`. A mutated copy (regent given `fire_transcend`) is refused, so
  the check reads this pack and not only the fixture.
- Sprout merged its own beat table the same day (PR #66, `campaigns/mtgoa-ch1/beats.yaml`): one flat row per beat
  with the gate flags, the line pointers into `story.md` and the card moments. The pack cites those rows per beat
  and leaves the gates where they are, so the engine's table and the pack are two views of one track. Two needs are
  marked `built` against what exists (the spirit generator, page v28, and the wave room, bars-engine #317); the
  other 23 are `brief`.
- Next: the Challenger's reading of the beats (stage 2's check) at the two questions the pipeline sets: does each
  beat teach the move it names, and can a fresh player pick the right line from its wording alone. Then the Regent's
  asset pass (stage 3), which sorts the 23 briefs into built, started and board-step.
- Open: nothing on the board. One read for the Challenger: `a7-the-oath` carries `wood_transcend`, a move with no
  step from satisfied, so the oath's practice only lands while the player is dissatisfied or neutral. A beat whose
  quote would carry more than one line of the manuscript is a board question when one appears, and a gated need
  becomes a Your steps row before any money is spent.
