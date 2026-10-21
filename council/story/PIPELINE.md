# The story pipeline

The canonical way the six game masters push Calrunia's story forward while keeping it aligned with what the art side
has built. Wendell, 2026-10-21, step `ttv-cmvicm0aj000dfikxn526y6xx` on the Council Board:

> We need to have the 6 game masters study how current RPG story development works and what tools are being used to
> this aim. We want to study how Pokemon clone, and Stardew clones are dealing with story content. Specifically we are
> looking to create a repeatable pipeline that the 6 game masters can use to keep pushing the story forward in
> alignment with asset creation

This file is the map. The detail lives in the files it names; change the detail there and keep this in step.

## The unit: one chapter, one pack

A pack holds the story of one chapter of one source, in git as YAML, at
`council/story/packs/<world>/<chapter>/beats.yaml`. A beat names the place, the face whose practice it teaches, the
move from `schema/move-table.json` it puts in the player's hand, the record it comes from, the assets it needs and the
choices it offers. `python3 council/story/check.py` reads the pack against the four registries and refuses a pack that
drifts.

The first pack is Chapter 1, "The Infinite Arcade". Sprout's `campaigns/mtgoa-ch1/story.md` holds its A1 to A8 track
already, and this pipeline gives that track the fields the engine and the art side need. `calrunia/world.yaml` route
`chapter1` names the places each beat previews, so a pack follows the route rather than inventing a second map.

## What the study found

Twelve findings from the sources listed below, and what each one changes here.

| Finding | What we take |
|---|---|
| Stardew's content came from one person writing and rewriting for months: roughly three dozen townsfolk, more than 100 cutscene moments, portraits redrawn again and again | One owner per pass. The pipeline names a face for each stage so a chapter does not pass between five authors |
| Temtem's narrative designer wrote world, main quest and 120-plus sidequests together (over 400,000 words) and handed art descriptions and guidelines to the art department, then took its suggestions | Story and asset need are written in the same beat. The beat sheet is the handoff |
| Disco Elysium kept at least one document per in-game task, holding the expected path, the variants and the reactive moments | A beat carries variants as `choices` with three outcomes, and the pack is the document per beat |
| The same team used articy:draft because writers could read its dialogue trees, its search and its Boolean tags | Structure stays readable in plain text. A visual editor is a convenience, never the source of truth |
| One Disco Elysium choice of four call signs produced 428 new dialogue cards, each needing localisation and voice | Reactive lines are counted before they are written. A choice that multiplies lines is a board question, not an edit |
| ink ships a language and a JSON runtime for browsers; inkjs runs that JSON in Node and the browser, both MIT | The tool we already list in `council/toolbox.yaml`, held for the day a beat needs stateful branching we cannot keep in YAML |
| Yarn Spinner is C#/Unity-first with no official browser runtime; its CLI exports line and localisation CSVs; Yarn Spinner+ is $75 | Rung 4, kept as `available` for its CSV export. Its runtime is C#, so a three.js game would read the CSV and not the runtime |
| Twine and Tweego export a playable HTML bundle, not engine data | Prototype-only, `rejected` for production |
| articy:draft X exports JSON and XML, free to 700 objects, €79.99 a year for one seat | Gated, and only if three or more writers ever share a chapter |
| Arcweave exports JSON, CSV/XLSX and Markdown for $15 a member a month | Gated, noted rather than adopted |
| Godot's Dialogic 2 is MIT but Godot-only and still in development | `rejected`, with the reason, so nobody searches again |
| No studio published a scene-to-asset tracker. The handoff was descriptions and guidelines for the art side | We keep the handoff as `needs` on each beat, checked against the toolbox, because the gap in the record is where drift lives |

Sources read:

- [GQ's Stardew Valley profile](https://www.gq.com/story/stardew-valley-eric-barone-profile)
- [Stardew Valley's Steam announcements](https://store.steampowered.com/news/?appids=413150&appgroupname=Stardew+Valley&feed=steam_community_announcements) and the [1.6 changelog](https://www.stardewvalley.net/stardew-valley-1-6-update-full-changelog/)
- [Víctor Ojuel on Temtem](https://www.victorojuel.org/portfolio-games/clay-ceramics-x78nm) and [his Temtem interview](https://bigbossbattle.com/temtem-interview-12-questions-on-cremas-kickstarter-monster-hunting-sensation/)
- [ZA/UM on articy:draft](https://www.articy.com/en/showcase/disco-elysium/) and [Keenan's GDC talk, reported](https://www.gamedeveloper.com/business/understanding-the-meaningless-micro-reactive-and-marvellous-writing-of-i-disco-elysium-i-)
- [Spiritfarer's design interview](https://www.gamedeveloper.com/design/inside-the-thoughtful-design-of-thunder-lotus-i-spiritfarer-i-) and [Hades' dialogue talk](https://gdconf.com/article/dive-into-the-dialogue-of-hades-at-gdc-2021/)
- [ink](https://github.com/inkle/ink), [inkjs](https://github.com/y-lohse/inkjs/releases), [Yarn Spinner](https://github.com/YarnSpinnerTool/YarnSpinner) and [its CLI](https://github.com/yarnspinnertool/yarnspinner-console)
- [Twine](https://twinery.org/), [Tweego](https://www.motoslave.net/tweego/docs/), [articy:draft X exports](https://www.articy.com/en/adx_basics_exports/) and [prices](https://www.articy.com/shop/pricing/single-user/), [Arcweave exports](https://docs.arcweave.com/project-tools/export) and [prices](https://arcweave.com/pricing), [Dialogic](https://github.com/dialogic-godot/dialogic)

`scout: 3, inkjs (the JSON runtime a browser game can run), then 4 for the eight tools above; five keepers in
council/toolbox.yaml, inkjs the only one we would run today.`

## The stages, in order

Each stage is one thread with one owning face and one checking face, the way `text-to-campaign` runs. The other four
faces stay out of it, and the full council meets once, when the chapter closes.

| Stage | Owner | Checker | Reads | Writes |
|---|---|---|---|---|
| 1. Source | Architect | Sage | the chapter's text, its `extract.yaml`, the corpus BARs | the pack's `source` block |
| 2. Beats | Shaman | Challenger | the source block, `calrunia/world.yaml`, `schema/move-table.json` | `beats.yaml` |
| 3. Assets | Architect | Regent | the beats, `council/toolbox.yaml`, the art record | each beat's `needs` |
| 4. Build | the engine's own strand | Challenger | the pack | the built content, `status: built` and its `ref` |
| 5. Test | Challenger | Regent | the built content | the playtest note and any flipped beat |
| 6. Close | Sage | | the pack, the playtest, the board | the pass, the ledger record, the next chapter's `source` |

What the checkers ask:

- **Challenger on the beats:** does each beat teach the move it names, and can a fresh player pick the right line
  from its wording alone? A beat whose right line is the kindest one fails, the same test `text-to-campaign` carries.
- **Regent on the assets:** is every need either built, or a brief the art side can start, or a board step because its
  tool costs money? Nothing sits in `missing` across a chapter close.
- **Regent on the test:** did the playtest count the move used in play and something the player did outside it?
- **Sage at the close:** which face's finding was dropped, and where did the five disagree?

## What a beat holds

| Field | Meaning |
|---|---|
| `id` | lowercase kebab, unique in the pack |
| `kind` | `scene`, `quest`, `encounter` or `ambient` |
| `place` | a place id from `calrunia/world.yaml` |
| `face` | the face whose practice the beat teaches |
| `move` | a move id from `schema/move-table.json`, owned by that face; required on `quest` and `encounter` |
| `cites` | the BAR ids, manuscript locators or ledger rows the beat comes from. A beat with no record is a guess |
| `scene` | one sentence on what happens |
| `quote` | optional, one line at most, never more |
| `next` | the beats that follow |
| `needs` | assets: `id`, `kind`, `brief`, `tool` (a toolbox id or `brief`), `status`, `ref` when built |
| `choices` | `line` and `outcome` (`right`, `partial`, `wrong`). An `encounter` needs at least one of each |

A `need` carrying a gated tool or `status: gated` is a Your steps item on the board before anyone spends money
(`loop-auto-gate`). `status: missing` is allowed while a chapter is open and is an error at its close.

## The check

`python3 council/story/check.py` reads every pack under `council/story/packs/` and refuses one that:

- names a face, a place or a move that no registry holds, or a move its face does not own;
- leaves a beat with no `cites`, a dangling `next`, or no route from the entry;
- writes an `encounter` without a right, a partial and a wrong line, or a `quote` over one line;
- needs an asset with no brief, a rejected tool, a gated tool that is not marked gated, or a `built` need with no `ref`;
- repeats a beat id or an asset id.

It proves structure, not story. A pack that passes still has to survive the Challenger's reading and a playtest before
the chapter closes.

## What keeps it cheap

- The chapter's text is read once, at stage 1. Every later stage reads the pack and the registries, both small.
- The check runs in a second on the smallest machine, so a session never pays a model to look for a dangling id.
- git is the source of truth and the export. No paid editor sits between a writer and the file, and no copy of the
  story lives in a second place where it can drift.
- One thread per stage, and the pack carries what the next thread needs, so a chapter costs what its beats cost.

## What waits for him

Canonical prose, anything that names a person, money and `council/faces.yaml` stay reserved (`council/faces.yaml`). A
beat whose quote would carry more than a line of the manuscript is a board question. Everything else lands as a
position that stands unless he flips it, and the next stage reads the flip from the pack.

## Where the six faces sit

| Face | Owns in the pipeline |
|---|---|
| Shaman | the beats: what the player feels, which practice a scene asks for, the look of a place |
| Architect | this file, the schema, the check, the toolbox mapping from a need to a tool |
| Challenger | the guessing test, the three outcomes, what breaks when a beat is cut |
| Regent | the gates: what ships in a chapter, which needs become board steps, the definition of done |
| Diplomat | the player-facing words and the onboarding path into a chapter, and who a beat leaves out |
| Sage | the close, the dissent, the handoff to the next chapter |

## What this session did not check

No pack exists yet, so the check has run on a fixture and on the failures it refuses, not on Chapter 1. Whether a beat
sheet in YAML is faster to write than sprout's `story.md` is a question for the first chapter that runs through it,
and the pipeline says so rather than measuring a saving it has not seen.
