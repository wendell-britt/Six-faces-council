"""A session with no Artifact tools lands rows without a live page (docs/pickup-here.md, 2026-10-21).

Codex and Freebuff sessions can push to main and cannot save the live board page, so sync_board.py takes --rows on
its own: the row is added onto main, the page is rebuilt, and bars-engine serves it. These tests hold the two halves
of that: the rows still land, and a run that would drop a row on main still stops.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "board" / "sync_board.py"


def run(*args):
    return subprocess.run([sys.executable, str(SCRIPT), *args], cwd=ROOT, capture_output=True, text=True)


def test_rows_alone_is_accepted_and_a_bare_run_is_not():
    bare = run()
    assert bare.returncode != 0
    assert "give --live, --rows, or both" in bare.stderr

    both_checks = run("--check", "--rows", "rows.json")
    assert "give --live, --rows, or both" not in both_checks.stderr


def test_take_live_template_needs_a_live_page():
    r = run("--take-live-template", "--rows", "rows.json")
    assert r.returncode != 0
    assert "--take-live-template needs the live page" in r.stderr


def test_add_rows_adds_a_new_row_without_a_live_page(tmp_path):
    sys.path.insert(0, str(ROOT / "board"))
    import sync_board  # noqa: E402

    data = {"updated": "2026-10-20", "positions": [{"id": "p-one"}], "questions": [], "terms": [], "causes": []}
    rows = {"questions": [{"id": "q-no-claude", "title": "How does a session with no Artifact tools ask?"}],
            "updated": "2026-10-21"}
    report = []
    sync_board.add_rows(data, rows, report)
    assert [q["id"] for q in data["questions"]] == ["q-no-claude"]
    assert data["updated"] == "2026-10-21"
    assert sync_board.ids(data) - sync_board.ids({"positions": data["positions"], "questions": data["questions"]}) == set()


def test_a_row_that_would_replace_another_id_stops_the_run(tmp_path):
    sys.path.insert(0, str(ROOT / "board"))
    import sync_board  # noqa: E402

    rows = tmp_path / "rows.json"
    rows.write_text(json.dumps({"positions": [{"id": "p-one", "title": "different"}]}), encoding="utf-8")
    try:
        sync_board.add_rows({"positions": [{"id": "p-one", "title": "first"}], "questions": [], "terms": [],
                             "causes": []}, json.loads(rows.read_text()), [])
    except SystemExit as e:
        assert "already exists with different content" in str(e)
    else:
        raise AssertionError("a changed row under an existing id was accepted")
