# The Cave of Lessons in 3D: options for the build, with no Meshy

**Run 2026-10-09**, from Wendell's board saves of 16:54 to 17:00 UTC (ledger `2026-10-09-pull-170057.json`). This
is the second pass on the 3D pipeline; the first is `6FACE_PASS_unreal-pipeline1_2026-10-08.md`.

**The ask, in his words.** On `up-game-pick` he chose the Cave of Lessons. On `up-meshy-plan` he chose no Meshy:
"Let's see if there are other meshy alternatives that can use Claude Code or Codex tokens, or my own GPU befor we
commit to this". On `up-short-sessions` he overruled: "Im happy to do this slower in a way that preserves tokens as
well. Let's get an analysis on the most deft and efficient way to do this. Doing the first draft over a week for
instance is ok. Give me some options to choose from OR find a way to integrate this into workflows we're already
doing to justify the cost. The ontology game could be a really good one for this as it already uses blender and
we're looking for a strong immersive UI experience for it". `up-gpu-by-script`, `up-repo` and `up-cost-stop` stood.

**Inputs:** pass one; the ontology game's body map in bars-engine (`content/ontology-game/body/build_figure.py`,
`body-map.js`, `scripts/build-ontology-game.mjs`); the usage audit; web research on 9 October (sources at the end).
No daemons were sent: the problems were tool lookup and cost arithmetic. `council/due.py --ahead 7` lists nothing
due.

## What the record already shows

The ontology game already has a working 3D pipeline, and it is the cheap one. `build_figure.py` builds the body-map
figure in Blender from Python (`pip install bpy`, no Blender window, no GPU), exports `figure.glb`, and commits it.
`body-map.js` loads three.js and the figure on the page, on a phone, only when the player opens it. The site build
never needs Blender. That is Blender by script, a web 3D view and a committed asset, already in play.

So the Cave of Lessons does not need Unreal to exist. It can be the ontology game's immersive view: chambers built
by the same kind of script, walked through on the same page, on the phone the game is already played on.

## Meshy alternatives (searched 9 October)

| Route | Runs on | Cost | Licence | Fit |
|---|---|---|---|---|
| Blender by script (bpy), as the body map does | a cloud thread, or Codex | tokens only | his own | cave rock, chambers, plain props, stylised figures |
| Blender MCP (ahujasid/blender-mcp) | Blender on his Mac, driven by Claude Code or Codex | free (MIT) | his own | the same, interactively; it also pulls Poly Haven and Poly Pizza assets |
| CC0 kits: Poly Haven, Kenney, Quaternius | anywhere | free | CC0, no credit needed | rock and cave textures, lighting, props, base characters |
| TRELLIS.2, Microsoft, Mac port (trellis-mac) | his Mac's GPU, Apple Silicon, about 24 GB memory or more | free | MIT | image to textured 3D model, about 3.5 minutes a model on an M4 Pro (self-reported) |
| Hunyuan3D 2 / 2.1, Tencent | his Mac, shape only | free | community licence that excludes the EU, UK and South Korea | weak: texturing usually fails on Mac; licence limits a public release |
| AssetFurnace (image-to-3dlab) | Apple Silicon or NVIDIA | free (Apache-2.0) | per model inside it | a bundle of the above with auto-rig; new, untested here |

**The council's reading:** no Meshy is needed for a first draft. Script and CC0 kits carry the cave; TRELLIS.2 on
his Mac is the own-GPU route for the few hero pieces (the daemons), and it is MIT, so the art's licence stays clean.
Image-to-3D needs a picture to start from; concept images can come from the character look he ruled on 4 October or
from the image tools in ChatGPT or Codex (inferred, not checked against his plan). Whether his Mac has the memory for
TRELLIS.2 is answered by a script (`up-gpu-by-script`), not by asking him.

## The casts

| Face | Hexagram | Shows |
|---|---|---|
| Shaman | 28 Overload, changing to 47 Drained | This is carrying more than what holds it up. |
| Architect | 47 Drained, changing to 43 Unsaid | The explaining continues and the basin is dry. |
| Challenger | 55 Fullness | This is at its peak and you are saving some of it. |
| Regent | 2 Bearing, changing to 15 Understatement | The whole weight of this is yours, unasked. |
| Diplomat | 33 Retreat, changing to 12 Stalemate | Leaving is available, and the timing decides what you keep. |
| Sage | 4 Fog, changing to 40 Thaw | You are guessing where you could ask. |

## Shaman

**Overload:** "This is carrying more than what holds it up." Unreal, Meshy and a long session were three new loads on
one first build. **What the player wants is to walk into the cave and meet a daemon,** and the ontology game is where
the player already meets one by the body and the block. The cave as that game's immersive view gives the return early
and on the phone in their hand. Unreal can come later, for a game that needs it.

## Architect

**Drained, changing to Unsaid:** "The explaining continues and the basin is dry." The basin is the token budget, and
the unsaid sentence is that the pipeline is already built. **Use the body map's pattern for the cave:** one Python
script per chamber builds a `.glb` with lighting baked in, the script and the asset are committed, and the page loads
them with the three.js it already uses. Game data names asset ids from a manifest, Sprout's rule. **The scripts are
plain Python, so Codex can run a rebuild as well as Claude** (`c3d-codex-rebuilds`). If the web path is chosen, the
cave lives beside the body map in bars-engine and `up-repo`'s new repository is not made yet.

## Challenger

**Fullness:** "This is at its peak and you are saving some of it." **What breaks the web path is the phone:** a cave
too heavy to load. The test is a size and frame budget: each chamber under about 3 MB, and the walk holds a steady
frame rate on his phone. **What breaks TRELLIS.2 is his Mac's memory;** the script reads it before anything is
installed. **Cost:** pass ten measured $0.14 a call at 679,000 tokens; a short thread of 50 to 80 calls at an
opening near 120,000 tokens is estimated at $5 to $15, so a week of seven threads is about $35 to $100, under
`up-cost-stop`'s $200 (an estimate, measured after each thread).

## Regent

**Bearing:** "The whole weight of this is yours, unasked." He offered a week; the plan uses it and asks nothing it
can answer. **The week, one thread a day** (`c3d-week`): day 1 chamber design and the manifest; day 2 chamber one and
the walk; day 3 chambers two and three; day 4 the daemon and the lesson encounter wired to the game's steps; day 5 the
budget tests and a playable link on his steps list; days 6 and 7 his play and the fixes his steers ask for. Design days
run on Opus, rebuild days on Sonnet (CLAUDE.md). **Definition of done is unchanged:** he walks three chambers and passes
one daemon by its lesson.

## Diplomat

**Retreat, changing to Stalemate:** "Leaving is available, and the timing decides what you keep." Choosing the web
path now keeps Unreal and Meshy open for later; nothing is spent that blocks them. **The bridge to the Portland
community** is the ontology game itself: a cave on the game's page plays without an account, an install or a
model in the loop, which suits a community with a strong allergy to AI.

## Sage

**Fog, changing to Thaw:** "You are guessing where you could ask." The record answered most of what looked open: the
pipeline exists, the GPU is a script, the licence is CC0 or MIT. **What is left is his preference for where the cave
lives and how it is played,** the web view or an Unreal desktop game, and that changes everything built. That one
goes to him (`c3d-path`). **Dissent:** the Shaman would put TRELLIS.2 in from day 1 for the daemons' look; the
Challenger holds it until the script has read his Mac. The pass was otherwise unanimous, and again no face tried the
tools on his machine.

## Outputs

### Positions (stand unless he flips them)

- `c3d-meshy-alternatives`: no Meshy is needed for the first draft; script and CC0 kits carry the cave, TRELLIS.2 on
  his Mac is the own-GPU route for hero pieces, Hunyuan3D is left out for its licence and its Mac texturing.
- `c3d-week`: one thread a day for a week, as above, replacing `up-short-sessions`.
- `c3d-codex-rebuilds`: asset scripts are plain Python, so rebuild days can run in Codex on his OpenAI tokens.
- `c3d-cc0-only`: the first draft uses only CC0 kit assets, script-built geometry and MIT-generated models, each
  listed with its licence in the manifest.
- `c3d-phone-budget`: each chamber stays under about 3 MB and the walk is tested on his phone before he is asked to
  play it.

### Question (passed the reach test)

- `c3d-path` (Shaman, Regent): where the Cave of Lessons is built. His preference; it changes the engine, the repo
  and who can play it. Not asked before because pass one assumed Unreal and Meshy, and his steer opened the ontology
  game as a home.

### Tests, dated

- By the end of day 2: chamber one loads under 3 MB and walks on his phone.
- By the end of the week: he has walked three chambers and passed one daemon; the week's measured cost is recorded
  beside this pass's estimate of $35 to $100.

## Sources

- [TRELLIS.2 Mac port, The Agent Times](https://theagenttimes.com/articles/trellis-2-mac-port-frees-3d-asset-generation-from-nvidia-dep-1696b24e); repo https://github.com/shivampkumar/trellis-mac
- [Hunyuan3D-2 on Mac, Codersera](https://codersera.com/blog/how-to-install-and-run-hunyuan3d-2-on-macos-a-step-by-step-guide/)
- [Hunyuan3D-2 licence](https://huggingface.co/tencent/Hunyuan3D-2/blob/main/LICENSE)
- [Blender MCP](https://github.com/ahujasid/blender-mcp)
- [AssetFurnace (image-to-3dlab)](https://github.com/Bingeljell/image-to-3dlab)
