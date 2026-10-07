# The podcast episode move

A move the council runs once per podcast episode. It turns a recording into what the episode needs to go out: a
title, a description with chapters, a YouTube thumbnail and three short clips for Instagram, Facebook and X.
Wendell picks the title, the thumbnail and the clip moments on the Council Board, and uploading and posting stay on
his Your steps list.

## The ask, in his words

Wendell, 2026-10-07, in the Mastering the Game of Allyship project, attaching the transcript of episode 2:

> ok I want to start on the podcast work
>
> Looking for a title and description of the episode and want to integrate the creation of the Podcast Youtube
> Thumbnails into the council board workflow

The pass that designed this move is `council/passes/6FACE_PASS_podcast-ep2_2026-10-07.md`. Its first run is
episode 2 of the Mastering the Game of Allyship podcast, with Tom Hurlburt.

## When it runs

It runs when Wendell attaches an episode's transcript, audio or video in a project thread, or says an episode is
recorded. It runs for any show he hosts, so the Flirtcraft podcast's episodes use it too (battle
`fr-podcast-launch`, position `pod-ep1-from-audio`).

## The six steps

1. **Read the recording.** The session reads the whole transcript. A Zoom VTT has the speaker on each cue, and a
   few `grep` calls on phrases give chapter times. Claude's cloud sessions cannot open zoom.us
   (`pod-zoom-phone`), so the file has to come from him.
2. **Draft the copy.** The session writes three to four title options with one recommended, a YouTube description
   with chapters, and a two-line description for Spotify and Apple Podcasts. The copy follows the brand voice: dry
   honesty over hype, and no urgency or scarcity. It goes in the project files at
   `podcast/<episode>/episode-copy.md`. The title and the thumbnail are drafted together, so they do not repeat each
   other: the title carries what people search for, and the thumbnail carries the hook.
3. **Render the thumbnails.** The session writes `podcast/<episode>/thumbnails/spec.json` with two to four concepts,
   each with its own hook, and runs:

   ```
   NODE_PATH=$(npm root -g) node council/podcast/render_thumbnails.mjs <spec.json> <out-dir>
   ```

   Each concept becomes a 1280 by 720 PNG, the size YouTube asks for, in Mastering Allyship's look from the live
   `/mastering-allyship` page in bars-engine. A contact sheet shows every draft at full size and again at the size
   a phone's search results show it. A hook that cannot be read at the small size is redrawn before anything
   reaches him. When he supplies a still from the video, a concept can name it as `photo` and the layout puts it on
   the right.
4. **Put the picks on the board.** The title and the thumbnail are two questions on the Council Board, each with
   the options and one recommended, because both publish under his name and both are matters of taste
   (`reach_test` in `council/faces.yaml`). The description goes on the board as a position that stands unless he
   flips it. The episode is a battle on the board's map, with one round per draft he reviews. The contact sheet is
   attached in the thread, because the board shows text, not pictures.
5. **Write his steps.** Uploading needs his YouTube account, so the session writes a Your steps list: open the
   video in YouTube Studio, paste the title and description, upload the picked thumbnail, and publish. A custom
   thumbnail needs a channel with phone verification, so the list says so where that applies.
6. **Pick and cut the clips.** Added on 2026-10-07, when Wendell asked for episode 1's clips and said "I think we
   need a strategy for marketing episodes that have been created". The session proposes three or four clip moments
   from the transcript, each with its start and end time, its words and why it stands on its own, and at least one of
   them is the guest's. Lengths follow board row `pod-clip-length`: one or two of 60 to 90 seconds for the strongest
   stories, one or two of 30 to 60 seconds for sharp lines, none under 30, and each opens on its strongest line. The
   moments are one question on the board. Once he picks, and the episode's video is in a folder on his Mac that the
   session can reach, the session cuts each clip there with ffmpeg, vertical at 1080 by 1920, with no words burned
   into the video. Wendell, 2026-10-07: "we don't want to have the words on screen. Instragram is going to take care
   of that." He turns on Instagram's auto captions when posting, so his Your steps list says to, and the captions
   file carries the clip's words for checking them (row `pod-clip-no-words`). A clip cut from a Zoom recording keeps
   Zoom's "Recording Started" chapter, which makes players show the whole meeting's length (episode 1's 19-second
   clip showed as 48 minutes), so every cut drops it: `ffmpeg -i in.mp4 -map 0:v -map 0:a -map_chapters -1 -c copy
   out.mp4`, then `ffprobe` checks the length. A cut that re-encodes (to reframe to vertical or join two spans) drops
   it with `-map_chapters -1`, and ends the audio chain with `asetpts=N/SR/TB`, or the audio track reports a fraction
   of its real length (episode 1's 50-second recut first read as 12 seconds). Each clip also gets an Instagram cover,
   designed like the YouTube thumbnails and never a frame from the video (Wendell, 2026-10-07: "This is essentially
   working as a youtube thumbnail but for the clips and for instagram"): `council/podcast/render_reel_covers.mjs`
   renders one 1080 by 1920 cover per clip from a spec beside the episode's files, with the words and drawing inside
   the middle 3:4 that the profile grid shows, plus a contact sheet. The covers go to him in the thread, so he can
   save them to his phone and pick each one as the Reel's cover ("Edit cover", then "Add from camera roll"). It
   writes an Instagram, a Facebook and an X caption for each clip in `podcast/<episode>/clips-and-captions.md`, and a
   Your steps list that posts them on the rhythm in the project files' `podcast/episode-marketing-plan.md`: the
   episode on day 0, then one clip on days 2, 5 and 9.

## What it leaves alone

- It never publishes, schedules, uploads or posts anything, and it never messages a guest. Publishing under his name is reserved to him.
- It writes no quote of a guest that the recording does not hold, and it keeps a guest's family and health details
  out of public copy unless the guest offered them for that purpose.
- A guest named in the copy is a person named in public, which is on the reserved list. The description therefore
  stands only as a draft until he lets it stand on the board.
