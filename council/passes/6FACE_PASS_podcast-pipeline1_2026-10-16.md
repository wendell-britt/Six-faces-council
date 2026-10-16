# Six-face pass: podcast pipeline 1, taking the episode work off Wendell's hands

Wendell asked on 2026-10-16 at 17:09 UTC in the Mastering the Game of Allyship project: "ok we need to do a
brainstorm to see about the best way to automate taking the Podcast episodes- uploading them, generating clips and
publishing to social media. Right now these are the big friction points and I would like to make this as ergonomic as
possible. have the 6 game masters take this on as though you were a teal level non-profit marketing manager and needed
to free up 4-5 hours a week so you could bring in more money to the organization and you found this production
pipeline as a bottleneck". The project coordinator started the thread. This is the first pass on the pipeline as a
whole. The move it weighs is `council/moves/podcast-episode.md`.

**Board read.** The board was read at 17:12 UTC on 2026-10-16 (live page and store): `steer/general`, every `pod-`,
`promo-` and `lg-` row and their resolutions, and the steps lists `podcast-ep1-clips`, `podcast-ep2-clips`,
`podcast-ep2-youtube`, `podcast-spotify` and `flirtcraft-ep1-clips`. `council/due.py --ahead 7` found nothing deferred
due. No open question covers this pass.

**Casts** (`council/iching/cast.py`, three coins each, recorded in the ledger): Shaman 58 Banter, lines 3, 4 and 5,
becomes 11 Mingling. Architect 29 Depths, no changing lines. Challenger 61 Incubation, no changing lines. Regent 20
Witnessing, lines 4 and 6, becomes 45 Gathering. Diplomat 15 Understatement, lines 4 and 5, becomes 31 Mutuality. Sage
39 Impasse, line 4, becomes 31 Mutuality.

**Daemons.** None were sent. The evidence is the record itself (two episodes, five steps lists, four threads), and one
research subagent read the threads. The pass says so rather than send daemons for show.

## Scorecard

No earlier pass on the podcast pipeline set tests. The podcast episode pass of 2026-10-07 set none that this pass
grades. `pod-promo-rhythm` set one review, after three episodes, from the clips' numbers. No clip numbers exist yet:
steps `podcast-ep1-clips-05` (due 2026-10-17) and `podcast-ep2-clips-07` are open.

## Anchor

Each episode should reach YouTube, Instagram, Facebook and X on the ruled rhythm (`pod-promo-rhythm`) with as few of
Wendell's own touches as the reserved list allows. The hours that frees go to the pipe he picked for money,
guesting on other shows (`lg-first-pipe`, ruled 2026-10-10).

## What the record shows

**The making is fast and the posting stalls.** Claude's working time on episode 2 was about half an hour across two
sittings: title options, three thumbnails and the description with 20 chapters in nine minutes on 10/07, and four clips,
four covers and the captions in sixteen minutes on 10/08. Episode 2's posting list has seven steps and none is ticked
nine days later. Its day 0 post was moved by Wendell on 10/12 and its clip dates were moved by a session on 10/14,
because nothing had gone out. Episode 1's clip 3 was due on 10/15 and is open.

**What he does in one sitting at a computer gets done.** The four YouTube steps for episode 2 were ticked within five
seconds of each other on 10/07. On 10/12, between 16:26 and 16:40 UTC, he moved episode 2's dates, posted episode 1's
clip 2 and Flirtcraft's clip 1, and sent QC his clips. That was a catch-up sitting. What is spread one post at a time
across nine days, on a phone, is what slips.

**The rounds came from rules found late.** Episode 1's clips took three threads. Each round fixed a rule that had not
been written: Zoom's chapter marker made 19-second clips read as 48 minutes, the first clips were too short, words were
burned in ("we don't want to have the words on screen. Instragram is going to take care of that."), and a cover was a
frame from the video ("This is essentially working as a youtube thumbnail but for the clips and for instagram"). All
four are now in the move and in `cut_clips.sh` and `render_reel_covers.mjs`. Episode 2 needed one round for each pick.
He also had to ask "ok we've made those changes?" when a recut had been put off to a thread he had to start himself.

**His touches per episode.** For episode 2 the board and the steps lists hold fourteen: three picks (title, thumbnail,
clip moments), four YouTube steps, a day 0 post, four clip posts, sending Tom his clips, and noting the numbers. Each
clip post is three acts: getting the video and its cover onto the phone, posting the Reel with Share to Facebook and
auto captions on, and posting again on X. How the clip videos reach his phone was never written down. The council
puts his time at two to three hours per episode with the switching between tasks. That figure is the council's
estimate from the steps, not his, and it is the number the tests below check.

## Shaman

**Banter becomes Mingling.** The exchange is the whole of it: a clip exists to start a conversation with someone who
has not met him yet. The cast becomes Mingling, which the tradition calls fortunate and then warns that flat ground
turns to slope. A pipeline that runs smoothly can also run on without anyone in it.

**The felt read is exposure, not workload.** Rendering costs him nothing; posting is the moment his face and a guest's
words go out under his name. Spread across nine days, that moment comes back nine times. A stalled post is a charge to
meet (the board's blocker panel exists for it), not a lazy afternoon.

**The Shaman recommends one act of courage per episode.** He meets the whole episode once, at a computer, says yes to
all of it, and then it goes out without him. The guest gets their clips the same day, which keeps the exchange alive
on their side too.

## Architect

**Depths, no changing lines.** Water fills each hollow and moves on, being water the whole way through. The pipeline
should do the same work each time, with no step that depends on someone remembering it.

**The machine has five stations.** First, the recording lands in a folder this project can already reach. Zoom's local
recordings can be saved into `~/Movies`, which is approved, so a session finds the file without his attaching it. Second,
one sitting on the board holds all three picks as one battle, and the clips are cut in the same thread right after.
Third, the clips and covers need a home that a scheduler and his phone can both reach. Fourth, a scheduler holds every
post with its date. Fifth, numbers come back each Monday into the plan's Results section, the way `lg-tagged-links`
already reads the walk.

**Station four is where the hours are, and two tools fit it.** Metricool is in Claude's connector directory, with tools
to create, update and list scheduled posts and to read analytics. Buffer has an API on every plan and its own MCP, but
it is not in the directory. Buffer's 2026 comparison page gives Metricool's free plan as 20 published posts a month
with no X, its Starter plan from $25 a month, and X as a $10 a month add-on, and Buffer's free plan as three channels
with ten queued posts each. Those prices are Buffer's page, unchecked against Metricool's own
(https://buffer.com/resources/buffer-vs-metricool/). Meta Business Suite schedules Instagram and Facebook from a
computer for free and does not cover X.

**The Architect finds a third position.** The binary in the ask is "automate it" or "do it by hand". The third position is that Claude
prepares and queues everything and Wendell approves the queue once per episode. The approval is one act, and the
posting is the scheduler's.

## Challenger

**Incubation, no changing lines.** What is true here is still inside the shell: no one yet knows whether a clip brings
anyone to the walk. Both clip-numbers steps are open, so the pipeline would be automating something whose worth is
unmeasured.

**What is self-inflicted.** Automating the rendering saves nothing; it already takes half an hour. Buying a scheduler
saves nothing if the approval sitting slips the way the posting did. The cheapest test is the next sitting: episode 2's
four clips, all scheduled in one go, timed.

**Falsification tests** (each names the blocker it resolves). The posting stall: by 2026-10-26, every post on episode 2's
list is published or scheduled. The hours: on episode 3, his touches number four or fewer (the council's number) and
the sitting takes under 45 minutes (the council's number). The file gap: on the first run, a clip goes from his Mac to
a scheduled draft without his hands; if it cannot, the scheduler option is wrong.

**The Challenger dissents on the clip count.** It would cut clips from four to two per episode before buying anything. The record answers
it: `pod-promo-rhythm` sets three clips and the review after three episodes, so the count waits for the numbers.

## Regent

**Witnessing becomes Gathering.** The place you watch from is itself in view. A post published by a scheduler is still
him speaking in public, and the becoming warns that where numbers collect, the weapons stay in repair.

**What must be preserved.** Publishing under his name, money, and anything naming a person are on the reserved list
(`reserved` in `council/faces.yaml`). The move says the session "never publishes, schedules, uploads or posts anything".
Changing "schedules" in that line is his ruling to make, which is why the one question below exists. Guests' family and
health details stay out of public copy. Clip rules stand unchanged: no words burned in (`pod-clip-no-words`), the
lengths of `pod-clip-length`, designed covers inside the cover standard (`pod-clip-covers`,
`council/podcast/COVER_STANDARD.md`).

**The Regent defines done.** An episode is done when every post on its list is published or scheduled and
the guest has their kit. It is not done when the files exist.

## Diplomat

**Understatement becomes Mutuality.** What is underplayed had better be there. A pipeline he sees less of only works if the
work in it is real, and the guest is the person most easily left out of it.

**The guest is the bridge.** Tom has no social accounts and Isaac was tagged only. A guest needs one link that holds
their clips, covers and captions, and a short note from Wendell. Claude can put the files in a Google Drive folder and
write the note as a draft in his Gmail; he sends it. The note goes out under his name, so the draft waits for him.

**The queue reads whole.** Every post in the queue shows whole, as it will appear: the cover, the
caption with its tagged walk link (`lg-podcast-link`), the date and the networks. He should be able to approve it on a
phone in the time it takes to read it.

## Sage

**Impasse becomes Mutuality.** The direct route is closed, and the cast says to turn back and come again with others.
The direct route is full automation, and the reserved list closes it. The way through is with others: a scheduler that
posts, and Wendell's one yes per episode.

**What each face gave.** The Shaman named the stall as exposure and asked for one act per episode. The Architect drew
the five stations and found the third position, prepared by Claude and approved once. The Challenger set the tests,
the ones that time the sitting and move a file without his hands, and wanted fewer clips. The Regent held the reserved
list and defined done. The Diplomat brought the guest in and set how the queue reads.

**The pass was not unanimous.** The Challenger's clip count is answered by the record and stays a dissent. On
the question below, the Shaman and the Architect lean to the scheduler option and the Challenger would start with the
free sitting, because no numbers yet justify a monthly cost.

**The Sage names the smallest coherent whole.** Recording lands in `~/Movies`. One board sitting holds the picks, and the same thread
cuts the clips. The posts go into a queue he approves once. The guest gets one link. The numbers come back on Monday.
The freed hours go to guest pitches.

## Positions (stand unless he flips them)

- `pp-posting-is-the-bottleneck`: the making already takes about half an hour of Claude's time per episode; the hours
  and the stalls are in the posting. Source: the steps lists named above, read 2026-10-16.
- `pp-one-sitting`: each episode gets one board battle holding the title, the thumbnail and the clip moments together,
  and the same thread cuts the clips and covers right after his picks. Source: the record's three-thread recut and
  "ok we've made those changes?"; CLAUDE.md's handoff rule.
- `pp-zoom-to-movies`: Zoom saves local recordings into `~/Movies/Zoom`, an approved folder, so a session finds the
  recording itself; he changes the setting once (steps list `podcast-pipeline`). Source: `pod-zoom-phone` (zoom.us is
  unreachable from the cloud); the approved folders.
- `pp-guest-kit`: each guest gets one Drive folder with their clips, covers and captions, and a Gmail draft he sends.
  Source: Tom has no socials (`podcast-ep2-clips-02`); `pod1-isaac-handle` ruled tag only.
- `pp-done-means-out`: an episode is done when every post is published or scheduled and the guest has their kit.
  Source: the Regent; episode 2's files existed on 10/08 and nothing went out.
- `pp-hours-to-guesting`: the hours this frees are counted against the guest pitches of `coaching-pipeline-04`.
  Source: `lg-first-pipe`, ruled guesting on 2026-10-10.

## Question (passed the reach test)

`pp-who-schedules`, owner Architect with the Regent: **Who puts each episode's posts on the schedule?** The council
recommends Claude queueing them in Metricool for his one approval per episode.

- Claude queues them in Metricool, and you approve once per episode (Shaman, Architect). Claude can then also read the
  clip numbers back each Monday. It costs a paid plan, from about $25 a month plus $10 for X by Buffer's figures, and
  it changes the move's "never schedules" line.
- You schedule them yourself in one computer sitting (Challenger). Claude prepares a posting pack, and Meta Business
  Suite schedules Instagram and Facebook for free; X is posted or scheduled by hand. Nothing is bought.
- Keep posting each clip on its day, as now. Nothing changes, and the stalls stay.

Why only he can answer: posting under his name and money are both reserved. Why not asked before: the move was written
on 2026-10-07 with posting reserved and no scheduler on record; this is the first pass on the pipeline itself. Episode
2's remaining clips are the pilot for whichever he picks.

## Tests (dated)

- 2026-10-26: every post on episode 2's list is published or scheduled.
- Episode 3: his touches number four or fewer and the sitting takes under 45 minutes (both the council's numbers).
- First run of the picked option: a clip goes from his Mac to a scheduled post or the posting pack without his hands.
