# Spec: Send back for research

<!-- The six-faces pipeline's spec template (council/spec-kit/spec.md). Stages: intake and spec are written here; the falsify section holds the cheap test; plan and build wait for Wendell's word. -->

## The ask

> "I don't know how to answer this. We should have the 6 game masters weigh in on it. This should also be a feature. If I'm stumped I can send something back to the game masters to research best practices"
> Wendell, on the board's question `jev-asset-numbers`, 2026-10-04 (saved 00:16 UTC).

**Who it is for:** Wendell, as the person who rules on the Council Board, and later any cocreator who rules on a board of their own.
**What they feel now, and what should change:** The Shaman's read: a question that asks for a number he has no basis for reads as a test he can fail, so he stalls. The change is a way to say "I don't have the footing to answer" that returns a plain-language explanation and a recommendation to him, so that stumped becomes a move he can make instead of a stall.

## Purpose

Add a third response to a board question or position, beside answering and deferring: **send back for research**. The council researches best practice for the question, with linked sources, and returns a short explanation in plain language, the options re-stated with what each would let him conclude, and a recommendation. The item stays open until he rules.

**Problem:** A question that asks for a number he does not understand gets deferred again, and spaced deferral returns it on a schedule without adding the footing he lacks.

## User stories

### Stumped

**As Wendell**, I want to send a question back when I don't know how to answer, so that the council brings me the best practice and a recommendation instead of waiting for me to guess.
**Acceptance:** A button on a question or position row says "I'm stumped: send back for research", with an optional note in his words. After it, the row shows "Sent back" and stays on the Open tab. When the council has returned, the row shows a research box with a plain-language explanation, sourced findings, the options re-stated, and a recommendation. He answers or sends it back again.

### What came back

**As Wendell**, I want the returned research written for someone who does not know the field, so I can answer.
**Acceptance:** Each box opens with a five-year-old sentence, then a worked example using his own numbers, then the sourced findings. A reader can answer the question from the box alone.

## Design decisions

| Decision | Choice | Whose |
|---|---|---|
| A new action beside defer | `sent-back` is a decision state on a board item, written like a deferral so spaced deferral's code paths are reused | council; follows `deferrals` in `board/template.html` |
| What the council does with a sent-back item | The Challenger and the Diplomat run the research (a Skeptic daemon with sources, linked and quoted, per `daemon-skeptic.md`), the Diplomat writes the plain-language box, the Sage recommends and never decides | Wendell (his words above: "weigh in", "research best practices") |
| Who decides the answer | Wendell. The recommendation is the council's and is marked as such; the research never writes a ruling | the reserved list and the Numbers rule |
| Numbers | The research gives intervals and consequences for any number he must pick. It never picks the number for him | the Numbers rule: "no number inferred on Wendell's behalf" |
| Cost | A sent-back item is researched at most once per request. A new research run needs a new send-back. The daily run's cost limits apply and the run's cost is recorded in the row | `cost-per-row`, `cost-short-rule` |
| Where the research lives | In the item's `research` block in `board_data.json`, beside `review`, and the full report beside the pass in `council/daemons/reports/` | council; follows `save_report.py` |
| Who picks it up | Any session that reads the board, and the daily standing session, when it finds `sent-back` rows with no `research` block | council; follows `due.py` |
| Scope for cocreators | The same control works on a board a cocreator rules on. Whether cocreators get their own boards is not decided here | Wendell, not yet asked |

## Contracts

**The write (from the page, same database and same shape family as a deferral):**

```json
{ "decision": "sent-back", "recorded": "2026-10-04", "steer": "<his note, optional>", "requested_at": "<UTC time>" }
```

**The return (written into `board_data.json` by a session):**

```json
"research": {  // as built, 2026-10-04; the first draft's eli5, worked_example and findings fields became lead and sections
  "title": "...", "lead": "<two sentences, plain>",
  "sections": [ { "h": "<heading>", "p": "<optional sentence>", "items": ["<short line>"] } ],
  "recommend": "<the council's recommendation, marked as the council's>",
  "sources": [ { "text": "...", "url": "..." } ], "unchecked": "<sources not relied on, and why>"
}
```

The earlier draft, kept for the record:

```json
"research": {
  "asked": "2026-10-04",
  "eli5": "<one sentence a five-year-old can follow>",
  "worked_example": "<his own numbers, with the arithmetic shown>",
  "findings": [ { "text": "...", "source": "<url>", "quote": "<short quote from the source>" } ],
  "options": [ { "v": "<option id>", "lets_you_conclude": "...", "does_not_let_you_conclude": "..." } ],
  "recommend": "<the council's recommendation, marked as the council's>",
  "report": "council/daemons/reports/<stem>.md",
  "cost": "<read from the run's own record>"
}
```

A page that cannot save shows the existing banner and keeps the choice on screen only, as the board does today.

## What the first by-hand run found (2026-10-04)

The cheap test ran on `jev-asset-numbers`. It found two defects in the design, both fixed in the requirements below.

1. **A saved steer hid the item.** The board treats any saved item as no longer open, and a steer with no choice counts as saved (`status()` in `board/template.html`). Wendell's "I'm stumped" steer moved the question to Resolved, where only the title and his steer show, so he could not see the research. The send-back control must keep the item on the Open tab until he rules, and a sent-back state must not count as saved.
2. **One paragraph was unreadable.** The first version put the research in a single `why_you` paragraph. Wendell: "readability on the information that came back. Really hard to parse". The board now renders a `research` block (lead, labelled sections with lists, the recommendation set apart, sources folded away), checked at desktop and phone width. The contract below describes that shape, which differs from the first draft of this spec.

The test is not complete: he has not yet said whether he can answer from the new box.

## Reserved items

None are decided here. A sent-back item that touches a reserved item (money, a person's name, canonical prose, consent) returns research only, and the ruling stays his.

## How we will know it failed

- **The cheap test, run before building:** Run the feature by hand on its own origin, `jev-asset-numbers`. Send the question back (this spec is the request), have the Skeptic daemon research it, write the box with the five-year-old sentence and worked example, and show it to Wendell with the question. If he answers the question from the box without another round, the design holds. This is under way: the research report is `scratchpad/skeptic-passmark-report.md` in the session that wrote this spec.
- **The result that stops the work:** He still cannot answer after reading the box, or he answers by taking the recommendation without reading the findings. In the first case the box is not footing. In the second the control is a rubber stamp.

## Definition of done

- [ ] A button on questions and positions writes a `sent-back` state, the row shows it, and the item stays on the Open tab until he rules (a steer-only save does not hide it).
- [ ] A session that reads the board finds sent-back rows with no research block and runs the research once per request.
- [x] The research box renders beside the "Since you deferred this" box, with sources opening in a new tab. (Built 2026-10-04 as `researchBox` in `board/template.html`.)
- [ ] The row's research cost is recorded from the run's own record.
- [ ] The cheap test above has been run on `jev-asset-numbers` and its result is written into this spec.
- [ ] Only Wendell can confirm: the box reads well on his phone and he can answer from it. This goes on his steps list.
