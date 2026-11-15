import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert sum_of_digits(12345) == 15
    assert sum_of_digits(123) == 6
    assert sum_of_digits(-123) == 6
    assert sum_of_digits(0) == 0
    assert sum_of_digits_recursion(12345) == 15
    assert sum_of_digits_recursion(123) == 6
    assert sum_of_digits_recursion(-123) == 6
    assert sum_of_digits_recursion(0) == 0
    assert sum_of_digits_compact(12345) == 15
    assert sum_of_digits_compact(123) == 6
    assert sum_of_digits_compact(-123) == 6
    assert sum_of_digits_compact(0) == 0
