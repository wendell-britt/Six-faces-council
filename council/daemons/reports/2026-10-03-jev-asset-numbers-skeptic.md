# Skeptic report: pass mark and sample size for the Jev trial

## The cast
Hexagram 3 (Sprouting) changing to 11 (Mingling) says the trial is early, so five positives are a seed and no verdict can come from them yet. The change to 11 says the trial can work if the roles are clear, so the plan below separates teaching, marking and scoring.

## Wake Up
- Five positives is the whole evidence base, and two to five stay live. Zero labelled negatives exist, so a false-flag rate cannot be estimated today.
- Rule of three: "the interval from 0 to 3/n is a 95% confidence interval" when no event occurs in n subjects [1].
- The exact Clopper-Pearson interval is "usually conservative" (coverage "may be well above 95%"), while Wilson "can be safely employed with small samples" [2].
- Practitioner guidance suggests about 100 labelled examples (50 pass, 50 fail), split train 10-20%, dev 40-45%, test 40-45%, with the judge run "once on held-out test set" [3]. Another source says that below 60 labels the intervals get wide [4]. Source [4] is a search summary, so treat it as unlinked beyond that page.
- Anthropic's error-bars paper says evals are experiments and presents "formulas for ... planning an evaluation experiment" [5]. It also says new evals "should contain at least 1,000 questions" for good signal [6], which this trial cannot reach, so its results will be wide.

## Open Up
Raw moves: take Wilson intervals; take exact intervals; label 30 negatives; label 100; inject fake disagreements into docs; mutate real code constants to make new positives; compare against the script on the same items; set the mark after a calibration run; write the mark down first; cap the reader's budget; report counts only with no percentages.

## Clean Up
Compost: percentage-only reporting (5 positives makes each one 20 points), and tuning the mark on the scored items. A threshold chosen from a sweep over test outcomes means the threshold "has seen the test set" [7]. Pre-registration is proposed for predictive modeling because of "data-dependent decision-making" and "unintentional re-use of test data" [8]. Injected positives have a "realism gap": they "do not necessarily appear similar to organic bugs" [9], so they can test the plumbing and cannot stand in for real misses.

## Grow Up
- For reviewer-facing flags, the useful measures are precision at the reviewer's budget and false flags per reviewer, always next to the script as a baseline. Static analysis reports show false-positive shares of 76% in one industry set [10], and say tools with many false positives waste time and erode trust [10]. Paired comparison on the same items is "a 'free' reduction in estimator variance" [6].
- I could not open Google's Tricorder paper (the fetch failed), so I leave its false-positive targets out. Unlinked.
- For judge validation, a small human-labelled set gives the judge's true and false positive rates and the method should carry that uncertainty forward [11].

## Show Up
1. Label the negatives in two piles first: a teaching pile and a scoring pile, never overlapping. Aim for about 30 scoring negatives; with zero false flags in 30, the one-sided 95% upper bound on false-flag rate is 9.5% (computed below).
2. Write the pass mark, the reader budget and the script baseline in a dated file before the scored run, then run once.
3. Report counts with intervals (caught x of n, flags per reader hour), never a bare percentage.
4. Report the model against the script on the same items, with what the model added and what it lost.
5. If injected positives are used, label them as injected and keep them out of the headline recall.

## For the Player
A pass mark is the line you draw before the test: "this much catches means it passed". A sample size is how many labelled items you test on. Few items means a wide fuzzy answer.

Worked example, computed with stdlib python (Clopper-Pearson exact, 95%, two-sided; Wilson in brackets):
- 5 positives, model catches 5: 100% observed, true recall plausibly 47.8% to 100% (Wilson 56.6% to 100%).
- Model misses one (4 of 5): observed 80%, plausibly 28.4% to 99.5% (Wilson 37.6% to 96.4%).
- Model catches 3 of 5: 14.7% to 94.7%.
- If only 3 are live: 3 of 3 gives 29.2% to 100%; 2 of 3 gives 9.4% to 99.2%.
- Zero false flags among m clean statements, 95% one-sided upper bound on false-flag rate: m=10 gives 25.9%; m=20 gives 13.9%; m=30 gives 9.5%; m=50 gives 5.8%; m=100 gives 3.0%. About 29 negatives bring that bound under 10%.

One miss moves the estimate from 100% to 80%, yet the intervals overlap almost entirely. The data cannot separate "finds all" from "finds four of five".

What each option would let you conclude:
- A: a small trial can show the model caught what it was set to catch and matched the script on a handful of items. It cannot show a recall figure, and a tight pass on 5 means "no worse than weak evidence".
- B: finding "one the script missed" is a real existence result and holds even with few items. Finding all but one is compatible with a wide range of true recall.
- C: protects against tuning on the scored items [7][8]. It leaves the pass mark unchosen until the mark is fixed, and it needs enough items to split into two piles.

## Your questions
1. How many scoring negatives can you label, and will two separate piles fit?
2. How many flags per session can the reader actually read?

## Where you would overreach
I would turn a sample-size answer into a demand for statistical power that five positives can never give.

## Sources
1. https://en.wikipedia.org/wiki/Rule_of_three_(statistics) - "the interval from 0 to 3/n is a 95% confidence interval"
2. https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval - "is usually conservative"; Wilson "can be safely employed with small samples"
3. https://skills.sh/hamelsmu/evals-skills/validate-evaluator - "~100 traces with binary Pass/Fail labels"; "once on held-out test set"
4. https://arxiv.org/pdf/2605.16354 - title "Augmenting Human Evaluation with LLM Judges: How Many Human Reviews Do You Need?" (full text unreadable; the 60-label remark came from a search summary, treat as unverified)
5. https://arxiv.org/abs/2411.00640 - "planning an evaluation experiment"
6. https://arxiv.org/html/2411.00640v1 - "at least 1,000 questions"; paired differences a "'free' reduction in estimator variance"
7. https://christophermeiklejohn.com/series/the-machine-in-the-lab/the-holdout-is-a-one-way-door/ - threshold "has seen the test set" (from search summary; the page fetch returned 404, so unverified)
8. https://arxiv.org/abs/2311.18807 - "adapting pre-registration practices from explanatory modeling to predictive modeling"
9. https://arxiv.org/pdf/2208.11088 - "Evaluating Synthetic Bugs" (quote on realism gap from search summary, unverified)
10. https://arxiv.org/pdf/2601.18844 - "Reducing False Positives in Static Bug Detection with LLMs" (76% figure from search summary, unverified)
11. https://www.alphaxiv.org/abs/2601.20913.md - "small, high-quality human-labelled calibration set"

Python used: /private/tmp/claude-501/-Users-wendellbritt-The-Library--claude-worktrees-inspiring-bhabha-f752d0/a66abf59-ce24-4cbe-8f62-7767318e5305/scratchpad/ci.py
