import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert fibonacci_with_matrix_exponentiation(1, 5, 6) == 5
    assert fibonacci_with_matrix_exponentiation(2, 10, 11) == 11
    assert fibonacci_with_matrix_exponentiation(13, 0, 1) == 144
    assert fibonacci_with_matrix_exponentiation(10, 5, 9) == 411
    assert fibonacci_with_matrix_exponentiation(9, 2, 3) == 89
    assert simple_fibonacci(1, 5, 6) == 5
    assert simple_fibonacci(2, 10, 11) == 11
    assert simple_fibonacci(13, 0, 1) == 144
    assert simple_fibonacci(10, 5, 9) == 411
    assert simple_fibonacci(9, 2, 3) == 89
