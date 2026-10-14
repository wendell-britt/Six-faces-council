"""council/ttv_bars.py: the free write becomes pitches in his exact words, and only kept pitches reach the corpus."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("ttv_bars", ROOT / "council" / "ttv_bars.py")
ttv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ttv)

WRITE = {"sessionDate": "2026-10-14", "savedAt": "2026-10-14T15:00:00Z",
         "text": "Getting it wrong gets you closer.\nThen   I let it   go. I'm the one who holds the frame."}


class TtvBarsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.bars = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_pitch_must_be_his_exact_words(self):
        self.assertEqual(ttv.not_in_write(WRITE, ["Then I let it go.", "I let go of the frame."]), ["I let go of the frame."])

    def test_pitch_rows(self):
        rows = ttv.pitch_rows(WRITE, [{"line": "Getting it wrong gets you closer.", "slot": "gm-guide.intro", "why": "a thesis"}], "About learning.")
        r = rows[0]
        self.assertEqual(r["id"], "ttv-2026-10-14-1")
        self.assertEqual([o["v"] for o in r["options"]], ["keep", "unplaced", "no"])
        self.assertIn("gm-guide.intro", r["options"][0]["label"])
        self.assertEqual(r["bar_line"], "Getting it wrong gets you closer.")

    def data(self):
        rows = ttv.pitch_rows(WRITE, [{"line": "Getting it wrong gets you closer.", "slot": "gm-guide.intro"},
                                      {"line": "Then I let it go."}, {"line": "I'm the one who holds the frame."}], "s")
        return {"questions": rows, "resolved": {"questions": {
            "ttv-2026-10-14-1": {"decision": "keep", "record": "council/ledger/x.json"},
            "ttv-2026-10-14-2": {"decision": "no"},
            "ttv-2026-10-14-3": {"decision": "unplaced"}}}}

    def test_only_kept_pitches_written_once(self):
        todo = ttv.plan(ttv.accepted(self.data()), self.bars)
        for path, text in todo:
            path.write_text(text, encoding="utf-8")
        names = sorted(p.name for p in self.bars.iterdir())
        self.assertEqual(names, ["2026-10-14-getting-it-wrong-gets-you-closer.md", "2026-10-14-im-the-one-who-holds-the.md"])
        kept = (self.bars / names[0]).read_text(encoding="utf-8")
        self.assertIn("slot: gm-guide.intro", kept)
        self.assertIn("> Getting it wrong gets you closer.\n", kept)
        self.assertIn("slot: unplaced", (self.bars / names[1]).read_text(encoding="utf-8"))
        self.assertEqual(ttv.plan(ttv.accepted(self.data()), self.bars), [])

    def test_unanswered_pitch_writes_nothing(self):
        d = self.data()
        d["resolved"]["questions"] = {}
        self.assertEqual(ttv.accepted(d), [])


if __name__ == "__main__":
    unittest.main()
