# Clip cover standard

One standard for every podcast's clip covers: Mastering the Game of Allyship, Flirtcraft, Friendcraft and any show
after them. Wendell, 2026-10-12: "Need to edit the cover images for episode one of Mastering the Game of Allyship
Podcast with Ike so they fit the dimensions of the instagram reels and the profile grid. We need to standardize this
across all of our podcasta and the thumbnail studio".

The numbers live in `cover_standard.json`. `render_reel_covers.mjs` reads them, and the Podcast Thumbnail Studio
(https://claude.ai/artifact/RAiZ3keBiE6BvDD6YKA9S8) carries the same values in its `SAFE` and `UI` constants. Change
both together.

## The file

- One image, 1080 by 1920 (9:16), JPEG. It serves Instagram Reels, TikTok, YouTube Shorts and Stories.
- The render also writes its profile grid crop, 1080 by 1440, for any tool that asks for the grid image separately.

## Where it gets cut or covered

| What | Area on the 1080 x 1920 cover |
|---|---|
| Profile grid crop, 3:4 | y 240 to 1680, full width |
| Feed crop, 4:5 | y 285 to 1635, full width |
| Reels top tabs | the top 150 |
| Reels caption, name and audio | the bottom 400 (from y 1520) |
| Reels like, comment and share buttons | the right 180 (from x 900) |

## The safe box

**x 80 to 900, y 310 to 1500.** Every word, label and drawing that matters sits inside it, so it stays whole in the
grid, in the feed and on the Reels screen. Background colour and glow run to the edges.

The render script shrinks a headline until it fits and the drawing keeps at least a fifth of the box, and fails if
anything still sits outside. Break long quotes into lines in the spec, as the episode 1 spec does
(`specs/mtgoa-ep01-isaac-holze.json`). The contact sheet marks the Reels bands in red, the grid crop in gold, the feed
crop in blue and the safe box in green. In the studio, tick "Show platform UI zones" to see the same marks.

## Posting

Upload the clip, then "Edit cover" and "Add from camera roll" to pick the 1080 by 1920 cover. Instagram then offers a
profile grid crop; the default centre crop already keeps the safe box whole.
