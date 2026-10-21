"""board/email_pipeline.py and the page's approvalHash: the two hashes agree, only text that still matches his Send is
ready, a draft in sending is never offered again, and a session's draft never writes over an approved one. pull.py
prints the drafts' needs-work lines and writes nothing for them."""
import contextlib
import importlib.util
import io
import json
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


ep = load("email_pipeline", "board/email_pipeline.py")
pull = load("pull_for_email", "board/pull.py")

VECTOR = ([" Wendell@MasteringAllyship.com ", "a@b.org", "a@b.org"], ["Zoë@Example.com"], "  Hello — café  ",
          "Line one  \r\nLine two\t\r\n\r\n")
VECTOR_HASH = "3adb98f7a34d50a1ecc545d9efd5de73cfeefc2b8a6980fd84c13dc29c4fff98"
OTHERS = [([], [], "", ""), (["x@y.z"], [], 'Say "hi"', 'Tab\there, back\\slash, bell\x07, line sep\n  indented\n')]


def approved(subject="Hi", body="Hello there.\nWendell", **extra):
    d = {"to": ["someone@example.org"], "cc": [], "subject": subject, "body": body, "status": "send",
         "approvedAt": "2026-10-21T10:00:00Z", "messageId": None}
    d["approvedHash"] = ep.draft_hash(d)
    d.update(extra)
    return d


class Hash(unittest.TestCase):
    def test_pinned_vector(self):
        self.assertEqual(ep.approval_hash(*VECTOR), VECTOR_HASH)
        self.assertEqual(ep.canonical(*VECTOR), '{"body":"Line one\\nLine two","cc":["zoë@example.com"],'
                         '"subject":"Hello — café","to":["a@b.org","wendell@masteringallyship.com"]}')

    def test_any_text_change_changes_the_hash(self):
        base = ep.approval_hash(["a@b.c"], [], "S", "Body")
        for other in (ep.approval_hash(["a@b.d"], [], "S", "Body"), ep.approval_hash(["a@b.c"], ["c@d.e"], "S", "Body"),
                      ep.approval_hash(["a@b.c"], [], "S.", "Body"), ep.approval_hash(["a@b.c"], [], "S", "Body!")):
            self.assertNotEqual(base, other)

    @unittest.skipUnless(shutil.which("node"), "node is not installed")
    def test_page_computes_the_same_hash(self):
        page = (ROOT / "board/template.html").read_text(encoding="utf-8")
        fn = re.search(r"/\* approval-hash:start.*?\*/(.*?)/\* approval-hash:end \*/", page, re.S).group(1)
        cases = [VECTOR, *OTHERS]
        js = fn + f"\n(async () => {{ const out = []; for (const a of {json.dumps(cases)}) out.push(await approvalHash(...a));" \
                  " console.log(JSON.stringify(out)); })();"
        r = subprocess.run(["node", "-e", js], capture_output=True, text=True, timeout=60)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(json.loads(r.stdout), [ep.approval_hash(*c) for c in cases])
        self.assertEqual(json.loads(r.stdout)[0], VECTOR_HASH)


class Store(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.store = Path(self.tmp.name)
        (self.store / "contacts").mkdir()
        (self.store / "positions").mkdir()

    def tearDown(self):
        self.tmp.cleanup()

    def put(self, cid, draft=None, **fields):
        doc = {"name": cid, "status": "Identified", **fields}
        if draft is not None:
            doc["draft"] = draft
        (self.store / "contacts" / f"{cid}.json").write_text(json.dumps(doc))

    def test_ready_and_refused_split(self):
        self.put("good", approved())
        changed = approved()
        changed["body"] += " One more line he never saw."
        self.put("changed", changed)
        self.put("sent", approved(messageId="m1", status="sent"))
        self.put("plain", {"status": "draft", "subject": "x", "body": "y", "to": ["a@b.c"]})
        self.put("nodraft")
        out = ep.classify(self.store)
        self.assertEqual([r["contact"] for r in out["ready"]], ["good"])
        self.assertEqual(out["ready"][0]["body"], "Hello there.\nWendell")
        self.assertEqual(out["ready"][0]["to"], ["someone@example.org"])
        self.assertEqual([r["contact"] for r in out["refused"]], ["changed"])
        self.assertIn("text changed after approval", out["refused"][0]["reason"])

    def test_sending_is_never_ready_again(self):
        self.put("inflight", approved(status="sending", sendingAt="2026-10-21T11:00:00Z"))
        out = ep.classify(self.store)
        self.assertEqual(out["ready"], [])
        self.assertEqual([r["contact"] for r in out["stuck"]], ["inflight"])
        with self.assertRaises(SystemExit):
            ep.mark({"draft": approved(status="sending")}, "sending")
        with self.assertRaises(SystemExit):
            ep.refuse({"draft": approved(status="sending")}, "nothing went out")
        self.assertEqual(ep.refuse({"draft": approved(status="sending")}, "checked", checked=True)["status"], "draft")

    def test_mark_flow(self):
        d = ep.mark({"draft": approved()}, "sending", at="2026-10-21T12:00:00Z")
        self.assertEqual((d["status"], d["sendingAt"]), ("sending", "2026-10-21T12:00:00Z"))
        with self.assertRaises(SystemExit):
            ep.mark({"draft": d}, "sent")  # no message id
        d = ep.mark({"draft": d}, "sent", "msg-1", "thr-1", at="2026-10-21T12:00:05Z")
        self.assertEqual((d["status"], d["messageId"], d["threadId"]), ("sent", "msg-1", "thr-1"))
        with self.assertRaises(SystemExit):
            ep.mark({"draft": {**approved(), "body": "changed"}}, "sending")
        with self.assertRaises(SystemExit):
            ep.mark({"draft": approved(status="draft")}, "sent", "m")

    def test_draft_refuses_over_an_approved_one(self):
        for st in ("send", "sending"):
            with self.assertRaises(SystemExit):
                ep.make_draft({"draft": approved(status=st)}, ["a@b.c"], [], "S", "B", "t", [], "2026-10-21T00:00:00Z")
        d = ep.make_draft({"draft": approved(status="sent", messageId="m9", threadId="t9", sentAt="x")}, ["a@b.c"], [],
                          "S", "B", "t", [], "2026-10-21T00:00:00Z")
        self.assertEqual((d["status"], d["approvedHash"]), ("draft", None))
        self.assertEqual(d["previous"][0]["messageId"], "m9")

    def test_draft_cli_writes_locally_and_prints_the_artifactdata_update(self):
        self.put("demo")
        body = self.store / "body.txt"
        body.write_text("Hi Wendell.\nThis is a test from the board.\nWendell\n")
        r = subprocess.run(["python3", str(ROOT / "board/email_pipeline.py"), "draft", "--store", str(self.store),
                            "--contact", "demo", "--to", "wendell@masteringallyship.com", "--subject", "Test",
                            "--body-file", str(body), "--author", "test", "--no-push"],
                           capture_output=True, text=True, cwd=ROOT)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('"collection": "contacts"', r.stdout)
        doc = json.loads((self.store / "contacts" / "demo.json").read_text())
        self.assertEqual((doc["draft"]["status"], doc["draft"]["author"], doc["name"]), ("draft", "test", "demo"))
        self.assertIsInstance(doc["draft"]["lint"], list)
        self.put("locked", approved())
        r = subprocess.run(["python3", str(ROOT / "board/email_pipeline.py"), "draft", "--store", str(self.store),
                            "--contact", "locked", "--to", "a@b.c", "--subject", "x", "--body-file", str(body),
                            "--no-push"], capture_output=True, text=True, cwd=ROOT)
        self.assertNotEqual(r.returncode, 0)
        self.assertEqual(json.loads((self.store / "contacts" / "locked.json").read_text())["draft"]["status"], "send")

    def test_pull_lines(self):
        self.put("go", approved(subject="Podcast?"))
        bad = approved(subject="Edited")
        bad["subject"] = "Edited later"
        self.put("bad", bad)
        self.put("rev", {"status": "revise", "note": "Shorter, please", "subject": "Long one", "to": ["a@b.c"]})
        self.put("stuck", approved(subject="Hung", status="sending", sendingAt="2026-10-21T09:00:00Z"))
        lines = pull.find_drafts(self.store)
        self.assertTrue(any(l.startswith('contacts/go: email approved to send "Podcast?"') for l in lines), lines)
        self.assertTrue(any(l.startswith('contacts/bad: email "Edited later" not sendable: text changed') for l in lines))
        self.assertTrue(any(l.startswith('contacts/rev: email revise: "Shorter, please"') for l in lines))
        self.assertTrue(any(l.startswith('contacts/stuck: email "Hung" stuck in sending') for l in lines))
        self.assertEqual(lines, pull.find_drafts(self.store))  # a rerun prints the same and writes nothing

    def test_pull_without_contacts_folder(self):
        shutil.rmtree(self.store / "contacts")
        self.assertEqual(pull.find_drafts(self.store), [])


if __name__ == "__main__":
    unittest.main()
