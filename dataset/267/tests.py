import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert strand_sort([4, 2, 5, 3, 0, 1]) == [0, 1, 2, 3, 4, 5]
    assert strand_sort([4, 2, 5, 3, 0, 1], reverse=True) == [5, 4, 3, 2, 1, 0]
    assert strand_sort(["banana", "apple", "cherry"]) == ['apple', 'banana', 'cherry']
