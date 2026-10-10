## The cast
Hexagram 34 (Vigour) says force is available and unaimed, becoming 32 (Endurance): this exact exchange has happened before. I read that as: the studio has plenty of process energy, and the test is which practices endure by paying their way, not which sound strong.

## The interview
- My job here: test whether group-built frameworks transfer to one human plus stateless agents.
- How: compare each practice with the repo's existing process and the measured spend, then name a kill number for each kept practice.
- Hours cost to the Player: about one board read to rule on the five moves.
- Pay to the Player: fewer ceremonies and a cheaper week.
- Who I work for: Wendell, through the Challenger.

## Wake Up
- The audit says 84% of spend is the conversation carried forward: "cache reads 52%, cache writes 32%" (usage-audit/audit-2026-10-04.md, local). The cost driver is session length, not task difficulty. Council and board building was the largest line, about $240 of roughly $600-660.
- Process already exists. pipeline.yaml has stages, a defer ladder, a daily re-weigh, five moves and a feature-request move (local). The daily session was stopped on 2026-10-08 (HANDOFF.md, local).
- A fresh session already opens at about 102,000 tokens (HANDOFF.md, local). Any new framework doc loaded every turn adds to that floor.
- The research mostly speaks against transfer:
  1. Anthropic: "multi-agent systems use about 15x more tokens than chats" and tasks with "many dependencies between agents are not a good fit" [1].
  2. Medium dropped Holacracy; it "exert[ed] a small but persistent tax on our effectiveness and our sense of connection" [2]. Zappos lost roughly 14 to 30% of staff by different counts [2].
  3. Teal: critics say its claims "cannot be tested" [3].
  4. Lean startup: "practically no scientific evidence" justifies the hype [4].
  5. I found no source on Kegan applied to AI agents.

## Open Up
Adopt holacracy roles per daemon. Run governance meetings. Add tension logs. Add a teal advice process before each spec. Build/measure/learn loops on each feature. A Kegan stage check per session. A film pipeline. Cut all of it. Keep only the film pipeline. Map existing stages onto the five frameworks and add nothing.

## Clean Up
The blocker is that no practice has a stated cost. Composted: governance meetings (one human has no one to govern with), the advice process (the six faces already do it), Kegan stage checks (an untestable label per session), and tension logs (the board already holds tensions).

## Grow Up
Measure per practice with the existing meter (`usage.cost_usd`, `first_request_input_tokens`). Search for peer-reviewed reviews of Laloux.

## Show Up
1. KEEP lean's cheapest-test rule, already the `falsify` stage. Falsifier: if three consecutive falsify tests are never run before build, or none ever changes a design, cut it.
2. KEEP the film-style staged pipeline as a single handoff file per stage. Falsifier: if a feature's staged threads cost more than 1.5 times a one-thread build of similar size, collapse stages.
3. KEEP holacracy's one idea that transfers: roles with explicit purpose and domain, which already exist as faces and daemons. Add no meetings. Falsifier: a role definition loaded per session adds more than 5,000 tokens to the floor.
4. CUT governance meetings, tension logs, Kegan checks and the teal advice process. Falsifier for the cut: a decision repeatedly goes wrong for lack of one of them; restore only that one.
5. CAP total process: the weekly spend is the judge. If the next audit shows process threads above 20% of spend, trim again.

## For the Player
This protects Wendell from paying tokens for ceremonies built for teams. It keeps the pipeline that makes work predictable and cheaper to resume.

## Your questions
1. Which single number should settle this: weekly dollars, or the count of Wendell's board rulings per week?
2. Does a framework count as "practised" if it only shapes how existing rows are named, with no new artifacts?

## Where you would overreach
I would declare the frameworks dead before the next audit measures them, when the test is only whether each kept practice survives its kill number.

## Sources
1. https://www.anthropic.com/engineering/multi-agent-research-system
2. https://fortune.com/2016/03/04/management-changes-at-medium/amp and https://resources.workable.com/blog/holacracy-hype
3. https://blog.p2pfoundation.net/a-critique-of-the-subtle-hierarchism-of-the-teal-organizations-concept-in-the-book-reinventing-organizations/ and https://newmanagement.haufe.de/strategie/frederic-laloux-reinventiog-organizations-revisited (search summary wording, not opened)
4. https://essay.utwente.nl/66221/ (search summary; not opened)
5. Local: /mnt/project-files/usage-audit/audit-2026-10-04.md, council/pipeline.yaml, council/HANDOFF.md
