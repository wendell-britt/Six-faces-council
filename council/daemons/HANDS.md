# Daemon hands: how they are rigged and posed

Wendell, 2026-10-16, on the third hand sheet: "Better but controller still looks weird and the hands are still off.
Let's do some research on how to properly rig and use hands"

## What game rigs do

- **Bones.** The long-standing game hand is one hand bone plus three bones per finger, sixteen to a hand (practitioner
  convention on Polycount; VR and engine hand skeletons, such as Unigine's and Meta's OpenXR joints, add a metacarpal
  and a tip per finger). Some mobile rigs drop the last finger bone to save bones.
- **The thumb is different.** It needs its own free-turning metacarpal, set low in the palm, so it can swing across the
  palm and rest on the fingers. The ball of the thumb and the web are weighted to that bone. The other metacarpals are
  usually one stiff palm.
- **One mesh, many poses.** The hand is modelled once, open with the fingers straight and a little apart, and every
  shape (fist, point, relaxed, stop) is a pose of the bones. Nobody models a second fist mesh, because then the hand
  cannot open in animation.
- **Weights decide the look.** Most broken game hands are weight problems, not rig problems: a finger's bones blend
  over a short distance, and the sleeve must not take weight from the hand.

## Proportions from life (artists' rules of thumb)

- A hand is about a tenth of the body's height, wrist crease to middle fingertip.
- The palm is about as long as the middle finger.
- The knuckles sit on an arch; the index and ring fingers are a little shorter than the middle, the little finger about
  three quarters of it.
- A finger's three bones run about 5 : 3 : 2.5, root to tip.
- The thumb has two bones past its metacarpal, and its tip reaches about the middle of the index finger's first bone.

These are artists' rules and the sources disagree a little; they set a starting point, not a measurement.

## What the daemon rig now does

bars-engine `content/ontology-game/cave/character.py`, pull request #328:

- The wrist bone is the palm (wrist crease to the middle knuckle). Under it, five chains of three bones, the thumb's
  first one its metacarpal: 30 finger bones across both hands, 46 bones in all.
- The hand is made open and fused on its own, finer than the body, so the fingers stay apart. A hand at 1.75 m is
  0.19 m long and grows with the arm's thickness.
- `HAND_POSES` holds three poses, as a curl per finger joint and a spread: open (the stop), relaxed (hanging), fist.
  The fist lays the thumb across the front of the folded fingers. A `WARP` row names its pose in `hands`.
- The hand and the body share no vertex, so a bent wrist turns the hand at the cuff without dragging the sleeve.
- The walk does not key the fingers, so a game is free to open a fist or close a hand. That is the integration
  animation's first need: the Controller's grasp letting go.

## Sources

- [Polycount: hand bone counts and the thumb metacarpal](https://polycount.com/discussion/comment/2468009) and
  [follow-up](https://polycount.com/discussion/comment/2468027)
- [Blender Artists: rigging a low-poly hand](https://blenderartists.org/t/help-rigging-a-hand-in-2-5/477966)
- [University of Washington CSE 459: hand rig](https://courses.cs.washington.edu/courses/cse459/09wi/projects/rigging_2/hand.html)
- [Unigine VRBone hand joints](https://developer.unigine.com/docs/latest/api/library/vr/class.vrbone)
- [Meta OpenXR hand joint ids](https://developers.meta.com/horizon/reference/interaction/v77/enum_oculus_interaction_input_compatibility_open_x_r_hand_joint_id/)
- [Clip Studio tips: drawing hands](https://tips.clip-studio.com/zh-tw/articles/11101?org=1), for the proportions
