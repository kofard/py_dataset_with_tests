import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert quick_select([2, 4, 5, 7, 899, 54, 32], 5) == 54
    assert quick_select([2, 4, 5, 7, 899, 54, 32], 1) == 4
    assert quick_select([5, 4, 3, 2], 2) == 4
    assert quick_select([3, 5, 7, 10, 2, 12], 3) == 7
    assert median([3, 2, 2, 9, 9]) == 3
    assert median([2, 2, 9, 9, 9, 3]) == 6.0
