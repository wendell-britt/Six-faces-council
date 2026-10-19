"""The move table (schema/move-table.json): one fact for what a move does, read by every surface.

bars-engine keeps a copy at src/lib/quest-grammar/move-table.json and sprout at data/move-table.json, each with its own
test that its engine lands in the cells this table names. A change lands here and in both copies together;
test_copy_matches fails until it does (it runs where ../bars-engine or ../sprout is checked out).
"""
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
TABLE_PATH = ROOT / "schema" / "move-table.json"
T = json.loads(TABLE_PATH.read_text())
CHANNELS = [c["id"] for c in T["channels"]]
ELEMENT = {c["id"]: c["element"] for c in T["channels"]}


def apply(move_id, channel, state):
    move = next(m for m in T["moves"] if m["id"] == move_id)
    assert move["from"] == channel, f"{move_id} starts from {move['from']}, not {channel}"
    new_state = T["families"][move["family"]]["state"][state]
    return None if new_state is None else (move["to"], new_state)


def test_fifteen_moves_five_per_family():
    assert len(T["moves"]) == 15
    assert len({m["id"] for m in T["moves"]}) == 15
    for fam in T["families"]:
        assert sum(m["family"] == fam for m in T["moves"]) == 5


def test_every_family_says_every_state():
    for fam, rule in T["families"].items():
        assert set(rule["state"]) == set(T["states"]), fam
        assert all(v is None or v in T["states"] for v in rule["state"].values()), fam


def test_moves_follow_the_cycles():
    for m in T["moves"]:
        rule = T["families"][m["family"]]["channel"]
        expected = m["from"] if rule == "same" else T["cycles"][rule][m["from"]]
        assert m["to"] == expected, m["id"]
        assert m["id"] == (f"{ELEMENT[m['from']]}_transcend" if rule == "same" else f"{ELEMENT[m['from']]}_{ELEMENT[m['to']]}")


def test_each_channel_one_move_per_family():
    for fam in T["families"]:
        assert sorted(m["from"] for m in T["moves"] if m["family"] == fam) == sorted(CHANNELS)


def test_rulings_hold():
    # mn-transcend-plus-two overruled: two steps, never dissatisfied to satisfied in one.
    assert T["families"]["transcend"]["state"]["dissatisfied"] == "neutral"
    # mn-q-ke-state = depends: control never raises a state.
    order = T["states"]
    for start, end in T["families"]["control"]["state"].items():
        assert order.index(end) <= order.index(start)
    # mn-gold-names
    names = {c["id"]: c for c in T["channels"]}
    assert names["fear"]["satisfied_name"] == "Wonder-Excitement"
    assert names["neutrality"]["name"] == "Neutrality"


def test_owned_moves_name_real_moves():
    ids = {m["id"] for m in T["moves"]}
    for kind in ("faces", "daemons"):
        for owner, moves in T["owners"][kind].items():
            assert set(moves) <= ids, owner


@pytest.mark.parametrize("check", T["checks"], ids=lambda c: c["id"])
def test_checks(check):
    got = apply(check["move"], check["from"]["channel"], check["from"]["state"])
    assert got == (check["ends"]["channel"], check["ends"]["state"])


@pytest.mark.parametrize("repo,rel", [
    ("bars-engine", "src/lib/quest-grammar/move-table.json"),
    ("sprout", "data/move-table.json"),
])
def test_copy_matches(repo, rel):
    other = ROOT.parent / repo / rel
    if not (ROOT.parent / repo).is_dir():
        pytest.skip(f"../{repo} not checked out")
    assert other.is_file(), f"{repo} has no copy at {rel}"
    assert json.loads(other.read_text()) == T, f"{repo}'s {rel} differs from schema/move-table.json"
