# Six-face pass big-mind-trust 1, 2026-10-16

**Called by** the coordinator on Wendell's walkthrough notes of 2026-10-16, 21:52, after he walked the whole daemon path to
the centre (bars-engine #343). His words, unaltered, are in the brief below. First pass on this subject; the strand is
`council/callsheets/big-mind-cave.md`.

**Casts.** Shaman 32 Endurance, line 1 changing, becoming 34 Vigour. Architect 20 Witnessing, lines 3 and 6, becoming 39
Impasse. Challenger 10 Footing, no changing lines. Regent 13 Fellowship, line 5, becoming 30 Burning. Diplomat 20
Witnessing, lines 4, 5 and 6, becoming 16 Anticipation. Sage 49 Molting, line 6 changing (the rest of the Sage's cast was
cut off in the session's output, so the Sage reads only the primary figure: "A skin is coming off you, and the new one is
soft.").

**Ontology.** Default profile (QUICKSTART) for every face: "Trust, agency, and relationship", "Session depth, performance,
and disclosure", "Evidence authority", "Lifecycle grammar". Touches: TrustState, ConsentRecord, MovementFinding.

## Scorecard

No earlier pass on trust. Tests still open from the strand: his play of the W.A.V.E. in the Protector's chamber by
2026-10-18; the lever test and pass 3's hallway sit-down tests by 2026-10-25; the Challenger's by 2026-11-01. Not graded
here.

## Anchor

Wendell, 2026-10-16: "To get the voices to trust you and remove their burden is a part of the game." The design intent:
each voice on the daemon path is met, tested and let in by trust the player shows in action, so the cave is a game and a
practice of inner trust, played alone with the depth of the Big Mind transcript.

## His words (the brief)

> This first round is pretty good. I want to add a trust mechanics so that it feels like more of a game. Trust is
> capability integrity and benevolence
>
> Can you do x will you do x and do you seem like a good person.
>
> To get the voices to trust you and remove their burden is a part of the game. There should be actions the player can
> take from the perspective of the daemon to show they are trustworthy in more dimensions.
>
> This means we can use this as a skill that people can use to develop inner trust.
>
> We can also lean more into 321 and let people do full 321 dialogues with each part. I think we're at the point where we
> can bring spirits into the game as well. The game can ask the player how THEY feel about encountering a part and this
> would spawn a spirit the players can walk through the cave with and the spirits can also show they daemons how resources
> the players are.
>
> Also the next daemon shows up at the end of the path before the cave where they show up is at. We can remove this each
> of the shifts are getting permission from the player to move forward and giving the daemon too early ruins the magic of
> this.
>
> I think we can also open it up to free walking so players can walk or run to the next space and we can also start
> thinking about dressing the cave and developing models for each of the daemons now so they are game ready and not just
> place holders.
>
> We want to use the game design ontology to plan what changes we want to make so I'd spin up a design thread where we can
> have a back and forth about what we want to feel and how to negotiate the fact this process is usually facilitated but
> we want it to be able to be played alone but still have the depth of experience in alignment with the big mind
> transcript

Evidence limit, shared by every face: nobody read the Big Mind transcript itself (it is not in any repo in reach). Claims
about solo depth rest on DESIGN.md, the passes and the general shape of facilitation.

## Shaman

**The cast.** The voices have heard the self's promises before, and the cave runs the same ask seven times. Unaimed force
is the danger: a player pushing on a voice to open it. Trust that lasts comes from a form repeated and kept.

**What earning trust should feel like.** Being tested by something old in you that has a reason to doubt, and then being
let in by it; never picking a lock. Each dimension is one move made from the voice's seat. Can you: the voice asks the self
to hold what it holds, and the player steps back out and shows it, for example by sitting with the charge the voice
guards. Will you: the voice asks for one promise, and on the player's return asks "Did you?"; an honest "no" is itself
integrity and has to be playable. Are you good: the voice asks what the self would do with its job if it rested. That
exchange is the 3-2-1 turned into play: the player asks as the voice, then answers as the self.

**The feeling that spawns a companion.** "How do you feel meeting this part?" is the first time the game asks about the
player's relationship to the voice. Fear, disgust and tenderness are all honest; "I'm scared of you" is truth-telling and
never counts against trust. A "no word yet" route spawns a grey spirit and plays the same.

**Solo depth.** A facilitator holds pace, permission, witness and the return. The game holds pace (the breath), permission
(the asks, `bm-decline`) and some witness (the guide saying words back). Nothing yet holds the return. A skippable closing
rite at the mouth (thank the voices, one breath, back to the room) and one plain line naming the move practised, per the
Shaman lesson "The player leaves with a move they can use." The felt target: accompanied without being watched, met by
voices with reasons, tenderness at the centre, back in your ordinary day at the end.

**Standing test.** A voice's doubt speaks from its own history ("I've heard that before") and never names a lack in the
player. Reluctance, silence, "I don't know", refusal and no-shift leave trust where it was.

## Architect

**The cast.** While the player looks at the voice, the voice looks back. Trust is what the voice sees. Today the only road
past a voice is the charge falling to 3 (READY, bigmind.js:1009, 1068); when that road is closed, the voice should say what
it is waiting to see.

**What exists.** One number per voice, restarted each sitting; no trust in the save. The Protector's assure cards already
carry the three dimensions unnamed: a promise ("I'll come back to my own place", integrity), an intent ("Nothing will be
taken from you", benevolence), a pace the player commits to ("I'll go slowly, and you can stop me", capability). "Thank you
for not pushing" rewards an honoured refusal.

**The false binary is "low charge means it trusts you."** Charge is the voice's burden for one sitting. Trust is its
relationship with the player, kept across sittings. Model: per voice, three lists of evidence, never a computed number.
Will: an assurance is saved as a promise and becomes evidence only when the game sees it kept (stepping back out, coming
back another day, a waiting voice heard); an unkept promise stays visible as unkept. Can: acts only (a W.A.V.E. held to any
rung, a sitting that ends, waiting with a voice after a refusal), at most one per kind per sitting, "I don't know" equal to a
named element, length never counts. Good: honouring a refusal, and an assurance chosen or typed in the player's own words
(the words are never saved). From the seat, a fourth turn asks "As X, what would you need to see from me?": the part writes
its own conditions, which is the inner-trust skill. Refusals are typed by the missing dimension ("I don't know that you can
hold it"). The save gains `voices[id].trust = { seen:[{dim, kind, at}], promises:[{kind, made, kept}] }`, no words.

**Full 3-2-1.** The chamber is already a staged 3-2-1. "Talk it through" at any poll opens `K.talk321`; phase 1 opens only
through the voice's permission to step aside. One optional hook in cave.js `talk321` (`o.beforeOne`) keeps the WAVE room
unchanged.

**Spirits.** Meeting a part asks how the player feels; that spawns a spirit (`via: "meeting"`). A spirit sat with to an end
counts once as capability; the count never adds more. Spirits never move charge.

## Challenger

**The cast.** The ground matters, and play is what keeps it safe. Once trust is a score, play turns into compliance.

**Breakpoints.** The charge is already the player's report, paid in light when it falls; three more rewarded numbers
triple the grind. "Can you, will you, are you good" seats the voice as judge: for the Controller, Skeptic and Damaged Self
that can become practice in appeasing an inner critic, the opposite of inner trust. Benevolence is the easiest dimension
to buy with disclosure. Counting every sit-down as resource makes sitting down farming. A voice that must step aside once
trust is full is a vending machine. Every playtest so far is Wendell's, and he facilitates Big Mind, so the solo claim is
untested. Dressing and models are satisfying visible work that can run ahead of an untested trust design.

**Hiding the next daemon** spends no safety, because "Not now" still sits at every first meeting. **Free running** costs
nothing while the chamber threshold still stops the player and nothing reads speed as meaning.

**Recommendations.** Trust actions are things done: keep a promise across a sitting, do what the voice fears you cannot,
stay through its refusal; never a right card. The voice shows which dimension it doubts in words and stance and can still
refuse at any level. No trust state goes into the models until there is a stance list for it. Test the solo claim with
someone other than Wendell before building the full per-part 3-2-1.

## Regent

**The cast.** The player and each voice already serve the same child; trust is how that gets said. A sentence said too
often stops meaning anything: a trust check repeated at seven chambers can become a form.

**The ontology.** TrustState is "situated evidence of capability and integrity within a relationship and domain"
(design-ontology-model-v0.1.md line 95). The cave can build three dimensions now as a game-local extension on his words;
the ontology text changes only by his hand.

**Solo safety.** `bm-safety` (2026-10-04) says the free daemon experience on his coaching site stops before the Damaged
Self and "the deeper voices belong to a facilitated session." Its scope is the coaching site, so the cave does not break it
today, but "played alone but still have the depth" collides with it the moment the cave goes public. The `bmc-safety`
duties are met in code (mouth rules, 988 and findahelpline, the ask before the Damaged Self, Forget and Delete).

**Build order, one thread and one pull request each.** A: hide the next daemon (smallest). B: free walking and running,
after A (same file). C: trust. D: full 3-2-1 and the meeting spirit, after C. E: art alongside, WARP bodies (#328) first,
then dressing, under a phone load budget. Every visit asks "May I speak to..." again; a saved yes is a ConsentRecord, not
present willingness. Public copy says "a practice for meeting your parts" and claims no effect.

## Diplomat

**The cast.** Standing in the voice's seat and looking back at the self, the player is the one doing the reading. Trust
can be felt growing before any voice steps aside.

**For a five-year-old.** "Inside you are helpers who worry. Each one guards a door. You can visit, listen, and keep the
small promises you make. When a helper sees that you can, that you will, and that you care, it lets you pass. You can always
say not now, rest, or go home."

**Respect over persuasion.** The quickest route is recognition: saying its job back to it, asking, thanking, accepting its
no. Arguing and bargaining are slower. The copy says "From where it stands, you said it saw...", never "The Controller
trusts you" as a system finding.

**His earlier ruling.** `ontology/v0.1/source/aesthetic-source-research-round-1.md`, excavation response 6: "Trust can be
understood through capability, integrity, and benevolence. For the game mechanic, leave benevolence out because it is too
difficult to gamify responsibly." The clarified model there keeps benevolence in trust's meaning "without being presented
as a meter the player fills."

**Who is burdened.** A full typed 3-2-1 burdens slow typists, second-language and disabled players; the out-of-turn word
list misreads second-language phrasing; hold-to-walk and running burden motor limits; solo play removes the person who
notices someone going numb. Every trust action has a card, a nonverbal route (a breath, a WARP gesture) and an open line,
with the same effect. The full 3-2-1 stays skippable and never gates stepping aside ("321s are optional and should have an
option to skip", 12 October). The typed 3-2-1 runs on the device; if a build check confirms no AI reads it, the mouth can
say so.

## Verdicts

| Face | Trust shown | Step-aside gate | Spirits and trust | Hide next daemon | Free walk | Full 3-2-1 | Solo depth |
|---|---|---|---|---|---|---|---|
| Shaman | stance and words | not argued | a shown spirit is evidence, count buys nothing | yes, presence without form | yes | the trust exchange is the 3-2-1 | add the return rite |
| Architect | three marks, plain lines | charge 3 or below, or all three seen | one capability act per spirit sat to an end | yes | yes | optional, phase 1 by permission | not argued |
| Challenger | words and stance | voice can refuse at any level | only a spirit deliberately shown | yes | yes, threshold stops | after a solo test | untested; test first |
| Regent | not argued | charge stays, trust beside | a chosen act, count moves nothing | yes, first build | yes, second build | fourth build | collides with `bm-safety` once public |
| Diplomat | can and will marked, good in words | not argued | a spirit is "can" evidence | yes, mouth breathing | yes, with a one-touch route | skippable, never a gate | guide carries patience; one move home |

**Dissent check.** Unanimous on hiding the next daemon, free walking, actions over answers, no disclosure currency,
refusal at any level and rest never lowering trust. A unanimous pass is a flag: no face argued for keeping the next daemon
visible. Split on how trust shows (marks against words) and on the gate (charge alone against two roads).

## Sage

The faces agree on more than they split on. Each contributed: the Shaman the felt target and the missing return; the
Architect the separation of burden from trust and the evidence model; the Challenger the grind and appeasement
breakpoints and the untested solo claim; the Regent the build order and the `bm-safety` collision; the Diplomat his own
earlier ruling on benevolence and the access floor. Dropped: the Architect's fourth seat turn as a fixed step (kept as an
offer inside the trust build, since seven chambers of it is the Regent's sentence that consumes its subject).

The new skin (49) is his three-part trust over the old one-number gate. The synthesis keeps both: charge stays the
burden, trust is added beside it as a second road past the voice, built from three actions done from the voice's seat.
Can and will are things the game can see happen; benevolence stays the voice's read, in its words, which honours both his
note of today and his ruling that benevolence is "too difficult to gamify responsibly." How visible trust is, and how deep
a lone player may go, are his.

Dissent kept: the Architect would show three marks; the Shaman and Challenger would show none; the Challenger would hold
the full 3-2-1 until a solo test.

## Outputs

### Positions (each stands unless he flips it)

- `bmt-feel`: the felt target. Being tested by something old in you that has a reason to doubt, and being let in by it;
  accompanied without being watched; tenderness at the centre; back in your ordinary day at the end with one move you can
  use. Source: Shaman, his "what we want to feel".
- `bmt-burden-trust`: charge and trust are two things. Charge is the voice's burden in this sitting; trust is its
  relationship with you, kept across sittings. Source: his "get the voices to trust you and remove their burden".
- `bmt-three-moves`: trust is earned by three actions taken from the voice's seat. Can you: do what it fears you can't
  (sit with what it guards, hold a W.A.V.E., wait through its refusal). Will you: make it one small promise that resting or
  leaving can keep, which the cave checks on your return. Are you good: honour its refusal and tell it, in a card or your
  own words, what you would do for it. Never a right card, never by how much you say.
- `bmt-two-roads`: a voice offers to step aside when its charge is 3 or below (`dp-pass-rule`, unchanged) or when it has
  seen all three. It can still refuse on either road, and its refusal names what it hasn't seen yet.
- `bmt-good-in-words`: benevolence is the voice's own read, said in its words and stance, never a meter. Source: his
  excavation response 6, "leave benevolence out because it is too difficult to gamify responsibly."
- `bmt-never-falls`: trust never falls. Rest, Not now, silence and "I don't know" leave it where it was. A promise not yet
  kept stays visible as not yet kept, and the voice says so when you come back.
- `bmt-ontology-local`: the three-part trust is a game-local extension in the cave. The ontology's TrustState stays
  capability and integrity, and a reconciliation note records the divergence; the ontology changes only if you say so.
- `bmt-meeting-spirit`: when you meet a voice the game asks how you feel meeting it, with "no word yet" as an equal answer;
  your answer spawns a spirit that walks with you.
- `bmt-show-spirit`: you can choose to show a spirit to a voice. That is one "can you" act per spirit; how many spirits you
  carry adds nothing, and spirits never move a voice's charge. This changes half of `bms-voices-respond` on your words of
  today ("the spirits can also show the daemons how resources the players are").
- `bmt-321-offer`: a full 3-2-1 with any voice is offered from the chamber ("Talk it through") and from the voice's seat,
  in cards, gesture or your own words. It stays skippable and never gates stepping aside. Being it opens only with the
  voice's permission.
- `bmt-hidden-next`: the next voice is hidden until you reach its chamber. The end of each hallway shows the shut mouth
  breathing, with its light and a sound behind it. Voices already met still wait by the wall. Source: his "giving the
  daemon too early ruins the magic".
- `bmt-free-walk`: walk or run freely through every hallway; tap-to-walk stays as a one-touch route. Each chamber
  threshold still stops you, and nothing reads your speed as meaning anything.
- `bmt-return`: a closing rite at the mouth you can skip: thank the voices, one breath, back to the WAVE room, with one
  plain line naming the move you practised.
- `bmt-ask-again`: every visit asks "May I speak to..." again, whatever the save holds.
- `bmt-build-order`: builds run as one thread and one pull request each: hidden next voice with free walking first; then
  trust; then the full 3-2-1 and the meeting spirit; art alongside (the WARP daemon bodies from #328 wired in first, then
  dressing, under a phone load budget, with the trust stances added once the trust build names them).

### Questions (passed the reach test)

- `bmt-trust-shown` (owner Diplomat): how should a voice's trust show, now that you want it "more of a game"? Options:
  A marks for can and will with plain lines, benevolence in words only (recommended); B three marks; C no marks, words and
  stance only. Why only he can answer: the felt target "feels like more of a game" pulls against his excavation ruling on
  benevolence, and only he knows how game-like he means. Not asked before: the trust mechanic is new today.
- `bmt-solo-depth` (owner Regent): how far may someone go alone, once the cave reaches players other than you? Options:
  A the whole path to the centre behind the existing check-ins and the return rite (recommended); B a lone player stops
  before the Damaged Self, as `bm-safety` set for the coaching site; C the whole path opens after one complete visit.
  Why only he can answer: it weighs his new "played alone but still have the depth" against his 4 October ruling that the
  deeper voices belong to a facilitated session; safety and consent are his. Not asked before: until today the cave had
  one player, him.

### Tests

- T1, by 2026-10-30: one player who knows Big Mind, other than Wendell, plays the Protector to the Skeptic alone, then on
  another day with Wendell facilitating. Compare whether a voice ever held back, whether the player heard a voice say
  something unexpected, and how long each chamber took. Settles whether solo play needs more pacing from the guide, and the
  full 3-2-1's place in the order. (Challenger)
- T2, by 2026-10-30, after the trust build: a card-only player and a typing player reach the same voices in as many
  sittings, with replies as full. If the card-only player needs more steps, the access floor fails. (Diplomat)
- T3, after the trust build: if Wendell reports picking trust actions to open the voice rather than to answer it, the
  actions have become currency, and `bmt-two-roads` changes. (Regent, Shaman)
- T4, at his next play: if the hallways with the next voice hidden leave him unsure where to walk, the hallway end needs a
  stronger cue. (Regent)

Subagents: five face agents, about 278,000 tokens in total. No daemons were sent.

## After his answers (board read 22:12, ledger `council/ledger/2026-10-16-pull-221155.json`)

Answered: `bmt-trust-shown` A (marks for can and will, good in words); `bmt-solo-depth` A (the whole path, with
check-ins). Thirteen positions stand, five of them with steers. Overruled: `bmt-three-moves` and `bmt-show-spirit`.

- `bmt-three-moves` (overruled): "You can take these actions before you get in the voices seat. I do think there is a
  right answer but only honest plays should get you progress as made manifest through charge metabolizing". Replaced by
  `bmt-honest-moves`. The Challenger's position that no card is the right one is overruled; his lesson for that face.
- `bmt-show-spirit` (overruled): "The spirits can vouch for you. The way I see this game is like at the end of pokemon
  where you show the badges you've collected to be let into victory road." Replaced by `bmt-spirits-vouch`.
- `bmt-two-roads` stands, steer "Once it's willing to step aside isn't always the end of the interaction": `bmt-keep-talking`.
- `bmt-good-in-words` stands, steer "They each have a mental model of what goodness looks like": `bmt-goodness-models`.
- `bmt-never-falls` stands with the steer "I think trust should be able to fall. This is the accountability matrix". The
  steer is the later, more specific word, so `bmt-trust-falls` replaces the never-falls rule; rest and Not now still
  lower nothing (`bm-decline`). Nothing in the record names an accountability matrix, so `bmt-accountability` asks.

Scope of the two running builds is unchanged (hidden next voice and free walking; WARP bodies). The trust build's brief on
the callsheet takes all five revisions.
