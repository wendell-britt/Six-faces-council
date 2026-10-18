# Six faces, pass 1 on where the Between lives (2026-10-17)

**Called by:** Wendell, in the thread "Fix the 3D garden on iPhone", 2026-10-17 00:26 UTC.

**The question, in his words:** "Ok let's take a step back. We're being quite silly about this. It's still not working
which leads me to believe we're trying to brute force and hack a solution instead of taking a step back and
troubleshooting. Let's get the 6 game masters on this specifically why aren't your tests translating to my environment
and if we're chasing something we're going to need to change and remove anyway. This will ultimately be hosted on the
web so let's sure we're being coherent about that mantras of trying to fix the artifact tool. Also the WAVE and CAVES
are all working on bars-engine"

**Pass:** first on hosting. It follows the relationship creature pass (`6FACE_PASS_relationship-creature1_2026-10-16.md`)
and the ontology read for the 3D build (`BETWEEN_3D_ontology_2026-10-16.md`).

**Casts** (three coins, `cast.py --json`, kept in the ledger record):

| Face | Hexagram | Shows | Becomes |
|---|---|---|---|
| Shaman | 3 Sprouting | This is early, and you are reading the mess as a verdict. | 48 |
| Architect | 59 Dispersal | What you were holding rigid is coming apart. | 8 |
| Challenger | 24 Turning | What came back is one line deep. | 4 |
| Regent | 16 Anticipation | The good part has started and the event has not. | 24 |
| Diplomat | 30 Burning | You keep saying the same true sentence, and it is consuming its subject. | none |
| Sage | 38 Estrangement | You reached a conclusion from a distance. | none |

No daemons were sent. The evidence is this thread's own record and two repos' files.

## Scorecard

The relationship creature pass set tests T2 (paper play by 2026-10-30) and T3 (source read by 2026-10-23). Neither is
due. The 3D build's done line, "two-viewer test ... phone width, his link in the reply; then his play", is graded here:
**failed**. The phone-width check ran in desktop Chromium at 390 pixels wide. His play never started because the page
never opened on his phone.

## Anchor

A 3D space where two people tend the Between together, alone or at once, with their spirits and daemons walking in it
(callsheet `council/callsheets/relationship-creature.md`, build brief "the Between in 3D"). Wendell, today: it "will
ultimately be hosted on the web".

## What happened, in order

1. Version 1 (the 23:45 build) showed "The garden did not load" on his iPhone in the Claude app.
2. Patch 1 changed how textures load, because three.js treats the app's web view as non-Safari. Tested in desktop
   Chromium with an iPhone user-agent string. Still failed on his phone.
3. Patch 2 put the cave inside the page, added timeouts and a progress line. Tested with a fake store. It reached
   "reading your place in the garden" on his phone and stopped. That step is the artifact platform's own store call
   (`db.doc(...).get()`), which never answered.
4. Patch 3 gave that call an 8-second limit. Still not working on his phone, at a step we have not seen.

## Shaman · 3 Sprouting

*This is early, and you are reading the mess as a verdict.* The garden is a day old. Three failed patches read like a
verdict on the Between, and the Between hasn't been played yet.

**The felt sense underneath is shame-speed.** Each patch went out fast so he would have something by morning. Each
failure cost him a reopen, a wait and a screenshot, and made him the test rig. That is the cost he named as "brute
force".

**Ari is the person to protect.** The Between is for two people. If the first time Ari is invited the page hangs on a
loading screen, the relationship's first shared act is a broken invitation. The garden should not be shared until it
opens on both their phones.

**Recommendation:** stop sending him patches to try. The next link he gets is one that has already opened on an iPhone.

## Architect · 59 Dispersal

*What you were holding rigid is coming apart.* The rigid part was the hosting choice, made as a default and never
tested on the device that matters.

**Why the artifact was chosen.** The build brief's position (callsheet, "Default route") gave four reasons: an artifact
gives both people one link, sign-in, a shared store and live presence, and bars-engine had no live two-player channel.
It said to port into bars-engine later if the space earned it. Every one of those reasons is now either false on his phone or not needed:

- **The shared store** is the call that hung (patch 2's progress line). We cannot see inside it, and we cannot fix it.
- **Live presence** was never required by a ruling. `rc-tend-alone` and the brief's own rulings make tending
  asynchronous: "nothing changes the Between without the other's yes; async tending". Seeing each other walk is a
  pleasure, not the mechanic.
- **One link and sign-in:** bars-engine already has both. The Nonprofit Board runs at
  https://bars-engine.vercel.app/board behind his sign-in and saves to Postgres (this repo's CLAUDE.md).

**What bars-engine already holds.** WAVE and the caves run there (his words). The cave code is
`content/ontology-game/cave/cave.js` with `openRoom`, served under `/ontology-game/`. The Big Mind cave plays at
https://bars-engine.vercel.app/ontology-game/big-mind. The Between's page is one three.js file that borrowed the WAVE
cave's dome model. Moving it means giving it a page route, a Postgres table in the garden's store shape (garden, items,
spirits, daemons, shown), and an API route like `POST /api/board/saves`.

**Is the binary false?** The fork looked like "fix the artifact or abandon it". The third position: keep the artifact
page as the reference design and move the code to bars-engine, where we control the store and can test it on the
device. The rendering code (cave, walkers, garden, sheets) carries over almost whole. Only the boot and the store calls
change.

**Live presence later.** Polling the garden every few seconds gives "they are here now" without a realtime service.
Add one only if play shows polling isn't enough.

## Challenger · 24 Turning

*What came back is one line deep.* The return is shallow: one line of progress text per round, from his phone, by
screenshot.

**Why the tests didn't translate.** They tested a different machine at every layer that failed:

| Layer | What the tests ran | What his phone runs |
|---|---|---|
| Browser engine | Chromium (desktop, headless) | WebKit, inside the Claude iOS app |
| Host page | A local web server | claude.ai's artifact frame inside the app |
| Store | A fake `window.claude` written by the same session | The real artifact store bridge |
| Errors | Console visible to the session | No console; one grey line by screenshot |

Every test passed because it tested our own assumptions. The fake store answered because we wrote it to answer.
Changing the user-agent string doesn't turn Chromium into WebKit. This container has no WebKit (only Chromium is
installed, and the environment forbids downloading browsers), and it cannot open the iOS app.

**What is self-inflicted.** Three patches shipped against a hypothesis instead of an observation. Patch 1 guessed at
textures. The progress line in patch 2 was the first instrument, and it came in round two. It should have come first.

**The scheduling truth is that the plumbing we patched (the store bridge, the capability timeouts, the inline cave in the
page) is exactly what a move to the web deletes.** Every hour spent on it is spent on code with no future.

**Anti-pattern:** patch, publish, ask him to reopen. The cure is to observe before changing anything, and on the
device that fails.

**Falsification test (unlocks the move):** before building the web version, open the existing bars-engine page
https://bars-engine.vercel.app/ontology-game/big-mind on his iPhone. If it loads, the phone and three.js are fine, and
the fault is in the artifact host. That settles the move. If it fails too, the fault is three.js on his phone, and the
move alone won't fix it. He says the caves work, which reads as a pass already. The test stays so the claim is checked
on the phone, the device that failed.

## Regent · 16 Anticipation

*The good part has started and the event has not.* The design is settled and ratified (`rc-*` rows), and the play has
not happened.

**What must be preserved:**
- Ari's intake spark, copied into the artifact store the night it was built. It moves with the garden and is never
  dropped. The artifact page stays published, unchanged, until the web version holds that spark.
- Every `rc-*` ruling, unchanged by the move: the other's yes, async tending, the holding-space log with no counts,
  pictures private until shown, stale dims and never dies, ending needs both, the silent exit, the Kardos credit.
- Privacy. The garden's store holds what he wrote about one relationship. On bars-engine it lives in Postgres behind
  sign-in, readable only by the garden's two members. It is never written to a repo or a log.

**Obligation, not preference:** "This will ultimately be hosted on the web" is his ruling, given today. Building more
on the artifact host goes against it.

**Phase gates for the move:**
1. **Gate 0, the phone check** (Challenger's test): the Big Mind cave opens on his iPhone.
2. **Gate 1, the port:** the Between runs at a bars-engine route behind sign-in with its own store. It is tested in
   Chromium, and in WebKit through bars-engine's own CI if CI can run it.
3. **Gate 2, on the device:** a Vercel preview link opens on his iPhone before the thread says it is done. A Your steps
   card asks him to open it. The thread's reply waits for his tick.
4. **Gate 3, Ari:** the garden is shared with Ari only after Gate 2.

**Definition of done:** he opens the link on his phone, walks to the spark and tends it. Nothing short of that counts.

## Diplomat · 30 Burning

*You keep saying the same true sentence, and it is consuming its subject.* "Close it and open it again" was said three
times. Each time it was true and each time it used up a little of his patience.

**The bridge is the web route.** He works on his phone. The web route is the one that bridges: a bars-engine link opens in Safari, can be
saved to the home screen, and is the same surface the caves already use. Ari will need a way in too. Ari opens a
garden invitation link and signs in. bars-engine's membership check (`src/lib/garden/plant.ts` is named in the callsheet
as the place) admits only the garden's two people.

**The copy principle is simple.** No more requests to reopen until the link has opened on an iPhone. A reply that asks him to test
something says what was already checked on the device, or it says plainly that nothing was.

**Who is excluded right now:** Ari, entirely, and anyone who only has a phone.

## Sage · 38 Estrangement

*You reached a conclusion from a distance.* That is the whole failure: every fix was concluded from a desktop
container, far from his phone.

**Synthesis.** The smallest coherent whole is: stop patching the artifact, freeze it as the reference, and move the
Between to bars-engine, where WAVE and the caves already run on his phone. Check on the device before and after.

- **Shaman:** kept. No more test links for him to absorb, and Ari's first sight of the garden must be one that works.
- **Architect:** kept. The artifact route's reasons no longer hold. The third position is to port the rendering code
  and replace only the boot and the store. Polling stands in for live presence.
- **Challenger:** kept. The table of four layers is the answer to "why aren't your tests translating". The Big Mind
  phone check is the gate before building.
- **Regent:** kept. The spark is preserved, the rulings move unchanged, and four gates end in his phone, then Ari.
- **Diplomat:** kept. Safari and the home screen are the bridge, the invitation link is Ari's way in, and the copy rule
  stands.

**Dissent was absent on the move.** The pass was unanimous on the move. A unanimous pass is a flag. The disagreement that existed sat between
the Architect and the Challenger on presence. The Architect would ship polling now. The Challenger held that live
presence is the one feature the artifact host had that bars-engine can't, and that dropping it without a play test is
an untested claim. The Sage keeps the Architect's order (polling first) with the Challenger's condition: his first
two-person play says whether polling is enough.

**Order:** Gate 0 phone check, then the port (one thread, Opus, bars-engine), then the device gate, then Ari.

## Outputs

### Positions (each stands unless he flips it)

- **bh-stop-patching:** No more fixes to the artifact page's plumbing. It stays published as it is, as the reference
  design and the holder of Ari's spark, until the web version takes the spark over. *Why it didn't need him:* his
  message today ("trying to fix the artifact tool"; "will ultimately be hosted on the web").
- **bh-move-to-bars-engine:** The Between moves to a bars-engine route behind his sign-in, with a Postgres store in the
  garden's shape. It reuses the cave code and the WAVE cave's look, and keeps every `rc-*` ruling. *Why:* his ruling today,
  plus the Architect's finding that the artifact's reasons (store, presence, one link) are failing or available there.
- **bh-async-first:** The web version ships with async tending. Polling stands in for live presence. A realtime
  channel is added only if his first two-person play says polling is not enough. *Why:* `rc-tend-alone` and the build
  brief's "async tending".
- **bh-device-gate:** Nothing reaches him as "try this" until it has opened on an iPhone. The device check is a Your
  steps card with a Vercel preview link. A desktop test, or a phone-sized window, never counts as a phone test. *Why:*
  the scorecard above, and his standing rule that a step carries full context (2026-10-12).
- **bh-spark-carries:** Ari's spark and everything in the artifact garden's store move to the bars-engine store in the
  same thread that builds the route. They are read once from the artifact store and written once to Postgres. Nothing
  goes into a repo. *Why:* the Regent's preservation list. It is his data and he asked that it be kept (this thread's
  brief).

### Questions

No question reaches him. The reach test sent each fork to its face:
- Web or artifact: his ruling today.
- Live presence: answered by `rc-tend-alone` and the brief's rulings.
- Where Ari signs in: bars-engine's sign-in plus the garden membership check the callsheet already names. If Ari can't
  get a bars-engine account, that comes up at Gate 3, and only then does it become a question.

## Tests (dated)

- **T1, phone check, by 2026-10-18.** https://bars-engine.vercel.app/ontology-game/big-mind opens on his iPhone. It
  resolves the open blocker: is the fault in the artifact host or in three.js on his phone? It unlocks the port. His
  message ("the WAVE and CAVES are all working on bars-engine") counts as a provisional pass. The port thread starts on
  it and confirms on the phone at T2. No separate step is sent to him.
- **T2, port on the device, by 2026-10-24.** The bars-engine Between preview opens on his iPhone and he tends the
  spark. It unlocks inviting Ari. It fails if the page hangs or the spark is missing.
- **T3, first two-person play, after T2.** He and Ari tend it, together or in turn. It settles whether polling is
  enough (bh-async-first).
