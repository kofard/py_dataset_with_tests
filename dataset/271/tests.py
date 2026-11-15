import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    sam = SuffixAutomaton("abacaba")
    assert sam.contains("abac") == True
    assert sam.contains("caba") == True
    assert sam.contains("xyz") == False
    assert sam.count_distinct_substrings() == 21
    assert sam.count_occurrences("aba") == 2
    assert sam.count_occurrences("a") == 4
    sam = SuffixAutomaton("banana")
    assert sam.contains("nan") == True
    assert sam.contains("apple") == False
    sam = SuffixAutomaton("abc")
    assert sam.count_distinct_substrings() == 6
    assert SuffixAutomaton("aaaa").count_distinct_substrings() == 4
    sam = SuffixAutomaton("banana")
    assert sam.count_occurrences("an") == 2
    assert sam.count_occurrences("na") == 2
    assert sam.count_occurrences("banana") == 1
    assert sam.count_occurrences("xyz") == 0
