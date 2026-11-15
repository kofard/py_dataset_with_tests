import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert is_safe(0, 1, [[0,1],[1,0]], 2, [0,1]) == False
    assert is_safe(0, 2, [[0,1],[1,0]], 2, [0,1]) == True
    assert solve(0, [0]*3, 3, 3, [[0,1,0],[1,0,1],[0,1,0]]) == True
    assert solve(0, [0]*3, 2, 3, [[0,1,0],[1,0,1],[0,1,0]]) == True
    assert graph_coloring([[0,1,1],[1,0,1],[1,1,0]], 3, 3) == True
    assert graph_coloring([[0,1,1],[1,0,1],[1,1,0]], 2, 3) == False
