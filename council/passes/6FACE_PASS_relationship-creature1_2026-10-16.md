# Six-face pass relationship-creature 1, 2026-10-16

**Called by** the coordinator on Wendell's message of 2026-10-16, 22:20, proposing a co-tended relationship creature for
Mastering Allyship, Flirtcraft and Friendcraft. First pass on this subject; the strand is
`council/callsheets/relationship-creature.md`, and the board runs it as the battle `fr-between`.

**Casts.** The Shaman drew 56 Passing Through, line 6 changing, becoming 62 Overstep. The Architect drew 25 Candour,
lines 1 and 3 changing, becoming 33 Retreat. The Challenger drew 26 Reserves, line 1 changing, becoming 18 Stale Air. The
Regent drew 17 Following, line 4 changing, becoming 3 Sprouting. The Diplomat drew 32 Endurance, lines 4 and 6 changing,
becoming 18 Stale Air. The Sage drew 53 Emergence, line 5 changing, becoming 52 Stillness.

**Every face loaded the ontology's default profile** (QUICKSTART), chiefly "Trust, agency, and relationship", "Evidence
authority", "Privacy and consent authority", "Session depth, performance, and disclosure", "BAR scope" and
"Composting". The Architect also read the machine vocabulary's LL block and its `relationship_permission` verbs. The pass
touches Relationship, PermissionEnvelope and TrustState.

**Subagents.** Five face subagents, about 225,000 tokens together; no daemons were sent. The Sage synthesized in the
main session.

## Scorecard

No earlier pass on this subject, so nothing is graded.

## Anchor

Wendell, 2026-10-16: "these games involve tracking a creature in the LL intersubjective space that players co-tend with
the people they are in relationship with." The design intent: a creature that is the relationship, fed by charge each
person has worked through, living in a garden of shared BARs, so that tending it is the practice of keeping a living
agreement.

## His words (the brief)

> Ok for mastering allyship flirtcraft and friendcraft I want to introduce a new feature.
>
> Essentially these games involve tracking a creature in the LL intersubjective space that players co-tend with the
> people they are in relationship with.
>
> The creatures are fed by metabolized charge and live in a garden made out of BarQuests.
>
> The game is to keep the relationship healthy
>
> This is based on the work of Eri Kardos's book relationship agreements
>
> [a pasted summary of the book, kept in the thread]
>
> I want to gamify this framework and also leverage the work we're doing with big minds and spirits and daemons.
>
> Players can bring their own spirits to the collective garden but they are always co-tending their "fred" (definitely
> want another name)
>
> They can also tend to their projection of their partner AND their own concept of the Fred so they can see when what's
> being imagined is drifting
>
> I'd like to have the 6 game masters weigh in with the design ontology to explore this more

## Source check

The book exists: Eri Kardos, *Relationship Agreements: A Simple and Effective Guide for Strengthening Communication,
Reducing Conflict, and Increasing Intimacy to Design Your Ideal Relationship* (CreateSpace, 2016). Retail listings
describe written agreements as tools for communication and trust, usable in any relationship shape and revisited over
time. The only public line about Fred is on the Multiamory podcast's episode 103 page: "a small, blue, furry monster
named Fred can help change the way you think about your romantic relationships."
(https://www.multiamory.com/podcast/103). Nothing public says what Fred stands for. The pasted summary reads Fred as the
pair's anxieties and default assumptions; Wendell's design reads the creature as the relationship both people tend.
The game follows his words, credits her framework in paraphrase, and marks the book's meaning of Fred unconfirmed.

Evidence limit, shared by every face: nobody read the book, and Flirtcraft and Friendcraft are not readable from this
session.

## Shaman

**The cast.** The creature arrives as a stranger in two people's home and is judged fast, with only what they carry to
it. Line 6 says the design is doing slightly too much at once: a shared creature, brought spirits, daemons, two
projections and a garden. The bird does better coming down, and reverence is the one place to overdo.

**Who is in it.** Two or more people take part, and one of them may never have asked to play. Tending a shared hearth is
an old ritual form and can carry a great deal when both chose it. The invitation has to read "come tend this with me";
read as "you owe it care", the ritual becomes a ledger of obligation.

**The standing test fails as the design is stated.** "Keep the relationship healthy" lets a declining creature say that
something is wrong with the pair, or with whoever went silent. A creature that sickens when one person rests turns
silence into deficiency, and the relationship into a pet that can be held hostage. The cave already rules this out
(`bmt-never-falls`).

**The projected partner is the most alive part and the most dangerous.** Tending my picture of you can show me my picture
has moved. It must never show that you were misread, or that you changed against the agreement. The game does not infer
the partner. The symbolic distance of a third figure is the gift: two people can talk about the relationship through it,
and what it means stays theirs.

**Recommendations.** Decline only from a broken agreement or a push past a refusal, repaired by owning it; ending is a
playable closing rite; pictures private-local by default; one ritual before any system. Verdict: support with
conditions, design only. Dissent seed: "A creature that suffers from absence makes love a chore and silence a crime."

## Architect

**The cast.** Candour: build the creature only from what both people actually say, with nothing guessed about the other.
Retreat: leaving belongs in the machine from the first table, and a relationship that ends well is a valid state.

**The record already holds most of what the feature needs.** A charge is a dissatisfied configuration (`ss-intake-start`);
satisfaction runs 1 to 10 in three states (`ss-three-states`); a BAR is planted by setting `gardenId`
(bars-engine `src/lib/garden/plant.ts`), which today is always `personal:<playerId>` (`src/lib/lenses/ensure.ts:51`).
There is no garden table or membership. The planting writer does not check who owns the BAR; its callers do, and a
shared garden makes that check load-bearing.

**Five typed objects make up the feature.** A Bond with two or more members, each invited, joined, paused or left. A
Bond Garden with the id `bond:<bondId>`, where only joined members plant. An Agreement, a BAR planted there with its own
life: drafted, proposed, agreed by every member, up for revisit, then retired or composted; that carries the "living
document" without copying the book. The Creature, one per Bond, whose state only a joint check-in writes. A Private
Picture, each member's own image of the creature and of the other person, readable only by its author.

**Healthy or sick is the false binary.** The third state is unchecked: between check-ins the creature shows its last
joint reading with how long ago that was. Shared or private is the second; its third state is offered, a picture one
member chooses to show at a check-in and can take back.

**Drift is a finding made at a check-in.** Each member may reveal their picture. Drift is the gap between one member's
picture and what the other revealed. If either declines it reads "not compared", and declining costs nothing. AI never
fills the gap.

**Acceptance tests.** Planting in a bond garden fails for a non-member or a paused or departed one; a private picture is
never returned to anyone but its author unless offered; with one reveal missing, drift reads "not compared" and the
state does not move; a rest or refusal leaves the number unchanged; a member leaving changes no other member's private
records; a personal-garden charge never moves the creature.

## Challenger

**The cast.** Reserves: the council has stored real power (spirits, states, daemons, trust) and has not named the day to
spend it. Stale Air names both the creature's likely mechanic, decay from being left alone, and the design's likely
failure, punishing people for being away.

**The plain claim is a meter.** Strip the image and two people share a pet whose health stands for their relationship.
Mechanics claim reality (constitution 5). A creature that sickens when a partner stops feeding it tells that partner
they are failing. One partner can point at it in an argument, and leaving a bad relationship becomes letting the pet
die.

**Projection tending can turn into a dossier.** My picture of you is my own meaning. Drift can only show against your
report, which makes your disclosure the fuel and the comparison a "you are wrong about me" score.

**The source is weaker than the summary.** "Fred is the pair's fears" and "the creature is the relationship" are two
games: one feeds a monster you want to shrink, the other a creature you want to grow.

**The schedule is avoiding something.** The North Star is the Chapter 1 demo. A shared garden needs a table and a
two-person permission model, and neither exists; multiplayer consent is the expensive part, and the request treats it as
decoration.

**Hidden coercion has marks to watch for:** decay while someone is away, a shared score one person sees the other move,
an invitation that costs someone standing, a rest or ending that reads as a loss. Verdict: support with conditions,
concept only; opposes any health meter that decays from neglect.

**Tests.** T1 desk check: four scenarios (a breakup, one person stops playing, a controlling partner demands the other's
picture, a charge about the partner fed into the shared garden) run through the design, by 2026-10-20, council-run. T2
paper play: two people, one written agreement, a paper creature and two check-ins over a week, report by 2026-10-30. T3
source read: what Fred stands for in the book, by 2026-10-23.

## Regent

**The cast.** Following: fall in with what is already moving (spirits, the garden, Big Mind trust, the Friendcraft
redesign); start nothing new. Sprouting: this is early, so appoint helpers and take no journey.

**Four obligations bind; the rest is preference.** Credit to Eri Kardos in the council's own words; the consent of the second
person, who is not the player; the cap of three games; the North Star. The name, the look, how drift shows and which
product goes first are preference.

**The game may say "inspired by Eri Kardos, *Relationship Agreements* (2016)".** It may not say "this is Kardos's
Fred". Naming a person in public copy is reserved to Wendell.

**The second person holds a key.** Consent is authorization now; a yes from last month does not open tonight's check-in
(QUICKSTART, Privacy and consent). Each session asks again, as `bmt-ask-again` does for voices. A partner's agreement to
the relationship is not consent to the game.

**The cap and the North Star set the order.** Flirtcraft and Friendcraft sit outside the cap (`st-cap-games-only`), and
the demo stays the cave (`el-demo-scope`). The creature does not speed Chapter 1, so it does not ride with it. Phase
gates: G0 board rows now; G1 the source read and a credit line he approves; G2 a written two-key consent model with a
solo route and a harmless exit; G3 a paper play with a real pair; G4 one product, one thread.

**These stop the work:** storing the partner's data without their present consent; using the creature's state as
leverage ("you are starving our creature"); showing one person's picture to the other; putting the creature in Chapter 1
before the Kickstarter.

## Diplomat

**The cast.** Endurance is the old reading of marriage: two people in steady relation, lasting because the motion
repeats. Stale Air says what goes off when left alone. If the creature goes stale through neglect, the person who tends
less becomes the one to blame; staleness has to be something either can air out.

**The five-year-old doorway reads:** "You and someone you care about share a small creature. It grows when you check in and keep
your small promises. Each of you can also draw what you think the other one feels, and you only show the drawing if you
both want to."

**The second person did not choose this game.** No shared garden exists until they grant it themselves. Declining sends
"not now" and no reason, and the one declined keeps a full solo route.

**Uneven tending is the normal case.** If the creature shows who fed it, it becomes a scoreboard of who cares more. It
shows only a shared state.

**Disclosure does not feed it more.** A check-in by tapping "tired", a gesture, a symbol card or a second language feeds
as much as a long letter; "fine, nothing to add" is a complete check-in.

**Romance is one doorway among several.** Friends, housemates, family and allies can hold one; copy says "someone you
share a life with" unless players choose "partner".

**The paper version stands whole.** The Portland community's allergy to AI makes a printed agreement, check-in cards and
a drawn creature a full game, and no model reads the other person's words.

**A harmful relationship could make it a weapon.** Exits leave no trace: no read receipts, no last-seen times, no record of
who left, and the game never coaches anyone to stay. The Diplomat's own overreach: softening until nothing is at stake.
A creature that can go stale is a real stake, and the Diplomat would keep it.

## Verdicts

| Face | V1 what it is | V2 feeds / harms | V3 drift | V4 build first |
|---|---|---|---|---|
| Shaman | The relationship, a third presence; fears are what it hides | Chosen charge, check-ins, repairs / only a broken agreement or a push past refusal | "My picture moved", on my own copy; side by side by choice | Nothing; one paper ritual with a willing person |
| Architect | The relationship; unspoken fears are its veiled parts | Kept agreements, held check-ins, repairs, offered charge / unrepaired breaks, a missed agreed check-in | Only at a check-in, between revealed pictures; withheld reads "not compared" | Bond, membership, `bond:` garden id with a membership check, Agreement BARs |
| Challenger | The agreement made visible | Kept and revisited agreements, shared charge / only an owned broken agreement; absence never | Private; compared only with what was shared; no score | Nothing until T1 and T2; then paper, then a permission design |
| Regent | The relationship; assumptions dim it | Agreements made and kept, worked-through charge / an unowned break | Only to the holder, at a check-in both chose | Nothing; after G1 and G2, a paper check-in with a real pair |
| Diplomat | The repeated exchange itself | Check-ins of any length, kept promises, owned lapses, chosen charge / an unowned break or a push past refusal; neglect makes it stale, never dead | Privately to the holder; side by side when both reveal | Nothing; then a paper onboarding for two |

## Dissent check

Not unanimous. Four faces agree the creature is the relationship and that pictures stay private; they split on neglect.
The Shaman and the Challenger hold that absence never lowers the creature. The Diplomat would let it go stale from
neglect, as a real stake, never fatal. The Architect takes a middle line: a missed check-in lowers it only when the pair
agreed to that rhythm. The Architect alone would build now; the other four would build nothing before a paper play. Five
faces near agreement on privacy is a flag: none of them could read Flirtcraft or Friendcraft, so the agreement rests on
the ontology and the cave's record, not on either game.

## Sage

**The cast.** Emergence: a tree takes hold at the rate roots allow, by stages that cannot be skipped; becoming
Stillness, stop while the wanting is still running. The pass names the stages and builds none of them.

**What the council holds.** The creature is the relationship itself, the third presence two people tend, as his words say
(all five). The pasted summary's "Freds", the fears and default assumptions, already have a home: they are each person's
daemons, and they reach the garden only as spirits a player chooses to bring, or as the creature's veiled parts that a
check-in can reveal (Architect, Shaman, `ss-not-veiled`). This joins the feature to the cave: what the Big Mind cave
does inside one person, the garden does between two.

**What it feeds on and what lowers it.** Kept agreements, check-ins of any length and kind, owned repairs, and charge a
person chooses to offer (Architect, Diplomat). The trust rules already on the board carry over: a broken agreement or a
push past a refusal lowers it, owning it repairs it, rest never lowers it (`bmt-trust-falls`, `bmt-never-falls`). The
one open feel question is whether plain neglect can make it stale; the Architect's middle line (an agreed rhythm is
itself an agreement) is the council's recommendation, and the board asks him.

**Drift stays private.** Each person's pictures stay theirs; drift is a gap between two revealed pictures at a check-in both chose,
shown as a difference, never as an error, and "not compared" when either holds back (all five).

**The desk check (Challenger T1), run in this pass.** A breakup composts the shared creature with no death, and each
keeps their own pictures (`rc-exit`). One person stopping changes nothing unless the pair agreed a rhythm, which waits on
`rc-stale`. A controlling partner demanding the other's picture meets a picture that stays on its holder's device and
has no export (`rc-pictures-private`); the residual risk is a coerced "show", which looks like a chosen one, so the silent
exit and the outside resource line stand beside it. A charge about the partner fed into the shared garden needs a rule
the faces did not write: an offered charge is shown to the other person before it lands, and they can decline it
(`rc-offer-received`). T1 passes with that one new rule.

**Order.** Nothing is built in this pass, and the creature stays out of the Chapter 1 demo (Regent). Friendcraft is the
first home, because its redesign pass (BARs for friendship, basic moves rethought with emotional alchemy) is already
planned and is where this falls in (Regent, Following). The next move is a paper play with one willing person (Shaman,
Challenger, Regent, Diplomat). The Architect's five objects are the design the paper version mirrors, and its acceptance
tests are the build's.

**Dropped.** The Shaman's "Kith" and the Regent's "the Tend" and "the Kin" go to the name row only as the steer box's
prompt; "Hearthling" collides with the project's own tool name and is set down. The Challenger's question on who plays
T2 waits until the board answers who can hold a creature. The Regent's question on which product goes first stands as a
position, since the record answers it with the planned Friendcraft redesign.

**Dissent kept.** The Diplomat would keep staleness from plain neglect as a real stake. The Challenger and the Shaman
would allow no decay from absence at all. The Architect would build the bond schema now.

## Outputs

### Positions (stand unless he flips them)

- `rc-is-relationship`: the creature is the relationship itself; fears and assumptions are each person's daemons and the
  creature's veiled parts. Citation: his message; Source check; `ss-not-veiled`.
- `rc-joint-checkin`: only a check-in both people hold changes the shared creature. Citation: QUICKSTART, Evidence
  authority (relational attestation).
- `rc-pictures-private`: pictures are private-local, shown only by choice, never scored; drift as above. Citation:
  QUICKSTART, Privacy and consent; constitution 10; `bmt-show-spirit`.
- `rc-feeds`: what feeds and lowers it, and every route feeds equally, with no tally of who fed. Citation:
  `bmt-trust-falls`, `bmt-never-falls`; QUICKSTART, Session depth.
- `rc-offer-received`: an offered charge is shown to the other before it lands, and they can decline it. Citation: this
  pass's desk check; QUICKSTART, Privacy and consent.
- `rc-exit`: consent asked each session; rest and leave alone; leaving composts; silent exit and an outside resource line.
  Citation: `bmt-ask-again`; QUICKSTART, Composting and Trust.
- `rc-spirits-visit`: your spirits visit the garden and stay yours. Citation: QUICKSTART ("Access to an ally is not
  command").
- `rc-agreements-bars`: agreements are BARs with a life in a shared garden of the pair's own. Citation: Architect; BAR
  scope; `src/lib/garden/plant.ts`.
- `rc-goal`: keeping it healthy means the agreement stays honest and current; an honest ending is a valid completion.
  Citation: his words; QUICKSTART, Lifecycle grammar and Composting.
- `rc-credit`: never called Fred; Kardos credited in paraphrase; public mention waits on his word. Citation: Source
  check; reserved items in `council/faces.yaml`.
- `rc-order`: nothing built now; not in the demo; Friendcraft first; next a paper play. Citation: `el-demo-scope`,
  `st-cap-games-only`, `council/callsheets/friendcraft.md`.

### Questions (passed the reach test)

- `rc-name` (Shaman, Diplomat): what to call it. Only he can name it (term pass, his lock).
- `rc-stale` (Challenger, Diplomat, Shaman): whether plain neglect can make it stale. The faces split, and the answer
  sets what the creature's state tracks.
- `rc-who-holds` (Architect, Diplomat): who can hold one, and whether one person can start alone. Nothing in the record
  says; it sets the garden's shape.

### Tests, dated

- T1 desk check: run in this pass; passed with `rc-offer-received`.
- T2 paper play with one willing person, one agreement, a drawn creature and two check-ins over a week: report by
  2026-10-30, after `rc-who-holds` is answered. Proves the design wrong if either person uses the creature against the
  other or reports feeling obliged to feed it.
- T3 source read, what Fred stands for in the book: by 2026-10-23. Settles the credit line.
