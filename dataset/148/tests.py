import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert swap(2,3) == (3, 2)
    assert swap(3,4) == (4, 3)
    assert swap(67, 12) == (12, 67)
    assert swap(3,-4) == (-4, 3)
    max_node = 6
    parent = [[0, 0, 1, 1, 2, 2, 3]] + [[0] * 7 for _ in range(19)]
    parent = create_sparse(max_node=max_node, parent=parent)
    assert parent[0] == [0, 0, 1, 1, 2, 2, 3]
    assert parent[1] == [0, 0, 0, 0, 1, 1, 1]
    assert parent[2] == [0, 0, 0, 0, 0, 0, 0]
    max_node = 1
    parent = [[0, 0]] + [[0] * 2 for _ in range(19)]
    parent = create_sparse(max_node=max_node, parent=parent)
    assert parent[0] == [0, 0]
    assert parent[1] == [0, 0]
    level = [-1, 0, 1, 1, 2, 2, 2]
    parent = [[0, 0, 1, 1, 2, 2, 3],[0, 0, 0, 0, 1, 1, 1]] +                     [[0] * 7 for _ in range(17)]
    assert lowest_common_ancestor(u=4, v=5, level=level, parent=parent) == 2
    assert lowest_common_ancestor(u=4, v=6, level=level, parent=parent) == 1
    assert lowest_common_ancestor(u=2, v=3, level=level, parent=parent) == 1
    assert lowest_common_ancestor(u=6, v=6, level=level, parent=parent) == 6
    level = [-1] * 7
    parent = [[0] * 7 for _ in range(20)]
    graph = {1: [2, 3], 2: [4, 5], 3: [6], 4: [], 5: [], 6: []}
    level, parent = breadth_first_search(
    level=level, parent=parent, max_node=6, graph=graph, root=1)
    assert level == [-1, 0, 1, 1, 2, 2, 2]
    assert parent[0] == [0, 0, 1, 1, 2, 2, 3]
    level = [-1] * 2
    parent = [[0] * 2 for _ in range(20)]
    graph = {1: []}
    level, parent = breadth_first_search(
    level=level, parent=parent, max_node=1, graph=graph, root=1)
    assert level == [-1, 0]
    assert parent[0] == [0, 0]
