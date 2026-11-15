import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert bfs(test_graph, 0, 5, [-1] * 6) == True
    assert bfs([[0, 0], [0, 0]], 0, 1, [-1, -1]) == False
    assert mincut(test_graph, source=0, sink=5) == [(1, 3), (4, 3), (4, 5)]
    assert sum(test_graph[u][v] for u, v in mincut(test_graph, 0, 5)) == 23
    assert mincut([[0, 7], [0, 0]], source=0, sink=1) == [(0, 1)]
