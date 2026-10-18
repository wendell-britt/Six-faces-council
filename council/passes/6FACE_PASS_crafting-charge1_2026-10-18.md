# Crafting the charge: embers and lanterns in the Between

**Run 2026-10-18**, started by the project coordinator from Wendell's note in the project chat (18 October, 18:42 UTC). The council's deliverable is a Claude Doc: https://claude.ai/code/artifact/c01e8825-0736-455a-8541-a877eb6d2627. This file is the council's record of it. Working files (brief, research, face reports) are in the project folder `council-passes/crafting-charge-2026-10-18/`.

**The ask, in his words.**

> Want to go 6 game master research on Minecraft and Roblox crafting logic. Include no mans sky as well. The goal is the alchemy of inner charge into game assets into items that can improve gameplay or customize the game world. An application is for The Between relational game. If there are other Taoist cultivation games that have crafting legs research that too

**Inputs:** research on Minecraft, Roblox, No Man's Sky and Taoist cultivation games (`research-sandbox.md`, `research-cultivation.md`); what bars-engine holds today (`bars-engine-today.md`); the Between's rulings in `council/callsheets/relationship-creature.md` (`rc-*`, `bh-*`); `ontology/v0.1/QUICKSTART.md`. `council/due.py` was not run; this is a pass, not a board read.

**Casts** (`cast.py`, three coins; the record is in the ledger):

| Agent | Hexagram | Shows |
|---|---|---|
| Shaman | 39 Impasse, changing to 8 Alliance (line 3) | The direct route is closed and you have asked nobody. |
| Architect | 2 Bearing, changing to 32 Endurance (lines 2, 3, 4) | The whole weight of this is yours, unasked. |
| Challenger | 39 Impasse, changing to 2 Bearing (lines 3, 5) | The direct route is closed and you have asked nobody. |
| Regent | 26 Reserves, changing to 41 Spending (line 3) | You have been storing this and never named the day. |
| Diplomat | 56 Passing Through, changing to 13 Fellowship (lines 1, 5) | You are a stranger here, and you will be judged fast. |
| Sage | 40 Thaw, changing to 32 Endurance (line 3) | The knot just loosened, and the window is short. |

**Daemons:** none sent. The faces drew on the research files above.

## Anchor

A worked-through charge becomes an ember the player keeps. The hearth turns one ember into one lantern, placed in the hollow. In shared space the lantern is an offer, and it counts toward the Between once, on the other person's yes. A stronger feeling never buys a stronger item, nothing is counted or compared between the two, nothing fails at random and a feeling is never used up.

## What the record already answers

- **Charge to asset:** the move fixes the element (`move-engine.ts:27-51`), so the ember stores the move and the element is derived. Intensity is look only (QUICKSTART: disclosure is not progression currency).
- **Privacy:** `rc-pictures-private` and `rc-offer-received` settle who sees what. The sealed-text leak (`store.ts:55-62`, `garden.js:447`) is a bug today and is fixed first.
- **Staleness:** his steer on `rc-stale-neglect` already rules out an item that holds it off.
- **Source of ingredients:** his message names inner charge. Failure and ash: composting is valid completion and owes no harvest.

## Shaman (39 Impasse > 8 Alliance)

Verdict: support_with_conditions (lantern slice only).
- Fill the placement hole first: one essence into the hearth, a lantern in that element's colour comes out, placed anywhere in the hollow by its maker; a given lantern is placed only after the other's yes (rc-offer-received); maker's mark, no stats (trims).
- Element is a choice: pick one or none; no element makes a clear essence with the same uses. Intensity changes nothing.
- Sheng becomes weather, not a multiplier: the Between's state at the moment of making tints the result (Grow a Garden weather).
- Rename ash: "the fire took it", never "failed"; the essence stays yours.
- Not making is play: essences sit as pots on the shelves, never decay, no reminders. Tea for two waits for slice two.
- Opposes: potency from intensity (a louder feeling buys a stronger item, disclosure as currency), settling narrowing variance (penalises the unsettled), a staleness-holding lantern (item stands in for tending, against rc-stale-neglect), recipes that need both (lock out the one resting), unlock-on-first-feeling (hides recipes behind feelings not had).
- Access: invite "Bring something you worked through to the fire; it can become a light for this place." Routes preset, symbolic (clear), private-local, nonverbal. Rest: leave pots unmade, take back or compost a lantern.
- Test: Wendell and Ari each make or decline one lantern; fails if either feels prompted to bring a stronger feeling.
- Question: does the other person see a gift's element? A shown as colour, B hidden until shown (rc-pictures-private), C never.
- Dissent seed: a feeling's strength must never set an item's strength.

## Architect (2 Bearing > 32 Endurance)

Verdict: support_with_conditions, slice 1 only.
- Each of the 15 moves carries its element pair (bars-engine src/lib/quest-grammar/move-engine.ts:27-51, e.g. Temper Action fire_metal), so element and move are one fact; store only move, derive from/to, reject a move whose from-element does not match the charge.
- BUG today: sealing is a screen effect. store.ts:55-62 returns every item row to both members; sealed is decided in the browser (garden.js:447), so a sealed charge's text already reaches the other person's device. Fix on the server first (T8).
- BetweenPrivate accepts only keys garden and spark (rules.ts:17,31); either member may update any item (rules.ts:90-93), so a maker's mark could be overwritten (T7).
- satisfaction() counts any non-agreement item received or kept (garden.js:162-168): keep made items out until co-tended.
- False binaries: private vs offered (third: essence from an unoffered charge); success vs ash (third: banked or let go by choice); sheng stronger vs weaker (third: variants kindled/tempered/kin/plain, no ranking).
- Recommends (DISSENT on slice item): tea at the hearth first, one essence from each, both yes to brew, drunk when both sit, each brew glazes a pot in the two hues.
- No randomness or ash for now; letting go returns the essences.
- Question: where does a charge become an essence? A only inside the Between, B from charge capture (cross-boundary permission), C both.
- Structure: Satchel in BetweenPrivate key "satchel" {essences:{id:{move, from, to, name, intensity|null, settled, source, state held|committed|spent|released}}}, no text field. Shared: Making {kind:"making", recipe, slots, status, yes} and Made {kind:"made", made, maker, from:[{owner, element, move}], variant, holder, status, yes, pos}. Recipes in code.
- Tests: T1 valid move; T2 B's GET has none of A's satchel, no shared row holds intensity or text; T3 essence from unoffered = offered; T4 two-person brew; T5 variants, no numeric potency; T6 satisfaction rises once on drunk; T7 maker change by other returns 400; T8 sealed text not in other's GET (fails today); T9 log has no counts.
- Dissent seed: an essence records a declared move, never a transformation, and never carries intensity or text into a shared row.

## Challenger (39 Impasse > 2 Bearing)

Verdict: support_with_conditions for the slice; oppose visible sheng bonus, intensity as potency, anti-stale lantern, joint recipes before F2, random failure.
- Stripped of image: only one claim holds alone, a person can change the look of the hollow. The item must not certify inner work (FC-05).
- Showing an element shows the feeling (Metal lantern says "fear"). The sheng bonus leaks by arithmetic: "stronger" narrows your element to two of five from theirs.
- Intensity sets the look (size, glow), never the effect. Position, record settles it.
- Joint recipes = "I need your Anger": the paper play's fail case (feeling obliged to feed).
- Anti-stale lantern undoes rc-stale-neglect. Cut.
- Random failure makes a slot machine; ash-to-soil makes compost owe a harvest.
- Schedule: sitting together tested only with two local players; Ari said not cozy or fun enough; optional crafting gets skipped (ToI).
- Take: trims, adjacency as placement, hand-made once then repeated, fires as tempo later. Leave: fusion and resale, corrupting inversion, random grades, timing minigame, mood penalty.
- Slice: set one worked charge, still sealed, at the hearth; it becomes a lantern or plant placed anywhere with the maker's mark; move and intensity set its look; colour is the maker's hue unless the maker shows the element. Tap only, preset charge without text, private, only maker removes (composts), refusing costs nothing.
- F1 first shared session (fails if neither makes a second item unprompted or either reports pressure; unlocks recipes next vs gaps 6-10). F2 Ari reads one joint-recipe card on paper (unlocks joint recipes in slice 2; Your steps). F3 desk count of wuxing pairs (unlocks hiding or dropping sheng).
- Question: crafted items first change only the look (A) or one also changes play, e.g. tea to sit together (B)?
- Dissent seed: no two-person recipe ships until the second person has been asked.

## Regent (26 Reserves > 41 Spending)

Verdict: support_with_conditions (slice one only).
- Wrong in strawman: the stale lantern (object stands in for tending; his steer on rc-stale-neglect); intensity as potency (pays bigger reported feelings, FC-04); shared recipes from stored essences (a stored essence is not present willingness: each puts their own in by their own act); the element on a gift is a disclosure (Fire is Anger), shown only by the maker's choice.
- Binding: rc-is-relationship, rc-pictures-private, rc-feeds (steer), rc-offer-received (steer: co-tended to affect the Between), rc-spirits-visit, rc-agreements-bars, rc-goal, rc-credit, rc-spark (steer), rc-tend-alone, rc-stale-neglect, rc-end-together, rc-demo-garden, bh-device-gate, bh-spark-carries, bars-engine behind sign-in. Overruled, not binding: rc-joint-checkin, rc-exit, rc-order, bh-async-first (synchronous making allowed; silent exit still carried).
- Other: Prisma migrate only; element and intensity are a new persistence purpose, private by default; the charge BAR is never used up, only the essence; no vibeulon link; assets carry source and licence, only own work and CC0 ship (QUICKSTART).
- Gates: G0 scope (scout line, board rows, rc mapping); G1 probe (recipe table + test that the source charge survives every making and no field compares the two); G2 preview (build, check, WebKit iPhone); G3 bh-device-gate (he makes something on his iPhone); G4 Ari after G3.
- Stop: anything counts or compares the two; an essence buys power; an item changes the Between without the other's yes; an asset without licence.
- Slice one, two small bowls: working a charge yields one essence named by element; the hearth makes one lantern coloured by it; the lantern sits as an offer and becomes part of the Between on the other's yes. No shared recipes, sheng, potency or failure. Slice two: tea from two bowls, each put in by its maker at the time; drinking seats both.
- Ash, if kept, is optional CompostResidue; nothing owed.
- Coinages essence, satchel, ash are the council's, expect cuts. Element canon and 15 moves inherited, never renamed.
- Question: toolbox.yaml line 7 lets CC-BY ship with credit, QUICKSTART allows only own work and CC0. A strict, B CC-BY with credit. Stricter holds until he rules.
- Dissent seed: a made item never stands in for tending; a stored essence is never a yes.

## Diplomat (56 Passing Through > 13 Fellowship)

Verdict: support_with_conditions on the first slice.
- Element on an essence leaks a feeling (Metal = Fear). Show colour, not feeling: "a green wood ember"; feeling word and move visible to maker only; a gift's element hidden by default, maker may show.
- Intensity changes character (larger, other hue), never strength.
- Joint recipes and sheng put the weight on the newcomer with an empty pouch.
- DISSENT from Regent/Shaman/Challenger: the away-lantern is a good rest route (rest allowed, not failure, FC-07).
- Settling by WAVE breath alone excludes some; a timing or drawing minigame excludes motor-limited. Let settling be time; breath, stillness or rhythm tap optional with the same result.
- Spark-phase makings go to the maker's private store at the welcome (rc-spark steer); no gifts to someone not yet joined (Flirtcraft carry-over).
- Slice: one worked charge (real, fictional or preset) becomes one ember; the hearth turns it into a lantern in the ember's colour, placed as an offer, lighting the hollow only on the other's yes.
- Copy: "When something stirs you, sit with it. What's left is a little glowing ember you keep. At the hearth you can turn embers into items for your home together, or a present." Ember, pouch, soil proposed (council's). "It went to ash." Never "your gift helped Ari".
- Ari: joins, sits on the plum cushion, no tutorial; recipes appear once Ari holds an ingredient; any route makes the same ember; can let a gift pass, rename an ember's element ("not mine"); embers leave with Ari.
- Bridge: say plainly no language model makes anything at the hearth; own work or CC0 art; credit line "The five elements and their cycles come from Chinese five-phase thought; the feelings paired with them are this game's own." Tea and gifts carry to Friendcraft.
- Tests: newcomer makes one lantern by colour-only route; second player cannot tell which route made it. Screen readers not checked.
- Question: should the hearth also take non-charge items (foraged leaves for tea) so a newcomer can make before inner work? A foraged route beside charge, B everything from charge with fictional and preset as the floor.
- Dissent seed: a gift that shows its element shows the feeling behind it.

## Sage

**Deconflicted.** The smallest whole is one ember into one lantern, built on the store that exists, with the privacy fix first. Each face's finding is kept above. The Roblox market and fusion counts, the timing minigame and No Man's Sky's random grades are set down. The Sage recommends and does not decide.

**The agreement is a flag, not a result.** All five faces supported slice 1 on conditions, and they split on what it makes: four want the lantern, the Architect wants tea. The strawman lost four parts: intensity as strength, a lantern that holds off staleness, recipes that need both people, and random failure.

**The dissents.** The Architect wants tea as the first made item. The Diplomat holds the away-lantern as a rest route against the other four. The Challenger warns that even a visible 'stronger' result between two elements lets the other person work out your feeling. The Diplomat raised a foraged route beside charge.

## Verdicts

| Face | Cast | Verdict | Main finding |
|---|---|---|---|
| Shaman | 39 Impasse, changing to 8 Alliance | Support, lantern only | Placement is the hole to fill; element is a choice; the Between's mood can tint a result as weather |
| Architect | 2 Bearing, changing to 32 Endurance | Support, slice 1 only | Store the move, derive the element; found the sealed-text leak; wants tea first |
| Challenger | 39 Impasse, changing to 2 Bearing | Support, with five cuts | A recipe that needs both reads as 'I need your anger'; no two-person recipe until Ari is asked |
| Regent | 26 Reserves, changing to 41 Spending | Support, slice 1 only | A stored ember is never a yes; five gates, ending with Ari after his phone check |
| Diplomat | 56 Passing Through, changing to 13 Fellowship | Support, first slice only | An element shows the feeling, so it stays hidden unless shown; wrote the copy and Ari's path |
| Sage | 40 Deliverance, changing to 32 Endurance | Synthesis | One ember into one lantern, privacy fix first |

## Outputs

### Positions (stand unless he flips them; rows prefixed `cc-`)

- `cc-hearth-slice`: The first crafting build is one ember into one lantern at the hollow's hearth. It has no recipes, no randomness, no failure and no counts. Why: All five faces backed slice 1 on conditions and cut the rest of the strawman. Pass: council/passes/6FACE_PASS_crafting-charge1_2026-10-18.md
- `cc-seal-fix-first`: Before anything is crafted, the sealed charge's text stops reaching the other member's device. The fix goes on the server first, then the hearth is built. Why: bars-engine src/lib/between/store.ts:55-62 returns every item row to both members and garden.js:447 hides a sealed one only in the browser, so a sealed charge's text already reaches the other person's device. rc-pictures-private.
- `cc-move-sets-element`: The ember stores the move the player chose. Its element comes from the move's element pair in move-engine.ts, and a move that does not match the charge's element is rejected. Why: bars-engine src/lib/quest-grammar/move-engine.ts:27-51 gives each of the 15 moves its pair, so move and element are one fact and storing both could disagree.
- `cc-pouch-private`: Embers live in BetweenPrivate under a new key. No shared row holds an ember's text or intensity. Why: BetweenPrivate takes only garden and spark today (rules.ts:17,31). rc-pictures-private; QUICKSTART: intimate disclosure is not progression currency.
- `cc-intensity-look`: A charge's intensity sets how big and bright its ember and lantern look and never what they do. Why: QUICKSTART: disclosure is not a progression currency. A louder feeling buying a stronger item pays for bigger reported feelings.
- `cc-element-hidden`: The element of a shared lantern is hidden from the other person unless its maker shows it. The lantern is the maker's own hue until then. Why: Showing an element shows the feeling behind it (Metal is fear). rc-pictures-private. Diplomat's copy: a green wood ember, never the feeling word.
- `cc-no-stale-lantern`: No item holds off the Between's staleness. A made item never stands in for tending. The Diplomat dissents: an away-lantern is a good rest route. Why: Your steer on rc-stale-neglect: plain neglect makes the Between stale. The Regent, Shaman and Challenger cut it; the Diplomat kept it as a rest route (FC-07).
- `cc-no-failure`: Slice 1 has no random failure. A lantern the maker lets go of 'went to ash', composts, and owes the maker nothing. Why: QUICKSTART: composting is valid completion and owes no harvest. Random failure makes a slot machine (Challenger). Never the word failed (Shaman).
- `cc-charge-only`: Everything made at the hearth comes from charge. Preset and story feelings are the floor for someone with nothing worked through. The Diplomat raised a foraged route and that stays with her as a note. Why: Your message of 2026-10-18 names inner charge as the source. A newcomer can still make an ember from a preset or a colour only, with the same result as a worked one.
- `cc-between-only`: Charges become embers only inside the Between for now. Carrying a charge in from charge capture needs its own permission record first. Why: Smallest build. Moving a charge across games crosses a privacy boundary (ontology permission envelope) and is not asked for yet.
- `cc-lantern-offer`: A lantern placed in shared space is an offer. It counts toward the Between once, on the other person's yes. Only its maker can move, take back or compost it, and the other cannot change the maker's mark. Why: Your steer on rc-offer-received: needs to be co-tended to affect the Between. Architect T7: rules.ts:90-93 lets either member update any item today.
- `cc-no-joint-before-ari`: No recipe that needs both people ships until Ari has read one recipe card. That is a later Your steps item. Why: A recipe that needs both reads as 'I need your anger', the paper play's fail case (Challenger F2). A stored ember is never a yes (Regent).

### Question (passed the reach test)

- `cc-first-made` (Sage, from the Architect's dissent): is the first made item the lantern or tea? A, the lantern (recommended, four faces): it customizes the hollow, one person can make it alone, and it ships smallest. B, tea from two bowls (Architect): it changes play, both sit and drink; it needs both people present and risks reading as 'I need your feeling' before Ari is asked. Why only he can answer: his message asks for both kinds, and the faces split on order. Why not before: there was no hearth to ask about.

### Deferred

- `cc-licence-conflict`: `council/toolbox.yaml` line 7 lets CC-BY ship with credit and QUICKSTART allows only our own work and CC0. The lantern is code-made, so this waits until an item needs an outside model. The stricter rule holds.

### Tests, dated

- **F1**, the first shared session with the slice (after his iPhone check): fails if neither person makes a second lantern unprompted or either reports pressure. Unlocks recipes next versus the hollow's gaps 6 to 10.
- **F2**, Ari reads one two-person recipe card: unlocks tea or joint recipes.
- **F3**, a desk count of wuxing pairs: unlocks whether element-pair variants can show.

## Build brief: embers and lanterns (bars-engine, Opus, on the hollow #366/#367)

See the doc's section 'Recommended first slice'. The Architect's data shape and tests T1 to T9 are in his section above (T5, T6 and the Making/tea rows are slice 2). Run a Prisma migration only if a schema change is needed; the BetweenPrivate key is likely a `rules.ts` change. `bh-device-gate` holds: iPhone-size WebKit, then his iPhone, then Ari. Lantern art is made in code. Scout line owed by the build thread (CLAUDE.md, tool ladder).

## Not checked

The No Man's Sky wiki refused every fetch, so its facts come from guides and search summaries. Several Roblox numbers come from low-quality guide sites and disagree. Taiwu details come from search summaries. No screen-reader check of the hearth was done, and nothing here has been played.
