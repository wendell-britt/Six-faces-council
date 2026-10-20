"""A step change the pull has already recorded is not pending (bars-engine's store has no pickup/last, so the
steps_recorded_through line is the only thing that keeps the bar from counting every old tick as unsent)."""
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent / "board"


def test_pending_steps_stop_at_steps_recorded_through():
    html = (HERE / "template.html").read_text()
    assert "t > (DATA.steps_recorded_through || '') && after(t)" in html
