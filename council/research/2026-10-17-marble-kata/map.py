#!/usr/bin/env python3
"""Map the Marble Skill Taxonomy's social-emotional topics onto Emotional Alchemy, and check the kata against it.

Usage: python3 -I map.py <path to a clone of withmarbleapp/os-taxonomy> [--table]

The taxonomy is not vendored here. Clone it next to this file or anywhere else:
  git clone --depth 1 https://github.com/withmarbleapp/os-taxonomy

Every assignment below is a design choice for research, made 2026-10-17. The channel is the element and emotion the
topic mostly works (Sprout docs/design.md, the season table; "all" means it works every channel). The move is the Basic
Move it practises. The quadrant is the AQAL perspective it mostly asks for. None of them is a claim about a child.

Attribution: Marble Skill Taxonomy (v1), Generative Spark, Inc. (Marble), https://withmarble.com, ODbL 1.0 (database)
and CC BY-SA 4.0 (content). This file names topics by their title only.
"""
import json
import sys
from pathlib import Path

SUBJECT = "Personal & Social Development"

# name: (channel, basic move, quadrant)
TOPICS = {
    # Emotional Literacy
    "Naming Basic Emotions": ("all", "wake", "UL"),
    "Feelings Change and Differ": ("all", "wake", "UL"),
    "Triggers and Causes of Feelings": ("all", "wake", "UL"),
    "Expressing Feelings with Words": ("all", "show", "UR"),
    "Emotion Vocabulary": ("all", "grow", "UL"),
    "Hidden and Masked Feelings": ("metal", "clean", "LL"),
    "How Emotions Feel in Your Body": ("earth", "open", "UR"),
    "Mild to Strong Emotions": ("all", "grow", "UL"),
    "Culture and Experience Shape Emotions": ("all", "grow", "LL"),
    "Emotional Patterns Over Time": ("earth", "grow", "UL"),
    "Emotions and Decision-Making": ("metal", "clean", "UL"),
    "Mixed and Conflicting Emotions": ("all", "grow", "UL"),
    "Brain Science of Emotions": ("all", "grow", "UR"),
    "Identity and Belonging in Adolescence": ("water", "grow", "LL"),
    "Emotional Intelligence": ("all", "grow", "UL"),
    # Empathy & Social Awareness
    "Everyday Kindness and Care": ("water", "show", "LL"),
    "Other People's Feelings and Thoughts": ("all", "wake", "LL"),
    "Similarities & Differences": ("earth", "wake", "LL"),
    "Vocabulary: understanding others": ("all", "grow", "LL"),
    "Different Lives and Experiences": ("water", "grow", "LL"),
    "Fairness, Equality and Equity": ("fire", "grow", "LR"),
    "Seeing Someone Else's Point of View": ("earth", "grow", "LL"),
    "Vocabulary: social awareness": ("all", "grow", "LL"),
    "Prejudice and Discrimination": ("fire", "grow", "LR"),
    "Questioning Your Own Biases": ("metal", "clean", "UL"),
    "Stereotypes and Individual Differences": ("metal", "clean", "LL"),
    "The world contains many cultures, traditions": ("earth", "grow", "LL"),
    "Systemic Inequality and Allyship": ("fire", "show", "LR"),
    "Sympathy Versus Empathy": ("water", "grow", "LL"),
    "Global Citizenship": ("earth", "show", "LR"),
    # Friendship & Cooperation
    "Asking for Help": ("water", "show", "LL"),
    "Listening to Others": ("earth", "open", "LL"),
    "Makes someone a good friend": ("wood", "wake", "LL"),
    "Taking Turns and Sharing": ("wood", "show", "LL"),
    "Vocabulary: working with others": ("all", "grow", "LL"),
    "Communication Vocabulary": ("all", "grow", "LL"),
    "Friendships change over time": ("water", "grow", "LL"),
    "Resolving Disagreements with Friends": ("fire", "show", "LL"),
    "Roles in a Group": ("earth", "wake", "LR"),
    "Working Well in a Group": ("earth", "show", "LR"),
    "Assertive Communication": ("fire", "show", "UR"),
    "Giving and Receiving Feedback": ("metal", "show", "LL"),
    "Helping Others Resolve Conflicts": ("fire", "show", "LL"),
    "Self-Reflection in Relationships": ("all", "clean", "UL"),
    "Social Cues and Group Dynamics": ("metal", "grow", "LL"),
    "Honest Conversations and Conflict Repair": ("water", "show", "LL"),
    "Leadership Styles and Influence": ("fire", "grow", "LR"),
    # Responsible Decision-Making
    "Actions and Their Consequences": ("metal", "wake", "UR"),
    "Everyday Safety Awareness": ("metal", "wake", "UR"),
    "Right and Wrong Choices": ("metal", "wake", "UL"),
    "Rules and agreements exist": ("fire", "wake", "LR"),
    "Vocabulary: making decisions and keeping safe": ("all", "grow", "LR"),
    "Basic digital citizenship": ("metal", "grow", "LR"),
    "Bystanders and Upstanders": ("fire", "show", "LL"),
    "Stop, Think, Then Choose": ("earth", "clean", "UR"),
    "Understanding Bullying": ("fire", "wake", "LL"),
    "Vocabulary: ethics and citizenship": ("all", "grow", "LR"),
    "Community Rights and Responsibilities": ("earth", "grow", "LR"),
    "Difficult Ethical Choices": ("metal", "grow", "UL"),
    "Ethics in Real-World Issues": ("metal", "grow", "LR"),
    "Peer Pressure and Resisting It": ("fire", "show", "LL"),
    "Risk, Uncertainty, and Cognitive Bias": ("metal", "grow", "UL"),
    "Online Identity and Misinformation": ("metal", "grow", "LR"),
    "Ethical Frameworks and Moral Reasoning": ("metal", "grow", "UL"),
    # Self-Awareness
    "Naming Your Feelings": ("all", "wake", "UL"),
    "Vocabulary: self": ("all", "grow", "UL"),
    "Feelings Versus Actions": ("earth", "clean", "UL"),
    "Patterns in Your Own Reactions": ("all", "clean", "UL"),
    "Your Impact on Others": ("water", "clean", "LL"),
    "Questioning First Impressions": ("metal", "clean", "UL"),
    "Personal Growth Over Time": ("wood", "grow", "UL"),
    # Self-Regulation & Resilience
    "Coping with Life Changes": ("water", "open", "UL"),
    "Learning from Mistakes": ("metal", "clean", "UL"),
    "Patience and Delayed Gratification": ("wood", "clean", "UR"),
    "Simple Calming Strategies": ("earth", "open", "UR"),
    "Words for Big Feelings": ("all", "wake", "UL"),
    "Breaking Tasks into Steps": ("earth", "show", "UR"),
    "Choosing the Right Coping Strategy": ("all", "grow", "UL"),
    "Growth Mindset": ("wood", "grow", "UL"),
    "Positive Self-Talk": ("metal", "clean", "UL"),
    "Vocabulary: resilience and self": ("all", "grow", "UL"),
    "Personal Coping Toolkit": ("all", "grow", "UR"),
    "Personal Goal-Setting": ("fire", "show", "UR"),
    "Resilience and Bouncing Back": ("water", "grow", "UL"),
    "Time and Attention Management": ("earth", "show", "UR"),
    "Good Stress and Bad Stress": ("metal", "grow", "UR"),
    "Habits and Motivation": ("wood", "show", "UR"),
    "Growth Through Adversity": ("water", "grow", "UL"),
}

# Kata: (move id from bars-engine move-engine.ts, band, anchors). A band is the age range in which that form of the
# move is offered. Anchors are Marble topics the form practises; they may come from any subject.
KATA = [
    # Open Up is not one of the fifteen moves. Its breathing practice is WAVE, whose steps stay unspecified here.
    ("open_up", "5-7", ["Simple Calming Strategies"]),
    ("open_up", "7-9", ["How Emotions Feel in Your Body"]),
    # Transcend: one channel, dissatisfied toward satisfied.
    ("fire_transcend", "5-7", ["Naming Basic Emotions", "Expressing Feelings with Words", "Rules and agreements exist"]),
    ("fire_transcend", "7-9", ["Resolving Disagreements with Friends", "Understanding Bullying"]),
    ("fire_transcend", "9-11", ["Assertive Communication", "Peer Pressure and Resisting It"]),
    ("water_transcend", "5-7", ["Naming Basic Emotions", "Asking for Help", "Coping with Life Changes"]),
    ("water_transcend", "7-9", ["Friendships change over time"]),
    ("water_transcend", "9-11", ["Resilience and Bouncing Back"]),
    ("wood_transcend", "5-7", ["Patience and Delayed Gratification", "Persisting When It's Hard"]),
    ("wood_transcend", "7-9", ["Growth Mindset"]),
    ("wood_transcend", "9-11", ["Personal Growth Over Time"]),
    ("metal_transcend", "5-7", ["Naming Basic Emotions", "Everyday Safety Awareness"]),
    ("metal_transcend", "7-9", ["Actions and Their Consequences", "Feeling of not understanding"]),
    ("metal_transcend", "9-11", ["Questioning First Impressions"]),
    ("earth_transcend", "5-7", ["Simple Calming Strategies"]),
    ("earth_transcend", "7-9", ["How Emotions Feel in Your Body"]),
    ("earth_transcend", "9-11", ["Emotional Patterns Over Time"]),
    # Generative: one channel feeds the next (Wood, Fire, Earth, Metal, Water).
    ("wood_fire", "5-7", ["Expressing Feelings with Words"]),
    ("wood_fire", "7-9", ["Making a Simple Plan", "Planning a Task"]),
    ("wood_fire", "9-11", ["Personal Goal-Setting"]),
    ("fire_earth", "5-7", ["Expressing Feelings with Words"]),
    ("fire_earth", "7-9", ["Learning from Mistakes"]),
    ("fire_earth", "9-11", ["Reflecting After Learning"]),
    ("earth_metal", "7-9", ["Thinking Before Starting", "Stop, Think, Then Choose"]),
    ("earth_metal", "9-11", ["Difficult Ethical Choices"]),
    ("metal_water", "7-9", ["Right and Wrong Choices", "Understanding Why"]),
    ("metal_water", "9-11", ["Emotions and Decision-Making"]),
    ("water_wood", "7-9", ["Coping with Life Changes"]),
    ("water_wood", "9-11", ["Resilience and Bouncing Back"]),
    # Control: one channel checks the one it controls, at a cost that prevents a larger loss.
    ("wood_earth", "5-7", ["Patience and Delayed Gratification", "Taking Turns and Sharing"]),
    ("wood_earth", "7-9", ["Breaking Tasks into Steps"]),
    ("wood_earth", "9-11", ["Time and Attention Management"]),
    ("fire_metal", "5-7", ["Feelings Versus Actions"]),
    ("fire_metal", "7-9", ["Stop, Think, Then Choose"]),
    ("fire_metal", "9-11", ["Emotions and Decision-Making"]),
    ("earth_water", "7-9", ["Hidden and Masked Feelings"]),
    ("earth_water", "9-11", ["Self-Reflection in Relationships"]),
    ("metal_wood", "5-7", ["Persisting When It's Hard"]),
    ("metal_wood", "7-9", ["Positive Self-Talk", "Trying a New Approach"]),
    ("metal_wood", "9-11", ["Learning from Failure"]),
    ("water_fire", "7-9", ["Fairness, Equality and Equity", "Bystanders and Upstanders"]),
    ("water_fire", "9-11", ["Prejudice and Discrimination"]),
]


def band(b):
    lo, hi = b.split("-")
    return int(lo), int(hi)


def main():
    root = Path(sys.argv[1])
    topics = json.loads((root / "data/topics.json").read_text())["topics"]
    deps = json.loads((root / "data/dependencies.json").read_text())["dependencies"]
    by_id = {t["id"]: t for t in topics}
    by_name = {}
    for t in topics:
        by_name.setdefault(t["name"], []).append(t)
    failures = []

    psd = [t for t in topics if t["subject"] == SUBJECT]
    psd_names = {t["name"] for t in psd}
    for name in sorted(psd_names - TOPICS.keys()):
        failures.append(f"unmapped {SUBJECT} topic: {name}")
    for name in sorted(TOPICS.keys() - psd_names):
        failures.append(f"mapped name not in {SUBJECT}: {name}")

    def resolve(name):
        hits = by_name.get(name, [])
        psd_hits = [t for t in hits if t["subject"] == SUBJECT]
        return (psd_hits or hits or [None])[0]

    anchored = set()
    for move, b, anchors in KATA:
        lo, hi = band(b)
        for a in anchors:
            t = resolve(a)
            if t is None:
                failures.append(f"{move} {b}: anchor not in taxonomy: {a}")
                continue
            anchored.add(t["id"])
            # A form is offered no earlier than Marble places the idea it practises.
            if t["ageRangeStart"] >= hi:
                failures.append(f"{move} {b}: {a} starts at {t['ageRangeStart']}, after the band")

    # A hard prerequisite of an anchor should not belong to a later band of the same move.
    first_band = {}
    for move, b, anchors in KATA:
        for a in anchors:
            t = resolve(a)
            if t:
                first_band.setdefault((move, t["id"]), band(b)[0])
    for (move, tid), lo in first_band.items():
        for d in deps:
            if d["topicId"] == tid and d["strength"] == "hard":
                later = first_band.get((move, d["prerequisiteId"]))
                if later is not None and later > lo:
                    failures.append(f"{move}: {by_id[tid]['name']} at {lo} needs {by_id[d['prerequisiteId']]['name']} at {later}")

    counts = {}
    for name, (ch, mv, q) in TOPICS.items():
        for key in (("channel", ch), ("move", mv), ("quadrant", q)):
            counts[key] = counts.get(key, 0) + 1
    print(f"{len(TOPICS)} topics mapped, {len(KATA)} kata, {len(anchored)} distinct anchor topics")
    for axis in ("channel", "move", "quadrant"):
        row = sorted((k[1], v) for k, v in counts.items() if k[0] == axis)
        print(f"  {axis}: " + ", ".join(f"{k} {v}" for k, v in row))
    unused = sorted(n for n in TOPICS if resolve(n)["id"] not in anchored)
    print(f"  mapped topics no kata anchors yet: {len(unused)}")

    if "--table" in sys.argv:
        for name, (ch, mv, q) in sorted(TOPICS.items(), key=lambda kv: (resolve(kv[0])["domain"], resolve(kv[0])["ageRangeStart"])):
            t = resolve(name)
            print(f"| {t['domain']} | {name} | {t['ageRangeStart']}-{t['ageRangeEnd']} | {ch} | {mv} | {q} |")

    for f in failures:
        print("FAIL", f)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
