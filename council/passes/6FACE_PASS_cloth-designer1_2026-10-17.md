# Six-face pass: cloth through a fashion designer's eyes (pass 1), 2026-10-17

**Called by** Wendell, in the J5 cuffs thread, 01:36, after the round 10 cuffs (bars-engine #359): *"Better but still
bad. They are moving like solid objects and not clothes. Let's do some 6 game master research on deft ways to render
clothes in environment similar to ours in the genre we are exploring and expanding into. If you were a fashion
designer who decided they wanted to learn how to create clothes for games what intuitions and principles for how real
cloth moves would be violated and what advantages does digital first have for giving the illusion of moving
clothes?"*

**Subject.** The J5 robe (skirt as live cloth in `cloth.js`, sleeves and cuffs skinned) and the cloth postmortem,
https://claude.ai/artifact/Srk4nKN4GdbsriodvfSfgn, which recommends an XPBD rebuild with painted limits. This pass
adds the art-direction side the postmortem left out. The write-up he reads is that doc's second tab, "Through a
designer's eyes". First pass on this subject.

**Ontology.** Not loaded: this pass designs no mechanic, it judges how a garment reads in motion
(docs/ontology-in-flows.md).

**Casts** (`cast.py --json`, kept in the ledger record): Shaman 17 Following, becoming 54 Home Field Advantage;
Architect 47 Drained, becoming 43 Unsaid; Challenger 29 Depths, becoming 28 Overload; Regent 1 Unbroken, becoming 10
Footing; Diplomat 5 Hosting, becoming 32 Endurance; Sage 26 Reserves, becoming 19 Spring.

**Research.** Two researchers on the middle model, findings kept with the doc's sources: real cloth against game
cloth, and the tricks shipped stylized games use. No daemons were sent. Subagent tokens: about 197,000.

## Scorecard

No earlier pass on this subject. The postmortem's own done-whens stand.

## Anchor

The robe should read as cloth on a phone: weight at the edges, motion that trails the body, and a hand-made, stylized
look. Unchanged.

## Shaman (17 Following, becoming 54 Home Field Advantage)

The reading says to fall in with what is already moving. The cloth has been fighting the body for ten rounds; the
move is to let it follow the body, late.

**The felt sense is a freeze.** "Solid objects" names a body that does not breathe through its clothes. Viewers rarely
notice secondary motion, but they feel its absence (Hodgins; O'Brien, Zordan and Hodgins). Wendell named the feeling,
which is the right report: no single bug will match it.

**The sleeves carry the feeling.** A bell sleeve is the softest, most delayed part of a robe, and ours is skinned. The
cuffs round 10 made clean are clean rings riding the forearm exactly, which makes the freeze easier to see, not harder.

**Recommendation.** Give the sleeves lag before anything else. A robe whose sleeves trail reads alive even with a plain
skirt.

## Architect (47 Drained, becoming 43 Unsaid)

The reading warns that more explaining will land badly while the basin is dry. Ten rounds explained the skirt's
physics; the one unsaid sentence is that timing, not physics, makes cloth read as cloth.

**What must be true in the machine.** Motion coherence is the measure. Bi, Jin, Nienborg and Xiao (Journal of Vision
2019) changed only how uniformly nearby points move and changed how stiff cloth looked. A skinned sleeve has
coherence 1 with its forearm by construction. The machine needs parts whose phase differs from their support.

**The binary is false.** Live simulation against skinning is not the choice. The third position is a spring-bone
chain: a few joints per sleeve rim and sash tail, each with stiffness, drag and gravity, on top of the skinning.
`@pixiv/three-vrm-springbone` runs on plain three.js objects without a VRM file, and colliders are spheres and
capsules, which the robe's leg capsules already are.

**Structure.** Sleeves: two or three chains per bell rim from the elbow, the cuff ring weighted to the chain's last
joints. The Node rig (`cloth_walk.mjs`) runs the same spring code as the game, as it does for `cloth.js`, so J5d
measures what the phone shows. Skirt: stays live cloth; the XPBD rebuild's painted maps gain a mass map so the hem is
heavier than the body.

## Challenger (29 Depths, becoming 28 Overload)

The reading is the pit below the pit: the sleeves are under the skirt's problem. It becomes Overload, a ridgepole
carrying more than its ends: `cloth.js` alone cannot carry every garment.

**What goes wrong.** A spring chain tuned while looking breaks the round 9 lesson: tune with a measure first. Springs
also jitter at low frame rates and overshoot through the body when the arm snaps forward.

**Self-inflicted.** Round 10 made the cuff ring ride the forearm alone, which is exactly the rigid look he named. It
was the right fix for torn trim, and it moved the problem into plain view.

**Falsification tests** (dated).
- **T1, by 2026-10-24:** J5d gains a sleeve measure: the sleeve rim's lag behind the forearm in frames, and the
  coherence of rim points with the forearm. A chain passes when the rim trails by 3 to 6 frames at the walk and the
  rim's coherence with the forearm falls below 0.8 (skinned today: 1.0). If Wendell still says "solid" on a sleeve
  that passes, the measure is wrong and the pass is reopened.
- **T2, by 2026-10-24:** no sleeve point inside the arm or body over the J4 walk and a fast arm swing (J5's through
  test, run on the chain).
- **T3, by 2026-10-31:** cost. The springs for one figure stay under 0.2 ms on his iPhone, on the frame readout the
  postmortem's plan step 3 adds.

## Regent (1 Unbroken, becoming 10 Footing)

The reading is the most able figure with nowhere to land, becoming Footing: the step decides whether the ground
holds. Order matters more than force.

**Phase gates.** Sleeves first (they are skinned, so the work does not wait on the XPBD rebuild and is not thrown
away by it). Then the postmortem's plan resumes in its order, with the mass map folded into the XPBD step. Vertex
flutter and baked loops come after his look at the sleeves, not before.

**Definition of done for the sleeves.** T1 and T2 pass, a side-by-side clip of round 10 and round 11 sleeves is on
the board as a look step, and his note on it is recorded.

**Non-negotiables.** The game and the Node rig run one spring code. The robe's cut does not change without his ruling.
#359's clean cuff ring stays, as the shape the chain carries.

## Diplomat (5 Hosting, becoming 32 Endurance)

The reading: ready, and the ground is not. Feed the work while the crossing waits. It becomes Endurance, a motion that
repeats.

**Bridge.** His question was a designer's question, so the answer is in a designer's words: delay that grows toward
the free edge, weight at the hem and cuff, and nothing stopping at once. The doc's tab puts each principle beside what
our robe does.

**Community.** The Portland community's allergy to AI favours hand-made reads. A robe that moves with an animator's
timing reads as crafted, and the same chains take hand-keyed motion for the let-go stances.

**Copy principle.** Every look step shows a before and after clip, sleeve first, at a third speed and full speed.

## Verdicts

| Face | What breaks the read | Next move | Robe re-cut into panels? |
| --- | --- | --- | --- |
| Shaman | The sleeves freeze with the arm | Sleeve lag first | Not now |
| Architect | Coherence 1 on skinned parts | Spring-bone chains, same code in Node | Not now; panels are a later lever |
| Challenger | Tuning without a measure | T1 to T3 before his look | Only if T1 passes and he still says solid |
| Regent | Order of work | Sleeves, then the postmortem plan with a mass map | Only by his ruling |
| Diplomat | A designer's question answered in physics words | Answer in designer's terms, show clips | His taste decides |

## Dissent check

Not unanimous. The Challenger holds that a re-cut into panels may be the real fix and wants it on the table if the
sleeves pass T1 and still read solid; the other four keep the cut and treat panels as a later lever.

## Sage (26 Reserves, becoming 19 Spring)

The reading is power held in store, becoming a rising with an edge on its window: the springs are ready and the time
is now.

**Synthesis.** The robe reads as solid because its sleeves share the arm's timing. The smallest coherent whole is
spring-bone chains on the sleeve rims, carrying the clean cuff ring, measured by lag and coherence, in one spring code
for game and Node rig. The skirt's plan stays as the postmortem set it, with a mass map added to the XPBD step.
Contributions: Shaman (sleeves first), Architect (coherence measure, chains, shared code), Challenger (T1 to T3,
panels kept in view), Regent (order, done), Diplomat (designer's terms, clips). Dropped: vertex flutter and baked
loops for now, kept in the doc's table.

**Dissent.** The Challenger's panel re-cut, recorded, not decided.

## Outputs

**Positions** (stand unless he flips them):
- **cd-sleeve-springs.** Next cloth work: spring-bone chains on the sleeve rims (`three-vrm-springbone`, same code in
  `cloth_walk.mjs`), the cuff ring riding the chain's last joints, measured by T1 to T3, then a look step. Why it did
  not need him: his note names the symptom and the research names the cause; the robe's cut does not change.
- **cd-hem-mass.** The XPBD rebuild's painted maps gain a mass map, heavier at the hem and cuffs. Why: it folds into a
  step already in the postmortem's plan.
- **cd-keep-cut.** The robe keeps its cut. Panels and strips stay a later lever, raised only if the sleeves pass T1 and
  still read solid. Why: a cut change is his taste; nothing yet says it is needed.

**Questions:** none. A re-cut would be his call, and the record does not yet say one is needed, so it waits behind T1.
