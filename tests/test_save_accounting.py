"""Every save the board-pull Action acknowledges is accounted for (board/fetch_store.py account).

Run 2 of board-pull (2026-10-15 22:22) acknowledged three saves and recorded one, and nothing said what the other two
were. Wendell: "We need to account for these in future". Each pending save now gets one status and a reason, and a
save that is neither on main nor passed over on purpose stays unacknowledged.
"""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "board" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


fs = _load("fetch_store")
pull = _load("pull")

DATA = {"resolved": {"questions": {"np-age-band": {"decision": "high", "saved_at": "2026-10-15T20:00:00Z"}}},
        "steer_recorded_through": "2026-10-15T22:01:10.939Z", "picks": [{"id": "menu-task:a"}],
        "steps_recorded_through": "2026-10-15T22:00:00Z",
        "morning": {"gathered_at": "2026-10-15T21:55:10Z", "sealed": "2026-10-15"}}


def save(i, collection, doc_id, at):
    return {"id": f"s{i}", "collection": collection, "docId": doc_id, "receivedAt": at}


def run(tmp_path, docs, pending, data=DATA, skip=()):
    fs.write_store({"docs": docs, "unrecorded": pending}, tmp_path)
    return {r["id"]: r for r in fs.account(pending, tmp_path, data, pull, skip)}


def test_run_two_older_steer_versions_are_superseded(tmp_path):
    steer = {"text": "Context for the agents", "savedAt": "2026-10-15T22:01:10.939Z"}
    rows = run(tmp_path, {"steer": {"general": steer}},
               [save(1, "steer", "general", "2026-10-15T22:00:01Z"), save(2, "steer", "general", "2026-10-15T22:00:40Z"),
                save(3, "steer", "general", "2026-10-15T22:01:11Z")])
    assert rows["s3"]["status"] == "recorded"
    assert [rows[i]["status"] for i in ("s1", "s2")] == ["superseded", "superseded"]
    assert "s3" in rows["s1"]["why"]


def test_answer_on_main_is_recorded_and_a_new_one_is_unaccounted(tmp_path):
    old = {"choice": "high", "savedAt": "2026-10-15T20:00:00Z"}
    rows = run(tmp_path, {"questions": {"np-age-band": old}}, [save(1, "questions", "np-age-band", "2026-10-15T20:00:01Z")])
    assert rows["s1"]["status"] == "recorded"
    new = {"choice": "low", "savedAt": "2026-10-15T23:00:00Z"}
    rows = run(tmp_path, {"questions": {"np-age-band": new}}, [save(2, "questions", "np-age-band", "2026-10-15T23:00:01Z")])
    assert rows["s2"]["status"] == "unaccounted"


def test_passed_over_on_purpose(tmp_path):
    rows = run(tmp_path, {"questions": {"np-x": {"savedAt": "2026-10-15T20:00:00Z"}},
                          "picks": {"menu-task:b": {"removed": True, "savedAt": "2026-10-15T20:00:00Z"}},
                          "steer": {"general": {"text": " ", "savedAt": "2026-10-15T23:00:00Z"}}},
               [save(1, "questions", "np-x", "a"), save(2, "picks", "menu-task:b", "b"), save(3, "steer", "general", "c")])
    assert {r["status"] for r in rows.values()} == {"nothing-to-record"}


def test_work_for_a_session_is_held_and_except_is_held(tmp_path):
    rows = run(tmp_path, {"morning": {"freewrite": {"text": "raw", "savedAt": "2026-10-15T23:00:00Z"},
                                      "menu": {"items": [], "savedAt": "2026-10-15T23:00:00Z"}},
                          "ttv": {"2026-10-16": {"status": "bars-engine", "savedAt": "2026-10-16T08:00:00Z"}}},
               [save(1, "morning", "freewrite", "a"), save(2, "morning", "menu", "b"), save(3, "ttv", "2026-10-16", "c")],
               skip=("morning/menu",))
    assert rows["s1"]["status"] == "held" and rows["s3"]["status"] == "held"
    assert rows["s2"]["status"] == "held" and "--except" in rows["s2"]["why"]


def test_unknown_collection_is_unaccounted(tmp_path):
    rows = run(tmp_path, {}, [save(1, "mystery", "x", "a")])
    assert rows["s1"]["status"] == "unaccounted"


def test_only_acked_statuses_are_sent():
    assert set(fs.ACKED) == {"recorded", "superseded", "nothing-to-record"}
