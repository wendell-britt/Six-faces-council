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


with open(os.path.join(OUT, "probe.json"), "w", encoding="utf-8") as fh:
    json.dump(results, fh, indent=1)
print("@@DONE@@ " + os.path.join(OUT, "probe.json"), flush=True)
