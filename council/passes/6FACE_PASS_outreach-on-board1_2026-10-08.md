# Podcast outreach on the Council Board: a six-faces pass

**Run 2026-10-08**, from Wendell's note on board step `podcast-outreach-chase-01` (saved 2026-10-07 23:55 UTC). The
project's coordinator started the pass. This is the first pass on the subject.

**The ask, in his words:** "we need to also be able to have changs here be able to update the podcast outreach document
OR have that document live inside of the council board" and "Let's also make a note to bring in each of these steps in
the Podcast outreach artifact to the council board. Let's have the council weigh in for how to injest these steps."

**The board was pulled first** (`board/pull.py`): every saved answer was already recorded. Board read 2354 already
copied that note's contact news (Pragya, Nora, Mattias, Annastasia, Vince) into the outreach store by hand, so this
pass does not redo it.

**Inputs:** the Podcast Outreach page and its store (https://claude.ai/artifact/LSrgR62X3GWJ9ryvbCrV9L: 76 contacts,
a `shows` collection, eight statuses, the five-day chase rule in the page's code); the board's step list
`podcast-outreach-chase`, made from the morning brief of 2026-10-07; the Morning brief routine
(`trig_01KkW95XDC3xrnYxmBLbjmX2`), which reads the outreach store read-only on weekdays and writes the day's chases
into the board's `state/current`; `docs/pickup.md`; and the Architect's lesson from board read 8.

## Scorecard

No earlier pass on this subject set tests. Retro 1's standing test applies: this pass names its sources above.

## The anchor

The board is where Wendell sees what only he can do. A chase is one of those tasks, so it belongs on the board,
and what he writes about it has to land on the contact it is about without a session copying it across.

## The casts

Drawn with `council/iching/cast.py`, three coins each; the ledger carries them under `casts`.

| Face | Hexagram | Becomes |
|---|---|---|
| Shaman | 53 Emergence: *This has stages, and you are trying to skip one.* | 37 Household: *An arrangement has formed here without being discussed.* |
| Architect | 59 Dispersal: *What you were holding rigid is coming apart.* | 47 Drained: *The explaining continues and the basin is dry.* |
| Challenger | 2 Bearing: *The whole weight of this is yours, unasked.* | 15 Understatement: *What you are underplaying had better be there.* |
| Regent | 43 Unsaid: *One sentence is still unsaid, and it is going anyway.* | 49 Molting: *A skin is coming off you, and the new one is soft.* |
| Diplomat | 28 Overload: *This is carrying more than what holds it up.* | no changing lines |
| Sage | 47 Drained: *The explaining continues and the basin is dry.* | 48 The Well: *What you want is there and your reach is broken.* |

No daemons were sent. Each face's problem was answerable from the record above.

## Shaman

**Household, out of Emergence, names what happened.** An arrangement formed without anyone deciding it: the outreach
page holds the contacts, the morning brief reads them, and a session turned the brief into seven board steps. Wendell
then answered on the step, which is the natural place to answer, and his answer stopped there. The note had to be
carried to the contacts by a person reading it at board read 2354.

**The stage being skipped is the one where his words land.** What he writes about Pragya is about Pragya. When it
lands on a copy, someone has to notice and carry it, and each carry is a session he pays for. The Shaman wants a chase
where writing "Nora booked an episode" updates Nora, with no hand in between.

**A chase is a message to someone who knows him.** The step list said so ("Each of these is a message from you to
someone who knows you"). The chase view should keep that: the person's name first, why they matter, the last event
that happened, and one box for what he did.

## Architect

**One store is the design; a sync is an explanation that keeps running.** The board page can reach only its own store,
and the outreach page only its own. Any design that keeps two stores needs a session to carry changes between them,
and Drained is the right word for that: the carrying never ends and nobody gets more from it.

**So the contacts move into the board's store, and the board gets an Outreach tab.** His lesson from board read 8
settles where: "I think a tab on this board is quite useful". One place to look beats separating surfaces by the
rhythm of use. The tab carries the outreach page's own view (show filters, the status picker, add a contact, add a
show), lifted from its code, writing `contacts` and `shows` in the board's store.

**Ingesting the steps means computing them, never copying them.** Your steps gets a standing list, "Podcast chases",
built live from `contacts` by the same three rules the morning brief uses: the flag says FOLLOW UP NOW, the next touch
is today or past, or the status is Pitched and the last touch is five or more days old. A Booked contact whose next
touch is within three days shows as a recording coming up. Each chase has one form: what happened (sent, booked, not
now), a next-touch date, and a note. Saving writes the contact itself: `lastTouch` becomes today, the status moves,
and the note is added to the contact's notes with the date. A chase leaves the list when its rule stops firing, so
there is nothing to tick off by hand and nothing to fall out of date.

**The migration copies, it does not move.** The 76 contacts and the shows are copied into the board's store with their
ids. The outreach page's own store stays as it is, as the record of the old page, and the page is republished as a
short pointer to the board's Outreach tab. Nothing is deleted.

**The morning brief reads the board's store instead.** Its outreach section changes one URL and collection path. It
keeps writing `state/current` as it does now.

## Challenger

**Bearing says the board will carry whatever is set on it, so check the weight.** The board's job until now was
unresolved council work. A contact list is not council work, and the template is already 74,587 bytes. The Event
Pipeline page (the same shape, read by the same brief) will ask for the same treatment next. The Challenger would
rather keep the board narrow and give the outreach page a write-back path.

**The write-back path does not exist, and that is the case against it.** No page can write another artifact's store,
so "changes here update the outreach document" with two pages means a session reads each note and edits the contact.
That is what board read 2354 did by hand, and it took judgment: "I'm going to ping mattias again" is not a status.
The Challenger concedes the tab, and holds the dissent on scope: the Event Pipeline does not follow without its own
pass.

**What would show the tab wrong.** First, the outreach view slows the board: if the board takes visibly longer to open
on his phone with 76 more documents, move the view to a second page inside the same artifact (one artifact, one store,
two pages) and test that its store calls work there. Second, a chase saved on the board fails to show on the contact
in the Outreach tab without a refresh. Either one is a blocker; each test names the decision it unlocks, as his
lesson of 2026-10-03 asks.

## Regent

**The unsaid sentence is the Send button's.** Today a step note lights the Send bar and wakes a board read. A chase is
not council work: nothing in it needs a face. If chases light the Send bar, every follow-up he logs costs a session,
which is the cost the short-sessions rule exists to stop (CLAUDE.md, "Short sessions"). Saving a chase writes the
contact and does not light the Send bar. A note that asks the council for something still goes on a step or the
context box, as now.

**Molting: the old page's skin comes off, its record stays.** The rule "keep the lower level" (`transcend_and_include`
in `council/pipeline.yaml`) holds: the old store is kept, the pointer says where the list went, and the ledger records
the move.

**The routine change is in scope.** The Morning brief is his routine; repointing its outreach section is a reversible
edit to a read path, done in the build thread. Nothing it writes changes.

## Diplomat

**Overload is about the phone.** His chase note came from the steps tab, where `device` is phone. The chase form has
to work one-handed: three buttons (Sent, Booked, Not now), a date that defaults to five days out, and one note line.
The full contact editor stays on the Outreach tab.

**Use his words for every label.** The tab is "Outreach", the list is "Podcast chases", and the statuses are the eight his
page already uses. No new terms.

## Sage

**What each face gave.** The Shaman named the cost: his words stop on a copy. The Architect gave the design: one store,
an Outreach tab, chases computed live. The Challenger forced the weight check and two tests, and kept the Event
Pipeline out. The Regent kept chases off the Send bar. The Diplomat set the phone form. Nothing was dropped.

**The Well's reading fits.** What he wants already exists (the contacts, the rules, the brief); the reach between them
is what was broken. The pass repairs the reach and adds nothing else.

**The Challenger dissents on scope.** It would keep the board to council work if a write-back path existed,
and accepts the tab only because none does. It asks that the Event Pipeline not follow without its own pass. The pass
is not unanimous on the reasoning, and is on the result.

## Verdicts

| Face | Outreach on the board | Chases computed from contacts | Chases off the Send bar |
|---|---|---|---|
| Shaman | yes | yes | yes |
| Architect | yes, as a tab | yes | yes |
| Challenger | yes, with tests; dissents on scope | yes | yes |
| Regent | yes, old store kept | yes | yes, the reason for it |
| Diplomat | yes | yes, phone form | yes |
| Sage | synthesised, does not rule | | |

## Outputs

### Positions

- **`outreach-on-board`**: Podcast Outreach moves onto the Council Board as an Outreach tab, with its contacts and
  shows in the board's store. Why it did not need him: he named this option himself in the note, and his board read 8
  ruling ("I think a tab on this board is quite useful") picks a tab over a second surface.
- **`outreach-chases-live`**: Your steps gets a standing "Podcast chases" list computed live from the contacts by the
  morning brief's three rules; saving a chase writes the contact. Today's hand-made list `podcast-outreach-chase` is
  withdrawn once it ships. Why it did not need him: his note asks for exactly this ("have changs here be able to update
  the podcast outreach document"), and the rules are already his, in the outreach page's code and the brief's prompt.
- **`outreach-old-page`**: the old outreach page becomes a pointer to the tab, its store kept untouched, and the
  morning brief reads contacts from the board's store. Why it did not need him: `transcend_and_include` in
  `council/pipeline.yaml`; the page is private, so nobody else loses a link.
- **`outreach-no-send`**: saving a chase does not light the Send bar. Why it did not need him: the short-sessions rule in
  CLAUDE.md and `docs/pickup.md`; a chase needs no face.

### Questions

The pass sends no question. The reach test found no fork that turns on his preference: he offered both options, and his earlier tab ruling
chooses between them.

### Tests, dated

- By 2026-10-15: a chase he saves on the board shows on the contact in the Outreach tab at once, with no session run.
  Resolves: whether one store removed the carrying. Unlocks: withdrawing the hand-made chase list for good.
- By 2026-10-15: the first weekday morning brief after the build lists its chases from the board's store. Resolves:
  whether the brief survived the move. Unlocks: retiring the old page to a pointer.
- On the build's first phone check: the board opens no slower with the contacts in its store. Resolves: tab or second
  page. Unlocks: the Challenger's fallback, if needed.
