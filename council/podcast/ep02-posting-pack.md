# Episode 2 posting pack: one computer sitting

Board row `pp-who-schedules`, Wendell, 2026-10-16: "You schedule them in one computer sitting". Nothing is bought.
Meta Business Suite schedules Instagram and Facebook for free. X goes up by hand. This pack replaces the four
phone posts in Your steps `podcast-ep2-clips-03` to `-06`. Plan for about 30 minutes; the council's estimate, not a measurement.

## The clips (what each one is)

| Clip | Length | Post on | Cover file | File name starts with |
|---|---|---|---|---|
| 1. Tom on how long do you want to feel this way | 37 s | Mon 19 Oct | `cover-clip1-how-long.jpg` | clip 1 |
| 2. Charity as domination | 59 s | Wed 21 Oct | `cover-clip2-charity.jpg` | clip 2 |
| 3. How would you like to feel | 74 s | Sat 24 Oct | `cover-clip3-how-would-you-like-to-feel.jpg` | clip 3 |
| 4. Tom on allowing the purpose | 72 s | Tue 27 Oct | `cover-clip4-allow-the-purpose.jpg` | clip 4 |

If you already posted a clip, skip its row. Dates are the ones Your steps holds now (moved by you on the board, 2026-10-16 17:51 UTC).

## Where the files are

- The four clips and `captions.md` are in `~/Downloads/podcast/ep02-clips/` on your Mac (handoff of 2026-10-08).
- `captions.md` holds an Instagram, a Facebook and an X caption for each clip. Copy from it; do not retype.
- The covers were saved with the clips' episode files. I could not see them from this session. Step 1 opens the
  clips folder; if the four `cover-clip*.jpg` files are not in it, see "If something is missing".

## Step 1. One line in Terminal

Open Terminal (press Cmd+Space, type Terminal, press Enter), paste this one line, press Enter:

```
open ~/Downloads/podcast/ep02-clips && open -t ~/Downloads/podcast/ep02-clips/captions.md && open "https://business.facebook.com/latest/composer"
```

That opens the folder in Finder, the captions in TextEdit, and Business Suite's composer in your browser (sign in as the page owner if asked).

## Step 2. Schedule each clip on Instagram and Facebook (repeat four times, once per clip)

1. In Business Suite, click Create reel.
2. Under "Share to", tick your Instagram account and your Facebook page.
3. Drag the clip's video file from the Finder window into the upload box.
4. Cover: click Edit cover, then upload the clip's `cover-clip*.jpg` from the Finder window.
5. Caption: copy the clip's Instagram caption from `captions.md` into the box. If Business Suite offers a separate
   Facebook caption, paste the Facebook caption there.
6. Turn on auto captions if the composer shows the toggle. Instagram generates them from the audio.
7. Under Scheduling, pick "Schedule", set the date from the table above and a time (the board's usual slot is fine, or 9:00 am Pacific), and click Schedule.

Check Instagram's auto captions against the words in `captions.md` once the Reel is live. Clip 4's file flags two words, Almaas and "con into", to check against the audio.

## Step 3. X goes up by hand

Business Suite does not cover X. Open x.com, post each clip's X caption from `captions.md` with the same video on its date. You can do all four today as drafts: click the pencil, pick Schedule, set the date. Scheduling is built into x.com's composer (the calendar icon).

## Before you finish

- `[episode link]` in the captions needs the episode 2 YouTube link. Replace it with the link on the X captions before scheduling them. If the YouTube video is not public yet, schedule the clips and edit this one word later.
- Tom has no social accounts, so there is no tag to add.

## If something is missing

- Covers not in the clips folder: tell the project thread "ep 2 covers missing". The session re-renders them with `council/podcast/render_reel_covers.mjs` and puts them in the thread.
- Captions file not there: same message; the session rewrites it from the transcript.
- A Business Suite screen differs from step 2: send a screenshot in the thread and the session adjusts this pack.

## After

Tick `podcast-ep2-clips-03` to `-06` on Your steps. Nine days after clip 1, paste each clip's views, saves and shares in the podcast thread (`podcast-ep2-clips-07`, now 5 Nov). Scheduling all four in this sitting meets the 2026-10-26 check, "every post on episode 2's list is published or scheduled".
