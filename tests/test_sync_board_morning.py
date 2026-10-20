"""sync_board takes a gathered morning whole: the later gather wins, and a stale live page never merges its categories
into today's (2026-10-20, the 10-14 morning came back through the sync)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "board"))
import sync_board  # noqa: E402


def morning(date, keys):
    return {"date": date, "gathered_at": f"{date}T08:00:00Z", "categories": [{"key": k, "items": []} for k in keys]}


def test_stale_live_morning_is_not_merged():
    main = {"morning": morning("2026-10-20", ["board", "prs"])}
    live = {"morning": morning("2026-10-14", ["board", "menu"])}
    out = sync_board.union(main, live, [])
    assert out["morning"] == main["morning"]


def test_later_live_morning_wins_whole():
    main = {"morning": morning("2026-10-14", ["board", "menu"])}
    live = {"morning": morning("2026-10-20", ["prs"])}
    report = []
    out = sync_board.union(main, live, report)
    assert out["morning"] == live["morning"]
    assert report == ["from live: morning (later snapshot)"]
