import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert topology_sort(test_graph_1, 0, 5 * [False]) == [1, 2, 4, 3, 0]
    assert topology_sort(test_graph_2, 0, 6 * [False]) == [2, 1, 5, 4, 3, 0]
    assert find_components({0: [1], 1: [2], 2: [0]}, 0, 5 * [False]) == [0, 1, 2]
    assert find_components({0: [2], 1: [0], 2: [0, 1]}, 0, 6 * [False]) == [0, 2, 1]
    assert strongly_connected_components(test_graph_1) == [[0, 1, 2], [3], [4]]
    assert strongly_connected_components(test_graph_2) == [[0, 2, 1], [3, 5, 4]]
