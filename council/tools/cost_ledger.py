"""Cost ledger: turn get_session rows into the table Wendell reads (docs/cost-ledger.md).

    python3 council/tools/cost_ledger.py rows.jsonl [more.jsonl ...] [--ledger ledger.jsonl] [--json out.json] [--md out.md]

Rows are the JSON `get_session` returns (id, title, created_at, updated_at, last_served_model, used_tokens, usage{...}),
one per line; an optional `first_request_input_tokens` is the opening load. Rows with an `error` are counted and skipped.
With --ledger, rows merge into that file by session id (the later updated_at wins) and the report reads the whole file.
Targets for 2026-10-25 (council #272): under 20% of threads end past 200,000 tokens, median end under 150,000.
"""
import argparse
import json
import statistics
import sys
from collections import defaultdict

PAST_A, PAST_B = 150_000, 200_000
TARGET_SHARE_PAST_B, TARGET_MEDIAN = 0.20, 150_000


def kind(title):
    t = (title or "").lower()
    if "board read" in t or t.startswith("board send") or "morning menu" in t:
        return "Board reads"
    if "compost" in t:
        return "Compost pass"
    if "coordinator" in t or t == "":
        return "Coordinators"
    if any(w in t for w in ("j5", "cloth", "spirit", "art round", "round ", "sheet", "sprite")):
        return "Art rounds"
    return "Build and design"


def load(paths):
    rows = {}
    for p in paths:
        for line in open(p):
            if line.strip():
                r = json.loads(line)
                if r.get("id"):
                    old = rows.get(r["id"])
                    if not old or (r.get("updated_at") or "") >= (old.get("updated_at") or ""):
                        rows[r["id"]] = r
    return list(rows.values())


def summarize(rows):
    good = [r for r in rows if "usage" in r]
    out = {"sessions": len(good), "skipped": len(rows) - len(good), "kinds": {}, "days": {}}

    def block(rs):
        ends = [r["used_tokens"] for r in rs]
        firsts = [r["first_request_input_tokens"] for r in rs if r.get("first_request_input_tokens")]
        return {
            "n": len(rs),
            "cost": round(sum(r["usage"]["cost_usd"] for r in rs), 2),
            "median_end": int(statistics.median(ends)) if ends else 0,
            "past_150k": sum(e > PAST_A for e in ends),
            "past_200k": sum(e > PAST_B for e in ends),
            "cost_past_200k": round(sum(r["usage"]["cost_usd"] for r in rs if r["used_tokens"] > PAST_B), 2),
            "median_first_call": int(statistics.median(firsts)) if firsts else None,
            "models": sorted({(r.get("last_served_model") or "?") for r in rs}),
        }

    out["all"] = block(good) if good else {}
    by_kind, by_day = defaultdict(list), defaultdict(list)
    for r in good:
        by_kind[kind(r.get("title"))].append(r)
        by_day[(r.get("updated_at") or r.get("created_at") or "")[:10]].append(r)
    out["kinds"] = {k: block(v) for k, v in sorted(by_kind.items())}
    out["days"] = {d: block(v) for d, v in sorted(by_day.items())}
    if good:
        a = out["all"]
        out["targets"] = {
            "share_past_200k": round(a["past_200k"] / a["n"], 3),
            "share_target": TARGET_SHARE_PAST_B,
            "median_end": a["median_end"],
            "median_target": TARGET_MEDIAN,
        }
    return out


def markdown(s):
    def line(label, b):
        fc = f"{b['median_first_call']:,}" if b["median_first_call"] else "n/a"
        return (f"| {label} | {b['n']} | ${b['cost']:,.2f} | {b['median_end']:,} | {fc} | "
                f"{b['past_150k']} | {b['past_200k']} (${b['cost_past_200k']:,.2f}) | {', '.join(b['models'])} |")

    head = ("| | Sessions | Cost | Median end | Median first call | Past 150k | Past 200k (cost) | Model |\n"
            "|-|-:|-:|-:|-:|-:|-:|-|")
    md = [f"{s['sessions']} sessions ({s['skipped']} skipped, no usage)", "", "Per thread kind", "", head]
    md += [line(k, b) for k, b in s["kinds"].items()]
    if s["all"]:
        md.append(line("All", s["all"]))
        t = s["targets"]
        md += ["", f"Targets: past 200k {t['share_past_200k']:.0%} (goal under {t['share_target']:.0%}); "
                   f"median end {t['median_end']:,} (goal under {t['median_target']:,})."]
    md += ["", "Per day (by last update)", "", head] + [line(d, b) for d, b in s["days"].items()]
    return "\n".join(md) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("rows", nargs="+")
    ap.add_argument("--ledger")
    ap.add_argument("--json")
    ap.add_argument("--md")
    ap.add_argument("--flat", help="directory for kinds.json, days.json, targets.json (the dashboard's datasets)")
    a = ap.parse_args(argv)
    paths = list(a.rows)
    if a.ledger:
        import os
        if os.path.exists(a.ledger):
            paths.append(a.ledger)
    rows = load(paths)
    if a.ledger:
        with open(a.ledger, "w") as f:
            for r in sorted(rows, key=lambda r: r.get("created_at") or ""):
                f.write(json.dumps(r, separators=(",", ":")) + "\n")
    s = summarize(rows)
    if a.json:
        json.dump(s, open(a.json, "w"), indent=1)
    if a.flat:
        import os
        os.makedirs(a.flat, exist_ok=True)
        flat = lambda d, key: [dict(b, **{key: k}, models=", ".join(b["models"])) for k, b in d.items()]
        tg = s.get("targets", {})
        for name, data in (("kinds", flat(s["kinds"], "kind") + ([dict(s["all"], kind="All", models=", ".join(s["all"]["models"]))] if s["all"] else [])),
                           ("days", flat(s["days"], "day")),
                           ("targets", [{"measure": "Threads ending past 200k tokens", "now": tg.get("share_past_200k"), "goal": tg.get("share_target")},
                                        {"measure": "Median end size (tokens)", "now": tg.get("median_end"), "goal": tg.get("median_target")}] if tg else [])):
            json.dump(data, open(os.path.join(a.flat, name + ".json"), "w"))
    md = markdown(s)
    if a.md:
        open(a.md, "w").write(md)
    sys.stdout.write(md)


if __name__ == "__main__":
    main()
