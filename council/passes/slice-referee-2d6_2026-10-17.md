# The referee on a 2d6 table (story encounter and faction)

**2026-10-17**, a short answer thread, not a pass. Wendell answered `q-slice-referee-clear-2` B at 20:17 UTC (ledger
`council/ledger/2026-10-17-pull-201904.json`): *"So the system in place id want to model for story beats the
apocalypse engine. So the idea that there are ranked outcomes and negative outcomes roll against a table (the 2d6
model)"*. The ontology QUICKSTART is the only ontology loaded. The earlier example is
`council/passes/slice-referee-worked-example_2026-10-17.md`; Mara and the Tenders come from it. The band edges (10 and
7) are Apocalypse World's own. Every modifier, cost and consequence below is a placeholder.

## What changes from the second example

The five steps stay. Two of them change shape for story beats:

- **Step 3** was "odds, then one roll against a percentage". It becomes **roll two six-sided dice and add a
  modifier**. The modifier is the fit from step 2.
- **Step 4** was "lands or misses". It becomes **three ranked results**, read off one table:

| Total | Result | What happens |
|---|---|---|
| 10 or more | **Hit** | You get what you went for, cleanly. |
| 7 to 9 | **Partial** | You get it, with a cost or a hard choice. The player picks the cost from a short list. |
| 6 or less | **Miss** | It goes wrong. The referee takes the next consequence from the other side's ranked list. |

Battle keeps its percentage odds for now, because his steer named story beats. Its logbook line has the same shape,
so it can move to the table later without touching the story side.

### The modifier (step 2 becomes a number)

| Fit | Modifier |
|---|---|
| You listened first (Attune; it spends a beat) | +1 |
| What you bring matches what they need | +1 |
| What you bring misreads them | −1 |
| Standing with their faction (faction rolls only) | + standing |

The modifier is capped at +3, as in Apocalypse World. The player sees the three chances before choosing:

| Modifier | Hit | Partial | Miss |
|---|---|---|---|
| −1 | 8% | 33% | 58% |
| 0 | 17% | 42% | 42% |
| +1 | 28% | 44% | 28% |
| +2 | 42% | 42% | 17% |
| +3 | 58% | 33% | 8% |

Listening and matching (+2) makes a miss rare and never impossible. Guessing wrong (−1) makes a miss likely and a hit
still possible.

### The ranked negative list (what a miss does)

Each faction carries its own list of consequences, ranked from mildest to hardest. On a miss with any member, the
referee takes **the next rung down**. It never picks freely, so the engine stays predictable and every miss is
written down. A hit with a member climbs one rung back up. The Tenders' list:

1. **Cool.** The member steps back. Their trust drops 1.
2. **Talk.** The Tenders hear the worst version. Standing drops 1.
3. **Close a door.** The compost circle is shut to you until standing is back to +1.
4. **Act.** The Tenders take back their seed share. Compost earns less each day until the rung is climbed back.
5. **Rupture.** The relationship breaks, as a rupture does in the trust loop. Only a repair scene reopens it.

A miss always moves something: in Apocalypse World a miss never means nothing happens. **Show Up Honestly** stays the
safe move. It does not roll, moves nothing up or down, and never costs a rung.

## Scene 1: a story encounter (Mara at the gate)

Same morning as before: a logbook line from yesterday reads `offering … fed: no`, so Mara of the Tenders comes to the
gate. The player listens first and learns she needs the plain truth about the field (Earth). The player plays the
Earth card, "Tell it plainly". Modifier +1 (listened) +1 (match) = **+2**. Chances shown: hit 42%, partial 42%, miss
17%. Tenders' list marker: at the top, no rungs taken.

Three ways the same roll can go:

**On a hit**, dice 5 + 4 = 9, plus 2 is **11**. Mara's trust goes 3 to 5, the Tenders' standing goes up 1, and she names
one other Tender's need, so the next talk with that neighbor starts as if the player had listened.

`day 4 | talk | Mara of the Tenders | listened, match | card: tell it plainly | 2d6+2 | 5+4 → 11 | hit | trust 3→5 | Tenders +1 | learned: Ferro needs Water`

**On a partial**, dice 3 + 3 = 6, plus 2 is **8**, so she takes the player's word, with a cost. The player picks one:

- She trusts you, and asks a favor: a day's chore at the Tenders' field (a promise in the logbook, and a door later
  if it is kept or broken).
- She trusts you, but keeps it to herself: trust goes up, the Tenders' standing does not.
- She half believes you: trust goes up 1 now, and up 1 more only when you show her the field.

`day 4 | talk | Mara of the Tenders | listened, match | card: tell it plainly | 2d6+2 | 3+3 → 8 | partial | cost: a day at their field | trust 3→5 | Tenders +1 | promise: day 5`

**On a miss**, dice 1 + 2 = 3, plus 2 is **5**. The referee takes the first rung of the Tenders' list: **Cool**. Mara
steps back and her trust drops 3 to 2. The beat is spent. Show Up Honestly is still on the table.

`day 4 | talk | Mara of the Tenders | listened, match | card: tell it plainly | 2d6+2 | 1+2 → 5 | miss | rung 1 cool | trust 3→2 | Tenders 0`

If the player had guessed and played the wrong card, the modifier is −1 and the miss is the likely result (58%).

## Scene 2: a faction relationship (asking the Tenders)

Two days later the player wants the Tenders to share seed for the burned field. This roll is with the group, not a
person, so the modifier is the standing. After Mara's hit, standing is +1: chances hit 28%, partial 44%, miss 28%.

**On a hit**, dice 4 + 5 = 9, plus 1 is **10**. They share the seed, and standing goes up 1 to +2. That opens the door
from the second example: *Tenders standing 2 or more*, so the compost circle invitation fires.

`day 6 | ask | the Tenders | standing +1 | request: seed for the burned field | 2d6+1 | 4+5 → 10 | hit | seed: yes | Tenders +1→+2 | door: compost circle`

**On a partial**, dice 3 + 4 = 7, plus 1 is **8**, so they share it, and the player picks one:

- You owe them a day at the compost circle.
- They share half.
- One of them stays wary: the next miss with that Tender takes two rungs instead of one.

`day 6 | ask | the Tenders | standing +1 | request: seed for the burned field | 2d6+1 | 3+4 → 8 | partial | cost: half the seed | Tenders +1 (no change)`

**On a miss**, suppose Mara's talk missed on day 4 instead: standing is 0 and rung 1 is already taken. Dice 2 + 3 = 5, plus
0 is **5**. The referee takes the next rung down, rung 2, **Talk**: the Tenders hear the worst version, and standing
drops 1.

`day 6 | ask | the Tenders | standing 0 | request: seed for the burned field | 2d6+0 | 2+3 → 5 | miss | rung 2 talk | Tenders 0→−1`

## What the faction is now

A faction is two records the referee keeps, both moved only by logbook lines:

- **Standing**, a number. Hits raise it, rung 2 lowers it, and it is the modifier for rolls with the whole group.
- **A marker on its ranked list.** Misses push it down one rung, hits climb it back one.

Story doors are conditions on those two and on the logbook: `Tenders standing ≥ 2`, `Tenders rung ≥ 3` (a scene
where someone from another faction offers seed instead), `promise day 5 not kept`. Switch the referee off and none
of the lines are written, so Mara never arrives, the marker never moves, and no door opens. That is pass 2's
`slice-referee-off` test, unchanged.

## The three examples side by side

| | Battle | Story (2nd example) | Story and faction (this one) |
|---|---|---|---|
| Step 2: fit | the five-element chart | listened, matched | listened +1, matched +1, misread −1, or standing |
| Step 3 | one percentage roll | one percentage roll | 2d6 plus the modifier |
| Step 4 | lands or misses | lands or misses | hit, partial (player picks the cost), miss (next rung down) |
| A miss | beat spent, Listen stays | beat spent, trust drops | the faction's next consequence; Show Up Honestly stays |
| Step 5 | one line | one line | one line, with the dice, the band and what moved |

The player's own state is still never rolled. The referee rolls only for what the player does and how the other side
answers.

## What this leaves open

- Every modifier, cost list and rung is invented for this example. Real lists are content for each faction, written
  after the engine runs. Test 5's bots can report how often each band comes up.
- Whether battle moves to the 2d6 table too. His steer named story beats, so battle keeps its percentage here.
- Apocalypse World's descendants mark experience on a miss. That would fit "composting is valid completion", and it
  is left out here because nothing in the slice tracks experience yet.
