"""council/tools/blender_here.py: the install and probe driver for a rootless cloud VM.

The probe itself needs a Blender and takes about forty seconds, so these tests check the parts that keep the driver
and the doc honest instead. Run the probe by hand with `python3 council/tools/blender_here.py probe`.
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRIVER = ROOT / "council" / "tools" / "blender_here.py"
PROBE = ROOT / "council" / "tools" / "blender_probe.py"
DOC = ROOT / "docs" / "blender-here.md"

sys.path.insert(0, str(DRIVER.parent))
import blender_here  # noqa: E402

STEPS = ["version", "scene", "cycles_480p_32spp", "gltf_export", "rigify", "cloth_sim", "garment_job"]


def test_the_pin_matches_what_the_doc_promises():
    assert blender_here.BLENDER_VERSION in DOC.read_text(encoding="utf-8")
    assert blender_here.BLENDER.parent.name == f"blender-{blender_here.BLENDER_VERSION}-linux-x64"


def test_every_probe_step_has_a_line_in_the_report():
    doc = DOC.read_text(encoding="utf-8")
    assert re.findall(r'@step\("(\w+)"\)', PROBE.read_text(encoding="utf-8")) == STEPS
    for row in ("Cycles still, 480x270", "Rigify", "Auto-skin", "Cloth bake", "Asset QA", "glTF export",
                "Composed garment job"):
        assert row in doc, row
    assert "EEVEE" in doc and "does not work" in doc


def test_env_names_are_what_a_later_shell_exports():
    lines = blender_here.env_lines()
    assert set(lines) == {"LD_LIBRARY_PATH", "BAS_SKIP_GPU", "BLENDER_HERE_ROOT", "PROBE_OUT"}
    assert lines["LD_LIBRARY_PATH"].endswith("sysroot/usr/lib/x86_64-linux-gnu")


def test_probe_says_what_is_missing_instead_of_crashing(tmp_path):
    env = dict(os.environ, BLENDER_HERE_ROOT=str(tmp_path / "nowhere"))
    run = subprocess.run([sys.executable, str(DRIVER), "probe"], capture_output=True, text=True, env=env)
    assert run.returncode == 2
    report = json.loads(run.stdout.strip())
    assert report["ok"] is False
    assert "run setup" in report["why"]


def test_env_command_prints_exports():
    run = subprocess.run([sys.executable, str(DRIVER), "env"], capture_output=True, text=True)
    assert run.returncode == 0
    assert run.stdout.count("export ") == 4
