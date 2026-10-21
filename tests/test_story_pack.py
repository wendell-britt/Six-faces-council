"""The story pack check (council/story/check.py): a pack agrees with the faces, the moves, the tools and the places.

The fixture is `tests/fixtures/story-pack/beats.yaml`; each test breaks one rule on a copy and expects the finding.
"""
import copy
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "council" / "story"))
import check as story_check  # noqa: E402

FIXTURE = ROOT / "tests" / "fixtures" / "story-pack" / "beats.yaml"
BASE = yaml.safe_load(FIXTURE.read_text(encoding="utf-8"))
TABLES = story_check.tables()


def findings():
    return story_check.check_pack(copy.deepcopy(BASE), TABLES)


def beat(data, beat_id):
    return next(b for b in data["beats"] if b["id"] == beat_id)


def test_fixture_passes():
    assert findings() == []
    assert story_check.summary(BASE).startswith("ok fixture-carry: 3 beats, 4 assets")


def test_registries_say_what_the_pack_relies_on():
    assert TABLES["faces"] == {"shaman", "architect", "challenger", "regent", "diplomat", "sage"}
    assert {"water_wood", "fire_transcend", "water_transcend"} <= TABLES["moves"]
    assert TABLES["places"] >= {"sprout", "root", "between", "vessel", "cave"}
    assert TABLES["tools"]["kenney"]["status"] == "available"


def test_dangling_next_is_refused():
    data = copy.deepcopy(BASE)
    beat(data, "a2-carry")["next"] = ["a9-nowhere"]
    assert any("next names 'a9-nowhere'" in f for f in story_check.check_pack(data, TABLES))


def test_unreachable_beat_is_refused():
    data = copy.deepcopy(BASE)
    beat(data, "a2-carry")["next"] = []
    assert any("no route from the pack's entry" in f for f in story_check.check_pack(data, TABLES))


def test_two_outcomes_are_refused():
    data = copy.deepcopy(BASE)
    beat(data, "a3-fire")["choices"] = [
        {"line": "Say it out loud.", "outcome": "right"},
        {"line": "Swallow it.", "outcome": "wrong"},
    ]
    assert any("missing a partial line" in f for f in story_check.check_pack(data, TABLES))


def test_encounter_without_choices_is_refused():
    data = copy.deepcopy(BASE)
    beat(data, "a3-fire")["choices"] = []
    assert any("an encounter needs its choices" in f for f in story_check.check_pack(data, TABLES))


def test_move_the_face_does_not_own_is_refused():
    data = copy.deepcopy(BASE)
    beat(data, "a2-carry")["move"] = "fire_transcend"
    assert any("shaman does not own fire_transcend" in f for f in story_check.check_pack(data, TABLES))


def test_unknown_move_is_refused():
    data = copy.deepcopy(BASE)
    beat(data, "a2-carry")["move"] = "harvest_moon"
    assert any("is not in schema/move-table.json" in f for f in story_check.check_pack(data, TABLES))


def test_beat_without_a_record_is_refused():
    data = copy.deepcopy(BASE)
    beat(data, "a4-hollow")["cites"] = []
    assert any("needs cites" in f for f in story_check.check_pack(data, TABLES))


def test_unknown_place_is_refused():
    data = copy.deepcopy(BASE)
    beat(data, "a4-hollow")["place"] = "the-moon"
    assert any("is not in calrunia/world.yaml" in f for f in story_check.check_pack(data, TABLES))


def test_rejected_tool_is_refused():
    data = copy.deepcopy(BASE)
    beat(data, "a2-carry")["needs"][0]["tool"] = "agent-beacon"
    assert any("rejected in the toolbox" in f for f in story_check.check_pack(data, TABLES))


def test_gated_tool_must_be_a_board_step():
    data = copy.deepcopy(BASE)
    need = beat(data, "a3-fire")["needs"][0]
    need["tool"], need["status"] = "mixamo", "brief"
    assert any("is gated, so this need is a board step" in f for f in story_check.check_pack(data, TABLES))


def test_need_without_a_brief_is_refused():
    data = copy.deepcopy(BASE)
    beat(data, "a4-hollow")["needs"][0]["brief"] = " "
    assert any("needs a brief" in f for f in story_check.check_pack(data, TABLES))


def test_built_need_names_its_ref():
    data = copy.deepcopy(BASE)
    beat(data, "a2-carry")["needs"][0]["status"] = "built"
    assert any("a built need names its ref" in f for f in story_check.check_pack(data, TABLES))


def test_repeated_asset_id_is_refused():
    data = copy.deepcopy(BASE)
    beat(data, "a4-hollow")["needs"][0]["id"] = "prop-crate"
    assert any("asset id already used" in f for f in story_check.check_pack(data, TABLES))


def test_quote_longer_than_a_line_is_refused():
    data = copy.deepcopy(BASE)
    beat(data, "a2-carry")["quote"] = " ".join(["word"] * 45)
    assert any("one line is the limit" in f for f in story_check.check_pack(data, TABLES))


def test_entry_must_be_a_beat():
    data = copy.deepcopy(BASE)
    data["entry"] = "a0-missing"
    assert any("is not a beat id" in f for f in story_check.check_pack(data, TABLES))


def test_command_reports_a_pack_outside_the_repo(tmp_path, capsys):
    bad = tmp_path / "beats.yaml"
    data = copy.deepcopy(BASE)
    beat(data, "a2-carry")["next"] = ["a9-nowhere"]
    bad.write_text(yaml.safe_dump(data), encoding="utf-8")
    assert story_check.main([str(bad)]) == 1
    out = capsys.readouterr().out
    assert out.startswith("FAIL")
    assert "next names 'a9-nowhere'" in out


def test_gated_assets_are_counted_in_the_summary():
    data = copy.deepcopy(BASE)
    need = beat(data, "a3-fire")["needs"][0]
    need["tool"], need["status"] = "mixamo", "gated"
    assert story_check.check_pack(data, TABLES) == []
    assert story_check.summary(data).endswith("1 waiting on a board step")
