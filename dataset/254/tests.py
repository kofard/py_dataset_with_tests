import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert round(method_2([0, 2, 4], 10), 10) == 2.6666666667
    assert round(method_2([2, 0], 10), 10) == -0.2666666667
    assert round(method_2([-2, -1], 10), 10) == 2.172
    assert round(method_2([0, 1], 10), 10) == 0.3333333333
    assert round(method_2([0, 2], 10), 10) == 2.6666666667
    assert round(method_2([0, 2], 100), 10) == 2.5621226667
    assert round(method_2([0, 1], 1000), 10) == 0.3320026653
