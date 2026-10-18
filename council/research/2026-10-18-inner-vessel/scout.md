# Tool scout: inner-space ship builder + small inner world

Repo facts (bars-engine package.json): no three.js, no react-three-fiber, no drei. Has pixi.js ^8.17 (2D) and @xyflow/react ^12.10 (node graphs). No "recipe"/"craft" in src; "lantern" only in avatar-parts.ts; Prisma has no player inventory model (only BacklogItem, BetweenItem). The scout.py tool returned "no known tool" for jobs 1, 2, 4; it returned off-topic matches (rigify, blender-skills) for 3 and 5.

## 1. Snap-grid modular builder
scout: 5 (rung 4 skipped, no search spent: the job is a ~150-line data model). Part = {id, footprint cells, sockets[{cell, dir, type}]}; place if a socket pairs with a compatible socket and no cell overlaps. Render with pixi.js (already a dependency) as a 2D top-down or side-on grid; no 3D needed for a first slice. Adding three/r3f only if ship parts must be seen in 3D.
Not checked: no existing builder library was searched.

## 2. Low-poly ship parts
scout: 4, Kenney Space Kit, CC0 1.0, over 150 models in OBJ/FBX/DAE/STL/glTF, includes ships and modular pieces. https://kenney-assets.itch.io/space-kit . Alternates: Kenney Space Station Kit (CC0, 80+ models) https://kenney-assets.itch.io/space-station-kit ; OpenGameArt "Modular Space Kit" (40 objects, FBX/OBJ/glTF; license not verified, check before shipping) https://opengameart.org/content/modular-space-kit . Quaternius not searched.
Note: results say glTF, not confirmed .glb; check the download. For a 2D pixi slice, render sprites from the models in Blender (blender-skills, vendored) or use Kenney's 2D Space Shooter Redux (not checked).
Add to toolbox.yaml: kenney-space-kit, status available, licence CC0.

## 3. Procedural planet / inner world
scout: 4, no MIT-verified turnkey. Candidates, licenses unverified: xenocide-world-generator (React + r3f) https://github.com/duchu-net/xenocide-world-generator ; PlanetTech (three.js, quadtree) https://github.com/InterstellarJS/PlanetTech ; Lagrange (Vue+three, biomes) https://discourse.threejs.org/t/lagrange-procedural-planet-builder-vue-js-three-js-tsl-in-progress/83453 . Recommendation: rung 5 for the slice. A planet from 3 parameters (seed, temperature, wetness) = noise heightmap + biome lookup, drawn flat in pixi (equirectangular or disc) with a small seeded noise function; no library. Take a candidate only if it is MIT/Apache after reading its LICENSE.
Not checked: licenses of the three candidates.

## 4. Recipe / crafting data
scout: 2 partial, then 5. bars-engine has no recipe table (no "recipe" or "craft" hits in src beyond UI copy). Build a typed JSON table {id, inputs[{item, qty}], outputs[], station?} plus a pure `craft(inventory, recipe)` function with a unit test. No inventory model exists, so keep player stock in a JSON column or new table; the `charge` code (charge-capture, DailyChargePanel) is the closest existing resource and is a candidate currency for the "Ember/Lantern" idea.

## 5. Travel between worlds
scout: 2, @xyflow/react ^12.10.1 is already in bars-engine (rung 2 holds). Use it for a node map: worlds as nodes, routes as edges with cost/requirement, current node highlighted. Free flight is a rung-5 build (needs a 2D/3D engine loop) and is not needed for a first slice; recommend node map first.

## Suggested stack for the first web slice
pixi.js (have) for builder + planet; @xyflow/react (have) for map; JSON recipe table (build); Kenney Space Kit (CC0) as art source, rendered to sprites. No new npm dependency required. If 3D is wanted later: three + @react-three/fiber (MIT) are the known tools, not yet in the repo.
Not checked: Sprout repo (not checked out); Quaternius; any snap-builder library.
