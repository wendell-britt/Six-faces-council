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

## Next round brief (Wendell, 2026-10-20 19:02 UTC, on the live hand)

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
