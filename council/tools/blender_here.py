"""Blender in a Freebuff cloud VM that has no root: install it into a folder, then measure it.

The bars-engine pipeline runs Blender headless in a container with a GPU. This VM is 2 vCPU, 3 GB of RAM and no GPU,
so it needs its own measure before asset work is planned on it. docs/blender-here.md carries the numbers from
2026-10-21 and what they mean.

  python3 council/tools/blender_here.py setup    # Blender, the system libs it needs, and the skill scripts
  python3 council/tools/blender_here.py env      # the environment lines to export in a later shell
  python3 council/tools/blender_here.py probe    # run the probe and the upstream skill tests, print the numbers

setup needs no root: Ubuntu's missing libraries are downloaded and unpacked into ROOT/sysroot and reached through
LD_LIBRARY_PATH. Everything lives under ROOT (BLENDER_HERE_ROOT, default ~/blender-here), never in the repo.
"""
import argparse
import gzip
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import time
import urllib.request
from pathlib import Path

ROOT = Path(os.environ.get("BLENDER_HERE_ROOT", Path.home() / "blender-here"))
HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
BLENDER_VERSION = "5.2.2"          # the version the council's skills are built for (they say Blender 5.2 LTS+)
BLENDER_MAJOR_MINOR = ".".join(BLENDER_VERSION.split(".")[:2])
SKILLS_REPO = "https://github.com/EL4CTEO/blender-skills"
MIRROR = "http://archive.ubuntu.com/ubuntu"
SUITES = ("noble", "noble-updates")
COMPONENTS = ("main", "universe")

# library file -> Ubuntu package that ships it. Blender links X and GL at startup even in --background.
LIBS = {
    "libXrender.so.1": "libxrender1",
    "libXfixes.so.3": "libxfixes3",
    "libXi.so.6": "libxi6",
    "libxkbcommon.so.0": "libxkbcommon0",
    "libSM.so.6": "libsm6",
    "libICE.so.6": "libice6",
    "libX11.so.6": "libx11-6",
    "libXext.so.6": "libxext6",
    "libXau.so.6": "libxau6",
    "libXdmcp.so.6": "libxdmcp6",
    "libxcb.so.1": "libxcb1",
    "libXxf86vm.so.1": "libxxf86vm1",
    "libXrandr.so.2": "libxrandr2",
    "libXinerama.so.1": "libxinerama1",
    "libXcursor.so.1": "libxcursor1",
    "libGL.so.1": "libgl1",
    "libEGL.so.1": "libegl1",
    "libgbm.so.1": "libgbm1",
    "libGLU.so.1": "libglu1-mesa",
    "libz.so.1": "zlib1g",
    "libtbb.so.12": "libtbb12",
    "libasound.so.2": "libasound2t64",
    "libpulse.so.0": "libpulse0",
    "libfontconfig.so.1": "libfontconfig1",
    "libfreetype.so.6": "libfreetype6",
}

BLENDER = ROOT / f"blender-{BLENDER_VERSION}-linux-x64" / "blender"
SYSROOT = ROOT / "sysroot"
SKILLS = ROOT / "skills"
SKILLS_TESTS = SKILLS / "tests" / "run_all.py"


def say(msg):
    print(msg, flush=True)


def env_lines():
    libs = SYSROOT / "usr" / "lib" / "x86_64-linux-gnu"
    return {"LD_LIBRARY_PATH": str(libs),
            "BAS_SKIP_GPU": "1",
            "BLENDER_HERE_ROOT": str(ROOT),
            "PROBE_OUT": str(ROOT / "probe")}


def blender_env():
    env = dict(os.environ)
    env.update(env_lines())
    return env


def fetch(url, dest, label=""):
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    started = time.time()
    if shutil.which("curl"):  # urllib stalled on archive.ubuntu.com; curl is on every image that has git
        result = subprocess.run(["curl", "-sSL", "--fail", "--max-time", "600", "-o", str(dest), url])
        if result.returncode:
            raise RuntimeError(f"curl exited {result.returncode} on {url}")
    else:
        request = urllib.request.Request(url, headers={"User-Agent": "blender-here/1"})
        with urllib.request.urlopen(request, timeout=120) as response, open(dest, "wb") as fh:
            shutil.copyfileobj(response, fh, length=1 << 20)
    mb = dest.stat().st_size / (1 << 20)
    say(f"  {label or dest.name}: {mb:.0f} MB in {time.time() - started:.0f}s")
    if mb < 0.01:
        raise SystemExit(f"{url} came back as an empty file")


def ensure_blender():
    if BLENDER.exists():
        say(f"blender: {BLENDER} already unpacked")
        return
    free_gb = shutil.disk_usage(ROOT if ROOT.exists() else ROOT.parent).free / (1 << 30)
    if free_gb < 4:
        raise SystemExit(f"need about 3 GB free for Blender and its libs, this disk has {free_gb:.1f} GB")
    url = (f"https://download.blender.org/release/Blender{BLENDER_MAJOR_MINOR}/"
           f"blender-{BLENDER_VERSION}-linux-x64.tar.xz")
    archive = ROOT / f"blender-{BLENDER_VERSION}.tar.xz"
    ROOT.mkdir(parents=True, exist_ok=True)
    say(f"blender: downloading {BLENDER_VERSION} LTS")
    fetch(url, archive)
    say("blender: unpacking")
    with tarfile.open(archive) as tar:
        tar.extractall(ROOT)
    archive.unlink()
    if not BLENDER.exists():
        raise SystemExit(f"unpacked, but {BLENDER} is not there")


def missing_libs():
    """The shared libraries ldd says the binary cannot find, in the order it lists them."""
    probe = [str(BLENDER), "--version"]
    out = subprocess.run(["ldd", *probe], capture_output=True, text=True,
                         env={"LD_LIBRARY_PATH": str(SYSROOT / "usr" / "lib" / "x86_64-linux-gnu"),
                              "PATH": os.environ.get("PATH", "")})
    text = out.stdout + out.stderr
    if "not a dynamic executable" in text:
        return []
    return re.findall(r"^\s*(\S+) => not found", text, re.M)


def package_index():
    cache = ROOT / "packages.txt"
    if cache.exists():
        return {line.split()[0]: line.split()[1] for line in cache.read_text().splitlines() if line.strip()}
    say("libs: reading Ubuntu's package lists")
    index = {}
    for suite in SUITES:
        for component in COMPONENTS:
            url = f"{MIRROR}/dists/{suite}/{component}/binary-amd64/Packages.gz"
            raw = ROOT / f"{suite}-{component}.gz"
            try:
                fetch(url, raw, label=f"{suite}/{component}")
            except Exception as exc:  # noqa: BLE001 - a missing component is not fatal
                say(f"  {suite}/{component} unavailable ({exc})")
                continue
            text = gzip.open(raw, "rt", errors="replace").read()
            for block in text.split("\n\n"):
                name = re.search(r"^Package: (\S+)$", block, re.M)
                path = re.search(r"^Filename: (\S+)$", block, re.M)
                if name and path:
                    index[name.group(1)] = path.group(1)
            raw.unlink()
    cache.write_text("\n".join(f"{k} {v}" for k, v in sorted(index.items())))
    return index


def ensure_libs():
    missing = missing_libs()
    if not missing:
        say("libs: nothing missing")
        return
    say(f"libs: {len(missing)} missing ({', '.join(missing)})")
    index = package_index()
    unknown = [lib for lib in missing if lib not in LIBS]
    if unknown:
        raise SystemExit(f"no Ubuntu package known for {unknown}; add it to LIBS in {Path(__file__).name}")
    for lib in missing:
        package = LIBS[lib]
        path = index.get(package)
        if not path:
            raise SystemExit(f"{package} is in none of the package lists; check the Ubuntu release name")
        deb = ROOT / Path(path).name
        fetch(f"{MIRROR}/{path}", deb, label=package)
        subprocess.run(["dpkg-deb", "-x", str(deb), str(SYSROOT)], check=True)
        deb.unlink()
    still = missing_libs()
    if still:
        raise SystemExit(f"still missing after unpacking: {still}")
    say("libs: all found")


def ensure_skills():
    if SKILLS_TESTS.exists():
        say(f"skills: {SKILLS} already cloned")
        return
    say("skills: cloning blender-skills")
    subprocess.run(["git", "clone", "-q", "--depth", "1", SKILLS_REPO, str(SKILLS)], check=True)
    say(f"skills: {sum(1 for _ in (SKILLS / 'skills').iterdir())} skills")


def setup():
    ensure_blender()
    if not shutil.which("dpkg-deb"):
        raise SystemExit("dpkg-deb is needed to unpack the Ubuntu libraries")
    ensure_libs()
    ensure_skills()
    say("")
    say("ready. In this shell:")
    for key, value in env_lines().items():
        say(f"  export {key}={value}")
    say(f"  {BLENDER} --version")
    say("then: python3 council/tools/blender_here.py probe")


def run_probe():
    if not BLENDER.exists():
        say(json.dumps({"ok": False, "why": f"{BLENDER} is not installed; run setup"}))
        return 2
    probe_script = HERE / "blender_probe.py"
    result = subprocess.run([str(BLENDER), "-b", "--factory-startup", "-P", str(probe_script)],
                            capture_output=True, text=True, env=blender_env(), timeout=900)
    steps = {}
    for line in result.stdout.splitlines():
        if line.startswith("@@STEP@@ "):
            try:
                steps.update(json.loads(line[len("@@STEP@@ "):]))
            except json.JSONDecodeError:
                continue
    if not steps:
        say(json.dumps({"ok": False, "why": "the probe printed no steps",
                        "stderr": (result.stderr or result.stdout)[-800:]}, indent=1))
        return 1

    skills = None
    if SKILLS_TESTS.exists():
        tests = subprocess.run([str(BLENDER), "-b", "--factory-startup", "--python-exit-code", "1",
                                "-P", str(SKILLS_TESTS)], capture_output=True, text=True,
                               env=blender_env(), timeout=1200)
        # Blender prints export timings after the summary line, so search the whole output
        match = re.search(r"(\d+) passed, (\d+) failed, (\d+) skipped", tests.stdout)
        skills = ({"passed": int(match.group(1)), "failed": int(match.group(2)), "skipped": int(match.group(3)),
                   "exit": tests.returncode} if match
                  else {"error": (tests.stderr or tests.stdout)[-600:], "exit": tests.returncode})
    report = {"ok": all(s["ok"] for s in steps.values()), "steps": steps, "skill_tests": skills}
    (ROOT / "measure.json").write_text(json.dumps(report, indent=1))
    say(json.dumps(report, indent=1))
    return 0 if report["ok"] else 1


def main():
    ap = argparse.ArgumentParser(description="Blender in a rootless cloud VM: setup, env, probe.")
    ap.add_argument("command", choices=("setup", "env", "probe"))
    args = ap.parse_args()
    if args.command == "setup":
        setup()
        return 0
    if args.command == "env":
        for key, value in env_lines().items():
            say(f"export {key}={value}")
        return 0
    return run_probe()


if __name__ == "__main__":
    sys.exit(main())
