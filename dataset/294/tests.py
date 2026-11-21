import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})


def test_solution():
    matcher = AhoCorasick(["he", "she", "hers", "his"])
    assert matcher.find_all("ushers") == [
        (1, 4, "she"), (2, 4, "he"), (2, 6, "hers")
    ]
    assert matcher.first_match("xxshe") == (2, 5, "she")
    assert matcher.first_match("nomatch") is None
    assert matcher.find_all("") == []
    assert matcher.count_by_pattern("ushers") == {"he": 1, "she": 1, "hers": 1, "his": 0}

    repeated = AhoCorasick(["a", "aa", "aaa"])
    assert len(repeated.find_all("aaaa")) == 9
    assert repeated.count_by_pattern("aaaa") == {"a": 4, "aa": 3, "aaa": 2}
    assert repeated.find_all("a") == [(0, 1, "a")]

    unicode_matcher = AhoCorasick(["ёж", "ж", "ёж"])
    assert unicode_matcher.find_all("ёж") == [(0, 2, "ёж"), (0, 2, "ёж"), (1, 2, "ж")]
    assert unicode_matcher.count_by_pattern("ёж") == {"ёж": 2, "ж": 1}

    for invalid in ([], [""], ["ok", ""], [2]):
        try:
            AhoCorasick(invalid)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid pattern list was accepted")
    try:
        matcher.find_all(None)
    except TypeError:
        pass
    else:
        raise AssertionError("non-string input was accepted")
