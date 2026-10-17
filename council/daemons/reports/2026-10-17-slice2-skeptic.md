# Skeptic, for the Challenger: where Pokémon's balance broke, and whether Sprout's chart is a lookup

## The cast
Hexagram 36 Nightfall becoming 7 Muster: the light is hidden, so the fact that would organise the chart is unsaid. Muster asks for discipline over a larger force. I treat the unsaid fact as "what does the player know when they pick a stance?", and I weigh the moves by that.

## The interview
- My job here: doubt that a Pokémon-style chart is what makes this fight interesting.
- How: read fight.js, simulate the numbers by hand, and cite what Pokémon and other cycle games did.
- Hours for Wendell: about 1 hour to read this and about 2 hours to try the cheapest fix.
- Pay: a fight where the stance choice matters, not a lookup.
- Who I work for: Wendell, as first player of Sprout Plot.
- What I doubt: that the cycle plus stats alone makes choices. Doubt serves him by catching a dull fight before the playtest. Without me, the controlling-stance spam ships unnoticed.

## Wake Up
- fight.js: `relation()` gives five outcomes. Controls does 8 to both hp and demand, same does 3, generatedBy does 2, generates feeds +3 satisfaction, and controlledBy costs the player 4. The spirit always pushes 2.
- The numbers sit in /home/user/sprout/data/slice.json (`fight`: playerHp 20, damage 8/3/2, feed 3, hurt 4, push 2, mood 3/6). Spirit stats are 20 hp and 10 demand in spirits.json, and 16 and 8 in daemons.json.
- There is no per-stance cost, cooldown, accuracy or stat. All five stances are always available. `listen` reveals what the spirit needs, and the push text hints at it.
- Pokémon facts:
  - Gen I Psychic was the balance problem. Dark and Steel in Gen II were the fix. Psychic was also immune to Ghost, apparently unintended [1].
  - Fairy arrived in Gen VI against Dragon [1]. I found no direct Game Freak quote for the motive [2].
  - Normal has no super-effective row [3].
- Pokémon damage runs on level, Attack and Defense, move power, a roughly 1.5x same-type bonus and a random factor [4]. The depth comes from dual types, limited move pools, switching and stats, none of which Sprout has.
- Magic's pie has five colours, and five is the lowest number that gives every colour equal allies and enemies [5].
- RPSLS gives each option 2 wins and 2 losses, and ties drop from 1/3 to 1/5 [6]. Odd cycles have a unique mixed equilibrium [7].
- I found no source on Ōkami, Avatar or wuxing as game balance. That is a gap, not a finding [8].

## Open Up
Unranked: cost per stance; stance cooldowns; a stamina meter; spirit resistances; dual-element spirits; accuracy; a limited stance deck; a stat per stance; a tempo clock; fewer visible tells; pushText only as the hint; a controlling hit that raises the spirit's anger; a chart on screen; a playtest log; a simulation.

## Clean Up
- Pure-cycle test (reasoning, not a source). With identical relations, the best reply to a known element is always the same stance. Stats can only make choices if stances differ in cost or risk.
- Sprout's chart is not fully dominant, because the controlling hit hurts the goal: a third hit dismisses the spirit with no ally.
- The real dominance problem is the first turn. After `listen`, the chart is a one-step lookup.
- Same (3) and generatedBy (2) are the two guessed relations. They are cheap to cut or give a job.
- Readability: Legends: Arceus put the chart in-game [9]. Sprout's two-step wuxing rule is learnable and explainable by image.

## Grow Up
- Simulate: script the fight to a win-rate table for each policy (always control, control-then-feed, random).
- Read Rosewater's primary pie articles and a wuxing-in-games source.

## Show Up
1. Simulate "always controls" against "2 controls, 2 feeds, offer". Make sure the first earns less.
2. Give each stance a cost: a cooldown or limited uses.
3. Give same and generatedBy a distinct job, or cut them.
4. Make `listen` cost a turn so the guess has weight.
5. Add spirit variation (resists, hp and demand) before adding more chart entries.

## For the Player
This protects Wendell from shipping a chart that is a lookup table. It makes the fight a real negotiation: restrain, then feed.

## Your questions
1. Which spirit stats does the fight read, spirits.json (20/10) or daemons.json (16/8)?
2. Does the offering formula reward demand near 0 more than satisfaction?

## Where you would overreach
I would call the chart dominated before anyone has run the numbers above.

## Sources
1. https://bulbapedia.bulbagarden.net/wiki/Psychic-type
2. https://www.pokecommunity.com/goto/post?id=7580127
3. https://bulbapedia.bulbagarden.net/wiki/Type_chart_(Generation_IV)
4. https://bulbapedia.bulbagarden.net/wiki/Damage
5. https://mtg.wiki/page/Bend and https://casualplaneswalker.com/wiki/color-pie
6. https://www.johndcook.com/blog/2018/08/07/rock-paper-scissors-lizard-spock/
7. https://animorepository.dlsu.edu.ph/etd_bachelors/14923
8. https://okami.fandom.com/wiki/%C5%8Ckami?oldid=9066
9. https://automaton-media.com/en/news/20220131-9111/
10. https://consolepulse.com/nintendo/pokemon/guides/pokemon-type-matchups-explained
