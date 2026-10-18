"""council/toolbox.yaml is what rung 3 of the tool ladder reads (docs/tool-scout.md)."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "council" / "tools"))
import scout  # noqa: E402

KEYS = {"id", "does", "tags", "where", "licence", "status"}
STATUSES = {"in_use", "vendored", "available", "gated", "rejected"}


def test_every_tool_is_complete():
    ids = [t["id"] for t in scout.tools()]
    assert len(ids) == len(set(ids))
    for t in scout.tools():
        assert KEYS <= set(t), t["id"]
        assert t["status"] in STATUSES, t["id"]
        assert t["tags"], t["id"]


def test_jobs_we_hand_built_find_their_tool():
    assert "rigify" in [t["id"] for t in scout.match("rig the daemon bodies")]
    assert "blender-cloth-bake" in [t["id"] for t in scout.match("robe sleeve cloth jitter")]
    assert "cmu-mocap" in [t["id"] for t in scout.match("animate a walk from mocap")]
