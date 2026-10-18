# Six-face pass: asset cost, Claude-built versus a generated route (2026-10-18)

Called by Wendell in the thread on github.com/Bingeljell/image-to-3dlab (now AssetFurnace): "We're essentially comparing
the costs of asset creation in Claude AND game design versus outsourcing to local or cloud options and how it would fit
into our development pipeline. Using a sense and respond strategy when would we learn we'd need a new asset and how
could we keep costs down quality and consistency up". No ontology loaded. Faces ran as read-only subagents; the Sage
section is the thread's synthesis. Reports were not saved through `check_report.py` (no daemons were sent).

## Facts used
- AssetFurnace: Apache-2.0 code; Pixal3D (MIT weights, DINOv3 encoder under its own licence), Hunyuan3D (not licensed
  for the EU, UK or South Korea), TRELLIS.2, Stable Fast 3D; needs Apple Silicon 32 GB or an NVIDIA card with 24 GB;
  Blender 4.2+ for finishing; MCP server (`lab mcp`). Wendell's MacBook Air is not enough. Cloud containers here have no GPU.
- Cloud GPU (search results, sources disagree, estimates): RTX 4090 about $0.29 to $0.69 an hour, L40S about $0.47 to
  $1.19; storage $0.07 per GB-month; trial under $3 and $10 to $30 a month are the thread's estimates, GPU time only.
- Measured in the record: J5 robe cloth took 13+ rounds over 5 days (`council/callsheets/blender-pipeline-test.md`);
  Opus threads cost $2 to $12 and 84% of spend was rereading context (`usage-audit/sessions-2026-10-08.md`).

## Casts
Shaman 27 Feeding; Architect 52 Stillness to 20 Witnessing; Challenger 57 Persuasion; Regent 46 Ascent to 18 Stale Air;
Diplomat 7 Muster to 23 Erosion; Sage 46 Ascent (cast in `cast.py`, not read into a section).

## Verdicts
| Face | Verdict |
|---|---|
| Shaman | Claude and Blender rebuilds ship; a generator is a labelled concept and blockout step. |
| Architect | Do not buy the GPU path yet. Add route, rounds and token cost to the sidecar; run one capped trial. |
| Challenger | Hold. Licence read first (free), then a one-hour trial, a rig-fit test on a J4 figure, a nine-figure consistency test. |
| Regent | Trial as reference-only within $3; nothing ships until Wendell rules; ceiling and pod stop rule. Money is reserved. |
| Diplomat | Keep the pipeline Claude-built and human-paid; players' requests trigger new assets; label how each was made. |

## Dissent check
Not unanimous in emphasis: the Architect and Regent would run the trial; the Challenger holds it behind the licence
read and the rig-fit test; the Diplomat would put the second-player test first and spend nothing on cloud GPU before it.
All five agree nothing generated ships under today's rules.

## Sage
The Sage synthesises and does not decide. Contributions kept: the Shaman's route-per-felt-sense (no silent AI), the
Architect's cost structure and signal list, the Challenger's falsification tests and "cheap is not honest" (rounds and
review time are the cost, not GPU hours), the Regent's gates and authority, the Diplomat's labels and player signals.
Dropped: the Architect's per-class dollar ranges (estimates with no ledger), kept only as shape. The order that
satisfies every face: licence read, second-player test, then at most one capped trial.

## Outputs
Positions (auto, on the board): `af-route-per-class`, `af-licence-first`, `af-trial-capped`, `af-ledger-fields`,
`af-sense-and-respond`, `af-honest-labels`. Questions (passed the reach test): `q-af-ship`, `q-af-ceiling`.
Tests set: licence read by 2026-10-22; trial by 2026-10-25 only if the licence passes and Wendell starts it; rig-fit by
2026-10-30; nine-figure set by 2026-11-06 only if rig-fit passes.
