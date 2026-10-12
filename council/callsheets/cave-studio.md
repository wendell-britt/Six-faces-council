2026-10-12 (updated 22:55)
# Cave studio (Blender in the cloud for the cave, battle fr-cave-studio)

## Next
One fresh thread, one piece of work: record his round 1 and turn it into the first test.

1. **His round 1 is answered and already in main** (board pulls, ledger `2026-10-12-pull-222843.json`, `-222920.json`, `-223756.json`):
   - `cs-chatgpt-ai-art` = concept only. His steer: "for now it's for concept, we will need an additional production step to rebuild the pieces ourselves".
   - `cs-first-piece` = chamber dressing for the kit. The council had leaned to the daemons.
   - `cs-asset-kind` = pictures to build from. His steer: "I'd need to see and trust blenders ability to take pictures to build from".
   - `cs-cc0-or-own` = overruled, with a question in the steer (below). The other seven positions stand.
2. **Record his turns, quoted, under Round 1** in bars-engine `.specify/specs/cave-studio/request.md` (merged in #284), then change
   `spec.md`, `plan.md` and `tasks.md` to match: the first piece is chamber dressing, ChatGPT art is a reference that sessions rebuild by
   script or by hand, and nothing from ChatGPT ships. `cs-stand-in` has nothing to stand in for until he says otherwise.
3. **Answer the question in his overrule from the record, then reshape the row.** He wrote: "How are people getting around this? Well not
   around but if royalty free can be extracted then what's the point of this". The council's draft answer: Blendkit's Royalty Free licence
   covers renders, images, prints and software whose models a third party cannot separate or open. Its Licensing FAQ says a game may use
   them "if these can't be extracted by the users in an easy way". A plain GLB in a web page can be extracted, so a page cannot carry
   one. Games get around this by shipping models inside their own protected asset bundles, and a page can show a render or a video
   instead. CC0 has no such limit. Do not loosen the studio's CC0 gate in `tools/blender-cloud/` until he rules; it matches the terms
   as read on 12 October (article 5 of the terms, and the FAQ).
4. **The test he asked for.** From one reference picture, build one chamber-dressing piece in Blender by script and show the preview beside
   the picture, so he can see and trust the step. It waits on a picture. The Drive folder step is `steps/cave-studio-01`.
5. **Tick the Definition of done** in bars-engine `.specify/specs/blender-cloud-hardening/spec.md`. Every item is met; the evidence is in
   ledger `2026-10-12-blender-cloud-session.json`.

## Waiting on
- His picture, for the see-and-trust test (Your steps, Cave studio, step 1, due 2026-10-19). Step 2, the Blendkit search check from his own
  machine, is optional.
- His eyes on the published Cloud Walker page (https://claude.ai/artifact/SUZYu1w1P5b61Cn6pj7Vwg) and on the board. Neither was opened as
  a private URL from the cloud.
- Motion2MixamoRig is set aside until he asks (`mm-set-aside`, deferred). Its chain is non-commercial; the licence reading is in the ledger record.

## Files
- bars-engine `.specify/specs/cave-studio/` (request, spec, plan, tasks; PR #284, merged 04da026); `tools/blender-cloud/` and
  `.specify/specs/blender-cloud-hardening/` (PR #281, merged 7d9d179)
- ledger `2026-10-12-feature-request-cave-studio-round-1.json`, `2026-10-12-blender-cloud-session.json`
- Falsification test, passed 2026-10-12: `build_figure.py` and `build_kit.py` rebuild `figure.glb`, `cave-kit.glb` and `spots.json` byte for
  byte in the cloud (about 6 seconds).
- Session cost is not recorded: read it from the result events of session_015usKXsYhza5EkN1GcKofCT after the work.
- See cave-of-lessons.md and big-mind-cave.md (the two caves), studio.md (the pipeline they sit in).

## Archive
Nothing is archived yet.
