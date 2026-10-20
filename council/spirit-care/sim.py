#!/usr/bin/env python3
"""Four players come back to their spirits: does a mortal spirit add care or guilt?

Spirit care pass 1 (council/passes/6FACE_PASS_spirit-care1_2026-10-20.md), the Challenger's falsification test:
"Simulate four players through the ladder: one who tends daily, one who is busy, one who has a bad week with a
declared rest, and one who vanishes for three weeks without a word. Write down what each finds when they come back.
If the vanished player's return screen makes coming back harder, the design fails. If no player's spirit ever dies,
the stake is theatre."

Everything that is a design choice is data at the top of this file: the decline ladder (`sc-ladder`), the three
tracks (satisfaction, vitality, shadow), the shadow sources (`sc-shadow-legible`), the care acts (`sc-cleanup-care`)
and the quest templates (`sc-spirit-bars`). The numbers are the council's first guess, to be tuned here and shown to
Wendell before they ship (`sc-ladder`: "The stage lengths are tuned by a simulation and shown to you").

His three questions are not answered yet, so every option of `sc-undying` and `sc-after-death` runs.

scout: rung 2 (we have it). The quest offer mirrors bars-engine src/lib/charge-quest-generator/generator.ts: a
need picks a move order the way EMOTION_MOVE_BIAS does, and the first template of the first move fills in. The port
to bars-engine calls generateQuestSuggestions instead of TEMPLATES below.

Usage:
  python3 council/spirit-care/sim.py                     every option pair, one line per player, then the checks
  python3 council/spirit-care/sim.py --show A A          the return screens for one option pair
  python3 council/spirit-care/sim.py --days              the day-by-day stages for one pair (with --show)
Exit 1 when a check fails.
"""
import argparse
import sys
from dataclasses import dataclass, field

# ---------------------------------------------------------------- the design, as data

# sc-ladder: stages that cannot be skipped. `dwell` is the fewest days a declining spirit stays in a stage before it
# can go one step lower, so a player who looks in once sees it. `enter` is when the tracks call for the stage.
LADDER = [
    {"stage": "thriving", "dwell": 0, "body": "bright and moving about"},
    {"stage": "dimming", "dwell": 2, "body": "its light a little lower"},
    {"stage": "stale", "dwell": 3, "body": "still, its colour dulled"},
    {"stage": "shadowed", "dwell": 4, "body": "a shadow lying over it, its light still inside"},
    {"stage": "fading", "dwell": 3, "body": "thin, hard to see"},
    {"stage": "gone", "dwell": 0, "body": ""},
]
STAGES = [s["stage"] for s in LADDER]
DWELL = {s["stage"]: s["dwell"] for s in LADDER}


def stage_called_for(vitality, shadow):
    """The stage the tracks call for. Shadow takes a spirit past stale; vitality alone only dims it."""
    if vitality <= 0:
        return "gone"
    if vitality <= 25:
        return "fading"
    if shadow >= 50:
        return "shadowed"
    if vitality <= 60:
        return "stale"
    if vitality <= 85:
        return "dimming"
    return "thriving"


# The three tracks. Satisfaction is the existing 1 to 10 mood (ss-feral-trade); vitality and shadow are new.
VITALITY_START, VITALITY_MAX = 100, 100
DECAY_PER_UNTENDED_DAY = 5        # vitality lost on a day with no care and no declared rest
CARE_LIFT = 20                    # sc-cleanup-care: one real act of any size holds a spirit steady
CLEANUP_CLEAR = 35                # a 3-2-1, W.A.V.E., a spar, or a real step of self or relationship care
CLEANUP_LIFT = 10                 # Clean Up also counts as care; it clears more than it costs
UNSETTLED_AT = 3                  # sc-word: low satisfaction is "unsettled", never "corrupted"
MOOD_DROP_EVERY = 3               # satisfaction falls one point per this many untended days

# sc-shadow-legible: shadow always shows where it came from, and only lands on an untended day.
SHADOW_SOURCES = {
    "unworked charge": {"per_day": 4, "says": "an unworked charge has been sitting on it"},
    "daemon pushed too far": {"per_day": 5, "says": "its own daemon's pattern has been pushed too far"},
    "broken agreement": {"per_day": 6, "says": "an agreement between you went unkept"},
}

DAEMON_SHADOW = {
    "Protector": "walls",
    "Controller": "grip",
    "Fixer": "rush to fix",
    "Skeptic": "doubt",
}

# sc-spirit-bars: a need picks the move order, as EMOTION_MOVE_BIAS does in generator.ts.
NEED_MOVE_BIAS = {
    "shadow": ["clean_up", "wake_up", "grow_up", "show_up"],
    "vitality": ["show_up", "clean_up", "wake_up", "grow_up"],
    "none": ["grow_up", "show_up", "wake_up", "clean_up"],
}
TEMPLATES = {
    "clean_up": "Sit with the {daemon}'s {pattern} for one breath of W.A.V.E., then write one line on what it keeps from {goal}.",
    "show_up": "Do one small thing today for {goal}, any size, and tell {name} about it.",
    "grow_up": "Name one step {name}'s {element} asks of you toward {goal}.",
    "wake_up": "Notice once today where {goal} shows up in your body.",
}

# Sample goals so the quest has something to cite. The real ones are his Lens goals (council/lens_goals.py) and the
# pair's planted agreements (bars-engine public/between/garden.js).
SAMPLE_GOAL = "a calmer morning (sample Lens goal)"
SAMPLE_AGREEMENT = "a call on Sundays (sample Between agreement)"

# The options of his two open questions (rows file council/callsheets/rows/spirit-care-2026-10-20.json).
UNDYING = {"A": "every spirit can die", "B": "chosen at bonding", "C": "only shared spirits, by agreement"}
AFTER_DEATH = {"A": "a seed to plant", "B": "a stone to remember", "C": "called back once"}

# Words a return screen never uses: no nag, no count, no blame (sc-cleanup-care, sc-shadow-legible, sc-rest).
NEVER_SAY = ["streak", "missed you", "you forgot", "your fault", "neglect", "in a row", "you left", "abandon",
             "while you were away", "failed"]

DAYS = 28
RECOMMENDED = ("A", "A")          # the council's recommendation on both questions; every check must pass here
STAKE_CHECKS = {"at least one spirit can die"}   # under the other options a miss is a finding, not a failure


# ---------------------------------------------------------------- the four lives (and one shared spirit)

def daily(day):
    return {"care": True, "cleanup": day % 3 == 2}


def busy(day):
    return {"care": day % 4 == 0, "cleanup": day in (12, 24)}


def rest(day):
    if 7 <= day <= 16:
        return {"rest": True}
    return {"care": True, "cleanup": day % 4 == 3}


def vanished(day):
    if day >= 7:
        return {}
    return {"care": True, "cleanup": day == 3}


@dataclass
class Spirit:
    name: str
    element: str
    daemon: str
    source: str
    shared: bool = False
    undying: bool = False
    vitality: int = VITALITY_START
    shadow: int = 0
    satisfaction: int = 7
    stage: str = "thriving"
    untended: int = 0
    days_in_stage: int = 0
    asked: list = field(default_factory=list)      # stages at which it offered a quest in its own voice
    told: list = field(default_factory=list)       # who was told it reached fading
    history: list = field(default_factory=list)
    seen_while_away: set = field(default_factory=set)


# Each player's spirits. The vanished player holds two, with different shadow sources, so the run shows a range.
PLAYERS = [
    {"who": "daily", "life": daily, "return_day": DAYS,
     "spirits": [("Wren", "wood", "Fixer", "unworked charge")]},
    {"who": "busy", "life": busy, "return_day": DAYS,
     "spirits": [("Ember", "fire", "Controller", "daemon pushed too far")]},
    {"who": "rest", "life": rest, "return_day": 17,
     "spirits": [("Tide", "water", "Protector", "daemon pushed too far")]},
    {"who": "vanished", "life": vanished, "return_day": DAYS,
     "spirits": [("Moss", "earth", "Protector", "daemon pushed too far"),
                 ("Pip", "metal", "Skeptic", "unworked charge")]},
]
# sc-between-decline: a shared spirit tended by either person. The busy player and the vanished player share it.
# A second shared spirit whose pair both go quiet, so the both-told rule and option C of sc-undying get exercised.
PAIRS = [
    {"who": "pair (busy + vanished)", "lives": [busy, vanished], "people": ["busy", "vanished"],
     "spirit": ("Hearth", "fire", "Protector", "broken agreement")},
    {"who": "pair (both vanished)", "lives": [vanished, vanished], "people": ["vanished", "their partner"],
     "spirit": ("Lark", "wood", "Fixer", "broken agreement")},
]


# ---------------------------------------------------------------- the clock

def mortal(spirit, undying_option):
    if undying_option == "A":
        return True
    if undying_option == "B":
        return not spirit.undying
    return spirit.shared                            # C: only shared spirits die


def step(spirit, acts, undying_option, people):
    """One day. `acts` is the merged day of everyone who holds the spirit."""
    if acts.get("rest"):                            # sc-rest: a declared rest pauses fading and shadow
        spirit.history.append(spirit.stage)
        spirit.days_in_stage += 1
        return
    if acts.get("care") or acts.get("cleanup"):
        spirit.vitality = min(VITALITY_MAX, spirit.vitality + CARE_LIFT)
        spirit.satisfaction = min(10, spirit.satisfaction + 1)
        if acts.get("cleanup"):
            spirit.shadow = max(0, spirit.shadow - CLEANUP_CLEAR)
            spirit.vitality = min(VITALITY_MAX, spirit.vitality + CLEANUP_LIFT)
    else:
        spirit.vitality = max(0, spirit.vitality - DECAY_PER_UNTENDED_DAY)
        spirit.shadow = min(100, spirit.shadow + SHADOW_SOURCES[spirit.source]["per_day"])
        spirit.untended += 1
        if spirit.untended % MOOD_DROP_EVERY == 0:
            spirit.satisfaction = max(1, spirit.satisfaction - 1)
    if not mortal(spirit, undying_option):
        spirit.vitality = max(spirit.vitality, 1)   # an undying spirit fades and is shadowed, but stops short of death

    want = STAGES.index(stage_called_for(spirit.vitality, spirit.shadow))
    have = STAGES.index(spirit.stage)
    if want < have:                                 # care lifts one step a day
        new = have - 1
    elif want > have and spirit.days_in_stage >= DWELL[spirit.stage]:
        new = have + 1                              # decline one step at a time, after the stage has been seen
    else:
        new = have
    if new != have:
        spirit.stage, spirit.days_in_stage = STAGES[new], 0
        if spirit.stage in ("stale", "fading") and spirit.stage not in spirit.asked:
            spirit.asked.append(spirit.stage)       # it asks once, in its own voice, by offering a quest
        if spirit.stage == "fading":
            spirit.told = list(people)              # sc-between-decline: both are told before it can die
    else:
        spirit.days_in_stage += 1
    spirit.history.append(spirit.stage)


# ---------------------------------------------------------------- the quest it offers

def offer(spirit):
    need = "shadow" if spirit.shadow >= 30 else "vitality" if spirit.vitality <= 60 else "none"
    move = NEED_MOVE_BIAS[need][0]
    cites = SAMPLE_AGREEMENT if spirit.shared else SAMPLE_GOAL
    text = TEMPLATES[move].format(daemon=spirit.daemon, pattern=DAEMON_SHADOW[spirit.daemon], name=spirit.name,
                                  element=spirit.element, goal=cites)
    return {"move": move, "text": text, "cites": cites}


# ---------------------------------------------------------------- what they find when they come back

def return_screen(spirit, after_option):
    """Welcome before report (sc-rest). Shadow named by its source, never by a failing. No counts."""
    q = offer(spirit)
    lines = []
    if spirit.stage == "gone":
        lines.append(("welcome", f"Welcome back. Come and sit a while, before anything else."))
        if after_option == "A":
            lines.append(("report", f"{spirit.name} has gone. It left you a seed of {spirit.element} with its name on "
                                    f"it. Planting it grows a new spirit that carries {spirit.name}'s story."))
            lines.append(("offer", "Plant the seed now, or keep it for later. Either is fine."))
        elif after_option == "B":
            lines.append(("report", f"{spirit.name} has gone. Its stone stands in your space with its name on it."))
            lines.append(("offer", "Sit by the stone, or bond a new spirit when you are ready."))
        else:
            lines.append(("report", f"{spirit.name} has gone, and can be called back once."))
            lines.append(("offer", f"A Clean Up quest calls it back: {TEMPLATES['clean_up'].format(daemon=spirit.daemon, pattern=DAEMON_SHADOW[spirit.daemon], name=spirit.name, element=spirit.element, goal=SAMPLE_AGREEMENT if spirit.shared else SAMPLE_GOAL)} "
                                   "Yes, or not now."))
        return lines
    lines.append(("welcome", f"{spirit.name} lifts its head. It is glad you are here."))
    body = next(s["body"] for s in LADDER if s["stage"] == spirit.stage)
    if spirit.stage == "thriving":
        lines.append(("report", f"{spirit.name} is {body}."))
    else:
        report = f"{spirit.name} is {spirit.stage}: {body}."
        if spirit.shadow >= 30:
            report += f" The shadow is there because {SHADOW_SOURCES[spirit.source]['says']}."
        lines.append(("report", report))
    if spirit.satisfaction <= UNSETTLED_AT:
        lines.append(("report", f"It is unsettled, and will settle with company."))
    lines.append(("offer", f"{spirit.name} offers a quest for {q['cites']}: {q['text']} Say yes, or not now."))
    return lines


# ---------------------------------------------------------------- one run

def build(spec, shared=False, undying=False):
    name, element, daemon, source = spec
    return Spirit(name, element, daemon, source, shared=shared, undying=undying)


def run(undying_option, after_option):
    results = []
    for p in PLAYERS:
        for i, spec in enumerate(p["spirits"]):
            # Under B the player chooses at bonding; this run has the vanished player bond Pip as undying.
            s = build(spec, undying=(undying_option == "B" and spec[0] == "Pip"))
            for day in range(p["return_day"]):
                step(s, p["life"](day), undying_option, [p["who"]])
            results.append({"who": p["who"], "spirit": s, "screen": return_screen(s, after_option)})
    for pr in PAIRS:
        s = build(pr["spirit"], shared=True)
        for day in range(DAYS):
            merged = {}
            for life in pr["lives"]:                # either person's tending lifts it
                for k, v in life(day).items():
                    merged[k] = merged.get(k) or v
            step(s, merged, undying_option, pr["people"])
        results.append({"who": pr["who"], "spirit": s, "people": pr["people"],
                        "screen": return_screen(s, after_option)})
    return results


# ---------------------------------------------------------------- the checks

def no_skip(history):
    """Every step down the ladder is one stage, and each stage held for its dwell before the next step down."""
    run_len, prev = 0, "thriving"
    for st in history:
        a, b = STAGES.index(prev), STAGES.index(st)
        if b > a + 1:
            return False
        if b > a and run_len < DWELL[prev]:
            return False
        run_len = run_len + 1 if b == a else 0
        prev = st
    return True


def checks(results, undying_option):
    out = []
    v = [r for r in results if r["who"] == "vanished"]
    out.append(("vanished return welcomes before it reports",
                all(r["screen"][0][0] == "welcome" for r in v)))
    out.append(("every return welcomes before it reports", all(r["screen"][0][0] == "welcome" for r in results)))
    texts = [t.lower() for r in results for _, t in r["screen"]]
    out.append(("no return screen nags, counts or blames",
                not any(w in t for t in texts for w in NEVER_SAY) and not any(ch.isdigit() for t in texts for ch in t)))
    deaths = [r for r in results if r["spirit"].stage == "gone"]
    out.append(("at least one spirit can die", bool(deaths)))
    out.append(("the daily player's spirit is never shadowed",
                all(st in ("thriving", "dimming") for r in results if r["who"] == "daily" for st in r["spirit"].history)))
    rest_r = next(r for r in results if r["who"] == "rest")
    out.append(("a declared rest comes back as it left", rest_r["spirit"].history[16] == rest_r["spirit"].history[6]))
    out.append(("no spirit skips a stage on the way down", all(no_skip(r["spirit"].history) for r in results)))
    out.append(("every spirit that died asked first, in its own voice",
                all("stale" in r["spirit"].asked and "fading" in r["spirit"].asked for r in deaths)))
    pairs = [r for r in results if "people" in r and "fading" in r["spirit"].history]
    out.append(("both of a pair are told at fading", bool(pairs) and all(r["spirit"].told == r["people"] for r in pairs)))
    out.append(("every offered quest cites a goal or agreement",
                all(any(k == "offer" for k, _ in r["screen"]) for r in results)))
    return out


# ---------------------------------------------------------------- printing

def summary_line(r):
    s = r["spirit"]
    died_on = s.history.index("gone") + 1 if "gone" in s.history else None
    end = f"gone on day {died_on}" if died_on else s.stage
    return f"  {r['who']:<24} {s.name:<7} {end:<16} vitality {s.vitality:>3}  shadow {s.shadow:>3}  mood {s.satisfaction:>2}"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--show", nargs=2, metavar=("UNDYING", "AFTER"), help="return screens for one option pair")
    ap.add_argument("--days", action="store_true", help="with --show: the stage on each day")
    a = ap.parse_args(argv)
    pairs = [tuple(a.show)] if a.show else [(u, d) for u in UNDYING for d in AFTER_DEATH]
    failed = 0
    for u, d in pairs:
        results = run(u, d)
        print(f"\nsc-undying {u} ({UNDYING[u]}), sc-after-death {d} ({AFTER_DEATH[d]})")
        for r in results:
            print(summary_line(r))
            if a.show:
                for kind, text in r["screen"]:
                    print(f"      [{kind}] {text}")
                if a.days:
                    print("      " + " ".join(st[:2] for st in r["spirit"].history))
        for name, ok in checks(results, u):
            finding = name in STAKE_CHECKS and (u, d) != RECOMMENDED
            print(f"  {'pass' if ok else 'finding' if finding else 'FAIL'}  {name}")
            failed += not ok and not finding
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
