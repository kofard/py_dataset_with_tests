import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    def f(x): return x**3 - x - 2
    assert round(brent_method(f, 1, 2), 5) == 1.52138
    def f2(x): return x**2 + 1
