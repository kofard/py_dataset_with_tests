import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert get_parent_position(1) == 0
    assert get_parent_position(2) == 0
    assert get_child_left_position(0) == 1
    assert get_child_right_position(0) == 2
    queue = MinPriorityQueue()
    queue.push(1, 1000)
    queue.push(2, 100)
    queue.push(3, 4000)
    queue.push(4, 3000)
    assert queue.extract_min() == 2
    queue.update_key(4, 50)
    assert queue.extract_min() == 4
    assert queue.extract_min() == 1
    assert queue.extract_min() == 3
    graph = GraphUndirectedWeighted()
    graph.add_edge("a", "b", 3)
    graph.add_edge("b", "c", 10)
    graph.add_edge("c", "d", 5)
    graph.add_edge("a", "c", 15)
    graph.add_edge("b", "d", 100)
    dist, parent = prims_algo(graph)
    assert abs(dist["a"] - dist["b"]) == 3
    assert abs(dist["d"] - dist["b"]) == 15
    assert abs(dist["a"] - dist["c"]) == 13
