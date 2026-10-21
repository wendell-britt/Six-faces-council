"""The story pack check (council/story/PIPELINE.md): refuse a pack that has drifted from the registries.

python3 council/story/check.py                      # every pack under council/story/packs/
python3 council/story/check.py path/to/beats.yaml   # one pack
Prints one line per pack it passes, one line per finding, and exits 1 on any finding.

The check reads the four registries the story has to agree with: the faces (council/faces.yaml), the moves
(schema/move-table.json), the tools (council/toolbox.yaml) and the places (calrunia/world.yaml). It proves structure,
not story: a pack that passes still waits on the Challenger's reading and a playtest.
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
PACKS = ROOT / "council" / "story" / "packs"
KINDS = {"scene", "quest", "encounter", "ambient"}
NEED_KINDS = {"character", "prop", "set", "animation", "vfx", "ui", "audio"}
NEED_STATUSES = {"built", "brief", "gated", "missing"}
OUTCOMES = {"right", "partial", "wrong"}
ID = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
QUOTE_WORDS = 40


def tables():
    """The four registries, read once per run."""
    faces = yaml.safe_load((ROOT / "council" / "faces.yaml").read_text(encoding="utf-8"))["faces"]
    moves = yaml.safe_load((ROOT / "schema" / "move-table.json").read_text(encoding="utf-8"))
    tools = yaml.safe_load((ROOT / "council" / "toolbox.yaml").read_text(encoding="utf-8"))["tools"]
    world = yaml.safe_load((ROOT / "calrunia" / "world.yaml").read_text(encoding="utf-8"))
    return {
        "faces": set(faces),
        "moves": {m["id"] for m in moves["moves"]},
        "owned": {face: set(ids) for face, ids in moves["owners"]["faces"].items()},
        "tools": {t["id"]: t for t in tools},
        "places": {p["id"] for p in world["places"]},
    }


def check_pack(data, t):
    """Return the findings for one parsed pack. An empty list means it passes."""
    out = []

    def err(where, msg):
        out.append(f"{where}: {msg}")

    if not data or not isinstance(data, dict):
        return ["pack: is not a mapping"]
    if not data.get("pack"):
        err("pack", "needs a name")
    if not data.get("world"):
        err("pack", "needs a world id")
    source = data.get("source") or {}
    if not source.get("repo") or not source.get("locator"):
        err("source", "needs a repo and a locator, so a later stage knows what it came from")

    beats = data.get("beats") or []
    if not beats:
        return out + ["pack: has no beats"]
    ids = [b.get("id") for b in beats]
    if len(ids) != len(set(ids)):
        err("pack", "has a repeated beat id")
    if data.get("entry") not in ids:
        err("pack", f"entry {data.get('entry')!r} is not a beat id")

    needs_seen = {}
    for b in beats:
        where = str(b.get("id") or "beat")
        if not isinstance(b.get("id"), str) or not ID.match(b["id"]):
            err(where, "id must be lowercase kebab")
        if b.get("kind") not in KINDS:
            err(where, f"kind must be one of {sorted(KINDS)}")
        face = b.get("face")
        if face not in t["faces"]:
            err(where, f"face {face!r} is not in council/faces.yaml")
        elif face not in t["owned"]:
            err(where, f"face {face!r} owns no moves yet")
        if b.get("place") not in t["places"]:
            err(where, f"place {b.get('place')!r} is not in calrunia/world.yaml")
        if not isinstance(b.get("scene"), str) or not b["scene"].strip():
            err(where, "needs a scene line")

        cites = b.get("cites")
        if not isinstance(cites, list) or not cites or not all(isinstance(c, str) and c.strip() for c in cites):
            err(where, "needs cites: the BAR ids, manuscript locators or ledger rows behind it")

        quote = b.get("quote")
        if quote is not None:
            words = len(re.findall(r"[A-Za-z'’-]+", str(quote)))
            if words > QUOTE_WORDS:
                err(where, f"quote runs to {words} words; one line is the limit")

        move = b.get("move")
        if move is None:
            if b.get("kind") in ("quest", "encounter"):
                err(where, f"a {b.get('kind')} needs the move it teaches")
        elif move not in t["moves"]:
            err(where, f"move {move!r} is not in schema/move-table.json")
        elif face in t["owned"] and move not in t["owned"][face]:
            err(where, f"{face} does not own {move}")

        nxt = b.get("next") or []
        if not isinstance(nxt, list):
            err(where, "next must be a list of beat ids")
        else:
            for n in nxt:
                if n not in ids:
                    err(where, f"next names {n!r}, which is not a beat")

        choices = b.get("choices") or []
        if b.get("kind") == "encounter" and not choices:
            err(where, "an encounter needs its choices")
        if choices:
            got = [c.get("outcome") for c in choices]
            for o in OUTCOMES - set(got):
                err(where, f"choices are missing a {o} line: three outcomes, never two")
            for c in choices:
                if not isinstance(c.get("line"), str) or not c["line"].strip():
                    err(where, "a choice needs its line")

        for need in b.get("needs") or []:
            nid = str(need.get("id") or "need")
            nwhere = f"{where}/{nid}"
            if not isinstance(need.get("id"), str) or not ID.match(need["id"]):
                err(nwhere, "id must be lowercase kebab")
            elif need["id"] in needs_seen:
                err(nwhere, f"asset id already used on beat {needs_seen[need['id']]}")
            else:
                needs_seen[need["id"]] = where
            if need.get("kind") not in NEED_KINDS:
                err(nwhere, f"kind must be one of {sorted(NEED_KINDS)}")
            if not isinstance(need.get("brief"), str) or len(need["brief"].strip()) < 8:
                err(nwhere, "needs a brief the art side can start from")
            status = need.get("status")
            if status not in NEED_STATUSES:
                err(nwhere, f"status must be one of {sorted(NEED_STATUSES)}")
            tool = need.get("tool")
            if tool == "brief":
                pass
            elif tool not in t["tools"]:
                err(nwhere, f"tool {tool!r} is not in council/toolbox.yaml and is not 'brief'")
            elif t["tools"][tool]["status"] == "rejected":
                err(nwhere, f"tool {tool!r} is rejected in the toolbox")
            elif t["tools"][tool]["status"] == "gated" and status != "gated":
                err(nwhere, f"tool {tool!r} is gated, so this need is a board step: status must be 'gated'")
            if status == "built" and not need.get("ref"):
                err(nwhere, "a built need names its ref")

    # every beat reachable from the entry, so no scene sits on a branch nobody walks
    adjacency = {b.get("id"): list(b.get("next") or []) for b in beats}
    seen, stack = set(), [data.get("entry")]
    while stack:
        here = stack.pop()
        if here in seen or here not in adjacency:
            continue
        seen.add(here)
        stack.extend(adjacency[here])
    for b in beats:
        if b.get("id") not in seen:
            err(str(b.get("id")), "no route from the pack's entry")
    return out


def shown(path):
    """A pack's name in the report, relative to the repo when it sits inside it."""
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def summary(data):
    beats = data.get("beats") or []
    needs = [n for b in beats for n in (b.get("needs") or [])]
    gated = sum(1 for n in needs if n.get("status") == "gated")
    line = f"ok {data.get('pack')}: {len(beats)} beats, {len(needs)} assets"
    return line + (f", {gated} waiting on a board step" if gated else "")


def main(argv):
    paths = [Path(p) for p in argv] or sorted(PACKS.glob("*/**/beats.yaml"))
    if not paths:
        print("no packs yet: the first is Chapter 1 at council/story/packs/calrunia/chapter1/beats.yaml")
        return 0
    t = tables()
    bad = 0
    for path in paths:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        findings = check_pack(data, t)
        if findings:
            bad += 1
            print(f"FAIL {shown(path)}")
            for f in findings:
                print(f"  {f}")
        else:
            print(summary(data))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
