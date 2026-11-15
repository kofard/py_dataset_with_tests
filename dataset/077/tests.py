import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert decimal_to_fraction(2) == (2, 1)
    assert decimal_to_fraction(89.) == (89, 1)
    assert decimal_to_fraction("67") == (67, 1)
    assert decimal_to_fraction("45.0") == (45, 1)
    assert decimal_to_fraction(1.5) == (3, 2)
    assert decimal_to_fraction("6.25") == (25, 4)
    assert decimal_to_fraction(0) == (0, 1)
    assert decimal_to_fraction(-2.5) == (-5, 2)
    assert decimal_to_fraction(0.125) == (1, 8)
    assert decimal_to_fraction(1000000.25) == (4000001, 4)
    assert decimal_to_fraction(1.3333) == (13333, 10000)
    assert decimal_to_fraction("1.23e2") == (123, 1)
    assert decimal_to_fraction("0.500") == (1, 2)
