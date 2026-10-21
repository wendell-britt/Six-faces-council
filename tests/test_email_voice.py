"""board/email_voice.py and its profile: the tells fire on an AI-sounding draft, a draft in Wendell's voice passes,
an accepted tell (with a reason) stops blocking, and email_pipeline.py draft refuses to place a draft with an open tell."""
import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("email_voice", ROOT / "board/email_voice.py")
ev = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ev)

AI = """Dear Sam,

I hope this email finds you well. I'm reaching out to share an update on the project — it is moving along.

Please don't hesitate to reach me; I would be delighted to circle back. We value clarity, trust, and growth.

In summary, once again, thank you for your time and consideration.

Best regards,
Claude
"""

HIS = """Hey Sam!

Oh snap, the flyer is done and it looks hella good!

Feel free to throw some time on my calendar this week so we can pick the print date (I promise I'll actually show up on time).

Looking forward to it!
"""


class Pass(unittest.TestCase):
    def test_tells_fire_on_an_ai_draft(self):
        found = ev.scan(AI, "outreach")
        rules = {f["rule"] for f in ev.open_tells(found)}
        for r in ("dear-opener", "finds-you-well", "reaching-out", "em-dash", "dont-hesitate", "delighted",
                  "circle-back", "semicolon", "rule-of-three", "recap-closer", "restated-ask", "time-and-consideration",
                  "regards"):
            self.assertIn(r, rules)
        self.assertTrue(all(f["instead"] for f in found))

    def test_his_voice_passes(self):
        found = ev.scan(HIS, "outreach")
        self.assertEqual(ev.open_tells(found), [], found)
        self.assertEqual([f for f in found if f["class"] == "fit"], [], found)

    def test_fit_notes_never_block(self):
        flat = "Hi Sam,\n\nThe meeting is on Tuesday at noon in the usual place.\n\nWendell\n"
        found = ev.scan(flat, "reply")
        self.assertEqual(ev.open_tells(found), [])
        self.assertTrue({"no-exclamation", "greeting", "signoff-block"} <= {f["rule"] for f in found}, found)

    def test_accept_needs_a_reason_and_clears_the_tell(self):
        body = "Hey Sam!\n\nThe dates are Monday, Tuesday and Friday.\n\nSee ya then!\n"
        self.assertEqual([f["rule"] for f in ev.open_tells(ev.scan(body))], ["rule-of-three"])
        with self.assertRaises(ValueError):
            ev.parse_accepts(["rule-of-three"])
        with self.assertRaises(ValueError):
            ev.parse_accepts(["no-such-rule:because"])
        acc = ev.parse_accepts(['rule-of-three:"three real dates, not rhythm"'])
        found = ev.scan(body, accept=acc)
        self.assertEqual(ev.open_tells(found), [])
        self.assertEqual(found[0]["accepted"], "three real dates, not rhythm")

    def test_cli_exit_codes(self):
        with tempfile.TemporaryDirectory() as t:
            p = Path(t) / "ai.txt"
            p.write_text(AI)
            r = subprocess.run(["python3", str(ROOT / "board/email_voice.py"), str(p), "--json"], capture_output=True,
                               text=True)
            self.assertEqual(r.returncode, 1)
            self.assertGreater(json.loads(r.stdout)["open_tells"], 5)
            p.write_text(HIS)
            r = subprocess.run(["python3", str(ROOT / "board/email_voice.py"), str(p)], capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stdout)


class Draft(unittest.TestCase):
    def run_draft(self, store, body, *extra):
        f = store / "body.txt"
        f.write_text(body)
        return subprocess.run(["python3", str(ROOT / "board/email_pipeline.py"), "draft", "--store", str(store),
                               "--contact", "demo", "--to", "a@b.org", "--subject", "Hi", "--body-file", str(f),
                               "--no-push", *extra], capture_output=True, text=True, cwd=ROOT)

    def test_draft_refuses_on_a_tell_and_places_after_accept(self):
        with tempfile.TemporaryDirectory() as t:
            store = Path(t)
            (store / "contacts").mkdir()
            (store / "contacts" / "demo.json").write_text(json.dumps({"name": "demo", "status": "Identified"}))
            r = self.run_draft(store, "Hey Sam!\n\nI wanted to reach out about Friday!\n\nSee ya then!\n")
            self.assertNotEqual(r.returncode, 0)
            self.assertIn("--accept", r.stderr)
            self.assertNotIn("draft", json.loads((store / "contacts" / "demo.json").read_text()))
            r = self.run_draft(store, "Hey Sam!\n\nI wanted to reach out about Friday!\n\nSee ya then!\n",
                               "--kind", "reply", "--accept", "reaching-out:quoting the old subject line")
            self.assertEqual(r.returncode, 0, r.stderr)
            d = json.loads((store / "contacts" / "demo.json").read_text())["draft"]
            self.assertEqual(d["voice"][0]["accepted"], "quoting the old subject line")
            self.assertIsInstance(d["lint"], list)
            self.assertNotIn("voice", json.loads(ev_canonical(d)))  # the approval hash covers to/cc/subject/body only


def ev_canonical(d):
    spec = importlib.util.spec_from_file_location("email_pipeline_v", ROOT / "board/email_pipeline.py")
    ep = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ep)
    return ep.canonical(d["to"], d["cc"], d["subject"], d["body"])


if __name__ == "__main__":
    unittest.main()
