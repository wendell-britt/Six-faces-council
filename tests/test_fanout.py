"""ts-fanout: a recorded save fires the Board Send routine, and a session start lists the steers it has not seen."""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "board"))
sys.path.insert(0, str(ROOT / "council" / "tools"))
import fire_send  # noqa: E402
import steers  # noqa: E402

PUSHED = """2026-10-24T01:40:00.000Z  positions ts-fanout  stands
2026-10-24T01:41:00.000Z  steer     general
2 saves to record in council/ledger/x.json
pushed to main; now republish board/council-board.html to https://claude.ai/artifact/x without capabilities
"""


def test_rows_only_when_pushed():
    assert fire_send.recorded_rows([PUSHED]) == ["positions/ts-fanout stands", "steer/general"]
    assert fire_send.recorded_rows([PUSHED.replace("pushed to main", "no change to commit")]) == []


def test_no_token_sends_nothing(tmp_path, monkeypatch, capsys):
    monkeypatch.delenv("SEND_ROUTINE_TOKEN", raising=False)
    log = tmp_path / "pull.log"
    log.write_text(PUSHED)
    assert fire_send.main([str(log)]) == 0
    out = capsys.readouterr().out
    assert out.startswith("Board Send at ") and "SEND_ROUTINE_TOKEN is not set" in out


def test_fire_text_starts_like_a_send():
    text = fire_send.fire_text(["questions/q1 a"], datetime(2026, 10, 24, 2, 5, tzinfo=timezone.utc))
    assert text.startswith("Board Send at 02:05 UTC")  # the coordinator's project rule keys on this


DATA = {"resolved": {"positions": {
    "old": {"label": "Stands", "saved_at": "2026-10-01T00:00:00Z", "steer": "old words"},
    "new": {"label": "Overruled", "saved_at": "2026-10-24T01:00:00Z", "steer": "new words"},
    "none": {"label": "Stands", "saved_at": "2026-10-24T01:00:00Z"}}},
    "steers_recorded": [{"text": "general words", "savedAt": "2026-10-24T01:30:00Z"}]}


def test_lists_only_new_steers_and_moves_the_mark(tmp_path, monkeypatch, capsys):
    mark = tmp_path / "seen"
    mark.write_text("2026-10-20T00:00:00\n")
    monkeypatch.setenv("COUNCIL_STEERS_SEEN", str(mark))
    data = tmp_path / "board_data.json"
    data.write_text(json.dumps(DATA))
    steers.main(["--data", str(data)])
    out = capsys.readouterr().out
    assert "2 (" in out and "new words" in out and "general words" in out and "old words" not in out
    steers.main(["--data", str(data)])
    assert capsys.readouterr().out == ""  # seen now


def test_bad_data_never_breaks_a_session_start(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("COUNCIL_STEERS_SEEN", str(tmp_path / "seen"))
    bad = tmp_path / "bad.json"
    bad.write_text("{not json")
    assert steers.main(["--data", str(bad)]) == 0
    assert capsys.readouterr().out == ""
