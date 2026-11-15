import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert euclidean_distance([0, 0], [3, 4]) == 5.0
    assert euclidean_distance([1, 1], [1, 1]) == 0.0
    validate_graph({"A": [10, 20], "B": [30, 21], "C": [15, 35]})  # Valid graph
    graph = {"A": [10, 20], "B": [30, 21], "C": [15, 35]}
    assert travelling_salesman_brute_force(graph) == (['A', 'B', 'C', 'A'], 56.35465722402588)
    graph = {"A": [10, 20], "B": [30, 21], "C": [15, 35]}
    assert travelling_salesman_dynamic_programming(graph) == (['A', 'C', 'B', 'A'], 56.35465722402587)
