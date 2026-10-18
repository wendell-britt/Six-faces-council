# Generated meshes: the rule, the licence read and the spend rule (2026-10-18)

Rulings (Wendell, Council Board, recorded 2026-10-18, `council/ledger/2026-10-18-pull-010000.json`):
- `q-af-ship` = B: a generated mesh ships once it is retopologised and re-skinned to the J4 rig, with a plain credit line.
- `q-af-ceiling` = A: $30 a month for cloud GPU spend on assets.
- The six `af-` positions stand (route per class, licence first, capped trial, ledger fields, sense-and-respond, honest labels).
- Wendell, 2026-10-18 01:16, in the thread: "Go" (write the rule, the licence read and the spend rule).

Pass record: `council/passes/6FACE_PASS_asset-cost_2026-10-18.md`.

## The channel: generated_mesh_rebuilt
A mesh made by an image-to-3D tool (AssetFurnace, github.com/Bingeljell/image-to-3dlab) is a shipping source only when both hold:
1. It has been retopologised and re-skinned to the J4 skeleton, hem bones included, and passes the J4 and J4b tests. A mesh that
   has not been is `ai_concept`: reference only.
2. Its credit line says in plain words that it began as a generated mesh and names who reworked it. The line sits where
   players and clients see it, with no click needed. B changes what we promise Portland, so the line is never dropped to save space.

Its manifest sidecar names the model and that model's licence, plus the three ledger fields (`route`, `rounds_used`,
`tokens_cost`). The channel is listed in `asset_sourcing.source_channels` in `ontology/v0.1/source/design-ontology-v0.1.yaml`.

## Licence read (2026-10-18)
Read from the AssetFurnace repo pages (README, NOTICE, `docs/info_and_credits.md`) and Meta's DINOv3 licence page, through a page
summariser. The licence files themselves (`LICENSE`, the DINOv3 text) have not been read word for word.

| Part | Licence | What it means for output |
|---|---|---|
| AssetFurnace code | Apache-2.0 | Keep NOTICE; credit image-to-3dlab with a link if redistributed. |
| Pixal3D code and flow weights | MIT | Clear. |
| DINOv3 encoder bundled with Pixal3D and TRELLIS.2 | DINOv3 License | The README classes TRELLIS output `commercial-conditional` and says to treat Pixal3D Q8_0 output the same. Meta's text, as summarised, does not restrict commercial use or define outputs, bars military, nuclear and espionage uses, requires trade-control compliance, and asks for "Built with DINOv3" where the DINO materials are distributed. |
| Hunyuan3D weights | Tencent Community License | Not licensed for the EU, UK or South Korea, so this rule does not use it. |
| Stable Fast 3D | Stability AI Community License | Gated; not used. |
| Animation clips in the tool (`motions/`) | NVIDIA Open Model License | NVIDIA claims no ownership of outputs; use our own clips for the J4 rig regardless. |

Reading: Pixal3D is the only backend this rule allows. `docs/info_and_credits.md` states the Pixal3D and DINOv3 terms only as "MIT;
the bundled DINOv3 encoder is under the DINOv3 License" and has no output wording. Open before the first shipped asset: read the
DINOv3 License text itself, and decide whether "Built with DINOv3" applies to a shipped mesh (the encoder is not in the mesh).
The tool's `.provenance.json` sidecar goes in the manifest as evidence; it is not clearance.

## Spend rule (money is reserved to Wendell; the pod starts only when he starts it)
- Ceiling: $30 a month. Stop at the ceiling.
- Before any pod: set a provider spend alert at $5 and at $30, and an auto-stop. A pod idle over 30 minutes, or still running when its session ends, is ended.
- The trial: one static daemon body, hard cap $3, a pod ended the same session, results logged with route, rounds and cost.
- Spend is read at the end of every session that used a pod; a forgotten pod counts against the ceiling.
