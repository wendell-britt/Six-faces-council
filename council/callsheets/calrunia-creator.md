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
