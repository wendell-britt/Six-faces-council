#!/usr/bin/env python3
"""The council's weekly read of the unchosen lines: the brainstorm lines Wendell named on a past morning and did not
choose, read where they live in bars-engine, with at most five patterns written back there, each with one pitch.

Pass unchosen1 (council/passes/6FACE_PASS_unchosen1_2026-10-21.md) set the positions; he answered `uc-who-reads` B on
2026-10-21: the council reads the pile once a week, in place, keeps no copy, and writes back at most five patterns, each
quoting his lines from two or more mornings with their dates. His steer on `uc-pattern-returns`, 2026-10-21: "And we
should intelligently pitch a new action item based on the fact it's coming back. Then compost the old one. this way
these unchosen fragments get better and more aligned over time".

The rules this script checks (bars-engine checks the same on POST, src/lib/tap-the-vein/unchosen-read.ts):
- `uc-pattern-returns`: a pattern is a word that comes back on two or more mornings. Every quote is one of his unchosen
  lines, word for word, with its day, and holds the word; the quotes span two mornings or more. At most five a week.
- His steer: each pattern carries one pitch, one action item. A word with a live pitch from an earlier week needs a new
  pitch; bars-engine composts the old one and keeps it muted under the new, so the pitch sharpens.
- `uc-no-duty`: a pitch is an offer, never a task. Nothing is written into his day; nothing reminds him.
- `uc-links-by-hand`: a pitch never turns lines into qi, vibeulons or spirits.
- `tb-loss-not-avoidance`: the read speaks about conditions, never about him.
- `uc-who-reads` B, keep no copy: the pile is fetched to a folder outside the repository and deleted after the write.
  Nothing from it is committed, quoted in a ledger or posted in chat. The report names how many patterns were written.

Usage:
  python3 council/unchosen_read.py fetch <dir>                    # the pile and live pitches, to <dir>/pile.json
  python3 council/unchosen_read.py check <dir>/pile.json <dir>/reads.json         # check the faces' read here
  python3 council/unchosen_read.py write <dir>/pile.json <dir>/reads.json         # check, dry-run, write, delete <dir>
      reads.json: [{"word": "<a word from the pile's patterns>", "face": "shaman|architect|challenger|regent|diplomat|sage",
        "kernel": "<one sentence: what the returning word reaches for, in his terms>",
        "pitch": "<one action item he could take, an offer>",
        "quotes": [{"day": "YYYY-MM-DD", "text": "<his line, word for word>"}, ...]}]
Auth: the egress proxy injects COUNCIL_MENU_TOKEN for bars-engine.vercel.app in a session; elsewhere set it in the env.
BARS_ENGINE_URL overrides https://bars-engine.vercel.app. The procedure: docs/unchosen-read.md.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = os.environ.get("BARS_ENGINE_URL", "https://bars-engine.vercel.app").rstrip("/")
PATH = "/api/tap-the-vein/unchosen"
FACES = ["shaman", "architect", "challenger", "regent", "diplomat", "sage"]
MAX_PATTERNS = 5
MIN_DAYS = 2
PITCH_MAX = 240
KERNEL_MAX = 240
# The same lists as bars-engine's unchosen-read.ts and council/bar_read.py.
ABOUT_HIM = re.compile(r"\b(avoid\w*|procrastinat\w*|resist\w*|lazy|excuse\w*|self-sabotag\w*|should have|failed to)\b", re.I)
CONVERTS = re.compile(r"\b(qi|vibeulons?|vibulons?|spirits?)\b", re.I)
# bars-engine's patternWords (src/lib/tap-the-vein/unchosen.ts): words under four letters and these are not patterns.
STOP = set((
    "about after again also back been before being both could didn does doing done down each even every from have "
    "here just know like make more most much need only other over really should some still such than that their "
    "them then there these they thing things this those through today very want what when where which while will "
    "with would your into onto maybe something start get going gonna").split())
COUNCIL_MENU_401 = ("COUNCIL_MENU_TOKEN is not accepted (401). The token rotation waits on Wendell's steps in the "
                    "\"Morning menu token steps\" thread (council/callsheets/morning-menu.md); the read runs once it answers 200.")


def norm(text):
    return re.sub(r"\s+", " ", (text or "").strip().lower())


def pattern_words(text):
    out = []
    for w in re.findall(r"[a-z][a-z']+", (text or "").lower()):
        w = re.sub(r"'s$", "", w).replace("'", "")
        if len(w) < 4 or w in STOP:
            continue
        if w.endswith("s") and not w.endswith("ss") and len(w) > 4:
            w = w[:-1]
        if w not in out:
            out.append(w)
    return out


def call(method, body=None):
    headers = {"Content-Type": "application/json", "User-Agent": "six-faces-council unchosen-read"}
    token = os.environ.get("COUNCIL_MENU_TOKEN", "").strip()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(BASE + PATH, method=method, headers=headers,
                                 data=json.dumps(body).encode() if body is not None else None)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        text = e.read().decode()[:600]
        if e.code == 401:
            sys.exit(COUNCIL_MENU_401)
        if e.code == 422:
            sys.exit("bars-engine refused the read:\n- " + "\n- ".join(json.loads(text).get("problems", [text])))
        sys.exit(f"{method} {PATH} answered {e.code}: {text}")
    except urllib.error.URLError as e:
        sys.exit(f"{method} {PATH} failed: {e.reason}")


def outside_repo(path):
    """The pile is his private writing (uc-who-reads B, keep no copy): it never lands inside the repository."""
    p = Path(path).resolve()
    if p == ROOT or ROOT in p.parents:
        sys.exit(f"{path} is inside the repository; fetch the pile to a scratch folder outside it (keep no copy)")
    return p


def check(pile, reads):
    """Every problem with the faces' read, against the pile and the live pitches; [] when it may be written."""
    problems = []
    if pile.get("readThisWeek"):
        problems.append(f"the week of {pile.get('weekOf')} has been read already")
    if not isinstance(reads, list):
        return problems + ["reads.json must be a list"]
    if len(reads) > MAX_PATTERNS:
        problems.append(f"at most {MAX_PATTERNS} patterns, got {len(reads)}")
    lines = {(l["day"], norm(l["text"])) for l in pile.get("lines", [])}
    live = {norm(p["word"]): p for p in pile.get("pitches", [])}
    seen = set()
    for i, r in enumerate(reads, 1):
        at = f"pattern {i}"
        words = pattern_words(r.get("word", ""))
        if not words:
            problems.append(f"{at}: needs a word that can carry a pattern (four letters or more, not filler)")
            continue
        word = words[0]
        if word in seen:
            problems.append(f'{at}: "{word}" is read twice')
        seen.add(word)
        if r.get("face") not in FACES:
            problems.append(f"{at}: face must be one of {', '.join(FACES)}")
        kernel, pitch = (r.get("kernel") or "").strip(), (r.get("pitch") or "").strip()
        if not 0 < len(kernel) <= KERNEL_MAX:
            problems.append(f"{at}: kernel is one sentence, 1 to {KERNEL_MAX} characters")
        if not 0 < len(pitch) <= PITCH_MAX:
            problems.append(f"{at}: pitch is one action item, 1 to {PITCH_MAX} characters")
        for name, text in (("kernel", kernel), ("pitch", pitch)):
            m = ABOUT_HIM.search(text)
            if m:
                problems.append(f'{at}: the {name} speaks about him, not the conditions ("{m.group(0)}")')
        if CONVERTS.search(pitch):
            problems.append(f"{at}: a pitch does not turn lines into qi, vibeulons or spirits (uc-links-by-hand)")
        days = set()
        for j, q in enumerate(r.get("quotes") or [], 1):
            day, text = q.get("day", ""), q.get("text", "")
            if (day, norm(text)) not in lines:
                problems.append(f"{at}, quote {j}: not an unchosen line of {day or 'that day'}, word for word")
            elif word not in pattern_words(text):
                problems.append(f'{at}, quote {j}: does not hold the word "{word}"')
            else:
                days.add(day)
        if len(days) < MIN_DAYS:
            problems.append(f"{at}: quotes his lines from {len(days)} morning(s); a pattern needs {MIN_DAYS}")
        old = live.get(word)
        if old and norm(old["pitch"]) == norm(pitch):
            problems.append(f'{at}: "{word}" came back, so it needs a new pitch, not the one from {old["weekOf"]}')
    return problems


def returning(pile, reads):
    """The words whose live pitch this read replaces, so the report can say what was composted."""
    live = {norm(p["word"]) for p in pile.get("pitches", [])}
    return [w for w in (next(iter(pattern_words(r.get("word", ""))), "") for r in reads) if w in live]


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] not in ("fetch", "check", "write"):
        sys.exit(__doc__)
    cmd = args.pop(0)
    if cmd == "fetch":
        if len(args) != 1:
            sys.exit("usage: unchosen_read.py fetch <dir outside the repository>")
        d = outside_repo(args[0])
        d.mkdir(parents=True, exist_ok=True)
        pile = call("GET")
        (d / "pile.json").write_text(json.dumps(pile, indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"{len(pile.get('lines', []))} unchosen lines, {len(pile.get('patterns', []))} returning words, "
              f"{len(pile.get('pitches', []))} live pitches; week of {pile.get('weekOf')}"
              + (" (already read)" if pile.get("readThisWeek") else "") + f". Saved to {d / 'pile.json'}.")
        return 0
    if len(args) != 2:
        sys.exit(f"usage: unchosen_read.py {cmd} <pile.json> <reads.json>")
    pile_path, reads_path = outside_repo(args[0]), outside_repo(args[1])
    pile, reads = load(pile_path), load(reads_path)
    problems = check(pile, reads)
    if problems:
        print("The read is not ready:\n- " + "\n- ".join(problems))
        return 1
    back = returning(pile, reads)
    if cmd == "check":
        print(f"The read checks: {len(reads)} pattern(s), {len(back)} returning with a new pitch.")
        return 0
    dry = call("POST", {"patterns": reads, "dry": True})
    wrote = call("POST", {"patterns": reads})
    for f in (pile_path, reads_path):
        f.unlink(missing_ok=True)
    print(f"Wrote the week of {wrote.get('weekOf')}: {wrote.get('created', 0)} pitch(es), "
          f"{wrote.get('composted', 0)} composted (dry run planned {len(dry.get('plan', {}).get('create', []))}). "
          "The pile and the read were deleted here; they live only in bars-engine.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
