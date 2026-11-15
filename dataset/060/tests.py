import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert extended_euclid(10, 6) == (-1, 2)
    assert extended_euclid(7, 5) == (-2, 3)
    assert chinese_remainder_theorem(5,1,7,3) == 31
    assert chinese_remainder_theorem(6,1,4,3) == 14
    assert invert_modulo(2, 5) == 3
    assert invert_modulo(8,7) == 1
    assert chinese_remainder_theorem2(5,1,7,3) == 31
    assert chinese_remainder_theorem2(6,1,4,3) == 14
