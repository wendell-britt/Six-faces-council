# Calrunia character creator

Wendell, 2026-10-21 17:04 UTC: "ok next thing I need to work on is a Calrunia Character creator. This will create the
avatars that will be used in Root and Sprout, and the Cave of Lessons. I want to think through what kind of character
creator customization options are avaiable, and what needs to be added to the pipeline to make this make sense."

Pass `calrunia-creator1` (thinking pass, 2026-10-21; built nothing). Rows: `council/callsheets/rows/calrunia-creator1-2026-10-21.json`.

## What exists (three creators that do not talk)

| Creator | Where | Choices | Output |
|---|---|---|---|
| Sprout traveler | sprout `slice/creator.html` (#19), `tools/build-traveler.mjs` (#16) | 3 outfits (jacket, wrap dress, long coat) open to every gender (`tr-outfits-open`); male/female/nonbinary bodies on LPC; 4 builds, width only, 32 px cap (`tr-builds-narrow`) | walk, slash, thrust sheets |
| J4 cave figure | bars-engine `content/ontology-game/cave/character.py` | build slight/average/broad (width, height fixed 1.75 m); palette dusk/jade/hemp (cloth only, one fixed skin) | glb; six daemons are its `WARP` rows |
| J5 garments | `garments.py --all`, `cloth.js` on draft PRs #315, #364, #365 (not main) | robe, sash, topknot, cuffs, skinned to the one rig | glb pieces |
| bars-engine portraits (older) | `src/lib/avatar-utils.ts` `AvatarConfig {nationKey, archetypeKey, domainKey, variant, genderKey}`, `Avatar.tsx`, `public/sprites/parts` | nation and archetype layers | 64 px portraits, walkable sheets |

The cave walks `cave/player/walker.glb` (Average Dusk mocap, #381); the Between walks `public/between/m/player.glb` with a hue ring as the only personal mark. Root lives in root-game (not cloned here); its renderer is unread. The passport (`schema/passport.schema.json`, #410) has no appearance field.

## Tool scout (rung 4, one worker, 2026-10-21)

- Ready Player Me: shut down 31 January 2026 (Netflix bought it). Do not build on it.
- VRM + `@pixiv/three-vrm` (MIT): a standard humanoid container; optional export later, not needed for the first build.
- MPFB2 (MakeHuman for Blender): assets CC0, code GPL. Use its targets as reference shapes for our own low-poly shape keys. Headless use untested.
- CharMorph / MB-Lab: licence friction (AGPL bases), realistic style. No.
- Avaturn: $800 a month, selfie-based. No (and `ba-likeness-choices` rules out photos).
- 2D: render our glb to sprites (our `tools/blender-cloud/content/spirits/shellback.py` already does it for spirits; `coreway-labs/blender-sprite-render` batches 4 directions). LPC stays under `cc-store-safe`.
- Verdict: build our own on rung 3 pieces (Rigify, shape keys, three.js morph targets, our sprite render). Toolbox keepers: three-vrm (already listed), MPFB2 targets, blender-sprite-render.

## The one spec: `look` in the passport

Keys only, never free values, so each place maps a key to its own assets:

```
look: {
  v: 1,
  body:  "a" | "b" | "c"                 # the three body shapes Sprout already draws (named by shape, open to all genders)
  build: "slight" | "average" | "broad" | "round"
  skin:  0..7                            # one ramp shared by every place
  hair:  {style: key, color: 0..7}       # store-safe styles only (cc-store-safe)
  outfit:{set: "traveler" | "robe", piece: key, palette: key}
  move:  key                             # later: gait from the Six Fundamental Movements
}
```

Each place has a resolver: Sprout maps keys to build-traveler parts; the cave and the Between map them to character.py
builds, shape keys, skin colour and garment glbs; Root reads the same rig once its renderer is known; bars-engine
portraits can render from the same keys later.

## Option menu (first creator vs later)

- First: body shape (3), build (4), skin (8), hair style (4 to 6) and hair colour (8), outfit set and palette.
- Later: height, age, face marks (the 3D figure is faceless, `cave-avatar-self`), gait/move style (`ba-likeness-choices` "how they move"), mobility aids, earned pieces (sash colour by element, jade by nation), spirit companion.

## Pipeline gaps

1. Passport has no `look` field: schema bump, fixtures, both contract tests.
2. 3D figure has no body shapes, skin ramp or hair: shape keys on the base (MPFB2 targets as reference), skin as a material parameter, hair meshes through his eye (`cc-wardrobe-gate`).
3. J5 garments are not on main (#315, #364, #365 wait on `j5-panels-look-12`).
4. No sprite render of the player figure from 3D; Sprout keeps LPC until a rendered sheet passes his eye.
5. Root's renderer is unread: a find-it task for the root-game thread.
6. The walker and the Between's player.glb need morph targets and garment swap at runtime (`bpt-skinned-garments`).
7. The older bars-engine AvatarConfig stays as is; nation and archetype stay identity, not appearance.

## Recommended first build (no art round)

The look contract, in bars-engine: `look` in `schema/passport.schema.json` with fixtures and the contract test; a
resolver table (`calrunia/look-map`) from each key to Sprout traveler parts and to character.py parameters; the cave
walker and the Between's player tinting skin and cloth from `look`, and character.py taking `--skin`. Proof: one
fixture look renders in the cave and the Between and names the matching Sprout sheet. Then round 2: body shapes as
shape keys, and a four-direction sprite render of the 3D figure beside the LPC traveler for his eye.

## Open

- Board: question `cr-look-by-place`, positions `cr-*` (rows file above). Rows landed on main and the board republished (2026-10-21).
  Deliverable page: https://claude.ai/artifact/GUcAH9AvymhZdEpLCp932V.

## Pass calrunia-creator2: the creator as play (2026-10-21, Opus, design ontology game_design profile)

His board answers (council/ledger/2026-10-21-pull-171630.json): `cr-look-by-place` C (traveler first, robe earned);
`cr-build-own` overruled ("worth another pass at what kinds of character creators are already out there that are open
source"; "the UI that have been made on our v1 ... hasn't been very good"); `cr-first-build` overruled ("too small a
first build ... feels like a gamified experience ... designing from the POV of the player"). Rows:
`council/callsheets/rows/calrunia-creator2-2026-10-21.json` (ten `cr2-*` positions, question `cr2-arrival-scene`).

**The scene (player's seat).** Intrinsic pleasure: becoming someone by doing, and a small mystery you carry.
1. Road mist: you walk in as fog; drag settles a body shape, a wide/narrow pull sets build; the fog thins as you choose.
2. The well at the south gate: draw a bucket; the reflection shows you (faceless); eight river stones are skin; a swipe
   on the water changes hair style and colour.
3. The satchel: jacket, wrap dress, long coat, dyed violet or saffron. A tied bundle will not open: the robe, untied at
   the oath at the hollow (A8).
4. The travel paper: Ede writes your name and, if you like, how folk speak of you (default they). This is the passport
   as the player sees it; places stamp it.
5. Through the gate to Tam's farm (A1). "Choose for me" opens every beat; a skip gives a ready traveler.
AQAL: UL the player authors who they are; UR gestures, not forms; LL Ede's welcome and the settlers' topknots read you as
foreign; LR the look is keys in the passport, changeable free, never a cost or gate. Test: time to the gate (<3 min,
skip <30 s), and whether he plays it on his phone without a word about the page.

**Survey (one worker, 2026-10-21).** CharacterStudio (M3-org, MIT, three.js/VRM, active Aug 2026): trait swap, mesh
merge, export; sample asset licences unchecked. Mozilla hackweek-avatar-maker (MPL code, CC-BY-SA models, dormant):
copy its parts convention only. LPC generator (now LiberatedPixelCup org, GPL code, mixed art, active): copy the recipe
JSON and credits export idea, not the code. Quaternius bases/outfits: Quaternius Asset License, not CC0, so reference
only. Kenney Mini Characters CC0 but little to customise. No good free 3D-to-sprite add-on; render ourselves.

## Brief for the next thread (Sonnet, Six-faces-council, clerical, design settled)

1. Land the rows: save the live board with Artifact read, `python3 board/sync_board.py --live <saved> --rows
   council/callsheets/rows/calrunia-creator2-2026-10-21.json --push -m "calrunia-creator2 rows"`, publish
   `board/council-board.html` to https://claude.ai/artifact/DxyShVS8tmvJym4HAsgnho.
2. Publish a short HTML page, "Calrunia Character Creator" (new artifact): the five beats as a storyboard, the survey
   table, the reuse plan, the first build, the rows with the board link. Content is this section and the rows file.
   Run `python3 council/tools/voice_lint.py` on it.
3. Reply to Wendell under 80 words naming the page, the board rows and the one question; no question in the reply.

## His answers, 2026-10-21 17:29 UTC (council/ledger/2026-10-21-pull-172912.json)

`cr2-arrival-scene` C, the Infinite Arcade (a cabinet), not the well. `cr2-first-build` overruled: "I Think I want to
build the web scene in 3d in blender. Have it be like a cutscene for sprout". Read as the arrival scene ("web" for
"well"); if he meant something else, the thread asks on the board. The other nine `cr2-*` positions stand. The row
`cr2-first-build` now carries the revised build below.

## Brief after that (Opus; Blender in bars-engine `tools/blender-cloud`, play in sprout)

Scout: rung 2. We have headless Blender (`tools/blender-cloud`, bpy 5.2.2), the Average Dusk walker, CC0 BlenderKit
fetch, the vendored blender-skills (animation, lighting, rendering) and Sprout's traveler parts. Nothing new to find.

The scene, from the player's seat:
1. **Shot one (Blender, about 8 s, rendered video).** Mist, a corridor of arcade cabinets going on forever, their
   screens glowing; the camera drifts to one cabinet marked for Chapter 1. Its screen shows road mist. Low poly, dusk
   palette; the cabinets are ours (box modelling), any prop from BlenderKit is CC0.
2. **The cabinet screen (Sprout, interactive).** The video holds on its last frame; the creator runs inside the
   screen rectangle, using the existing traveler sprites: mist takes shape (body, build), the screen goes dark and its
   glass is the reflection (skin, hair), the satchel (outfit, dye, the tied bundle). "Choose for me" on every beat,
   skip gives a ready traveler.
3. **Shot two (Blender, about 5 s).** The camera pushes through the screen into light and comes out on the road to the
   south gate.
4. **The travel paper (Sprout).** Ede writes your name and how folk speak of you, then `prototype/ch1-arcade.html`
   opens with the look in the link (`c1w-link-handoff`).

Build: a Blender script in bars-engine `tools/blender-cloud/content/arcade/` (renders both shots, 720p WebM and MP4,
under 3 MB each, plus poster stills and the screen rectangle as JSON); the creator in sprout replacing
`slice/creator.html`/`creator.js`, playing the shots. Proof the cheap way first: a still of the corridor before the
video. Preview: the sprout preview deploy opened on the scene. Then the ship's looking-glass (CharacterStudio refit)
as round 2.
