# Email voice pass: the test draft, before and after

The callsheet names a first test draft to Wendell's own address (contact `demo-wendell-self`). No earlier session
wrote a body for it, so the BEFORE is the plain test email a session writes by default. The pass output below is
pasted from `python3 board/email_voice.py <file>` as run on 2026-10-21.

## Before

```text
Dear Wendell,

I hope this email finds you well. I'm reaching out to test the new email pipeline on the Council Board. This message is a test of the Send button — it confirms that an approved draft can travel from the board, through Gmail, and back.

Please don't hesitate to reply if anything looks off; your feedback is greatly appreciated. I would be delighted to circle back on any issues.

In summary, this is simply a test, and once again, no action is required on your part.

Thank you for your time and consideration.

Best regards,
Claude
```

## The pass on the before

```text
email voice pass (outreach): 13 open tell(s), 0 accepted, 3 fit note(s)
  L1   TELL dear-opener: "Dear Wendell,"
         his mail: "Hey <Name>!" (or "Hi <Name>," for formal mail).
  L3   TELL finds-you-well: "I hope this email finds you"
         his mail: Open with "Hey <Name>!" or go straight to the point.
  L3   TELL reaching-out: "I'm reaching out"
         his mail: Say the thing. "Hey <Name>! Quick one:" and then the ask.
  L3   TELL em-dash: "...test of the Send button — it confirms that an app..."
         his mail: A period, a comma, or a parenthetical. Hand-typed mail has no dashes.
  L3   TELL rule-of-three: "the board, through Gmail, and back."
         his mail: Keep the one or two that matter. Three-item rhythm reads written-by-machine.
  L5   TELL dont-hesitate: "Please don't hesitate"
         his mail: "Feel free to throw some time on my calendar" or "Let me know!"
  L5   TELL delighted: "I would be delighted"
         his mail: "I'm in!" or "Sounds like a PLAN!"
  L5   TELL circle-back: "circle back"
         his mail: "Talk soon!" or name the day: "Catch you tomorrow!"
  L5   TELL semicolon: "...ly if anything looks off; your feedback is greatl..."
         his mail: Two sentences, or an exclamation point.
  L7   TELL recap-closer: "In summary"
         his mail: Stop when the ask is made. End forward-looking: "See ya then!"
  L7   TELL restated-ask: "once again"
         his mail: Ask once, early. The ending looks forward instead.
  L9   TELL time-and-consideration: "Thank you for your time and consideration"
         his mail: Quick, specific thanks: "Thanks so much!"
  L11  TELL regards: "Best regards"
         his mail: End on a forward-looking exclamation ("Looking forward to it!") and no sign-off block. Formal mail: "Best, Wendell".
  L3   fit  no-exclamation: "no exclamation point"
         his mail: Nearly every email of his has one, often 2 to 4: "Looking forward to it!"
  L3   fit  no-playful: "no playful line"
         his mail: One playful line or a self-aware parenthetical: "(and actually put it in my calendar this time)"
  L9   fit  flat-ending: "Thank you for your time and consideration."
         his mail: End forward-looking: "Looking forward to it!", "See ya then!"
Rewrite each TELL, or accept it with a reason: --accept RULE:"why it stays".
exit 1
```

## After

Subject: `First round trip through the Send button!`

```text
Hey Wendell!

Oh snap, this is the very first round trip through the Send button on the council board!

You pressed Send, a Claude picked it up, and Gmail carried it to your own inbox (so far so good lol).

Reply if you feel like it, or just ignore it. Either way we're good to go!
```

## The pass on the after

```text
email voice pass (outreach): 0 open tell(s), 0 accepted, 0 fit note(s)
exit 0
```

The rewrite opens with his greeting, says what the test is in the first line, keeps one playful aside, and ends
looking forward. It has no sign-off block.
