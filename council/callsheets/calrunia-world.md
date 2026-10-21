# Calrunia: one world, many places

Wendell, 2026-10-21 01:31 UTC, overruling `ba-worlds-stored`: "We can start building a structure that holds all of them. The between is a subfeature of an emergent calrunian world along with root and the sprout game  game"

## Where it stands

- Pass `calrunia-world1` (council/passes/6FACE_PASS_calrunia-world1_2026-10-21.md): one world, many places, one passport. Eight `cw-*` positions; `cw-front-door` on the board.
- Registry: `calrunia/world.yaml` lists every place, its engine and repo, and the passport and currency.
- Qi is a meter and the vibeulon its currency (`cw-qi-meter-scales`, replacing part of `ba-qi-is-light`).
- Chapter 1 comes first; until it ships, world work is the registry and the passport only (`cw-chapter1-first`).

## Brief for the next thread (bars-engine, Opus)

The passport contract, no art round, so `hx-looks-gate` is untouched. Read this sheet, the pass's "Build brief", and `calrunia/world.yaml`. Build: `schema/passport.schema.json` with fixtures and a contract test (pattern: the board-save contract); a guest passport in the browser that reads today's `oag.vessel.v1` and the cave's spirits into the passport shape without moving data; a Prisma model for the signed-in passport beside the Between's tables, migrations only, with claim-on-sign-in. Leave sprout as it is. Give a Vercel preview link. If `cw-front-door` is answered first, store the last place only if he picks C.

## Open

- `cw-front-door`: ship, Sprout's settlement, or wherever you last were.
- Tests W1 (a spirit survives the guest-to-sign-in and cave-to-Between trip) and W2 (no place writes a field another owns).
- Not read: sprout `docs/decisions/calrunia-and-domains.md`, bars-engine branch `codex/wip-inner-garden-calrunia`, the hd-wallet vibeulon plan.
