import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert estimate_pi(100, 1) == 3.2
    assert estimate_pi(1000, 11) == 3.156
    assert estimate_pi(1000000, 111) == 3.139892
