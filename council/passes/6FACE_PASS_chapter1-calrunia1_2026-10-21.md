# Chapter 1 inside Calrunia: the demo as the first route through the world

**Run 2026-10-21**, started by the project coordinator after the board pull of 01:48 UTC
(`council/ledger/2026-10-21-pull-014837.json`), where Wendell overruled `cw-chapter1-first`. Pass `chapter1-calrunia1`,
the first on how the Chapter 1 demo and the Calrunian world fit together. Design ontology loaded (profile
`game_design`). Callsheets: `council/callsheets/chapter1-demo.md`, `council/callsheets/calrunia-world.md`.

**The ask, in his words** (steer on `cw-chapter1-first`, overrule):

> How can we more tightly integrate chapter 1 and this work? It feels as though leaning into what has most of the mechanical elements of the book (which is now the game) can give peopel a taste of the practice as they are learning the content through play

Same pull: `cw-front-door` answered **A, the ship**; `cw-qi-meter-scales` stands with the steer "Vibeulons are the gold
of friendcraft too". The coordinator's note adds that the Kickstarter still launches on the Chapter 1 demo, so its
path stays short, and that the passport is being built in its own thread.

**Inputs:** sprout `campaigns/mtgoa-ch1/` (extract, story, encounters, guessing test) and `prototype/ch1-arcade.html`;
sprout `docs/decisions/calrunia-and-domains.md`; pass `calrunia-world1` and `calrunia/world.yaml`; the Allyship Deck
(bars-engine `public/allyship-deck/allyship-deck.json`, 147 cards); `ontology/v0.1/QUICKSTART.md`. Read by one worker.

**Casts** (`cast.py`, three coins):

| Agent | Hexagram | Shows |
|---|---|---|
| Shaman | 29 Depths, changing to 53 Emergence (lines 2, 3, 6) | The bottom of this has another bottom under it. |
| Architect | 50 The Cauldron, changing to 44 Serendipity (line 5) | This is being transformed, and you are carrying it by the handles. |
| Challenger | 23 Erosion, changing to 39 Impasse (lines 3, 5, 6) | The ground under this is going and you have not said so. |
| Regent | 59 Dispersal, changing to 29 Depths (line 6) | What you were holding rigid is coming apart. |
| Diplomat | 59 Dispersal, changing to 2 Bearing (lines 2, 5, 6) | What you were holding rigid is coming apart. |
| Sage | 1 Unbroken, changing to 26 Reserves (lines 4, 5) | Every line here sends, and the return has nowhere to land. |

**Daemons:** none sent.

## Scorecard

Pass `calrunia-world1` set W1 (a spirit survives guest to sign-in and cave to Between) and W2 (no place writes a field
another owns). Neither can be graded yet: the passport is still being built. Its position `cw-chapter1-first` was
overruled, so this pass replaces it.

## Anchor

Chapter 1 is the player's first road into Calrunia: they learn the book's first lessons by doing the practice, and
when the chapter ends they are standing aboard their own ship with the spirit they woke, the cards they played and
one blank card, ready to come back tomorrow.

## What the record already answers

- **Where Chapter 1 ends.** `cw-front-door` A, as written on the board: "Chapter 1 still opens in Sprout once, as the
  pull, and ends with you aboard." He picked it at 01:46 UTC. So the demo's last screen is the ship.
- **Where Chapter 1 happens.** `mh-calrunia-hall` and sprout's `calrunia-and-domains.md`: Sprout is Calrunia in its
  Early Regent era, and the ship is the world's far future. The Arcade is a place on the same planet.
- **What the hollow is.** sprout `story.md` A7: the hollow's door is the hand-off to the 3D WAVE room; `world.yaml`
  puts the WAVE room aboard the vessel.
- **What carries over.** `cw-passport`: one player record, guest in the browser first; `world.yaml` already says the
  Chapter 1 demo runs as a guest and lists `hand` and `spirits` on the passport.
- **Where it is hosted.** Standing rule of 2026-10-17: playable spaces are hosted on bars-engine.vercel.app, never an
  Artifact page.

## Shaman — 29 Depths, becoming 53 Emergence

Depths says there is a floor under the floor, and Emergence says there are stages that cannot be skipped. **What moves
under his steer is that a reader should feel the practice work on them before they are told its name.**
Chapter 1 already does this more than its callsheet admits: the player grounds a real feeling to burn through a gate
(A3), sits outside a closed door until it opens (A6), and grows a spirit from their own urge without being scored
(A8). **The stage that cannot be skipped is the return.** A practice is something you come back to, and today the
page ends on "Copy this" and "Play again". Per his lesson `mh-input-chosen`, the player should leave with a move to
use in real life. The smallest true version: the blank BAR card the chapter hands them becomes the first question their
spirit asks about aboard the ship, so the next visit is the practice, not a replay.

## Architect — 50 The Cauldron, becoming 44 Serendipity

The Cauldron says the raw material is already in the pot; Serendipity warns against building on one piece of
evidence. **The machine needs three joins and no new engine.**

**Join one: the hollow is the ship's WAVE room.** The 2D hollow in `ch1-arcade.html` stays for the Sprout page; its
last beat becomes a "Step through" link to bars-engine, where the WAVE room and the barn live. **Join two: the
hand-off travels in the link.** The page is served from sprout's host and the ship from bars-engine, so browser
storage will not cross. The end screen already builds the full record (cards played, stance, warden record, Pip's
line, the spirit's element, family and name, BAR text). It goes in the URL fragment as passport-shaped JSON, and an
arrival route on bars-engine writes it into the guest passport. It needs no server, no account and nothing to install.
**Join three: `world.yaml` gets a `chapter1` route** that names, for each beat, the Calrunian place whose practice it
previews, so W2 covers Chapter 1 like any other place.

**The book's renewable token is the vibeulon.** Chapter 1 teaches two kinds of token (extract lessons): the borrowed
kind that comes due, and the renewable kind made by burning a feeling through. That second kind is exactly what
`cw-qi-meter-scales` calls condensed qi. So A3's burn-through mints the player's first vibeulon into the passport,
and the sky glow on the hollow's far wall at A8 is the qi meter's first showing. The book's words (mana, tokens) stay
on the Sprout page; the passport uses the world's words.

**The beat-to-place map, which builds nothing new:**

| Beat | Practice the player does | Calrunian place that owns it |
|---|---|---|
| A1, A2 Tam's farm | carry one; two counters | Sprout's settlement |
| A3 to A5 Yun's dojo | burn a feeling through; stance on empty | Root, the training ground (`cw-root-training-ground`) |
| A6 Pip's warden | small moves open small doors | the trust rules the Between runs on (`cw-between-two-ships`) |
| A7 the oath | seven lines said aloud | the hollow's mouth |
| A8 the hollow | a spirit from your charge; push hands | the ship's WAVE room, then the barn |

## Challenger — 23 Erosion, becoming 39 Impasse

Erosion says the ground is going and nobody has said so. **Two supports are wearing away under this plan.** First, the
card fit: the guessing test scored 12 of 18 on paper and Wendell's own play matched 3 of 6, with A6 and A8 the
misses. Dealing more of the deck (one card per move) before that is settled multiplies a known weakness; I dissent
from any option that adds cards before a second player has played A6 and A8. Second, **the ship is not on main.**
`world.yaml` points the vessel at bars-engine `content/ontology-game/cave/vessel.js` and `oag.vessel.v1`, which exist
only on the unmerged inner-vessel branch (bars-engine #399, waiting on his note on the dock). An arrival screen
"aboard the ship" either waits for #399 or lands on a plain barn page first. The honest short path is the second:
an arrival page that shows the spirit, the hand and the blank card, which the ship absorbs when #399 merges.
**Scheduling truth:** the Kickstarter video should record the route only once it plays end to end, so the video
step stays waiting; it does not start on the old page.

## Regent — 59 Dispersal, becoming 29 Depths

Dispersal says what was held rigid is coming apart, and it is: `cw-chapter1-first` kept the world behind the demo, and he
dissolved that. **What must be kept is the gate itself.** His words of 2026-10-14 make the demo the Kickstarter gate,
and his lesson `mh-scope-only` says work that serves a gate runs beside it, never behind it. So every join must make
the demo better as a demo; anything that only serves the world after launch waits. **Obligations, not preferences:**
the passport carries no global rank (Regent, `calrunia-world1`); dojo standing never becomes a world number; and the
BAR text is the player's own words, so the passport stores it for them and no place reads it for scoring
(QUICKSTART: intimate disclosure is not progression currency). **Whose word:** the book's terms stay on the page;
vibeulon is the world's term and appears only aboard.

## Diplomat — 59 Dispersal, becoming 2 Bearing

The same Dispersal, becoming Bearing: the whole weight is carried, unasked. **The people this must bridge to are
backers who have never heard of Calrunia, and Portland readers allergic to AI.** The route has to play with no model
and no sign-in: guest passport, link hand-off, plain data the player can read. **A backer must not feel switched
between two games.** The hand-off screen says in the story's voice where they are going ("the hollow opens onto a
ship you did not know was yours") and the arrival page looks like the same chapter, not a new product. **Who is
excluded:** a reader on a slow phone. The arrival page is 2D first; the 3D WAVE room is one tap further, never the
gate to seeing your spirit.

## Verdicts

| Face | Ends aboard the ship | Link hand-off to a guest passport | A3 mints the first vibeulon | Beat-to-place map | How much practice to add |
|---|---|---|---|---|---|
| Shaman | yes | yes | yes | yes | inside the beats, plus the return |
| Architect | yes | yes | yes | yes | inside the beats |
| Challenger | yes, on a plain arrival page until #399 | yes | yes | yes | inside the beats; dissents on more cards now |
| Regent | yes | yes, no rank, BAR text private | yes | yes | inside the beats |
| Diplomat | yes, 2D first | yes | yes | yes | inside the beats or an epilogue |
| Sage | | | | | names the split |

## Dissent check

Not unanimous. The Challenger dissents from dealing one card per move before the A6 and A8 fit is settled; the
Diplomat leans toward a short epilogue aboard; the rest want the practice inside the existing beats. Five agreeing on
the joins is a flag that they were cheap to agree on, since each only reuses what exists.

## Sage — 1 Unbroken, becoming 26 Reserves

Unbroken says every line sends and nothing receives; Reserves says a store has been kept and never given a day.
**The store is Chapter 1 itself: it already holds most of the book's mechanics** (the deck as a hand, the six
faces as stances, the charge and its element, the daemon families as the urge, push hands, the trust rules, the oath,
the BAR). What it lacked was a place to land. The smallest coherent whole is the Architect's three joins, the
Shaman's return, the Regent's gate rule and the Challenger's plain arrival page. **Order:** the passport thread's
schema first, then the link hand-off and arrival page, then the video. **What Wendell alone decides** is how much of
the practice a first-time player tries before the chapter ends: inside the beats, an epilogue aboard, or a card from
every move. I keep the Challenger's dissent and set down nothing.

## Outputs

### Positions (stand unless he flips them)

- `c1w-first-route`: Chapter 1 is the first route through Calrunia. It opens once in Sprout's settlement and ends
  aboard the player's ship, where the spirit they woke waits in the barn (`cw-front-door` A, story A7).
- `c1w-link-handoff`: the Chapter 1 page hands its end record to bars-engine in the link itself, as passport-shaped
  data, and an arrival route writes it into the guest passport. No sign-in, no server, no model.
- `c1w-renewable-vibeulon`: the book's renewable token, made by burning a feeling through at A3, is the vibeulon. A3
  mints the player's first one into the passport, and the hollow's sky glow is the qi meter's first showing. The book's
  words stay on the Sprout page.
- `c1w-beats-are-places`: each Chapter 1 beat names the Calrunian place whose practice it previews (Sprout, Root, the
  Between's trust rules, the WAVE room), recorded as a `chapter1` route in `calrunia/world.yaml`. No new engine.
- `c1w-arrival-page`: until the ship (bars-engine #399) merges, Chapter 1 lands on a plain 2D arrival page that shows
  the spirit, the hand and the blank card, and the ship absorbs it when #399 merges.
- `c1w-video-after-route`: the Kickstarter video records the whole route, Sprout to the ship, once it plays end to
  end. The step still waits on his go.

### Question

- `c1w-taste-depth` (Shaman, Architect): how much of the practice should a first-time player try before Chapter 1
  ends? Options and consequences on the board. Only he can answer: his steer asks to lean in, and the Kickstarter gate
  asks to stay short, and the trade between them is his preference. Not asked before: the overrule came at 01:48 UTC
  today.

### Tests

- **C1 (after the arrival page):** play the Chapter 1 page on a phone to the end, tap Step through, and the arrival
  page shows the same spirit name, element and family, the cards played and one vibeulon. Pass: all match, no sign-in.
- **C2 (desk):** every beat in `world.yaml`'s `chapter1` route names one place, and the passport fields Chapter 1
  writes are a subset of the passport schema. Pass: the contract test accepts a Chapter 1 fixture.
- W1 and W2 carry over unchanged.

## Build brief

Two threads, after the passport schema lands.

1. **bars-engine (Opus, no art):** an arrival route (`/calrunia/arrive`) that reads passport-shaped JSON from the URL
   fragment, validates it against `schema/passport.schema.json`, writes the guest passport, and shows the spirit, the
   hand, the vibeulon and the blank card in the chapter's look. A Chapter 1 fixture in the passport contract test.
   Vercel preview link opened with a sample fragment.
2. **sprout (Sonnet, once #52 to #55 are merged):** the end screen of `prototype/ch1-arcade.html` gains Step through,
   encoding the record into the arrival link; A3 records one vibeulon; the story line at the hollow names the ship.
   Then `world.yaml` gains the `chapter1` route (council).

The answer to `c1w-taste-depth` adds to brief 1 or 2; it does not block the joins.

scout: rung 2, we have it. Every join reuses the existing page record, the passport being built and the bars-engine
host; nothing new is built that a tool would do.

## Not checked

The manuscript's `ch1.md` itself; sprout `design.md`; whether the sprout host and bars-engine share any origin (assumed
not); the URL length of a full record on phones (a probe in brief 1 should measure it); the ontology's encounter
families in the model files.
