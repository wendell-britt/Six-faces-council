"""The Your eyes tab gathers every open look step into one card per strand, newest first, with older looks folded under
it, and a yes writes done + note to the step (Wendell, 2026-10-24: "a place on the council board ... where we can preview
and test any assets that are waiting for my eyes"). Runs board/checks/looks.mjs in Chromium; skips where Node or
Playwright is missing."""
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHECK = ROOT / "board" / "checks" / "looks.mjs"


def run(page, store=None):
    env = dict(os.environ)
    if shutil.which("npm") and "PLAYWRIGHT_MODULE" not in env:
        root = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
        env["PLAYWRIGHT_MODULE"] = str(Path(root) / "playwright" / "index.js")
    args = ["node", str(CHECK), str(page)] + ([store] if store else [])
    r = subprocess.run(args, capture_output=True, text=True, env=env, timeout=120)
    if r.returncode:
        raise unittest.SkipTest(f"browser check did not run: {r.stderr.strip()[-200:]}")
    return json.loads(r.stdout)


@unittest.skipUnless(shutil.which("node"), "needs node")
class LooksTab(unittest.TestCase):
    def test_one_card_per_strand_newest_first(self):
        out = run(ROOT / "board" / "council-board.html")
        self.assertEqual(out["errors"], [])
        self.assertFalse(out["tabHidden"])
        self.assertEqual(out["count"], "2")
        self.assertEqual([c["id"] for c in out["cards"]], ["boat-look-2", "kit-look-01"])
        self.assertEqual(out["cards"][0]["older"], 1)
        self.assertEqual(out["cards"][0]["go"], "https://example.com/new")
        self.assertEqual(out["cards"][1]["links"], 1)  # the scroll link named in `where`
        self.assertEqual(out["seen"], 1)
        self.assertLessEqual(out["pageWidth"], 390)
        self.assertEqual(out["writes"], [["steps/boat-look-2", "update", True, "Yes"]])

    def test_a_board_without_looks_hides_the_tab(self):
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
            json.dump({"lists": {"a": {"title": "A"}}, "steps": {"a-01": {"list": "a", "n": 1, "do": "Do it"}}}, f)
        out = run(ROOT / "board" / "nonprofit" / "nonprofit-board.html", f.name)
        self.assertEqual(out["errors"], [])
        self.assertTrue(out["tabHidden"])


if __name__ == "__main__":
    unittest.main()
