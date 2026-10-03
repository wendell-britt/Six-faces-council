#!/usr/bin/env python3
"""Cast the I Ching for one agent or several: one hexagram each, drawn evenly from the 64.

Usage:
  python3 council/iching/cast.py shaman architect daemon-skeptic     one cast per agent named
  python3 council/iching/cast.py --json shaman                       the same, as JSON for a ledger
  python3 council/iching/cast.py --seed 7 shaman                     repeatable, for tests only

Wendell, 2026-10-03: "all agents should be casting the I Ching and using its wisdom to inform their
decisions (not unlike flirtcraft)". Flirtcraft draws one hexagram evenly from the 64 and reads it with its
two trigrams, so this does the same. Each agent gets its own cast. A face casts for the daemons it sends,
and passes each daemon its hexagram, so the daemons stay read-only.
"""
import json
import random
import secrets
import sys
from pathlib import Path

import yaml

TABLE = Path(__file__).resolve().parent / "hexagrams.yaml"


def figure(lines):
    # top line first, the way a hexagram is drawn
    return "\n".join("━━━━━━━" if x else "━━━ ━━━" for x in reversed(lines))


def cast(agents, seed=None):
    data = yaml.safe_load(TABLE.read_text())
    hexes, tri = data["hexagrams"], data["trigrams"]
    rng = random.Random(seed) if seed is not None else secrets.SystemRandom()
    out = []
    for agent in agents:
        h = hexes[rng.randrange(64)]
        lo, up = tri[h["lower"]], tri[h["upper"]]
        out.append({"agent": agent, "n": h["n"], "name": h.get("name"), "cn": h["cn"], "pinyin": h["pinyin"],
                    "lines": h["lines"], "shows": h.get("shows"), "image": h.get("image"),
                    "situation": h.get("situation"),
                    "lower": {"trigram": h["lower"], **{k: lo[k] for k in ("symbol", "name", "quality")}},
                    "upper": {"trigram": h["upper"], **{k: up[k] for k in ("symbol", "name", "quality")}}})
    return out


def main(argv):
    args = argv[1:]
    as_json = "--json" in args
    seed = None
    if "--seed" in args:
        i = args.index("--seed")
        seed = int(args[i + 1])
        del args[i:i + 2]
    agents = [a for a in args if not a.startswith("--")] or ["agent"]
    casts = cast(agents, seed)
    if as_json:
        print(json.dumps(casts, ensure_ascii=False))
        return 0
    for c in casts:
        print(f"{c['agent']}: hexagram {c['n']}, {c['name']}, {c['cn']} ({c['pinyin']})")
        print(figure(c["lines"]))
        print(f"  {c['upper']['symbol']} {c['upper']['trigram']}, {c['upper']['name']} ({c['upper']['quality']}), above")
        print(f"  {c['lower']['symbol']} {c['lower']['trigram']}, {c['lower']['name']} ({c['lower']['quality']}), below")
        print(f"  Shows: {c['shows']}\n  Image: {c['image']}\n  Situation: {c['situation']}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
