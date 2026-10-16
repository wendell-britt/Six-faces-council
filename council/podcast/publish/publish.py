#!/usr/bin/env python3
"""Publishes approved podcast posts to Instagram and the Facebook Page through Meta's Graph API.

Pass podcast-pipeline2 (council/passes/6FACE_PASS_podcast-pipeline2_2026-10-16.md). Each episode's posts sit in
council/podcast/queue/<episode>.json (schema/publish-queue.schema.json). Wendell approves the whole queue once on the
board, and .github/workflows/publish-queue.yml runs this every fifteen minutes. Nothing here schedules on Meta's side:
Instagram has no scheduling field, so a post goes out on the run after its time.

  publish.py check                      validate every queue, show its hash, approval and what is due (no network)
  publish.py plan [--now T]             the dry run: every call a live run would make, with no network and no token
  publish.py run [--now T]              publish what is due in approved queues and write the ids back (META_TOKEN)
  publish.py numbers [--now T]          read each published post's insights into the queue (pa-numbers-auto)
  publish.py accounts                   the Page and Instagram account the token reaches (setup step 03's check)
  publish.py container-test --clip C --cover P
                                        the gate before episode 3: one Reel container uploaded and FINISHED,
                                        never published. C is a local path or release:<tag>/<asset>.
  publish.py approval-row <queue> [--write]
                                        the board question that approves a queue, with every post shown whole

Approval (pa-approval-publishes): the queue's approval_row is answered "approve" in board/board_data.json and the
row's queue_sha equals the queue's hash now. Any change to a post changes the hash, and nothing in that queue
publishes until a new row is approved. The hash covers `episode` and `posts`; `state` and `numbers` are ours.

The token is META_TOKEN, a system user token Wendell pastes into the repo's secrets (pa-token-in-secrets). It is
never printed. The Page and Instagram ids come from it through /me/accounts; META_PAGE_ID picks one Page if it
reaches several. META_GRAPH_VERSION sets the API version.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
QUEUE_DIR = ROOT / "council" / "podcast" / "queue"
BOARD = ROOT / "board" / "board_data.json"
REPO = os.environ.get("GITHUB_REPOSITORY", "wendell-britt/six-faces-council")
VERSION = os.environ.get("META_GRAPH_VERSION", "v24.0")
GRAPH = "https://graph.facebook.com"
RUPLOAD = "https://rupload.facebook.com"
MISS_HOURS = 6        # a post more than this late is marked missed, never published late without him
MAX_ATTEMPTS = 3      # retries only for failures before the publish call, so nothing goes out twice
POLL_SECONDS, POLL_TRIES = 10, 60
PLACEHOLDER = re.compile(r"\[[a-z][a-z ]*\]")   # [episode link] and the like must be filled before approval


# ---------- the queue ----------

def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def save(path, q):
    Path(path).write_text(json.dumps(q, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def queue_sha(q):
    body = json.dumps({"episode": q["episode"], "posts": q["posts"]}, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"))
    return hashlib.sha256(body.encode()).hexdigest()


def when(s):
    t = dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
    if t.tzinfo is None:
        raise ValueError(f"time without an offset: {s}")
    return t


def raw_url(path):
    return f"https://raw.githubusercontent.com/{REPO}/main/{path}"


def validate(q, name="queue", root=ROOT):
    """Problems with a queue, as plain sentences. An empty list means it is fit to approve."""
    out = []
    for k in ("episode", "approval_row", "posts"):
        if k not in q:
            out.append(f"{name}: missing {k}")
    if out:
        return out
    if not re.fullmatch(r"pq-[a-z0-9-]+", q["approval_row"]):
        out.append(f"{name}: approval_row must look like pq-<episode>")
    ids = set()
    for p in q["posts"]:
        pid = p.get("id", "?")
        where = f"{name} post {pid}"
        if pid in ids:
            out.append(f"{where}: id used twice")
        ids.add(pid)
        try:
            when(p.get("at", ""))
        except ValueError as e:
            out.append(f"{where}: {e}")
        nets = p.get("networks") or []
        if not nets or set(nets) - {"instagram", "facebook"}:
            out.append(f"{where}: networks must be instagram and/or facebook")
        for n in nets:
            cap = (p.get("captions") or {}).get(n)
            if not cap:
                out.append(f"{where}: no {n} caption")
            elif PLACEHOLDER.search(cap):
                out.append(f"{where}: the {n} caption still holds {PLACEHOLDER.search(cap).group(0)}")
            elif n == "instagram" and len(cap) > 2200:
                out.append(f"{where}: the Instagram caption is over 2,200 characters")
        if len(p.get("collaborators") or []) > 3:
            out.append(f"{where}: at most three collaborators")
        if p.get("kind") == "reel":
            clip = p.get("clip") or {}
            if not (clip.get("path") or (clip.get("release") and clip.get("asset"))):
                out.append(f"{where}: a Reel needs clip.release and clip.asset")
            out += _jpeg(root, p.get("cover"), f"{where}: cover")
        elif p.get("kind") == "image":
            out += _jpeg(root, p.get("image"), f"{where}: image")
        else:
            out.append(f"{where}: kind must be reel or image")
    return out


def _jpeg(root, rel, what):
    if not rel:
        return [f"{what} is missing"]
    f = Path(root) / rel
    if not f.is_file():
        return [f"{what} {rel} is not in the repo"]
    head = f.read_bytes()[:3]
    if head != b"\xff\xd8\xff":
        return [f"{what} {rel} is not a JPEG (Meta's cover_url takes JPEG only)"]
    if f.stat().st_size > 8 * 1024 * 1024:
        return [f"{what} {rel} is over 8 MB"]
    return []


def approval(q, board):
    """(approved, why) for a queue against the board data."""
    row = next((r for r in board.get("questions", []) if r.get("id") == q["approval_row"]), None)
    if row is None:
        return False, f"no board row {q['approval_row']}"
    if row.get("queue_sha") != queue_sha(q):
        return False, f"{q['approval_row']} approved a different version of the queue; a changed post needs a new row"
    ans = (board.get("resolved", {}).get("questions", {}) or {}).get(q["approval_row"])
    if not ans:
        return False, f"{q['approval_row']} is not answered yet"
    if ans.get("decision") != "approve":
        return False, f"{q['approval_row']} answered {ans.get('decision')!r}, not approve"
    return True, f"approved {ans.get('recorded', '')}".strip()


def due(q, now):
    """Each (post, network, action) a run at `now` acts on: publish, or mark missed."""
    out = []
    for p in q["posts"]:
        t = when(p["at"])
        if t > now:
            continue
        for n in p["networks"]:
            st = q.get("state", {}).get(p["id"], {}).get(n, {})
            if st.get("status") in ("published", "missed", "publishing"):
                continue
            if st.get("status") == "failed" and (st.get("stage") == "publish" or st.get("attempts", 0) >= MAX_ATTEMPTS):
                continue
            late = (now - t).total_seconds() / 3600
            out.append((p, n, "missed" if late > MISS_HOURS else "publish"))
    return out


def queues(qdir):
    return sorted(Path(qdir).glob("*.json"))


# ---------- the Graph API ----------

class GraphError(Exception):
    pass


def http(method, url, data=None, headers=None):
    """One HTTP call. Returns parsed JSON. Tests replace this."""
    req = urllib.request.Request(url, data=data, method=method, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            body = r.read()
    except urllib.error.HTTPError as e:
        body = e.read()
        try:
            err = json.loads(body).get("error", {})
            msg = f"{err.get('type', 'HTTP')} {err.get('code', e.code)}: {err.get('message', '')}"
        except ValueError:
            msg = f"HTTP {e.code}"
        raise GraphError(msg) from None
    return json.loads(body) if body else {}


class Graph:
    def __init__(self, token, call=None, sleep=time.sleep):
        self.token, self.call, self.sleep = token, call or http, sleep

    def get(self, path, token=None, **params):
        params["access_token"] = token or self.token
        return self.call("GET", f"{GRAPH}/{VERSION}/{path}?{urllib.parse.urlencode(params)}")

    def post(self, path, token=None, **params):
        params["access_token"] = token or self.token
        data = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None}).encode()
        return self.call("POST", f"{GRAPH}/{VERSION}/{path}", data,
                         {"Content-Type": "application/x-www-form-urlencoded"})

    def upload(self, url, blob, token=None):
        return self.call("POST", url, blob, {"Authorization": f"OAuth {token or self.token}", "offset": "0",
                                             "file_size": str(len(blob))})

    def multipart(self, path, fields, file_field, filename, blob, token=None):
        b = uuid.uuid4().hex
        parts = [f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode()
                 for k, v in {**fields, "access_token": token or self.token}.items()]
        parts.append(f'--{b}\r\nContent-Disposition: form-data; name="{file_field}"; filename="{filename}"\r\n'
                     f'Content-Type: image/jpeg\r\n\r\n'.encode() + blob + f"\r\n--{b}--\r\n".encode())
        return self.call("POST", f"{GRAPH}/{VERSION}/{path}", b"".join(parts),
                         {"Content-Type": f"multipart/form-data; boundary={b}"})

    def accounts(self):
        pages = self.get("me/accounts", fields="id,name,access_token,instagram_business_account").get("data", [])
        want = os.environ.get("META_PAGE_ID")
        if want:
            pages = [p for p in pages if p["id"] == want]
        if len(pages) != 1:
            names = ", ".join(f"{p.get('name')} ({p['id']})" for p in pages) or "none"
            raise GraphError(f"the token reaches {len(pages)} matching Pages ({names}); set META_PAGE_ID to one")
        p = pages[0]
        ig = (p.get("instagram_business_account") or {}).get("id")
        return {"page_id": p["id"], "page_name": p.get("name", ""), "page_token": p.get("access_token"),
                "ig_user_id": ig}

    def wait_container(self, cid):
        for _ in range(POLL_TRIES):
            st = self.get(cid, fields="status_code,status")
            code = st.get("status_code")
            if code in ("FINISHED", "PUBLISHED"):
                return code
            if code in ("ERROR", "EXPIRED"):
                raise GraphError(f"container {cid} {code}: {st.get('status', '')}")
            self.sleep(POLL_SECONDS)
        raise GraphError(f"container {cid} not FINISHED after {POLL_TRIES * POLL_SECONDS} seconds")


# ---------- one post on one network ----------

_CLIPS = {}


def clip_bytes(clip, fetch=None):
    """The clip's bytes, from a local path or this repo's release asset, fetched once per run."""
    if clip.get("path"):
        return Path(clip["path"]).read_bytes()
    url = f"https://github.com/{REPO}/releases/download/{clip['release']}/{clip['asset']}"
    if fetch:
        return fetch(url)
    if url not in _CLIPS:
        with urllib.request.urlopen(url, timeout=300) as r:
            _CLIPS[url] = r.read()
    return _CLIPS[url]


def ig_container(g, acct, p, blob=None):
    """Creates and uploads an Instagram container, waits for FINISHED, returns its id. Does not publish."""
    ig = acct["ig_user_id"]
    if not ig:
        raise GraphError("the Page has no Instagram professional account linked")
    cap = p["captions"]["instagram"]
    collab = json.dumps(p["collaborators"]) if p.get("collaborators") else None
    if p["kind"] == "image":
        c = g.post(f"{ig}/media", image_url=raw_url(p["image"]), caption=cap, collaborators=collab)
    else:
        c = g.post(f"{ig}/media", media_type="REELS", upload_type="resumable", caption=cap,
                   cover_url=raw_url(p["cover"]), share_to_feed=str(p.get("share_to_feed", True)).lower(),
                   collaborators=collab)
        g.upload(c.get("uri") or f"{RUPLOAD}/ig-api-upload/{VERSION}/{c['id']}", blob)
    g.wait_container(c["id"])
    return c["id"]


def publish_one(g, acct, p, net, st, root=ROOT, fetch=None, checkpoint=lambda: None):
    """Publishes p on net, writing progress into st as it goes. checkpoint() saves the queue just before the call
    that publishes, so a run that dies there leaves "publishing" on record and the next run never posts it twice."""
    blob = clip_bytes(p["clip"], fetch) if p["kind"] == "reel" else None
    if net == "instagram":
        st["stage"] = "container"
        cid = ig_container(g, acct, p, blob)
        st.update(stage="publish", container=cid, status="publishing")
        checkpoint()
        r = g.post(f"{acct['ig_user_id']}/media_publish", creation_id=cid)
        st.update(status="published", id=r["id"])
        try:
            st["permalink"] = g.get(r["id"], fields="permalink").get("permalink")
        except GraphError:
            pass
        return
    page, ptok = acct["page_id"], acct["page_token"]
    cap = p["captions"]["facebook"]
    if p["kind"] == "image":
        st.update(stage="publish", status="publishing")
        checkpoint()
        r = g.post(f"{page}/photos", token=ptok, url=raw_url(p["image"]), message=cap, published="true")
        st.update(status="published", id=r.get("post_id") or r["id"])
        return
    st["stage"] = "upload"
    s = g.post(f"{page}/video_reels", token=ptok, upload_phase="start")
    vid = s["video_id"]
    st["video_id"] = vid
    g.upload(s.get("upload_url") or f"{RUPLOAD}/video-upload/{VERSION}/{vid}", blob, token=ptok)
    try:
        cover = (Path(root) / p["cover"]).read_bytes()
        g.multipart(f"{vid}/thumbnails", {"is_preferred": "true"}, "source", Path(p["cover"]).name, cover, ptok)
    except (GraphError, OSError) as e:
        st["warning"] = f"cover not set: {e}"
    st.update(stage="publish", status="publishing")
    checkpoint()
    g.post(f"{page}/video_reels", token=ptok, upload_phase="finish", video_id=vid, video_state="PUBLISHED",
           description=cap)
    st.update(status="published", id=vid)


# ---------- commands ----------

def now_arg(s):
    return when(s) if s else dt.datetime.now(dt.timezone.utc)


def stamp(t):
    return t.astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def cmd_check(a):
    board = load(a.board) if Path(a.board).exists() else {}
    bad = 0
    for f in queues(a.queue_dir):
        q = load(f)
        probs = validate(q, f.name, a.root)
        ok, why = approval(q, board) if not probs else (False, "invalid")
        print(f"{f.name}: sha {queue_sha(q)[:12]} · {why}")
        for x in probs:
            print("  " + x)
        bad += bool(probs)
        for p, n, act in (due(q, now_arg(a.now)) if not probs else []):
            print(f"  due: {p['id']} on {n} ({act})")
    return 1 if bad else 0


def cmd_plan(a):
    """The offline dry run. Prints the calls a live run would make, in order, with no network and no token."""
    board, now = load(a.board), now_arg(a.now)
    calls = []

    def fake(method, url, data=None, headers=None):
        shown = re.sub(r"access_token=[^&]*", "access_token=***", url)
        if data and "multipart" in (headers or {}).get("Content-Type", ""):
            shown += f"  <form with the cover JPEG, {len(data)} bytes>"
        elif data and b"access_token" in data[:4000]:
            body = re.sub(rb"access_token=[^&]*", b"access_token=***", data)
            shown += "  " + body.decode(errors="replace")[:300]
        elif data:
            shown += f"  <{len(data)} bytes>"
        calls.append(f"{method} {shown}")
        if "me/accounts" in url:
            return {"data": [{"id": "PAGE_ID", "name": "(the Page)", "access_token": "PAGE_TOKEN",
                              "instagram_business_account": {"id": "IG_USER_ID"}}]}
        if "fields=status_code" in url:
            return {"status_code": "FINISHED"}
        if "upload_phase=start" in (data or b"").decode(errors="ignore"):
            return {"video_id": "VIDEO_ID"}
        return {"id": "NEW_ID", "uri": None}

    g = Graph("TOKEN", call=fake, sleep=lambda s: None)
    acct = None
    for f in queues(a.queue_dir):
        q = load(f)
        probs = validate(q, f.name, a.root)
        ok, why = approval(q, board) if not probs else (False, "invalid: " + "; ".join(probs))
        print(f"{f.name}: {why}")
        if not ok:
            continue
        for p, n, act in due(q, now):
            print(f"  {p['id']} on {n}: {act}")
            if act != "publish":
                continue
            acct = acct or g.accounts()
            calls.clear()
            publish_one(g, acct, p, n, {}, a.root, fetch=lambda u: b"\0" * 1024)
            for c in calls:
                print("    " + c)
    return 0


def cmd_run(a):
    token = os.environ.get("META_TOKEN")
    if not token:
        print("META_TOKEN is not set; nothing published (setup steps meta-publishing-setup 01-03)")
        return 0
    board, now = load(a.board), now_arg(a.now)
    g = Graph(token)
    acct, failures = None, []
    for f in queues(a.queue_dir):
        q = load(f)
        probs = validate(q, f.name, a.root)
        if probs:
            print(f"{f.name}: invalid, skipped: " + "; ".join(probs))
            continue
        ok, why = approval(q, board)
        if not ok:
            print(f"{f.name}: {why}")
            continue
        changed = False
        for pid, nets in (q.get("state") or {}).items():
            for n, st in nets.items():
                if st.get("status") == "publishing":
                    # an earlier run died at the publishing call: it may or may not have gone out, so never retry
                    st.update(status="failed", error="an earlier run stopped at the publishing call; check the "
                              "account before approving it again")
                    p = next(x for x in q["posts"] if x["id"] == pid)
                    failures.append(_failure(f, p, n, st))
                    changed = True
        for p, n, act in due(q, now):
            st = q.setdefault("state", {}).setdefault(p["id"], {}).setdefault(n, {})
            changed = True
            if act == "missed":
                st.update(status="missed", at=stamp(now),
                          error=f"more than {MISS_HOURS} hours late when the timer reached it; not posted late")
                failures.append(_failure(f, p, n, st))
                continue
            st["attempts"] = st.get("attempts", 0) + 1
            try:
                acct = acct or g.accounts()
                publish_one(g, acct, p, n, st, a.root, checkpoint=lambda: save(f, q))
                st["at"] = stamp(dt.datetime.now(dt.timezone.utc))
                st.pop("error", None)
                print(f"{f.name}: {p['id']} published on {n} ({st['id']})")
                if st.get("warning"):
                    failures.append(_failure(f, p, n, st))
            except (GraphError, OSError, KeyError) as e:
                st.update(status="failed", error=str(e), at=stamp(dt.datetime.now(dt.timezone.utc)))
                print(f"{f.name}: {p['id']} FAILED on {n} at {st.get('stage')}: {e}")
                failures.append(_failure(f, p, n, st))
            save(f, q)
        if changed:
            save(f, q)
    if a.failures_out:
        Path(a.failures_out).write_text(json.dumps(failures, ensure_ascii=False, indent=1))
    return 0


def _failure(f, p, n, st):
    retry = st.get("status") == "failed" and st.get("stage") != "publish" and st.get("attempts", 0) < MAX_ATTEMPTS
    return {"queue": f"council/podcast/queue/{f.name}", "post": p["id"], "title": p.get("title", p["id"]),
            "network": n, "at": p["at"], "status": st.get("status"), "stage": st.get("stage"),
            "error": st.get("error") or st.get("warning"), "retrying": retry}


METRICS = {"instagram": "views,reach,likes,comments,saved,shares,total_interactions",
           "facebook": "blue_reels_play_count,post_impressions_unique,post_video_likes_by_reaction_type"}


def cmd_numbers(a):
    token = os.environ.get("META_TOKEN")
    if not token:
        print("META_TOKEN is not set; no numbers read")
        return 0
    g, day = Graph(token), now_arg(a.now).date().isoformat()
    acct = None
    for f in queues(a.queue_dir):
        q = load(f)
        changed = False
        for pid, nets in (q.get("state") or {}).items():
            for n, st in nets.items():
                if st.get("status") != "published":
                    continue
                kind = next((p["kind"] for p in q["posts"] if p["id"] == pid), "reel")
                try:
                    if n == "instagram":
                        r = g.get(f"{st['id']}/insights", metric=METRICS[n])
                    elif kind == "reel":
                        acct = acct or g.accounts()
                        r = g.get(f"{st['id']}/video_insights", token=acct["page_token"], metric=METRICS[n])
                    else:
                        continue
                    vals = {m["name"]: (m.get("values") or [{}])[0].get("value", m.get("total_value", {}).get("value"))
                            for m in r.get("data", [])}
                except GraphError as e:
                    vals = {"error": str(e)}
                q.setdefault("numbers", {}).setdefault(pid, {}).setdefault(n, {})[day] = vals
                changed = True
                print(f"{f.name}: {pid} {n} {vals}")
        if changed:
            save(f, q)
    return 0


def cmd_accounts(a):
    token = os.environ.get("META_TOKEN")
    if not token:
        print("META_TOKEN is not set")
        return 1
    acct = Graph(token).accounts()
    print(f"Page: {acct['page_name']} ({acct['page_id']})")
    print(f"Instagram account: {acct['ig_user_id'] or 'none linked to this Page'}")
    return 0 if acct["ig_user_id"] else 1


def cmd_container_test(a):
    """The gate before episode 3 (pass podcast-pipeline2): a Reel container reaches FINISHED and is not published."""
    token = os.environ.get("META_TOKEN")
    if not token:
        print("META_TOKEN is not set; the container test needs it")
        return 1
    if a.clip.startswith("release:"):
        tag, _, asset = a.clip[len("release:"):].partition("/")
        clip = {"release": tag, "asset": asset}
    else:
        clip = {"path": a.clip}
    probs = _jpeg(a.root, a.cover, "cover")
    if probs:
        print("; ".join(probs))
        return 1
    p = {"id": "container-test", "kind": "reel", "clip": clip, "cover": a.cover,
         "captions": {"instagram": "Container test. Not published."}, "share_to_feed": True}
    g = Graph(token)
    acct = g.accounts()
    cid = ig_container(g, acct, p, clip_bytes(clip))
    print(f"PASS: container {cid} is FINISHED on {acct['page_name']}'s Instagram and was not published.")
    print("It expires unpublished after 24 hours.")
    return 0


def approval_row(q, qfile):
    sha = queue_sha(q)
    posts = []
    for p in sorted(q["posts"], key=lambda p: when(p["at"])):
        img = p.get("cover") if p["kind"] == "reel" else p.get("image")
        posts.append({"id": p["id"], "title": p.get("title", p["id"]), "at": p["at"], "kind": p["kind"],
                      "networks": p["networks"], "captions": {n: p["captions"][n] for n in p["networks"]},
                      "image_url": raw_url(img) if img else "",
                      "clip": (p.get("clip") or {}).get("asset", ""),
                      "collaborators": p.get("collaborators", [])})
    n = len(posts)
    first, last = posts[0]["at"][:10], posts[-1]["at"][:10]
    return {
        "id": q["approval_row"], "faces": ["regent", "shaman"], "pass": "podcast pipeline 2",
        "q": f"Publish {q.get('title') or q['episode']}: these {n} posts as shown, each on its date from {first} to {last}?",
        "why_you": "Posting under your name is reserved to you, and your approval here is the publishing act "
                   "(pa-approval-publishes). Every post is shown whole below. A change to any post after you "
                   "approve sends it back to you as a new row. Source: council/passes/6FACE_PASS_podcast-pipeline2_2026-10-16.md",
        "not_before": f"The queue was finished on {dt.date.today().isoformat()}; it could not be shown whole before.",
        "options": [
            {"v": "approve", "label": "Approve; publish them on their dates",
             "c": "The timer posts each one to the networks shown, within fifteen minutes of its time, with its cover and caption."},
            {"v": "hold", "label": "Hold; change something first",
             "c": "Nothing goes out. Say what to change in the steer box and the queue comes back as a new row."},
        ],
        "queue": {"file": f"council/podcast/queue/{Path(qfile).name}", "sha": sha, "posts": posts},
        "queue_sha": sha,
    }


def cmd_approval_row(a):
    q = load(a.queue)
    probs = validate(q, Path(a.queue).name, a.root)
    if probs:
        print("\n".join(probs))
        return 1
    row = approval_row(q, a.queue)
    if not a.write:
        print(json.dumps(row, ensure_ascii=False, indent=1))
        return 0
    board = load(a.board)
    if row["id"] in (board.get("resolved", {}).get("questions") or {}):
        print(f"{row['id']} is already answered; give the changed queue a new approval_row (e.g. {row['id']}-2)")
        return 1
    board["questions"] = [r for r in board.get("questions", []) if r.get("id") != row["id"]] + [row]
    Path(a.board).write_text(json.dumps(board, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {row['id']} to {a.board}; rebuild with board/build_board.py and republish")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--queue-dir", default=str(QUEUE_DIR))
    ap.add_argument("--board", default=str(BOARD))
    ap.add_argument("--root", default=str(ROOT), help="repo root the cover and image paths are read from")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("check", "plan", "run", "numbers"):
        s = sub.add_parser(name)
        s.add_argument("--now", help="ISO time to act as if it were (tests, plans)")
        if name == "run":
            s.add_argument("--failures-out", help="write this run's failures here as JSON, for the workflow")
    sub.add_parser("accounts")
    s = sub.add_parser("container-test")
    s.add_argument("--clip", required=True)
    s.add_argument("--cover", required=True, help="repo path of a cover JPEG on main")
    s = sub.add_parser("approval-row")
    s.add_argument("queue")
    s.add_argument("--write", action="store_true")
    a = ap.parse_args(argv)
    return {"check": cmd_check, "plan": cmd_plan, "run": cmd_run, "numbers": cmd_numbers, "accounts": cmd_accounts,
            "container-test": cmd_container_test, "approval-row": cmd_approval_row}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
