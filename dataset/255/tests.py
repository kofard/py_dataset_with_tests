import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert simplify([[1, 2, 3], [4, 5, 6]]) == [[1.0, 2.0, 3.0], [0.0, 0.75, 1.5]]
    assert simplify([[5, 2, 5], [5, 1, 10]]) == [[1.0, 0.4, 1.0], [0.0, 0.2, -1.0]]
    assert solve_simultaneous([[1, 2, 3],[4, 5, 6]]) == [-1.0, 2.0]
    assert solve_simultaneous([[0, -3, 1, 7],[3, 2, -1, 11],[5, 1, -2, 12]]) == [6.4, 1.2, 10.6]
