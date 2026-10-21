"""Blocking steps (Wendell, 2026-10-21): a step with blocking: true holds the Council Board ahead of Tap the Vein until
it is done or sent to Claude. The behaviour is checked in a browser by /mnt/project-files/board-blocking-2026-10-21/
check.mjs; this keeps the pieces it depends on from being dropped by a later edit of the page."""
import unittest
from pathlib import Path

PAGE = (Path(__file__).resolve().parents[1] / "board" / "template.html").read_text()


class BlockingStepsTest(unittest.TestCase):
    def test_gate_holds_every_other_tab(self):
        self.assertIn("body.blk-held .tab:not(#tab-steps){opacity:.4;pointer-events:none}", PAGE)
        self.assertIn('id="blk-gate"', PAGE)

    def test_blocking_comes_before_tap_the_vein(self):
        self.assertIn("body.ttv-held:not(.blk-held) .tab:not(#tab-morning)", PAGE)
        self.assertIn("if (held && document.body.classList.contains('blk-held')) return;", PAGE)

    def test_done_withdrawn_or_with_claude_releases(self):
        self.assertIn("const blkIs = s => !!(s && s.blocking && !stClosed(s) && !s.aiBack);", PAGE)
        self.assertIn("from: 'blocking'", PAGE)

    def test_gate_runs_on_every_steps_render(self):
        body = PAGE.split("function renderSteps(){", 1)[1].split("\n}\n", 1)[0]
        self.assertIn("blkGate();", body)


if __name__ == "__main__":
    unittest.main()
