# Controller, for the Architect: Pokémon's type chart, moves and stats

## The cast
Hexagram 26 becoming 19: Reserves has stored power and must now spend it. Sprout has held the chart's shape (the cycle) but never named the day its numbers get stats. I weigh moves toward naming one tuning table, not a perfect one.

## The interview
- My job: set the standard for Sprout's balance by reading Pokémon's model.
- How: read the sources, compare them to fight.js, and carry back at most five moves.
- Hours: about 1 to 2 for Wendell to read this and pick moves; each move is small code or data.
- Pay: a fight where stance choice and spirit stats both matter, and numbers that have reasons.
- Who I work for: the Player (Wendell), not control itself.

## Wake Up
Sprout today: relation() in /home/user/sprout/slice/fight.js gives five fixed outcomes, and damage comes from cfg.fight.damage by relation alone. Spirits have only maxHp and demand. Stances have no power and no stats feed damage. The "same" (3) and "generatedBy" (2) values are builder guesses.

Pokémon facts found:
1. Type chart: it has 18 types and 324 matchups. One guide counts 51 at 2x, 61 at 0.5x, 8 at 0x and 204 neutral (derived, not stated by the article). The grid is attacker by defender, so it is not symmetric [1]. Dual types multiply the two numbers (4x, 0.25x), and an immunity overrides a weakness [1].
2. Damage: Bulbapedia's pages returned 403, so I could not quote the formula. Search snippets confirm STAB is 1.5 when the move shares a user type, type effectiveness applies per defending type, and the random factor is 0.85 to 1.00 [2][3]. The full formula is from my memory only: floor(floor(floor(2L/5+2) × Power × A/D)/50)+2, then times STAB, type and random. Treat it as unverified until someone opens Bulbapedia's Damage page.
3. Physical/special split: before Gen IV a move's type decided whether it used Attack/Defense or Sp.Atk/Sp.Def. From Gen IV each move carries its own category, so Sneasel's Ice and Dark moves no longer waste its stats [4].
4. Balance by addition: Fairy came in Gen VI (Dark and Steel in Gen II) [5]. Masuda said it was made to counter Dragon, and that weakening Dragon would have been sad [6]. Dragon was weak only to itself and Ice before. Fairy resists Fighting, Bug and Dark, is immune to Dragon, and hits Dragon super effectively [1][6].
5. Power, accuracy, PP, coverage moves and per-type stat spreads: I did not find a citable source.

## Open Up
Spirit Attack/Resist stats; stance power; STAB for a player's own element; a 0x immunity; a status stance that moves Demand or mood; a random roll; dual-element spirits; coverage stances; accuracy as a "listening" check; a sixth element as a check (Fairy model).

## Clean Up
Blockers: no primary source for the formula; Sprout's chart is a cycle, so each element has exactly one of each relation. Pokémon's chart is mostly neutral (204 of 324 by the count in [1]). Sprout's has none neutral, so the 2x/0.5x logic does not transfer directly. Composted: accuracy and PP (no stat to hang them on) and a sixth element (CLAUDE.md says not to change rules).

## Grow Up
Open Bulbapedia's Damage page in a browser and confirm the formula. Read Smogon's damage-calc notes. Write a table of the 25 stance-by-spirit cells with proposed numbers before touching code.

## Show Up
1. Keep the five relations as the "type multiplier" row: controls 2.0, generates feed, same 1.0, generatedBy 0.5, controlledBy hurts.
2. Add to each stance a `power` and to each spirit `attack` and `resist`. Damage becomes power × multiplier × (1 + attack/resist term).
3. Candidate STAB: a stance matching the player's own element gets ×1.5. Candidate status moves: Listen (Ting) and offer already act this way; add stances that change Demand or mood without damage.
4. Candidate special/physical split: a stance either lowers Demand (pressure) or raises satisfaction (feed), each using its own spirit stat.
5. The Fairy lesson as a check on the strongest spirit: give the strongest element a deliberate weakness or low resist, not a nerf.

## For the Player
This protects Wendell from tuning by guess. It makes fights feel earned, because the spirit's nature and the stance's power both matter.

## Your questions
1. Should satisfaction have its own multiplier (generates is more effective on a sad spirit), or stay flat at +3?
2. Is "player's own element" a stat the player has, or is it chosen per fight?

## Where you would overreach
I would hold the numbers back until the formula is verified and the whole grid is perfect, when one first table would do.

## Sources
1. https://billsarchive.com/articles/pokemon-type-chart.html
2. https://bulbapedia.bulbagarden.net/wiki/Damage (search snippet only; page returned 403)
3. https://bulbapedia.bulbagarden.net/wiki/Special:Diff/2488007 (snippet)
4. https://bulbapedia.bulbagarden.net/wiki/Damage_category (snippet)
5. https://bulbapedia.bulbagarden.net/wiki/Elemental_types (snippet)
6. https://www.nintendojo.com/news/fairy-pokemon-result-of-unfair-dragon-advantage (snippet)
