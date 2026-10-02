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

## Version two, after Wendell's board answer of 23:45

**His answer:** "help each face while it drafts", with this steer:

> "The daemons exist to solve problems in the faces domain. They are designed to protect the player but
> also all work for the players enjoyment. They should be able to ask questions and help with specific
> problems"

**What changes.** Version one read a daemon as a defense to be caught. Wendell reads it as a helper in a
face's domain, working for the Player. So a face dispatches a daemon while it drafts, on one specific
problem. The daemon works that problem from its aim at the face's altitude, says what it protects the
Player from and what it makes more enjoyable, asks at most two questions, and names where it would
overreach. The Player says what it wants from the problem. Its questions go through the reach test like
any other.

| Decision | Choice | Whose |
|---|---|---|
| When a daemon runs | While a face drafts, on a problem the face names; not after the pass | Wendell (board, 23:45) |
| What a daemon is for | Solving problems in the face's domain, protecting the Player, and the Player's enjoyment | Wendell (board steer) |
| Who the Player is | Named by the caller for each problem: Wendell for council work, or the person a product serves | Council |
| How many per face | As many as the face's problem needs, usually one to three; never all eight by default | Council |
| Overreach | Each daemon names where its cell's distortion would show up in this problem, so the face can stop it there | Council, from the cells' own `does` |

## How we will know version two failed

- **The cheap test, run before building further:** the Challenger's open proposal from flirtcraft pass one,
  "A failed production deploy should notify someone", is a real and unbuilt problem. The Challenger
  dispatches four daemons on it (the Protector, the Controller, the Skeptic and the Fixer) and the Player.
  The Player is Wendell. A separate judge then receives the four daemon outputs with the names removed and
  the order shuffled, plus the four Challenger cells, and matches each output to its cell.
- **Pass mark, set before the run:** the judge matches all four outputs to the right cells, and at least
  three of the four propose a concrete move that none of the others proposes.
- **The result that stops the work:** the judge cannot tell the outputs apart, or the moves repeat each
  other. Either would make eight subagents one subagent with eight names.

## Result of the version two test, 2026-10-02

**It passed against the pass mark set before the run.**

- The judge matched all four outputs to the right daemons: A was the Fixer, B the Skeptic, C the
  Controller, and D the Protector.
- All four proposed a move that none of the others proposed. The Fixer proposed turning on the notice
  Vercel or GitHub may already offer before building anything. The Skeptic proposed letting a failing
  preview block the merge. The Controller proposed a sign-in request after each deploy, to catch run-time
  failures. The Protector proposed an alert when production recovers, repeated at an interval Wendell
  picks.

**The result has one caveat.** The judge's reasons quote each output's overreach line most often, and that
line restates the daemon's own distortion. So the match test partly measures that section. The second
test, distinct moves, does not depend on it, and it also passed.

**What the run found for the open problem itself.** Every daemon asked the same question: which channel
Wendell actually reads on his phone, and whether Vercel already sent failure emails that went unread. That
belongs to the deploy-alert proposal from flirtcraft pass one, which nobody has started. It is noted here
and not sent to the board, because nobody asked to build that alert.

## Definition of done, version two

- [x] The cheap test passes, and its result is recorded here.
- [x] Eight agent definitions in `.claude/agents/`, synced to every council repo by the hook and installed by
  `council/install.py`. A scratch copy of root-game picked them up on its second sync.
- [x] The skill's pass shape tells a face how to send its daemons while it drafts, and what to do when
  friendcraft cannot be attached.
- [x] Nothing on Wendell's steps list.
- [ ] Ships as a board position that merges on the next board read unless he flips it.
