"""council/ttv_bars.py: lines marked BAR in the board's Tap the Vein reach the corpus once, unedited."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("ttv_bars", ROOT / "council" / "ttv_bars.py")
ttv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ttv)

DOC = {"sessionDate": "2026-10-14", "savedAt": "2026-10-14T15:00:00Z",
       "bars": ["Getting it wrong gets you closer.", "  Getting it wrong   gets you closer.  ", "I'm the one who holds the frame."]}


class TtvBarsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.bars = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, doc=DOC):
        for path, text in ttv.plan(doc, self.bars):
            path.write_text(text, encoding="utf-8")

    def test_each_line_once_with_exact_words(self):
        self.write()
        names = sorted(p.name for p in self.bars.iterdir())
        self.assertEqual(names, ["2026-10-14-getting-it-wrong-gets-you-closer.md", "2026-10-14-im-the-one-who-holds-the.md"])
        text = (self.bars / names[1]).read_text(encoding="utf-8")
        self.assertIn("> I'm the one who holds the frame.\n", text)
        self.assertIn("kind: bar", text)
        self.assertIn("said: 2026-10-14", text)

    def test_safe_to_run_twice(self):
        self.write()
        self.assertEqual(ttv.plan(DOC, self.bars), [])

    def test_same_slug_different_words_gets_its_own_file(self):
        self.write()
        self.write({**DOC, "bars": ["Getting it wrong gets you closer, every time."]})
        self.assertTrue((self.bars / "2026-10-14-getting-it-wrong-gets-you-closer-2.md").exists())

    def test_line_must_be_in_the_free_write(self):
        doc = {"sessionDate": "2026-10-14", "text": "I hold the frame.\nThen   I let it   go."}
        self.assertEqual(ttv.not_in_write(doc, ["Then I let it go.", "I let go of the frame."]), ["I let go of the frame."])
        self.write_lines(doc, ["Then I let it go."])
        self.assertTrue((self.bars / "2026-10-14-then-i-let-it-go.md").exists())

    def write_lines(self, doc, lines):
        for path, text in ttv.plan(doc, self.bars, lines):
            path.write_text(text, encoding="utf-8")

    def test_no_bars_no_files(self):
        self.assertEqual(ttv.plan({"sessionDate": "2026-10-14", "bars": []}, self.bars), [])


if __name__ == "__main__":
    unittest.main()
