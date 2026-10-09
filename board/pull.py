#!/usr/bin/env python3
"""Record every answer Wendell saved on the board that main has not recorded, in one step, safe to run twice.

Wendell, 2026-10-07, on pickup-pull-model: pull, not push. Until then a save reached main only when the Send button's
chain of sessions ran a board read, and that chain broke six ways in a day and a half
(council/research/2026-10-07-pickup-hostile-review.md). The answers were safe in the board's store the whole time.
Now any session that has the repo pulls them: the board read a Send starts, the daily run, and any session about to
act on a ruling. Recording takes no judgment, so this script does all of it. Acting on what he said (a steer, an
overrule, a question's pick) stays with the session, which reads the list this prints at the end.

Save the store first with the ArtifactData tool, once per collection, into one folder:
  action list, url https://claude.ai/artifact/DxyShVS8tmvJym4HAsgnho, collection positions (then questions, terms,
  causes, steer, picks), query {"limit": 1000}, out_dir <dir>
Then, from the repo root on main:
  python3 board/pull.py <dir>            # report what would be recorded, write nothing
  python3 board/pull.py <dir> --push     # record, rebuild, commit and push to main
Then republish board/council-board.html to the board URL without passing capabilities.

Running it twice, or in two sessions at once, records the same thing the same way. The ledger file is named after
the newest save it records and holds no time of its own, so two runs that see the same saves write the same file, and
the board merge driver joins resolved entries by id.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA = HERE / "board_data.json"
LEDGER = ROOT / "council" / "ledger"
BOARD_URL = "https://claude.ai/artifact/DxyShVS8tmvJym4HAsgnho"
KINDS = ("positions", "questions", "terms", "causes")

sys.path.insert(0, str(ROOT / "council"))
import due  # noqa: E402  the deferral ladder, so a deferral is recorded the way the board computed it


def git(*a, check=True):
    r = subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)
    if check and r.returncode:
        sys.exit(f"git {' '.join(a)} failed: {r.stderr.strip()}")
    return r


def answer(kind, doc):
    """What he decided, as resolved records it, or '' when the doc holds no decision."""
    if kind == "positions":
        return doc.get("status") or ""
    if kind == "terms":
        return doc.get("action") or ""
    if kind == "causes":
        return "kept" if doc.get("kept") else (doc.get("name") or "")
    choices = [c for c in (doc.get("choices") or []) if c]
    return ", ".join(choices) if choices else (doc.get("choice") or "")


def recorded(entry, doc, ans):
    """Whether main already holds this save. Entries pull.py writes carry saved_at; older ones are judged by date."""
    if not entry:
        return False
    saved = doc.get("savedAt", "")
    if entry.get("saved_at"):
        return saved <= entry["saved_at"]
    if doc.get("deferred"):
        return entry.get("decision") == "deferred" and any(
            h.get("saved_at", "")[:19] >= saved[:19] for h in entry.get("history", []))
    return entry.get("decision") == ans or saved[:10] <= entry.get("recorded", "")


def label(kind, row, doc, ans):
    if kind == "positions":
        return {"stands": "Stands", "overrule": "Overruled", "retire": "Retired"}.get(ans, ans)
    if kind == "questions":
        opts = {o["v"]: o["label"] for o in (row or {}).get("options", [])}
        picked = [c.strip() for c in ans.split(",")] if doc.get("choices") else [ans]
        names = []
        for v in picked:
            name = opts.get(v, v).replace(" (recommended)", "")
            names.append(name.split(". ", 1)[1] if len(name) > 2 and name[1:3] == ". " else name)
        return " and ".join(n for n in names if n) or "Steer only"
    if kind == "terms" and doc.get("rename"):
        return f"{ans}, renamed {doc['rename']}"
    return ans


def find_new(data, store):
    """Every save in the store that main has not recorded, oldest first."""
    rows = {k: {r["id"]: r for r in data.get(k, [])} for k in KINDS}
    resolved = data.get("resolved", {})
    new = []
    for kind in KINDS:
        for f in sorted((store / kind).glob("*.json")):
            doc = json.loads(f.read_text(encoding="utf-8"))
            ans = "deferred" if doc.get("deferred") else answer(kind, doc)
            if not (ans or (doc.get("steer") or "").strip()) or not doc.get("savedAt"):
                continue
            if recorded(resolved.get(kind, {}).get(f.stem), doc, ans):
                continue
            new.append({"kind": kind, "id": f.stem, "doc": doc, "answer": ans, "row": rows[kind].get(f.stem)})
    steer = store / "steer" / "general.json"
    general = None
    if steer.exists():
        g = json.loads(steer.read_text(encoding="utf-8"))
        if (g.get("text") or "").strip() and g.get("savedAt", "") > data.get("steer_recorded_through", ""):
            general = g
    # mm-picks-become-threads: a morning pick he saved is one board row marked as his; the next read starts its thread
    taken = {p["id"] for p in data.get("picks", [])}
    for f in sorted((store / "picks").glob("*.json")) if (store / "picks").is_dir() else []:
        doc = json.loads(f.read_text(encoding="utf-8"))
        if f.stem in taken or doc.get("removed") or not doc.get("savedAt"):
            continue
        new.append({"kind": "picks", "id": f.stem, "doc": doc, "answer": "picked", "row": None})
    new.sort(key=lambda n: n["doc"]["savedAt"])
    return new, general


def apply(data, new, general, ledger_rel):
    """Write resolved entries, deferrals and the general steer onto data. Returns the ledger record."""
    record = f"{ledger_rel} (six-faces-council)"
    answers, work = {}, []
    for n in new:
        kind, rid, doc, ans = n["kind"], n["id"], n["doc"], n["answer"]
        steer = (doc.get("steer") or "").strip()
        answers[rid] = {"kind": kind[:-1], **{k: v for k, v in doc.items() if k != "previous"}}
        if kind == "picks":
            b = doc.get("bridge") or {}
            goal = b.get("goalTitle") or (f"new {b.get('cadence')} goal \"{b.get('title')}\" under {b.get('parentTitle')}"
                                          if b.get("kind") == "new" else "unaligned")
            data.setdefault("picks", []).append({"id": rid, "date": doc.get("date"), "category": doc.get("category"),
                                                 "text": doc.get("text"), "bridge": b, "note": doc.get("note", ""),
                                                 "saved_at": doc["savedAt"], "record": record})
            work.append(f'picks/{rid}: start a thread: "{doc.get("text")}" (goal: {goal})'
                        + (f' (note: "{doc["note"]}")' if doc.get("note") else ""))
            continue
        if doc.get("deferred"):
            due.record(data, kind, rid, doc["savedAt"], doc.get("until") or "spaced", steer, record, doc.get("hours"))
            data["resolved"][kind][rid]["saved_at"] = doc["savedAt"]
            continue
        entry = {"decision": ans or "steer", "label": label(kind, n["row"], doc, ans), "recorded": doc["savedAt"][:10],
                 "saved_at": doc["savedAt"], "record": record}
        if steer:
            entry["steer"] = steer
        for k in ("faces", "pass"):  # proc-record-face: so an overrule can be traced to the face that made the row
            if (n["row"] or {}).get(k):
                entry[k] = n["row"][k]
        data.setdefault("resolved", {}).setdefault(kind, {})[rid] = entry
        if kind == "questions" or ans in ("overrule", "retire") or steer or n["row"] is None:
            work.append(f"{kind}/{rid}: {entry['label']}" + (f' (steer: "{steer}")' if steer else "")
                        + ("" if n["row"] else " [no row on main; it came from another board version]"))
    if general:
        data.setdefault("steers_recorded", []).append({"text": general["text"], "savedAt": general["savedAt"],
                                                       "record": record})
        data["steer_recorded_through"] = general["savedAt"]
        work.append(f'steer/general: "{general["text"]}"')
    newest = max([n["doc"]["savedAt"] for n in new] + ([general["savedAt"]] if general else []))
    data["updated"] = max(data.get("updated", ""), newest[:10])
    return {"date": newest[:10], "kind": "board-pull", "newest_save": newest, "answers": answers,
            "steer": general, "needs_work": work,
            "note": "Recorded by board/pull.py. needs_work lists what a session still has to act on."}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("store", help="folder the ArtifactData reads saved the store into")
    ap.add_argument("--push", action="store_true", help="record, commit and push to main")
    a = ap.parse_args()
    store = Path(a.store)
    if not (store / "positions").is_dir() and not (store / "questions").is_dir():
        sys.exit(f"{store} holds no positions or questions folder; save the store first (see --help)")
    if a.push:
        if git("status", "--porcelain", "--untracked-files=no").stdout.strip():
            sys.exit("the work tree has changes of its own; commit or stash them first")
        if git("rev-parse", "--is-shallow-repository").stdout.strip() == "true":
            git("fetch", "-q", "--unshallow", "origin")  # a shallow cloud checkout cannot merge main (board-read-slim)
        git("checkout", "-q", "main")
        git("pull", "-q", "--no-rebase", "origin", "main")
    data = json.loads(DATA.read_text(encoding="utf-8"))
    new, general = find_new(data, store)
    if not new and not general:
        print("every saved answer is recorded")
        return
    for n in new:
        print(f"{n['doc']['savedAt']}  {n['kind']:<9} {n['id']}  {n['answer'] or 'steer'}")
    if general:
        print(f"{general['savedAt']}  steer     general")
    newest = max([n["doc"]["savedAt"] for n in new] + ([general["savedAt"]] if general else []))
    name = f"{newest[:10]}-pull-{newest[11:19].replace(':', '')}.json"
    ledger_rel = f"council/ledger/{name}"
    led = apply(data, new, general, ledger_rel)
    print(f"{len(new) + bool(general)} saves to record in {ledger_rel}")
    if led["needs_work"]:
        print("needs work:\n  " + "\n  ".join(led["needs_work"]))
    if not a.push:
        print("(report only; pass --push to record)")
        return
    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (LEDGER / name).write_text(json.dumps(led, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    subprocess.run([sys.executable, str(HERE / "build_board.py")], cwd=ROOT, check=True, capture_output=True)
    git("add", "board", str(LEDGER / name))
    if git("diff", "--cached", "--quiet", check=False).returncode == 0:
        print("no change to commit")
        return
    git("commit", "-q", "-m", f"Board pull: {len(new) + bool(general)} saves through {newest}")
    for _ in range(3):
        if git("push", "-q", "origin", "main", check=False).returncode == 0:
            print(f"pushed to main; now republish board/council-board.html to {BOARD_URL} without capabilities")
            return
        git("pull", "-q", "--no-rebase", "origin", "main")   # the board merge driver joins rows by id
        subprocess.run([sys.executable, str(HERE / "build_board.py")], cwd=ROOT, check=True, capture_output=True)
        git("add", "board/council-board.html")
        git("commit", "-q", "-m", "Board: rebuild after merging main", check=False)
    sys.exit("push to main failed three times; run git pull --no-rebase origin main and push by hand")


if __name__ == "__main__":
    main()
