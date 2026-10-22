# 3D math rules for our builds

From a read of *3D Math Primer for Graphics and Game Development* (https://gamemath.com/book/) against our code on
2026-10-21. The learnings page is https://claude.ai/artifact/SDpTCr4QGo99NsTWr9suv4. Each rule names the chapter it
comes from and where our code stands.

## Rules

1. **Rotations are quaternions.** Store and blend rotations as quaternions (slerp, flip the sign when the dot product
   is negative). Euler is for authoring and single-axis yaw through `wrapAng` only. Import BVH with
   `rotate_mode='QUATERNION'`, or sample whole source frames and slerp between them; never sample Euler curves at
   subframes. (Ch. 8.3.4, 8.5.12.) Today: `retarget.py` imports `NATIVE` Euler and samples subframes; `cave.js`
   already slerps.
2. **Direction is not roll.** Matching a bone's +Y fixes two of three degrees of freedom. Every retarget round prints the
   per-bone roll residual (target X against source X after the swing) next to the ankle path and fails past about 10
   degrees. (Ch. 8.1, 8.7.)
3. **Spread twist across split bones.** Linear blend skinning collapses skin at a joint that takes all the twist. Split
   the hand's twist relative to the forearm (swing-twist) and give half to the lower forearm segment. (Ch. 10.8, 8.5.11.)
   Today: `retarget.py` line 57 gives unmapped bones their rest pose, so the cuff joint takes the whole wrist turn; a
   likely, unproven contributor to the hand passing through the J5 sleeve.
4. **Smoothing is frame-rate independent.** Use `1 - Math.exp(-k*dt)` (one shared `damp(k, dt)`) or a spring tuned by
   frequency and damping ratio, never `Math.min(1, k*dt)`. (Ch. 12.2.3.) Today: both forms appear in `cave.js` and
   `walk-room.js`.
5. **Cloth runs in fixed substeps.** Step cloth and springs at a fixed 1/240 s with an accumulator (Verlet or
   position-based), and apply colliders such as the backstop as a position push to the surface after each substep,
   not as a force. For a capsule, take the closest point on the bone segment and push out by the radius. (Ch. 12.6.3,
   App. A.2, A.4.)
6. **Frame to the narrower angle.** three.js `fov` is vertical. Fit the camera with
   `hfov = 2*atan(tan(vfov/2)*aspect)` and `d = r / sin(min(vfov, hfov)/2)` from the figure's bounding sphere, through
   one `frameSphere(camera, center, r)` helper, instead of per-orientation hand-tuned FOVs. (Ch. 10.2.4.)
7. **Apply scale before export.** Skinning normals assume no non-uniform scale on bones; apply scale on rigs before GLB
   export. (Ch. 6.3.3, 10.8.)

8. **Hide what clothes cover; drive the cloth from the body.** This is the standing rule for every garment round, J5
   included (Wendell, 2026-10-22: "legs are moving through the robe... what would a professional in the field say").
   Games do not try to make cloth never touch the body. They make poke-through impossible to see:
   - **Hidden-surface removal.** Body triangles under a garment are not drawn (a per-garment body mask, or a body mesh
     cut per outfit). Keep a band of about 12 cm above a hem drawn, because a leg swinging out under the hem must not
     show a hole.
   - **Skin long garments to the legs.** A skirt or robe below the waist follows the thighs and shins, through blended
     leg weights, a few skirt bones, or capsule pushes off thigh and shin (rule 5's push, with a soft margin of a few cm).
     Free cloth near the legs is the last resort, not the default.
   - **Any sim that stays** gets leg capsule colliders sized to the outermost layer (skin plus pants), not the bare body.
   - **Measure with rays, not nearest points.** A probe that skips body points more than a few cm from the cloth never
     sees a leg that is well through. Cast a ray out from each body point and count the ones with no cloth in front.
   (Industry practice: UE and Unity outfit systems hide the body under clothing, and game skirts are skinned or bone
   driven.) Today: Sprout's creator figure does both (sprout #72, `tools/figure-legs-probe.mjs`). Round-5 coat legs
   showing: 197 point-frames before, 0 after, on four body builds and all three cuts.

## Not checked

The cloth and backstop code itself, how the cuff is weighted, rendered output, and Sprout.
