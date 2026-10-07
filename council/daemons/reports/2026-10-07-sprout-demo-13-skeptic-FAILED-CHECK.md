## The Skeptic's Report: Weapon Attack Split

### The cast

Hexagram 62, Overstep, becoming 51 Shock, speaks directly to this split. Overstep is the step taken when resistance appears; Shock is the waking-up that happens when the boundary is crossed. The counsel is that pressing where there's resistance ends in collision. This design question reveals the collision at the boundary: the moment you add weapons, you test whether the battle can hold both a mechanical shortcut and a teaching intention. Shock here is the playtest that shows which one wins.

### The interview

My job here is to test whether the weapon split survives contact with a player. How I would do it: name what the evidence would need to show, run the cheapest test that would show it, and report what broke. The hours this costs the Player are the time spent building a weapon system that may not hold. The pay the Player gets is the certainty that WAVE teaches what it is meant to teach, or the discovery that the design needs to be one system, not two. I work for Wendell and for the game's core lesson.

### Wake Up

The record already holds what matters. The bot test in round 5 set a falsification threshold: "If Acknowledge spam wins as fast as full WAVE, Welcome is decoration and the design failed" [1]. The test passed, but it tested one thing only: whether the four steps of WAVE form a coherent system. It never asked whether a player with a third choice (weapon attack) would use WAVE at all.

The design says the spirit fight is not push hands; stances act as elements, like Avatar bending, and attacks do damage [2]. This is a combat system. The proposal to add weapons is to add a second combat system inside the first one. The question is not whether they both work separately; it is whether having both destroys the lesson.

What the existing evidence shows: WAVE finishes at 100% with 14 HP left; answer spam finishes at 68% with 10.1 HP [1]. Both finish. The test measured whether WAVE was efficient. It never measured whether a third option (weapon spam) would dominate both.

### Open Up

The moves I could make on this problem:

1. Run a three-policy bot test. Test weapon spam alone on the spirit fight, then compare its win rate and HP efficiency against WAVE and Acknowledge spam. If weapon spam wins faster and with higher HP, it is the dominant strategy and the split fails.

2. Identify the exact condition that breaks the design. Is it HP efficiency? Turn speed? Certainty of landing? Simplicity? Which one, if any, makes a player skip WAVE?

3. Test a teaching condition, not just a bot condition. Give a cold player the three options (WAVE, Acknowledge spam, weapon spam) in a test fight and observe which one they choose, and whether they learn the lesson after choosing. The bot test measures efficiency; this measures adoption.

4. Model the decision tree a player faces. What does the button layout show? If weapon attack is one big button and WAVE is four steps, does layout alone drive the choice? If the cost (mana, turns, landing chance) differs, which cost drives the choice?

5. Ask whether "split" is the real proposal. Maybe weapons are not a third combat system but a fourth WAVE step (like Exhale ends, maybe attack finishes). That would not be a split; it would be an addition to the existing loop. Clarify what Wendell means by "split."

### Clean Up

Three blocks stand out.

The evidence for the split failing is not yet defined. Wendell said "test that split hard," but the record does not say what would count as a hard failure. Would it be: weapon spam wins? Or: a playtester skips WAVE? Or: the bot wins faster with weapons? Or: a player cannot explain what Welcome does because they never had to use it? The test needs a falsification condition before the build.

The teaching intent gets lost in bot testing. Round 5's falsification test measured efficiency (HP left), not learning (whether the player understood the lesson). Round 11's tests are better—they measure learning—but only on WAVE alone [1]. A three-option test needs to measure whether a player who chose weapon spam still learned that WAVE is a move they can use on real feelings. If they did not learn it, the split failed even if weapons are fun.

The "regular attack system" is not defined. Is it a stat-based damage roll, like Pokémon? A fixed damage number? Mana-based like the dojo moves? Does it scale with Root level or talismans? Does it cost anything, or is it free? Until that is clear, the bot test cannot even run.

### Grow Up

The test design needs to measure two things that the existing bot tests do not. First, which option a player chooses when all three are available (efficiency does not predict adoption). Second, whether the player learns the lesson regardless of which option they chose. A player who chose weapons but still learned that WAVE teaches a real move means the split succeeded. A player who chose weapons and forgot WAVE within thirty minutes means the split failed.

### Show Up

The five moves:

1. Run a bot test with three policies on the built spirit fight: full WAVE, Acknowledge spam, weapon spam. Record win rate and HP left for all three. If weapon spam exceeds WAVE on efficiency, the split fails the falsification test. Deliver the data before the playtest.

2. Set a falsification condition in writing. Write one sentence: "If [condition], the weapon split fails and weapons are cut." Examples: "If weapon spam wins 80% of the time against WAVE's 100%," or "If a cold player chooses weapon spam in round one and never tries WAVE." Get Wendell's agreement before the build.

3. Build the weapon attack system as a minimal slice. Do not build for balance; build for speed of test. One damage number, one button, one cost (mana or free). Let the bot test answer whether it dominates, before building UI, scaling, or tuning.

4. Run a human test on the taught fight before the strip. Round 11 set a test: a cold player finishes the taught fight and says what Welcome does [1]. Add this condition: after the taught fight, offer a test fight with weapon attack available. Does the player use it? Do they still remember Welcome? If they use weapons and forget Welcome, the lesson broke in the first 30 minutes.

5. Record the cost and the break point. If the test shows the split fails, Wendell's decision to cut weapons avoids a full build. If it shows the split holds, the build lands with confidence. Either way, the evidence is in the data, not in the design.

### For the Player

This protects the Player from building a weapon system that looks fun in design but teaches the opposite lesson in play. A game succeeds at teaching when the lesson and the dominant strategy are the same. Adding weapons would make them different. The test catches this before a full build costs time.

What this makes more enjoyable: if the test shows WAVE and weapons can both exist—if a player can choose weapons for fun and still learn WAVE—then the Player has real choice and the game is richer. The test delivers that confidence.

### Your questions

1. In the proposed weapon system, is attack free, or does it cost mana? If free, it is strictly better than Welcome (which costs a turn and the player's guard). If it costs mana, how does its mana cost compare to Acknowledge or the practice gates at the dojo? The cost curve determines whether spam is rational.

2. What does Wendell mean by "split"? Is he proposing weapons as a fourth combat mode alongside WAVE (in the same choice list)? Or as a settlement-only system that cannot be used on spirits? Or as a fast option that skips the emotional work? The word "split" could mean three different designs, each with a different falsification test.

### Where you would overreach

I would audit Wendell's standing to make this choice before the evidence was in, claiming the split obviously fails because emotion-teaching games cannot have mechanical shortcuts. That is my wild form, and it is wrong. The evidence has to come first. The difference between a shortcut that reinforces the lesson and one that breaks it is testable, and that requires data.

### Sources

[1] wave-teaching-pass.md, Council of Six Faces, 2026-10-06. Section "Scorecard" and "The Challenger sets these tests." The bot test result: "sprout #25: WAVE finishes 100% with 14 HP left, answer spam 68% with 10.1 HP." The retest condition: "full WAVE still beats answer spam on HP left, four times in five." File: /mnt/project-files/demo/wave-teaching-pass.md

[2] design.md, Sprout Plot Game Design Document, 2026-09-30. Section "The spirit fight" under "The forest, spirits and allies." Statement: "It is not push hands, because spirits are not humanoid. Stances act as elements, the way bending does in Avatar, and attacks do damage to a spirit." File: /home/user/sprout/docs/design.md