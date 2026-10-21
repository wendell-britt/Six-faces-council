#!/usr/bin/env python3
"""The email voice pass: does a drafted email sound like Wendell, and does anything in it read as AI?

    python3 board/email_voice.py <file> [--kind reply|outreach] [--json] [--accept RULE:"reason" ...]

The checks come from the profile, council/voice/email-voice.yaml (docs/email-voice.md). A port of the MTGOA editorial
pipeline's idea, not its book machinery: one profile file says what is true of this voice, and the scanner is generic.

  tell  reads as AI to a wary reader. Every hit ends in one of two terminal states: rewritten in the text, or
        accepted with a written reason (--accept RULE:"reason", which accepts every hit of that rule).
  fit   off his voice but not a tell. Printed as a note and never blocks.

voice_lint's hard findings (council/tools/voice_lint.py) are read too, each given a class by the profile.
Each finding prints its line, rule, the text, and what his own mail does instead. Exit 1 while an unaccepted tell
remains, 2 on bad usage.
"""
import argparse
import json
import re
import statistics
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
PROFILE = ROOT / "council" / "voice" / "email-voice.yaml"
VOICE_LINT = ROOT / "council" / "tools" / "voice_lint.py"
KINDS = ("reply", "outreach")

GREETING = re.compile(r"^\s*(hey|heyo|hi|hello|dear|good (morning|afternoon|evening))\b[^.!?]{0,30}[!,.:]?\s*$", re.I)
SIGNOFF_LEAD = re.compile(r"^\s*[A-Za-z' ]{1,25},\s*$")
SENT_SPLIT = re.compile(r"(?<=[.!?])[\"')\]]*\s+")
WORD = re.compile(r"[A-Za-z0-9][A-Za-z0-9'-]*")
CONTRACTION = re.compile(r"\b\w+n't\b|\b\w+'(m|re|ve|ll|d)\b|\b(it|that|there|here|what|let|who|he|she)'s\b", re.I)
EXPANDED = re.compile(r"\bI am\b|\b(do|does|did|is|are|was|were|could|would|should|have|has|had|will) not\b|\bcannot\b"
                      r"|\b(I|we|you|they) (will|would|have|are)\b|\b(it|that|there) is\b|\blet us\b", re.I)
ACRONYMS = {"AI", "CST", "PST", "PDT", "EST", "PT", "ET", "URL", "PDF", "FAQ", "RSVP", "ASAP", "USA", "PR", "OK", "TV",
            "CEO", "API", "UI", "NYC", "PDX", "DM", "CC", "BCC"}
CAPS_WORD = re.compile(r"\b[A-Z]{2,}\b")
STRETCHED = re.compile(r"([A-Za-z])\1\1")
PAREN = re.compile(r"\([^)]{8,}\)")
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")


def load_profile(path=PROFILE):
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))


def rule_ids(profile):
    return {t["id"] for t in profile["tells"]} | set(profile.get("voice_lint", {})) | set(FIT_RULES)


# ---- reading the email ----
def parse(body):
    """Lines kept for the pass (quoted reply text and the signature cut off), with their 1-based line numbers."""
    kept = []
    for i, line in enumerate(str(body).replace("\r\n", "\n").split("\n"), 1):
        if line.rstrip() == "--" or re.match(r"^On .{4,120} wrote:\s*$", line):
            break
        if line.lstrip().startswith(">"):
            continue
        kept.append((i, line.replace("’", "'")))
    paras, cur = [], []
    for n, line in kept:
        if line.strip():
            cur.append((n, line))
        elif cur:
            paras.append(cur)
            cur = []
    if cur:
        paras.append(cur)
    greeting = signoff = None
    if paras and GREETING.match(paras[0][0][1]) and len(WORD.findall(paras[0][0][1])) <= 6:
        greeting = paras[0][0]
        paras[0] = paras[0][1:]
        if not paras[0]:
            paras.pop(0)
    if paras:
        last = paras[-1]
        tail = last[-2:] if len(last) >= 2 and SIGNOFF_LEAD.match(last[-2][1]) else None
        if tail and len(WORD.findall(tail[-1][1])) <= 3:
            signoff = tail
            paras[-1] = last[:-2]
        elif len(last) >= 2 and re.fullmatch(r"\s*-?\s*[A-Z][a-z]+\s*", last[-1][1]):
            signoff = last[-1:]
            paras[-1] = last[:-1]
        elif len(last) == 1 and re.fullmatch(r"\s*-?\s*[A-Z][a-z]+\s*", last[0][1]) and len(paras) > 1:
            signoff = last
            paras[-1] = []
        if paras and not paras[-1]:
            paras.pop()
    return {"lines": kept, "paras": paras, "greeting": greeting, "signoff": signoff}


def sentences(para):
    text = " ".join(l.strip() for _, l in para)
    return [s for s in SENT_SPLIT.split(text) if WORD.search(s)]


# ---- the checks ----
def finding(rule, cls, line, text, instead, source="profile"):
    return {"rule": rule, "class": cls, "line": line, "text": str(text).strip()[:80], "instead": instead,
            "source": source}


def context(line, m):
    """The hit, widened to its neighbouring words when it is a single mark (a dash, a semicolon)."""
    if len(m.group(0).strip()) >= 6:
        return m.group(0)
    a, b = max(0, m.start() - 24), min(len(line), m.end() + 24)
    return ("..." if a else "") + line[a:b].strip() + ("..." if b < len(line) else "")


def tell_hits(profile, doc):
    out = []
    # the closing: the last two paragraphs above the sign-off, where a recap or a restated ask sits
    closing = [l for p in doc["paras"][-2:] for l in p] if len(doc["paras"]) >= 2 else []
    for t in profile["tells"]:
        rx = re.compile(t["pattern"], re.I | re.M)
        lines = closing if t.get("scope") == "closing" else doc["lines"]
        for n, line in lines:
            for m in rx.finditer(line):
                out.append(finding(t["id"], "tell", n, context(line, m), t["instead"]))
    return out


def lint_hits(profile, body, doc):
    classes = profile.get("voice_lint", {})
    his_lines = {x.lower() for x in profile["traits"]["closers"] + profile["traits"].get("short_lines", [])}
    frame = {n for n, _ in ([doc["greeting"]] if doc["greeting"] else []) + (doc["signoff"] or [])}
    with tempfile.TemporaryDirectory() as t:
        p = Path(t) / "draft.txt"
        p.write_text(body, encoding="utf-8")
        r = subprocess.run([sys.executable, str(VOICE_LINT), str(p), "--json"], capture_output=True, text=True)
    try:
        rep = json.loads(r.stdout)
    except json.JSONDecodeError:
        return [finding("voice_lint", "fit", 0, "voice_lint did not run", "Run council/tools/voice_lint.py by hand.",
                        "voice_lint")]
    out = []
    for e in rep:
        for h in e["hard"]:
            cls = classes.get(h["rule"], "tell")
            if cls == "off" or h["line"] in frame:  # "Hey Wendell!" and "Best, Wendell" are not sentences
                continue
            if h["rule"] == "fragment" and h["text"].strip().lower() in his_lines:
                continue
            out.append(finding(h["rule"], cls, h["line"], h["text"], h["why"], "voice_lint"))
    return out


def playful(profile, text):
    low = text.lower().replace("’", "'")
    if any(s in low for s in profile["traits"]["playful"]["slang"]):
        return True
    caps = [w for w in CAPS_WORD.findall(text) if w not in ACRONYMS and w != "I"]
    return bool(caps or STRETCHED.search(text) or PAREN.search(text) or EMOJI.search(text))


FIT_RULES = ("length", "sentence-length", "even-sentences", "long-paragraph", "no-exclamation", "contractions",
             "greeting", "signoff-block", "no-playful", "flat-ending")


def fit_hits(profile, doc, kind):
    tr, out = profile["traits"], []
    paras = doc["paras"]
    body_lines = [l for p in paras for l in p]
    text = "\n".join(l for _, l in body_lines)
    words = len(WORD.findall(text))
    first = body_lines[0][0] if body_lines else 1
    lo, hi = tr["words"][kind]
    if not lo <= words <= hi:
        out.append(finding("length", "fit", first, f"{words} words",
                           f"His {kind}s run {lo} to {hi} words. Most replies are 1 to 4 sentences."))
    sents = [s for p in paras for s in sentences(p)]
    lens = [len(WORD.findall(s)) for s in sents]
    if lens and statistics.mean(lens) > tr["sentence_words"]["max_mean"]:
        out.append(finding("sentence-length", "fit", first, f"{statistics.mean(lens):.1f} words a sentence",
                           f"His sentences average under {tr['sentence_words']['max_mean']} words. Break the long ones."))
    if len(lens) >= 4 and statistics.pstdev(lens) / statistics.mean(lens) < tr["sentence_words"]["evenness"]:
        out.append(finding("even-sentences", "fit", first, f"lengths {lens}",
                           "Polished, even sentences read as machine. Mix a two-word line in: \"Copy that!\""))
    for p in paras:
        if len(sentences(p)) > tr["paragraph_sentences_max"]:
            out.append(finding("long-paragraph", "fit", p[0][0], p[0][1],
                               "His paragraphs are one or two sentences, a line break between."))
    if text.count("!") < tr["exclamations_min"]:
        out.append(finding("no-exclamation", "fit", first, "no exclamation point",
                           "Nearly every email of his has one, often 2 to 4: \"Looking forward to it!\""))
    c, e = len(CONTRACTION.findall(text)), list(EXPANDED.finditer(text))
    if e and c / (c + len(e)) < tr["contraction_rate_min"]:
        n = next((num for num, l in body_lines if EXPANDED.search(l)), first)
        out.append(finding("contractions", "fit", n, e[0].group(0),
                           f"Contractions everywhere: I'm, we're, can't, gonna. {c} here against {len(e)} spelled out."))
    g = doc["greeting"]
    if g and re.match(r"^\s*hi\b", g[1], re.I) and kind == "reply":
        out.append(finding("greeting", "fit", g[0], g[1], "\"Hi <Name>,\" is his formal opener. Casual mail: \"Hey <Name>!\""))
    if not g and kind == "outreach":
        out.append(finding("greeting", "fit", first, "no greeting",
                           "First outreach opens \"Hey <Name>!\". Replies can dive straight in."))
    s = doc["signoff"]
    if s and kind == "reply":
        out.append(finding("signoff-block", "fit", s[0][0], " / ".join(l.strip() for _, l in s),
                           "Casual mail ends on the last line, no sign-off block. Formal mail: \"Best, Wendell\"."))
    if words >= tr["playful"]["after_words"] and not playful(profile, text):
        out.append(finding("no-playful", "fit", first, "no playful line",
                           "One playful line or a self-aware parenthetical: \"(and actually put it in my calendar this time)\""))
    if sents and not sents[-1].rstrip(" )\"'").endswith(("!", "?")):
        out.append(finding("flat-ending", "fit", body_lines[-1][0], sents[-1],
                           "End forward-looking: \"Looking forward to it!\", \"See ya then!\""))
    return out


def scan(body, kind="outreach", accept=None, profile=None):
    """Every finding on the body, tells first. accept maps a rule id to its written reason."""
    if kind not in KINDS:
        raise ValueError(f"kind must be one of {KINDS}")
    profile = profile or load_profile()
    doc = parse(body)
    found = tell_hits(profile, doc) + lint_hits(profile, body, doc) + fit_hits(profile, doc, kind)
    for f in found:
        if (accept or {}).get(f["rule"]):
            f["accepted"] = accept[f["rule"]]
    found.sort(key=lambda f: (f["class"] != "tell", f["line"]))
    return found


def open_tells(found):
    return [f for f in found if f["class"] == "tell" and not f.get("accepted")]


def parse_accepts(items, profile=None):
    """["RULE:reason", ...] -> {rule: reason}. A reason is required: that is the second terminal state."""
    known = rule_ids(profile or load_profile())
    out = {}
    for item in items or []:
        rule, _, reason = item.partition(":")
        rule, reason = rule.strip(), reason.strip().strip('"')
        if not reason:
            raise ValueError(f'--accept {item!r} needs a written reason: --accept {rule}:"why it stays"')
        if rule not in known:
            raise ValueError(f"--accept: no rule named {rule!r} (rules: {', '.join(sorted(known))})")
        out[rule] = reason
    return out


def report(found, kind, words=None):
    tells = [f for f in found if f["class"] == "tell"]
    lines = [f"email voice pass ({kind}): {len(open_tells(found))} open tell(s), "
             f"{len(tells) - len(open_tells(found))} accepted, {len(found) - len(tells)} fit note(s)"]
    for f in found:
        tag = "TELL" if f["class"] == "tell" else "fit "
        acc = f'  [accepted: {f["accepted"]}]' if f.get("accepted") else ""
        lines.append(f'  L{f["line"]:<3} {tag} {f["rule"]}: "{f["text"]}"{acc}')
        lines.append(f'         his mail: {f["instead"]}')
    if open_tells(found):
        lines.append('Rewrite each TELL, or accept it with a reason: --accept RULE:"why it stays".')
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--kind", choices=KINDS, default="outreach")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--accept", action="append", default=[], metavar='RULE:"reason"')
    a = ap.parse_args()
    profile = load_profile()
    try:
        accept = parse_accepts(a.accept, profile)
    except ValueError as e:
        print(e, file=sys.stderr)
        return 2
    found = scan(Path(a.file).read_text(encoding="utf-8"), a.kind, accept, profile)
    if a.json:
        print(json.dumps({"kind": a.kind, "open_tells": len(open_tells(found)), "findings": found}, indent=1,
                         ensure_ascii=False))
    else:
        print(report(found, a.kind))
    return 1 if open_tells(found) else 0


if __name__ == "__main__":
    sys.exit(main())
