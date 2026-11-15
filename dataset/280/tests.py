import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert triplet_sum1([13, 29, 7, 23, 5], 35) == (5, 7, 23)
    assert triplet_sum1([37, 9, 19, 50, 44], 65) == (9, 19, 37)
    arr = [6, 47, 27, 1, 15]
    target = 11
    assert triplet_sum1(arr, target) == (0, 0, 0)
    assert triplet_sum2([13, 29, 7, 23, 5], 35) == (5, 7, 23)
    assert triplet_sum2([37, 9, 19, 50, 44], 65) == (9, 19, 37)
    arr = [6, 47, 27, 1, 15]
    target = 11
    assert triplet_sum2(arr, target) == (0, 0, 0)
