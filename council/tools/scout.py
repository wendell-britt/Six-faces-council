"""Rung 3 of the tool ladder (docs/tool-scout.md): which known tools in council/toolbox.yaml fit a job.

python3 council/tools/scout.py rig the daemon bodies
python3 council/tools/scout.py --all
Prints one line per match, best first, so the check costs a few hundred tokens.
"""
import re
import sys
from pathlib import Path

import yaml

TOOLBOX = Path(__file__).resolve().parents[1] / "toolbox.yaml"
STOP = {"the", "a", "an", "and", "or", "of", "to", "for", "in", "on", "with", "its", "each", "all", "from", "as", "at"}


def tools():
    return yaml.safe_load(TOOLBOX.read_text())["tools"]


def words(text):
    return {w.rstrip("s") for w in re.findall(r"[a-z0-9][a-z0-9.\-]+", text.lower())} - STOP


def match(job, limit=5):
    want = words(job)
    scored = []
    for t in tools():
        if t["status"] == "rejected":
            continue
        tags = {x.rstrip("s") for x in t["tags"]}
        score = 3 * len(want & tags) + len(want & words(t["does"]))
        if score:
            scored.append((score, t))
    scored.sort(key=lambda s: -s[0])
    return [t for _, t in scored[:limit]]


def line(t):
    return f"{t['id']} [{t['status']}, {t['licence'].split(';')[0]}]: {t['does']}. Where: {t['where'].split(';')[0]}"


def main(argv):
    if not argv:
        sys.exit(__doc__)
    found = tools() if argv == ["--all"] else match(" ".join(argv))
    for t in found:
        print(line(t))
    if not found:
        print("no known tool: rung 4, one Sonnet worker searches the web (docs/tool-scout.md)")


if __name__ == "__main__":
    main(sys.argv[1:])
