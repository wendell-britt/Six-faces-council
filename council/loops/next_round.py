#!/usr/bin/env python3
"""Next-round contracts: which loop round may start itself now (docs/loops.md).

  python3 council/loops/next_round.py                      say, per strand, what may start
  python3 council/loops/next_round.py start  STRAND N      round N is running
  python3 council/loops/next_round.py finish STRAND N      round N is done; the next queued round moves up
  python3 council/loops/next_round.py look   STRAND N --verdict keep-going|redirect|stop --words "..." [--render PATH] [--at ISO]
                                                           record his look at round N and its label
A round starts itself only when its gate is "auto", no round of the strand is running, and it is at most
max_ahead rounds past his last look.
"""
import argparse, datetime, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent


def load(strand):
    p = HERE / f"{strand}.json"
    if not p.exists():
        sys.exit(f"no contract {p}")
    return p, json.loads(p.read_text())


def save(p, c):
    p.write_text(json.dumps(c, indent=2, ensure_ascii=False) + "\n")


def profiles():
    """Load profile names from ontology/manifest.yaml, read without a YAML dependency."""
    text = (HERE.parents[1] / "ontology/manifest.yaml").read_text()
    block = text.split("load_profiles:", 1)[1].split("\n\n", 1)[0]
    return {l.strip()[:-1] for l in block.splitlines() if l.startswith("  ") and not l.startswith("   ") and l.strip().endswith(":")}


def find(c, n):
    for r in c["rounds"]:
        if r["round"] == n:
            return r
    sys.exit(f"{c['strand']}: no round {n}")


def verdict(c):
    """(round or None, reason)."""
    if any(r["status"] == "running" for r in c["rounds"]):
        run = next(r for r in c["rounds"] if r["status"] == "running")
        return None, f"round {run['round']} is running"
    nxt = next((r for r in c["rounds"] if r["status"] == "next"), None)
    if not nxt:
        return None, "no next round in the contract"
    if nxt.get("gate") != "auto":
        return None, f"round {nxt['round']} needs {nxt.get('gate')}"
    ahead = nxt["round"] - c["last_look"]["round"]
    if ahead > c.get("max_ahead", 2):
        return None, f"round {nxt['round']} is {ahead} rounds past his last look (round {c['last_look']['round']}); waits for his look"
    return nxt, f"round {nxt['round']} may start: {nxt['builds']}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", nargs="?", choices=["status", "start", "finish", "look"], default="status")
    ap.add_argument("strand", nargs="?")
    ap.add_argument("round", nargs="?", type=int)
    ap.add_argument("--verdict", choices=["keep-going", "redirect", "stop"])
    ap.add_argument("--words")
    ap.add_argument("--render")
    ap.add_argument("--at")
    ap.add_argument("--delivered", action="store_true", help="finish: every_round deliverables are on the page")
    a = ap.parse_args()

    if a.cmd == "status":
        for p in sorted(HERE.glob("*.json")):
            c = json.loads(p.read_text())
            if a.strand and c["strand"] != a.strand:
                continue
            print(f"{c['strand']}: {verdict(c)[1]}")
        return
    if not (a.strand and a.round is not None):
        sys.exit("give STRAND and ROUND")
    p, c = load(a.strand)
    r = find(c, a.round)
    if a.cmd == "start":
        prof = r.get("ontology_profile")
        if prof and prof != "none" and prof not in profiles():
            sys.exit(f"round {a.round}: ontology_profile {prof!r} is not a profile in ontology/manifest.yaml")
        r["status"] = "running"
        print(f"ontology: load {prof} only (docs/ontology-in-flows.md)" if prof and prof != "none" else "ontology: load none")
        for d in c.get("every_round", []):
            print(f"every round delivers: {d}")
    elif a.cmd == "finish":
        if c.get("every_round") and not a.delivered:
            sys.exit("finish needs --delivered: every round delivers " + "; ".join(c["every_round"]))
        r["status"] = "done"
        if not any(x["status"] == "next" for x in c["rounds"]):
            q = next((x for x in c["rounds"] if x["status"] == "queued"), None)
            if q:
                q["status"] = "next"
    elif a.cmd == "look":
        if not (a.verdict and a.words):
            sys.exit("look needs --verdict and --words (his words, unaltered)")
        at = a.at or datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        lid = f"{c['strand']}-r{a.round}"
        if a.round >= c["last_look"]["round"]:
            c["last_look"] = {"round": a.round, "at": at, "label": lid}
        label = {"id": lid, "round": a.round, "at": at, "render": a.render or r.get("render", ""),
                 "verdict": a.verdict, "words": a.words}
        lp = HERE / "labels" / f"{c['strand']}.jsonl"
        lines = [l for l in lp.read_text().splitlines() if l.strip()] if lp.exists() else []
        lines = [l for l in lines if json.loads(l)["id"] != lid] + [json.dumps(label, ensure_ascii=False)]
        lp.write_text("\n".join(lines) + "\n")
        if a.verdict == "stop":
            for x in c["rounds"]:
                if x["status"] in ("next", "queued"):
                    x["status"] = "held"
    save(p, c)
    print(f"{c['strand']}: {verdict(c)[1]}")


if __name__ == "__main__":
    main()
