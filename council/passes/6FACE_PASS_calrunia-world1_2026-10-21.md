# One Calrunian world: a structure that holds every place we have built

**Run 2026-10-21**, started by the project coordinator after the board pull of 01:31 UTC (`council/ledger/2026-10-21-pull-013156.json`), where Wendell overruled `ba-worlds-stored`. Pass `calrunia-world1`, the first on the world as a whole. Callsheet: `council/callsheets/calrunia-world.md`. Registry: `calrunia/world.yaml`. Ledger: `council/ledger/2026-10-21-calrunia-world1-pass.json`. Rows: `council/callsheets/rows/calrunia-world-2026-10-21.json`.

**The ask, in his words** (steer on `ba-worlds-stored`):

> We can start building a structure that holds all of them. The between is a subfeature of an emergent calrunian world along with root and the sprout game  game

Also from the same pull, his steer on `ba-qi-is-light`, which stood but asked for more:

> I think it should be a meter and should be a currency like the scales one I’ll eights cradle. I see this as how we can integrate vibeulons into the game world

**Inputs:** `mh-calrunia-hall` ("Calrunia is Sprout's world", 2026-10-03), the callsheets for the Between, Root, the inner vessel, spirit care, the cave and its levels, the Chapter 1 demo, element settings and the engine slice; the `hx-*` and `ba-*` rows; bars-engine's `.specify/specs/six-guide-calrunia-orientation/` (the Orientation Stack, BARs as the membrane, "the player must not see two Calrunias"); the design ontology (`ontology/manifest.yaml`, game_design profile: PlayUnit nesting, encounter contract families, BAR portability, constitution #5, #7, #14). One worker read them; nothing it read is quoted beyond what the faces cite.

**Casts** (`cast.py`, three coins; line values in the ledger):

| Agent | Hexagram | Shows |
|---|---|---|
| Shaman | 39 Impasse, changing to 31 Mutuality (line 4) | The direct route is closed and you have asked nobody. |
| Architect | 55 Fullness, changing to 22 Adornment (lines 4, 6) | This is at its peak and you are saving some of it. |
| Challenger | 30 Burning, changing to 33 Retreat (lines 1, 5) | You keep saying the same true sentence, and it is consuming its subject. |
| Regent | 59 Dispersal, no changing lines | What you were holding rigid is coming apart. |
| Diplomat | 56 Passing Through, changing to 50 The Cauldron (line 2) | You are a stranger here, and you will be judged fast. |
| Sage | 46 Ascent, changing to 48 The Well (line 5) | This is growing at a rate you cannot see day to day. |

**Daemons:** none sent.

## Scorecard

First pass on the subject; nothing to score. The test this pass sets is at the end.

## Anchor

Calrunia is one world, and every game we build is a place in it. A player is one person across all of them: the same spirits, the same hand, the same qi.

## What the record already answers

- **Which world.** `mh-calrunia-hall`: Calrunia is Sprout's world, not only the ship-school of the book.
- **The ship.** `iv-*`: places are reached from the ship, the ship does not travel to them; it is a living ship you have a relationship with. `ba-barn-in-ship`: your spirits' own space is inside your ship.
- **Spirits.** `rc-spirits-visit`: a spirit visits the Between and stays its owner's. `sc-ruling-mortal`: spirits can die of neglect. `hx-carry-feeds-spirit`: a card put back three times wakes a wild spirit of the family of the daemon holding it.
- **The membrane.** bars-engine's Calrunia spec: a BAR is outer-world reality made playable inside Calrunia, and there must never be two Calrunias.
- **The order.** Chapter 1 ships first for the Kickstarter (chapter1-demo.md); the engine question waits for it (council #302); `hx-looks-gate` holds every strand to his looks.

## Shaman — 39 Impasse, becoming 31 Mutuality

The direct route is closed and nobody was asked. For two weeks each place grew as its own game, and every time two of them touched (Ari's barn, the dance on Root, the procedural worlds) the council filed the touch on someone's callsheet and moved on. His steer says the touch is the point. What moves underneath is one person walking between the places of one home: the farm where they were pulled in, the cave inside them, the hollow they share with one other person, the floor where two bodies practice, and the ship that carries them home. The felt sense is continuity. The spirit you woke in the cave is the one that follows you onto Root and sits in your barn at night. Mutuality is the becoming: the world exists between players as much as inside each one, which is why the Between is a place two ships make, not a place one person owns.

## Architect — 55 Fullness, becoming 22 Adornment

What must be true in the machine is small. The binary on the table is "one engine" against "many games". It is false, and #302 already refuses to choose an engine now. The third position: **one world, many places, one passport.**

1. **Places.** Each game is a place with its own engine and repo: the vessel, Sprout's settlement, the cave, Root, the Between, later one land per element. Each is typed by its dominant encounter family (vessel recovery, Sprout training, cave transformational, Root contest, Between relational). `calrunia/world.yaml` registers them.
2. **The passport.** One player record crosses places, and nothing else does: player, spirits (with their care state), the hand of cards and BARs, qi, vibeulons, embers, places reached. A place reads it on entry and writes back on exit (PlayUnit nesting: a place visit is a Session; the passport is its ContinuationRecord). It lives in bars-engine Postgres behind sign-in, beside the Between's tables; a guest passport lives in the browser and is claimed at sign-in. Constitution #5 holds: what the passport tracks is what is real in Calrunia.
3. **The currency.** His steer settles `ba-qi-is-light` the other way: qi is a meter that practice fills, shown as the light and weather of where you are, and condensed qi is the vibeulon, spent like Cradle's scales. The vibeulon is the one currency every place honours. Gold stays friendcraft's and is minted by grounding.
4. **The map grows.** A place is on a player's map once it is built and they have entered it. A Between appears when two people make one. That is what "emergent" means in the machine.

Fullness saves some of it: none of this is runtime work before Chapter 1 except the passport's first write.

## Challenger — 30 Burning, becoming 33 Retreat

The same true sentence, said until it consumes its subject: "it's all one world" can eat the Chapter 1 demo. What breaks: a world-structure build that starts now pulls sprout, the cave, the vessel and the Between into one refactor while #399 waits on his note, the cave game PRs wait on his plays, and the demo waits on a second player. Self-inflicted risk: two state stores already disagree (the Between in Postgres, the cave and vessel in `oag.*` localStorage), and a third would be worse than either. Scheduling truth: the structure is a registry and a schema until Chapter 1 ships. Retreat is the becoming: build the contract, not the world.

## Regent — 59 Dispersal

What was held rigid is coming apart, on purpose: `ba-worlds-stored` filed the worlds away and he dissolved that. What must be preserved through the dispersal: Chapter 1 first; `hx-looks-gate` per place, so the world never becomes a way round the gate; the Between's consent rules (nothing changes without the other's yes); spirits stay their owner's; no global rank, so the passport carries no level that one place can use to rank a player in another. The obligation: one Calrunia, never two, which bars-engine's own decision already demands.

## Diplomat — 56 Passing Through, becoming 50 The Cauldron

A stranger here is judged fast. A Kickstarter backer arrives through Chapter 1 and will judge the world by whether the spirit they woke is still theirs on the next screen. Ari arrives through the Between and should find it is a doorway into a larger world, not a hollow with no outside. The Portland community's allergy to AI matters here too: the passport is plain data a player can read, and every place plays without a model. The Cauldron: the structure is the vessel that holds the places while they cook together.

## Verdicts

| Face | Verdict |
|---|---|
| Shaman | One person walking between the places of one home; the Between is made by two ships. |
| Architect | One world, many places, one passport; qi a meter, vibeulons its currency. |
| Challenger | Build the contract, not the world, until Chapter 1 ships. |
| Regent | Keep Chapter 1 first, looks-gate per place, consent, no rank. |
| Diplomat | The passport is the backer's continuity and is readable without AI. |

## Dissent check

The Shaman and the Architect want the front door named now: is a player's daily entry the ship or Sprout's settlement? The record splits. `iv-*` makes the ship the hub; `mh-calrunia-hall` makes Calrunia Sprout's world, and Chapter 1 opens in Sprout. The Challenger says the door can wait until after the demo. The reach test sends it back to the Architect, who finds no ruling that settles daily entry and no fact the record holds; it is his preference, and it changes the registry's root and the first screen after the demo. It goes to the board as `cw-front-door`.

## Sage — 46 Ascent, becoming 48 The Well

The smallest coherent whole is the registry, the passport and the currency; everything else is already built or already planned, and each piece now has a place to stand. The five resolve in this order: the Regent's guards first (Chapter 1, looks, consent, no rank), then the Challenger's limit (contract only), then the Architect's three parts, with the Shaman's and Diplomat's test as the measure: the spirit you woke is still yours on the next screen. The Well: a world that many places draw from without exhausting it.

## Outputs

### Positions (stand unless he flips them)

- `cw-one-world`: Calrunia is the one world, and every game is a place in it with its own engine and repo (Architect, Shaman; mh-calrunia-hall, #302).
- `cw-passport`: one player record crosses places and nothing else does; Postgres behind sign-in, guest store in the browser (Architect, Diplomat).
- `cw-qi-meter-scales`: qi is a meter, the vibeulon is condensed qi spent like Cradle's scales; supersedes "never a meter or a currency" in `ba-qi-is-light` per his steer (Architect, Regent).
- `cw-between-two-ships`: the Between is a place two ships make, existing only between two passports (Shaman, Regent; rc-spirits-visit, ba-barn-in-ship).
- `cw-root-training-ground`: Root is the training ground for practice with another body, sparring, push hands and partner dance; it raises qi and grants no rank (Shaman, Regent; ba-formation-card steer).
- `cw-cave-inner-land`: the cave is the land inside you, where your daemons keep their chambers (Shaman; dmt-*, cave-levels).
- `cw-emergent-map`: a place is on your map once built and entered; a Between appears when two people make one (Architect).
- `cw-chapter1-first`: until Chapter 1 ships, world work is the registry and the passport only, the engine stays deferred, and `hx-looks-gate` applies per place (Challenger, Regent).

### Question

- `cw-front-door` (Architect, Shaman): where does a player step into Calrunia each time they play? Options and consequences are on the board.

### Tests

- **W1** (after the passport is built): a guest wakes a spirit in the cave, signs in, opens the Between, and the same spirit is theirs there. Pass if the spirit's name and care state match.
- **W2** (desk): every place in `calrunia/world.yaml` names what it reads from and writes to the passport. Pass if no place writes a field another place owns.

## Build brief

One bars-engine thread on Opus, no art round, so `hx-looks-gate` is not touched:

1. `schema/passport.schema.json` with fixtures and a contract test, the same pattern as the board-save contract.
2. A guest passport in the browser that folds today's `oag.vessel.v1` and the cave's spirits into the passport shape, without moving any data.
3. A Prisma model for the signed-in passport beside the Between's tables, with a claim-on-sign-in path. Migrations only, never `db push`.
4. No change to sprout. Chapter 1's end will write its hand and woken spirits to the guest passport once the demo is done.

## Not checked

The sprout, root-game and calrunia-3d repos were not opened; sprout's `docs/decisions/calrunia-and-domains.md` and bars-engine's branch `codex/wip-inner-garden-calrunia` were not read. Whether vibeulons as Cradle's scales fit the hd-wallet plan for vibeulons is not checked.
