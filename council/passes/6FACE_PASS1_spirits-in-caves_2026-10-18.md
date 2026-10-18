# Six-face pass 1: spirits in the caves (2026-10-18)

Called by the coordinator on Wendell's message of 2026-10-18 23:01 (project chat). His words: "The spirit of anger should be
pulling in a cloud spirit of the type of the daemon they are in front of. ... The features inside of the big mind cave should
also be in the starting cave. The choice to doing W.A.V.E. with spirits inside that first cave should be an integration of the
sitting down version while inside the cave. Both waves should be integrating the spirit proof spirits in the order of their
unfolding from gas to core to hologram to creature to standing ally. We need to think through on the demo how to showcase these
type of spirits. We'll also need the ability to save spirits between runs and continue to cultivate them over time. Choosing a
spirit load out should be something you can do in the intro cave". First pass on this subject. Ontology: game_design profile
(QUICKSTART read; principles 5, 10, 11 and the WAVE boundary used). His figure notes in the same message (shoulders, stand on
stop, a run clip) go to the thread changing the player figure's animation, not this pass.

Casts (`cast.py --json`): Shaman 6 Divergence (becomes Bite); Architect 60 Measure (becomes Drained); Challenger 12 Stalemate;
Regent 58 Banter (becomes Following); Diplomat 56 Passing Through (becomes Feeding); Sage 14 Noon (becomes Estrangement).

## Scorecard
No earlier pass on this subject. Inherited and standing: `sg-body-from` A (the daemon picks the family), `sg-holo-stages`
(gas at level 1, core at 3, hologram at 5), `dmt-trainer` A (the daemon is never fought; its family's wild spirit is sat with),
`dmt-ally-honored` (the ally stands in its daemon's honored pose), `dmt-same-order`, `sg-romp-four-feet`.

## Anchor
A spirit is born of meeting a daemon, wears that daemon's family, and grows by being sat with in W.A.V.E.; the player keeps it
across runs and chooses which ones walk with them.

## What exists (worker map of bars-engine main 7a81014)
The meeting spirit (`bigmind.js` `felt` :1268) is an orb in its element's colour (`cave.js` `buildSpirit` :1572); nothing in the
game has a family or a stage. Big Mind keeps spirits in `oag.bigmind.v1`; the Cave of Lessons keeps them one visit. Spirits join
a sitting only one at a time ("sit with it again"). No loadout exists. The art exists: per family, base and element, five GLBs,
`gas`, `core`, `hologram`, `creature`, `ascended` (`/mnt/project-files/3d-build/spirit-shellback-2026-10-14/`, about 600 KB each).

## Shaman (6 Divergence: going deeper and pushing forward at once cancel)
**The cloud should arrive before the name.** When the feeling is chosen, the daemon's own gas drifts from its body to the spirit
at your side; the player sees kinship without being told it. **Growth must be felt as company, not earned as score.** A sitting
that ends in no shift still counts as time spent together (principle 10: the player authors the meaning). **The cast warns
against doing both at once:** the first slice is the cloud alone, then the unfolding.

## Architect (60 Measure: say where the edge is)
**One store, one shape.** `oag.spirits.v1` holds every spirit: id, name, element, family (daemon id), sittings, stage, born
(where and when), and a lineage list of sittings (principle 11). Big Mind's `voices[id].spirit` and `save.spirits` read from it.
**Stage is derived from sittings**, never stored apart: gas 0, core 2, hologram 4, creature 6, standing ally 8 sittings, which
keeps `sg-holo-stages`' 1-3-5 spacing as levels 1, 3, 5, 7, 9. **The edge:** three spirits walk with you (`SPIRITS_SHOWN` is
already 3); the rest rest in the WAVE room. **Assets:** the gas is drawn in three.js as motes (no download); core and hologram
come next from the GLBs, each family and element fetched on demand and compressed (the export check, not a page budget).

## Challenger (12 Stalemate: seeking one game, wearing the face of another)
**The risk is a collection game wearing a healing game's face.** A loadout and levels pull toward grinding sittings. Two guards:
one sitting counts once per spirit per run, and nothing is locked behind a stage (the ally form changes how it walks with you,
not what you may do). **Falsification test T1:** after the first slice he can say, unprompted, which daemon a spirit came from by
its cloud alone.

## Regent (58 Banter: the exchange is the whole of it)
**Order of build, one pull request each:** 1, the family cloud for the meeting spirit, with family saved; 2, W.A.V.E. unfolds a
spirit one stage per sitting, with the five forms; 3, one shared save and the loadout in the intro cave; 4, Big Mind's features
in the starting cave and the sitting-down W.A.V.E. with the loadout's spirits around you; 5, the demo showcase on his answer.
**Done for slice 1:** the hallway spirit is a cloud of the chamber daemon's family in the felt element, saved with its family,
bigmind-test and cave-test pass, a preview link, and what was not checked.

## Diplomat (56 Passing Through: a stranger, judged fast)
**A first-time player meets the spirit in the first hallway**; the cloud must read in a second on a phone. Keep the label, keep
reduced motion (the motes hold still and fade in). **Damaged Self and Emotional Body** have no family built yet; their spirits
stay plain element clouds until those rounds, so no one sees a broken shape.

## Verdicts
| Face | Family cloud | Unfold by sittings | One save, loadout of 3 | Demo showcase |
|---|---|---|---|---|
| Shaman | yes, cloud first | yes, no-shift counts | yes | his call |
| Architect | yes, motes in code | yes, 0/2/4/6/8 | yes | his call |
| Challenger | yes, T1 | yes, once per run | yes, nothing locked | his call |
| Regent | slice 1 | slice 2 | slice 3 | slice 5 |
| Diplomat | yes, reads in a second | yes | yes | his call |

## Dissent check
Unanimous on the positions, which is a flag: every face leaned on records already decided. The one open split is the showcase,
where the Shaman leans to an elder spirit already grown and the Architect to a gallery of forms; that goes to him.

## Sage (14 Noon: a lot here, all of it visible)
Kept: the Shaman's cloud-before-name and no-shift-counts, the Architect's store and sitting thresholds, the Challenger's guards and
T1, the Regent's order, the Diplomat's first-hallway read and plain clouds for unbuilt families. Dropped: nothing. The Sage does
not decide the showcase.

## Outputs
Positions (stand unless he flips them; rows `council/callsheets/rows/spirits-in-caves-2026-10-18.json`): `sic-family-cloud`,
`sic-unfold-by-sitting`, `sic-one-store`, `sic-loadout-three`, `sic-first-cave-sitting`.
Question: `sic-demo-showcase`.
Tests: T1 (Challenger) at his play of slice 1; T2, after slice 2, a spirit he has sat with twice shows its core and he can say why.
Not done in this pass: no daemon reports were run; no ledger record yet (the board read that records his answer writes it).
