import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    from math import isclose, sin
    assert all(isclose(maclaurin_sin(x, 50), sin(x)) for x in range(-25, 25)) == True
    assert maclaurin_sin(10) == -0.5440211108893691
    assert maclaurin_sin(-10) == 0.5440211108893704
    assert maclaurin_sin(10, 15) == -0.544021110889369
    assert maclaurin_sin(-10, 15) == 0.5440211108893704
    from math import isclose, cos
    assert all(isclose(maclaurin_cos(x, 50), cos(x)) for x in range(-25, 25)) == True
    assert maclaurin_cos(5) == 0.2836621854632268
    assert maclaurin_cos(-5) == 0.2836621854632265
    assert maclaurin_cos(10, 15) == -0.8390715290764524
    assert maclaurin_cos(-10, 15) == -0.8390715290764521
