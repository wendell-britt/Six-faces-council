"""Tests for board/pull.py, which records Wendell's saved board answers on main without a board read.

pull.py replaced the Send button as the way a save reaches main (pickup-pull-model, 2026-10-07). It must record each
save once, catch a flip he makes after a save was recorded, and record the same thing however often it runs.

Run: python3 -m unittest discover -s tests
"""
import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("pull", ROOT / "board/pull.py")
pull = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pull)

DATA = {
    "updated": "2026-10-06",
    "positions": [{"id": "p-old"}, {"id": "p-new", "faces": ["architect", "sage"], "pass": "pass 13"}],
    "questions": [{"id": "q-one", "options": [{"v": "a", "label": "A. Apples (recommended)"},
                                              {"v": "b", "label": "B. Bananas"}]},
                  {"id": "q-many", "options": [{"v": "x", "label": "Wonder"}, {"v": "y", "label": "Bliss"}]},
                  {"id": "q-later", "options": [{"v": "a", "label": "A. Now"}]}],
    "terms": [], "causes": [],
    "resolved": {"positions": {"p-old": {"decision": "stands", "recorded": "2026-10-05", "record": "x"}},
                 "questions": {}, "terms": {}, "causes": {}},
    "steers_recorded": [], "steer_recorded_through": "2026-10-06T00:00:00Z",
}


class PullTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.store = Path(self.tmp.name)
        self.data = copy.deepcopy(DATA)

    def tearDown(self):
        self.tmp.cleanup()

    def save(self, kind, rid, doc):
        d = self.store / kind
        d.mkdir(exist_ok=True)
        (d / f"{rid}.json").write_text(json.dumps(doc))

    def pull(self):
        new, general, steps = pull.find_new(self.data, self.store)
        if new or general or steps:
            return pull.apply(self.data, new, general, steps, "council/ledger/t.json")
        return None

    def test_old_save_already_recorded_is_skipped(self):
        self.save("positions", "p-old", {"status": "stands", "savedAt": "2026-10-05T10:00:00Z"})
        self.assertIsNone(self.pull())

    def test_new_save_recorded_once(self):
        self.save("positions", "p-new", {"status": "overrule", "steer": "try trigrams", "savedAt": "2026-10-07T10:00:00Z"})
        led = self.pull()
        e = self.data["resolved"]["positions"]["p-new"]
        self.assertEqual((e["decision"], e["label"], e["steer"]), ("overrule", "Overruled", "try trigrams"))
        self.assertIn("p-new", led["answers"])
        self.assertTrue(any("p-new" in w for w in led["needs_work"]))
        self.assertIsNone(self.pull(), "a second run must find nothing")

    def test_resolved_entry_carries_faces_and_pass(self):
        # proc-record-face, 2026-10-07: an overrule must be traceable to the face that made the position
        self.save("positions", "p-new", {"status": "overrule", "savedAt": "2026-10-07T10:00:00Z"})
        self.pull()
        e = self.data["resolved"]["positions"]["p-new"]
        self.assertEqual((e["faces"], e["pass"]), (["architect", "sage"], "pass 13"))

    def test_flip_after_recording_is_caught(self):
        self.save("positions", "p-old", {"status": "overrule", "savedAt": "2026-10-07T09:00:00Z"})
        self.pull()
        self.assertEqual(self.data["resolved"]["positions"]["p-old"]["decision"], "overrule")
        self.save("positions", "p-old", {"status": "stands", "savedAt": "2026-10-07T11:00:00Z"})
        self.pull()
        self.assertEqual(self.data["resolved"]["positions"]["p-old"]["decision"], "stands")

    def test_morning_pick_recorded_once_as_work(self):
        # mm-picks-become-threads: a pick is one row marked as his, and the next read starts one thread for it
        self.save("picks", "menu-l1", {"text": "Post the clips", "category": "menu", "date": "2026-10-09",
                                       "bridge": {"kind": "named", "goalTitle": "Publish podcasts"},
                                       "savedAt": "2026-10-09T15:00:00Z"})
        self.save("picks", "menu-l2", {"text": "Dropped", "removed": True, "savedAt": "2026-10-09T15:01:00Z"})
        led = self.pull()
        self.assertEqual([p["id"] for p in self.data["picks"]], ["menu-l1"])
        self.assertTrue(any(w.startswith("picks/menu-l1: start a thread") and "Publish podcasts" in w
                            for w in led["needs_work"]))
        self.assertIsNone(self.pull(), "a second run must find nothing")

    def test_pasted_menu_flagged_until_gathered(self):
        self.save("morning", "menu", {"menu": "{}", "savedAt": "2026-10-09T16:00:00Z"})
        self.assertIsNotNone(pull.pasted_menu(self.data, self.store))
        self.data["morning"] = {"gathered_at": "2026-10-09T16:05:00Z"}
        self.assertIsNone(pull.pasted_menu(self.data, self.store))

    def test_question_labels(self):
        self.save("questions", "q-one", {"choice": "a", "savedAt": "2026-10-07T10:00:00Z"})
        self.save("questions", "q-many", {"choice": "x", "choices": ["x", "y"], "savedAt": "2026-10-07T10:01:00Z"})
        self.pull()
        q = self.data["resolved"]["questions"]
        self.assertEqual(q["q-one"]["label"], "Apples")
        self.assertEqual((q["q-many"]["decision"], q["q-many"]["label"]), ("x, y", "Wonder and Bliss"))

    def test_deferral_uses_the_ladder(self):
        self.save("questions", "q-later", {"deferred": True, "until": "week", "steer": "", "savedAt": "2026-10-07T10:00:00Z"})
        self.pull()
        e = self.data["resolved"]["questions"]["q-later"]
        self.assertEqual(e["decision"], "deferred")
        self.assertTrue(e["until"].startswith("2026-10-14"))
        self.assertIsNone(self.pull())

    def test_general_steer(self):
        self.save("positions", "p-old", {"status": "stands", "savedAt": "2026-10-05T10:00:00Z"})
        (self.store / "steer").mkdir()
        (self.store / "steer" / "general.json").write_text(json.dumps({"text": "more tea", "savedAt": "2026-10-07T12:00:00Z"}))
        self.pull()
        self.assertEqual(self.data["steers_recorded"][-1]["text"], "more tea")
        self.assertIsNone(self.pull())

    def test_two_runs_write_the_same_ledger(self):
        self.save("positions", "p-new", {"status": "stands", "savedAt": "2026-10-07T10:00:00Z"})
        first = self.pull()
        self.data = copy.deepcopy(DATA)
        self.assertEqual(first, self.pull())

    def test_step_note_and_move_need_work_once(self):
        # The 18:40 Send of 2026-10-12 carried only step notes, and pull.py never read the steps collection.
        self.save("steps", "gs-1", {"do": "Do it", "note": "need step by step", "noteAt": "2026-10-12T16:52:00Z",
                                    "done": True, "doneAt": "2026-10-12T16:53:00Z",
                                    "moved": [{"from": "2026-10-08", "to": "2026-10-14", "at": "2026-10-12T16:26:00Z"}]})
        self.save("steps", "gs-old", {"note": "read by hand", "noteAt": "2026-10-07T10:00:00Z"})
        led = self.pull()
        self.assertEqual([e["what"] for e in led["steps"]], ["moved", "note", "ticked"])
        self.assertIn('steps/gs-1: note "need step by step"', led["needs_work"])
        self.assertIn("steps/gs-1: moved from 2026-10-08 to 2026-10-14", led["needs_work"])
        self.assertEqual(self.data["steps_recorded_through"], "2026-10-12T16:53:00Z")
        self.assertIsNone(self.pull())


if __name__ == "__main__":
    unittest.main()


class BlockerTest(unittest.TestCase):
    """The overdue card's blocker panel (2026-10-12): each run reaches main once, and a later save of it replaces it."""
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.store = Path(self.tmp.name) / "store"
        (self.store / "blockers").mkdir(parents=True)
        self.main = Path(self.tmp.name) / "blockers"
        self.was, pull.BLOCKERS = pull.BLOCKERS, self.main

    def tearDown(self):
        pull.BLOCKERS = self.was
        self.tmp.cleanup()

    def run_doc(self, saved, **extra):
        doc = {"step": "s1", "task": "Add the env var", "savedAt": saved, "status": "resolved", "stage": "done",
               "charge": {"before": 7, "after": 3}, "rounds": [{"name": "dread"}, {"name": "guard"}],
               "resolution": {"kind": "change", "text": "add a rollback line"}, **extra}
        (self.store / "blockers" / "s1--a.json").write_text(json.dumps(doc))

    def test_run_recorded_once_with_a_needs_work_line(self):
        self.run_doc("2026-10-12T17:00:00Z")
        found = pull.find_blockers(self.store)
        self.assertEqual([b["id"] for b in found], ["s1--a"])
        self.assertEqual(pull.blocker_line(found[0]), 'blockers/s1--a: Add the env var (dread, guard; the step needs '
                                                        'changing: "add a rollback line", charge 7 to 3)')
        self.main.mkdir()
        (self.main / "s1--a.json").write_text(json.dumps(found[0]["doc"]))
        self.assertEqual(pull.find_blockers(self.store), [])
        self.run_doc("2026-10-12T18:00:00Z")
        self.assertEqual(len(pull.find_blockers(self.store)), 1)

    def test_run_left_half_way_says_where(self):
        self.run_doc("2026-10-12T17:00:00Z", status="open", stage="validate", resolution=None, charge={"before": 5})
        self.assertIn("left at validate", pull.blocker_line(pull.find_blockers(self.store)[0]))

    def test_no_blockers_folder_is_fine(self):
        (self.store / "blockers").rmdir()
        self.assertEqual(pull.find_blockers(self.store), [])
