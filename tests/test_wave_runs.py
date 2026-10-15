"""Tests for council/wave_runs.py, which brings the board's WAVE room runs back from bars-engine (ttv-skip-wave).

Run: python3 -m unittest discover -s tests
"""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("wave_runs", ROOT / "council/wave_runs.py")
wave_runs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wave_runs)

RUN = {"engine": "wave-room", "version": 1, "savedAt": "2026-10-14T21:30:00.000Z", "status": "resolved", "stage": "end",
       "task": "Tap the Vein, skipped 2 days running", "rounds": [{"name": "dread"}],
       "resolution": {"kind": "now", "text": "open the page"}, "charge": {"before": 7, "after": 3}}


class WaveRunsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.store = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_writes_a_new_run_where_pull_reads_blockers(self):
        wrote = wave_runs.place([{"ref": "tap-the-vein--abc", "record": RUN}], self.store)
        self.assertEqual(wrote, ["tap-the-vein--abc"])
        doc = json.loads((self.store / "blockers" / "tap-the-vein--abc.json").read_text())
        self.assertEqual(doc["engine"], "wave-room")

    def test_keeps_a_newer_save_already_in_the_store(self):
        (self.store / "blockers").mkdir()
        newer = dict(RUN, savedAt="2026-10-14T22:00:00.000Z")
        (self.store / "blockers" / "tap-the-vein--abc.json").write_text(json.dumps(newer))
        self.assertEqual(wave_runs.place([{"ref": "tap-the-vein--abc", "record": RUN}], self.store), [])
        later = dict(RUN, savedAt="2026-10-14T23:00:00.000Z")
        self.assertEqual(wave_runs.place([{"ref": "tap-the-vein--abc", "record": later}], self.store), ["tap-the-vein--abc"])

    def test_refuses_bad_refs_and_other_engines(self):
        runs = [{"ref": "../x", "record": RUN}, {"ref": "x", "record": dict(RUN, engine="board-wave")},
                {"ref": "y", "record": dict(RUN, savedAt="")}]
        self.assertEqual(wave_runs.place(runs, self.store), [])

    def test_dry_writes_nothing(self):
        self.assertEqual(wave_runs.place([{"ref": "a", "record": RUN}], self.store, dry=True), ["a"])
        self.assertFalse((self.store / "blockers").exists())

    def test_pull_reads_a_placed_run_as_a_blocker(self):
        spec2 = importlib.util.spec_from_file_location("pull", ROOT / "board/pull.py")
        pull = importlib.util.module_from_spec(spec2)
        spec2.loader.exec_module(pull)
        wave_runs.place([{"ref": "tap-the-vein--zzz-test", "record": RUN}], self.store)
        found = [b for b in pull.find_blockers(self.store) if b["id"] == "tap-the-vein--zzz-test"]
        self.assertEqual(len(found), 1)
        self.assertIn("dread", pull.blocker_line(found[0]))


if __name__ == "__main__":
    unittest.main()
