"""The board pages never call a function they no longer define (council/postmortems/2026-10-20-steps-outreach-blank.md).

#312 deleted ttvRender and left a call to it ahead of the store subscriptions, so Your steps and Outreach loaded
empty on 2026-10-19 while the store held every row."""
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("page_calls", ROOT / "board" / "page_calls.py")
page_calls = importlib.util.module_from_spec(spec)
spec.loader.exec_module(page_calls)


class PageCalls(unittest.TestCase):
    def test_board_pages_call_only_what_they_define(self):
        for page in page_calls.DEFAULT + [ROOT / "board" / "council-board.html"]:
            if page.exists():
                with self.subTest(page=page.name):
                    self.assertEqual(page_calls.undefined_calls(page.read_text(encoding="utf-8")), [])

    def test_the_19_october_page_is_refused(self):
        html = "<script>\nfunction renderMorning(){}\n(async () => {\n  renderMorning(); ttvRender();\n  db.collection('steps');\n})();\n</script>"
        self.assertEqual(page_calls.undefined_calls(html), ["ttvRender"])

    def test_names_in_strings_comments_and_templates_are_not_calls(self):
        html = ("<script>\n// ghost() in a comment\nconst a = 'ghost()', b = \"ghost()\";\n"
                "const f = x => `Run (${x}) and save (it)`;\nf(a + b);\n</script>")
        self.assertEqual(page_calls.undefined_calls(html), [])

    def test_template_expressions_are_still_read(self):
        html = "<script>\nconst f = x => `a ${gone(x)} b`;\nf(1);\n</script>"
        self.assertEqual(page_calls.undefined_calls(html), ["gone"])


if __name__ == "__main__":
    unittest.main()
