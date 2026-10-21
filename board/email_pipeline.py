#!/usr/bin/env python3
"""Outreach email drafts on the Council Board's Outreach tab, and the guard that sends only what Wendell approved
(.specify/specs/outreach-drafts/spec.md, docs/email-pipeline.md).

A draft lives on the contact it is for, as one `draft` block on contacts/<id>:

  {to: [...], cc: [...], subject, body, status, updated, lint: [...], voice: [...], author, approvedHash, approvedAt, note,
   sendingAt, sentAt, messageId, threadId}

The draft step runs the email voice pass (board/email_voice.py, docs/email-voice.md) and keeps its findings as
`voice`. A draft with an unaccepted tell is refused: rewrite it, or pass --accept RULE:"reason".

status is draft, send, revise, sending, sent or dropped. Any client may draft (a Claude thread, Zo, Codex, a routine);
drafting never sends. Wendell reads and edits the draft on the tab. His Send press saves the text he saw, sets status
send and stores approvedHash, the sha256 of that exact text (approval_hash below; the page computes the same hash with
crypto.subtle, and tests/test_email_pipeline.py pins one vector for both). Revise and Drop never send.

  python3 board/email_pipeline.py draft --store <dir> --contact <id> --to a@b --subject S --body-file f [--cc x@y]
                                        [--author name] [--kind reply|outreach] [--accept RULE:"reason"] [--no-push]
  python3 board/email_pipeline.py ready <dir>
  python3 board/email_pipeline.py mark --store <dir> <contact> sending|sent [--message-id M --thread-id T] [--no-push]
  python3 board/email_pipeline.py refuse --store <dir> <contact> <reason> [--checked-sent-folder] [--no-push]

<dir> is a store folder as board/pull.py reads it (<dir>/contacts/<id>.json, saved with ArtifactData). Every write
updates the local copy, prints the ArtifactData update for the claude.ai board (collection contacts, mode update,
data {draft}) and sends the same update to bars-engine through board/store_write.py. When bars-engine refuses (its
token answered 401 on 2026-10-21) the script says so and the printed ArtifactData write is the path.

Sender rule. Only a session holding the Gmail connector sends, and only what `ready` lists:
  1. Fetch the store fresh, run `ready`, and take each payload exactly as printed. Never retype or reflow the text.
  2. Run `mark <contact> sending` and make sure that write landed (ArtifactData update done) before any Gmail call.
  3. Send with the explicit addresses in the payload. The Gmail connector's `me` alias fails, so never pass it.
  4. Run `mark <contact> sent --message-id <id> --thread-id <id>` with the ids Gmail returned.
A draft found in `sending` is never resent automatically: the send may have gone out before the session stopped. It
goes on the needs-work list (board/pull.py) for a person to check the Sent folder, then `mark ... sent` with the ids
found there, or `refuse ... --checked-sent-folder` when nothing went out.
"""
import argparse
import datetime
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
VOICE_LINT = ROOT / "council" / "tools" / "voice_lint.py"
STATUSES = ("draft", "send", "revise", "sending", "sent", "dropped")
LOCKED = ("send", "sending")  # a session's draft never writes over an approved or in-flight email


# ---- the approval hash (keep identical to approvalHash in board/template.html) ----
def _ascii_lower(s):
    return re.sub(r"[A-Z]", lambda m: m.group(0).lower(), s)


def _trim(s):
    return re.sub(r"^[ \t]+|[ \t]+$", "", s)


def norm_addrs(addrs):
    out = {_ascii_lower(_trim(unicodedata.normalize("NFC", str(a)))) for a in (addrs or [])}
    return sorted(a for a in out if a)


def norm_body(body):
    b = unicodedata.normalize("NFC", str(body or "")).replace("\r\n", "\n").replace("\r", "\n")
    b = re.sub(r"[ \t]+$", "", b, flags=re.M)
    return re.sub(r"\n+$", "", b)


def canonical(to, cc, subject, body):
    """The fixed string both sides hash: keys in this order, no spaces, non-ASCII kept as is."""
    doc = {"body": norm_body(body), "cc": norm_addrs(cc), "subject": _trim(unicodedata.normalize("NFC", str(subject or ""))),
           "to": norm_addrs(to)}
    return json.dumps(doc, ensure_ascii=False, separators=(",", ":"))


def approval_hash(to, cc, subject, body):
    return hashlib.sha256(canonical(to, cc, subject, body).encode("utf-8")).hexdigest()


def draft_hash(d):
    return approval_hash(d.get("to"), d.get("cc"), d.get("subject"), d.get("body"))


# ---- reading the store ----
def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


def contacts(store):
    d = Path(store) / "contacts"
    return {f.stem: json.loads(f.read_text(encoding="utf-8")) for f in sorted(d.glob("*.json"))} if d.is_dir() else {}


def classify(store):
    """{ready, refused, stuck}. ready holds exactly what he approved; nothing else is ever sendable."""
    ready, refused, stuck = [], [], []
    for cid, c in contacts(store).items():
        d = c.get("draft")
        if not isinstance(d, dict):
            continue
        st = d.get("status")
        if st == "sending":
            stuck.append({"contact": cid, "subject": d.get("subject", ""), "sendingAt": d.get("sendingAt"),
                          "reason": "in sending: check the Sent folder by hand; never resent automatically"})
            continue
        if st != "send":
            continue
        why = None
        if d.get("messageId"):
            why = "already has a Gmail message id"
        elif not d.get("approvedHash"):
            why = "no approval hash: the Send press did not record what he saw"
        elif draft_hash(d) != d["approvedHash"]:
            why = "text changed after approval: the hash of the saved text does not match his Send"
        elif not norm_addrs(d.get("to")):
            why = "no recipient"
        if why:
            refused.append({"contact": cid, "subject": d.get("subject", ""), "reason": why})
            continue
        ready.append({"contact": cid, "to": list(d.get("to") or []), "cc": list(d.get("cc") or []),
                      "subject": d.get("subject", ""), "body": d.get("body", ""), "approvedHash": d["approvedHash"]})
    return {"ready": ready, "refused": refused, "stuck": stuck}


# ---- writing ----
def _store_write():
    spec = importlib.util.spec_from_file_location("store_write", HERE / "store_write.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def write_draft(store, cid, contact, draft, push=True):
    """Save locally, print the ArtifactData write, and send the same update to bars-engine when it accepts it."""
    contact = {**contact, "draft": draft}
    (Path(store) / "contacts" / f"{cid}.json").write_text(json.dumps(contact, ensure_ascii=False, indent=1) + "\n",
                                                          encoding="utf-8")
    doc = {"collection": "contacts", "docId": cid, "mode": "update", "data": {"draft": draft}}
    print("ArtifactData update for the claude.ai board (url https://claude.ai/artifact/DxyShVS8tmvJym4HAsgnho):")
    print(json.dumps({"action": "update", "collection": "contacts", "doc_id": cid, "data": {"draft": draft}},
                     ensure_ascii=False))
    if not push:
        return 0
    try:
        return _store_write().push([doc], dry=False)
    except SystemExit as e:
        print(f"bars-engine did not take the write ({e}); make the ArtifactData update above instead")
        return 0


def load_contact(store, cid):
    f = Path(store) / "contacts" / f"{cid}.json"
    if "/" in cid or not cid or not f.exists():
        sys.exit(f"contacts/{cid} is not in {store}; save the contacts collection with ArtifactData first")
    return json.loads(f.read_text(encoding="utf-8"))


def lint(body):
    """voice_lint's hard findings on the body, as short strings for the card."""
    with tempfile.TemporaryDirectory() as t:
        p = Path(t) / "draft.txt"
        p.write_text(body, encoding="utf-8")
        r = subprocess.run([sys.executable, str(VOICE_LINT), str(p), "--json"], capture_output=True, text=True)
    try:
        rep = json.loads(r.stdout)
    except json.JSONDecodeError:
        return ["voice_lint did not run"]
    return [f'{h["rule"]} L{h["line"]}: {h["text"]}' for e in rep for h in e["hard"]]


def _email_voice():
    spec = importlib.util.spec_from_file_location("email_voice", HERE / "email_voice.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def make_draft(contact, to, cc, subject, body, author, findings, at, voice=None):
    old = contact.get("draft") if isinstance(contact.get("draft"), dict) else {}
    if old.get("status") in LOCKED:
        sys.exit(f"refusing: this contact's draft is in status {old['status']}; it was approved or is being sent")
    previous = list(old.get("previous") or [])
    if old.get("status") == "sent":  # keep the sent email's ids so a reply check can still find its thread
        previous.append({k: old.get(k) for k in ("subject", "sentAt", "messageId", "threadId")})
    d = {"to": list(to), "cc": list(cc or []), "subject": subject, "body": body, "status": "draft", "updated": at,
         "lint": findings, "voice": list(voice or []), "author": author, "approvedHash": None, "approvedAt": None, "note": "", "sendingAt": None,
         "sentAt": None, "messageId": None, "threadId": None}
    if previous:
        d["previous"] = previous
    return d


def cmd_draft(a):
    contact = load_contact(a.store, a.contact)
    body = Path(a.body_file).read_text(encoding="utf-8")
    ev = _email_voice()
    try:
        accept = ev.parse_accepts(a.accept)
    except ValueError as e:
        sys.exit(f"refusing: {e}")
    voice = ev.scan(body, a.kind, accept)
    print(ev.report(voice, a.kind))
    if ev.open_tells(voice):
        sys.exit("refusing: the draft still reads as AI in the places marked TELL. Rewrite it, or pass "
                 '--accept RULE:"reason" with a written reason for each rule that stays.')
    d = make_draft(contact, a.to, a.cc, a.subject, body, a.author, lint(body), now(), voice)
    if d["lint"]:
        print("voice_lint findings (shown on the card):\n  " + "\n  ".join(d["lint"]))
    return write_draft(a.store, a.contact, contact, d, not a.no_push)


def mark(contact, what, message_id=None, thread_id=None, at=None):
    d = dict(contact.get("draft") or {})
    at = at or now()
    if what == "sending":
        if d.get("status") != "send" or d.get("messageId"):
            sys.exit(f"refusing: status is {d.get('status')}, not an approved draft")
        if not d.get("approvedHash") or draft_hash(d) != d["approvedHash"]:
            sys.exit("refusing: the text changed after approval; run refuse instead")
        d.update(status="sending", sendingAt=at)
    else:
        if d.get("status") != "sending":
            sys.exit(f"refusing: status is {d.get('status')}; mark sending before the Gmail call")
        if not message_id:
            sys.exit("refusing: mark sent needs --message-id from Gmail")
        d.update(status="sent", sentAt=at, messageId=message_id, threadId=thread_id)
    d["updated"] = at
    return d


def refuse(contact, reason, checked=False, at=None):
    d = dict(contact.get("draft") or {})
    if d.get("status") == "sending" and not checked:
        sys.exit("refusing: this draft is in sending; check the Sent folder, then pass --checked-sent-folder")
    if d.get("status") == "sent":
        sys.exit("refusing: this draft was sent")
    at = at or now()
    d.update(status="draft", note=reason, approvedHash=None, approvedAt=None, sendingAt=None, updated=at)
    return d


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("draft")
    p.add_argument("--store", required=True)
    p.add_argument("--contact", required=True)
    p.add_argument("--to", action="append", required=True)
    p.add_argument("--cc", action="append", default=[])
    p.add_argument("--subject", required=True)
    p.add_argument("--body-file", required=True)
    p.add_argument("--author", default="session")
    p.add_argument("--kind", choices=("reply", "outreach"), default="outreach")
    p.add_argument("--accept", action="append", default=[], metavar='RULE:"reason"')
    p.add_argument("--no-push", action="store_true")
    r = sub.add_parser("ready")
    r.add_argument("store")
    m = sub.add_parser("mark")
    m.add_argument("--store", required=True)
    m.add_argument("contact")
    m.add_argument("what", choices=("sending", "sent"))
    m.add_argument("--message-id")
    m.add_argument("--thread-id")
    m.add_argument("--no-push", action="store_true")
    f = sub.add_parser("refuse")
    f.add_argument("--store", required=True)
    f.add_argument("contact")
    f.add_argument("reason")
    f.add_argument("--checked-sent-folder", action="store_true")
    f.add_argument("--no-push", action="store_true")
    a = ap.parse_args()
    if a.cmd == "draft":
        sys.exit(cmd_draft(a))
    if a.cmd == "ready":
        print(json.dumps(classify(a.store), ensure_ascii=False, indent=1))
        return
    contact = load_contact(a.store, a.contact)
    d = (mark(contact, a.what, a.message_id, a.thread_id) if a.cmd == "mark"
         else refuse(contact, a.reason, a.checked_sent_folder))
    sys.exit(write_draft(a.store, a.contact, contact, d, not a.no_push))


if __name__ == "__main__":
    main()
