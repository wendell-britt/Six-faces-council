# Codex brief: asset sources and the Blender pipeline in the design ontology

Wendell, 2026-10-17: "How do we make sure the design ontology includes using blenderkit? As well as other assets for
making the blender pipeline part of the ontology"

Paste into Codex, in this repo:

    Read docs/codex/asset-sources-brief.md and make the ontology change it describes, then run the validation commands it lists.

The ontology is written with Codex (`docs/ontology-in-flows.md`, "Changes to the ontology itself"), so this file is the
brief and the change itself is Codex's to make.

## What is missing

The rules for game assets already exist, but only in the board, the ledger and bars-engine:

| Rule | Where it lives |
|---|---|
| Only own work and CC0 assets ship; each asset lists source and licence in the manifest | board `c3d-cc0-only`, `cs-cc0-or-own` |
| A Blendkit Royalty Free model may appear in renders and previews, never in a published page (a GLB in a page can be extracted; Blendkit terms, article 5) | bars-engine `tools/blender-cloud/README.md`, "A seventh problem: licences"; board `bpt-no-restricted-flag` |
| ChatGPT art is concept only; a production step rebuilds each piece | board `cs-chatgpt-ai-art`, answered "Concept only" on 2026-10-12 |
| The non-AI route is first class | bars-engine `CLAUDE.md`; ontology `equivalent_routes` |

The ontology has no word for a production asset or a pipeline stage. A design thread that loads the `game_design`
profile cannot see any of the rows above, so it can propose a mechanic whose art the record already forbids.

## The shape to add

Extend the provenance vocabulary the ontology already has. Do not start a parallel one: `Source`, `Artifact`,
`DerivationRecord`, `AttributionRecord` and `ReuseAuthorization` already carry most of the meaning, and
`authority.creative_source_use` already says who decides a licence.

1. **A new section `asset_sourcing`** in `ontology/v0.1/source/design-ontology-v0.1.yaml`, placed after
   `creative_reuse_and_personal_meaning`, with a `decision_record` pointing at this brief until the council records
   one. It holds:
   - `objects`: `AssetSourceRecord` (the manifest row and the `.json` sidecar beside each fetched file: name, author,
     licence, source URL, library id), `SourceChannel`, `PipelineStage`.
   - `source_channels`, each with `licence`, `may_ship_in_web_build` and `may_appear_in`:

     | Channel | Licence | Ships in a page | Example |
     |---|---|---|---|
     | `own_work_script` | own work | yes | `procgen.py`, `cave/build_kit.py`, `character.py` |
     | `blendkit_cc0` | CC0 | yes | Fern 02, Boulder 01 (fetched with `license:cc_zero`) |
     | `blendkit_royalty_free` | Royalty Free | no; renders and previews only | the first viewer's chair, replaced in version 5 |
     | `cc0_library` | CC0 | yes | Poly Haven; ambientCG, Kenney and Quaternius (inferred CC0, check each asset's page) |
     | `code_library` | MIT or similar | yes, as code | three.js |
     | `ai_concept` | none claimed | no; reference for a rebuild | Wendell's ChatGPT concept pictures |
     | `owner_reference` | Wendell's own | reference | photos and sketches he supplies |

     A source not on the list is not cleared until it is added here by his ruling.
   - `pipeline_stages`, in order, each a `DerivationRecord` from the stage before: `concept`, `source`
     (`blenderkit_fetch.py`), `prepare` (`prepare_asset.py`), `build` (`scene.py`, `procgen.py`, `from_picture.py`,
     `chamber.py`), `detail_and_bake` (`detail.py`, `bake_tiles.py`), `export` (GLB), `register` (manifest row),
     `present` (`build_viewer.py`, the game page).
   - `invariants`:
     - `shipped_asset_has_source_and_licence`
     - `no_restricted_licence_in_extractable_build`
     - `ai_concept_is_reference_until_rebuilt`
     - `every_shipped_asset_has_a_non_ai_route` (ties to `equivalent_routes`)
   - `authority`: licence terms belong to the rights holder (`creative_source_use`); which channels are admitted is
     Wendell's (`c3d-cc0-only`).
2. **`entity_families.ProvenanceObject.types`** gains `AssetSourceRecord`. `DesignObject.types` gains
   `SourceChannel` and `PipelineStage`.
3. **`hard_invariants`** gains `shipped_asset_has_source_and_licence` and `no_restricted_licence_in_extractable_build`.
4. **`ontology/manifest.yaml`**: under `current_sources`, an entry `asset_pipeline` pointing at bars-engine
   `tools/blender-cloud/README.md` with `status: implementation_record`, and a note that bars-engine test G6
   (`tools/blender-cloud/tests/test_offline.py`) and `build_viewer.py` enforce the two invariants. No new load profile:
   `implementation_translation` already covers it.
5. **`QUICKSTART.md`**: one line under the BAR paragraph: a game asset carries its source and licence, only own work and
   CC0 ship in a page, and AI concept art is a reference until rebuilt.

## What this does not change

- No flow starts loading more of the ontology. Art, build and tuning rounds still load nothing; bars-engine's G6 check
  and `build_viewer.py` already carry the rule as a check (`docs/ontology-in-flows.md`).
- No ruling changes. Every row above is already Wendell's answer; this only gives them a place in the ontology.

## Validation

    python3 -m unittest tests.test_design_ontology
    python3 ontology/tools/validate_package.py
    python3 ontology/tools/term_lint.py
