import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert largest_divisible_subset([1, 16, 7, 8, 4]) == [16, 8, 4, 1]
    assert largest_divisible_subset([1, 2, 3]) == [2, 1]
    assert largest_divisible_subset([-1, -2, -3]) == [-3]
    assert largest_divisible_subset([1, 2, 4, 8]) == [8, 4, 2, 1]
    assert largest_divisible_subset((1, 2, 4, 8)) == [8, 4, 2, 1]
    assert largest_divisible_subset([1, 1, 1]) == [1, 1, 1]
    assert largest_divisible_subset([0, 0, 0]) == [0, 0, 0]
    assert largest_divisible_subset([-1, -1, -1]) == [-1, -1, -1]
    assert largest_divisible_subset([]) == []
