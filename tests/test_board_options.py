"""Every question option on the board can be saved.

The page saves an option's `v` as the choice. On 2026-10-17 four slice rows were written with `consequence` and no `v`,
so picking one and pressing Save only showed "Pick an option or write a steer first."

Run: python3 -m unittest discover -s tests
"""
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("build_board", ROOT / "board/build_board.py")
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class BoardOptions(unittest.TestCase):
    def test_every_option_has_a_value_and_consequence(self):
        data = json.loads((ROOT / "board/board_data.json").read_text())
        self.assertEqual(build.option_problems(data), [])

    def test_missing_value_is_caught(self):
        data = {"questions": [{"id": "x", "options": [{"label": "a", "consequence": "b"}]}]}
        self.assertEqual(len(build.option_problems(data)), 1)


if __name__ == "__main__":
    unittest.main()
