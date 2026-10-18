# Perceptual shadow: the games-and-introspection research run against the design ontology

Scope: take the "Perceptual Shadow in Games" research report (pasted by Wendell, 2026-10-17) and test it
against the design ontology (Quickstart, constitution, evidence authority) and against what bars-engine #326 already
built (`content/ontology-game/cave/cave.js`, callsheet `council/callsheets/perceptual-shadow.md`). Profile loaded:
`game_design`. Nothing here is a ruling. Positions stand unless Wendell flips them on the board.

The report says it was compiled without live retrieval. Its own caveats list four items to re-check (Ducharme and
Iyadurai sample sizes, the Jennett tangram statistics, Khaled's four principles, Brazil's 2025 provision). Under the
evidence rule ("empirical effect: evidence within declared scope"), none of those four figures goes into player-facing
text or the ontology until someone has retrieved the source.

## design_intent

Let a player who can tell a charge is there, but cannot see it or keep attention on it, meet whatever is hiding it, by
asking it what it protects, without being pushed out of range of their own comfort. Overcoming here means the shadow
clears because its work was understood and its protective function was heard. It does not mean the shadow was defeated.

## intrinsic_pleasure

Whose pleasure leads: the player's, in the discovery of "hide and seek" (Wendell's own phrase, 2026-10-14: the Player
"secretly enjoying the game of hide and seek"). The pleasure is inference and uncanny precision: a grey fog, a creature
standing back by the door, a question that lands. The research supports this register, since players value games that
make them question what they are shown, and value moving or sad moments (Bopp et al. 2016; Mekler et al. 2018, both cited in the report).

## ontology_objects

| Report term | Ontology or build term | Note |
|---|---|---|
| the four "faces" (forgetting, distracting, dissociating, numbness) | the four **shadow kinds** (`ps-four-kinds`) | Do not call them "faces". Face is the Six Faces namespace (`face_namespaces` binding decision). The callsheet already says "kinds". |
| daemon | the seven daemons in `council/daemons/daemons.yaml`, and the shadow spirit that asks each daemon's set | The four kinds are not daemons. A daemon is a protector figure that can hold a kind in place. |
| IFS protector / firefighter | the Protector daemon and the shadow spirit | Design metaphor only. The report's own advice is to cite IFS as metaphor and anchor to schema modes and experiential avoidance. |
| window of tolerance | polarity, -10 to 10 (`ps-polarity-poles`) | Below 0 floods (hyperarousal side), above 0 hides (hypoarousal side). A close match. The window is a teaching heuristic, so polarity stays a player-reported reading and not a measurement. |
| "perceptual shadow" | council vocabulary, not a scientific term | The report says so. Keep it out of any claim that sounds clinical. |
| `DesignShadow` in the ontology yaml | a different object: a recurring shadow of the designer | Do not merge it with perceptual shadow. Principle 13 does allow a later playable version of perceptual shadow for the designer's own tool. |

Empirical anchors the council may name in design notes, each marked as an analogue and not a proof:

| Kind | Construct | Source in the report |
|---|---|---|
| Forgetting | time loss; prospective-memory slips | Wood, Griffiths & Parke 2007 |
| Distracting | attentional capture; zoning out vs tuning out | Schooler et al. 2011 |
| Dissociating | absorption, depersonalization | Guglielmucci et al. 2019 (cross-sectional) |
| Numbness | experiential avoidance; suppression; Detached Protector mode | Hayes 1996; Young 2003; Gross & John 2003 |

## mechanical_claims

What #326 tracks, rewards, gates and remembers, set against the report:

- **Tracks:** polarity per creature and spirit; the kind the player names; each ask and answer (`shadow.asks`); which
  signal fired. The report supports tracking the player's own reading over any inferred state (Nisbett and Wilson on
  confabulated introspection; the ontology's "player report establishes reported meaning").
- **Triggers:** two signals, both player-facing: "I know it's here, but I can't feel it" (self-caught), and a round whose
  reading did not come down. The first is the report's "self-caught" case, the better one. The second is a system
  inference offered as "Something may be hiding part of it", which reads as a proposal and not a verdict. That wording
  should stay.
- **Rewards:** each finished daemon set or practice lowers polarity by 3.
- **Gates:** none seen. The player can go on with the creature still veiled. This meets the report's "never punish leaving".
- **Remembers:** the run record, kept as lineage.

## aqal_attention

- **UL:** the felt sense of "it's here but I can't reach it"; the player authors what the shadow means.
- **UR:** the 0 to 10 charge reading before and after; the somatic practices (feet and seat, long out-breath).
- **LL:** none foregrounded. Shared play of the WAVE room is out of scope, and a relational version would need the
  permission intersection rule.
- **LR:** the run record and the polarity rules.
- **Lines made consequential:** perceiving charge (Wake Up). Stay with the named-line rule: this is not a whole-person rank.
- **States invited, not made traits:** hiding and flooding are states of this charge in this sitting.
- **Burdened types:** players who are trauma-exposed, or who dissociate readily, meet a page whose second kind is named
  "Dissociating". The report's strongest caution applies here (surfacing without pacing).

## agency_and_consent

What the build already does well, by the report's test (visible, chosen, exitable):

- Visible: the shadow shows only when a signal fires, and the player names its kind or says "I can't tell".
- Chosen: 3-2-1 is skippable ("321s are optional and should have an option to skip", Wendell, 2026-10-12). The Big Mind
  wall offers "Not now" as a full answer.
- Exitable: "Stop here", "Rest it by the door", a Rest button at the deepest place of the 3-2-1, and the calm button.
- Negotiated and not defeated: the shadow spirit is asked what its work is for. This is the verb the report asks for.

Three places where the build and the ontology pull apart:

1. **Disclosure behaves as a progression currency.** A daemon set lowers polarity only when each question has written
   text or a picked answer (`said.disabled` stays true until there is one). Constitution rule: intimate disclosure is not
   progression currency, answer length proves nothing, and the system must not weaken anything to pressure disclosure.
   Provisional position: the set counts as one practice whenever the player completes it, and "nothing to say" or "pass"
   is a full answer that counts the same as a paragraph.
2. **No named way to decline the system's reading.** When the number did not come down, the only button is "Look again
   for what's hiding it". Leaving works, but the screen does not say that a no-shift is a valid ending. The ontology's
   `MovementFinding` includes no-shift and uncertainty. Provisional position: add a second button beside it, "This is
   where it is for now", which ends the encounter with no polarity change and no penalty.
3. **The word "Dissociating" is a label the player may not want.** The player names the kind, which helps. A content note
   before the four kinds ("Stop or rest at any point; nothing here needs to be done in one sitting") and a visible step-back
   at every page cover the report's window-of-tolerance caution.

## evidence_and_unknowns

- Time loss, absorption, mood management and dark patterns are well supported as common. Whether absorption is harmful
  depends on function and flexibility (Stenseng; Bonanno & Burton), which is what the report's refined thesis says.
- The inverse (games that help) has modest and mixed evidence. MindLight did no better than a commercial control game and
  EndeavorRx did not move parent-rated symptoms. **Do not claim the cave reduces shadow in life.** It can claim only that
  a player reported a reading change in this sitting.
- Transfer is the weakest link. It is not a design flaw of the cave. It is a claim the cave must not make.
- Almost all child-specific causal evidence is missing. The report calls its child claims extrapolations.
- Unknown: whether the four practices thin anything, or whether engagement does the work. The run already records
  `shadow.practices`, `signals`, and the readings, which is enough to compare practice rounds against plain rounds.

## provenance_effects

The run record already keeps signals, kind, polarity start and end, practices and asks. Add only: which signal fired
(self-caught or prompted), so a later reader can tell Wendell's "aware but can't perceive" from the system's "number
did not drop". The report treats those as different cases (Schooler: self-caught vs probe-caught). Record the difference.
Do not reward the difference.

## risks_and_tests

| Risk | Proportionate test |
|---|---|
| Proxy capture: players write filler to thin the shadow | Run a set with one-word and "pass" answers; confirm polarity and the run record treat them identically. Read the record for whether answer length predicts anything. |
| System inference read as truth (the number did not drop, so something hides it) | Check that the decline button exists and that a declined offer leaves polarity as it was. |
| Surfacing without pacing for trauma-exposed players | Walk the flood path and the dissociating path at once; confirm Stop, Rest and step-back appear on every page, including the daemon set pages. |
| The cave's own practices feel like therapy claims | Run `voice_lint.py` and `scan.py` over every practice line. A practice line states what to do, not what it will cure. |
| The community's allergy to AI | Run the whole sitting on paper: four kinds, four practices, a 0 to 10 number, and eight daemon questions. It already works that way. Keep any AI reading of a player's answers an optional proposal. |

## implementation_translation

Smallest changes, in bars-engine, none required to ship:

1. Make the daemon set count with a "pass" answer (`said` button, `cave.js` near line 3913).
2. Add "This is where it is for now" beside "Look again" (`lookAgainRow`, near line 4067).
3. Add the one-line content note on the shadow-kind page.
4. Record `signalSource: "self" | "offered"` in `shadow.signals`.

Candidates the research suggests that the build does not yet have, each optional and each needing its own permission
before it is built, since each touches data or contact outside a sitting:

- **An if-then bridge** at the end of a sitting: "If I notice X, then I will Y", written by the player, kept private
  and local by default. This is the report's best-supported transfer technique (Gollwitzer and Sheeran, d = 0.65 in the
  report; re-check before quoting). It is a player-authored `ActionIntention`, which the ontology already has as a type,
  and it is not a claim that the move was made.
- **A check-in outside play** ("what's your weather right now?"). This is a notification and needs its own
  `PermissionGrant` (purpose, audience, duration). Do not build it as part of the cave.
- **A reorientation line** on Release. The cave already walks back to the exact marker. Adding feet-and-seat on exit
  answers the Jennett reorientation caution at almost no cost.

Out of scope: biofeedback (heart rate in, as Mightier does). It would make the body signal real, and the ontology gives
the body a vote, but sensor data is a new data category with its own permission envelope and the report's child-data law
concerns. Not part of this task.

## decision_or_open_authority

Reach test run on each candidate question.

- *Is this for children?* The record answers it. The psychographic center is skilled helpers and adult near-neighbors;
  the community is adult. Position: the report's child findings serve as a conservative floor (externalized characters,
  concrete meters, no abstract self-report), and no kids' version is in scope. The audience decision is Wendell's if he
  ever wants one, and that would also bring the reserved consent and release items.
- *Should answers thin the shadow?* The record answers it (constitution 14 and 15, and the disclosure rule). Position above stands.
- *Which empirical claims may appear in the ontology?* Settled by the evidence authority rule. None, until retrieved.

No question reaches the board from this session. The three changes in `agency_and_consent` are positions, built only if
the next bars-engine session picks them up; they stand unless he flips them.
