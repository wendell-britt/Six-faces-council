2026-10-14
# Dissolving spirits (ice to water to gas to pure spirit)

## Next
- Wendell, 2026-10-14 22:24 (thread "Dissolving spirits into mana"): "Players can also dissolve charged spirits (a form of
  dismissal) by going through a form of WAVE-like process. 'Ice to water water to gas gas to pure spirit'. Ice in this case is
  the current density of the charge (allies being the highest density) and charge sprites in their particle form being their
  gas style energy. Pure spirit is mana itself. This is how players can increase their own stats by taking spirits into
  themselves instead of using them as allies".
- First build (2026-10-14): bars-engine `content/ontology-game/cave/dissolve.js`, wired into the cave's spirit card (a third
  way beside breathe it out and take it home), branch `claude/project-thread-dnhcby`, draft bars-engine #327, stacked on #324. cave-test 397 pass, 0 fail. DESIGN.md "Dissolving
  a spirit into yourself". Positions on the board: `sd-density-ladder`, `sd-mana-to-stat`, `sd-gone-after`, `sd-shadow-skip` (rows
  `council/callsheets/rows/spirit-dissolve-2026-10-14.json`). No question survived the reach test.
- Next, after his play: carry dissolving to the Big Mind cave's spirits (`bigmind.js` letGo) and to the spirit generator's
  allies on sprout #51 (its forms already sit on the ladder through `FORM_STATE`), and let the player's stats from mana feed
  the fight once the generator's allies and the cave share a player.

## Fits with
- Perceptual shadow (thread "Perceptual shadow in WAVE", bars-engine branch `claude/project-thread-8r44dc`): a spirit with
  `polarity` above 0 is hidden and is not offered for dissolving until it is seen. The two branches touch different lines of
  cave.js; whichever lands second merges onto the other.
- `sg-overcharge` (taking in more charge than your character can handle has consequences) is not applied to dissolving yet.

## Waiting on
- His play of dissolving in the cave (page from the merged branch).
