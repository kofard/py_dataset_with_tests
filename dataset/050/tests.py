import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    bms = BoyerMooreSearch(text="ABAABA", pattern="AB")
    assert bms.match_in_pattern("B") == 1
    bms = BoyerMooreSearch(text="ABAABA", pattern="AB")
    assert bms.mismatch_in_text(2) == 3
    bms = BoyerMooreSearch(text="ABAABA", pattern="AB")
    assert bms.bad_character_heuristic() == [0, 3]
    bms = BoyerMooreSearch(text="AAAAA", pattern="AB")
    assert bms.bad_character_heuristic() == []
    bms = BoyerMooreSearch(text="ABABAB", pattern="ABA")
    assert bms.bad_character_heuristic() == [0, 2]
    bms = BoyerMooreSearch(text="", pattern="AB")
    assert bms.bad_character_heuristic() == []
    bms2 = BoyerMooreSearch(text="AAAAAA", pattern="AA")
    assert bms2.bad_character_heuristic() == [0, 1, 2, 3, 4]
    bms3 = BoyerMooreSearch(text="ABCDEF", pattern="XY")
    assert bms3.bad_character_heuristic() == []
