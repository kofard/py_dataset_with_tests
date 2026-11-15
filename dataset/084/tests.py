import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert differentiate(lambda x: x**2, 2, 2) == 2
    assert differentiate(lambda x: x**2 * x**4, 9, 2) == 196830
    assert differentiate(lambda y: 0.5 * (y + 3) ** 6, 3.5, 4) == 7605.0
    assert differentiate(lambda y: y ** 2, 4, 3) == 0
