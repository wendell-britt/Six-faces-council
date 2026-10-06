"""Regression tests for the two pieces of code that merge board rows from different sessions.

A row lost in a merge is one of Wendell's answers or steers gone from the board. On 2026-10-04 that happened twice:
a live page one publish behind replaced a battle's rounds whole (fixed in 43bd364), and then replaced
steers_recorded whole, dropping three of his round 2 steers (40425d1, fixed in 97cff4c). These tests pin both fixes
and the merge driver's rules, so a later change to either file cannot drop a row unnoticed.

Run: python3 -m unittest discover -s tests
"""
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


sync = load("sync_board", "board/sync_board.py")
driver = load("board_merge", "council/tools/board_merge.py")


def row(rid, **kw):
    return {"id": rid, "pos": f"text of {rid}", **kw}


class SyncUnion(unittest.TestCase):
    """board/sync_board.py: main plus everything on the live page, nothing removed."""

    def merged(self, main, live):
        report = []
        return sync.union(main, live, report), report

    def test_rows_on_either_side_are_kept(self):
        out, _ = self.merged({"positions": [row("a")]}, {"positions": [row("b")]})
        self.assertEqual([r["id"] for r in out["positions"]], ["a", "b"])

    def test_live_wins_where_both_have_a_row(self):
        out, report = self.merged({"positions": [row("a")]}, {"positions": [row("a", pos="newer")]})
        self.assertEqual(out["positions"], [row("a", pos="newer")])
        self.assertIn("from live: positions a (changed)", report)

    def test_battle_keeps_every_round_by_number(self):
        main = {"battles": [{"id": "fr-x", "rounds": [{"n": 1}, {"n": 2, "q": "main"}]}]}
        live = {"battles": [{"id": "fr-x", "rounds": [{"n": 1}, {"n": 3}]}]}
        out, _ = self.merged(main, live)
        self.assertEqual([r["n"] for r in out["battles"][0]["rounds"]], [1, 2, 3])

    def test_steers_without_ids_keep_mains_entries(self):
        main = {"steers_recorded": ["s1", "s2", "s3"]}
        live = {"steers_recorded": ["s1", "s4"]}
        out, _ = self.merged(main, live)
        self.assertEqual(out["steers_recorded"], ["s1", "s2", "s3", "s4"])

    def test_resolved_entries_from_both_sides_survive(self):
        main = {"resolved": {"positions": {"a": {"decision": "stands"}}}}
        live = {"resolved": {"positions": {"b": {"decision": "overrule"}}}}
        out, _ = self.merged(main, live)
        self.assertEqual(set(out["resolved"]["positions"]), {"a", "b"})

    def test_updated_takes_the_later_date(self):
        out, _ = self.merged({"updated": "2026-10-05"}, {"updated": "2026-10-04"})
        self.assertEqual(out["updated"], "2026-10-05")

    def test_main_is_not_changed_in_place(self):
        main = {"positions": [row("a")]}
        before = json.dumps(main)
        self.merged(main, {"positions": [row("a", pos="x"), row("b")]})
        self.assertEqual(json.dumps(main), before)


class MergeDriver(unittest.TestCase):
    """council/tools/board_merge.py: git's three-way merge for board_data.json, by meaning."""

    def merged(self, base, ours, theirs):
        conflicts = []
        return driver.merge(base, ours, theirs, "$", conflicts), conflicts

    def test_two_branches_adding_different_rows_keep_both(self):
        base = {"positions": [row("a")]}
        out, conflicts = self.merged(base, {"positions": [row("a"), row("ours")]},
                                     {"positions": [row("a"), row("theirs")]})
        self.assertEqual(conflicts, [])
        self.assertEqual([r["id"] for r in out["positions"]], ["a", "theirs", "ours"])

    def test_two_branches_resolving_different_rows_keep_both(self):
        base = {"resolved": {"positions": {}}}
        out, conflicts = self.merged(base, {"resolved": {"positions": {"a": {"decision": "stands"}}}},
                                     {"resolved": {"positions": {"b": {"decision": "stands"}}}})
        self.assertEqual(conflicts, [])
        self.assertEqual(set(out["resolved"]["positions"]), {"a", "b"})

    def test_lists_without_ids_keep_both_sides_entries(self):
        base = {"steers_recorded": ["s1"]}
        out, conflicts = self.merged(base, {"steers_recorded": ["s1", "s2"]}, {"steers_recorded": ["s1", "s3"]})
        self.assertEqual(conflicts, [])
        self.assertEqual(sorted(out["steers_recorded"]), ["s1", "s2", "s3"])

    def test_same_field_changed_two_ways_is_a_conflict(self):
        base = {"positions": [row("a")]}
        _, conflicts = self.merged(base, {"positions": [row("a", pos="ours")]},
                                   {"positions": [row("a", pos="theirs")]})
        self.assertEqual(len(conflicts), 1)

    def test_updated_takes_the_later_date(self):
        out, conflicts = self.merged({"updated": "2026-10-03"}, {"updated": "2026-10-05"}, {"updated": "2026-10-04"})
        self.assertEqual((out["updated"], conflicts), ("2026-10-05", []))


if __name__ == "__main__":
    unittest.main()
