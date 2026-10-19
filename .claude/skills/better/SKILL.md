---
name: better
description: Deepen a natural-language ask once before building. Use at the start of a build, design or research thread started from Wendell's plain message, or when anyone types /better. Never for board reads, merges, compost or other clerical threads.
---

<!-- Core prompt from Josh's /better skill (gist joshp123/a1443d30fa1b7c577e74882895cea61b), verbatim. The council's
rules for applying it follow; why they look like this is in council/research/2026-10-19-better-pass.md. -->

> I want a deeper version of this task, not a bigger one. Before rewriting it: (1) say what a top professional in this
> field would do here that I'm not asking for; (2) name the rawest material they would start from instead of what has
> already been digested for me; (3) name the specific methods and tools they would use; (4) say what, other than you
> or me, would show the result is right. Then rewrite my prompt to ask for exactly that.

## How the council applies it

1. **Once, never in a loop.** A second pass rewrites the first pass's additions, not his ask, and each pass grew the
   brief about twofold in the 2026-10-19 test. If one pass leaves the ask unclear, that is a question for the board,
   not a second pass.
2. **In the thread, never in the coordinator.** The coordinator's brief carries his words by id and adds nothing
   (the brief rule). The thread runs the pass as its first step, on the brief it was given.
3. **His words stay on top, unaltered.** Write the four answers and the deepened brief under his message in the
   thread's callsheet or working notes. Never replace or paraphrase his quoted words.
4. **Keep the deeper parts, drop the bigger ones.**
   - Answer (2), the rawest material, and answer (4), the outside check, are kept whole. They match standing rules:
     reference photos before a new animal, and every build leaves a check the next round can rerun
     (docs/tool-scout.md).
   - Answer (3) goes through the tool ladder: `python3 council/tools/scout.py <job>`, and the `scout:` line records it.
   - Answer (1), what a professional would add, is kept only where it passes rung 1 of the ladder: it answers his ask
     or the round's check. Extra studies, samples, variants and experiments he did not name are dropped, and the
     report names what was dropped in one line.
5. **A pause goes to the board.** Where the gist says to show the new brief and wait, put the question through the
   reach test (`reach_test` in `council/faces.yaml`) and onto the Council Board. What the record can answer becomes a
   position that stands, and work carries on with it.
6. **Report the check.** Before the report, run the outside check from answer (4) and say what it showed, or say it
   was not run.
