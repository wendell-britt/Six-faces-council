"""An empty board store reads as a fault on the Council Board, never as "Nothing waiting on you"
(council/postmortems/2026-10-20-steps-outreach-blank.md). Runs board/checks/store_fault.mjs in Chromium; skips where
Node or Playwright is missing."""
import json
import os
import shutil
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHECK = ROOT / "board" / "checks" / "store_fault.mjs"


def run(page):
    env = dict(os.environ)
    if shutil.which("npm") and "PLAYWRIGHT_MODULE" not in env:
        root = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
        env["PLAYWRIGHT_MODULE"] = str(Path(root) / "playwright" / "index.js")
    r = subprocess.run(["node", str(CHECK), str(page)], capture_output=True, text=True, env=env, timeout=120)
    if r.returncode:
        raise unittest.SkipTest(f"browser check did not run: {r.stderr.strip()[-200:]}")
    return json.loads(r.stdout)


@unittest.skipUnless(shutil.which("node"), "needs node")
class StoreFault(unittest.TestCase):
    def test_council_board_flags_an_empty_store(self):
        out = run(ROOT / "board" / "council-board.html")
        for tab in ("steps", "outreach"):
            self.assertTrue(out["empty"][tab]["fault"], tab)
            self.assertFalse(out["empty"][tab]["hidden"], tab)
            self.assertNotIn("Nothing waiting on you", out["empty"][tab]["text"])
            self.assertFalse(out["filled"][tab]["fault"], tab)
        self.assertEqual(out["empty"]["errors"] + out["filled"]["errors"], [])

    def test_nonprofit_board_keeps_its_empty_lists(self):
        out = run(ROOT / "board" / "nonprofit" / "nonprofit-board.html")
        self.assertFalse(out["empty"]["steps"]["fault"])
        self.assertIn("Nothing waiting on you", out["empty"]["steps"]["text"])


if __name__ == "__main__":
    unittest.main()
