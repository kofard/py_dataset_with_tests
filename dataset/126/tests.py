import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert jaro_winkler("martha", "marhta") == 0.9611111111111111
    assert jaro_winkler("CRATE", "TRACE") == 0.7333333333333334
    assert jaro_winkler("test", "dbdbdbdb") == 0.0
    assert jaro_winkler("test", "test") == 1.0
    assert jaro_winkler("hello world", "HeLLo W0rlD") == 0.6363636363636364
    assert jaro_winkler("test", "") == 0.0
    assert jaro_winkler("hello", "world") == 0.4666666666666666
    assert jaro_winkler("hell**o", "*world") == 0.4365079365079365
    assert round(jaro_winkler("aa ", "aa"), 6) == 0.911111
    assert round(jaro_winkler("a a", "aa"), 6) == 0.9
    assert round(jaro_winkler("aabb", "bab"), 6) == 0.722222
