import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert kruskal(4, [(0, 1, 3), (1, 2, 5), (2, 3, 1)]) == [(2, 3, 1), (0, 1, 3), (1, 2, 5)]
    assert kruskal(4, [(0, 1, 3), (1, 2, 5), (2, 3, 1), (0, 2, 1), (0, 3, 2)]) == [(2, 3, 1), (0, 2, 1), (0, 1, 3)]
    assert kruskal(4, [(0, 1, 3), (1, 2, 5), (2, 3, 1), (0, 2, 1), (0, 3, 2),
(2, 1, 1)]) == [(2, 3, 1), (0, 2, 1), (2, 1, 1)]
