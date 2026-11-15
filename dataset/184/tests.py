import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert find_narcissistic_numbers(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert find_narcissistic_numbers(160) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153]
    assert find_narcissistic_numbers(400) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371]
    assert find_narcissistic_numbers(1000) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
    assert find_narcissistic_numbers(10000) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474]
    assert find_narcissistic_numbers(1) == [0]
    assert find_narcissistic_numbers(0) == []
