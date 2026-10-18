"""council/daemons/questions.yaml: Wendell's question sets for the daemons (2026-10-14).

Every daemon in daemons.yaml has a set, every question sits in a known slot, and the shared skeleton holds: each set
asks what it works on and what would happen without it, and each daemon but the Protector and the Player asks who it
works for.
"""
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SLOTS = {"object", "boss", "method", "stakes", "vulnerable_to", "violated", "measure", "advocates_for", "payoff",
         "source", "growth", "blocked_by"}


class DaemonQuestions(unittest.TestCase):
    def setUp(self):
        self.q = yaml.safe_load((ROOT / "council/daemons/questions.yaml").read_text())
        self.sets = {d["id"]: d for d in self.q["daemons"]}

    def test_every_daemon_has_a_set(self):
        known = {d["id"] for d in yaml.safe_load((ROOT / "council/daemons/daemons.yaml").read_text())["daemons"]}
        self.assertEqual(set(self.sets), known)

    def test_slots_and_skeleton(self):
        for did, d in self.sets.items():
            slots = [q["slot"] for q in d["questions"]]
            self.assertTrue(set(slots) <= SLOTS, did)
            self.assertIn("object", slots, did)
            self.assertIn("stakes", slots, did)
            if did not in ("protector", "player"):
                self.assertIn("boss", slots, did)
            ids = [q["id"] for q in d["questions"]]
            self.assertEqual(len(ids), len(set(ids)), did)
            for q in d["questions"]:
                self.assertTrue(q["words"].strip() and q["ask"].strip(), (did, q["id"]))
                for boss in q.get("by_boss") or {}:
                    self.assertIn(boss, self.q["bosses"], (did, q["id"]))


if __name__ == "__main__":
    unittest.main()
