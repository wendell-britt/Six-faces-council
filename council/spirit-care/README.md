# Spirit care: the return simulation

`sim.py` is the Challenger's test from spirit care pass 1 (`council/passes/6FACE_PASS_spirit-care1_2026-10-20.md`):
four players come back to mortal spirits, and the run writes down what each finds. Rerun it with
`python3 council/spirit-care/sim.py`; `--show A A` prints the return screens, `--days` the stage on each day. The
test is `tests/test_spirit_care_sim.py`.

Wendell's three `sc-` questions were not answered when this ran (2026-10-20), so every option of `sc-undying` and
`sc-after-death` runs. `sc-shadow-what` is not modelled beyond the source a shadow names.

## The numbers it runs on (first guess, for tuning)

| What | Value |
|---|---|
| Ladder | thriving, dimming, stale, shadowed, fading, gone; one step at a time |
| Fewest days in a stage before the next step down | dimming 2, stale 3, shadowed 4, fading 3 |
| Vitality | starts 100, falls 5 on a day with no care and no rest, rises 20 for any act of care |
| Clean Up | clears 35 shadow and adds 10 vitality |
| Shadow on an untended day | unworked charge 4, daemon pushed too far 5, broken agreement 6; never on a tended day |
| Mood (the existing 1 to 10) | falls one point for every third untended day, rises one for each act of care |

## What each player finds (council's recommendation, A and A)

| Player | Life | On return |
|---|---|---|
| daily | care every day, Clean Up every third day | thriving |
| busy | care one day in four, Clean Up twice | dimming, with the shadow's source named |
| rest | declared rest for ten days in the middle | exactly as it was when the rest began |
| vanished | care for a week, then three weeks of silence | Moss is gone and left a seed; Pip is fading |
| pair, one busy and one vanished | either person's care counts | dimming |
| pair, both vanished | | gone, and both were told when it reached fading |

Every return screen welcomes before it reports, names no count of days and no blame, and offers one quest that
cites a goal or an agreement, with "not now" as the other button. Every spirit that died had offered a quest at
stale and at fading first.

## What the run found

- **Three weeks of silence is the edge.** With these numbers a spirit dies 21 days after its last care, when its
  shadow is the daemon's own pattern. The vanished player comes back on the day Moss goes; a day earlier it would
  have been fading. Pip, whose shadow is a slower unworked charge, is still fading.
- **The stages are short for a weekly look.** Dimming lasts two days and stale three, so a player who looks in
  once a week can miss them. `sc-ladder` asks for each stage to be seen by a player who looks in once. Longer
  stages push death past three weeks.
- **Under `sc-undying` C no solo spirit dies.** Only a pair who both go silent loses one. Under B, the spirit
  bonded as undying (Pip) stops at fading.
- **The busy player is fine.** Care one day in four keeps a spirit between thriving and dimming. Finch's
  "any act of any size counts" holds.

## Not checked

The quests use a sample goal and a sample agreement, not his Lens goals or a real Between; bars-engine's
`generateQuestSuggestions` is mirrored, not called; one partner resting while the other is silent is not
modelled; nothing here is art or copy he has read.
