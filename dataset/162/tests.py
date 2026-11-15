import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert median_of_five([2, 4, 5, 7, 899]) == 5
    assert median_of_five([5, 7, 899, 54, 32]) == 32
    assert median_of_five([5, 4, 3, 2]) == 4
    assert median_of_five([3, 5, 7, 10, 2]) == 5
    assert median_of_medians([2, 4, 5, 7, 899, 54, 32]) == 54
    assert median_of_medians([5, 7, 899, 54, 32]) == 32
    assert median_of_medians([5, 4, 3, 2]) == 4
    assert median_of_medians([3, 5, 7, 10, 2, 12]) == 12
    assert quick_select([2, 4, 5, 7, 899, 54, 32], 5) == 32
    assert quick_select([2, 4, 5, 7, 899, 54, 32], 1) == 2
    assert quick_select([5, 4, 3, 2], 2) == 3
    assert quick_select([3, 5, 7, 10, 2, 12], 3) == 5
