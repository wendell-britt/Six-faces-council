#!/usr/bin/env python3
"""Report saves left unrecorded on main for more than N hours (default 6). Exit 1 when there are any.

Two sources, same rule:
  python3 board/staleness.py                    # ask bars-engine (GET /api/board/pull?stale_hours=6), BOARD_PULL_TOKEN
  python3 board/staleness.py --store <dir>      # a saved store folder (bars-engine or the old artifact store),
                                                # judged by board/pull.py's own find_new against board_data.json

A save counts when pull.py would record it (find_new) or would hand it to a session (a pasted morning menu newer than
the last gather), and it was saved more than N hours ago. The scheduled Action runs the first form after every pull,
so a red run is the alarm (docs/failure-modes.md). Added 2026-10-16 after the 20:09 Send of 2026-10-15 stalled.
"""
import argparse
import datetime as dt
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def from_store(store, hours, now):
    pull = _load("pull", HERE / "pull.py")
    data = json.loads(pull.DATA.read_text(encoding="utf-8"))
    new, general, steps = pull.find_new(data, store)
    cutoff = (now - dt.timedelta(hours=hours)).isoformat().replace("+00:00", "Z")
    rows = [(n["doc"]["savedAt"], f"{n['kind']}/{n['id']}") for n in new]
    rows += [(general["savedAt"], "steer/general")] if general else []
    rows += [(e["at"], f"steps/{e['id']}") for e in steps]
    rows += [(b["doc"]["savedAt"], f"blockers/{b['id']}") for b in pull.find_blockers(store)]
    menu = pull.pasted_menu(data, store)
    if menu:
        rows.append((json.loads(menu.read_text())["savedAt"], "morning/menu"))
    return sorted(r for r in rows if r[0] < cutoff)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--hours", type=float, default=6)
    ap.add_argument("--store", help="a saved store folder instead of asking bars-engine")
    a = ap.parse_args()
    now = dt.datetime.now(dt.timezone.utc)
    if a.store:
        stale = from_store(Path(a.store), a.hours, now)
    else:
        fs = _load("fetch_store", HERE / "fetch_store.py")
        import os
        r = fs.call("GET", f"/api/board/pull?board={os.environ.get('BOARD', 'nonprofit')}&stale_hours={a.hours:g}")
        stale = [(s["receivedAt"], f"{s['collection']}/{s['docId']}") for s in r.get("stale") or []]
    for at, row in stale:
        print(f"{at}  {row}")
    print(f"stale saves (unrecorded for more than {a.hours:g} hours): {len(stale)}")
    sys.exit(1 if stale else 0)


if __name__ == "__main__":
    main()
