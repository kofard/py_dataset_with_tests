import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert comb_sort([0, 5, 3, 2, 2]) == [0, 2, 2, 3, 5]
    assert comb_sort([]) == []
    assert comb_sort([99, 45, -7, 8, 2, 0, -15, 3]) == [-15, -7, 0, 2, 3, 8, 45, 99]
    assert comb_sort([2, 0, 3, 4, 5, 6, 1]) == [0, 1, 2, 3, 4, 5, 6]
    assert comb_sort(["c", "a", "b"]) == ['a', 'b', 'c']
    assert comb_sort([2.5, -1, 0.0]) == [-1, 0.0, 2.5]
