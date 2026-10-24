2026-10-17 (updated 2026-10-23)
ontology: default; touches: Relationship, PermissionEnvelope, TrustState
# Relationship creature, the Between (battle fr-between)

## Next
**2026-10-23, Wendell asks for the next phase (thread "Build Between rooms and homeroom", his message of 22:45 UTC):**
> 1) create new rooms for different people 2) the ability to choose room styles 3) the ability to send invitations to a room
> 4) a "homeroom" for players to start in and customize their character along with their relationship goals
> [...] we want one able to port whatever we create in here into those games [Cave of Lessons, Big Mind]. [...] The current
> state of the Between should be able to suggest next actions so people are checking in with themselves with the between
> and with their partner as part of the game loop

The first thread read the code and wrote the brief below, then handed off at the context line before building.

**2026-10-23, part 1 built** (thread "Build Between rooms, part 1"; bars-engine branch `claude/project-thread-yspmw4`, draft PR
on #409). Server rules (home kind, `looks` own key, `invitations` sender/answer rule, `home` private doc, `style`, a planted
garden is always `kind: "room"`), `GET /api/between` now returns `{ home, gardens }` and makes the home on first call;
each garden is a `roomSummary` (waiting, revisit, invitations, stale, joinWaiting, hereNow, lastSatTogether, person,
personName, style; ids and kinds only, never item words). The four modules are in `public/calrunia/` (look, room-styles,
next-moves, spellbook) with `src/lib/between/__tests__/calrunia.test.ts`; `npm run test:between` runs both files.
`hollow.js buildHollow` now returns `handles` (sky uniforms uTop/uMid/uLow/uHor, sun, stars, lights, lanterns, base
strengths the flicker reads). Probe: all four styles render with no WebGL errors
(`/mnt/project-files/between/rooms-home/room-styles-probe.jpg`). Not checked: the mountains, valley floor and pines keep
their dusk colours under every style (Spring morning reads odd); rain is only a `weather: "rain"` flag; the page does
not call any of this yet. The `br-*` positions are on the board (council main 4d14db0). voice_lint bans "room"; it is
his named feature, so page copy keeps it.

**2026-10-23, part 2 built** (thread "Build Between rooms, part 2"; bars-engine c8523b7 on `claude/project-thread-yspmw4`, PR #428).
No `?g=` opens the homeroom: a mirror where the Between stands, sheets Look (BEATS rows, Choose for me, kept in the home doc
and copied into each open room's `looks`, link to the sprout creator branch preview with `?look=`), Rooms (person, kind,
style, one move; Make a new room plants via POST and goes in), Goals, Check-in, Invitations (answer yes/later/no from home),
Style. In a room: Style (history line in While you were away via `garden.history`), Invite (join link + note, share or
copy; sit invitation with time and note, answers listed), a Next card (all three lanes, home's check-in included), Home
door, Spellbook on the cushions (leave-a-light waits in `garden.spells`). The figure takes the look's skin and dyed cloth by
vertex colour (player.glb has six colours, no hair mesh). Styles tint mountains, valley, river, pines; Ember rain rains.
Checked: test:between, a phone-size Chromium run on a mock store using the real rules.ts (no page errors; look, check-in,
goal, invitation yes, new room, style, sit and cast all wrote), screenshots /mnt/project-files/between/rooms-home/part2-*.
Not checked: WebKit (not installed here), a real two-phone session, the Vercel preview's store, hair colour on the figure,
a 3D mark for a left light. voice_lint: only "room" (his named feature) and old copy.
**Next:** part 3 below is built; part 4 (his 23:33 steers) is next; the dance minigame round with Ari's look after.

**2026-10-24, part 3 built** (thread "Build Between rooms, part 3"; bars-engine on `claude/project-thread-yspmw4`, PR #428).
Everyone spawns in the homeroom; `?g=` is a doorway beside the mirror (open at once for a room you share; shut for an
invitation until the orientation sheet is ticked); Rooms "Go in" and the Next card walk you through it; a reload spawns
home again (a one-time sessionStorage token carries the walk). `?skipHome=1` works on previews only (position
`br-skip-home-preview`). Style in a two-person room is `garden.styleAsk`; `rules.ts styleWrite` lets only the other person
set `style`, to the asked style, clearing the ask; Next card partner lane and While you were away show it. Checked:
test:between, npm run check, a phone-size Chromium run on a mock store built from the real rules.ts (no page errors;
home spawn, orientation gate, walk-through, reload-home, ask, a direct write refused 403, the other's yes), screenshots
/mnt/project-files/between/rooms-home/part3-*. Not checked: WebKit, a real two-phone session, local `npm run build`
(no DATABASE_URL here; the Vercel preview is the build check). Art direction (room kit page
https://claude.ai/artifact/HwUN8nLCjbjpyBLv173yww): the orientation, invite and style sheets are not polished further;
the mood stills replace them.

**2026-10-24, part 4 built** (thread "Build Between rooms, part 4"; bars-engine 4a8c89e on `claude/project-thread-yspmw4`, PR #428).
Look is the mirror: the camera stands where the glass is and the canvas flips, a short strip of part tabs and round swatches
re-dresses the figure live (build scales width, shape moves shoulder/hip bones, no new mesh), Save / Choose for me / Leave.
Check-in is a W.A.V.E. walk (seven steps, `public/calrunia/spirit-care.js`), saved with `wave:7`, leaving an ember
(home doc `embers`, rules.ts validates) offered to a spirit, kept, or left on a stone in a room. Homeroom Spirits sheet
(care word, Give an ember, Call one from the caves via `oag.spirits.v1` + new `place()`); rooms' Bring a spirit lists
homeroom spirits first (`homeSpirit`, home `away`). Checked: test:between, npm run check, mock harness at 390x844,
screenshots /mnt/project-files/between/rooms-home/part4-*. Not checked: Vercel preview build at hand-off time, two
phones, a real cave hand-off, decay over real days, iOS Safari. Barn still waits on `ba-barn-in-ship` (#399 dock look).
**Next:** his look at the part 4 preview; then the dance minigame round with Ari's look.

### Build brief, part 4: his 23:33 steers (fresh Opus thread, bars-engine, same branch and PR #428)
Wendell, 2026-10-23 23:33 UTC:
> Ok the Look in the Between should open a screen that instead of having a check list should have an interactive
> character generator. It opens a mirror where they can change the options and it changes the image in the mirror in
> real time. When they are satisfied they can save the look.
>
> We also need check-in to be more robust. Right now it's just saving data but a check-in is basically a wave. This
> check in energy can be used to feed spirits that are developed in the room. They can choose to bring spirits from
> their homeroom into the between.
1. Look = a live mirror. Scout rung 2: sprout's creator (`slice/creator.js`, KEYS and swatches, the same contract as
   `public/calrunia/look.js`). Walking to the mirror swaps the Look sheet's option rows for a mirror view: a second camera
   (or a render target on the mirror glass) on your figure, option pickers beside it, each pick re-tints the figure at
   once (`colorsOf`), Save keeps it (`keepLook`), Leave drops the draft. No new mesh, so the 3D rules bind only if one is added.
2. Check-in = a WAVE. Reuse, do not rebuild: the WAVE room and gas spirits (bars-engine #412/#413/#419), spirit care
   (`council/callsheets/spirit-care.md`), and the spirit store `cave/spirit-store.js` (`oag.spirits.v1`, on main). A
   finished check-in gives an ember the player offers to a spirit, raising its satisfaction per spirit-care.md.
3. Bring spirits from the homeroom into the Between: add a home / brought-along flag to the spirit store entry; the
   room's existing "Bring a spirit" lists your homeroom spirits. The barn is not this round (ruling `ba-barn-in-ship`:
   the barn lives in each person's ship and waits on his dock look at #399).
Done as part 3: tests, check, the mock harness (rebuild from rules.ts, about 80 lines), phone-size screenshots, one-click
preview links per state (`?skipHome=1&sheet=`).

### Build brief, part 3: his 23:25 rulings (fresh Opus thread, bars-engine, same branch and PR #428)
Board read 23:25 (2026-10-23): `br-home-is-a-room` OVERRULED: players always spawn in their homeroom; an invite link opens
a portal to the invited room only after orientation and the rules. `br-style-is-the-place` STANDS with his note: both
players must consent to a style change. Other `br-*` rows stand. Part 2 (c8523b7) built the old readings, so:
1. Boot always lands in the homeroom. `?g=` (and `?g=&invite=`) no longer opens the room directly: the home shows a portal
   (a doorway mesh by the mirror) to that room. With an invite, the portal stays shut until an orientation sheet (what the
   Between is, the rules: yes before anything changes, the silent exit, nothing scored) is read and ticked; then it opens
   and leads in. Rooms sheet "Go in" also walks through the portal, not a page jump. Keep a test skip (`?skipHome=1`) for
   previews only if he wants it; otherwise ask the board.
2. Style in a shared room becomes an ask: `garden.styleAsk = {by, style, at}`, the other says yes (sets `style`, clears the
   ask) or not now; it shows on the Next card partner lane and in While you were away. In a spark (one member) and the
   homeroom it changes at once. Server rule in `rules.ts`: with two members, `style` may be written only by the person
   answering someone else's `styleAsk` for that style; tests in rules.test.ts.
3. Re-run the mock harness (scratchpad is gone: rebuild it from rules.ts, about 80 lines: in-memory gardens, `/as/<pid>`
   cookie, the real mayWrite/merge/roomSummary), phone-size run, screenshots to /mnt/project-files/between/rooms-home/,
   preview links per sheet.

### Build brief, part 2: the page (fresh Opus thread, bars-engine, same branch and PR)
Owns the bars-engine PR on `claude/project-thread-yspmw4` and this council PR #378. Read part 1 above, not the code
history. In `public/between/garden.js` (keep the room code; add sheets):
1. Boot: no `?g=` opens `list.home.id` (today it opens the newest garden). Poll and write work on the home like any garden.
2. Style: `applyStyle({ ...hollow.handles, scene }, garden.style)` on load and on change; a Style sheet writes
   `garden/main {style}` and a history line for While you were away. Tint mountains/valley/pines per style (add their
   materials to `handles`), and draw rain for `weather: "rain"`.
3. Home sheets: Look (`look.js` BEATS as option rows, "Choose for me" = `randomLook`, saves `data/users/<me>/home {look}`
   and copies `looks[<me>]` into each room; your figure tinted with `colorsOf`; a link to Chapter 1 with `?look=`), Rooms
   (each summary with person, style and its one move from `suggest`; "Make a new room" runs today's setup sheet), Goals,
   Check-in (a feeling from the five and one line, writes `checkins` and `lastCheckin`), Invitations.
4. In a room: Style, Invite (the join link with a note, `navigator.share` and copy; and "come sit with me" writing
   `invitations.<id>`), a small Next card from `suggest({ rooms:[summary], here:id })`, a door home, a Spellbook on the
   cushions using `castable` (sitAccepted from a yes-answered invitation).
5. `?sheet=rooms|look|style|invite|checkin` jumps at boot. Done: `npm run test:between`, `npm run check`, build, iPhone-size
   WebKit run with no errors, screenshots in `/mnt/project-files/between/rooms-home/`, a one-click Vercel preview link per
   sheet in the reply, voice_lint on copy. Next after: the dance minigame round and Ari's look.

### Build brief: rooms, styles, invitations, homeroom, next moves (fresh Opus thread, bars-engine)
Branch `claude/project-thread-yspmw4` in bars-engine, already cut from round 4 (`claude/project-thread-r1hsuf`, PR #409,
ready), so the PR stacks on #409. Scout: rung 2 (we have it): a room is the existing garden; the look is sprout's creator
contract; nothing new to find. Not 3D modelling work, so the 3D rules (docs/3d-math.md, garment rule council #375) only
bind if a figure's mesh changes; tinting the existing `public/between/m/player.glb` does not change its mesh.

What exists (no need to reread): a room is a `BetweenGarden` row; `plant()` already makes one per relationship and
`gardensOf()` lists them, but boot (`garden.js` near "finding your garden") silently opens the newest one. The join is
`?g=&invite=` then `joinRequest` then the starter's welcome (`rules.ts mayWrite`). Garden updates by a member are open
except `startedBy`, `v`, `members`. Private docs are `data/users/<id>/garden|spark|pouch` (`PRIVATE_KEYS`).

**Positions (stand unless he flips them; the build thread lands them on the board as `br-*` rows via sync_board.py):**
- `br-room-is-garden`: a room is one garden, one per relationship. No new table, so the Vercel preview (which skips
  `migrate deploy`) still has a working store.
- `br-home-is-a-room`: the homeroom is a garden with `kind: "home"`, one member, `phase: "home"`, no creature, no join.
  `plantedHome()` beside `plantedGarden()`; `GET /api/between` makes it on first call if missing; boot with no `?g=` opens the
  home, never the newest room.
- `br-style-is-the-place`: a room style changes the place, not the Between, so either member may change it with no yes;
  the change shows in "While you were away". Stored as `garden.style`.
- `br-look-is-sprouts`: the look is sprout's creator text `shape.build.skin.style.colour.outfit.dye` (sprout
  `slice/creator.js` KEYS and option ids), so a look made in the homeroom opens Chapter 1 with `?look=` and the reverse.
  Kept in the home's private doc; copied into each room as `garden.looks[<me>]` (rule: a member writes only their own key)
  so the other person sees you as you made yourself. Never a photo (`ba-likeness`).
- `br-goals-private`: relationship goals live in the home's private doc, each optionally tied to a room; the room's
  `setup.hopes` stays as it is.
- `br-invite-two-kinds`: an invitation is either "join this room" (the existing token link, now with a note, the phone's
  share sheet and copy) or "come sit with me" for a member (a time and a note, `garden.invitations.<id> = {by, kind:"sit",
  when, note, at, answer}`; the other answers yes, another time, or no). A sit invitation answered yes is what opens dual
  spells (Ari, `between-ari-formation-01`).
- `br-next-moves-three-lanes`: suggestions come in three lanes, yourself, the Between, your partner, at most one each,
  plain words, never a count or a score. No AI. Examples: yourself: no check-in today; the Between: stale, or a lantern
  waits; partner: an offer or agreement waits for your yes, an agreement is up for revisit, an invitation waits, they
  are here now, you have not sat together this week.

**Portable modules (plain ES modules in `public/calrunia/`, no three.js import, node tests through tsx in
`src/lib/between/__tests__/`), so the Cave of Lessons and Big Mind take them as they are:**
1. `look.js`: the creator contract (KEYS, option ids, `parseLook`, `lookText`, `colorsOf(look)` giving skin, hair and cloth
   hex from sprout's swatches and DYED table). Test that a sprout look text round-trips.
2. `room-styles.js`: three to four styles as data (Dusk hollow, today's look and the default; Moonlit, night blue and
   silver with stars; Spring morning, bright and green; Ember rain, warm hearth with rain past the opening). Each style is
   sky colours, fog, hemi/dusk/rim/fire light colours and strengths, lantern hue. `applyStyle(handles, style)` takes the
   lights and sky that `hollow.js buildHollow` returns (add them to its return value) and only sets values.
3. `next-moves.js`: `suggest(state)` is pure; state is `{ home: {lastCheckin, goals}, rooms: [summary] }` from the home, or
   one room's view inside a room. Each move has `{lane, id, title, line, act}`; `act` names a sheet or `room:<id>`.
4. `spellbook.js`: spells as data with `kind: solo|dual|async-dual` and `castable(spell, {sitting, otherSitting,
   sitAccepted})`: solo needs you on a cushion, dual needs both on cushions and an accepted sit invitation, async-dual
   starts on your cushion and the other completes it later. Three starter spells only; the dance minigame (Ari: instead
   of push hands) is the next round, not this one.

**Server:** `rules.ts`: `kind:"home"` refuses join and items from anyone else; `looks` own-key rule; `invitations` rule
(you write your own invitation; the other writes only `answer`); add `home` to `PRIVATE_KEYS`. `store.ts gardensOf`
returns a summary per room for the next-moves lanes (waiting on my yes, up for revisit, invitations for me, stale,
join request waiting for my welcome). Tests in `rules.test.ts` for each new rule.

**Page (`garden.js`, keep the room code; add sheets):** the home opens in its style with your figure tinted by the look,
a mirror spot that opens the Look sheet (the creator's beats as option rows, "Choose for me"), a Rooms sheet (each room
with its person, style and its one next move; "Make a new room" runs today's setup sheet), Goals sheet, a Check-in sheet
(feeling from the five, one line, private), and an Invitations sheet. Inside a room: a Style sheet, an Invite sheet, a
small "Next" card from `suggest()` above the tools, a door back home, and a Spellbook on the cushions.

**Done:** `npm run test:between` plus the new tests, `npm run check`, build; an iPhone-size WebKit run with no errors;
screenshots in `/mnt/project-files/between/rooms-home/`; one-click Vercel preview links in the reply opened at the state
to test (add `?sheet=rooms|look|style|invite` jumps to boot); voice_lint on copy; record the `br-*` positions; end with
the next move (the dance minigame round, Ari's look).

**2026-10-21, Ari's playtest (Wendell's message of 01:08 UTC, relayed in chat, word for word):**
> I sent Ari’s link and the feedback was they wanted
>
> 1) an ability to design our room
> 2) the ability to move objects around
> 3) more ergonomic controls for someone who is already tired at looking at screens. She suggested captions and scrolling text that moves at the speed of comprehension and can be sped through
> 4) they want to be able to customize their character to look and feel just like them
> 5) they want the actions in the rooms to be spells. They’re attached to the idea of this as a dual cultivation space. Where players can create and design formations and moves. She wants the spirits movements to be more natural and a space for them that’s just their own like the barn in Stardew valley.
>
> She loved the idea of the gummy ship with a farm inside of it and really resonated with the ability to render worlds mathematically like no mans sky. She seemed to think this would be easy because of conversations she had with the developers and how they kept the cost of computation and rendering low by procedurally generating the world but only to the decree the player could see or travel
>
> Loved the ability to dance and wants to see how partners could use the root engine to play with each other and cultivate spirit energy
>
> She’s also been using the 5 elements negong by mantak chiu and was curious if there was a way for characters in the between could cultivate their spheres in alignment with emotional alchemy to raise qi for use in the room

Ari's invite step is done: Wendell sent Ari the link (step 3 under Waiting on). Pass on the notes: `council/passes/6FACE_PASS_between-ari1_2026-10-21.md`.

**2026-10-21, pass `between-ari1`** on Ari's notes (ledger `council/ledger/2026-10-21-between-ari1-pass.json`, rows `council/callsheets/rows/between-ari-2026-10-21.json`). Seven `ba-*` positions stand: round 4 is comfort (caption mode at a pace each player sets, moving your own items, spirits that pause and turn; `ba-round4-comfort`); spells start as one formation card to Ari, which also asks what the dance was (`ba-formation-card`); spells in plain words (`ba-spells-plain`); the spirit barn lives in each person's ship (`ba-barn-in-ship`); likeness by creator choices, never a photo (`ba-likeness-choices`); qi is the hollow's light, never a currency (`ba-qi-is-light`); procedural worlds and Root dance stored on their strands (`ba-worlds-stored`). Question: `ba-ari-look` (A, Ari's play counts as his look so round 4 starts, recommended; B, he looks first). Deferred: `ba-chia-credit`. Tests T1 (Ari reads the card, by 10-28), T2, T3.
Next: (1) a Sonnet thread lands the `ba-*` rows on the board and publishes the formation-card step for Wendell to send Ari; (2) on `ba-ari-look` A, or his ticks on the hollow and lantern steps, a fresh Opus thread on bars-engine builds round 4 per the pass's build brief. Hold round 4 until then (`hx-looks-gate`).

**2026-10-21, round 4 (comfort) started on `ba-ari-look` = yes** (ledger `council/ledger/2026-10-21-pull-013156.json`). Build: bars-engine branch `claude/project-thread-r1hsuf` (caption mode, moving your own items, spirits that pause, sniff and turn). His steers on that pull, for later rounds; round 4's scope stays the three comfort fixes:
- `ba-formation-card` stands, steer: "We are dancers and she was curious if the figures could dance together in addition to doing push hands Nan dance studio". Formations should cover partner dance as well as push hands.
- `ba-spells-plain` stands, steer: "Some spells need both people there. Individual spells can be cast by one’s self but dual cultivation spells need both people there. There should probably be asynchronous dual cultivation spells as well". Three kinds: solo, dual (both present), asynchronous dual.
- `ba-qi-is-light` stands, steer: "I think it should be a meter and should be a currency like the scales one I’ll eights cradle. I see this as how we can integrate vibeulons into the game world". This turns the position's "never a currency": qi is a meter and a currency, the way vibeulons enter the game world. A later pass reconciles it with `rc-*`/`cc-*` before any build.
- `ba-worlds-stored` overruled, steer: "We can start building a structure that holds all of them. The between is a subfeature of an emergent calrunian world along with root and the sprout game  game". A structure that holds the Between, Root and the sprout game as parts of one world is wanted; it needs its own pass.

**Crafting, 2026-10-18, pass `crafting-charge1`:** Wendell's message of 18:42 asked for six-face research on Minecraft, Roblox, No Man's Sky and Taoist cultivation crafting, aimed at turning inner charge into game assets and items. Pass `council/passes/6FACE_PASS_crafting-charge1_2026-10-18.md`, ledger `council/ledger/2026-10-18-crafting-charge1-pass.json`, rows `council/callsheets/rows/crafting-charge-2026-10-18.json`, doc https://claude.ai/code/artifact/c01e8825-0736-455a-8541-a877eb6d2627. All five faces backed slice 1 on conditions. Twelve `cc-*` positions stand (slice 1 is one ember into one lantern at the hearth, `cc-hearth-slice`; the sealed-text leak is fixed on the server first, `cc-seal-fix-first`; embers private, intensity is look only, element hidden unless shown, no staleness-holding item, no random failure, no two-person recipe before Ari reads one). Question on the board: `cc-first-made` (A lantern, recommended; B tea). Deferred: `cc-licence-conflict` (toolbox.yaml allows CC-BY, QUICKSTART only own work and CC0). Tests F1 (first shared session), F2 (Ari reads a recipe card), F3 (desk count of wuxing pairs).
Next: a fresh Opus build thread on bars-engine, on the hollow (#366/#367), per the build brief at the end of the pass file: the server fix, then embers and lanterns, `bh-device-gate` iPhone first, Ari after. Name the scout line.

**2026-10-16, pass `relationship-creature1`:** Wendell's message of 22:20 proposing a creature two people co-tend in the
Lower-Left space, fed by worked-through charge, living in a garden of BARs, drawn from Eri Kardos's *Relationship
Agreements* (2016), for Mastering Allyship, Flirtcraft and Friendcraft. Pass
`council/passes/6FACE_PASS_relationship-creature1_2026-10-16.md`, ledger
`council/ledger/2026-10-16-relationship-creature1.json`, rows `council/callsheets/rows/relationship-creature-2026-10-16.json`.
Eleven `rc-*` positions stand: the creature is the relationship and the Freds are each person's daemons
(`rc-is-relationship`); only a joint check-in moves it (`rc-joint-checkin`); pictures private, drift only between shown
pictures (`rc-pictures-private`); what feeds and lowers it, the cave's trust rules carried over (`rc-feeds`); an offered
charge needs the other's yes (`rc-offer-received`); consent each session, silent exit, leaving composts (`rc-exit`);
your spirits visit and stay yours (`rc-spirits-visit`); agreements are BARs in a shared garden with a membership check
(`rc-agreements-bars`); an honest ending completes (`rc-goal`); never Fred, Kardos credited in paraphrase (`rc-credit`);
nothing built, not in the demo, Friendcraft first, a paper play next (`rc-order`).
Questions on the board, round 1 of the battle: `rc-name` (A the Between), `rc-stale` (A only a broken agreement, the
faces split), `rc-who-holds` (A two people, one can start).

**2026-10-16, 22:40, his answers (board read, ledger `council/ledger/2026-10-16-pull-224001.json`):** `rc-name` A, the
Between. `rc-stale` B: plain neglect can make it stale too. `rc-who-holds` A, with his steer: you can start alone tending a spirit made of
the charge you project onto someone you are not yet in a relationship with (Flirtcraft especially), and it becomes a
Between when they join. He overruled `rc-joint-checkin`, `rc-exit` and `rc-order`. Steers on standing rows: `rc-feeds`
"Also fed by metabolized charge offered to the relationship and inspirations and ideas and desires"; `rc-offer-received`
"Can show up in the garden but needs to be co-tended for it to affect the between". Five revised positions on the board
(rows `council/callsheets/rows/relationship-creature-answers-2026-10-16.json`): `rc-spark`, `rc-tend-alone`,
`rc-stale-neglect`, `rc-end-together`, `rc-demo-garden`. T2 (paper play) is dropped by his overrule.

**2026-10-16, 23:20, demo garden built:** https://claude.ai/artifact/W4MpDsm5xnnaLGcoPNWVv6 (the Between Garden).
One page with a shared store (db, user, downloads). Setup asks who, what kind, what he hopes for; spark until the other
person asks to join and he welcomes them, then the Between with history kept. Three states from satisfaction
(charged, steadied, allied, base 3, fed by agreed agreements and offerings said yes to), stale after 5 days untended
(dims, never dies, any tending airs it out). Agreements run drafted, proposed, agreed, revisit, retired, composted;
revisit, a named break, retire and compost each wait for the other's yes. Offerings wait for a yes; a charge arrives
sealed and can pass unopened. "While you were away" lists the other's acts with no counts. Pictures stay in
localStorage until shown; drift is the two shown pictures side by side, "Not compared" otherwise. Visiting spirits
stay their owner's. Ending needs both; each ticks what to keep (private) and takes a JSON copy; the garden closes or
changes kind. Silent exit closes it with no trace of who; help lines shown. Writes made offline wait on the device and
send when back. Tested with a mock store in two pages at once and one page offline (all 15 steps pass); the real store
was checked with a read and a refused contributor write to another person's shown pictures. The other person needs
Editor (outside the organization) or Contributor access from the Share menu to tend it.
Next: his play, then round 2 from his notes.

**2026-10-16, 23:05, his look at the demo garden (ruling, in chat):** "Ok the garden is a bit too abstract. I'm looking
for it to be a 3d game space not unlike the WAVE room but 2 people can inhabit it and it's interactable. This version
might be useful for an intake but the output should be a 3D space where the spirits and daemons can interact and walk
around. Let's use the design ontology for this". The 2D page (https://claude.ai/artifact/W4MpDsm5xnnaLGcoPNWVv6) stays
as the intake; the play space is 3D.

**2026-10-16, 23:16, board read (ledger `council/ledger/2026-10-16-pull-231549.json`):** `rc-spark` stands with his steer:
"History should start when the other person joins. The player who jumped ahead should metabolize their charge or just
have it as a personal spirit." `rc-tend-alone`, `rc-stale-neglect`, `rc-end-together`, `rc-demo-garden` stand.

**2026-10-16, 23:45, the Between in 3D built:** https://claude.ai/artifact/NTi4jcpaHkDEMnqpVA9LBq. Ontology read
first: `council/passes/BETWEEN_3D_ontology_2026-10-16.md` (default profile; every fork settled by an `rc-*` position or
his steer, nothing to the board). One three.js page under the WAVE cave's dome (bars-engine `rooms/wave-room/room.glb`)
with `db`, `room`, `user`, `downloads`. Each person walks (tap the floor, drag to look, WASD) and sees the other live,
with a ring of their hue at their feet (teal for whoever started, plum for whoever joined). The Between stands in the
middle (a plum flame while it is a spark), breathing 4 in, 6 out, jittery when charged, in leaf when allied, grey and
dim when stale. Agreements are plants planted where you stand (seed, bud, flower in both hues, drooping amber,
stone, soil); offerings are lights set on stones, sealed charge a dark shell; walking up gives the acts (take it in,
let it pass, open it, propose, agree, ask to revisit...), and a yes flies the light into the Between. Spirits (fox or
tortoise in their element's colour) and daemons (the WARP bodies, npc-gesture 10-14) walk paths drawn from their seed
and the shared clock, so both screens agree; they stop and face whatever they meet, and a daemon meeting the other
person's walker says so. Only the owner can call a walker over or send it home; the other can greet it. His steer:
when the starter welcomes the other in, the spark's items leave the shared store for the starter's private store, and
the spark walks on as their own fire spirit or composts; the Between's history starts at the welcome. Pictures,
"While you were away", ending, silent exit and credit carry over from the intake. Models ship as `.json` glTF files
beside the page (Artifacts do not serve `.glb`). His intake garden (Ari, romance or flirting, "Become powerful
together", a spark) was copied into the new page's store. Tested in a browser with a stand-in store, a desktop page
and a phone page at once: join, welcome, sealed offering opened and taken in, daemons and a spirit brought,
agreement planted, proposed and agreed, one page away while the other tended, then back to "While you were away".
Next: his play; round 2 from his notes.

**2026-10-17, 00:45, hosting pass `between-hosting1`:** the 3D page never opened on his iPhone in the Claude app.
Three patches (textures, inline cave with timeouts, a limit on the store read) each passed in desktop Chromium with a
stand-in store and failed on his phone; the last visible stop was the artifact platform's own store read. He called
the six: "This will ultimately be hosted on the web ... Also the WAVE and CAVES are all working on bars-engine". Pass
`council/passes/6FACE_PASS_between-hosting1_2026-10-17.md`, ledger `council/ledger/2026-10-17-between-hosting1.json`,
rows `council/callsheets/rows/between-hosting-2026-10-17.json`. Five `bh-*` positions stand: stop patching the
artifact (it stays published, untouched, holding Ari's spark), move the Between to bars-engine behind sign-in, async
first with polling for presence, nothing reaches him as "try this" until it has opened on an iPhone, and the spark
moves to the new store in the port thread. Patched page source (version 4) is the artifact itself.

### Build brief: the Between on bars-engine (next thread, Opus, bars-engine)
- **Start from** the artifact page's source (Artifact read of https://claude.ai/artifact/NTi4jcpaHkDEMnqpVA9LBq): the
  scene, walkers, garden, sheets and acts carry over; replace only the boot and the store calls. Drop the artifact-only
  workarounds (inline models, capability timeouts, the texture-loader override) unless a WebKit test shows one is needed.
- **Where:** a route beside the caves (`/ontology-game/between`), behind his sign-in like `/board`, models served from
  `public/` as `.glb`. Store in Postgres with a Prisma migration (migrate, never `db push`), tables in the garden's
  shape: garden (with members), items, spirits, daemons, shown, plus each person's private note. API routes do the
  writes; the page polls every few seconds for presence and changes (`bh-async-first`).
- **Membership:** only the garden's two members read or write it (`src/lib/garden/plant.ts` per the callsheet). Ari
  joins by an invitation link and signs in; if Ari cannot get an account, that becomes a board question then.
- **Carry the spark** (`bh-spark-carries`): read the artifact's store once with ArtifactData, write it once to the new
  tables; nothing goes into a repo, log or reply.
- **Rulings hold:** every `rc-*` ruling the 3D page carries, unchanged.
- **Done** (`bh-device-gate`): build and check pass, a Vercel preview link opens on his iPhone (a Your steps card with
  the link, what to tap, and what he should see), and he tends the spark. Only then is it shared with Ari.

### Build brief: the Between in 3D (next thread, Opus, load design-ontology)
- **Ontology first.** Load `.claude/skills/design-ontology/SKILL.md` and the profile `ontology/manifest.yaml` names for
  relationship and trust mechanics (touches: Relationship, PermissionEnvelope, TrustState). Map each `rc-*` ruling onto
  what it becomes in the space before building; anything the ontology and the rulings can't settle goes through the
  reach test and onto the board, never to chat.
- **What he asked for:** a 3D space like the WAVE room (bars-engine `content/ontology-game/cave/`, `openRoom` in
  `cave.js`, DESIGN.md "The WAVE room"), which two people inhabit at once or in turn, where the Between, each person's
  visiting spirits and their daemons walk around and interact, and where the garden's acts (offering, agreeing, saying
  yes, tending) are things you do in the space.
- **Default route (position, stands unless he flips it):** a three.js Artifact page with `db` (the garden, persistent),
  `room` (live presence: both figures, their walking, live acts) and `assets` (the existing spirit and daemon .glb
  files: `/mnt/project-files/3d-build/npc-warp-2026-10-14/`, `spirit-rig-2026-10-14/glb/`), reusing the cave kit and
  the WAVE room's look. It reuses the intake page's store shape where it can (garden/main, items, spirits, shown), so
  the intake's setup carries into the space. Reason: an Artifact already gives both people one link, sign-in, a shared
  store and live presence; bars-engine has the WAVE room code but no live two-player channel. Port into bars-engine
  later if the space earns it.
- **Rulings still hold:** nothing changes the Between without the other's yes; async tending; holding-space log with no
  counts; pictures private until shown; stale dims, never dies; ending needs both; silent exit; Kardos credited, never
  Fred.
- **Done:** published, two-viewer test (two figures moving at once, one acting while the other is away), phone width,
  his link in the reply; then his play.

### Build brief: the demo garden (next thread, Opus, one pull request or artifact)
His words (rc-order): "We should create a demo garden that I can play with a design with one relationship I want to work
on. It should be able to be accessed synchronously and synchronously by the two players".
- **Where:** one published Artifact page with the `db` capability (a shared store, as the Council Board has), so both
  people open the same link, alone or at the same time. Load the artifact-capabilities skill first. The page is private
  until he shares it from its Share menu; the reply says so. Non-AI in play.
- **Setup:** the page asks him about the one relationship he wants to work on (who, what kind, what he hopes for). That
  lives only in the garden's store, never in the repo or the reply.
- **The creature:** before the second person joins, a spark (`rc-spark`): a spirit of the charge he projects, drawn in the
  spirits' states. When the other person joins, it becomes the Between, history kept. Shown in three states from its
  satisfaction (`ss-three-states`), plus stale (`rc-stale-neglect`): dims after a stretch untended, never dies, aired
  out by either person's tending, names no one.
- **The garden:** beds of BARs. Agreements (`rc-agreements-bars`: drafted, proposed, agreed by both, up for revisit,
  retired or composted). Offerings: worked-through charge, inspirations, ideas, desires (`rc-feeds` steer). Anything one
  person adds alone shows in the garden as an offer and changes the Between only once the other co-tends it (says yes)
  (`rc-tend-alone`, `rc-offer-received`). Visiting spirits stay their owner's (`rc-spirits-visit`).
- **Holding space:** a log of each person's acts while the other was away, as the acts themselves, with no counts or
  comparisons (`rc-tend-alone`).
- **Pictures:** each person's picture of the Between and of the other person stays in their own browser (localStorage)
  and is shown only by choice; drift is the gap between two shown pictures, "not compared" when either holds back
  (`rc-pictures-private`).
- **Ending:** both consent; each picks what to keep; each takes a copy of the Between with its history; the garden
  closes or turns into another relationship type (`rc-end-together`). A silent exit and a line to outside help stay
  for anyone being hurt (`rc-exit`).
- **Credit:** a small line, "Inspired by Eri Kardos, Relationship Agreements (2016)", in the council's words; never
  "Fred" (`rc-credit`).
- **Done:** published, his link in the reply, voice_lint and no-ai-slop run on the copy, two browser tests (two
  profiles editing the same store, one offline then back). Then his play, then round 2 from his notes.

1. **His answers** came in (above). A second round covers whatever his answers open (likely the paper
   play's shape and who plays it).
2. **T2 paper play** with one willing person, by 2026-10-30, after `rc-who-holds`. Fails if either person uses the
   creature against the other or feels obliged to feed it. Needs a person, so it becomes a step on Your steps.
3. **T3 source read** by 2026-10-23: what Fred stands for in the book; settles the credit line.
4. **Build** waits on the paper play. Then one thread in Friendcraft's redesign pass, against the Architect's acceptance
   tests in the pass. A bars-engine shared garden needs a garden id two players hold and a membership check in
   `src/lib/garden/plant.ts`.

## Waiting on
2026-10-17: the port merged (bars-engine #357). The garden is at https://bars-engine.vercel.app/ontology-game/between,
behind bars-engine sign-in, with its own Postgres tables (migration `20261017120000_add_between_garden`), API routes
under `/api/between`, models in `public/between/m/`, and the cave build's cave model. Two people only; the second joins by
the invite link in the page's More sheet. Local two-player test passed (join, welcome, sealed offering, agreement,
daemon, presence, a stranger refused).

Open, in order:
1. **His device check**, Your steps list `between-on-bars-engine` (step 01 open it on the iPhone, step 02 tend the
   spark). A stuck screen comes back as the step's note; troubleshoot from that text, no more artifact patches.
2. **Carry the spark** (`bh-spark-carries`): POST `/api/between/carry` with the artifact store's `garden/main` and
   `from: "artifact:NTi4jcpaHkDEMnqpVA9LBq"`, bearer COUNCIL_MENU_TOKEN. Blocked while that key returns 401 (the
   menu-key-match steps). The route is idempotent and answers "not needed" if he has already replanted under step 02,
   so either order is safe. Read the store with ArtifactData in the thread that runs it; its contents go nowhere else.
3. **Done 2026-10-21: shared with Ari** (Wendell sent the link; Ari's notes are under Next). Was: **Share with Ari** (steps 01 and 02 ticked 2026-10-18 00:17 UTC, no notes; the invite is the only thing left, and only he can make it from the More sheet on his phone, since it needs his sign-in): copy the invite link from the More sheet. If Ari can't make a
   bars-engine account, that is a board question.
4. **Round 2, cozy and fun** (2026-10-17, board read 01:40: `bh-async-first` overruled after Ari said it is not cozy or
   fun enough). Gap list and the ChatGPT prompt: `council/passes/BETWEEN_round2_cozy_2026-10-17.md`. Waiting on his
   concept image, Your steps list `between-round2-concept` step 01; he attaches it in the thread "Between round 2: cozy".
   **Image in (2026-10-17 04:37):** four views from ChatGPT, in his Drive folder "Cave studio inbox" and copied to
   `/mnt/project-files/between/round2/concept/the-between-view-1.png` to `-4.png` (step 01 ticked). Build brief below
   ("Build brief: round 2, the hollow"). Gaps 6 to 10 are round 3. The artifact page stays as it is and is retired once
   he plays here.
   **Built (2026-10-17 05:30):** bars-engine #366, the hollow (gaps 1 to 5), CI green, preview opened clean in an
   iPhone-size WebKit run. Screenshots beside the four views: `/mnt/project-files/between/round2/build/`
   (`concept-vs-build.jpg`). His try: Your steps list `between-round2-try` step 01 (preview link, share token until
   18 Oct 04:27 UTC). Next: his note on that step decides fixes or round 3 (gaps 6 to 10); Ari's invite only after he
   ticks it. Sitting together was tested with two local players only.
   **Round 3 started (2026-10-17):** `ppo-who-paints` answered "code-paints": our code paints the four views. bars-engine #367
   (draft, on #366) adds `public/between/paint.js`, a painterly patch to three's standard material keyed to the concept
   views' luminance ramp (banded light, brush noise, warm shadow fill, rim; `?paint=0` for plain). Pictures:
   `/mnt/project-files/between/round3/`. His try: Your steps `between-round3-try` step 01 (due 10-19); his note picks
   textures next or gaps 6 to 10. Not yet measured on his phone. Sitters and creature in the four views were not
   captured (store-down run).

### Build brief: round 2, the hollow (next thread, Opus, bars-engine; load design-ontology default profile)
- **Look at the four views first** (`/mnt/project-files/between/round2/concept/`); they are the target. Gap list and
  reasons: `council/passes/BETWEEN_round2_cozy_2026-10-17.md`. Build gaps 1 to 5 in one bars-engine pull request.
- **The place (gaps 1, 2):** replace the WAVE dome with a hollow under a great tree's roots: arching root walls and
  vines, a stone hearth with shelves of pots on one side, two hanging paper lanterns, and one wide opening onto a dusk
  valley (gradient sky, sun low over mountains, a river, pines). Inside, a round raised mossy dais with a stone rim; a
  stream with stepping stones, lily pads and glowing crystals runs past it toward the opening, a rope fence at the
  edge. Small enough that both figures and the creature fill the frame on a phone. Light: warm pools from hearth and
  lanterns (flicker), cool blue dusk outside. Default: procedural three.js geometry plus the existing kit, kept light
  for an iPhone; Blender only if a part can't be made to read in code.
- **Alive when idle (gap 3):** fire flicker, fireflies, water shimmer, leaves sway; quiet ambient sound (fire, water,
  night insects) through Web Audio, starting on the first tap, with a mute toggle.
- **The Between (gap 4):** the round, fluffy, leaf-scaled creature from the views, teal fading to plum, a sleepy smile,
  a sprout on top. It opens its eyes and turns toward whoever arrives, bounces when an offering flies in, sleeps when
  nobody is there, dims when stale. Spark phase: the same creature small and plum only. States from satisfaction keep
  their meaning (charged jittery, allied leafier).
- **Together (gap 5):** cushions on the dais, one teal, one plum; tap a cushion to sit there (sit pose, in code if the
  player model has no clip). When both sit, the camera eases to the low view of view 3 and the creature glows
  between them. Waving from the near sheet. Agreements grow as the glowing lotus flowers; offerings rest on the low
  table or stones; the fox and tortoise keep their walkers (the fox curls up asleep near a sitting owner).
- **Keeps:** the store, API, sign-in, invite link and every `rc-*` ruling from #357; only the scene, creature, bodies'
  poses and camera change. Sheets keep working.
- **Done:** build and check pass; screenshots beside the four views at phone and desktop size in
  `/mnt/project-files/between/round2/build/`; it opens on an iPhone-size WebKit run with no errors; then a Your steps
  card "try this" with the preview link (bh-device-gate). Ari gets it only after he has tried it.

## Files
- Pass, ledger and rows above. Source: Multiamory episode 103 page, https://www.multiamory.com/podcast/103.
- 2026-10-19 board: putting a charge into the shared lantern makes its element public (his steer on `cc-element-hidden`, which stands for the pouch).
- 2026-10-20 (Wendell, build thread, bars-engine #380): he could not open the Between from a link. Fix in #380: `/games` page (sign in, open The Between, Admin at the bottom) and eslint ignores `public/game`, `public/understood-app`, `public/ontology-game` (gitignored `npm run build` outputs that failed the pre-commit lint). Lanterns reach production only when #380 merges.
- Done, admin refresh (his ask, 2026-10-20): bars-engine #406 merged; `/admin` opens on what he uses most and `/admin/games` is the development dashboard for the games on bars-engine.

## Room kit, scroll invitation, first minute (art direction, 2026-10-23)
His ask, 2026-10-23: a scroll-like invitation card, an orientation, and "a lightweight room customizer and ... an even
more basic room people can use to update things and add items and assets they earn through play". Art direction first
(game-briefs-art-first). Page with three touchable stills, reference board, first-minute script and the kit's shape:
https://claude.ai/artifact/HwUN8nLCjbjpyBLv173yww (source `/mnt/project-files/between/room-kit/homeroom-kit.html`).
Board rows (`rows/room-kit-2026-10-23.json`): positions `rk-spots-not-grid`, `rk-earned-only`, `rk-place-is-shared`,
`rk-one-kit`; questions `rk-still-nook`, `rk-still-scroll`, `rk-still-minute`. Nothing built.

Coordination: the part 3 thread ("Build Between rooms, part 3", bars-engine #428) keeps building as briefed. Its
orientation sheet, invite form and style sheet are what these stills replace, so it should not polish those three
screens further; the kit lands as a new pull request stacked on #428 once his yes arrives.

### Brief: room kit build (Opus, bars-engine, starts on his yes to any still)
- Read the page above first; build only the stills he said yes to, with his notes. Match them in the hollow's real 3D
  look (paint.js), not the sketch.
- `public/calrunia/room-kit.js` beside `room-styles.js`, no three.js inside: `SHELLS` (spots with `takes`: hang, small,
  floor), `ITEMS` (glb, takes, earned-by), `applyRoom(handles, room)` with `room = { shell, style, placed: {spot: item} }`.
  The Dusk hollow becomes shell `hollow` with today's pieces pre-placed; shell `nook` is the starter (hearth, window,
  five spots). Styles become the window's light.
- Placing: tap item in the satchel, glowing spots that take it pulse, tap a spot; tap a placed item to send it back.
  Shared rooms per `rk-place-is-shared`; both show in While you were away. Save `placed` with the garden row (no new
  table if it fits the existing JSON), so previews keep a working store.
- Earned items come from events that already exist: first kept agreement (lantern), let-go spirit (seed pot,
  spirit-store.js), first sit together (cushion), orientation (mirror, first blank scroll).
- Scroll: replaces the invite form. When as chips, one handwritten line, seal press sends; arrives sealed on the
  shelf; three ribbons (Yes, Another time, No with no reason). Yes opens the doorway between rooms.
- First minute: wake, tend the hearth, place the mirror, write a hope (private, br-goals-private), the yes rule; a vine
  falls per step and the doorway opens; skipped steps stay as a glow. Captions at reading speed (Ari's note 3).
- Portability check: the Cave of Lessons or Big Mind lists its own spots and calls `applyRoom` with no kit changes.
- Done: Vercel preview link opened at the nook (skip-ahead param past orientation, his testable-preview rule), screenshots
  beside each still in `/mnt/project-files/between/room-kit/build/`, two-player test of placing in a shared room.

### Room kit build, round 1 (2026-10-24, thread "Build the Between room kit")
His yes to rk-still-nook, rk-still-scroll, rk-still-minute (board read 00:32, no notes). bars-engine draft #431
(branch claude/project-thread-q2xj75, stacked on #428). Part 1 cd8987a: `public/calrunia/room-kit.js` (SHELLS, ITEMS,
applyRoom, place/lift helpers, room-kit.test.ts), homeroom = shell `nook`, satchel placing, shared-room owner rule,
`placed` in the garden JSON. Preview params `?satchel=all&nook=1`. Summary and renders:
`/mnt/project-files/between/room-kit/build/part1-summary.md`. Part 2 (scroll, first minute, two-player test) was
running in a worker when the thread hit the 150k line; its report is `part2-summary.md` in the same folder.
br-orient-each-invite steer (00:35): anyone who did the first minute skips per-invite orientation.

### Brief: room kit, finish round 1 (Sonnet is fine unless part 2 is missing)
- Read `part1-summary.md` and `part2-summary.md` in `/mnt/project-files/between/room-kit/build/`. If part 2's summary
  or commit on claude/project-thread-q2xj75 is missing, build part 2 from "Brief: room kit build" above (Opus).
- Own bars-engine #431: subscribe, merge #428's head (642b972 or later, robes on every figure) into the branch, confirm the #428 preview for 642b972 is green, get #431's Vercel preview green, update the PR body with part 2.
- Give Wendell the one-click preview opened at the nook (`/ontology-game/between?satchel=all&nook=1` on the #431
  preview), plus `?minute=1` and the scroll param from part 2, and the side-by-side renders beside each still, as a
  board step (his look), not chat questions. Choices the workers made that he may want to flip go on the board as
  positions. Then hand off and resolve.

### Mirror clothes fix (2026-10-24, thread "Fix clothes in the Between mirror")
His look at part 4: "The mirror looks great but the clothes and robes aren't rendering". Cause: the Between drew
player.glb, a body with a short tunic painted on; the Clothes choice only recoloured it. Fix on bars-engine #428
(commit 642b972, branch claude/project-thread-yspmw4): `public/between/wardrobe.js` dresses every player figure as
sprout's creator does (Average Dusk + mocap Walk, baked J5 robe cut to jacket / wrap dress / long coat, sash on the
dress, travel pants, hair, legs masked under the cut, leg and arm capsules; `figure-robe.js` copied from sprout #72,
models in `public/between/m/dusk/`). A standing figure holds the Walk's first frame (where the robe was baked).
Checked: local render of the mirror with stubbed /api/between, all three cuts. Not checked: walking in the room,
sitting on a cushion (the robe does not follow the sit pose; legs are masked so it hangs), two players at once (cost),
a real phone. #431 (room kit) is stacked on #428 and needs a rebase onto 642b972.

### Brief: real body types (his note 2026-10-24, next round, art first, Opus)
His words: "the round body type isn't actually round we've just been widening the character rather actually creating a
different body type. Some of the changes can be subtle transformation but others need to be more complex and interact
with the clothing differently". Today shape and build are bone scales (wardrobe.js SHAPE/BUILD, sprout figure.js).
1. Tool ladder first (docs/tool-scout.md): MPFB2/MakeHuman targets as shape keys on Average Dusk (calrunia-creator.md
   option 2), CharacterStudio, VRoid-style body sliders. Record the rung.
2. Art first: a reference board of four bodies (slender, average, broad, round) plus the three shapes, and one mood
   still per build in the long coat, before code. His yes on a still opens the build.
3. Build: shape keys on the body and matching corrective shape keys on the robe/sash/pants (robe-baked needs a bake
   per key or a delta set), mask bands per body; keep subtle ones (slender, shoulders) as bone scales.
4. Probe as tools/figure-legs-probe.mjs does, at each body. Preview at ?sheet=look on the Between.

## Mirror light and standing idle build (brief, 2026-10-24, round 2)

TRIGGER: his yes on board step `lt-mirror-look-02`. A note instead starts a third lighting round from it. Opus thread, bars-engine, stacked on room kit #431 (branch claude/project-thread-q2xj75).

- Round 1 (https://claude.ai/artifact/GVQ24jwUAMUEMGDC2JMRtW) drew his note on lt-mirror-look-01: better, but light edges too harsh and each light from one direction. Round 2 page: https://claude.ai/artifact/2TC2ewz3tG63hVwaPUeaGo (source /mnt/project-files/between/lighting/r2/). Positions `lt-true-colours`, `lt-idle-default`, `lt-soft-light`.
- Still-maker: r2/still2.html + shoot.cjs (serve bars-engine/public on :8765 with still2.html copied in; paint patch r2/paint-edge.patch). Probe prints figure L*, room L*, darkShare (figure px under L* 10), gradP95 (steepest light edges). Round 2 mirror: figure 43 vs room 4, darkShare 0.05, gradP95 4.1 (round 1: 33, 0.58, 5.6). Walking: figure 35 vs room 20.
- Build: (1) figure-only room probe: on room entry and style change, hide the player, CubeCamera 64px HalfFloat at chest height, PMREM once, envMap on the player figure's materials only, envMapIntensity = k / luminance of the SH DC term (LightProbeGenerator), k 1 mirror and 2 walking, roughness floor 0.85. (2) wrap lighting on figure materials only: onBeforeCompile swaps the irradiance line of lights_physical_pars_fragment for saturate((N.L + 0.5) / 1.5). (3) mirror mode (garden.js setMirror): three SpotLights, penumbra 1, decay 2, distance 3.5: warm sconce left of the frame (~4), cool sconce right (~2), wide window rim behind (~8); on only while mirroring. (4) walking: waveLight as a narrow soft key (angle 0.25, penumbra 1, decay 2, ~30, distance 6). (5) paint.js uEdge (band half-width), 0.3 in the hollow (was a fixed 0.2). (6) player figure materials get userData.noPaint (wardrobe.js). (7) Mid-stride pose: setWalking holds acts.Walk at time 0 for dressed figures because the robe is baked on the Walk. Fix: a CMU mocap idle retargeted with 3d-build/autorig-mocap-2026-10-18/scripts/retarget.py (quaternions, docs/3d-math.md), the robe baked over it (blender-cloth-bake), an Idle action whenever stationary and not sitting, and a test for that rule. (8) Per-style strengths in calrunia/room-styles.js. (9) Phone frame time measured. For more direction, raise the warm sconce alone.
- Garment rule (council #375) and docs/3d-math.md apply. Reply with a hosted preview opened in mirror mode.

## Between lighting, round 3: split the difference (brief, 2026-10-24)

His note on round 2 (thread "Soften the Between lighting", 2026-10-24 04:10 UTC): "Split the difference the lighting is now too harsh and uniform". Round 1 had hard edges and one direction; round 2 reads flat and even. Round 3 sits between them. Opus thread, one art round, then a new look step (lt-mirror-look-03) and this brief's build section updated for his yes.

- Tools: /mnt/project-files/between/lighting/r2/ (still2.html, shoot.cjs, paint-edge.patch, probe.json; params key, fill, rim, fenv, wrap, edge, dist, ang). Serve bars-engine/public (branch claude/project-thread-q2xj75, paint patch applied) on :8765 with still2.html copied in.
- Starting point to try: wrap 0.25 (round 2: 0.5), fenv 0.5 (round 2: 1), warm sconce key 6 with cool fill 1.5 (ratio 4:1, round 2 was 2:1), rim 10, edge 0.25. Aim for darkShare about 0.2 to 0.3 (round 1: 0.58, round 2: 0.05) and a visible warm side and cool side on the robe. Shoot a 3-step sweep and show round 1, round 2 and round 3 side by side, mirror at dusk, moonlit and walking.
- Republish the page https://claude.ai/artifact/2TC2ewz3tG63hVwaPUeaGo from r2/soft-light.html (or a new r3 page), land the look step through board/sync_board.py, and keep the standing-idle fix in the build brief.
