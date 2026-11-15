import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert ucal(1, 2) == 0
    assert ucal(1.1, 2) == 0.11000000000000011
    assert ucal(1.2, 2) == 0.23999999999999994
