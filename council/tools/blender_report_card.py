import subprocess, json, sys, pathlib, re, os
BE = pathlib.Path("/home/user/bars-engine")
PY = "/home/user/blenv/bin/python"
glbs = subprocess.check_output(["git","-C",str(BE),"ls-files"],text=True).split("\n")
glbs = [g for g in glbs if g.endswith(".glb")]
probe = "import bpy,sys;bpy.ops.wm.read_factory_settings(use_empty=True);bpy.ops.import_scene.gltf(filepath=sys.argv[1]);print('@@A@@'+json.dumps([o.name for o in bpy.data.objects if o.type=='ARMATURE']))".replace("import bpy","import json,bpy")
def run(args):
    p = subprocess.run([PY, str(BE/"tools/blender-cloud/skill_run.py")]+args, capture_output=True, text=True, cwd=BE, timeout=600)
    m = re.findall(r"@@JSON@@(.*)", p.stdout)
    try: return json.loads(m[-1]), p.returncode
    except Exception: return {"error": (p.stderr or p.stdout)[-400:]}, p.returncode
out = []
for g in glbs:
    path = str(BE/g); r = {"glb": g, "kb": round(os.path.getsize(path)/1024)}
    r["qa"], r["qa_rc"] = run(["blender-asset-qa/qa_check.py","--glb",path,"--","--profile","game"])
    r["stats"], r["stats_rc"] = run(["blender-game-optimization/mesh_stats.py","--glb",path,"--","--budget","web"])
    a = subprocess.run([PY,"-c",probe,path],capture_output=True,text=True).stdout
    arms = json.loads(re.findall(r"@@A@@(.*)",a)[-1]) if "@@A@@" in a else []
    r["armatures"] = arms
    if arms: r["rig"], r["rig_rc"] = run(["blender-character-rigging/rig_check.py","--glb",path,"--","--armature",arms[0]])
    out.append(r); print(g, flush=True)
    json.dump(out, open("card.json","w"), indent=1)
open("DONE","w").write("ok")
