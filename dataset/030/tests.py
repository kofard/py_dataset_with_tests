import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    edges = [(2, 1, -10), (3, 2, 3), (0, 3, 5), (0, 1, 4)]
    g = [{"src": s, "dst": d, "weight": w} for s, d, w in edges]
    assert bellman_ford(g, 4, 4, 0) == [0.0, -2.0, 8.0, 5.0]
    g = [{"src": s, "dst": d, "weight": w} for s, d, w in edges + [(1, 3, 5)]]
