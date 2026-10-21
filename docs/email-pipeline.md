# Outreach email drafts and sends

An outreach email waits on the Council Board's Outreach tab as a `draft` block on the contact it is for. Wendell
reads and edits it there. His Send press is the permission to send it, and a session that holds the Gmail connector
sends exactly the text he approved. The design is in `.specify/specs/outreach-drafts/spec.md`, and the code is in
`board/email_pipeline.py`.

## Who can draft

Any client can draft: a Claude thread, Zo, Codex, or a routine. Drafting writes the block and never sends.

```
python3 board/email_pipeline.py draft --store <dir> --contact <id> --to someone@example.org \
  --subject "..." --body-file body.txt --author "<which client>" [--kind reply] [--accept RULE:"reason"]
```

The script reads the contact from a saved store folder, runs `voice_lint` on the body, and keeps the findings on the
draft so the card shows them. It writes the block to bars-engine through `board/store_write.py` and prints the
ArtifactData update for the claude.ai board. When bars-engine refuses the token, the printed update is the path. A
draft never writes over one in status `send` or `sending`.

## The voice step

Every draft goes through the email voice pass before it reaches the board (docs/email-voice.md). The pass reads the
profile in `council/voice/email-voice.yaml`, keeps its findings on the draft as `voice` next to `voice_lint`'s `lint`,
and shows both on the card. A draft that still reads as AI is refused until each tell is rewritten or accepted with a
written reason (`--kind reply|outreach`, `--accept RULE:"reason"`). Wendell's edit on the board comes after the pass,
and the text he saves when he presses Send is the text that goes out.

## Who can send

Only a session with the Gmail connector sends, and it sends only what `email_pipeline.py ready <dir>` lists. Send
saves the subject and body he sees, sets status `send`, and stores `approvedHash`, a sha256 of the addresses, subject
and body. The page and the script compute the same hash, and `tests/test_email_pipeline.py` pins one value for
both. `ready` recomputes the hash from the saved text. A draft whose text changed after his press lands in a
separate `refused` list and is never sent. Revise, Drop and Take back never send.

The Send press also lights the Send to Claude bar. That is a deliberate exception to `outreach-no-send` (2026-10-08),
because only a session can make the Gmail call. Chase saves and contact edits still leave the bar dark.

## The duplicate guard

1. The sender fetches the store fresh and runs `ready`, then takes each payload exactly as printed.
2. It runs `mark <contact> sending` and confirms that write landed before any Gmail call.
3. It sends with the explicit addresses in the payload, because the connector's `me` alias fails.
4. It runs `mark <contact> sent --message-id <id> --thread-id <id>` with the ids Gmail returned.

A draft found in `sending` is never resent automatically, since the email may have gone out before the session
stopped. `board/pull.py` lists it as stuck, and a person checks the Sent folder. If the email went out, that person
runs `mark ... sent` with the ids found there. If nothing went out, they run `refuse ... --checked-sent-folder`.

`board/pull.py` prints one needs-work line for each draft that is approved, refused, stuck, or sent back for
revision. The lines follow the drafts' state, so a rerun prints the same lines. They stay out of the ledger, because
contacts never go to the public repos.

## The Gmail connector

The connector can create, update, get and list drafts. It can send a new message, send an existing draft by its id,
reply in a thread, and read threads. Every draft and send goes out as the signed-in Gmail account. This pipeline
therefore works only if the connected account is wendell@masteringallyship.com, and nobody has checked that here.
