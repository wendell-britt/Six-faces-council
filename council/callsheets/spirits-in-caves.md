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
- Nothing yet.

## Next
Slices, one bars-engine pull request each from main (Opus for slice 1 and 2's design, Sonnet after):
1. **The family cloud** (`sic-family-cloud`). In `bigmind.js` `felt()` the new spirit gets `family: V.id`; it is saved in
   `voices[id].spirit` and `save.spirits`. A new `cave/spirit-forms.js` (exported on the kit beside `buildSpirit`) draws the gas
   as motes in three.js in the element's colour, shaped per family as the spirit page's gas is (Holdfast a clenched fist, Hedge a
   question mark; read the page's family notes in spirit-generator.md, rounds 1 to 20); Damaged Self and Emotional Body get a
   plain cloud. On birth the motes stream from the daemon's body to the spirit. Reduced motion: motes still, fade in. Keep the
   label. Touch cave.js only where `buildSpirit` picks the form, since the walkthrough thread's #382 to #384 edit cave.js and
   bigmind.js heavily: build on main, and rebase onto whichever of those merges first. Checks: bigmind-test sees a Protector
   spirit built with family `protector` and stage `gas`, motes moving from the daemon; cave-test unchanged. Test T1 at his play.
2. **The unfolding** (`sic-unfold-by-sitting`): sittings counted per spirit (once per run), stage from sittings (0/2/4/6/8);
   core and hologram from the GLBs (`/mnt/project-files/3d-build/spirit-shellback-2026-10-14/`, per base and element), fetched
   on demand and compressed; creature and ascended after. Climb the tool ladder first (docs/tool-scout.md).
3. **One store and the loadout** (`sic-one-store`, `sic-loadout-three`): `oag.spirits.v1`, read by both caves; the picker at the
   WAVE room rug.
4. **Big Mind's features in the starting cave** (`sic-first-cave-sitting`), list in the worker map below.
5. **The demo showcase**, on his answer to `sic-demo-showcase`.

Worker map (bars-engine main 7a81014): starting cave = Cave of Lessons, `cave/cave.js` (`start` :1818, WAVE room `openRoom`
:3812, sitting `sitDown` :2946). Big Mind's features it lacks: Self (`selfPause` :1226), Trust and can/will marks (`trustOffer`
:1892, `marksUi`), the meeting spirit (`feelAsk`/`felt` :1258-1270), allies and vouching (`allyJoins` :1881), the two charge
meters and easing, standing W.A.V.E. (`waveStart` :1434), let-go after 3-2-1 (`letGoVoice` :1362), full 3-2-1 (`talkThrough`
:2087), the approach check-in (`approach` :2343), Run (`runBtn` :1180), saves across visits (`leave` :2510). Spirits: orb
`buildSpirit` cave.js:1572, `followSpirits` :1579, `SPIRITS_SHOWN = 3`; Big Mind save `oag.bigmind.v1`.

## Waiting on
- His answer to `sic-demo-showcase` (slice 5 only).
