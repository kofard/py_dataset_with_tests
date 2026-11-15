import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert modular_division(4,8,5) == 2
    assert modular_division(3,8,5) == 1
    assert modular_division(4, 11, 5) == 4
    assert invert_modulo(2, 5) == 3
    assert invert_modulo(8,7) == 1
    assert modular_division2(4,8,5) == 2
    assert modular_division2(3,8,5) == 1
    assert modular_division2(4, 11, 5) == 4
    assert extended_gcd(10, 6) == (2, -1, 2)
    assert extended_gcd(7, 5) == (1, -2, 3)
    assert extended_euclid(10, 6) == (-1, 2)
    assert extended_euclid(7, 5) == (-2, 3)
    assert greatest_common_divisor(7,5) == 1
    assert greatest_common_divisor(121, 11) == 11
