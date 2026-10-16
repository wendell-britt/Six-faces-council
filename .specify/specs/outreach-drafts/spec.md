# Spec: Outreach drafts with send, on the Outreach tab

<!-- The six-faces pipeline's spec template (council/spec-kit/spec.md). Stages: intake and spec are written here; the falsify section holds the cheap test; plan and build wait for Wendell's word. -->

## The ask

> "So yes this is part of getting unblocked for outreach for speaking engagements and having people on the podcasts. I think having drafts that I can review in the council board and the ability to trigger a send from there will be quite useful."
> Wendell, 2026-10-15 (Zo session).

**Who it is for:** Wendell, ruling on the Council Board's Outreach tab.
**What should change:** An outreach email can be drafted, reviewed, and sent without leaving the board's existing structure: the draft lives on the contact it is for, he reviews it on the Outreach tab, and his send decision is executed by a session through the connected Gmail account.

## Correction this spec carries

The first draft of this spec (written in the same session, before the board read) proposed a new `drafts` list beside positions/questions/causes. That duplicated the Outreach tab, which the `outreach-on-board` pass already resolved against: two pages cannot write each other. This version anchors on the existing tab and its store collections (`contacts`, `shows`).

## What exists already

- The Outreach tab (built 2026-10-08, `council/ledger/2026-10-08-outreach-tab-build.json`): 76 contacts and shows live in the board's store, copied from the old Podcast Outreach page with their ids. Chases are computed from contacts; chase saves and contact edits deliberately do **not** light the Send bar (`outreach-no-send`).
- Gmail is connected in Zo: send, draft, reply, thread read all verified working 2026-10-15. Send uses explicit addresses (the `me` alias throws).
- Sessions read the board via the store-save flow (`board/read.py`, `board/pull.py`). **The contacts and shows collections are not in that flow** — pull.py reads positions, questions, terms, causes, steer, steps, blockers, picks, morning, ttv only. Main's `board_data.json` holds no contact rows.

## Design

| Decision | Choice | Whose |
|---|---|---|
| Where a draft lives | On the contact row it belongs to, as a `draft` block: `subject`, `body`, `status` (`draft`/`ready`/`sent`), `updated`, and after sending the Gmail message id and thread id. No new list | follows `outreach-on-board`: the tab is the one surface |
| Who authors a draft | A session, on Wendell's naming a person or show. No automated sourcing in this spec (the candidate moves at positions 479 and 558 already put people on the tab) | Wendell's ask, minimal schema |
| How Wendell rules | On the tab: edit the draft text, then `send`, `revise`, or `drop`. His write lands in the store like any answer | follows the answer/steer write shape |
| Who executes the send | The next session running a board read picks up contacts whose draft status is a send decision, sends the body verbatim through Gmail, records the message/thread ids, sets status `sent` | follows `sent-back`: decision state + session pickup |
| Replies | A later read checks sent rows' threads with Gmail; a reply flags the contact onto the needs-work list | follows pull.py's needs-work pattern |
| Editing before send | If a steer note or text edit arrives after the send decision, the send does not fire; the row returns to `draft` and the next read lists it for revision | the send must be verbatim-what-he-saw |

## Tension needing a ruling

`outreach-no-send` (2026-10-08): saving a chase or editing a contact does not light the Send to Claude bar — chases need no face, and every Send starts a paid session. A send decision on a draft is different by design: it **must** light Send, because only a session can execute the Gmail call. This is a deliberate exception to the standing ruling, or a change to it. Wendell rules which.

## Open plumbing question (not invented past this)

How a session's draft text reaches the store. Contacts never sync to main, so the session cannot write a draft the way it writes a ledger row. Options, not decided here: (a) the session writes the draft to a project file and Wendell pastes it into the contact on the tab; (b) sessions gain a store-write path for contact drafts. Decided at plan stage with the board's existing write paths in view.

## Falsify

The cheap test: one real draft row for a low-stakes recipient (Wendell's own address), walked through the full cycle — draft → `send` decision → pickup → Gmail send → message id recorded → reply check. If the round trip cannot complete in one board read plus one session, the design is wrong.

## Ruling update (2026-10-16)

The visibility choice named above is answered by a chat ruling (see
`council/ledger/2026-10-16-store-visibility-ruling.json`): neither claude.ai-login-in-Zo nor Claude-only execution —
the store itself reaches main so every environment reads it from git. That work is its own feature, spec at
`.specify/specs/full-store-mirror/spec.md`; this spec's build waits on it.
