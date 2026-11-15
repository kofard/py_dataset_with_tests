import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert prime_factors(100) == [2, 2, 5, 5]
    assert number_of_divisors(100) == 9
    assert sum_of_divisors(100) == 217
    assert euler_phi(100) == 40
