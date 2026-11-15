import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert count_inversions_bf([1, 4, 2, 4, 1]) == 4
    assert count_inversions_bf([1, 1, 2, 4, 4]) == 0
    assert count_inversions_bf([]) == 0
    assert count_inversions_recursive([1, 4, 2, 4, 1]) == ([1, 1, 2, 4, 4], 4)
    assert count_inversions_recursive([1, 1, 2, 4, 4]) == ([1, 1, 2, 4, 4], 0)
    assert count_inversions_recursive([]) == ([], 0)
    assert _count_cross_inversions([1, 2, 3], [0, 2, 5]) == ([0, 1, 2, 2, 3, 5], 4)
    assert _count_cross_inversions([1, 2, 3], [3, 4, 5]) == ([1, 2, 3, 3, 4, 5], 0)
