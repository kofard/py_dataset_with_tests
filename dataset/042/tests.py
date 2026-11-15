import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert bisection(lambda x: x ** 3 - 1, -5, 5) == 1.0000000149011612
    assert bisection(lambda x: x ** 2 - 4 * x + 3, 0, 2) == 1.0
    assert bisection(lambda x: x ** 2 - 4 * x + 3, 2, 4) == 3.0
