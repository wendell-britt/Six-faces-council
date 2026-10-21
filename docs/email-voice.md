# The email voice pass

Wendell overruled `em-voice-pass` on 2026-10-21: "I think we can pull in a version of the editorial pipeline we used
for MTGOA but specifically for developing an email voice. I think we also need to create that email voice so that it
doesn't trigger anti AI folk and sounds and friendly and playful as I am in real life."

This pass is that port. It takes the shape of the MTGOA editorial pipeline (`bars-engine/editorial-core`) and leaves
the book machinery behind. One profile file says what is true of his email voice, and one generic scanner reads it.

- The profile: `council/voice/email-voice.yaml`. It holds the reader, his measured traits, and the AI tells.
- The scanner: `python3 board/email_voice.py <file> [--kind reply|outreach] [--json] [--accept RULE:"reason"]`.
- The wiring: `board/email_pipeline.py draft` runs the pass on every draft (docs/email-pipeline.md).

The traits come from about 45 of his hand-written sent emails. The notes behind them stay private, and the repo
carries none of the names or bodies.

## Who reads the email

The recipient is a community member, a collaborator or an organizer, often in Portland, and many of them are wary of
AI. They stop trusting an email when it opens with a stock pleasantry, when every sentence is evenly polished, or when
it signs off `Best regards` from someone who writes `See ya then!`. The full list sits in the profile under `reader`.

## What the pass checks

Each rule in the profile has a class.

- A **tell** reads as AI to a wary reader. Examples are `I hope this email finds you well`, `I'm reaching out`,
  `Please don't hesitate`, `I'd be delighted`, `circle back`, `Best regards`, em-dashes, semicolons, bold text or
  headers, a three-item list for rhythm, a `not X, but Y` pair, a recap paragraph at the end, and the ask said twice.
- A **fit** note marks something off his voice that a reader would not take for AI. The pass measures the length
  against his band for a reply or a first outreach, the sentence length, how even the sentences are, the paragraph
  length, the exclamation points, the contraction rate, the greeting, a sign-off block on casual mail, a playful line,
  and whether the email ends looking forward.

`voice_lint` still runs on every draft, and its findings stay on the draft's `lint` list as before. The pass also reads
them and gives each rule a class from the profile. Book rules that his email breaks on purpose count as fit.
His closers (`Looking forward to it!`, `Copy that!`) are fragments by the book's rule, and the greeting and sign-off
lines are never scanned as sentences.

Every finding prints its line, the rule, the text, and what his own mail does instead.

## The two terminal states

Every tell ends in one of two states, the same rule the editorial pipeline keeps for a zero target.

1. **Rewritten.** The text changes and the next run no longer finds it.
2. **Accepted with a written reason.** `--accept rule-of-three:"three real dates, not rhythm"` accepts every hit of
   that rule in this draft. The reason travels on the draft's `voice` list and shows on the board card.

A hit handed back as "flagged for review" is neither state. `email_pipeline.py draft` refuses to place a draft while
an unaccepted tell remains, and its message says to rewrite it or pass `--accept` with a reason. Fit notes never block.
The approval hash still covers the addresses, the subject and the body, and nothing from the pass.

## Writing like Wendell

This guide is for any drafting client: a Claude thread, Zo or Codex. Write the draft this way, then run the pass.

- Open with `Hey <Name>!`. On a reply, dive straight in with no greeting: `Works for me! See ya then!`
  Keep `Hi <Name>,` for formal or job mail.
- Ask early and plainly. `Feel free to throw some time on my calendar`, `Let me know what the next steps are`.
- Keep it short. Most replies run one to four sentences, and a long one stays under eight short paragraphs.
  Each paragraph holds one or two sentences, with a blank line between.
- Use exclamation points, usually two to four in an email. Use contractions everywhere (I'm, we're, can't, gonna).
- Put in one playful line or one self-aware parenthetical. His registers include `Oh snap!`, `coming in hot`,
  a word in caps for joy (`PERFECT.`), a stretched word (`soooo`), and an aside like
  `(and actually put it in my calendar this time)`. Keep it to one or two per email, so it reads as him and not as a
  costume.
- Thank people quickly and name what you are thanking them for: `Thanks so much!`
- End looking forward, with an exclamation and no sign-off block on casual mail: `Looking forward to it!`,
  `Talk to you tomorrow!`. Formal mail ends `Best, Wendell`.
- Number a list only when it carries real content, written `1)`, `2)`.

A before and after on the first test draft is in `docs/examples/email-voice-test-draft.md`.

## Changing the voice

The profile is the one place to change it. Add a tell when a phrase keeps showing up in drafts and reads as AI, and
give it an `instead` taken from his own mail. Move a rule between `tell` and `fit` when his edits on the board show
the class is wrong. `tests/test_email_voice.py` pins one AI-sounding draft and one draft in his voice, and both must
keep their results.
