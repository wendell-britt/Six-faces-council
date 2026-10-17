# Six-face pass: the projection paint-over as a technique (2026-10-17)

Called by Wendell, in the thread "The Between: the hollow", 2026-10-17. His words, after reading a post about turning
concept art into a playable 3D world:

> "How does this compare to what we already do?"

> "Let’s bring in the game design ontology and add this as a technique. I’d want to see how each of the game master
> faces would interface with this kind of pipeline"

First pass on this subject. Ontology loaded: `default` (`ontology/v0.1/QUICKSTART.md`) plus the pending
`asset_sourcing` brief (`docs/codex/asset-sources-brief.md`), which is where a technique for making game surfaces
belongs. No daemons were sent; subagent tokens: 0.

## The technique, as the post describes it

1. A cel-shaded concept picture is made with GPT.
2. A model rebuilds the layout as simple 3D blocks (the blockout).
3. A screenshot of the blocks is taken from a fixed camera.
4. GPT paints over that screenshot, using the concept as reference.
5. A shader projects the painting back onto the blocks from the same camera.
6. Interiors repeat the loop. Characters are GPT pictures animated with Minimax.

The film industry has done steps 2 to 5 by hand for decades as camera-projection matte painting: a painter paints over
a render, and the painting is projected onto rough geometry from the render's camera. Blender has the tools for it built in
(a camera, the UV Project modifier, and baking). What the post adds is who paints: a model instead of a matte painter.
The council calls the technique the **projection paint-over** (the council's name, expected to be cut if a better
one turns up).

## What we do today

From the Between thread's reply (15:40 today): Wendell's ChatGPT concept views are the target, a session rebuilds the
layout in three.js or Blender and paints it in code, with real lights, flicker and sound. The result moves and lights
well and does not look like the illustration (`/mnt/project-files/between/round2/build/concept-vs-build.jpg`). The
hollow's round 2 geometry (bars-engine #366, `public/between/hollow.js`) is already a blockout, and the four concept
views are in `/mnt/project-files/between/round2/concept/`.

## Scorecard

No earlier pass on this subject, so no tests to grade. Three tests are set at the end.

## Anchor

Make a space that looks like the picture Wendell fell for and still plays, on a phone, without modelling every detail,
and keep every rule the record already holds about who made the art.

## Casts

| Face | Cast | Becomes |
|---|---|---|
| Shaman | 59 Dispersal (lines 1, 5) | 41 Spending |
| Architect | 7 Muster (line 4) | 40 Thaw |
| Challenger | 44 Serendipity (lines 5, 6) | 32 Endurance |
| Regent | 1 Unbroken (line 2) | 13 Fellowship |
| Diplomat | 23 Erosion (no changing lines) | none |
| Sage | 18 Stale Air (lines 4, 5) | 44 Serendipity |

The Sage's first cast printed past the end of the output window before it was read, so the Sage cast again. The
ledger record carries the second cast.

## Shaman

**The Shaman casts 59, Dispersal, becoming 41, Spending.** What was held rigid comes apart, and the change has a price nobody has
named yet. What is rigid here is the habit of rebuilding every picture in code and accepting that it looks less
alive than the picture. The price is whose hand is on the surface.

**The felt target is the picture's spell.** Wendell and Ari responded to a painted place, with a painter's light and a
painter's softness. A procedural rebuild keeps the layout and loses the spell. The projection paint-over keeps the spell
because a painting is literally the surface.

**The paint-over is the most human step in the loop.** Painting over a screenshot of your own place is something a
person can do on a phone or an iPad with a finger. For the Between, a place two people make together, the painting
itself could be play: each person paints a wall of the hollow. That is belonging made by hand (constitution 7,
relationship can create capability). The council does not assume Ari wants this; it is an offer, and Ari is invited
only after Wendell ticks his Between steps.

**The risk is a broken spell.** A painted place that tears when you step off the painted spot feels worse than a plain
place, because it promised more. The Shaman judges each view by sitting in it, not by a still.

**The Shaman owns the felt brief.** Before any paint-over, the Shaman writes one line per view: what it should feel like to be here. After
it, the Shaman sits in each view and says whether the line came true. The Shaman owns the felt brief and the felt
check.

## Architect

**The Architect casts 7, Muster, becoming 40, Thaw.** The fact that would organise this has not been said: which cameras. Once it is said,
the work moves fast.

**The camera is the contract.** Every stage after the blockout depends on one record per view: position, target, field
of view, aspect and resolution, with an id. The capture, the painting and the projection all carry that id. A painting
without its camera cannot be projected correctly, so the record is what makes the technique repeatable.

**The machine, in five parts.**
1. Blockout: the scene's own geometry, as it ships (for the hollow, `hollow.js`).
2. Capture: for each camera record, a colour render of the blocks with flat light and a depth render.
3. Paint: an image at exactly the capture's size, painted over the colour render.
4. Project: in the shader, each surface point is transformed by the capture camera's view and projection to find its
   place in the painting. Where several views see a point, they blend by how squarely each camera sees it. Where no
   camera saw a point (the depth render shows it was hidden), the surface falls back to its plain material.
5. Live layers: fire, lanterns, motes, the creature and the players draw on top with their own light. The painting's
   light is baked, so live light is added, never relied on for the base look.

**A third position exists.** The choice is not "projected painting versus procedural paint". Near, walkable surfaces can keep
procedural paint while far and set-dressing surfaces take the projection. For Blender scenes, the projection can be
baked once into ordinary textures (UV Project, then bake), so the phone draws plain textures and the Blender pipeline's
manifest registers them like any other asset. For the hollow, a three.js scene, the runtime shader is simplest.

**The Architect owns the machine.** It owns the camera records, the projection shader or bake, the fallback for unseen surfaces,
and the measurement of stretch away from each camera.

## Challenger

**The Challenger casts 44, Serendipity, becoming 32, Endurance.** We are building on one piece of evidence: a post. This exact exchange
has happened before: a demo that looks right from where it was filmed.

**Where it breaks.**
- **Off the painted spot.** Surfaces seen edge-on smear, and anything hidden from the camera has no paint. A
  free-walking camera finds both in seconds. This is why it fits the hollow (small, a few set views) and does not fit
  the caves.
- **Seams between views.** Four paint-overs made separately will not agree where they overlap: a different stone
  colour, a different light direction. GPT varies from call to call, and so does a person.
- **Baked light against live light.** The painting's fire glow does not flicker, and the live fire's light does not
  reach the painting. Without care the two lights disagree.
- **Phone memory.** Four 2048-pixel paintings are about 64 MB uncompressed on the GPU. Compressed textures bring that
  down, and the cost has to be measured on Wendell's phone, as with the chamber (`bpt-j1-frame-rate`).

**The record already rules on the painter.** `cs-chatgpt-ai-art` was answered "Concept only" on 2026-10-12: ChatGPT
art is a reference, sessions rebuild each piece, and nothing from ChatGPT ships. The post's step 4 ships a GPT painting
as the surface, and its characters are GPT pictures animated by Minimax. As described, the post's pipeline breaks
Wendell's ruling twice. The Between thread's round 3 plan ("one step to run through ChatGPT as a paint-over") is fine
as a private preview and breaks the ruling if that painting reaches the page.

**Falsification test, and the blocker it resolves.** Open blocker: nobody knows whether the projection survives the
hollow's own movement. Test: project one painted view onto the hollow and walk the camera to where a player actually
sits and turns, then 1 m off the capture camera. If the smear is visible at the cushions, the technique fails for the
Between and round 3 should not use it. The painting for this test may be a GPT preview, because it never ships. This
unlocks the round 3 decision.

**The Challenger owns the tests.** It owns the off-axis test, the seam check and the phone budget, and refuses any "it looks
like the picture" claim made from a still taken at the capture camera.

## Regent

**The Regent casts 1, Unbroken, becoming 13, Fellowship.** Everything here pushes and nothing yields; the remedy is timing, and walking
the same road as the work already under way.

**Obligations, not preferences.**
- `cs-chatgpt-ai-art` (concept only): a GPT paint-over is a reference and a preview. The painting that ships is painted
  by a person or made by our own code.
- `c3d-cc0-only` and `cs-cc0-or-own`: every shipped painting is own work and carries a manifest row with its source.
- The non-AI route is first class (bars-engine `CLAUDE.md`; ontology `equivalent_routes`). The technique has one: a
  person paints over the capture.
- Characters: Minimax-animated GPT pictures do not enter. Characters stay on the rigged models we build.
- The ontology is written with Codex (`docs/ontology-in-flows.md`). This pass writes a Codex brief and leaves
  `ontology/` alone.

**Fellowship with the asset-sources brief.** The asset-sources brief (2026-10-17) adds `asset_sourcing` with source
channels and pipeline stages. The projection paint-over is a technique inside that section, using its channels. A
separate section would be a parallel vocabulary, which that brief forbids.

**Phase gates.** The technique enters the ontology now, through the brief. Using it in a build waits for Wendell's round
2 note on the Between (the Between thread owns #366 and the try step) and for the Challenger's off-axis test.

**Definition of done for this pass.** The brief, the pass and the ledger record merged; the board carries the positions
and the one question; `term_lint.py` and the ontology validation commands pass after Codex applies the brief.

**The Regent owns provenance.** It owns the provenance rows: each painting gets an `AssetSourceRecord` naming its channel, its
painter, its camera id and the blockout commit it was captured from.

## Diplomat

**The Diplomat casts 23, Erosion, with no changing lines.** The ground is going and nobody has said so. Keep still; do not push.

**What erodes.** The Portland community around this work is wary of AI (bars-engine `CLAUDE.md`), and the Kickstarter
depends on its trust. A space whose whole visible surface was painted by GPT erodes that trust slowly, more than one
AI prop would, because the painting is everything you see.

**A painter's craft is the bridge.** Camera-projection matte painting is a craft painters already know. Taken that way, the technique is
an invitation to artists: a template (the capture, with faint outlines of the blocks) that anyone can paint by hand,
on a phone, an iPad, or on paper and scanned. A painter's name in the credits is a story the community can welcome.

**Keep still where it does not fit.** The Diplomat would not carry the technique into the caves or the Chapter 1 demo
to save effort. It fits small places with set views.

**The Diplomat owns the hand-off.** It owns the painting template and the step that hands it to whoever paints: the capture as a
file on the step card, the camera's view described in words, and how to send the painting back. The step follows
Wendell's step rules (full context, says where everything is).

## Verdicts

| Face | Add as a technique | Fits the Between | Fits the caves | GPT paint-over ships | Who owns what |
|---|---|---|---|---|---|
| Shaman | yes | yes, painted by hand | no | no | felt brief and felt check per view |
| Architect | yes | yes, runtime shader | partly, as a bake for far surfaces | no comment | camera records, projection, fallback |
| Challenger | yes, as unproven | only if the off-axis test passes | no | no, by the ruling | off-axis test, seams, phone budget |
| Regent | yes, inside `asset_sourcing` | after round 2 and the test | no | no, by the ruling | provenance rows, gates |
| Diplomat | yes | yes, painted by a person | no | no | painting template and step |

## Dissent check

The pass is not unanimous. The Architect would use a Blender bake to bring the technique to far cave surfaces; the
other four keep it out of the caves. The Shaman and the Diplomat want a hand-painted route as the plan for the Between;
the Challenger wants no plan until the off-axis test runs. All five agree a GPT painting does not ship, and that
agreement rests on Wendell's ruling, so it is a flag: if he lifts that ruling, three columns change.

## Sage

**The Sage casts 18, Stale Air, becoming 44, Serendipity.** Something spoiled through being left alone, and the repair is bracketed by
thinking about how it got there. What was left alone is the gap between the concept and the build: every round has
rebuilt the picture and accepted the gap. The one new piece of evidence is a post, and it deserves watching rather than
seizing.

**The smallest coherent whole is short.** The projection paint-over is an old matte-painting technique with a new painter. Our
record already decides the painter: a person or our own code ships, and GPT previews. So the technique enters the
ontology as stages that use the asset-sources channels, with the paint stage's allowed channels written down, and its
first use is the Between, after round 2 and the off-axis test.

**What each face gave.** Shaman: the felt brief per view, and painting as shared play. Architect: the camera record as
the contract, the five-part machine, and the bake as a third position. Challenger: the four breakpoints, the ruling
conflict, and the off-axis test. Regent: the obligations, the place inside `asset_sourcing`, and the gates. Diplomat:
the painters' template and the reason to keep it out of the caves. Dropped: nothing; the Architect's cave bake is kept
as dissent.

**Dissent carried.** The Architect's cave bake. The Shaman and Diplomat's hand-painted route against the Challenger's
"test first".

## Outputs

### Positions (stand unless Wendell flips them)

- **ppo-technique.** The projection paint-over enters the design ontology as a technique inside `asset_sourcing`,
  through a Codex brief (`docs/codex/projection-paint-over-brief.md`). It fits small places with set views, like the
  Between, and does not fit free-walking caves. Why it did not need him: he asked for it to be added; where it lives
  follows `docs/ontology-in-flows.md` and the asset-sources brief.
- **ppo-paint-channel.** A GPT paint-over is a private preview. The painting that ships on a page is painted by a person
  or made by our own code, with a manifest row naming the painter. Minimax-animated GPT characters do not enter;
  characters stay on our rigged models. Why it did not need him: his ruling `cs-chatgpt-ai-art` (concept only,
  2026-10-12), `cs-cc0-or-own`, and the first-class non-AI route.
- **ppo-offaxis-first.** No build ships the technique before the off-axis test passes on the hollow, and round 3 of the
  Between waits for his round 2 note. Why it did not need him: the Between thread's own recommendation (one change per round) and `bh-device-gate` (nothing reaches him as "try this" until it has opened on an iPhone).

### Questions (passed the reach test)

- **ppo-who-paints** (owner: Diplomat; Shaman). If round 3 of the Between uses the projection paint-over, who paints
  the four views that ship? Options: you paint them by hand (recommended); a hired artist paints them; our code paints
  them in the concept's style. The record says a person or our code ships, and holds no answer on which person, whether
  you want to paint, or money for an artist; all three are his. It changes what round 3 builds and what step he gets. It
  was not asked before because the technique reached the record today.

## Tests, dated

| Id | Face | Due | Resolves |
|---|---|---|---|
| ppo-offaxis | Challenger | when round 3 of the Between starts | whether the projection survives the hollow's own movement |
| ppo-seams | Architect | with ppo-offaxis | whether two painted views agree where they overlap |
| ppo-codex-applied | Regent | 2026-10-24 | whether Codex applied the brief and the validation commands pass |
