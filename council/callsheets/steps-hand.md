# Your hand (Your steps as five cards)

Wendell, 2026-10-20: "Tasks that i need to do (this in the your steps pane) should be rendered as cards with an
animation that shuffles them. I can only have 5 at a time in my "hand" this includes what comes from tap the vein. I
can pay a cost (yet to be determined) to discard a card, but it comes back based on the spaced repetition rules.
(Actualy I can discard a card if I do some inner work on it, a 321 a WAVE process- that would mint a vibeulon and I can
pay a vibeulon to discard the card)"

## Built (steps-hand 1, 2026-10-20)

- `board/template.html`, `hd-` code: the hand draws five cards over the steps store (hd-draw), deals them after a
  riffle of the deck, keeps the rest in a folded deck (hd-deck). Inner work opens the blocker panel's WAVE run; a
  finished run carries `vibeulon` on its blockers/ record (hd-mint). Discard spends the oldest unspent one, two taps,
  and writes `discards[]` and `discardedUntil` on the step (hd-spend, hd-ladder: 3, 7, 14, 30, 60, 90 days).
- A Tap the Vein line becomes `steps/ttv-<taskId>` in list `ttv` the first time he acts on it.
- `board/pull.py` records discards in the ledger as priority data (no needs-work line).
- Rerunnable check: `/mnt/project-files/board-hand-2026-10-20/check.mjs <built page> <out dir>` (Playwright, in-memory
  store; writes result.json and hand.png).

## Open

- hd-wallet: board vibeulons live on the board's records. Next build: mint them into his bars-engine wallet
  (bars-engine `src/actions/economy.ts`) from the blockers records on main, only when he wants that.
- Not checked: the shuffle on a real phone, and the hand against the live store's 160+ steps.

## Built (steps-hand 2, the card table, 2026-10-20)

scout: rung 3, no known tool. The toolbox has nothing for UI, and card libraries (deck-of-cards and the like) draw
playing-card faces, not cards that carry text and controls; the fan is plain CSS transforms on the existing hd- code.

- A felt table: the deck face down, the discard pile and Claude's pile face up, podcast chases as their own pile, and
  the vibeulons as a coin stack. The hand is a fan of overlapping cards, an arc on a computer and a vertical fan on a
  phone. Tapping a card picks it up: full size, the whole step, Inner work, Discard, Back in my hand, and "Give it back
  to Claude".
- The hand is held: `inHand: <iso>` on the step, written when he taps the deck. He draws only into a free slot; the deck
  deals its top card in the hd-draw order. Done, discarded (pays a vibeulon) or handed back frees the slot; discard and
  hand-back clear `inHand`. The hand starts empty on the first visit after this ships.
- Give it back to Claude writes `aiBack: {text, automate, at}` and clears `inHand`, no vibeulon. `board/pull.py` lists
  it as needs-work, `steps/<id>: back to AI (automate): "..."` (test in tests/test_pull.py). The card stays in Claude's
  pile until Claude finishes the step or removes `aiBack`, which returns it to the deck.
- Check: `node /mnt/project-files/board-hand-2026-10-20/check.mjs <built page> <out dir> [width]` plays the loop (draw
  five, full hand refuses a sixth, pick up, hand back, mint, discard) and writes result.json and screenshots; it passed
  at 390 and 1200 wide. Shots: /mnt/project-files/board-hand-2026-10-20/round2/.
- Not checked: a real phone's touch on overlapping cards, and the live store's 160+ steps in the deck.

## Round 2 brief, done (Wendell, 2026-10-20 19:02 UTC, on the live hand)

His words: "Hand doesn't really feel like a card hand. The think I'm imagingin is card that can overlap each other in a
fan (fan can be vertical) but I want the experience to feel like I'm playing cards this is still too.... dashboardy. The
goal is to have a skeuomorphic view of a deck of cards which is wha tI need to interact with and have the game loop be
that I can take a card once I discarda a card and I have to do inner work to discard a card. I Should also be able to
add context to a card to push it back to AI if I identify an approach that can be automated"

Build (Opus, design-ontology loaded, one thread):
1. Skeuomorphic table: a face-down deck pile, a fanned hand of overlapping cards (vertical fan on a phone, arc on a
   computer), the discard pile. Tapping a card lifts it out of the fan and turns it face up, full size, with the step's
   details. Keep `hd-` code in board/template.html and replace the grid of `hd-card`s.
2. Game loop: the hand stops refilling by itself. He takes a card from the deck only when a slot is free; a slot frees
   when a card is done or discarded; a discard costs a vibeulon minted by inner work (unchanged). This needs the hand's
   membership stored, so a card stays in the hand until it is done or discarded: `inHand: <iso>` on the step (steps
   collection, no schema change), written when he draws. Flip hd-draw's "moving a date can change the hand" to match.
   Which card the deck gives (top by hd-draw order, or his pick from a face-down spread) goes through the reach test.
3. "Give it back to AI": a context box on each card, plus a "Claude can automate this" mark, saving `aiBack: {text, at}` on
   the step. board/pull.py lists it as needs-work (`steps/<id>: back to AI: "..."`), with a test in tests/test_pull.py.
   Does the card leave the hand when handed back? Put that through the reach test (position: yes, without a vibeulon,
   since Claude takes it).
- Keep: never drop step data (council/postmortems/2026-10-20-steps-outreach-blank.md); page_calls guard; term lint
  ("WAVE order" is banned); the rerunnable check /mnt/project-files/board-hand-2026-10-20/check.mjs (extend it).
- Deliver: a hosted way to see it before merge if cheap, otherwise merged to main and the link
  https://bars-engine.vercel.app/board/council#steps. New positions on the board as rows.
