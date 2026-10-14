# Perceptual shadow (WAVE room)

Started 2026-10-14 from Wendell's message in the project thread "Perceptual shadow for WAVE". Code lives in
johnair01/bars-engine `content/ontology-game/cave/cave.js` (the WAVE room, `openRoom`), stacked on #324 (which is
stacked on #317). Board rows: `rows/perceptual-shadow-2026-10-14.json`.

## His words (2026-10-14)

"This is around perceptual shadow specifically the shadow that stops players from being able to see or hold their
attention on charge. The 4 shadows are forgetting, distracting, dissociating, and numbness. Numbness collides with the
blocker numbness but they also do similar work and it's why perceptual shadow can exist. It's hiding charge from the self
so that it can't be dealt with or worked with. From a skill development standpoint perceptual shadow is only triggered
when peopel report they are aware of a charge but not about to perceive it and if they aren't able to get the charge
number down. I imagine there's a polarity (alongside size, and brightness) that's also able to occlude charge spirits as a
function of emergent perceptual shadow"

## The design (positions; each stands unless he flips it on the board)

- **What it is.** A perceptual shadow hides a charge from the player so it cannot be worked. It is never a step every
  player sees: the room shows it only when one of his two signals fires.
- **The two signals** (`ps-trigger`). Either one raises the shadow, and they stack:
  1. *Aware but can't perceive.* Witness has a third answer, "I know it's here, but I can't feel it". Polarity rises by 6.
  2. *The number won't come down.* A round whose charge reading after is not lower than before (the 3-2-1's readings,
     or the board run's 0 to 10 before and after). The round's end offers "Look again for what's hiding it"; the next
     creature comes in as the hidden part of the last one, with polarity raised by 4 over what it carried.
  His sentence joins the two with "and"; the build reads them as two ways in, since they happen at different moments of a
  sitting (Witness, and the end of a round). Flip to "both" on the board if he meant both at once.
- **The four shadows** (`ps-four-kinds`). When the shadow rises the player names it, with a line each, or says "I can't
  tell" (an unnamed shadow, worked with the plain practice "Look again, slowly").
  | Shadow | What the player feels | How it hides the creature | The practice that thins it |
  |---|---|---|---|
  | Forgetting | It slips out of mind as soon as I turn to it | It fades in and out | Say its name out loud, slowly, three times |
  | Distracting | Something keeps pulling my attention away | It drifts aside | Name what pulled you away, then come back |
  | Dissociating | It feels far away, like it's someone else's | It stands back toward the door, greyed | Feel your feet and your seat, then look again |
  | Numbness | Where it should be there is only blank | A grey fog wraps it | Find the edge of the numb: where feeling starts again |
- **Numbness, twice** (`ps-numbness-link`). The numbness texture (a blocker: how the charge feels) and the numbness
  shadow (what hides it) stay separate. They link: when the creature's texture is numbness, the shadow page names the
  overlap ("Numbness is how it feels, and also what keeps it out of reach") and puts Numbness first. The shadow's fog
  uses the numbness texture's grey, so the two read as kin.
- **Polarity** (`ps-polarity`). A third property beside size and brightness, 0 to 10, on every creature and spirit. Size
  and brightness are the player's sliders on Allow; polarity is emergent: only the two signals raise it, and only the
  practice lowers it (3 a time). Allow shows it as a third reading, not a slider. At 0 the creature is clear; at 10
  only a faint outline shows and its aura is dark. The player can go on with the creature still veiled.
- **Spirits** (`ps-spirits`). A creature that leaves as a spirit carries its polarity out: a veiled spirit in the cave
  glows dimmer, by the same rule.
- **The run** (`ps-run-record`). Each round in the board run records `shadow: { kind, polarity, start, signals }` and its
  readings, so the council can see when shadow came up and whether the practice thinned it.

## Answered on the board

- `ps-polarity-poles`, 2026-10-14: "two". Polarity runs -10 to 10; below 0 the charge floods. Built in bars-engine #326:
  Witness's "It's too much to be with" (-6); a round stuck at 9 or 10 that does not come down points the second signal at
  flooding (part comes in at its polarity minus 4); the creature grows past its allowed size, blazes past its allowed
  brightness and glares in its own colour; three practices turn it down by 3 each (long out-breath behind the seat, name
  one thing that isn't it, picture it at arm's length). Flooding has no kinds. The run records `shadow.pole`. Hidden
  still means polarity above 0, which the dissolving thread reads.

## State

- 2026-10-14: both poles built in bars-engine #326 (stacked on #324 and #317), shadow-test 41 of 41.
