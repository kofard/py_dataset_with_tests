import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert longest_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]) == [10, 22, 33, 41, 60, 80]
    assert longest_subsequence([4, 8, 7, 5, 1, 12, 2, 3, 9]) == [1, 2, 3, 9]
    assert longest_subsequence([28, 26, 12, 23, 35, 39]) == [12, 23, 35, 39]
    assert longest_subsequence([9, 8, 7, 6, 5, 7]) == [5, 7]
    assert longest_subsequence([1, 1, 1]) == [1, 1, 1]
    assert longest_subsequence([]) == []
