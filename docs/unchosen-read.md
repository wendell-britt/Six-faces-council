# The weekly read of the unchosen lines

Once a week the council reads the lines Wendell named in a Tap the Vein brainstorm and did not choose, in bars-engine
where they live, and writes back at most five patterns, each with one pitch. He answered `uc-who-reads` B on 2026-10-21
(the board pull of 17:16 UTC, `council/ledger/2026-10-21-pull-171630.json`). The pass: `council/passes/6FACE_PASS_unchosen1_2026-10-21.md`.

His steer on `uc-pattern-returns`, the same day: "And we should intelligently pitch a new action item based on the fact
it's coming back. Then compost the old one. this way these unchosen fragments get better and more aligned over time".

## What he sees

The "Not chosen" section of Tap the Vein (`/tap-the-vein?view=unchosen`) shows "The council's read" under the words that
keep coming back: each pattern's word, the face that read it, one sentence on what it reaches for, the pitch, and the
lines it came from with their days. When a word comes back in a later week with a new pitch, the old pitch shows struck
through beneath it as composted. `?view=unchosen&sample=1` shows sample mornings, labelled, for a preview.

## The read, step by step

One Sonnet thread, once a week, after a board read or on its own. Nothing from the pile is committed, written to a
ledger, quoted in a reply or sent to a worker.

1. `python3 council/unchosen_read.py fetch /tmp/unchosen` saves the pile, the returning words and the live pitches
   outside the repository. It stops if the week has been read already.
2. For each returning word worth reading (at most five), one face writes the read in `/tmp/unchosen/reads.json`: the word,
   the face, the kernel (what it reaches for, in his terms), the pitch, and the quotes. The pitch is intelligent the way
   `council/bar_read.py` reads are: look the word up in the record first (a strand's call sheet, a board row, a Lens
   goal, `python3 board/needs_work.py`) and pitch the smallest action that fits what the council already holds. A word
   with a live pitch came back, so its pitch must be new and should be sharper, built on why the old one did not land.
3. `python3 council/unchosen_read.py check /tmp/unchosen/pile.json /tmp/unchosen/reads.json` until it passes.
4. `python3 council/unchosen_read.py write /tmp/unchosen/pile.json /tmp/unchosen/reads.json` runs a dry run, writes,
   and deletes both files. bars-engine composts each returning word's old pitch in the same write.
5. The reply says how many patterns were written and how many composted, links the view, and quotes none of it.

## What the checks hold (both sides)

The script and bars-engine's POST (`src/lib/tap-the-vein/unchosen-read.ts`) check the same rules: every quote is one of
his unchosen lines word for word with its day and holds the word; the quotes span two mornings; at most five patterns
and one read a week; a returning word gets a new pitch; no avoidance words about him (`tb-loss-not-avoidance`); no qi,
vibeulons or spirits in a pitch (`uc-links-by-hand`). A pitch is an offer, never a task (`uc-no-duty`): nothing reaches
his day unless he draws it.

## What it depends on

`COUNCIL_MENU_TOKEN` (the egress proxy injects it for bars-engine.vercel.app). On 2026-10-21 it answered 401; the
rotation waits on his steps in the "Morning menu token steps" thread, and the read cannot run until it answers 200.
The weekly routine is started once it does (council/callsheets/morning-menu.md).
