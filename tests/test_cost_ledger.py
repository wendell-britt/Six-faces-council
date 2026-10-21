"""The ledger reproduces the 18 October audit: $627.64 over 107 sessions, 63 past 200,000 tokens."""
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "council" / "tools"))
import cost_ledger  # noqa: E402

AUDIT = Path("/mnt/project-files/usage-audit/sessions-2026-10-18.jsonl")


def row(i, tokens, cost, title="Build x"):
    return {"id": i, "title": title, "updated_at": "2026-10-20T00:00:00Z", "used_tokens": tokens,
            "last_served_model": "m", "usage": {"cost_usd": cost}}


def test_counts_and_skips_errors():
    s = cost_ledger.summarize([row("a", 100_000, 1), row("b", 250_000, 3), {"id": "c", "error": "gone"}])
    assert (s["sessions"], s["skipped"], s["all"]["cost"], s["all"]["past_200k"], s["all"]["past_150k"]) == (2, 1, 4, 1, 1)
    assert s["targets"]["share_past_200k"] == 0.5


def test_ledger_merge_keeps_later_row(tmp_path):
    p = tmp_path / "r.jsonl"
    old, new = row("a", 1, 1), row("a", 2, 2)
    new["updated_at"] = "2026-10-21T00:00:00Z"
    p.write_text(json.dumps(new) + "\n" + json.dumps(old) + "\n")
    assert cost_ledger.load([p])[0]["used_tokens"] == 2


@pytest.mark.skipif(not AUDIT.exists(), reason="project files not mounted")
def test_reproduces_the_audit():
    s = cost_ledger.summarize(cost_ledger.load([AUDIT]))
    assert (s["sessions"], s["all"]["cost"], s["all"]["past_200k"], s["all"]["cost_past_200k"]) == (107, 627.64, 63, 503.65)
