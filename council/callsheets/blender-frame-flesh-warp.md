# Blender: frame, flesh, warp (parametric creatures and NPCs)

## Next
- Source: a tweet Wendell shared 2026-10-14 (skeleton first, then flesh, then warp; headless Blender practice). Its numbers (benchmark scores, who built it) are unverified; the practice is sound on its own and was checked against our scripts.
- Ruling (Wendell, 2026-10-14 22:15, overruling the first draft): "Overrule the rigging spirit skeletons first. What it buys is a good operational foundation and we ARE going to be using the rigs in the cave forms of these sprites emerging." Spirits are rigged skeleton first, and the rigs go into the cave forms.
- Position (stands unless he flips it): one frame, flesh, warp recipe for both strands. The NPC generator for the Chapter 1 demo builds on the humanoid rig we already have, with the warp as a numbers table applied last. The spirits get the same treatment, starting with the Shellback families, whose rig is built before any further look rounds.
- Build, in a fresh thread on Opus, in bars-engine (not on #318's branch, which round 8 is using):
  0. Spirit rig first: a per-family frame (joint table, parent map, weights, one Walk and one Idle), the fused flesh skinned to it, the existing element, nation and base layers as the warp. Not on #318's branch while round 8 runs; it lands as its own module that #318 later imports. The cave forms use these rigs, so the sprite is rendered from the rigged model posed at its sprite angle.
  1. `content/ontology-game/cave/census.py`: loads any GLB, asserts the mesh census (non-manifold edges, loose verts, degenerate faces, size within a stated box). Humanoid figures must pass it; kit-bashed spirits and the chamber only report.
  2. A `WARP` table beside `BUILDS` in `cave/character.py` (limb ratio, head size, spine curve, stoop, one joint collapsed), each row named for a blockage, applied after the fused body and before the weights are painted. The blockage list comes from the ontology; ask the board (`reach_test` first) only if the record cannot map a blockage to a row.
  3. A 12-figure sheet from one frame, each figure one number away, to look at before anything else.

## Built (2026-10-14, bars-engine #325)
- Item 0, the spirit rig: `tools/blender-cloud/content/spirits/rig.py`. A joint table per base and stage (tortoise,
  armadillo, pangolin, fox; creature on four legs, ally form on two, gas, core and hologram on one float bone), the
  cave avatar's joint names, the fused body, cloth and tail weighted per vertex, every other piece on the bone it sits
  on, the aura on the root, Walk (one second) and Idle (two seconds). rig_scene(base, stage) is what shellback.py calls
  before export once #318 lands; until then it rigs an exported GLB. Sheets and four rigged GLBs:
  /mnt/project-files/3d-build/spirit-rig-2026-10-14/.
- Scale declared (`SIZE` in rig.py) and baked in, 1 unit = 1 m: tortoise creature 1.2 m long, armadillo 1.0, pangolin
  0.9, fox 0.75 nose to rump; ally forms 1.4 to 1.5 m tall; gas, core and hologram at their creature's scale.
- Item 1, the census: `content/ontology-game/cave/census.py`, plain Python. J4, J5 and the body map figure pass (closed,
  0 degenerate); spirits and the chamber report. Tests C1 (offline) and S1 (bpy, skips until shellback.py is on main).
- Position (stands unless he flips it): the WARP rows in item 2 are named for the seven daemons (Controller, Damaged
  Self, Emotional Body, Fixer, Protector, Skeptic, Victim), since the record already maps a blockage to a daemon and a
  daemon to a spirit family (sg-body-from, ch1-npc-from-blockage). No board question needed.

## Built (2026-10-14, bars-engine #328): items 2 and 3
- Item 2, the warp: `WARP` beside `BUILDS` in `content/ontology-game/cave/character.py`, one row per daemon (protector,
  controller, skeptic, fixer, victim, damaged-self, emotional-body). Five numbers per row: `arms` (arm length; legs stay,
  so height and stride stay), `head`, `curve` (upper back rounds forward, minus arches), `stoop` (lean from the waist),
  `collapse` (one joint held in its natural bend). Applied after the fused body and before the weights, so rig,
  weights and walk follow it; bands are painted at rest positions. Row numbers are first choices read from each
  daemon's "in you" line in `council/daemons/daemons.yaml`.
- Item 3, the sheet: `--one-number --sheet` (frame plus eleven figures, each one number off) and `--daemons --sheet`
  (frame plus the seven rows), front three-quarter and side. Files: /mnt/project-files/3d-build/npc-warp-2026-10-14/
  (`one-number.png`, `one-number-side.png`, `daemons.png`, `daemons-side.png`, the eight GLBs, `checks.txt`).
- An eighth row, `player` (the vulnerable child: big head, short arms, nothing bent), and `npc.boss` on the report
  row: the NPC's answer to its boss question (daemons/questions.js, bars-engine #329), with `npc.next` the figure the
  player meets next (`self` is the unwarped frame). `--boss` sets it.
- All twenty figures pass `census.py --kind humanoid` and J4's walk check; test J6 asserts it for the daemon set.

## Next
- His look at the two sheets. Then: the warp reads the player's charge (which daemon holds the blockage) to make the
  Chapter 1 NPC, and the J5 garments are checked on a warped body (the robe is skinned to the same rig).

## Round 2 of the warp, the gestural language (done 2026-10-14)
- His look (Wendell, 2026-10-14 23:35): "my notes for the daemon poses is they need to be more dramatic and different
  from each other. They are quite subtle nods but if you want to create a gestural language we might want to use the
  building blocks of the Six Fundamental Movements of contacting as a starting point with the context that the daemons
  emerge as a way to protect the vulnerable child through egos development until they need to be renegotiated with and
  integrated for the child to move into adulthood. This is essentially one of the things we are gamifying."
- Built on bars-engine #328: every WARP row carries a `gesture`, per-joint rest rotations (flex, out, turn, mirrored by
  side), feet set back on the ground. Movement per daemon and the source are in `council/daemons/GESTURES.md`; board row
  `dg-six-movements` holds the position. Census gets an `npc` box (arms flung to 1.5 m, Fixer 1.2 m deep, Victim sunk to
  1.4 m tall); the walk check measures the swing from the rest stance. J4, J4b, J6 and the offline tier pass.
- Sheets: /mnt/project-files/3d-build/npc-gesture-2026-10-14/ (daemons.png, daemons-side.png, one-number.png,
  one-number-side.png).

## Round 3, the hands (done 2026-10-16)
- His looks, 2026-10-16: "Better but controller still looks weird and the hands are still off. Let's do some research on
  how to properly rig and use hands"; then "Problem areas" (a crumpled stop wrist, torn finger webbing); then "Close to
  perfection. The wrist joints for the protector are still a little weird"; then "Perfect. Let's do the next thing".
- Built on bars-engine #328: 15 finger bones per hand (46 bones in all), one open mesh, and `HAND_POSES` open, relaxed
  and fist as curls and a spread; the hand and the body never share a vertex; the wrist is a ball on the joint. The
  Controller sets its fists on its hips. Research in `council/daemons/HANDS.md`. All rig tests pass, every figure under
  300 KB. Sheets in /mnt/project-files/3d-build/npc-gesture-2026-10-14/.

## Next thread (Opus, fresh): integration, the held movement completing
- His look is in ("Perfect", 2026-10-16). Animate each daemon's movement completing over a few seconds, from its held
  shape to the Player's open stance (a push that lands, a grasp that lets go), as a second action beside Walk. Start
  with the Controller: its fists open (fist to relaxed on the finger bones) as the arms come off the hips. The walk keys
  no finger bones, so the action may key them.
- Owns bars-engine #328 (and watches #325) until they merge.

## Round 4, integration: the Controller lets go (built 2026-10-16, bars-engine #351)
- `character.py --warp controller --integrate` adds a second action, Integrate, beside Walk: half a second held, three
  seconds of the move, half a second still. Elbows swing in first so the fists clear the hips outward, the shoulders
  follow, the fists open finger by finger (thumb last), chest and chin settle into the Player's stance (`INTEGRATE_TO`:
  the Player's gesture, curve and stoop, relaxed hands; the daemon keeps its own proportions). Timing per joint is the
  `INTEGRATE` row. Skin weights now reuse the pre-warp blend so a fist opens without tearing. Test J7.
- #325 and #328 merged 2026-10-16. Renders: /mnt/project-files/3d-build/npc-integrate-2026-10-16/. 3D view:
  https://claude.ai/artifact/515E62dAHmCaVffBw7EDSm
- His look at round 1 (2026-10-16): "Let the controller hands fall to their sides in a slightly more relaxed posture
  at the end". Round 2 (bars-engine #352): the `controller` INTEGRATE row now carries its own `"to"`, merged over
  `INTEGRATE_TO` (shoulder flex 0.06 out 0.0, elbow 0.18, wrist 0, neck 0.02, curve and stoop 0.03), so the arms end
  hanging close at the sides. J7 passes, 298 KB. 3D page republished as version 2; renders in
  /mnt/project-files/3d-build/npc-integrate-2026-10-16/round2-relaxed/. Board step `controller-letgo-look-02`
  (list blender-cloud-test, step 17). Other daemons whose open stance should not be the Player's can use `"to"` too.
- Next, after his look at the Controller: one `INTEGRATE` row per daemon (Protector's push landing, Skeptic's pull
  returning, Fixer's reach arriving, Victim rising from the yield, Damaged Self's release, Emotional Body gathering
  back), in a fresh thread, one round each or all six on one sheet; then the cave plays Integrate when the player's
  move completes the daemon's movement. On a "no", tune the Controller from his note first.

## What we already follow
- Version pinned: `bpy==5.2.2` on Python 3.13 (tools/blender-cloud/README.md). Matches the tweet's current LTS.
- Scale convention: GLB exports 1 unit = 1 m; characters are 1.75 m. Cameras and dims in the cave scripts agree.
- Frame, then flesh: `cave/character.py` starts from the body map's parts with a joint table (`J`), a parent map, fuses the surface, then weights each vertex by nearest part. That is frame and flesh. `BUILDS` is a small warp (three widths).
- Parametric and seeded: `procgen.py` has same seed, same mesh asserts (roots, mushrooms). `character.py` checks the walk's joints per figure.
- Render for a contact sheet, judge by eye: `LOOKED.md`, the sheets in every thread. Cycles on CPU because the cloud has no GPU (the tweet's offscreen EEVEE route needs one).

## Which would fix problems we have had
- Census on outputs. Ran trimesh over exports on 2026-10-14 (vertices merged): the J4 figure is clean (0 non-manifold edges, a volume, 4 degenerate faces). The spirits are 130 to 190 separate parts and 7,000 to 9,000 non-manifold edges each, and the generated chamber GLB has 19,000 and 438 degenerate faces. For sprites that is fine; for a 3D game, solid-looking pieces that are open shells will break any boolean, physics collider or print. Nothing asserts any of it today.
- Scale declared once. The spirits export at about 4 m long (tortoise creature 3.9 m) because they were framed for a sprite camera, and nothing says so. A 3D game would meet them at four times a person.
- Warp as numbers. Spirit variants today are 3 bases by flags and module globals (`SHELL_SQUASH`, `HEAD`, `NECK`) and one process per base. The parametric NPC need is the same shape as the humanoid.
- `--python-exit-code 1`: our scripts run under the bpy wheel, so a traceback already fails the run. It matters only if a build ever shells out to the Blender binary.

## Which do not fit
- (Withdrawn by his ruling: not rigging the spirits first.)
- Banning `bpy.ops` outright. Our metaball bodies (`blob`, `shellback.py`) convert through `bpy.ops.object.convert`, and 68 calls work headless on 5.2.2. Move to bmesh only where a run fails or a mesh needs measuring.
- Printing numbers (overhang, hole size, wall). Not printing anything.
- The Blender MCP servers. We run scripts in a pinned venv; the tweet's own warning about unguarded code applies.
- EXACT booleans, `gpu.init()` offscreen sheets: no booleans in these scripts, and Cycles CPU works.

## Built (2026-10-16, bars-engine #353): the bodies in the cave
- `content/ontology-game/cave/bake_daemons.py` (plain Python) bakes `character.py --daemons` into one GLB per daemon
  and the Player: 16-bit positions, 8-bit normals, a robe band per vertex, 88-89 KB and 6,328 triangles each (budget
  96 KB, 7,000). Static held pose only; the rig and the Integrate action are not played in the cave yet.
- `cave.js` fetches a body the first time a scene asks for that daemon and swaps it in for the stand-in (Big Mind
  chambers and the Cave of Lessons' daemon stops alike); the robe takes the daemon's colour. `dressCave` dresses the Big
  Mind tube from the cave kit. Renders: /mnt/project-files/3d-build/daemon-bodies-2026-10-16/.
- Rebake after any `character.py` change to a rest shape: `character.py --daemons --out X`, then `bake_daemons.py X
  content/ontology-game/cave/daemons`.
- #353 merged 2026-10-16. Next for this art line, one fresh Opus thread once bars-engine #355 (trust) merges: skin the
  baked bodies (joints and weights in `bake_daemons.py`, a small skinning path in `cave.js`) and pose each chamber
  voice by `voice.userData.stance` from #355 (`window.__oagBigMind.STANCES`: guarded, testing, softening, trusting,
  willing, hurt, repaired, each a variation on its held movement in GESTURES.md). The same skinning carries the
  Integrate action (#351) into the cave once his look approves it. #355 already rewrote the arrival lines.

## Built (2026-10-16, bars-engine #356): skinned bodies, trust stances, honored ends, a let-go for all seven
- The baked bodies are skinned (46 joints, two a vertex) and pose themselves from `voice.userData.stance`
  (`cave.js` `BODY_STANCES`). His look at the first stances: "many of the daemons are too subtle in their changes. We
  need them to be more exaggerated so it's obvious when shifts are happening. They need to end not in a neutral pose but
  essentially in the honored version of their pose empowered and healthy versus resistant and charged. How would these
  voices relate to a healthy inner child". So each body moves between two ends: **charged** (the WARP row times 1.4;
  guarded, testing, hurt) and **honored** (`character.py` `HONORED`; softening, trusting, willing, repaired). The honored
  forms are a position that stands unless he flips it; GESTURES.md has the table.
- His next note, "we need 'let go' stances for all the daemons", is the yes on `controller-letgo-look-02`: every daemon
  now has an `INTEGRATE` row ending in its honored form (the Controller's too, replacing the relaxed arms of #352), baked
  into the bodies. `integrateBody(g)` plays it; no scene calls it yet.
- 3D page (all eight, every stance, a Let go button): https://claude.ai/artifact/FE5zEcpm99qdYXB1aCxwuK
- Next: (1) his look at the honored forms and the let-go on that page; (2) the Big Mind build that decides when the cave
  plays the let-go (the player's move completing the daemon's movement) calls `integrateBody` and sets a stance that
  stays honored; (3) backlog, not now: props for each daemon that show the nature of its job (Wendell, 2026-10-16: "We
  will eventually need props and such for them as well to really hit home the nature of their jobs").

## His look (2026-10-17 01:45 UTC)
- Approved: "the let gos are where I want them to be." #356 and council #228 merge on it.

## Done: council pass on meeting a daemon (2026-10-17)
Pass `council/passes/6FACE_PASS_daemon-meeting1_2026-10-17.md`, ledger `2026-10-17-daemon-meeting1.json`, rows
`council/callsheets/rows/daemon-meeting-2026-10-17.json`. Nine `dmt-*` positions on the board, question `dmt-trainer`.
The build (approach check-in) is Big Mind build 4, owned by `council/callsheets/big-mind-cave.md`; the flooded squint
rides the spirit loop's next round (`spirit-generator.md`). The brief, kept for the record:

### The brief
His words, 2026-10-17: "The next thing we need to do is be able to have players as they get closer to the daemon to answer questions about how their body is responding to knowing they are going to meet a protector what kind of emotions are present and are the flooded veils satisfied or dissatisfied. I want to see how much of the spirit asset work we can use to break this down. I don't know if the daemons are pokemon trainers have have their own spirits that you can battle. OR IF the boss spirit becomes a daemon of the variety of our daemon ontology. Let's have the 6 game masters weigh in on this and specifically have the daemons self advocate for this. I think the victim at the storyteller level and as the sage should lead the charge"
- A six-faces pass (`.claude/skills/six-faces/SKILL.md`, design-ontology loaded for a mechanic). The Victim at its honored storyteller level leads, speaking with the Sage. Every daemon advocates for itself through its own agent (daemon-*).
- Questions for the pass: (1) the approach check-in: as the player walks toward a daemon, what the body is doing, which emotions are present, and whether the flooded and veiled states are satisfied or dissatisfied; (2) how the spirit assets (spirit-generator callsheet, the Holdfast and other families with their states) break this down; (3) whether daemons keep spirits the player can battle, like trainers, or whether a boss spirit becomes a daemon of the daemon ontology, or both.
- Inputs: council/daemons/GESTURES.md (honored and charged forms), council/daemons/questions.yaml, council/callsheets/big-mind-cave.md, council/callsheets/spirit-generator.md, bars-engine bigmind.js STANCES.
- What survives the reach test goes to the board; the rest stands as positions.
- Backlog: props for each daemon's job.
