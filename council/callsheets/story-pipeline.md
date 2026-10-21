# story-pipeline

State 2026-10-21. Wendell's board step `ttv-cmvicm0aj` asked the six game masters to study how RPGs and the Pokémon
and Stardew clones produce story, and to leave a repeatable pipeline that keeps story moving beside asset creation.
The pipeline is written; no chapter has run through it yet.

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
- Next: the first pack, Chapter 1 "The Infinite Arcade", at `council/story/packs/calrunia/chapter1/beats.yaml`, written
  by the Shaman from sprout's `campaigns/mtgoa-ch1/story.md` and its `extract.yaml`, then checked. Its asset pass is
  the first real test of whether a beat sheet written this way saves a thread from reading the chapter twice.
- Open: nothing on the board. A beat whose quote would carry more than one line of the manuscript is a board question
  when one appears, and the pack's `status: gated` needs become Your steps rows before any money is spent.
