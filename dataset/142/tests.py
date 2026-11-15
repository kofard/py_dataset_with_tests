import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert levenshtein_distance("planet", "planetary") == 3
    assert levenshtein_distance("", "test") == 4
    assert levenshtein_distance("book", "back") == 2
    assert levenshtein_distance("book", "book") == 0
    assert levenshtein_distance("test", "") == 4
    assert levenshtein_distance("", "") == 0
    assert levenshtein_distance("orchestration", "container") == 10
    assert levenshtein_distance_optimized("planet", "planetary") == 3
    assert levenshtein_distance_optimized("", "test") == 4
    assert levenshtein_distance_optimized("book", "back") == 2
    assert levenshtein_distance_optimized("book", "book") == 0
    assert levenshtein_distance_optimized("test", "") == 4
    assert levenshtein_distance_optimized("", "") == 0
    assert levenshtein_distance_optimized("orchestration", "container") == 10
