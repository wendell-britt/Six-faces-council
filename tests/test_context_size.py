"""The handoff hook speaks once the main loop's context passes the line, and never breaks a turn."""
import io
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "council" / "tools"))
import context_size  # noqa: E402


def transcript(tmp_path, tokens):
    path = tmp_path / "t.jsonl"
    path.write_text(json.dumps({"message": {"usage": {"input_tokens": 1, "cache_read_input_tokens": tokens}}}) + "\n")
    return path


def run(capsys, event):
    context_size.hook(io.StringIO(json.dumps(event)))
    return capsys.readouterr().out


def test_silent_under_the_line(tmp_path, capsys):
    assert run(capsys, {"transcript_path": str(transcript(tmp_path, 90_000))}) == ""


def test_orders_handoff_past_the_line(tmp_path, capsys):
    out = json.loads(run(capsys, {"transcript_path": str(transcript(tmp_path, 160_000))}))
    assert "HANDOFF LINE PASSED" in out["hookSpecificOutput"]["additionalContext"]


def test_stop_order_past_stop_line(tmp_path, capsys):
    out = run(capsys, {"transcript_path": str(transcript(tmp_path, 230_000))})
    assert "stop after this call" in out


def test_subagent_and_bad_input_are_silent(tmp_path, capsys):
    assert run(capsys, {"transcript_path": str(transcript(tmp_path, 300_000)), "agent_id": "a"}) == ""
    assert context_size.hook(io.StringIO("junk")) == 0
