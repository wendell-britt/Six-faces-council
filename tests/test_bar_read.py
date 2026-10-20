"""Pass ttv-bars 1: each sealed line is read as a BAR, its context gathered from the record before it meets council work,
and the face-off's factors are shown apart with a call that is only advice."""
import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "council"))
FIX = ROOT / "tests" / "fixtures" / "bar-read"


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "council" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


bar_read = load("bar_read")
MENU = json.loads((FIX / "menu.json").read_text(encoding="utf-8"))
HIST = json.loads((FIX / "history.json").read_text(encoding="utf-8"))
READS = json.loads((FIX / "reads.json").read_text(encoding="utf-8"))
DATA = json.loads((ROOT / "board" / "board_data.json").read_text(encoding="utf-8"))
WORK = [{"key": "SAMPLE#questions/x", "what": "Record the sample answer"}]


def run(reads=None, work=None, hist=HIST):
    return bar_read.check(MENU, reads if reads is not None else READS, DATA, hist, WORK if work is None else work)


def edit(i, **kw):
    reads = copy.deepcopy(READS)
    reads[i].update(kw)
    return reads


class BarReadTest(unittest.TestCase):
    def test_five_lines_give_five_checked_reads(self):
        intake, _, bad = run()
        self.assertEqual(bad, [])
        self.assertEqual(len(intake["items"]), 5)
        self.assertTrue(all("read" in it and "bridge" in it for it in intake["items"]))
        calls = [it["read"]["call"] for it in intake["items"]]
        self.assertEqual(calls, ["work-today", "join", "defer", "work-today", "defer"])

    def test_his_line_stays_word_for_word_with_its_task_and_bar(self):
        intake, _, _ = run()
        first = intake["items"][0]
        self.assertEqual(first["text"], MENU["items"][0]["text"])
        self.assertEqual((first["read"]["taskId"], first["read"]["barId"]), ("t-a1", "b-a1"))
        _, _, bad = run(edit(0, line="Write the first page of the video script"))
        self.assertTrue(any("word for word" in b for b in bad))

    def test_signal_comes_from_his_record(self):
        intake, _, _ = run()
        ari = intake["items"][2]["read"]
        self.assertEqual(ari["factors"]["signal"]["carryCount"], 2)
        self.assertEqual(ari["factors"]["signal"]["chargeLevel"], "high")
        self.assertFalse(ari["factors"]["signal"]["wroteToday"])
        self.assertEqual(ari["factors"]["signal"]["firstDay"], "2026-10-18")
        self.assertEqual(ari["factors"]["ready"]["notes"], 2)
        self.assertNotIn("notes", ari["factors"]["signal"])

    def test_what_the_record_fills_and_what_stays_missing(self):
        intake, _, _ = run()
        self.assertIs(intake["items"][0]["read"]["workable"], True)
        self.assertEqual(intake["items"][2]["read"]["workable"], ["blocker"])

    def test_a_blocked_task_lists_its_blocker(self):
        _, _, bad = run(edit(2, missing=["input"]))
        self.assertTrue(any("marked blocked" in b for b in bad))

    def test_no_home_yet_means_home_is_missing(self):
        _, _, bad = run(edit(4, missing=["next step"]))
        self.assertTrue(any("home is missing" in b for b in bad))

    def test_missing_comes_from_the_fixed_list(self):
        _, _, bad = run(edit(4, missing=["home", "motivation"]))
        self.assertTrue(any("missing comes from" in b for b in bad))

    def test_gathered_needs_a_real_source(self):
        g = [{"piece": "input", "found": "Someone said the link exists somewhere.", "source": "memory"}]
        _, _, bad = run(edit(2, gathered=g))
        self.assertTrue(any("needs a source" in b for b in bad))
        g = [{"piece": "input", "found": "The Between is live and the link is his.", "source": "row:no-such-row"}]
        _, _, bad = run(edit(2, gathered=g))
        self.assertTrue(any("no board row" in b for b in bad))

    def test_work_today_needs_a_workable_line(self):
        _, _, bad = run(edit(2, call="work-today", decided_by="signal"))
        self.assertTrue(any("work today needs a workable line" in b for b in bad))

    def test_the_factors_are_never_summed(self):
        reads = copy.deepcopy(READS)
        reads[0]["factors"]["score"] = 7
        _, _, bad = run(reads)
        self.assertTrue(any("never summed" in b for b in bad))

    def test_the_call_names_one_factor(self):
        _, _, bad = run(edit(0, decided_by="vibes"))
        self.assertTrue(any("decided_by" in b for b in bad))

    def test_a_loss_speaks_about_conditions_never_about_him(self):
        _, _, bad = run(edit(2, why="He keeps avoiding this call, so rest it again."))
        self.assertTrue(any("tb-loss-not-avoidance" in b for b in bad))

    def test_the_kernel_is_the_face_s_words(self):
        _, _, bad = run(edit(3, kernel=MENU["items"][3]["text"]))
        self.assertTrue(any("kernel" in b for b in bad))

    def test_the_opponent_shares_the_line_s_area(self):
        reads = copy.deepcopy(READS)
        reads[0]["opponent"] = {"kind": "strand", "ref": "podcast", "what": "episode two publishing steps"}
        _, _, bad = run(reads)
        self.assertTrue(any("its opponent is that work" in b for b in bad))

    def test_with_no_shared_area_needs_work_comes_before_a_call_sheet(self):
        reads = copy.deepcopy(READS)
        reads[4]["opponent"] = {"kind": "callsheet", "ref": "podcast", "what": "episode two publishing steps"}
        _, _, bad = run(reads)
        self.assertTrue(any("needs_work.py" in b for b in bad))
        _, _, bad = run(reads, work=[])
        self.assertEqual(bad, [])

    def test_every_line_gets_a_read(self):
        _, _, bad = run(READS[:4])
        self.assertTrue(any("no alignment for" in b for b in bad))


if __name__ == "__main__":
    unittest.main()
