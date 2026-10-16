"""The ontology term check (ontology/tools/term_lint.py): it catches the retired and reserved terms, leaves valid
WAVE use alone, and today's callsheets, docs and open board rows are clean (pass ontology-flows 1, 2026-10-16)."""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("term_lint", ROOT / "ontology/tools/term_lint.py")
term_lint = importlib.util.module_from_spec(spec)
spec.loader.exec_module(term_lint)


def hits(text):
    return term_lint.scan([("t", text)])


def test_catches_retired_and_reserved_terms():
    for bad in ("the TensionVector of the room", "BARS321TensionVector", "the five WAVE moves",
                "in WAVE order", "elemental WAVE", "the step is stalled on Wendell"):
        assert hits(bad), bad


def test_leaves_valid_use_alone():
    for ok in ("the WAVE room", "a TensionConfiguration", "stopping counts as a complete WAVE",
               "the Tension Map", "the manual W.A.V.E."):
        assert not hits(ok), ok


def test_current_records_are_clean():
    assert term_lint.scan(term_lint.default_texts()) == []
