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

## Arcade arrival, built (2026-10-21, thread "Arcade arrival cutscene")

bars-engine #416 (`tools/blender-cloud/content/arcade/arrival.py`, `encode.sh`) renders the two shots (Cycles on CPU,
46 min; shot1.mp4 430 KB, shot2.mp4 165 KB). sprout #70 replaces `slice/creator.*` with the scene, adds a dye option
to `runtime/traveler.js` and a look reader in `ch1-arcade.html`. Preview (Vercel login):
https://sprout-git-claude-project-thr-1570af-wendells-projects-9c1b16dc.vercel.app/creator.html (built slice serves the
scene at `/creator.html`, Chapter 1 at `/ch1/`; `?beat=reflection` jumps). Stills: /mnt/project-files/arcade-arrival/.
Checked in Playwright at phone and desktop sizes. Not checked: a real phone, Safari MP4, three halfway skin blends
(fawn, chestnut, umber) by eye; the Chapter 1 cabinet does not stand out enough at the start of shot one.

TRIGGER: his look at the preview. Notes -> fresh Opus thread owning #416 and #70 on branch
`claude/project-thread-u7hkk7`. Next after that (position, stands from the look contract above and
`c1w-link-handoff`): bars-engine writes the look from the Chapter 1 link into the guest passport (`look` in
`schema/passport.schema.json`, fixtures, contract tests).

## Arcade arrival, round 2 (2026-10-21, thread "Arcade arrival round 2")

His notes on round 1: work through a 3D character that becomes the 2D sprite, or a fork where the player picks sprite or
3D, the character's information the same either way ("I'm still testing which approach I like best"); space between the
arcade consoles and varied heights; he loved the grey gate, and NPC guide models should extend from there.

Built: sprout #71 (supersedes #70) and bars-engine #420 (supersedes #416, closed). The first beat in the Chapter 1 screen
is the fork: Sprite or Figure (3D) (Average Dusk from J5, three.js, `slice/figure.js`), a switch on every beat, and
Bake to pixels (the figure drawn at sprite size). The look string is unchanged; the form travels beside it as `&form=`
and `&bake=1` and `sprout.form`. The arcade re-rendered with 0.45 m gaps, back walls and six cabinet heights.
Preview (Vercel login): https://sprout-git-claude-project-thr-7fd764-wendells-projects-9c1b16dc.vercel.app/creator.html?beat=form
Stills: /mnt/project-files/arcade-arrival/round2/.

Not done: the figure's outfit cut (jacket, wrap dress, long coat all wear the robe; only the dye follows); the figure is
small on a phone (the whole frame is); not checked on a real phone or Safari.

TRIGGER: his look at the round 2 preview. Notes -> fresh Opus thread owning sprout #71 and bars-engine #420 on branch
`claude/project-thread-3ag8x2`. Next after the fork settles: NPC guide models from the grey gate (his ask), then the
outfit cuts on the figure if he keeps the 3D path.

## Arcade arrival, round 3 brief (2026-10-21 21:50 UTC, his notes on round 2)

His words: "the height change needs to also have screen shapes to match the new heights. Feel free to do some research on
how arcade cabinets differ from each other and how their screens change. We also need to improve the button and joystick.
On top of that when a player chooses the 3d version that model should be seen walking through the gate that they are
headed through in the mist. I think we also need to start figuring out how to render the different robes in 3d. I think
we've already done this work so look that up."

Owns sprout #71 and bars-engine #420, branch `claude/project-thread-3ag8x2` in both. Opus.
1. Scout first: one worker on real cabinet types (upright, cocktail, candy/Japanese, sit-down, cabaret/mini) and their
   screen shapes (4:3 landscape, 3:4 portrait/vertical shooters, widescreen later); then in `arrival.py` give each
   height a cabinet type with its own screen aspect, marquee and bezel. Chapter 1 cabinet stays as is (screen-rect).
2. Controls in `arrival.py`: a real joystick (ball-top on a shaft, base plate) and round buttons in a row, per type.
3. Figure path: when `form=figure`, the 3D figure walks the misty road through the grey gate (shot two). Cheapest
   first: three.js overlay of `slice/figure.js` walking over the shot-two video/poster with the camera matched to
   `shot2_pose`, before any Blender re-render with the figure in it.
4. Robes in 3D: the J5 robe work exists (callsheet j5 / `/mnt/project-files/3d-build/j5-*`, robe/sash/topknot GLBs in
   `j5-garments-2026-10-13`, cloth rounds to r13b, bars-engine #365/#364/#315). Map jacket, wrap dress and long coat
   onto it in `figure.js`; send the reading to a worker.
Re-render runs in the background (about 40 min, bpy==5.2.2 into /home/user/blenv, see tools/blender-cloud/README.md).
sprout `*.glb` is in Git LFS and cloud sessions cannot push LFS: name models `.glb.bin`. Hand off at 150k.
3D math (2026-10-21, `docs/3d-math.md`): before the next mocap or sleeve round, try the cheap fixes first: quaternion
BVH import, a per-bone roll check, and half the wrist twist on the lower forearm; frame the figure with `frameSphere`.

Robe clipping fix (2026-10-22, sprout #72, stacked on #71, branch `claude/project-thread-8zq73n`): the legs are hidden
under each cut's covered band, and the baked robe rides on thigh and shin capsules (docs/3d-math.md rule 8). Probe:
`tools/figure-legs-probe.mjs`. Left open: the coat's side slits show the robe's inside where the masked leg would be
(1 to 2 % of masked points), not judged at full size.

### Sleeve research run (next, any environment; board row `rc-sleeve-research`)

Wendell, 2026-10-22, after the leg fix: "ok its perfect. We still have some work to do on the sleeves... Let's do a best
practice research run on how to render the sleeve style we're looking for."

1. Research, through one worker search, how games and film render wide hanging (hanfu-style) sleeves. Cover hiding the
   forearm and hand inside the sleeve (masking, as rule 8 does for the legs), sleeve bones or arm-driven skinning compared
   with cloth, arm capsules sized to the sleeve's outer layer, cuffs that keep their shape, the wrist twist split
   (docs/3d-math.md rule 3), and how studios test for poke-through.
2. Write a short plain answer page (HTML Artifact): what the pros do, what we have now in the creator (the baked robe,
   arm capsules in `slice/figure-robe.js`, `armShare`), and what is missing.
3. Make the cheapest change the research points to in sprout (`slice/figure.js`, `slice/figure-robe.js`, branch off
   `claude/project-thread-8zq73n` / #72). Prove it with a probe like `tools/figure-legs-probe.mjs`, cast from the arm
   points, and give a one-click preview at `?beat=satchel&form=figure`.
4. Tell the "J5 sleeve round 15b" thread the approach, and add any garment rule to docs/3d-math.md.
