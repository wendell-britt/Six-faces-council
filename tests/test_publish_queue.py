"""The podcast publish queue (pass podcast-pipeline2): approval gates publishing, nothing posts twice, failures surface,
and the dry run needs no network or token. Meta's Graph API is faked; no test reaches it."""
import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path

import jsonschema
import pytest

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("publish", ROOT / "council/podcast/publish/publish.py")
pub = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pub)

JPEG = b"\xff\xd8\xff\xe0" + b"\0" * 64
NOW = datetime(2026, 10, 30, 16, 5, tzinfo=timezone.utc)


def make_queue(tmp):
    (tmp / "covers").mkdir()
    (tmp / "covers/c1.jpg").write_bytes(JPEG)
    (tmp / "covers/day0.jpg").write_bytes(JPEG)
    (tmp / "clip1.mp4").write_bytes(b"MP4" * 100)
    return {
        "episode": "mtgoa-ep03", "approval_row": "pq-mtgoa-ep03",
        "posts": [
            {"id": "day0", "title": "Episode is out", "kind": "image", "at": "2026-10-30T09:00:00-07:00",
             "networks": ["instagram", "facebook"], "image": "covers/day0.jpg",
             "captions": {"instagram": "Episode 3 is out. Link in bio.", "facebook": "Episode 3 is out: https://youtu.be/x"}},
            {"id": "clip1", "title": "Clip 1", "kind": "reel", "at": "2026-11-01T09:00:00-07:00",
             "networks": ["instagram", "facebook"], "clip": {"path": str(tmp / "clip1.mp4")}, "cover": "covers/c1.jpg",
             "captions": {"instagram": "Clip one.", "facebook": "Clip one: https://youtu.be/x"}},
        ],
    }


def board_for(q, decision="approve", sha=None):
    return {"questions": [{"id": q["approval_row"], "queue_sha": sha or pub.queue_sha(q)}],
            "resolved": {"questions": {q["approval_row"]: {"decision": decision, "recorded": "2026-10-29"}} if decision else {}}}


class FakeMeta:
    def __init__(self, fail_on=None):
        self.calls, self.fail_on, self.n = [], fail_on, 0

    def __call__(self, method, url, data=None, headers=None):
        body = (data or b"")[:2000].decode(errors="replace")
        self.calls.append((method, url, body, headers or {}))
        if self.fail_on and self.fail_on in url:
            raise pub.GraphError("OAuthException 190: token expired")
        self.n += 1
        if "me/accounts" in url:
            return {"data": [{"id": "P1", "name": "Mastering Allyship", "access_token": "PTOK",
                              "instagram_business_account": {"id": "IG1"}}]}
        if "fields=status_code" in url:
            return {"status_code": "FINISHED"}
        if "upload_phase=start" in body:
            return {"video_id": "V1", "upload_url": "https://rupload.facebook.com/video-upload/v24.0/V1"}
        if "/photos" in url:
            return {"id": "PH1", "post_id": "P1_PH1"}
        if "fields=permalink" in url:
            return {"permalink": "https://instagram.com/reel/abc"}
        return {"id": f"ID{self.n}"}


@pytest.fixture
def setup(tmp_path, monkeypatch):
    qdir = tmp_path / "queue"
    qdir.mkdir()
    q = make_queue(tmp_path)
    (qdir / "mtgoa-ep03.json").write_text(json.dumps(q))
    (tmp_path / "board.json").write_text(json.dumps(board_for(q)))
    fake = FakeMeta()
    monkeypatch.setattr(pub, "http", fake)
    monkeypatch.setenv("META_TOKEN", "SECRET-TOKEN")
    monkeypatch.setattr(pub.time, "sleep", lambda s: None)
    args = ["--queue-dir", str(qdir), "--board", str(tmp_path / "board.json"), "--root", str(tmp_path)]
    return tmp_path, qdir / "mtgoa-ep03.json", fake, args


def test_queue_fits_the_schema(tmp_path):
    schema = json.loads((ROOT / "schema/publish-queue.schema.json").read_text())
    jsonschema.validate(make_queue(tmp_path), schema)


def test_validate_catches_placeholders_and_bad_covers(tmp_path):
    q = make_queue(tmp_path)
    assert pub.validate(q, root=tmp_path) == []
    q["posts"][0]["captions"]["facebook"] = "Out now: [episode link]"
    (tmp_path / "covers/c1.jpg").write_bytes(b"\x89PNG....")
    probs = pub.validate(q, root=tmp_path)
    assert any("[episode link]" in p for p in probs)
    assert any("not a JPEG" in p for p in probs)


def test_approval_needs_the_same_queue_and_an_approve(tmp_path):
    q = make_queue(tmp_path)
    assert pub.approval(q, board_for(q))[0]
    assert not pub.approval(q, board_for(q, decision="hold"))[0]
    assert not pub.approval(q, board_for(q, decision=None))[0]
    assert not pub.approval(q, {"questions": []})[0]
    approved = board_for(q)
    q["posts"][1]["captions"]["instagram"] = "Clip one, edited after approval."
    ok, why = pub.approval(q, approved)
    assert not ok and "different version" in why


def test_state_and_numbers_do_not_change_the_hash(tmp_path):
    q = make_queue(tmp_path)
    sha = pub.queue_sha(q)
    q["state"] = {"day0": {"instagram": {"status": "published", "id": "1"}}}
    q["numbers"] = {"day0": {}}
    assert pub.queue_sha(q) == sha


def test_due_publishes_on_time_and_marks_late_posts_missed(tmp_path):
    q = make_queue(tmp_path)
    acts = {(p["id"], n): a for p, n, a in pub.due(q, NOW)}
    assert acts == {("day0", "instagram"): "publish", ("day0", "facebook"): "publish"}   # clip1 is not due yet
    late = datetime(2026, 10, 30, 23, 30, tzinfo=timezone.utc)
    assert {a for _, _, a in pub.due(q, late)} == {"missed"}


def test_run_publishes_due_posts_and_writes_ids_back(setup):
    tmp, qfile, fake, args = setup
    assert pub.main(args + ["run", "--now", NOW.isoformat(), "--failures-out", str(tmp / "f.json")]) == 0
    st = json.loads(qfile.read_text())["state"]["day0"]
    assert st["instagram"]["status"] == "published" and st["instagram"]["permalink"]
    assert st["facebook"] == {**st["facebook"], "status": "published", "id": "P1_PH1"}
    assert json.loads((tmp / "f.json").read_text()) == []
    ig_create = next(c for c in fake.calls if c[1].endswith("IG1/media"))
    assert "image_url=https%3A%2F%2Fraw.githubusercontent.com" in ig_create[2]
    assert all("SECRET-TOKEN" not in json.dumps(st) for _ in [0])
    # a second run publishes nothing again
    fake.calls.clear()
    pub.main(args + ["run", "--now", NOW.isoformat()])
    assert not [c for c in fake.calls if "media_publish" in c[1] or "/photos" in c[1]]


def test_reel_uses_resumable_upload_cover_and_the_page_reels_flow(setup):
    tmp, qfile, fake, args = setup
    later = datetime(2026, 11, 1, 16, 10, tzinfo=timezone.utc)
    q = json.loads(qfile.read_text())
    q["state"] = {"day0": {"instagram": {"status": "published", "id": "x"}, "facebook": {"status": "published", "id": "y"}}}
    qfile.write_text(json.dumps(q))
    pub.main(args + ["run", "--now", later.isoformat()])
    urls = [c[1] for c in fake.calls]
    create = next(c for c in fake.calls if c[1].endswith("IG1/media"))
    assert "media_type=REELS" in create[2] and "upload_type=resumable" in create[2] and "cover_url=" in create[2]
    up = next(c for c in fake.calls if "rupload.facebook.com/ig-api-upload" in c[1])
    assert up[3]["Authorization"] == "OAuth SECRET-TOKEN" and up[3]["offset"] == "0"
    assert any(u.endswith("IG1/media_publish") for u in urls)
    reels = [c for c in fake.calls if c[1].endswith("P1/video_reels")]
    assert "upload_phase=start" in reels[0][2] and "upload_phase=finish" in reels[1][2]
    assert "video_state=PUBLISHED" in reels[1][2] and "access_token=PTOK" in reels[1][2]
    assert any(u.endswith("V1/thumbnails") for u in urls)
    st = json.loads(qfile.read_text())["state"]["clip1"]
    assert st["instagram"]["status"] == st["facebook"]["status"] == "published"


def test_failure_at_the_publish_call_is_never_retried_and_reported(setup, monkeypatch):
    tmp, qfile, fake, args = setup
    fake.fail_on = "media_publish"
    pub.main(args + ["run", "--now", NOW.isoformat(), "--failures-out", str(tmp / "f.json")])
    st = json.loads(qfile.read_text())["state"]["day0"]["instagram"]
    assert st["status"] == "failed" and st["stage"] == "publish" and "token expired" in st["error"]
    failures = json.loads((tmp / "f.json").read_text())
    assert [f["network"] for f in failures] == ["instagram"] and failures[0]["retrying"] is False
    fake.fail_on, fake.calls = None, []
    pub.main(args + ["run", "--now", NOW.isoformat()])
    assert not [c for c in fake.calls if "IG1/media" in c[1]]


def test_failure_before_publishing_retries_then_stops(setup):
    tmp, qfile, fake, args = setup
    fake.fail_on = "IG1/media"
    for i in range(4):
        pub.main(args + ["run", "--now", NOW.isoformat(), "--failures-out", str(tmp / "f.json")])
        st = json.loads(qfile.read_text())["state"]["day0"]["instagram"]
        f = [x for x in json.loads((tmp / "f.json").read_text()) if x["network"] == "instagram"]
        if i < 3:
            assert st["attempts"] == i + 1 and f[0]["retrying"] is (i < 2)
        else:
            assert st["attempts"] == 3 and f == []


def test_a_run_that_died_mid_publish_is_reported_not_retried(setup):
    tmp, qfile, fake, args = setup
    q = json.loads(qfile.read_text())
    q["state"] = {"day0": {"instagram": {"status": "publishing", "stage": "publish"}}}
    qfile.write_text(json.dumps(q))
    pub.main(args + ["run", "--now", NOW.isoformat(), "--failures-out", str(tmp / "f.json")])
    st = json.loads(qfile.read_text())["state"]["day0"]["instagram"]
    assert st["status"] == "failed"
    assert not [c for c in fake.calls if "IG1/media" in c[1]]


def test_unapproved_queue_publishes_nothing(setup):
    tmp, qfile, fake, args = setup
    (tmp / "board.json").write_text(json.dumps(board_for(json.loads(qfile.read_text()), decision="hold")))
    pub.main(args + ["run", "--now", NOW.isoformat()])
    assert fake.calls == []


def test_plan_needs_no_token_and_no_network(setup, monkeypatch, capsys):
    tmp, qfile, fake, args = setup
    monkeypatch.delenv("META_TOKEN")
    monkeypatch.setattr(pub, "http", lambda *a, **k: pytest.fail("the dry run reached the network"))
    assert pub.main(args + ["plan", "--now", NOW.isoformat()]) == 0
    out = capsys.readouterr().out
    assert "IG_USER_ID/media_publish" in out and "PAGE_ID/photos" in out and "access_token=***" in out
    assert "TOKEN" not in out.replace("access_token", "")
    assert "state" not in json.loads(qfile.read_text())


def test_run_without_a_token_does_nothing(setup, monkeypatch):
    tmp, qfile, fake, args = setup
    monkeypatch.delenv("META_TOKEN")
    assert pub.main(args + ["run", "--now", NOW.isoformat()]) == 0
    assert fake.calls == []


def test_approval_row_shows_every_post_whole(setup):
    tmp, qfile, fake, args = setup
    q = json.loads(qfile.read_text())
    row = pub.approval_row(q, qfile)
    assert row["id"] == "pq-mtgoa-ep03" and row["queue_sha"] == pub.queue_sha(q)
    assert [o["v"] for o in row["options"]] == ["approve", "hold"]
    assert len(row["queue"]["posts"]) == 2
    assert all(p["image_url"].startswith("https://raw.githubusercontent.com/") for p in row["queue"]["posts"])
    assert row["queue"]["posts"][1]["captions"]["facebook"] == "Clip one: https://youtu.be/x"


def test_numbers_are_read_into_the_queue(setup):
    tmp, qfile, fake, args = setup
    pub.main(args + ["run", "--now", NOW.isoformat()])
    pub.main(args + ["numbers", "--now", "2026-11-03T15:30:00+00:00"])
    nums = json.loads(qfile.read_text())["numbers"]["day0"]["instagram"]
    assert "2026-11-03" in nums
