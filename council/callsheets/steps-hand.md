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
