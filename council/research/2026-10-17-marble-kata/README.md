# Emotional Alchemy kata on the Marble skill line

Research, 2026-10-17. Wendell's words: "the emotional alchemy moves can be derived as developmentally appropriate kata
toward satisfaction mastery along that skill line. We'd also want to include AQAL if we can."

The direction behind it, from the same thread: children raise inner creatures, in the way the people in Ted Chiang's
*The Lifecycle of Software Objects* raise their digients, so they can learn and play with what is going on for them
before it creates adverse life experiences. The design draws on Pokémon, parts work, family constellations, play
therapy and psychodrama.

Ontology profile: `game_design` (QUICKSTART, the v0.1 vocabulary). Nothing here is built, and nothing here is a
question for Wendell.

## Sources

- **The Marble Skill Taxonomy v1** (https://github.com/withmarbleapp/os-taxonomy, cloned 2026-10-17). It has 1,590
  micro-topics for ages 5 to 14 and 3,221 prerequisite edges, each with a reason. The skill line used here is its
  Personal & Social Development subject: 88 topics in six domains. Some kata also draw on its Learning to Learn and
  Life Skills topics. Every topic in that subject that links to a standard links only to the IB PYP framework, and
  only as a code.
- **The fifteen moves**: bars-engine `src/lib/quest-grammar/move-engine.ts` (names, element pairs, energy) and
  `move-expressions.ts` (internal, interpersonal and systemic registers).
- **Elements and channels**: Sprout `docs/design.md`, the season table and the domain table (Wood joy, Fire anger,
  Earth neutral, Metal fear, Water sadness; domains ruled 2026-10-03).
- **The ontology**: `ontology/v0.1/QUICKSTART.md` and `source/design-ontology-v0.1.yaml`.

`map.py` holds the topic map and the kata list. It checks both against a clone of the taxonomy:
`python3 -I map.py <clone>`. It fails if a topic is left unmapped, if an anchor is missing, if a form is offered before
Marble places its idea, or if a form needs a hard prerequisite that the same move only offers in a later band. It passes
today: 88 topics, 42 kata, 45 anchor topics.

## What a kata is here

A kata is a practised form of one move, sized to an age band. A child does it with their creature, repeats it, and it
deepens in the next band. The child does the move before they can name it (constitution principle 8, "play precedes
complete understanding"). Marble's topics say when a child can usually understand an idea, which is often later than
when they can play it.

**Satisfaction mastery** follows the ontology's Transcend vector: a channel moves from dissatisfied, through neutral,
to satisfied. The child's own report governs whether it moved (`self_directed_authority: player_satisfaction_report`).
The child reports it about the creature: "how does Ember feel now?" That gives a symbolic route, so intimate disclosure
never becomes the price of progress. Mastery of a kata means the child can do the form and reports that it moves their
creature. The growth shows in the creature, and the child never wears a badge or a level.

Marble's `assessmentPrompt`s are questions for an adult who watches. In the ontology they are behavioral observation
(UR). They show what the child did under those conditions. They never show motive or global capacity, and they never
gate the game.

## The topic map

Each of the 88 topics gets a channel, the Basic Move it practises and the quadrant it mostly asks for. These are
research choices, listed in full in `map.py`. The totals:

| Axis | Count |
|---|---|
| Channel | Metal 19, Earth 15, Fire 12, Water 11, Wood 6, all channels 25 |
| Basic Move | Grow 39, Show 18, Wake 14, Clean 13, Open 4 |
| Quadrant | UL 30, LL 29, UR 15, LR 14 |

Three findings come out of the totals:

1. **Wood is thin.** Delight and Play gets 6 topics, against 19 for Metal (safety, risk, consequence, ethics). The
   taxonomy teaches children to be careful far more than it teaches them to be alive. The creature game has to bring
   Wood from its own design.
2. **Open Up is nearly absent.** Four topics touch breath, body or listening. None of the fifteen moves in bars-engine
   names Open Up either, so the move-engine's `primaryWaveStage` field never holds it. Open Up is the first kata a
   five-year-old needs, so it sits ahead of the fifteen below.
3. **Grow dominates.** Thirty-nine topics are concepts and vocabulary, which fits a curriculum. Clean Up (13) is where
   parts work lives, and most of it starts at age 6 or later.

## The kata

The bands are 5 to 7, 7 to 9 and 9 to 11. Each cell gives the form, then the Marble topics it practises with
their ages.

### Open Up, the breath before any move

| Band | Form | Marble anchors |
|---|---|---|
| 5–7 | The child and the creature breathe together until the creature's colour settles. | Simple Calming Strategies (5–7) |
| 7–9 | The child finds where the feeling sits in their body and in the creature's body. | How Emotions Feel in Your Body (7–9) |

WAVE is the name of the Open Up breathing practice, and its steps stay Wendell's. This kata uses the move without
claiming the steps.

### Transcend: one channel, from dissatisfied toward satisfied

| Move | 5–7 | 7–9 | 9–11 |
|---|---|---|---|
| **Fire, Achieve Breakthrough** (anger to boundary honoured) | Name the mad and say what isn't okay. *Naming Basic Emotions, Expressing Feelings with Words, Rules and agreements exist* | Name the line and what you want instead. *Resolving Disagreements with Friends, Understanding Bullying* | Hold the line out loud without attacking. *Assertive Communication, Peer Pressure and Resisting It* |
| **Water, Reclaim Meaning** (sadness to value restored) | Name the sad and what was lost, and ask for comfort. *Asking for Help, Coping with Life Changes* | Say why the loss mattered. *Friendships change over time* | Carry what mattered into what comes next. *Resilience and Bouncing Back* |
| **Wood, Commit to Growth** (joy to lasting aliveness) | Tend something a little every day and wait for it. *Patience and Delayed Gratification, Persisting When It's Hard* | Keep playing at what you can't do yet. *Growth Mindset* | Look back and see how you have grown. *Personal Growth Over Time* |
| **Metal, Step Through** (fear to opportunity) | Name the scared, then take one small step with a grown-up near. *Everyday Safety Awareness* | Tell scary-and-safe from scary-and-unsafe. *Actions and Their Consequences, Feeling of not understanding* | Check the first scary read before acting on it. *Questioning First Impressions* |
| **Earth, Stabilize Coherence** (neutral to clarity) | Find the still spot. *Simple Calming Strategies* | Notice the whole body at once. *How Emotions Feel in Your Body* | Notice the pattern over weeks. *Emotional Patterns Over Time* |

### Generative: one channel feeds the next (Wood, Fire, Earth, Metal, Water)

A Generative or Control move needs two channels at once. Marble names that only at 9 to 11 (*Mixed and Conflicting
Emotions*), but children feel it much earlier. So these kata are played from 5 or 7, and the child names them at 9
to 11.

| Move | 5–7 | 7–9 | 9–11 |
|---|---|---|---|
| **Wood to Fire, Declare Intention** | Say what you want to play. *Expressing Feelings with Words* | Make a little plan for it. *Making a Simple Plan, Planning a Task* | Set a goal of your own. *Personal Goal-Setting* |
| **Fire to Earth, Integrate Gains** | After the game, tell a grown-up what happened. *Expressing Feelings with Words* | Find what the mistake taught. *Learning from Mistakes* | Reflect after something hard. *Reflecting After Learning* |
| **Earth to Metal, Reveal Stakes** | — | Stop and say what matters before you start. *Thinking Before Starting, Stop, Think, Then Choose* | Weigh a hard choice. *Difficult Ethical Choices* |
| **Metal to Water, Deepen Value** | — | Say why a choice is right or wrong. *Right and Wrong Choices, Understanding Why* | Feel what the fear is protecting. *Emotions and Decision-Making* |
| **Water to Wood, Renew Vitality** | — | After a change, plant something new. *Coping with Life Changes* | Let the loss feed what grows next. *Resilience and Bouncing Back* |

### Control: one channel checks another, at a cost that prevents a larger loss

| Move | 5–7 | 7–9 | 9–11 |
|---|---|---|---|
| **Wood to Earth, Consolidate Energy** | Wait your turn while the creature waits too. *Patience and Delayed Gratification, Taking Turns and Sharing* | Break the big excitement into steps. *Breaking Tasks into Steps* | Spend attention on purpose. *Time and Attention Management* |
| **Fire to Metal, Temper Action** | The creature can be mad without biting. *Feelings Versus Actions* | Stop, think, then choose. *Stop, Think, Then Choose* | Notice what the anger wants to decide. *Emotions and Decision-Making* |
| **Earth to Water, Reopen Sensitivity** | — | Notice the "I'm fine" that isn't. *Hidden and Masked Feelings* | Look at your own part in a friendship. *Self-Reflection in Relationships* |
| **Metal to Wood, Activate Hope** | Try once more when it's hard. *Persisting When It's Hard* | Talk back to the scared voice, and try a new way. *Positive Self-Talk, Trying a New Approach* | Learn from failing. *Learning from Failure* |
| **Water to Fire, Mobilize Grief** | — | Say "that's not fair" for someone else. *Fairness, Equality and Equity, Bystanders and Upstanders* | Name unfairness that happens to groups. *Prejudice and Discrimination* |

Five cells stay empty at 5 to 7, and Marble has no topic for them. Each of those five moves has a 5-to-7 form, but
the forms have to come from play design. One example for Mobilize Grief: the creature is sad that a friend's creature
was left out, and the child helps it go and say so.

## Parts work in the map

The creature is the part. The child's steady attention plays the role IFS gives to Self. Four Marble topics carry most
of the parts work, in kid language:

- *Feelings Versus Actions* (6–8): a part can feel something strongly without taking over. This is unblending, and
  it anchors Temper Action at 5 to 7.
- *Hidden and Masked Feelings* (7–9): a part that hides what another part feels. This is a protector, and it anchors
  Reopen Sensitivity.
- *Mixed and Conflicting Emotions* (9–11): two parts present at once. Here the child can name a Generative or
  Control move.
- *Honest Conversations and Conflict Repair* (12–13): repair between people. Family constellation and psychodrama
  belong here and in the LL quadrant.

The game never tells the child which part a creature is or what it means (principle 10). The kata give the child
forms to try, and the child's report decides whether a form helped.

## AQAL attention

bars-engine's move expressions already give each move three registers: internal, interpersonal and systemic. The three
map onto UL, LL and LR. The kata's form, what the child does with body and voice, supplies the fourth,
UR. So each kata covers all four quadrants:

| Quadrant | In a kata | Evidence it can give |
|---|---|---|
| **UL / I** | What the child feels, and how they say the creature feels after the form | Player report: satisfaction, which governs |
| **UR / It** | The form itself: breath, words, waiting, stepping, the creature's visible change | Behavioral observation, including Marble's prompts; never motive |
| **LL / We** | The caregiver who plays alongside, the friend's creature, the family on the board | Relational attestation from the other person |
| **LR / Its** | The growth tree (Marble's graph), the bands, the rule that a creature is never reset or deleted | System trace: what was offered and done |

- **Lines made consequential**: emotional, somatic, relational and rest_refusal_release. A child can always pass on
  a kata, and the creature can rest.
- **States invited**: calm, brave, sad and mad all count as states the play invites. None of them is written down as
  a trait of the child.
- **Types**: Marble's age bands describe a typical child, and a child who is ahead or behind is neither. Band sets
  which form is offered. It never ranks the child (hard boundary: no global developmental rank).
- **Allyship**: *Helping Others Resolve Conflicts* and *Systemic Inequality and Allyship* reach into other people. In
  those forms, the child's satisfaction does not show that they helped. The other person's word does.
- **Grammar boundary**: the fifteen moves are kept apart from the legacy translate/transcend grammar in
  `emotional-alchemy.ts`. The two are never merged by label.

## Risks and tests

- **Masks as curriculum.** A child with developmental trauma may have protectors for good reasons. A kata that
  works on *Hidden and Masked Feelings* must stay at the creature's level and let the child pass. Test: a clinician
  who works with traumatized children reads the Clean Up and Water kata before any child plays them.
- **The map is a choice.** The channel, move and quadrant assignments are one reading. Test: the six faces or a
  second reader re-map ten topics blind, and we compare.
- **Licensing.** The topic titles and the age data are Marble's. A product that ships this map ships a derivative
  database under ODbL and CC BY-SA text, with attribution. A design built from it, with our own words, owes nothing
  back. The research use here carries the attribution in `map.py`.
- **Empty Wood.** The game needs its own source for delight. Sprout's Wood village (planting, pruning, play) is the
  nearest one in the record.

## Where it could land

- **Sprout Plot.** It has the five elements, the cozy pace, spirits that grow with satisfaction, and "Ting shows what
  the spirit needs". The kata could become what a child does with a spirit between fights, ordered by band.
- **bars-engine.** It has the move engine and the registers. A `kata` table keyed by move id and band would be the
  smallest change. Nothing is specced.
- **The Between** (callsheet `relationship-creature`). It is the adult, two-person form of the same idea, so its
  co-tending rules are the nearest model for the caregiver-and-child LL layer.

The open work is in `council/callsheets/inner-creatures.md`.

Attribution: Marble Skill Taxonomy (v1), © Generative Spark, Inc. (Marble), https://withmarble.com, licensed under ODbL
1.0 (database) and CC BY-SA 4.0 (content).
