# The daemons' questions, and where they are used

Wendell, 2026-10-14: "Updating ontology for the daemons. In the game master agents and in the games itself. Questions
to ask each daemon/concerns for each daemon". The sets are in `questions.yaml`, in his exact words, with a plain
form for players beside each.

## What the sets add

The book gives each daemon an essence and a wild form (`daemons.yaml`). The sets give each one an interview, and
the interviews share four questions:

| Slot | The question | What it shows |
|---|---|---|
| object | What do you work on? | Where the daemon's attention is |
| boss | Who do you work for? | Which part is really in charge |
| method | How does your work serve that boss? | The strategy, and its cost |
| stakes | What happens if you're not there? | The fear that keeps it at its post |

The boss question is the new part. It turns seven separate figures into a chain. A Controller can work for the
Protector, for the self, for control itself, or for the vulnerable child, and his Controller set asks a different
follow-up for each (`by_boss`). The chain ends at the Protector, whose boss is the body's survival, or at the
Player, whom every daemon serves or gets in the way of.

## In the council's own work

1. **Every daemon report now opens with its own set.** The agents in `.claude/agents/` answer their questions
   about the problem before the five moves. This is live with this change.
2. **Two reports that name different bosses are a finding.** When the Skeptic says it works for the Protector
   and the Fixer says it works for the Player, the decision is being pulled two ways. The face names that in
   the pass, since it explains a split better than either report alone.
3. **A stalled thread gets the stakes question.** Stalled work usually has a daemon at its post. The compost
   pass can ask, of each stuck item, which daemon holds it and what it fears would happen without it. The answer
   says whether to compost the item or unblock it.

## In the game

1. **The daemon path chambers.** Each figure on the path (board `dp-seven`) is met with its own set. The
   Protector's chamber in bars-engine now asks his four questions after its first ones. The Controller's
   chamber, the next one built, is where the boss question first changes the conversation: the player picks
   who it works for, and the follow-up changes with the answer.
2. **The shadow spirit (perceptual shadow, bars-engine #326).** Its one line per daemon stays as the door.
   Picking a daemon opens that daemon's set. The boss the spirit names is the next daemon offered, so the player
   follows the chain the way the shadow actually runs. Each set answered thins the shadow as one practice.
3. **NPCs made from a blockage (bars-engine #328).** An NPC wears its daemon's warp in the body and speaks
   from its set. Its boss answer names who it defers to, which is the next NPC the player meets.

## In the story

A daemon's set, read in order, is a character arc. What it guards opens the scene, who it works for is the
reveal, how it works is the conflict, and what it fears would happen without it is the climax, the moment it is
asked to step aside. The Player's set gives the chapter its obstacles: "How does the other daemons get in your
way?" lists the figures the player meets. For the Chapter 1 demo, that question, answered by the player at the
start, picks which daemons appear and in what order.

## Recommended next move

Build the Controller's chamber on the daemon path with its set, including the boss follow-ups. It is the first
place the chain shows up in play, it is already the next chamber in the build order, and the code it needs (the
chamber, cards, the open line) is the Protector's.
