"""tb-lists-are-bars: the council's own lists on the Morning tab are read as BARs too, a few a morning on the seed
library's ladder, and a pick carries the faces' read into the thread it starts."""
import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "council"))
sys.path.insert(0, str(ROOT / "board"))
FIX = ROOT / "tests" / "fixtures" / "bar-read"


def load(name, where="council"):
    spec = importlib.util.spec_from_file_location(name, ROOT / where / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


bar_read = load("bar_read")
pull = load("pull", "board")
MENU = json.loads((FIX / "menu.json").read_text(encoding="utf-8"))
HIST = json.loads((FIX / "history.json").read_text(encoding="utf-8"))
READS = json.loads((FIX / "reads.json").read_text(encoding="utf-8"))
LIST_READS = json.loads((FIX / "list-reads.json").read_text(encoding="utf-8"))
BASE = json.loads((ROOT / "board" / "board_data.json").read_text(encoding="utf-8"))
TODAY = "2026-10-20"
LINES = [r["line"] for r in READS]


def data():
    d = copy.deepcopy(BASE)
    d["morning"] = json.loads((FIX / "morning.json").read_text(encoding="utf-8"))
    d["picks"], d["list_reads"] = [], {}
    return d


def run(reads=None, d=None):
    return bar_read.check_items(LIST_READS if reads is None else reads, d or data(), work=[], lines=LINES, today=TODAY)


def edit(i, **kw):
    reads = copy.deepcopy(LIST_READS)
    reads[i].update(kw)
    return reads


class SlateTest(unittest.TestCase):
    def test_a_few_from_each_list_never_read_first(self):
        s = bar_read.slate(data(), per=2, today=TODAY)
        by = {}
        for e in s:
            by.setdefault(e["list"], []).append(e["item"])
        self.assertEqual(set(by), {"handoff", "prs", "backlog"})
        self.assertTrue(all(len(v) <= 2 for v in by.values()))
        self.assertEqual(by["handoff"], ["handoff-a", "handoff-b"])

    def test_a_picked_item_is_his_and_a_resting_one_waits_for_its_rung(self):
        d = data()
        d["picks"] = [{"id": "handoff-a"}]
        d["list_reads"] = {"handoff-b": {"next": "2026-10-23", "rung": 0}, "handoff-c": {"next": "2026-10-19", "rung": 1}}
        s = [e["item"] for e in bar_read.slate(d, per=3, today=TODAY) if e["list"] == "handoff"]
        self.assertEqual(s, ["handoff-d", "handoff-c"])

    def test_hints_name_the_record(self):
        s = {e["item"]: e["hints"] for e in bar_read.slate(data(), per=3, today=TODAY)}
        self.assertIn("pr:johnair01/bars-engine#399", s["pr-bars-engine-399"])
        self.assertIn("spec:.specify/specs/sample/spec.md", s["backlog-smp"])
        self.assertIn("callsheet:podcast", s["handoff-a"])


class ListReadTest(unittest.TestCase):
    def test_the_sample_reads_check(self):
        out, bad = run()
        self.assertEqual(bad, [])
        self.assertEqual(set(out), {r["item"] for r in LIST_READS})
        r = out["pr-bars-engine-399"]
        self.assertEqual((r["list"], r["opponent"]["kind"]), ("prs", "line"))

    def test_the_same_rules_as_a_sealed_line(self):
        _, bad = run(edit(0, call="work-today", missing=["input"], gathered=[]))
        self.assertTrue(any("work today needs a workable line" in b for b in bad))
        _, bad = run(edit(0, kernel="You are avoiding the podcast again today."))
        self.assertTrue(any("tb-loss-not-avoidance" in b for b in bad))
        _, bad = run(edit(0, factors={"score": 3}))
        self.assertTrue(any("never summed" in b for b in bad))

    def test_a_spec_source_is_a_path_not_a_guess(self):
        g = [{"piece": "next step", "found": "The spec lists its first task as ready.", "source": "spec:../etc/passwd.md"}]
        _, bad = run(edit(2, missing=["next step"], gathered=g))
        self.assertTrue(any("spec source" in b for b in bad))

    def test_its_rival_is_a_sealed_line_or_council_work(self):
        _, bad = run(edit(1, opponent={"kind": "line", "ref": "A line he never wrote", "what": "a line from nowhere"}))
        self.assertTrue(any("sealed lines" in b for b in bad))
        _, bad = run(edit(1, opponent={"kind": "item", "ref": "pr-bars-engine-399", "what": "the same item"}))
        self.assertTrue(any("does not meet itself" in b for b in bad))
        _, bad = run(edit(1, opponent=None, call="work-today"))
        self.assertEqual(bad, [])

    def test_only_items_on_the_lists(self):
        _, bad = run(edit(0, item="menu-x"))
        self.assertTrue(any("not an item on the council's lists" in b for b in bad))


class LadderTest(unittest.TestCase):
    def test_a_deferral_climbs_the_seed_library_ladder(self):
        d = data()
        out, _ = run(d=d)
        bar_read.file_items(d, out, today=TODAY)
        led = d["list_reads"]["handoff-a"]
        self.assertEqual((led["call"], led["rung"], led["next"]), ("defer", 0, "2026-10-23"))
        bar_read.file_items(d, out, today="2026-10-23")
        self.assertEqual((d["list_reads"]["handoff-a"]["rung"], d["list_reads"]["handoff-a"]["next"]), (1, "2026-10-30"))
        self.assertEqual(d["list_reads"]["handoff-a"]["first"], TODAY)

    def test_work_today_comes_back_tomorrow_until_picked(self):
        d = data()
        out, _ = run(d=d)
        bar_read.file_items(d, out, today=TODAY)
        self.assertEqual(d["list_reads"]["pr-bars-engine-399"]["next"], "2026-10-21")
        item = next(it for c in d["morning"]["categories"] for it in c["items"] if it["id"] == "pr-bars-engine-399")
        self.assertEqual(item["read"]["call"], "work-today")


class SealedLineMeetsAListItem(unittest.TestCase):
    def test_a_line_with_no_home_can_meet_an_item_the_faces_read(self):
        reads = copy.deepcopy(READS)
        reads[4]["opponent"] = {"kind": "item", "ref": "handoff-a", "what": "the podcast handoff item"}
        _, _, bad = bar_read.check(MENU, reads, data(), HIST, [{"key": "K", "what": "x"}])
        self.assertEqual(bad, [])
        reads[0]["opponent"] = {"kind": "item", "ref": "handoff-a", "what": "the podcast handoff item"}
        _, _, bad = bar_read.check(MENU, reads, data(), HIST, [{"key": "K", "what": "x"}])
        self.assertTrue(any("at home in 'chapter1-demo'" in b for b in bad))


class PickCarriesRead(unittest.TestCase):
    def test_the_thread_brief_carries_the_read(self):
        out, _ = run()
        line = pull.read_brief(out["handoff-a"])
        self.assertIn("call defer", line)
        self.assertIn("still needs input", line)
        self.assertIn("(callsheet:inner-vessel)", pull.read_brief(out["pr-bars-engine-399"]))


class MorningKeepsReads(unittest.TestCase):
    def test_a_gather_keeps_the_last_read(self):
        morning = load("morning")
        first = morning.from_handoff()[0]["id"]
        d = data()
        out, _ = run(d=d)
        d["morning"]["categories"].append({"key": "handoff", "items": [{"id": first, "text": "x", "read": out["handoff-a"]}]})
        m = morning.gather(None, prs_file=str(FIX / "prs.json"), bars=str(FIX), data=d)
        h = next(c for c in m["categories"] if c["key"] == "handoff")
        self.assertEqual(next(it for it in h["items"] if it["id"] == first)["read"]["face"], "diplomat")
        self.assertFalse(any(it.get("read") for c in m["categories"] if c["key"] == "menu" for it in c["items"]))

if __name__ == "__main__":
    unittest.main()
