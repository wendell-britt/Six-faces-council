---
name: brief-master
description: Turn Wendell's plain ask, or any thread brief or face/daemon dispatch, into one tight prompt before it is sent. Use when writing a brief, a worker prompt, or a Claude Design/Code prompt.
---

# Brief master

Adapted from nidhinjs/prompt-master (MIT), cut to the council's rules. Run it silently, then output ONE copyable prompt and a one-line note on the strategy. Never show framework names.

## Steps
1. **Target.** Who runs this: a Sonnet clerical thread, an Opus solver thread, a daemon, Claude Design, Claude Code, an image or 3D tool? Match its format and model effort (clerical = Sonnet; solver, passes, new design = Opus).
2. **Pull the nine parts from the ask and the record, not from Wendell:** task, input (files, links, where they live), output (what, where, in what format), constraints, context (callsheet, board rows, rulings quoted), audience, memory (decisions already made, so the worker does not redo them), success criteria ("done when"), examples.
3. **Gaps.** Fill from the record first (callsheets, board, memory). A gap only Wendell can fill goes through the reach test and onto the board, never into chat and never as a question in the reply. Proceed on the most likely reading and say which.
4. **Council clauses, always included, one line each:** questions go to the board; reply says what changed and ends without a question; testable preview = one-click hosted link at the exact state, never a clone line; look steps open from the board or a hosted page, never GitHub; report ends with a recommended next move and what was not checked; hand off before 150k context and resolve; bulk reading goes to a worker; scout: line for anything new; the tool ladder first.
5. **Faces and daemons.** A dispatch carries: the face, the ONE problem, who the Player is, the daemon's overreach line, a word cap, and the output shape (at most five moves, at most two questions). Faces keep their lens from faces.yaml; never restate it from memory.
6. **Fix the credit-killers:** vague verbs ("improve", "clean up") become a measurable change; no success criteria; no stop condition for agents; open filesystem scope (name the files); missing stack or model constraints; asking for several things at once (split into threads); reasoning demanded where a number or still would prove it cheaper (probe before still before video).
7. **Token audit.** Cut every word that does not change the output. Brief under 300 words unless the callsheet carries the rest; point to the callsheet instead of pasting it.

## Output
One block: Goal, Inputs (with locations), Output and done-when, Constraints, Council clauses, Stop condition. Then one line: "Reading I chose: ...". Run voice_lint on anything he reads.

## Never
Do not rewrite his quoted words. Do not invent a lens for a face. Do not add steps for him; his steps follow the step shape in pipeline.yaml.
