# Codex brief: the projection paint-over as a technique in the design ontology

Wendell, 2026-10-17: "Let’s bring in the game design ontology and add this as a technique. I’d want to see how each of
the game master faces would interface with this kind of pipeline"

Paste into Codex, in this repo:

    Read docs/codex/projection-paint-over-brief.md and make the ontology change it describes, then run the validation commands it lists.

The ontology is written with Codex (`docs/ontology-in-flows.md`, "Changes to the ontology itself"), so this file is the
brief and the change itself is Codex's to make. The council's reasoning is the six-face pass
`council/passes/6FACE_PASS_projection-paintover1_2026-10-17.md`.

**Order.** Apply `docs/codex/asset-sources-brief.md` first. This brief adds to the `asset_sourcing` section that one
creates and uses its `source_channels` and `pipeline_stages`. If both are applied in one Codex run, apply that brief
first.

## The technique

A concept picture is rebuilt as simple 3D blocks, the blocks are rendered from fixed cameras, a painter paints over each
render in the concept's style, and a shader (or a bake) projects each painting back onto the blocks from its camera.
Film calls this camera-projection matte painting. The council's name for it is the **projection paint-over** (the
council's word, expected to be cut if a better one turns up).

## The shape to add

1. **`asset_sourcing.objects`** gains `Technique` and `CaptureCamera`. `DesignObject.types` gains both.
2. **A new list `asset_sourcing.techniques`** with one entry, `projection_paint_over`:
   - `summary`: the paragraph above, in one sentence.
   - `stages`, in order, each a `DerivationRecord` from the stage before:
     | Stage | What it makes | Allowed source channels |
     |---|---|---|
     | `concept` | the target picture | `ai_concept`, `owner_reference`, own drawing |
     | `blockout` | the scene's own geometry, as it ships | `own_work_script`, `blendkit_cc0`, `cc0_library` |
     | `capture` | per `CaptureCamera`: a flat-lit colour render and a depth render | `own_work_script` |
     | `paint_over` | a painting at the capture's exact size | a person's own work, or `own_work_script`; `ai_concept` for a preview only |
     | `project` | a projection shader, or a bake into ordinary textures | `own_work_script` |
     | `live_layers` | lights, particles, creatures and players drawn over the painting | the channels each asset already uses |
   - `CaptureCamera` fields: `id`, `position`, `target`, `field_of_view`, `aspect`, `resolution`, `blockout_commit`.
     Every capture and painting names its camera id.
   - `fits`: small places seen from a few set views (the Between's hollow is the first).
   - `poor_fit`: free-walking spaces such as the caves; whole scenes where the camera leaves the painted views.
   - `limits`: surfaces seen edge-on stretch; surfaces hidden from every camera have no paint and fall back to their
     plain material; light is baked into the painting, so moving light is a live layer; separately painted views can
     disagree at their seams.
   - `characters`: outside the technique. Characters stay on rigged models built in the pipeline; GPT pictures animated
     by Minimax or similar tools are `ai_concept` and do not ship.
   - `evidence`: a claim that the build looks like the concept is tested from where a player actually stands and turns,
     and at least 1 m off each capture camera, never from a still at the capture camera alone.
   - `face_interfaces` (from the pass):
     | Face | Owns |
     |---|---|
     | shaman | one line per view on what it should feel like to be there, and the felt check after |
     | architect | the camera records, the projection or bake, the fallback for unseen surfaces |
     | challenger | the off-axis test, the seam check, the phone budget |
     | regent | an `AssetSourceRecord` per painting: channel, painter, camera id, blockout commit |
     | diplomat | the painting template and the step that hands it to whoever paints |
     | sage | whether the technique fits a given scene, with the dissent kept |
   - `decision_record`: the pass file above, until the council records a decision of its own.
3. **`asset_sourcing.invariants`** gains `projected_painting_follows_source_channels` (a painting that ships is a
   person's own work or our own code's, and carries its `AssetSourceRecord`).
4. **`QUICKSTART.md`**: no change. The asset-sources line already says AI concept art is a reference until rebuilt, and
   a painted-over capture is a rebuild only when a person or our code paints it.

## What this does not change

- No ruling changes. `cs-chatgpt-ai-art` (concept only, 2026-10-12), `c3d-cc0-only` and `cs-cc0-or-own` stand; this only
  writes down how the technique keeps them.
- No flow loads more of the ontology. A round thread that uses the technique loads nothing extra; its callsheet names
  the technique in one line.

## Validation

    python3 -m unittest tests.test_design_ontology
    python3 ontology/tools/validate_package.py
    python3 ontology/tools/term_lint.py
