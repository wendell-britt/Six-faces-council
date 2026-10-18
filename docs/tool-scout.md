# The tool ladder: check what exists before building

Wendell, 2026-10-18, after the council learned that free rigging and motion tools (Rigify, mocap libraries, Mixamo)
existed while we hand-built rigging and animation: "Why haven’t we been using the third option before? Essentially
inwant to make sure we are getting smarter about using tools that increase our throughput and increasingly higher
quality and lower token costs." And: "I do think this was supposed to be the benefit of using something like
Ponytail. Essentially a hack of ponytail but for asset pipeline and 3d production".

Ponytail (github.com/DietrichGebert/ponytail, MIT) is a coding-agent skill that stops the agent at the first rung that
holds before it writes code: does this need to exist, is it already here, does the standard library do it. This is the
same idea for assets, 3D and game code, where the "standard library" is the free tools and asset libraries in
`council/toolbox.yaml`.

## The ladder

Before a thread builds something new (a loop round's `builds`, a feature, a model, a rig, an animation, a solver, a
material, a game system), it climbs these rungs and stops at the first one that holds:

1. **Does it need to exist?** It answers his ask or the round's `check`. If not, drop it.
2. **Do we have it?** An earlier round, another strand, bars-engine, sprout, or `/mnt/project-files/3d-build/`.
3. **Does a known tool do it?** `python3 council/tools/scout.py <the job in a few words>` lists the fitting tools in
   `council/toolbox.yaml`, one line each. Adapting a tool beats building from scratch even when the fit is partial.
4. **Does an unknown tool do it?** Only when rungs 1 to 3 fail and the build is bigger than one round: one Sonnet
   worker searches the web and returns at most five candidates, each with what it does, its licence and its cost.
   Keepers go into `council/toolbox.yaml` in the same pull request, so the next thread finds them at rung 3.
5. **Build it.** Say in one line why rungs 3 and 4 did not hold.

## Building it small

When the ladder reaches rung 5, or adapts a tool at rung 3, the rest of Ponytail's prompt applies, translated for
assets, 3D and game design:

- **List what the round must reach before starting.** The exported GLB, the viewer page, the game route on
  bars-engine, the callsheet, the board step. That list is the scope. Extra variants, options and "for later" dials
  are not.
- **Prove it the cheapest way first.** A number from a probe script beats a render, one still beats a sheet, a sheet
  beats a video. Go up a step only when the cheaper proof passes and his check needs the next one. Renders and videos
  cost a 3D thread the most to read back.
- **Never cut** what his check asks for, rig-readiness (four feet, no props on living creatures), the licence rules
  below, the route working in the game, and accessibility on anything a player touches.
- **Every build leaves its check.** A probe script, a test or a measured number that the next round can rerun without
  rereading the round (the J5 rounds' `probe.mjs` and the J5d cuff gap are the pattern).
- **The report ends with what was not checked** and any risk he should know, in one or two lines.

## Gates and licences

- A tool with `status: gated` needs money or an account. Its first use is a step for Wendell on the board's Your
  steps tab, never a sign-up by the thread (money and accounts are reserved, `loop-auto-gate`).
- CC0, MIT and Apache outputs ship. CC-BY ships with a credit line. SA and GPL assets do not ship (`cc-store-safe`).
  A tool whose own code is GPL (Blender, Rigify) is fine: what it makes is ours.
- Generated meshes follow docs/asset-generation.md.

## Recording it

One `scout:` line names the rung it stopped at and the tool: `scout: 3, rigify (fit the quadruped metarig)` or
`scout: 5, no tool rigs metaball bodies; rigify needs a mesh first`. It goes on the loop round
(`next_round.py start|finish <strand> <n> --scout "..."`, and `start` prints the matching tools), in the pass's
Architect section when a pass proposes a build, and in the pull request body otherwise.

## What it costs

Rung 3 is one command and a few hundred tokens. Rung 4 runs in a worker, so its reading never enters the thread,
and it runs once per kind of job, not once per round. A rejected tool stays in the toolbox as `rejected` with the
reason, so nobody searches for it again.

The first sweep of the open strands is `council/research/2026-10-18-tool-sweep.md`.
