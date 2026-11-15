import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    graph = {0: [1, 2], 1: [3], 2: [3], 3: [4, 5], 4: [], 5: []}
    assert topological_sort(graph) == [0, 1, 2, 3, 4, 5]
    graph_with_cycle = {0: [1], 1: [2], 2: [0]}
    topological_sort(graph_with_cycle)
    sparse_graph = {10: [20], 20: []}
    assert topological_sort(sparse_graph) == [10, 20]
    sparse_cycle = {10: [20], 20: [10]}
    topological_sort(sparse_cycle)
