#!/usr/bin/env python3
"""Constant-extraction baseline for the Jev asset trial (ruling jev-asset-beat-script). No model.

Usage: constant_baseline.py <pile.json> <bars-engine checkout>
Pulls literal constants out of each doc line (file paths, size/dimension numbers, ALL_CAPS and
snake_case/camelCase identifiers, route paths, npm script names) and looks each up in the code
(git grep, excluding .specify/ and docs/ and council/). A row is flagged when any constant has no hit.
The script never sees labels.
"""
import json, os, re, subprocess, sys

def hit(repo, needle):
    r = subprocess.run(["git", "grep", "-qF", "--", needle, "--", ".", ":!.specify", ":!docs", ":!council", ":!*.md"],
                       cwd=repo, capture_output=True)
    return r.returncode == 0

def constants(s):
    out = set()
    for m in re.findall(r"`([^`]+)`", s): out.add(m)
    for m in re.findall(r"[\w./{}-]+\.(?:png|ts|tsx|lua|json)\b", s): out.add(m)
    for m in re.findall(r"\b\d+\s?[×x]\s?\d+\b", s): out.add(re.sub(r"\s", "", m))
    for m in re.findall(r"\b\d+(?:\.\d+)?\s?MB\b", s): out.add(m.replace(" ", ""))
    for m in re.findall(r"\b[A-Z][A-Z0-9]+(?:_[A-Z0-9]+)+\b", s): out.add(m)
    for m in re.findall(r"\b[a-z]+(?:_[a-z]+)+\b", s): out.add(m)
    for m in re.findall(r"\b[a-z]+[A-Z]\w+\b", s): out.add(m)
    for m in re.findall(r"(?<![\w.])/(?:api|admin)/[\w/:.-]+", s): out.add(m)
    return {c.strip("{}") for c in out if len(c) > 3 and "{" not in c}

def variants(c):
    v = {c}
    if re.fullmatch(r"\d+\s?MB", c): n = c[:-2]; v |= {f"{n} * 1024 * 1024", f"{n}*1024*1024", f"{n} MB"}
    if re.fullmatch(r"\d+×\d+", c): v |= {c.replace("×", "x"), c.replace("×", " × ")} | {c.split("×")[0]}
    return v

pile, repo = sys.argv[1], sys.argv[2]
d = json.load(open(pile)); rows = d["rows"] if isinstance(d, dict) else d
res = {}
for r in rows:
    miss = [c for c in sorted(constants(r["statement"])) if not any(hit(repo, x) for x in variants(c))]
    res[r["id"]] = {"flag": bool(miss), "unmatched": miss}
print(json.dumps(res, indent=1))
