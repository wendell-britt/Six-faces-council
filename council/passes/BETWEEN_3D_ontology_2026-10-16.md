# The Between in 3D: the ontology read before the build (2026-10-16)

Task: turn the Between from the 2D demo garden into a 3D space two people share, where their spirits and daemons walk
and meet, and the garden's acts happen in the space (Wendell, 2026-10-16 23:05: "a 3d game space not unlike the WAVE
room but 2 people can inhabit it and it's interactable ... Let's use the design ontology for this"). Profile loaded:
`default` (`ontology/v0.1/QUICKSTART.md`), as the callsheet names; touches Relationship, PermissionEnvelope, TrustState.
The 2D page (https://claude.ai/artifact/W4MpDsm5xnnaLGcoPNWVv6) stays as the intake.

Steer folded in from the 23:16 board read (`rc-spark` stands): "History should start when the other person joins. The
player who jumped ahead should metabolize their charge or just have it as a personal spirit."

## design_intent
A garden under the dome of the WAVE cave's model where the relationship itself stands in the middle as a creature, and two people
walk up to it, to each other's offerings and to each other's daemons. Writing stays in sheets; acting is walking
somewhere and doing something there.

## intrinsic_pleasure
Being met. Leads: the person who opens the garden. Secondary: the uncanny pleasure of watching your own daemons and
spirits meet the other person's while you talk.

## ontology_objects
| Object | In the 3D garden | Where it lives |
| --- | --- | --- |
| Relationship (the Between) | A two-lobed creature, teal and plum, on a mound at the middle | `garden/main` |
| Spark (`rc-spark`) | A plum flame in the same place before the second person joins | `garden/main.phase = spark` |
| BAR: agreement (`rc-agreements-bars`) | A plant where it was planted: seed (draft), bud (proposed), flower in both hues (agreed), drooping amber (revisit), stone (retired), soil (composted) | `items/*` with `pos` |
| BAR: offering (`rc-feeds`) | A light on a stone where it was set down; sealed charge is a dark shell with a seam | `items/*` |
| Spirit (`rc-spirits-visit`) | A fox or tortoise in its element's colour, its owner's name on it | `spirits/*` |
| Daemon (`rc-is-relationship`: the Freds are each person's daemons) | A WARP body (#328) in its owner's hue | `daemons/*` (new) |
| Person | A player body in their hue: teal for whoever started it, plum for whoever joined | live presence only |
| PermissionEnvelope | Who may act on what: only the owner calls or sends home a spirit or daemon; only the other person can say yes to an offering or agreement | page logic and `db` rules |
| TrustState | The Between's three states from satisfaction, plus stale | derived, never stored |

## mechanical_claims
- Tracked: agreements and their lifecycle, offerings and who said yes, visiting spirits and daemons, pictures shown.
- Rewarded: nothing is scored. The Between grows and brightens from agreements both hold and offerings said yes to.
- Gated: the Between changes only through the other person's yes (`rc-offer-received`, `rc-tend-alone`).
- Remembered: each act, with who and when, in its item's history; "While you were away" shows the other person's acts
  as acts, with no counts (`rc-tend-alone`).
- Permitted: walking anywhere, greeting anything, calling and sending home only your own walkers.
- Changed: stale after five days untended dims the light and greys the creature; any tending airs it out
  (`rc-stale-neglect`).
- Spark: what one person tends alone feeds the spark only. When the other joins, the starter chooses: the spark walks
  on as their own spirit, or composts. The spark's items leave the shared store for the starter's private store, and
  the Between's history starts at the welcome (`rc-spark` steer).

## aqal_attention
- UL: each person's felt sense of the relationship; pictures stay private until shown (`rc-pictures-private`).
- UR: walking up, setting down, taking in, waving: observable acts in the space.
- LL: the Between is the We; agreements are its shared meaning; consent sits on every change.
- LR: the store, the rules, the lifecycle table.
- States invited: being met, being waited for. Not converted into traits.
- Exclusions: no AI on the page; no inference about either person; no counts.

## agency_and_consent
Access is not command: the other person can greet your daemon and cannot move it. Refusal is free ("Let it pass",
"Not now", "Let it pass unopened"). Ending needs both (`rc-end-together`). The silent exit closes the garden with no
trace of who (`rc-exit`). Live presence carries position only; being there stores nothing about a person.

## evidence_and_unknowns
Built and tested in a browser with a stand-in store and two pages at once. Unknown until his play: whether walking up to
an offering reads as play or as chores on a phone, and whether watching walkers meet carries meaning for him.

## provenance_effects
Agreements and offerings keep their histories. Spark items move to the starter's private store with the choice made
(spirit or composted), so the spark's lineage stays the starter's.

## risks_and_tests
- Risk: one person uses the creature's state against the other. Test: his play, then the paper play with one willing
  person (T2 was dropped by his overrule; the build's own test is his play).
- Risk: walkers drift apart between two screens. Mitigation: each walker's path comes from its seed and the shared
  clock, so both screens draw it in the same place without messages.

## implementation_translation
One Artifact page with `db` (the garden), the live presence capability (position and a wave moment), `user` and `downloads`; the WAVE cave's
model (`bars-engine content/ontology-game/cave/rooms/wave-room/room.glb`), the WARP daemon bodies
(`3d-build/npc-gesture-2026-10-14/`) and two earth spirit rigs (`3d-build/spirit-rig-2026-10-14/glb/`) ship as the
page's files. Store shape matches the intake page, plus `daemons/*`, so the intake's garden carries over. A bars-engine
port waits until the space earns it.

## decision_or_open_authority
Nothing goes up. Every fork above is settled by a standing `rc-*` position or his steer; nothing goes to the board from this read.
