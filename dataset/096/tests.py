import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert Fibonacci().get(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert Fibonacci().get(5) == [0, 1, 1, 2, 3]
