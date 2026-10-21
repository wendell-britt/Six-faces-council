# Calrunia: one world, many places

Wendell, 2026-10-21 01:31 UTC, overruling `ba-worlds-stored`: "We can start building a structure that holds all of them. The between is a subfeature of an emergent calrunian world along with root and the sprout game  game"

## Where it stands

- Pass `calrunia-world1` (council/passes/6FACE_PASS_calrunia-world1_2026-10-21.md): one world, many places, one passport. Eight `cw-*` positions; `cw-front-door` on the board.
- Registry: `calrunia/world.yaml` lists every place, its engine and repo, and the passport and currency.
- Qi is a meter and the vibeulon its currency (`cw-qi-meter-scales`, replacing part of `ba-qi-is-light`).
- `cw-chapter1-first` overruled 2026-10-21 01:48: Chapter 1 is the world's first route, not a gate in front of it. Pass `chapter1-calrunia1` (council/passes/6FACE_PASS_chapter1-calrunia1_2026-10-21.md): six `c1w-*` positions, question `c1w-taste-depth`, and the `chapter1` route in `calrunia/world.yaml`.

## Brief for the next thread (bars-engine, Opus)

The passport contract, no art round, so `hx-looks-gate` is untouched. Read this sheet, the pass's "Build brief", and `calrunia/world.yaml`. Build: `schema/passport.schema.json` with fixtures and a contract test (pattern: the board-save contract); a guest passport in the browser that reads today's `oag.vessel.v1` and the cave's spirits into the passport shape without moving data; a Prisma model for the signed-in passport beside the Between's tables, migrations only, with claim-on-sign-in. Leave sprout as it is. Give a Vercel preview link. If `cw-front-door` is answered first, store the last place only if he picks C.

## Passport (bars-engine #410, merged 2026-10-21)

- Position, standing unless Wendell flips it: the passport field owners are spirits=cave, hand=sprout, and qi/vibeulons/embers=vessel. Every place reads every field. `cw-front-door` was answered A (the ship), so no last place is stored.
- Built: schema, fixtures (including a Chapter 1 one), contract test, guest fold, `Passport` model, `/api/passport` claim. `/passport` is a developer view linked from `/admin/games` only; players never see a passport page (Wendell, 2026-10-21: "It looks terrible and I have no idea how someone would use it").
- Not yet done: the live W1 run needs a signed-in player. The API answers 401 on production, as designed.

## Open

- `cw-front-door`: ship, Sprout's settlement, or wherever you last were.
- Tests W1 (a spirit survives the guest-to-sign-in and cave-to-Between trip) and W2 (no place writes a field another owns).
- Not read: sprout `docs/decisions/calrunia-and-domains.md`, bars-engine branch `codex/wip-inner-garden-calrunia`, the hd-wallet vibeulon plan.
- `world.yaml`'s vessel pointer (`content/ontology-game/cave/vessel.js`, `oag.vessel.v1`) exists only on bars-engine branch `claude/inner-vessel-build-vqaqgw` (#399), not on main; the passport thread should read it there or fold the cave's `oag.spirits.v1` alone until #399 merges (found 2026-10-21, pass chapter1-calrunia1).
