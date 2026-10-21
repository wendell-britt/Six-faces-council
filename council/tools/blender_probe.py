"""What this Blender can do, printed as @@STEP@@ lines. Run it through council/tools/blender_here.py.

Each step is independent and records its own seconds, so one failure (an engine that needs a GPU, say) does not stop
the rest. Steps are the ones the council's asset work actually needs: a scene from script, a Cycles still, a glTF
export, a Rigify rig, and a cloth bake.

  blender -b --factory-startup -P council/tools/blender_probe.py
"""
import json
import os
import time
import traceback

import bpy

OUT = os.environ.get("PROBE_OUT", "/tmp/blender-probe")
os.makedirs(OUT, exist_ok=True)
results = {}


def step(name):
    def wrap(fn):
        started = time.time()
        try:
            results[name] = {"ok": True, "seconds": round(time.time() - started, 1), "detail": fn()}
        except Exception:  # a probe records the failure and carries on
            results[name] = {"ok": False, "seconds": round(time.time() - started, 1),
                             "detail": traceback.format_exc(limit=4)[-600:]}
        print("@@STEP@@ " + json.dumps({name: results[name]}), flush=True)
        return fn

    return wrap


@step("version")
def _version():
    return {"blender": bpy.app.version_string}


@step("scene")
def _scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scn = bpy.context.scene
    bpy.ops.mesh.primitive_plane_add(size=20)
    ground = bpy.context.object
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 1))
    cube = bpy.context.object
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1.2, location=(2.4, 0.6, 1.2), segments=32, ring_count=16)
    ball = bpy.context.object
    mat = bpy.data.materials.new("probe")
    mat.diffuse_color = (0.2, 0.5, 0.7, 1)
    cube.data.materials.append(mat)
    bpy.ops.object.light_add(type="AREA", location=(4, -4, 6))
    bpy.context.object.data.energy = 1200
    bpy.context.object.data.size = 6
    bpy.ops.object.camera_add(location=(6, -6, 4.2))
    cam = bpy.context.object
    cam.rotation_euler = (1.15, 0, 0.78)
    scn.camera = cam
    scn.render.resolution_x, scn.render.resolution_y = 480, 270
    scn.render.image_settings.file_format = "PNG"
    return {"objects": len(bpy.data.objects), "faces": sum(len(o.data.polygons) for o in (ground, cube, ball))}


@step("cycles_480p_32spp")
def _cycles():
    scn = bpy.context.scene
    scn.render.engine = "CYCLES"
    scn.cycles.device = "CPU"
    scn.cycles.samples = 32
    scn.cycles.use_denoising = True
    scn.render.filepath = os.path.join(OUT, "cycles.png")
    started = time.time()
    bpy.ops.render.render(write_still=True)
    return {"render_seconds": round(time.time() - started, 1),
            "png_kb": round(os.path.getsize(scn.render.filepath) / 1024)}


@step("gltf_export")
def _gltf():
    path = os.path.join(OUT, "probe.glb")
    bpy.ops.export_scene.gltf(filepath=path, export_format="GLB", export_apply=True)
    return {"glb_kb": round(os.path.getsize(path) / 1024)}


@step("rigify")
def _rigify():
    bpy.ops.wm.read_factory_settings(use_empty=True)  # enable after the reset, or the add-on goes with it
    bpy.ops.preferences.addon_enable(module="rigify")
    bpy.ops.object.armature_human_metarig_add()
    metarig_bones = len(bpy.context.object.data.bones)
    started = time.time()
    bpy.ops.pose.rigify_generate()
    rig = bpy.context.object
    path = os.path.join(OUT, "rig.glb")
    bpy.ops.export_scene.gltf(filepath=path, export_format="GLB")
    return {"metarig_bones": metarig_bones, "rig_bones": len(rig.data.bones),
            "generate_seconds": round(time.time() - started, 1), "rig_glb_kb": round(os.path.getsize(path) / 1024)}


@step("cloth_sim")
def _cloth():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.mesh.primitive_grid_add(x_subdivisions=20, y_subdivisions=20, size=3, location=(0, 0, 4))
    cloth = bpy.context.object
    cloth.modifiers.new("Cloth", "CLOTH").settings.quality = 5
    scn = bpy.context.scene
    started = time.time()
    first = last = 0.0
    count = 0
    for frame in range(1, 31):
        scn.frame_set(frame)
        # the depsgraph has to be asked for inside the loop, or the bake stays at the rest shape
        depsgraph = bpy.context.evaluated_depsgraph_get()
        heights = [v.co.z for v in cloth.evaluated_get(depsgraph).data.vertices]
        count = len(heights)
        if frame == 1:
            first = min(heights)  # frame 1 is the rest shape, so this is the reference height
        last = min(heights)
    # a sheet falling flat keeps its spread, so the drop is measured against where it started
    return {"sim_seconds": round(time.time() - started, 1), "verts": count, "fall_m": round(first - last, 2)}


@step("garment_job")
def _garment():
    """One job shaped like the council's J5 rounds: a figure, a garment skinned to it, cloth, an export.

    The single-step probes above each prove one primitive. This one proves the composition, and records peak memory,
    which is the number that decides whether a real garment job fits on this box.
    """
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scn = bpy.context.scene

    def cylinder(radius, depth, x, z):
        bpy.ops.mesh.primitive_cylinder_add(radius=radius, depth=depth, location=(x, 0, z))
        return bpy.context.object

    torso = cylinder(0.20, 0.75, 0.0, 1.15)
    head = cylinder(0.12, 0.24, 0.0, 1.66)
    arm = cylinder(0.06, 0.62, 0.28, 1.30)
    arm.rotation_euler = (0, 0.35, 0)

    # a two-bone rig, so the garment is skinned to something the way a J4 figure's robe is
    bpy.ops.object.armature_add(location=(0, 0, 0.8))
    rig = bpy.context.object
    bpy.ops.object.mode_set(mode="EDIT")
    spine = rig.data.edit_bones[0]
    spine.name = "spine"
    spine.tail = (0, 0, 1.45)
    arm_bone = rig.data.edit_bones.new("arm")
    arm_bone.head, arm_bone.tail = (0.16, 0, 1.45), (0.45, 0, 1.30)
    bpy.ops.object.mode_set(mode="OBJECT")

    # auto weights need the meshes selected and the armature active
    for mesh in (torso, head, arm):
        mesh.select_set(True)
    bpy.context.view_layer.objects.active = rig
    bpy.ops.object.parent_set(type="ARMATURE_AUTO")
    skinned_verts = sum(len(m.data.vertices) for m in (torso, head, arm))
    groups = len(torso.vertex_groups)

    # the garment: a robe front hanging off the shoulders, colliding with the body
    torso.modifiers.new("Collision", "COLLISION")
    bpy.ops.mesh.primitive_grid_add(x_subdivisions=24, y_subdivisions=24, size=1.0, location=(0, -0.21, 1.05))
    robe = bpy.context.object
    # stand the panel up as a front and tilt the hem 14 degrees out, so it has somewhere to swing from: a pinned,
    # inextensible panel that starts hanging straight measures the same whether the solver ran or stalled
    robe.rotation_euler = (1.3208, 0, 0)
    robe.modifiers.new("Solidify", "SOLIDIFY").thickness = 0.01
    # pin the top row, the way a robe hangs off the shoulders: the panel then settles instead of sliding off
    pin = robe.vertex_groups.new(name="pin")
    # the panel is rotated 90 degrees about X, so its local y is the world's height
    pin.add([v.index for v in robe.data.vertices if v.co.y > 0.49], 1.0, "REPLACE")
    cloth = robe.modifiers.new("Cloth", "CLOTH")
    cloth.settings.quality = 5
    cloth.settings.vertex_group_mass = "pin"
    robe_verts = len(robe.data.vertices)

    started = time.time()
    mid = end = 0.0
    through = 0
    # the robe's evaluated mesh is in its own local space, so both readings go through matrix_world:
    # a local-space reading of a rotated panel measures nothing that happens on screen
    for frame in range(1, 25):
        scn.frame_set(frame)
        depsgraph = bpy.context.evaluated_depsgraph_get()
        world = robe.matrix_world
        points = [world @ v.co for v in robe.evaluated_get(depsgraph).data.vertices]
        lo = min(p.z for p in points)
        if frame == 12:
            mid = lo
        end = lo
        # the check the J5 rounds carry: no garment point inside the body
        through = sum(1 for p in points if (p.x ** 2 + p.y ** 2) ** 0.5 < 0.20 and abs(p.z - 1.15) < 0.375)

    bpy.ops.object.select_all(action="SELECT")
    path = os.path.join(OUT, "garment.glb")
    bpy.ops.export_scene.gltf(filepath=path, export_format="GLB", export_apply=True)

    # peak RSS of this whole process, in MB: the box has 3 GB, and one render already took 1.13 GB
    import resource
    peak_mb = round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)
    # how far the hem still moves between the middle and the end of the sim: 0 means it hangs,
    # and a large number means 24 keys is too short for this panel
    return {"seconds": round(time.time() - started, 1), "skinned_verts": skinned_verts, "weight_groups": groups,
            "robe_verts": robe_verts, "settle_mm": round(abs(mid - end) * 1000), "through_verts": through,
            "glb_kb": round(os.path.getsize(path) / 1024), "peak_rss_mb": peak_mb}


with open(os.path.join(OUT, "probe.json"), "w", encoding="utf-8") as fh:
    json.dump(results, fh, indent=1)
print("@@DONE@@ " + os.path.join(OUT, "probe.json"), flush=True)
