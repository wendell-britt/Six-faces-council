#!/usr/bin/env python3
"""Fetch the WAVE room runs that started on the board, into a saved store's blockers folder, so pull.py lands them.

Wendell, 2026-10-14 (board, ttv-skip-wave): "It should deposit me inside the WAVE room and we should move to have the
WAVE room be able to metabolize context specific charges and send the results to the board in this case."

The board opens the cave page with #wave=board&charge=...&ref=tap-the-vein--<time> (docs/morning.md, Tap the Vein
first). The room saves the run at every step to bars-engine (POST /api/council/wave-runs, under his own sign-in), in
the blocker panel's record shape with engine "wave-room" (docs/blocker-panel.md). This script reads them back with
COUNCIL_MENU_TOKEN, the way council/morning.py fetches the menu, and writes each one to <store>/blockers/<ref>.json
unless the store already holds that save or a newer one. board/pull.py then copies it to council/blockers/ on main and
lists it under needs work like a run from the board's own panel.

pull.py runs this itself before it looks for blockers; run it alone to check:
  python3 council/wave_runs.py <store dir>          # fetch and write into <store dir>/blockers
  python3 council/wave_runs.py <store dir> --dry    # list what would be written
"""
import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS_URL = "https://bars-engine.vercel.app/api/council/wave-runs"
REF = re.compile(r"^[a-z0-9][a-z0-9-]{0,79}$")


def _morning():
    spec = importlib.util.spec_from_file_location("morning", HERE / "morning.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def fetch(url=RUNS_URL):
    """Returns (runs, None) or (None, reason)."""
    doc, why = _morning().fetch_json(url, "/api/council/wave-runs route (the bars-engine side is not deployed yet)")
    if why:
        return None, why
    return (doc or {}).get("runs") or [], None


def place(runs, store, dry=False):
    """Write each run the store lacks, or holds an older save of, to <store>/blockers/<ref>.json. Returns the refs written."""
    out = Path(store) / "blockers"
    wrote = []
    for r in runs:
        ref, rec = r.get("ref", ""), r.get("record") or {}
        if not REF.match(ref) or rec.get("engine") != "wave-room" or not rec.get("savedAt"):
            continue
        have = out / f"{ref}.json"
        if have.exists() and json.loads(have.read_text(encoding="utf-8")).get("savedAt", "") >= rec["savedAt"]:
            continue
        wrote.append(ref)
        if not dry:
            out.mkdir(parents=True, exist_ok=True)
            have.write_text(json.dumps(rec, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return wrote


def into(store, dry=False):
    """Fetch and place. Prints one line; never stops the caller, since a missing run only waits for the next read."""
    runs, why = fetch()
    if why:
        print(f"WAVE room runs not fetched: {why}")
        return []
    wrote = place(runs, store, dry)
    print(f"WAVE room runs: {len(runs)} in bars-engine, {len(wrote)} new or newer" + (f" ({', '.join(wrote)})" if wrote else ""))
    return wrote


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("store", help="the folder the board's store was saved into")
    ap.add_argument("--dry", action="store_true", help="list what would be written")
    a = ap.parse_args(argv)
    into(a.store, a.dry)


if __name__ == "__main__":
    sys.exit(main())
