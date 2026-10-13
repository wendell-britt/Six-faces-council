"""Tests for council/morning.py, which gathers the morning menu as separate categories, each item bridged to a goal.

Steers of 2026-10-09: mm-backlog-sources ("separate categories people can explore") and mm-menu-shape ("All items need
a bridge to lens goals"). mm-raw: only kept lines leave Tap the Vein.

Run: python3 -m unittest discover -s tests
"""
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "council"))
spec = importlib.util.spec_from_file_location("morning", ROOT / "council/morning.py")
morning = importlib.util.module_from_spec(spec)
spec.loader.exec_module(morning)

MENU = json.loads((ROOT / "docs/morning-menu.example.json").read_text())
GOALS = MENU["goals"]
DATA = {"questions": [{"id": "q-open", "q": "Where do you write?", "pass": "p1"}, {"id": "q-done", "q": "x"}],
        "positions": [], "resolved": {"questions": {"q-done": {"decision": "a"}}, "positions": {}}}


class MorningTest(unittest.TestCase):
    def test_named_goal_wins(self):
        b = morning.bridge("anything at all", GOALS, "g-q-podcast")
        self.assertEqual((b["kind"], b["goalTitle"]), ("named", "Publish twelve podcast episodes"))

    def test_shared_words_suggest_existing_goal(self):
        self.assertEqual(morning.bridge("Record two podcast episodes", GOALS)["goalId"], "g-q-podcast")

    def test_one_shared_word_suggests_smaller_goal_under_year_goal(self):
        b = morning.bridge("Book the allyship venue", GOALS)
        self.assertEqual((b["kind"], b["parentId"], b["cadence"]), ("new", "g-year-allyship", "quarter"))

    def test_no_goals_means_unaligned_with_reason(self):
        b = morning.bridge("Post the clips", [])
        self.assertEqual(b["kind"], "unaligned")
        self.assertIn("no Lens goals", b["why"])

    def test_goals_come_from_bridged_items_without_a_goals_list(self):
        bare = {k: v for k, v in MENU.items() if k != "goals"}
        self.assertEqual([g["id"] for g in morning.menu_goals(bare)], ["g-q-podcast"])

    def test_menu_pasted_on_the_board_is_read(self):
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
            json.dump({"menu": json.dumps(MENU), "savedAt": "2026-10-09T16:00:00Z"}, f)
        self.assertEqual(morning.load_menu(f.name)["sessionDate"], "2026-10-09")

    def test_categories_stay_separate_and_unaligned_last(self):
        morning.from_prs = lambda path=None: ([], None)  # no network in tests
        m = morning.gather(MENU, prs_file=None, bars="/nonexistent", data=DATA)
        keys = [c["key"] for c in m["categories"]]
        self.assertEqual(keys, ["menu", "board", "due", "handoff", "prs", "backlog"])
        menu = m["categories"][0]["items"]
        self.assertEqual(menu[0]["bridge"]["kind"], "named")
        self.assertEqual(menu[-1]["bridge"]["kind"], "unaligned")
        self.assertEqual(menu[1]["bridge"]["kind"], "unaligned", "a suggestion he never accepted stays unaligned")
        board = m["categories"][1]["items"]
        self.assertEqual([i["ref"] for i in board], ["q-open"])
        self.assertEqual(m["pick_limit"], 7)


if __name__ == "__main__":
    unittest.main()
