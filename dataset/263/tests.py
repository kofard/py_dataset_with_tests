import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert all(abs(square_root_iterative(i) - math.sqrt(i)) <= 1e-14 for i in range(500)) == True
    assert square_root_iterative(4) == 2.0
    assert square_root_iterative(3.2) == 1.788854381999832
    assert square_root_iterative(140) == 11.832159566199232
