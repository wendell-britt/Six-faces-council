# Depth Over Flatland — Owner Decision

**Date:** 2026-10-24

**Status:** Binding v0.1 ontology decision (board position `sd-depth-rule`, stood by Wendell on 2026-10-24,
`council/ledger/2026-10-24-pull-023536.json`)

**Scope:** Every player-facing game surface: scenes, menus inside a game world, the ship, the boat, caves, the board's game
views

**Does not authorize:** removing plain records, admin pages or accessibility text alternatives; a surface may keep a plain
fallback for reading or assistive technology as long as the play surface follows this rule

## Question resolved

How should the games show what a player carries and what they have done, after the ship dock (bars-engine #399) and the studio
boat deck (bars-engine #429) were rejected as dashboards?

## His words

Wendell, 2026-10-24, rejecting the dock:

> "The grid and gauge panel I didn't enjoy ... It was quite sophomoric and not particularly context aware."
> "We need a design language that consistently creates immersive experiences."
> "either needs to be an inviting image like the current art direction for the council board as spirit boat OR it needs to be
> an explorable space like the cave of lessons. It need to bring people deeply and emotionally into the world and we keep
> making flat dashboard surfaces."
> "The shadow of the diplomat is flatland ... it's also boomeritis and it's the shadow of integral green. Our job is to bring
> depth back into green. Depth and altitude as a way to pull them out of their flattened world via play."

## Decision

1. **Every play surface is an inviting image or an explorable space**, never a grid, gauge or panel.
2. **Data shows as world state.** Nothing the game tracks is drawn as a number, bar or meter on the play surface. Energy shows
   as size and light; work done shows as chambers grown, lamps lit, creatures living there; what a player carries hangs, sits or
   travels in the world. (Mechanics still claim reality, principle 5; this rule governs how they are shown.)
3. **Haze, scale and light lead inward.** A scene has a foreground, a threshold and a far place, so the eye travels into it.
4. **The world grows as inner work is done.** Inner work adds places and life; it never fills a meter.
5. **Every scene plays in 2D and 3D**, the way the asset pipeline works (a painted 2D reveal and an explorable 3D place can
   tell the same beat).
6. **Every named inspiration gets real reference images before a mood still**, and code waits on Wendell's yes to the still.

## Relation to the constitution

This is a design rule under the fifteen principles, not a sixteenth. It applies principle 8 (play precedes complete
understanding) and principle 9 (mystery rewards inquiry) to how state is shown, and names the Diplomat's shadow (flatland) as
the failure it guards against.

## First application

The living ship at bars-engine `/calrunia/arrive` (brief "Living ship build", Six-faces-council
`council/callsheets/inner-vessel.md`): the island's size and light are inner energy, spirits live on it, a chamber grows at its
rim for each ember of inner work, and Chapter 1's cards hang by the den's door. No count is on screen.
