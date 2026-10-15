"""The board-save contract (schema/board-save.schema.json) against its fixtures.

bars-engine checks the same fixtures with its own validator (src/lib/__tests__/board-save-contract.test.ts), so the
page, the API and pull.py agree on what a save is. A fixture changes here and in bars-engine's fixtures/board-saves
together; test_bars_engine_copy_matches fails until they do (it runs where ../bars-engine is checked out).
"""
import json
from pathlib import Path

import jsonschema
import pytest

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = json.loads((ROOT / "schema" / "board-save.schema.json").read_text())
FIX = ROOT / "tests" / "fixtures" / "board-saves"
validator = jsonschema.Draft202012Validator(SCHEMA)


def test_schema_is_valid():
    jsonschema.Draft202012Validator.check_schema(SCHEMA)


@pytest.mark.parametrize("path", sorted((FIX / "valid").glob("*.json")), ids=lambda p: p.stem)
def test_valid(path):
    errors = [e.message for e in validator.iter_errors(json.loads(path.read_text()))]
    assert not errors, errors


@pytest.mark.parametrize("path", sorted((FIX / "invalid").glob("*.json")), ids=lambda p: p.stem)
def test_invalid(path):
    assert not validator.is_valid(json.loads(path.read_text())), f"{path.name} should be refused"


def test_store_layout_round_trip(tmp_path):
    """A save that passes the contract lands where pull.py reads it: <store>/<collection>/<docId>.json."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("fetch_store", ROOT / "board" / "fetch_store.py")
    fs = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fs)
    docs = {}
    for p in sorted((FIX / "valid").glob("*.json")):
        s = json.loads(p.read_text())
        docs.setdefault(s["collection"], {})[s["docId"]] = s["data"]
    fs.write_store({"docs": docs}, tmp_path)
    assert json.loads((tmp_path / "questions" / "np-age-band.json").read_text())["choice"] == "high"
    assert (tmp_path / "picks" / "menu-task:cmv9yesei000213u0weuoya6f.json").exists()
    for kind in fs.STORE_DIRS:
        assert (tmp_path / kind).is_dir()


def test_bars_engine_copy_matches():
    other = ROOT.parent / "bars-engine" / "fixtures" / "board-saves"
    if not other.is_dir():
        pytest.skip("no ../bars-engine checkout")
    mine = {p.relative_to(FIX).as_posix(): p.read_text() for p in FIX.rglob("*.json")}
    mine["board-save.schema.json"] = (ROOT / "schema" / "board-save.schema.json").read_text()
    theirs = {p.relative_to(other).as_posix(): p.read_text() for p in other.rglob("*.json")}
    assert mine == theirs, "fixtures/board-saves in bars-engine differs from this repo's contract"
