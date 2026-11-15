import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    g = {
    0: [(1, 3), (2, 8), (4, -4)],
    1: [(3, 1), (4, 7)],
    2: [(1, 4)],
    3: [(0, 2), (2, -5)],
    4: [(3, 6)],
}
    assert round(johnson(g)[0][3], 2) == 2.0
