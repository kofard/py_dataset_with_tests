import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert bfs_shortest_path(demo_graph, "G", "D") == ['G', 'C', 'A', 'B', 'D']
    assert bfs_shortest_path(demo_graph, "G", "G") == ['G']
    assert bfs_shortest_path(demo_graph, "G", "Unknown") == []
    assert bfs_shortest_path_distance(demo_graph, "G", "D") == 4
    assert bfs_shortest_path_distance(demo_graph, "A", "A") == 0
    assert bfs_shortest_path_distance(demo_graph, "A", "Unknown") == -1
