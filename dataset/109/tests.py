import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert get_factors(45) == Counter({3: 2, 5: 1})
    assert get_factors(2520) == Counter({2: 3, 3: 2, 5: 1, 7: 1})
    assert get_factors(23) == Counter({23: 1})
    assert get_greatest_common_divisor(18, 45) == 9
    assert get_greatest_common_divisor(23, 37) == 1
    assert get_greatest_common_divisor(2520, 8350) == 10
    assert get_greatest_common_divisor(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == 1
