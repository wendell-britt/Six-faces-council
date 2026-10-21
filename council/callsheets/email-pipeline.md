# Email pipeline (drafts on the board, Send as permission)

ontology: none; touches: board Outreach tab, Gmail connector

Started 2026-10-21 from Wendell's step note: "hitting the send button on the council board gives permission to send the email". Pass: `email-pipeline1`. Rows: `em-send-is-permission`, `em-any-client-drafts`, `em-voice-pass`, `em-self-test-first`.

## State, 2026-10-21

- #351 builds the draft card, `board/email_pipeline.py` and `docs/email-pipeline.md`. Preview: https://claude.ai/artifact/Hv5PQwP4fn97tMWmiiJjSc
- The Gmail connector was checked on 21 October and is signed in as wendell@masteringallyship.com.
- `em-voice-pass` was overruled on 21 October: the email voice pass is built on `claude/project-thread-caz829`. The profile is `council/voice/email-voice.yaml`, the scanner `board/email_voice.py`, the doc `docs/email-voice.md`. `email_pipeline.py draft` refuses a draft with an unaccepted tell, and the card shows the `voice` list. The test draft's before and after is `docs/examples/email-voice-test-draft.md`. The test draft to `demo-wendell-self` uses the AFTER text.

## Next round brief

After #351 merges and the board is republished: export the contacts collection with ArtifactData, run `python3 board/email_pipeline.py draft --store <dir> --contact demo-wendell-self ...` to place a test draft to wendell@masteringallyship.com on the live board (create the contact doc first, same fields as the preview seed: name 'Wendell (test to yourself)', contact email, status Identified). When he presses Send, a board read runs `email_pipeline.py ready`, marks sending, sends with mcp__Gmail__send_message using explicit addresses, then marks sent with the ids.

## Open

- fetch_store.py does not export contacts for the scheduled pull.
- The reply check from the spec is not built.
