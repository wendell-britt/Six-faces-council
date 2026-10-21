"""council/unchosen_read.py: the checks on the council's weekly read of the unchosen lines (uc-who-reads B)."""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "council"))
import unchosen_read as ur  # noqa: E402

PILE = {
    "weekOf": "2026-10-19", "readThisWeek": False,
    "lines": [
        {"day": "2026-10-20", "text": "Walk the garden before calls", "fate": "unpicked"},
        {"day": "2026-10-17", "text": "Plant the garlic in the back garden", "fate": "raw"},
        {"day": "2026-10-13", "text": "Record a podcast intro", "fate": "raw"},
    ],
    "pitches": [],
}


def garden(pitch="Put ten minutes in the back garden on the next dry morning."):
    return {"word": "Gardens", "face": "shaman", "kernel": "The garden asks for hands in the morning.", "pitch": pitch,
            "quotes": [{"day": "2026-10-20", "text": "Walk the garden before calls"},
                       {"day": "2026-10-17", "text": "plant the garlic in the back  garden"}]}


def test_a_good_read_checks():
    assert ur.check(PILE, [garden()]) == []


def test_words_fold_like_bars_engine():
    assert ur.pattern_words("The Gardens' beds, and the bed") == ["garden", "beds"]


def test_quotes_are_his_lines_from_two_mornings():
    one = dict(garden(), quotes=garden()["quotes"][:1])
    assert any("1 morning(s)" in p for p in ur.check(PILE, [one]))
    made_up = dict(garden(), quotes=garden()["quotes"] + [{"day": "2026-10-13", "text": "The garden calls"}])
    assert any("word for word" in p for p in ur.check(PILE, [made_up]))
    other = dict(garden(), quotes=garden()["quotes"] + [{"day": "2026-10-13", "text": "Record a podcast intro"}])
    assert any('does not hold the word "garden"' in p for p in ur.check(PILE, [other]))


def test_at_most_five_and_once_a_week():
    assert any("at most 5" in p for p in ur.check(PILE, [garden()] * 6))
    assert any("read already" in p for p in ur.check(dict(PILE, readThisWeek=True), [garden()]))


def test_voice_and_no_conversion():
    assert any("speaks about him" in p for p in ur.check(PILE, [dict(garden(), kernel="You keep avoiding it.")]))
    assert any("uc-links-by-hand" in p for p in ur.check(PILE, [garden("Make the garden a spirit.")]))


def test_a_returning_pattern_needs_a_new_pitch():
    pile = dict(PILE, pitches=[{"word": "garden", "pitch": "Sketch the beds.", "weekOf": "2026-10-12"}])
    assert any("needs a new pitch" in p for p in ur.check(pile, [garden("Sketch the beds.")]))
    assert ur.check(pile, [garden()]) == []
    assert ur.returning(pile, [garden()]) == ["garden"]


def test_the_pile_never_lands_in_the_repository(tmp_path):
    with pytest.raises(SystemExit):
        ur.outside_repo(ur.ROOT / "council" / "pile.json")
    assert ur.outside_repo(tmp_path / "pile.json") == (tmp_path / "pile.json").resolve()


def test_stop_words_match_bars_engine():
    ts = (ur.ROOT.parent / "bars-engine" / "src" / "lib" / "tap-the-vein" / "unchosen.ts")
    if not ts.is_file():
        pytest.skip("bars-engine is not checked out beside the council")
    text = ts.read_text(encoding="utf-8")
    block = text[text.index("const STOP"):text.index(".split(' ')")]
    words = set(" ".join(part for part in block.split("'")[1::2]).split())
    assert words == ur.STOP
