# Spec: Daemon subagents for the six faces

## The ask

> "Ok I want to add a new feature. Subagents for the 6 game masters based on the daemons
> Protector controller skeptic fixer victim damaged self and player"
>
> Wendell, in chat, 2026-10-02 (evening).

**Who it is for:** Wendell, through every six-faces pass in every council repo.
**What changes:** a face argues from its altitude, and each altitude has its own way of being defended.
The faces have no way to see that in themselves. This evening Wendell overruled a position (the steps page)
and reversed another (migrations kept manual), and in both the face had argued a careful-sounding case. The
daemons are his own map of exactly that.

## Purpose

Seven daemon subagents and the Player read a finished pass before the Sage synthesises. Each daemon looks
for itself at work in each face's argument, using its cell for that face. The Player names what each face
would arrive at with no daemon on the joystick. The Sage carries their reads into the synthesis, and the
board marks any position a daemon read touches.

## Design decisions

| Decision | Choice | Whose |
|---|---|---|
| The daemons and their definitions | Wendell's: `decks/shared/parts.yaml` in friendcraft, seven daemons and the Player | Wendell (canon, MTGOA) |
| The cell per face | `decks/shared/parts_by_face.yaml` in friendcraft: 48 cells. Six follow the book's chapters; the other 42 were written by sessions and are marked as theirs | Wendell (6), sessions (42) |
| One subagent per daemon, not per cell | Eight files in `.claude/agents/`, each reading its six cells. Forty-eight files would duplicate the grid | Council |
| The Emotional Body is included | Wendell's list named six daemons and the Player. Canon seats seven daemons, and the Emotional Body's chapter is the Architect's (ch6 §5). It stands as a position he can flip | Council |
| Where the definitions are read | In friendcraft, which is private. A session attaches friendcraft read-only and passes the path. No copy is made, because a copy in the public home would publish book material (the permission check refused one) | Council; the permission check |
| When it runs | In every pass, after the six faces and before the Sage. Eight subagents per pass | Council |
| What a read is | A hypothesis with a quoted sentence and what would show it wrong, never a fault in a person (`parts.yaml`: a read "may not conclude") | Wendell (canon) |

## Reserved items

Canonical prose: the subagents read the book's material and never write it. Nothing else reserved.

## How we will know it failed

- **The cheap test, run before building further:** the eight subagents read two past passes blind. They do
  not see the board. In flirtcraft pass one, Wendell later reversed the position "migrations stay a manual,
  guarded step". In council pass five, he overruled "the steps live on their own page".
- **Pass mark, set before the run:** at least one daemon flags each of those two positions, with a quoted
  sentence. Positions that stood are flagged less often than the two that did not.
- **The result that stops the work:** neither reversed position is flagged, or the stood positions are
  flagged as often as the reversed ones, which would make the reads noise.

## Definition of done

- [ ] The test above passes, and its result is recorded here. **It failed on 2026-10-02; see below.**
- [ ] Eight agent definitions in `.claude/agents/`, synced to every council repo by the hook.
- [ ] The skill's pass shape includes the daemon check, and says what to do when friendcraft is absent.
- [ ] Nothing on Wendell's steps list, because nothing here needs him except the board.

## Result of the cheap test, 2026-10-02

**It failed against the pass mark set before the run.** The eight subagents read both passes blind, using
the agent files on this branch and the definitions in a local friendcraft clone.

| Position Wendell later reversed | Flagged by a daemon? |
|---|---|
| Flirtcraft pass one: "Migrations stay a manual, guarded step" | **No.** No daemon mentioned it. |
| Council pass five: "The steps live on their own page" | **No.** No daemon mentioned it. |

**What the daemons did flag, recorded here and not counted as a pass, because none of it was predicted:**

- Five of the seven daemons flagged the Shaman's caution in flirtcraft pass one, "The fix must not turn into
  a rushed launch to close that gap." Wendell then chose "merge now". This is the strongest agreement in
  the run, and it is a candidate for the next pre-registered test, not evidence that this design works.
- Four reads (the Fixer, the Victim, the Emotional Body and the Player) flagged the one question in pass
  five. In one answer it asked Wendell to approve a deploy change and to lift the permission check that
  had refused it. That framing bundled two decisions. It is recorded as a finding about how
  questions get written, whatever happens to this feature.
- Three reads flagged the Sage's unanimity flag in flirtcraft pass one. `faces.yaml` makes that flag a
  standing rule, so those reads are shown wrong by the falsifier each daemon named. The falsifiers worked.
- Positions that stood were flagged too: "Existing specs are not retrofitted" (the Skeptic) and "A feature
  ships as a position he can flip" (the Fixer). Wendell let both stand on the board.

**The council reads the result this way.** The daemons read sentences for defended argument, and they found some. The two
positions Wendell reversed were not defended arguments; each rested on a preference only he held (a tab
or a page, a manual step or an automatic one). The reach test covers that kind of gap, and the daemons
cannot see it. So the design answers a question the record did not show needed answering.

**Status:** stopped at the falsify stage. Nothing is wired into the pass shape. The eight agent files stay
on the branch `feature/daemon-subagents`, unmerged.
