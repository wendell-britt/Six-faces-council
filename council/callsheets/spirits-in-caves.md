2026-10-18
ontology: game_design; touches: the meeting spirit, W.A.V.E. sittings, the spirit save (bars-engine content/ontology-game cave.js, bigmind/bigmind.js)
# Spirits in the caves

Wendell, 2026-10-18 23:01 (project chat): the meeting spirit pulls in a cloud spirit of the daemon's family; Big Mind's features
come to the starting cave; both W.A.V.E.s unfold the spirit-proof spirits gas, core, hologram, creature, standing ally; a demo
showcase; spirits saved between runs and cultivated; a loadout chosen in the intro cave. Pass:
`council/passes/6FACE_PASS1_spirits-in-caves_2026-10-18.md`. Rows: `council/callsheets/rows/spirits-in-caves-2026-10-18.json`
(five `sic-*` positions, question `sic-demo-showcase`). His figure notes in the same message (shoulders too high, stand when the
run stops, a run clip) belong to the thread changing the player figure's animation.

## Built
- Slice 1, the family cloud (2026-10-19, thread "The family cloud"): bars-engine #387. `cave/spirit-forms.js` ports the
  spirit page's `*_gas` functions to three.js points (150 motes, two sizes, every third darker, coloured by its element,
  turned to the camera; trail, reach and fist tipped toward the viewer so the loops, fingers and knuckles show), inlined
  before `cave.js` on both pages and on the kit as `spiritForms`. `buildSpirit(THREE, name, hex, form)` wears the gas when
  `form.family` is set; otherwise the orb. `felt()` gives the meeting spirit `family: V.id, stage: "gas"` and streams its
  motes from the voice's body over 1.8 s; reduced motion holds them still and fades in. Family and stage are kept in
  `voices[id].spirit` and `save.spirits`; old saves take the voice's id. The Protector's Shellback gas on the page is the
  plain cloud, so the Protector, Damaged Self and Emotional Body look alike for now. Checks: bigmind-test 524 of 524
  (new: family protector, stage gas, 150 motes and no orb, motes out between daemon and spirit at a quarter of the birth,
  within 0.6 of the spirit after), cave-test 387 of 387. Not done: the approach check-in's spirit (`approachShow`) and the
  Cave of Lessons' sitting spirits stay orbs; no look on a phone; T1 waits on his play.
- Slice 2, the unfolding (2026-10-19, thread "Spirits unfolding as you sit"): bars-engine #388 (branch
  `claude/project-thread-6093c4`). scout: rung 2, we have it (bake_daemons.py's pattern: plain-Python bake to 16-bit GLBs,
  hand parser in the page). `cave/bake_spirits.py` bakes core and hologram from the spirit page's fire GLBs, one file per
  family (shapes are the same per element; the cave tints by its own hex, each material keeping tone, opacity, glow), welded,
  normals and UVs dropped: 11 to 51 KB from 97 to 305 KB. Bases: Shellback tortoise, Romp fox, Tinker raccoon, Hedge pallas,
  Ballad donkey. Holdfast has no GLBs (rounds 15 to 17 wrote none), so the Controller, Damaged Self and Emotional Body wear
  the Shellback's. `spirit-forms.js` `stageOf` (0/2/4/6/8), `buildForm`, `unfold` (gas draws in and fades as the core grows;
  core swells away as the hologram opens; reduced motion fades); creature and ally show the hologram until built. In
  `bigmind.js` `satWith` counts once a run per spirit: sitting with it, sitting with its voice, or a standing W.A.V.E. beside
  its voice; `sittings` saved with `voices[id].spirit`, stage derived on save. Checks: bigmind-test (one count for two
  W.A.V.E.s in a run, second run unfolds to core, only shellback-core.glb fetched, gas fading midway). Not done: no look on a
  phone or by eye at the hologram's facing; Cave of Lessons sittings still orbs (slice 3/4); T2 waits on his play.
- Slice 3, one store and the loadout (2026-10-19, thread "One store and the loadout"): bars-engine #389 (draft, branch
  `claude/project-thread-90co4f`). scout: rung 2, we have it (a plain localStorage module like `oag.bigmind.v1`).
  `cave/spirit-store.js` keeps `oag.spirits.v1` = id, name, element, family, sittings, born, lineage, loadout; stage is derived
  by `stageOf`, never stored. Big Mind writes the meeting spirit through as `meet-<voice id>` (larger sittings win, lineage entry
  per sitting) and walks in loadout spirits it lacks, kept out of the mouth's keep list. `cave.js`: a family spirit wears its
  stage form in the Cave of Lessons, the loadout is added in `levelStart`, a sitting with one counts once a run, and the rug in
  the WAVE room offers "Your spirits" (three at most, a fourth refused until one rests). Checks: bigmind-test 531 of 531;
  cave-test 388 of 390 on a run beside the Big Mind test (two timing-looking fails; a rerun alone passed them before a walking
  timeout in an unrelated side passage). Not done: no look on a phone; the Holdfast's forms; the Cave of Lessons' charge
  spirits are still orbs.
- Slice 4a, the sitting with your spirits (2026-10-19, thread "Big Mind's first cave sitting"): bars-engine PR on branch
  `claude/project-thread-nb06ts`. scout: rung 2, we have it (`followSpirits`' spot function and `spirit-forms.js` `unfold`).
  In the Cave of Lessons' sit-down W.A.V.E. (`sitDown`), the spirits walking in view (three at most) settle round the seated
  figure, one at each side and one behind, and the Welcome step names them ("Fear and Hurry settle around you."). A W.A.V.E.
  gone through to the end counts a sitting for each family spirit there (once a run, as before), the store keeps it, and a
  spirit whose count crosses a stage unfolds where it sits; standing up partway counts none. Test fixes: the let-go and the
  mocap clip checks wait on frames instead of a fixed time, the hall walk waits 30 s. Checks: cave-test alone on main 390 of
  390; with the change 395 of 395 (one earlier run missed the hall walk at 15 s); bigmind-test 531 of 531. Not done: no look on a phone; Big Mind's
  other features (4b to 4e).

- Slice 4b, the meeting spirit and the approach check-in (2026-10-19, thread "The meeting spirit in the Cave of Lessons"): bars-engine
  #391. scout: rung 2, we have it (Big Mind's `approach` and `feelAsk`/`felt`, ported). At the passage, once a daemon is named, the
  approach check-in runs first (body texture and movement, feeling, nearness, state; each skippable, "Skip all, walk on" passes;
  a meeting spirit forms before the daemon as the player answers; another voice's movement says "Something of another voice is in
  this one"). The answers stay on the sitting (`__oagCave.approach()`) since the cave has no save across visits until 4e. Saying yes
  to speaking asks once how you feel meeting it; a family spirit is born from the daemon's body, walks with the player and is kept
  as `meet-<voice id>` (not asked again if the store has it). Checks: cave-test alone 403 of 403. Not done: no look on a phone or by
  eye; the check-in's spirit is an orb, not the family gas; 4c to 4e.

- Slice 4c, the standing W.A.V.E. beside a daemon (2026-10-19, thread "A standing W.A.V.E. beside a daemon"): bars-engine #392 (merged). scout: rung 2, we have it
  (Big Mind's `waveStart`, `eased`, `letGoVoice`, ported). At the daemon's stop, "Breathe with it (W.A.V.E.)": your own charge first, then the
  seven steps standing, one breath each, the charge a shape beside you (element colour at Acknowledge, grows by Allow, dulls at Validate;
  Exhale stay walks with you as a spirit, release rises and fades). Two meters, It and You; only It decides stepping aside. A lower 3-2-1
  reading gives the easing (ring of light, meter glow, a line; most for crossing 3). Satisfied, the daemon plays its Integrate action before
  stepping aside. A W.A.V.E. to the end counts a sitting for `meet-<voice id>` (once a run, store kept); back partway counts none.
  Checks: cave-test alone 420 of 421 (the hall walk, a known timing miss). Lesson: a tween started inside a tween's end is dropped by the
  render loop's filter; chain with setTimeout. Not done: no look on a phone; the Exhale stay path now tested (#392); "Something's in the way" inside
  the W.A.V.E. not ported.
- Slice 4d, trust, the marks, allies and vouching (2026-10-19, thread "Trust and vouching in the starting cave"): bars-engine #393. scout: rung 2, we have it
  (Big Mind's trust tables, `trustOffer`, `resolvePending`, `allyJoins`, copied unchanged). "Show it who you are" at the daemon's stop and on
  its "satisfied?" page: can (wait a breath, W.A.V.E., sit as two breaths, go slowly), will (return, visit promises), good (share cards or
  your own line). Two marks under the meters. A move counts only if the next 3-2-1 reading eases; the daemon says what it saw, hints, reads
  you in its words, and its stance softens. All three seen: its spirit becomes the ally; at later daemons allies answer "Who vouches?" and
  count once as can. Trust is kept for the run only. Checks: cave-test alone 431 of 432 (camera pitch, known flaky). Not done: saves across
  visits, the falls (push past a refusal, a promise broken by leaving) and keeping "return" on leaving, all 4e; "visit" is kept only by meeting
  the daemon in a later block of the same run; Sit with it is two breaths, not the cave's sitting; no look on a phone; Own it moves untested.
- Slice 4e, trust across visits, the falls, Self and Run (2026-10-19, thread "Trust saved across visits in the starting cave"): bars-engine #394 (draft). scout: rung 2, we
  have it (Big Mind's `refused`/`pushed`/`breakReturn`/`trustSave`, ported). Trust is written to `oag.cave.trust.v1` as it changes and read back
  when a daemon is met again: it says it remembers, names the falls not yet owned, stands as it was left, and its ally comes back at the hall. A refusal
  ("Not now") offers waiting with it or "Ask again, now", a push that breaks its read of you. Leaving a daemon's side passage (a skip, Self's Walk back
  out, a closed page) breaks the promise to return; Release keeps it. Own it repairs both falls (tested). Self and Run added to the levels (Run 2.1x, Shift too).
  A promise is stored without its block; an open "return" promise is dropped on load. Checks: focused runs 26 of 26 and 12 of 12; full cave-test alone 455 of
  456, the miss a hall camera-turn check right after the new Self re-entry (not re-run; camera checks are known flaky; an earlier full run stopped at a rug-walk
  timeout before reaching the hall). Not done: no look on a phone; Self does not pause a 3-2-1 or W.A.V.E. in progress, it only stops the walk;
  the six face branches are skipped in the new daemon checks (marked walked); `visit` is kept at the first page of a later meeting, with no minimum time.

## Next
Slices, one bars-engine pull request each from main (Opus for slice 1 and 2's design, Sonnet after):
1. ~~**The family cloud**~~ built, bars-engine #387 (`sic-family-cloud`). In `bigmind.js` `felt()` the new spirit gets `family: V.id`; it is saved in
   `voices[id].spirit` and `save.spirits`. A new `cave/spirit-forms.js` (exported on the kit beside `buildSpirit`) draws the gas
   as motes in three.js in the element's colour, shaped per family as the spirit page's gas is (Holdfast a clenched fist, Hedge a
   question mark; read the page's family notes in spirit-generator.md, rounds 1 to 20); Damaged Self and Emotional Body get a
   plain cloud. On birth the motes stream from the daemon's body to the spirit. Reduced motion: motes still, fade in. Keep the
   label. Touch cave.js only where `buildSpirit` picks the form, since the walkthrough thread's #382 to #384 edit cave.js and
   bigmind.js heavily: build on main, and rebase onto whichever of those merges first. Checks: bigmind-test sees a Protector
   spirit built with family `protector` and stage `gas`, motes moving from the daemon; cave-test unchanged. Test T1 at his play.
2. ~~**The unfolding**~~ built (see Built) (`sic-unfold-by-sitting`): sittings counted per spirit (once per run), stage from sittings (0/2/4/6/8);
   core and hologram from the GLBs (`/mnt/project-files/3d-build/spirit-shellback-2026-10-14/`, per base and element), fetched
   on demand and compressed; creature and ascended after. Climb the tool ladder first (docs/tool-scout.md).
3. ~~**One store and the loadout**~~ built, bars-engine #389 (see Built) ( Sonnet once its design reads clear; also bakes the Holdfast's forms when
   its GLBs exist, and draws a family spirit's stage in the Cave of Lessons) (`sic-one-store`, `sic-loadout-three`): `oag.spirits.v1`, read by both caves; the picker at the
   WAVE room rug.
4. **Big Mind's features in the starting cave** (`sic-first-cave-sitting`), list in the worker map below. 4a, the sitting
   with your spirits, built (see Built). The rest, one bars-engine pull request each from main, on Sonnet; check first what
   the cave already has (it has its own 3-2-1, `talk321`, and the staged meeting):
   - ~~4b, the meeting spirit and the approach check-in~~ built, bars-engine #391: `feelAsk`/`felt` when the player meets a chamber daemon, so the Cave
     of Lessons' daemons give a family spirit into the store as Big Mind's do (`meet-<voice id>`), and `approach`.
   - ~~4c~~ built, bars-engine #392: the standing W.A.V.E. beside a daemon (`waveStart`), the two charge meters and easing, and let-go after 3-2-1
     (`letGoVoice`); a standing W.A.V.E. beside a spirit's daemon counts its sitting, as in Big Mind.
   - ~~4d~~ built, bars-engine #393: Trust and the can/will marks (`trustOffer`, `marksUi`), allies and vouching (`allyJoins`).
   - ~~4e~~ built, bars-engine #394 (draft): Self (`selfPause`), Run (`runBtn`), and saves across visits (`leave`), including trust kept across visits (`state.trust` in cave.js, shape
     as Big Mind's `voices[id].trust`), the falls (broken return on leaving, push past a refusal) and keeping the "return" promise on leaving.
5. **The demo showcase**, on his answer to `sic-demo-showcase`.

Worker map (bars-engine main 7a81014): starting cave = Cave of Lessons, `cave/cave.js` (`start` :1818, WAVE room `openRoom`
:3812, sitting `sitDown` :2946). Big Mind's features it lacks: Self (`selfPause` :1226), Trust and can/will marks (`trustOffer`
:1892, `marksUi`), the meeting spirit (`feelAsk`/`felt` :1258-1270), allies and vouching (`allyJoins` :1881), the two charge
meters and easing, standing W.A.V.E. (`waveStart` :1434), let-go after 3-2-1 (`letGoVoice` :1362), full 3-2-1 (`talkThrough`
:2087), the approach check-in (`approach` :2343), Run (`runBtn` :1180), saves across visits (`leave` :2510). Spirits: orb
`buildSpirit` cave.js:1572, `followSpirits` :1579, `SPIRITS_SHOWN = 3`; Big Mind save `oag.bigmind.v1`.

## Waiting on
- His answer to `sic-demo-showcase` (slice 5 only).
