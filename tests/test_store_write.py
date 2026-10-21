"""board/store_write.py: the hash matches bars-engine's, diff finds drift, and --push-missing sends only what the
artifact alone has (a document on both sides is never overwritten)."""
import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

spec = importlib.util.spec_from_file_location("store_write", Path(__file__).parents[1] / "board" / "store_write.py")
sw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sw)


class StoreWrite(unittest.TestCase):
    def test_canonical_matches_bars_engine(self):
        # bars-engine src/app/api/board/session-writes/__tests__/route.test.ts asserts the same string.
        self.assertEqual(sw.canonical({"b": [1, {"d": "\u00e9", "c": None}], "a": True}),
                         '{"a":true,"b":[1,{"c":null,"d":"\u00e9"}]}')

    def test_diff_and_push_missing(self):
        sent = []

        def call(method, path, body=None):
            if method == "GET":
                return {"hashes": {"steps": {"same": sw.doc_hash({"do": "a"}), "changed": sw.doc_hash({"do": "b"}),
                                             "theirs": "x"}}}
            sent.extend(body["docs"])
            return {"written": [f'{d["collection"]}/{d["docId"]}' for d in body["docs"]], "same": 0, "refused": []}

        with tempfile.TemporaryDirectory() as t, mock.patch.object(sw, "call", call):
            (Path(t) / "steps").mkdir()
            for i, d in {"same": {"do": "a"}, "changed": {"do": "b", "done": True}, "new": {"do": "c"}}.items():
                (Path(t) / "steps" / f"{i}.json").write_text(json.dumps(d))
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                self.assertEqual(sw.diff(t, push_missing=True), 1)
        out = out.getvalue()
        for line in ("only artifact: steps/new", "only bars-engine: steps/theirs", "differ: steps/changed",
                     "lists: not in the export"):
            self.assertIn(line, out)
        self.assertEqual(sent, [{"collection": "steps", "docId": "new", "mode": "set", "data": {"do": "c"}}])

    def test_load_docs_takes_artifactdata_spelling(self):
        with tempfile.TemporaryDirectory() as t:
            f = Path(t) / "d.json"
            f.write_text(json.dumps([{"collection": "contacts", "doc_id": "ari", "data": {"name": "Ari"}}]))
            self.assertEqual(sw.load_docs(f), [{"collection": "contacts", "docId": "ari", "data": {"name": "Ari"}}])


if __name__ == "__main__":
    unittest.main()
