import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert is_arithmetic_series([2, 4, 6]) == True
    assert is_arithmetic_series([3, 6, 12, 24]) == False
    assert is_arithmetic_series([1, 2, 3]) == True
    assert arithmetic_mean([2, 4, 6]) == 4.0
    assert arithmetic_mean([3, 6, 9, 12]) == 7.5
    assert arithmetic_mean([4, 8, 1]) == 4.333333333333333
    assert arithmetic_mean([1, 2, 3]) == 2.0
