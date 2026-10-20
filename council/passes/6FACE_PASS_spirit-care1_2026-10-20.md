# Six-face pass: spirit care (Finch, folded into spirits, daemons and the Between), pass 1

**Date.** 2026-10-20. **Called by** Wendell, in the project thread "Finch and spirit care". **Pass** 1 on the subject.

**His words.**

> I’d like to integrate the features of finch https://finchcare.com/ Into what we’re making. I’d like the 6 games masters take on it. The problems I have with it is that it’s gamification is weak and a bit too player directed and falls into the Duolingo problems of gamification. It’s a good starting point but the spirits and daemons I feel are a stronger model including the Between features where peopel can co-care for a spirit daemon and create spaces for them to inhabit.
>
> The big thing is want to add is that the spirits CAN die or be corrupted from neglect and there are shadow forces that act on what you’ve made so “clean up” practice ends up turning into self care and relationship care.
>
> The other big addition is that the spirits would be able to generate quest bars that align with the goals of the single player or the Between agreements

**Read before writing.** The Council Board was read at 21:55 UTC on 2026-10-20 (live page and `board/board_data.json` on main). Open spirit rows checked: `ss-push-down` (answered C), `sg-work-grows`, `bms-spirits-after`, `mh-pass1-stand`. The ontology loaded the `default` profile; a worker read the `game_design` profile and returned the objects cited below. Board rows checked against the record: `spirit-growth-by-training`, `rc-stale`, `rc-stale-neglect`, `iv-no-private-decay`, `cc-no-failure`, `bmt-trust-falls`, the spirit-states rows (`council/callsheets/rows/spirit-states-2026-10-16.json`).

**Casts** (`council/iching/cast.py`, three coins): Shaman 36 Nightfall, becoming 24 Turning. Architect 33 Retreat, becoming 53 Emergence. Challenger 6 Divergence, becoming 50 The Cauldron. Regent 29 Depths, unchanging. Diplomat 35 Sunrise, becoming 16 Anticipation. Sage 47 Drained, becoming 13 Fellowship.

**Scorecard.** First pass on the subject; no tests to grade.

## Anchor

Keep what Finch gets right: a small creature that notices you, and a tiny act of care that counts. Replace what it gets wrong: the player ticks their own boxes for points, and nothing real is ever at stake. In the new model a spirit has wants of its own, it can fade, be taken by shadow, or die when nobody tends it, and the Clean Up practice that saves it is the same practice that cares for the player and for the relationship.

## What exists already

- **Spirits** have a 1 to 10 satisfaction in three states, and neglect already lowers it (`ss-feral-trade`). He answered C on `ss-push-down`, so a move can unsettle any spirit, your own included.
- **The record says spirits never die.** The positions are `spirit-growth-by-training` ("No lifespan and no death; a neglected ally steps back"), the "never dies" clause of `rc-stale-neglect`, and the live Between copy ("It cannot die", `public/between/garden.js:948` in bars-engine). All three are council positions, not his words. His own picks lean toward stakes: `rc-stale` B over the council's A, `ss-push-down` C over A, and his overrule of `bmt-never-falls`.
- **The record bans the word "corrupt" for a feral spirit.** "A feral spirit is a protector held past its time, not a corrupted one" (spirit-states rows, lines 33 and 64).
- **The Between** goes stale after five days (`STALE_DAYS`, garden.js:18), and staleness never names who was away. It generates no quests. His first brief said its creatures "live in a garden made out of BarQuests" (`6FACE_PASS_relationship-creature1_2026-10-16.md:36-40`), and that part was never built.
- **Quest BARs** come from charges through a deterministic template generator (`src/lib/charge-quest-generator/generator.ts`), which already puts Clean Up first for anger, sadness and relational charges. Nothing generates a BAR from a spirit or an agreement.
- **The ontology** allows a real, irreversible consequence when it is disclosed (`disclose_irreversible_consequences`; `recoverability_does_not_erase_harm_failure_or_irreversible_consequence`). It forbids silence being treated as an automatic disposition (`silence_or_inactivity_is_not_automatic_composting`), streak and guilt pressure, rest named as a deficiency, and disclosure used as progression currency (QUICKSTART, "Intimate disclosure is not progression currency"). The inner-vessel pass already says "a streak is coercion dressed as care".

## Shaman (magenta)

**Cast: 36 Nightfall, becoming 24 Turning.** A light covered and still lit, and a return that is one line deep. The Shaman reads it as the shape of a corrupted spirit: the spirit is under the shadow, and its light is still inside.

**Observation.** What Finch gives people is the felt sense of being noticed by something small. The Shaman keeps that. Death adds grief, and grief is a real feeling the game may hold, but only if the spirit is mourned rather than lost to a meter.

**Risk.** The people who most need a care game are the ones whose weeks collapse. A spirit that dies during someone's worst week tells them something is wrong with them. That fails the Shaman's standing test.

**Recommendation.** A corrupted spirit is never simply gone; the player finds it again under the shadow. A death leaves something behind, such as a seed, an ember or a name, so the return is "one line deep" and real. The spirit asks for help in its own voice before it fades. The player never learns of the fading only after it is over.

## Architect (orange)

**Cast: 33 Retreat, becoming 53 Emergence.** Stages that cannot be skipped. The Architect reads it as a decline ladder in which no spirit goes from well to dead without passing every landing.

**Structure.** A spirit carries three separate tracks. *Satisfaction* is the existing 1 to 10 mood. *Vitality* is new: it falls with neglect and rises with care. *Shadow* is new: a load that outside forces lay on the spirit. Decline runs in stages: thriving, dimming, stale, shadowed (his "corrupted"), fading, gone. Each stage is visible on the spirit's body, and each stage lasts long enough that a player who looks in once sees it. No number is set here: the stage lengths are the council's to tune by probe, and he sees them before they ship.

**Mechanism for rest.** A *declared rest* (one tap, any length, from a phone) pauses vitality and shadow for every spirit the player holds. Silence without a declared rest is neglect. That line keeps the ontology's rule that silence is not an automatic disposition, because death is a disclosed consequence the player was told about when the spirit bonded, not a judgement read from silence.

**Mechanism for shadow.** Shadow is legible. Each shadow shows where it came from: an unworked charge, a broken agreement, or the spirit's own daemon family pushed too far. It is never shown as the player's fault.

**Mechanism for quests.** A spirit generates a quest BAR from three inputs: its own state (what it needs now), its element and daemon family, and the player's goals (his Lens goals, solo) or the pair's agreements (the Between). The deterministic charge-quest generator is the first tool to try (scout rung 2, "do we have it"). A generated BAR is an offer that needs the player's yes. Declining it costs nothing.

## Challenger (red)

**Cast: 6 Divergence, becoming 50 The Cauldron.** Two forces in one figure travelling apart. The Challenger names them: *more stakes* and *self care* pull opposite ways, and a design that pushes both to the end cancels itself.

**Anti-pattern: the Duolingo owl.** If the spirit's decline is sent as a nag ("your spirit misses you!"), this becomes exactly what he asked to escape. Fading may be seen when the player looks, and it may be sent once, in the spirit's voice, as a quest it offers. It is never a countdown or a streak.

**Anti-pattern: Clean Up as the chore.** If keeping a spirit alive needs daily Clean Up, Clean Up becomes Finch's checklist with a heavier name. The minimum care that holds a spirit steady is tiny (one real act of any size, as Finch does). Deep Clean Up, such as a 3-2-1, WAVE or a spar, is what clears shadow, and it pays more than its cost.

**Anti-pattern: arbitrary shadow.** Shadow that lands on a player who has been tending feels like weather. Shadow must come from a source the player can read and act on.

**Falsification test.** It resolves the open blocker of whether death adds stakes or only adds guilt. Simulate four players through the ladder: one who tends daily, one who is busy, one who has a bad week with a declared rest, and one who vanishes for three weeks without a word. Write down what each finds when they come back. If the vanished player's return screen makes coming back harder, the design fails. If no player's spirit ever dies, the stake is theatre. The Challenger dissents from the Diplomat below on choice: an undying spirit as an option makes death a setting, not a stake.

## Regent (amber)

**Cast: 29 Depths, unchanging.** Water fills every hollow the same way. The Regent reads it as consistency: the same rule for death in a solo spirit and a shared one.

**Non-negotiables.**
1. His words in the thread are a ruling: spirits can die or be corrupted from neglect. They flip the no-death clause of `spirit-growth-by-training` and the "never dies" clause of `rc-stale-neglect`. The rest of those positions stands, including "Staleness belongs to the pair and never names who was away".
2. Mortality is disclosed when a spirit bonds. A player never learns that spirits can die by losing one.
3. In the Between, a shared spirit's decline belongs to the pair. Either person's tending lifts it. Both are told when it reaches fading, before it can die. Nothing changes the shared spirit without the other person's yes, except the decline itself, which both agreed to when it bonded.
4. Ending a Between still composts it with no blame (the ending row stands). Ending and death are different events.
5. `iv-no-private-decay` stands for the ship and the player's own world. Spirits are the thing that can fade; the home that holds them does not.

**Phase gate.** This runs beside Chapter 1 and never blocks it. It is its own strand (`council/callsheets/spirit-care.md`) and does not touch the spirit-generator round loop, which waits on his look at v30. The first build is the Challenger's simulation, a probe before a still.

**Definition of done for the design.** The three board questions below are answered, the simulation runs, and the return-after-absence screen has copy he has read.

## Diplomat (green)

**Cast: 35 Sunrise, becoming 16 Anticipation.** The good part starts before the event. The Diplomat reads it as the return: a spirit that has been waiting for you should be glad you came back before it asks for anything.

**Bridge.** What Finch's players like should cross over intact: any act of any size counts, a creature greets you, and you can furnish its space. The Between already has the space (the cozy round names a nook, light, a creature that notices you and nuzzles). Co-care is the Between's own grammar: one person's tending waits as an offer, and the pair's yes changes the shared spirit.

**Who is excluded.** People with depression, chronic illness or caring duties, whose absence is not a choice. Declared rest covers the planned absence. For the unplanned one, the fading stage is long, the return screen welcomes before it reports, and a spirit that has died leaves a seed the player can plant, so the story goes on.

**Copy principles.** The spirit asks and never scolds. Shadow is named by its source, never by the player's failing. The word the player reads for "corrupted" is a term pass for later; in the council register his word stands.

**Non-AI path.** The quest BARs come from templates first, so the whole loop works with no model. The Portland community's allergy to AI is a reason to keep it that way.

**Dissent.** The Diplomat would let a player choose an undying spirit at bonding, for the players above. The Challenger disagrees. The question goes to the board.

## Verdicts

| Face | Verdict |
|---|---|
| Shaman | Death is allowed if it is mourned and leaves something; corruption keeps the light inside. |
| Architect | Three tracks (satisfaction, vitality, shadow), a staged decline, declared rest, legible shadow, spirit-made BARs as offers. |
| Challenger | Stakes and self care pull apart; no nag, tiny minimum care, legible shadow; test by simulating four returns. Dissents on optional death. |
| Regent | His words are a ruling; disclose at bonding; the pair owns a shared decline; separate strand beside Chapter 1. |
| Diplomat | Keep Finch's warmth and any-size acts; welcome before report; templates first; dissents toward an undying choice. |

**Dissent check.** Not unanimous. The Challenger and the Diplomat split on whether a player may choose a spirit that cannot die. The Shaman and the Challenger both warn that death can become a guilt meter, and the Architect's declared rest is the council's answer, which only the simulation can test.

## Sage (teal)

**Cast: 47 Drained, becoming 13 Fellowship.** The explaining continues and the basin is dry, then two going the same way. The Sage reads it as a warning against designing the whole system on paper, and a pointer to the Between, where two people already walk the same way.

**Synthesis.** The Shaman gives the meaning of death: mourned, with something left behind. The Architect gives the machine: three tracks, a ladder, declared rest, legible shadow and spirit-made BARs. The Challenger gives the test and the two anti-patterns that would turn this back into Finch. The Regent gives the rules that keep the Between fair and the strand out of Chapter 1's way. The Diplomat gives the bridge from Finch and the people a mortal spirit could hurt.

**Smallest coherent whole.** One spirit, one decline ladder, one shadow source, one Clean Up that clears it, and one spirit-generated quest BAR. It is proved first as a simulation of four players' returns, then as one spirit in the Between after the cozy round lands.

**Dissent kept.** Optional death (Challenger against Diplomat).

## Positions (stand unless he flips them)

Rows `sc-*` in `council/callsheets/rows/spirit-care-2026-10-20.json`.

## Questions (passed the reach test)

1. **`sc-undying`** Can a player keep a spirit that never dies? (owner Regent)
2. **`sc-after-death`** What is left when a spirit dies? (owner Shaman)
3. **`sc-shadow-what`** What are the shadow forces in the story? (owner Architect)

Each carries options, consequences, why only he can answer and why it was not asked before in the rows file.

## Tests set (dated 2026-10-20)

- The four-player simulation runs and prints each return. Pass: the vanished player's return welcomes before it reports, and at least one simulated spirit can die.
- A generated quest BAR for a solo spirit cites one of his Lens goals, and one for a Between spirit cites one agreement.

## Recommended next move

Build the four-player simulation as a small script in this repo (`council/spirit-care/sim.py`), with the decline ladder as data, on Opus in a fresh thread, while his three answers come in. It is reversible, cheap, and it decides whether the stakes add care or guilt before any art or bars-engine work.

## Record block

- Question: fold Finch into spirits, daemons and the Between; mortal spirits, shadow forces, spirit-generated quest BARs.
- Ruling in his words (chat, 2026-10-20 21:51 UTC): "The big thing is want to add is that the spirits CAN die or be corrupted from neglect and there are shadow forces that act on what you’ve made so “clean up” practice ends up turning into self care and relationship care." Flips the no-death clause of `spirit-growth-by-training` and the "never dies" clause of `rc-stale-neglect`.
- Verdicts: as in the table.
- Board rows: `sc-ruling-mortal`, `sc-ladder`, `sc-rest`, `sc-shadow-legible`, `sc-cleanup-care`, `sc-spirit-bars`, `sc-between-decline`, `sc-word`, `sc-strand`; questions `sc-undying`, `sc-after-death`, `sc-shadow-what`.
- Casts as in the header. Workers: two research readers (about 200,000 tokens between them).
