import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert match_pattern("aab", "c*a*b") == True
    assert match_pattern("dabc", "*abc") == False
    assert match_pattern("aaa", "aa") == False
    assert match_pattern("aaa", "a.a") == True
    assert match_pattern("aaab", "aa*") == False
    assert match_pattern("aaab", ".*") == True
    assert match_pattern("a", "bbbb") == False
    assert match_pattern("", "bbbb") == False
    assert match_pattern("a", "") == False
    assert match_pattern("", "") == True
