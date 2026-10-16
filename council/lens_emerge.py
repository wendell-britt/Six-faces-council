#!/usr/bin/env python3
"""Let Lens goals emerge from his saved Tap the Vein free writes: a council reading pitches goals that recur across
days, each quoting his own lines from at least two different mornings.

Wendell, 2026-10-16: "I need a way for lenses to emerge through a council analysis of saved tap the vein (with the
idea that my freewrites would have the seeds of my long term goals)". Pass ttv-loop 1
(council/passes/6FACE_PASS_ttv-loop1_2026-10-16.md), position `ttv-lens-emerge`.

The free writes live on bars-engine, the private server (TapTheVeinDailySession.rawEntry). This script reads them
through GET /api/tap-the-vein/history and never writes them into this repo:

1. `fetch` saves the history to a file OUTSIDE the repo (a scratch folder), and refuses a path inside it.
2. The lens emergence read (a council thread) reads every free write once and pitches goals. A goal emerges when it
   returns: each pitch paraphrases what he wrote on at least two different days and cites only the date. His words
   are never quoted, because the writing is raw (Wendell, board, `ttv-lens-emerge` overruled 2026-10-16: "It's ok
   for the Council to paraphrase, they only need to cite the date"). `pitch` refuses a date with no free write, a
   gist that copies six or more of his words in a row, and a pitch resting on one morning.
3. Each pitch becomes a board question in the shape council/lens_goals.py already sends, so after he answers,
   `python3 council/lens_goals.py kept --send` writes each kept goal to bars-engine as an active year goal.
4. The read deletes its scratch copy.

Usage:
  python3 council/lens_emerge.py fetch --out <scratch>/vein.json [--since YYYY-MM-DD]
  python3 council/lens_emerge.py summary <scratch>/vein.json            # days, words, seeds by maturity
  python3 council/lens_emerge.py pitch <scratch>/vein.json --pitches p.json > rows.json
      p.json: [{"title": "<goal, a few words>", "domain": "<lens domain>", "why": "<one sentence>",
                "seen": [{"date": "YYYY-MM-DD", "gist": "<what he wrote that day, in the council's words>"}, ...]}]
"""
import argparse
import collections
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lens_goals import DOMAINS  # noqa: E402
from ttv_bars import ROOT, norm  # noqa: E402

HISTORY_URL = "https://bars-engine.vercel.app/api/tap-the-vein/history"
PASS = "lenses: goals emerging from saved free writes"
MAX_PITCHES = 5
COPY_RUN = 6  # a gist sharing this many words in a row with that day's free write is a quote, not a paraphrase


def fetch(out, since=None):
    out = Path(out).resolve()
    if out.is_relative_to(ROOT.resolve()):
        sys.exit("the free writes stay out of the repo: save the history to a scratch folder")
    token = os.environ.get("COUNCIL_MENU_TOKEN", "").strip()
    url = HISTORY_URL + (f"?since={since}" if since else "")
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"} if token else {})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read()
    except urllib.error.HTTPError as e:
        sys.exit({401: "bars-engine refused the key (401)", 503: "COUNCIL_MENU_TOKEN is not set in Vercel (503)",
                  404: "bars-engine has no /api/tap-the-vein/history yet (404); it ships with this pass"}
                 .get(e.code, f"HTTP {e.code}"))
    except urllib.error.URLError as e:
        sys.exit(f"bars-engine is out of reach from this session: {e.reason}")
    out.write_bytes(body)
    return json.loads(body)


def summary(hist):
    days = hist.get("days", [])
    words = sum(d.get("wordCount") or 0 for d in days)
    seeds = [s for d in days for s in d.get("seeds", [])]
    ripe = collections.Counter(s.get("maturity") or "no BAR" for s in seeds)
    status = collections.Counter(s.get("status") for s in seeds)
    lines = [f"{len(days)} days since {hist.get('since')}, {sum(1 for d in days if d.get('freewrite', '').strip())}"
             f" with a free write, {words} words",
             f"{len(seeds)} seeds: " + ", ".join(f"{k} {v}" for k, v in status.most_common()),
             "BAR maturity: " + ", ".join(f"{k} {v}" for k, v in ripe.most_common())]
    return "\n".join(lines)


def copied_run(gist, freewrite, n=COPY_RUN):
    """The first run of n words the gist shares with the free write, or None."""
    words = lambda t: "".join(c if c.isalnum() or c == "'" else " " for c in t.lower()).split()
    g, f = words(gist), words(freewrite)
    runs = {tuple(f[i:i + n]) for i in range(len(f) - n + 1)}
    return next((" ".join(g[i:i + n]) for i in range(len(g) - n + 1) if tuple(g[i:i + n]) in runs), None)


def check(hist, pitches):
    """Problems with the read's pitches; an empty list means they stand."""
    writes = {d["date"]: d.get("freewrite", "") for d in hist.get("days", []) if d.get("freewrite", "").strip()}
    bad = []
    if len(pitches) > MAX_PITCHES:
        bad.append(f"{len(pitches)} pitches; at most {MAX_PITCHES}, so each one is worth his look")
    for p in pitches:
        title = norm(p.get("title", ""))
        if p.get("domain") not in DOMAINS:
            bad.append(f"{title!r}: domain must be one of {', '.join(DOMAINS)}")
        if len(norm(p.get("why", "")).split()) < 4:
            bad.append(f"{title!r}: the why is under four words")
        if "lines" in p:
            bad.append(f"{title!r}: quotes his lines; paraphrase each morning under `seen` and cite only its date")
        dates = set()
        for s in p.get("seen", []):
            gist, date = norm(s.get("gist", "")), s.get("date")
            if date not in writes:
                bad.append(f"{title!r}: no free write on {date}")
            elif len(gist.split()) < 3:
                bad.append(f"{title!r}: the {date} gist is under three words")
            elif run := copied_run(gist, writes[date]):
                bad.append(f"{title!r}: the {date} gist copies his words ({run!r}); say it in the council's words")
            else:
                dates.add(date)
        if len(dates) < 2:
            bad.append(f"{title!r}: rests on {len(dates)} morning(s); a goal emerges when it returns on two or more")
    return bad


def pitch_rows(hist, pitches):
    """One board question per goal, in the shape council/lens_goals.py `kept` sends to bars-engine."""
    rows = []
    for i, p in enumerate(pitches, 1):
        goal, domain = norm(p["title"]), p["domain"]
        seen = sorted(p["seen"], key=lambda s: s["date"])
        said = seen[-1]["date"]
        heard = " ".join(f"On {s['date']}: {norm(s['gist']).rstrip('.')}." for s in seen)
        rows.append({
            "id": f"lens-emerge-{said}-{i}", "faces": ["shaman", "regent"], "pass": PASS,
            "q": f"Keep “{goal}” as a {domain} goal for this year?",
            "why_you": f"It came back across {len(seen)} mornings, in the council's words: {heard} "
                       f"{norm(p.get('why', ''))}".strip(),
            "not_before": "You have no Lens goals yet and skipped the intake as the game's creator, so the council "
                          "read your saved free writes for goals that recur (ttv-lens-emerge). It paraphrases and "
                          "cites dates only; your words are not quoted.",
            "options": [
                {"v": "keep", "label": "A. Keep it (recommended)",
                 "c": f"It becomes an active {domain} year goal in bars-engine, and the Lenses panel shows it."},
                {"v": "no", "label": "B. Not a goal",
                 "c": "Nothing is saved. Rename it in your steer and the next read pitches your wording."}],
            "why": "Pitched by the lens emergence read from saved free writes (council/lens_emerge.py pitch).",
            "lens_goal": goal, "lens_domain": domain, "lens_line": norm(seen[-1]["gist"]), "lens_paraphrase": True,
            "said": said,
        })
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("fetch", help="save the vein history to a scratch file outside the repo")
    f.add_argument("--out", required=True)
    f.add_argument("--since", help="YYYY-MM-DD; default the last 90 days")
    s = sub.add_parser("summary", help="days, words and seeds in a saved history")
    s.add_argument("history")
    p = sub.add_parser("pitch", help="board rows for the pitched goals, printed as sync_board.py --rows JSON")
    p.add_argument("history")
    p.add_argument("--pitches", required=True)
    a = ap.parse_args()
    if a.cmd == "fetch":
        print(summary(fetch(a.out, a.since)))
        return
    hist = json.loads(Path(a.history).read_text(encoding="utf-8"))
    if a.cmd == "summary":
        print(summary(hist))
        return
    pitches = json.loads(Path(a.pitches).read_text(encoding="utf-8"))
    bad = check(hist, pitches)
    if bad:
        sys.exit("the pitches do not stand:\n  " + "\n  ".join(bad))
    print(json.dumps({"questions": pitch_rows(hist, pitches)}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
