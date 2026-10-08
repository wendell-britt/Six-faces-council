# Research without a site list: a six-faces pass

**Run 2026-10-08**, from Wendell's overrule of position `net-allowlist-not-full` (saved 2026-10-08 00:14 UTC,
recorded by the board pull at 00:15, main 2382fe2). The project's coordinator started the pass. This is the first
pass on the subject; the position it answers came from board read 2358.

**The ask, in his words:** "Allows sites will bee too cumbersome to manage everytime we do research" and "Is there
another way?"

**The board was pulled first:** the 00:15 pull had recorded every save, this overrule among them.

**Inputs:** the overruled row and its reasoning; the original question `dy-network` and his steer on it (board read
28, 2026-10-03: "Sounds like we need a way to push research to environments that have access to the browser and my
credentials"); the cloud environments page, https://code.claude.com/docs/en/cloud-environments (sections Access
levels, Allow specific domains, GitHub proxy); and the reach tests below, run in this session on the built-in
environment the project uses today.

## The tests

Run 2026-10-08 about 00:25 UTC in this thread's session, which runs on the built-in environment with no settings.

| Route | en.wikipedia.org | arxiv.org page | arxiv.org PDF | supermemo.guru | gutenberg.org | integralworld.net | plato.stanford.edu |
|---|---|---|---|---|---|---|---|
| Shell (`curl`) | blocked | blocked | not tried | blocked | not tried | not tried | not tried |
| WebFetch | read | read | read | read | read | read | reached; the page asked for was a 404 |

`www.nytimes.com` was also blocked from the shell. WebSearch returned results throughout.

What WebFetch gives back is a small model's answer about the page, not the page itself, and a direct quote is cut at
125 characters (the arXiv PDF answer said so). It cannot sign in anywhere and saves nothing to disk.

## Scorecard

No earlier pass on this subject set tests. Retro 1's standing test applies: this pass names its sources above.

## The anchor

Council research should reach the sources it needs without Wendell managing a list, and a hostile page should not be
able to push to main or carry the board away.

## The casts

Drawn with `council/iching/cast.py`, three coins each; the ledger carries them under `casts`.

| Face | Hexagram | Becomes |
|---|---|---|
| Shaman | 30 Burning: *You keep saying the same true sentence, and it is consuming its subject.* | 26 Reserves: *You have been storing this and never named the day.* |
| Architect | 44 Serendipity: *You are building on one piece of evidence.* | no changing lines |
| Challenger | 29 Depths: *The bottom of this has another bottom under it.* | 2 Bearing: *The whole weight of this is yours, unasked.* |
| Regent | 9 Restraint: *A small rule you never revisited is holding all of this.* | 61 Incubation: *What is true here is still inside the shell.* |
| Diplomat | 4 Fog: *You are guessing where you could ask.* | 35 Sunrise: *This is becoming visible faster than you planned.* |
| Sage | 14 Noon: *There is a lot here, and all of it is visible.* | 26 Reserves: *You have been storing this and never named the day.* |

No daemons were sent: the question turned on two facts the session could test itself.

## Shaman

**Burning becomes Reserves.** The council kept repeating one true sentence, that the network blocks research,
until it consumed the subject. What he wants is the reading, not the plumbing.

**The felt cost is the list itself.** His word is "cumbersome": every new source would be a stop, a settings dialog,
and a wait. A route that asks nothing of him per site is the only one that matches the ask. The Shaman backs any
option with no per-site step.

## Architect

**Serendipity has no changing lines.** One piece of evidence is not enough, so the Architect asked for seven sites, a PDF,
and both routes before building on it.

**Two routes leave a session, and only one is behind the list.** The shell goes through the environment's network
and was blocked everywhere it tried. WebFetch and WebSearch reached every site tried. The council's research
already runs on those two tools: every daemon in `.claude/agents/` lists WebSearch and WebFetch as its research
tools. The first daily run named Wikipedia, arXiv and supermemo.guru as blocked because it tried them from the
shell.

**So the change is a rule, not a setting.** Research reads through WebFetch and WebSearch. The shell fetches only
what must land on disk, and that is rare in council work.

## Challenger

**Depths becomes Bearing.** Under the first answer is a second one, and the Challenger looks for it.

**The old row overstated the risk.** It said a tricked session "can send that token" anywhere. The docs say the
GitHub token never enters the session: "all GitHub operations go through a dedicated proxy that keeps your real
GitHub credentials outside the session's VM, independent of the environment's access level" (GitHub proxy). What a
tricked session can still do is push through that proxy, or send text it has read, the board included, inside a
URL it fetches.

**WebFetch narrows the first door and leaves the second.** A hostile page reaches the session only through a small
model's answer to a question the session asked, which is a thinner channel than raw HTML in a shell. A fetch URL can
still carry data out. That is true of WebFetch at any network setting, so full access would add the shell as a
second way out and gain nothing for research.

**The limits are real and should be named.** Quotes stop at 125 characters, a page behind a login is out of reach,
and a file cannot be saved. For a long quote, a paywalled paper or a dataset, the session needs another route.

## Regent

**Restraint becomes Incubation.** A small rule nobody revisited, "add the site to the list", was holding the
whole plan. Dropping it costs nothing that is in use: the steps list `council-research-network` was never ticked.

**What guards main stays as it is.** Rows reach main only through `board/sync_board.py`, `council/faces.yaml`
changes wait for his label, and the network stays at the built-in default. None of that depends on which sites a
session can read.

**The rare download goes where he already pointed.** His 3 October steer asked for research to go to "environments
that have access to the browser and my credentials". Remote Control on his Mac is that: his browser, his logins,
and nothing in the cloud session's reach. A download that needs the shell goes there, asked for in the thread that
needs it.

## Diplomat

**Fog becomes Sunrise.** The council guessed that the list was the only door, where a two-minute test could have
asked. The test is in this pass now, and it should have been in the first one.

**Nothing here asks him for anything.** No settings dialog, no step, no cloud environment to create. The steps list
leaves his Your steps tab.

## Sage

**Noon becomes Reserves.** Everything is visible here: two routes, one blocked and one open, and a risk smaller
than first written.

- The Shaman set the bar: no per-site step for him.
- The Architect found the route that clears it, WebFetch and WebSearch, and tested it on seven sites.
- The Challenger corrected the old row's claim about the token and named WebFetch's limits.
- The Regent kept the guards on main and sent the rare download to his Mac, as he asked on 3 October.
- The Diplomat removed his step.

**No face dissents from the position.** The Challenger records that WebFetch can still carry data out inside a URL, which
no network setting closes. The pass was unanimous on the position, which is a flag: every face reasoned from the
same test, run once, in one session. If a later session finds WebFetch blocked on a site, that is the test failing.

## Outputs

**Position `net-research-webfetch`** (Architect, Regent). Council research reads through WebFetch and WebSearch,
which reach public sites without any list. The cloud environment stays as it is, no site gets added by hand, and
the research-sites steps leave Your steps. A file that must be downloaded goes to Remote Control on your Mac. Why
it did not need Wendell: his steer asked for a way with no per-site work, and this one needs nothing from him.

**Questions:** none. The reach test: whether to open the network fully is still his to choose, but this position
removes the reason he had for it, so asking now would not change what gets built.

## Tests for the next pass

- By 2026-10-22: the next research run (daily Wake up or a daemon) quotes at least one of Wikipedia, arXiv or
  supermemo.guru through WebFetch. If it reports a site blocked, record the site and the route it used.
- By 2026-11-08: count the research tasks that needed Remote Control for a download. If it is more than two, the
  council revisits a Custom domain list for those hosts only.
