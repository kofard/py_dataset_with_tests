import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert is_prime(2) == True
    assert is_prime(15) == False
    assert is_prime(19) == True
    assert is_prime(1) == False
    assert is_prime(-7) == False
    assert next_prime(2) == 3
    assert next_prime(7) == 11
    assert next_prime(14) == 17
    assert next_prime(0) == 2
    assert next_prime(-10) == 2
