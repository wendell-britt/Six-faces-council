"""Pass ttv-loop 1: Lens goals emerge only from lines that return across mornings, the free writes stay out of the
repo, and an intake item can join work already happening or have no home yet."""
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "council"))


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "council" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


emerge = load("lens_emerge")
intake = load("intake_align")
lens_goals = load("lens_goals")

HIST = {"version": 1, "since": "2026-07-18", "days": [
    {"date": "2026-10-10", "freewrite": "The book keeps calling.\nI want it in people's hands.", "wordCount": 10,
     "seeds": [{"id": "t1", "status": "completed", "maturity": "shared_or_acted"}]},
    {"date": "2026-10-14", "freewrite": "Again the book. I want it   in people's hands by spring.", "wordCount": 11,
     "seeds": [{"id": "t2", "status": "composted", "maturity": None}]},
]}
GOOD = {"title": "Put the book in people's hands", "domain": "career", "why": "It returns on both mornings unprompted.",
        "lines": [{"date": "2026-10-10", "line": "I want it in people's hands."},
                  {"date": "2026-10-14", "line": "I want it in people's hands by spring."}]}


class LensEmergeTest(unittest.TestCase):
    def test_a_goal_that_returns_stands(self):
        self.assertEqual(emerge.check(HIST, [GOOD]), [])

    def test_one_morning_is_not_emergence(self):
        one = dict(GOOD, lines=GOOD["lines"][:1])
        self.assertTrue(any("returns on two or more" in b for b in emerge.check(HIST, [one])))

    def test_his_exact_words_only(self):
        bent = dict(GOOD, lines=[GOOD["lines"][0], {"date": "2026-10-14", "line": "I need the book out."}])
        self.assertTrue(any("word for word" in b for b in emerge.check(HIST, [bent])))

    def test_domain_and_cap(self):
        self.assertTrue(emerge.check(HIST, [dict(GOOD, domain="fame")]))
        self.assertTrue(any("at most" in b for b in emerge.check(HIST, [GOOD] * 6)))

    def test_rows_are_what_lens_goals_kept_sends(self):
        row = emerge.pitch_rows(HIST, [GOOD])[0]
        self.assertEqual(row["id"], "lens-emerge-2026-10-14-1")
        self.assertIn("2026-10-10:", row["why_you"])
        data = {"questions": [row], "resolved": {"questions": {row["id"]: {"decision": "keep"}}}}
        self.assertEqual(lens_goals.kept(data)[0]["title"], GOOD["title"])

    def test_history_never_lands_in_the_repo(self):
        with self.assertRaises(SystemExit):
            emerge.fetch(ROOT / "vein.json")

    def test_summary_counts_seeds(self):
        self.assertIn("2 seeds", emerge.summary(HIST))


class IntakeToWorkTest(unittest.TestCase):
    MENU = {"sessionDate": "2026-10-16", "items": [{"key": "c1", "text": "Fix the Morning tab"},
                                                    {"key": "c2", "text": "Walk by the river"}]}

    def test_strand_and_no_home_yet(self):
        aligns = [{"line": "Fix the Morning tab", "strand": "morning-menu", "why": "This is the morning menu strand's work."},
                  {"line": "Walk by the river", "none": True, "why": "Rest; no goal or strand needs it."}]
        out, pitches, bad = intake.align(self.MENU, aligns, {"morning": {"goals": []}})
        self.assertEqual(bad, [])
        self.assertEqual(out["items"][0]["bridge"]["kind"], "strand")
        self.assertEqual(out["items"][0]["bridge"]["strand"], "morning-menu")
        self.assertEqual(out["items"][1]["bridge"]["kind"], "none")
        self.assertEqual(pitches, [])

    def test_unknown_strand_is_refused(self):
        aligns = [{"line": "Fix the Morning tab", "strand": "../HANDOFF", "why": "four words or more here"},
                  {"line": "Walk by the river", "none": True, "why": "Rest; no goal or strand needs it."}]
        _, _, bad = intake.align(self.MENU, aligns, {"morning": {"goals": []}})
        self.assertTrue(any("no call sheet" in b for b in bad))

    def test_strand_carries_its_kept_lens(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "demo.md").write_text("2026-10-16\n# Demo strand\nlens: g1\n", encoding="utf-8")
            old, intake.CALLSHEETS = intake.CALLSHEETS, Path(d)
            try:
                st = intake.strand("demo", {"g1": {"id": "g1", "title": "Ship the demo"}})
            finally:
                intake.CALLSHEETS = old
        self.assertEqual(st["goalTitle"], "Ship the demo")
        self.assertEqual(st["strandTitle"], "Demo strand")


if __name__ == "__main__":
    unittest.main()
