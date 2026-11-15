import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert num_digits(12345) == 5
    assert num_digits(123) == 3
    assert num_digits(0) == 1
    assert num_digits(-1) == 1
    assert num_digits(-123456) == 6
    assert num_digits_fast(12345) == 5
    assert num_digits_fast(123) == 3
    assert num_digits_fast(1000) == 4
    assert num_digits_fast(10**15) == 16
    assert num_digits_fast(0) == 1
    assert num_digits_fast(-1) == 1
    assert num_digits_fast(-123456) == 6
    assert num_digits_faster(12345) == 5
    assert num_digits_faster(123) == 3
    assert num_digits_faster(0) == 1
    assert num_digits_faster(-1) == 1
    assert num_digits_faster(-123456) == 6
