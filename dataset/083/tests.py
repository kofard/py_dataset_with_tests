import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    dg = DirectedGraph()
    dg.add_pair(-1,2)
    dg.add_pair(1,3,5)
    dg.add_pair(1,3,5)
    dg.add_pair(1,3,6)
    assert dg.all_nodes() == [-1, 2, 1, 3]
    assert dg.graph[1] == [[5, 3], [6, 3]]
    dg = DirectedGraph()
    assert dg.all_nodes() == []
    dg.add_pair(1,1)
    assert dg.all_nodes() == [1]
    dg.add_pair(2,3,3)
    assert dg.all_nodes() == [1, 2, 3]
    dg = DirectedGraph()
    dg.remove_pair(1,2) # silently exits
    dg.add_pair(0,5,2)
    assert dg.graph[0] == [[2, 5]]
    dg.remove_pair(5,0)
    assert dg.graph[0] == [[2, 5]]
    dg.remove_pair(0,5)
    assert dg.graph[0] == []
    dg = DirectedGraph()
    assert dg.dfs() == []
    dg.add_pair(1,1)
    assert dg.dfs(1,1) == [1]
    dg = DirectedGraph()
    dg.add_pair(0,1)
    dg.add_pair(0,2)
    dg.add_pair(1,3)
    dg.add_pair(1,4)
    dg.add_pair(1,5)
    dg.add_pair(2,5)
    dg.add_pair(5,6)
    assert dg.dfs(0,6) == [0, 2, 5, 6]
    assert dg.dfs(1,6) == [1, 5, 6]
    assert dg.dfs() == [0, 2, 5, 6, 1, 4, 3]
    assert dg.dfs(1,0) == [1, 5, 6, 4, 3]
    dg = DirectedGraph()
    assert dg.bfs() == []
    dg.add_pair(1,1)
    assert dg.bfs(1) == [1]
    dg = DirectedGraph()
    dg.add_pair(0,1)
    dg.add_pair(0,2)
    dg.add_pair(1,3)
    dg.add_pair(1,4)
    dg.add_pair(1,5)
    dg.add_pair(2,5)
    dg.add_pair(5,6)
    assert dg.bfs(0) == [0, 1, 2, 3, 4, 5, 6]
    assert dg.bfs(1) == [1, 3, 4, 5, 6]
    assert dg.bfs() == [0, 1, 2, 3, 4, 5, 6]
    ug = Graph()
    assert ug.dfs() == []
    ug.add_pair(1,1)
    assert ug.dfs(1,1) == [1]
    ug = Graph()
    ug.add_pair(0,1)
    ug.add_pair(0,2)
    ug.add_pair(1,3)
    ug.add_pair(1,4)
    ug.add_pair(1,5)
    ug.add_pair(2,5)
    ug.add_pair(5,6)
    assert ug.dfs(0,6) == [0, 2, 5, 6]
    assert ug.dfs(1,6) == [1, 5, 6]
    assert ug.dfs() == [0, 2, 5, 6, 1, 4, 3]
    assert ug.dfs(1,0) == [1, 5, 6, 2, 0]
    ug = Graph()
    assert ug.bfs() == []
    ug.add_pair(1,1)
    assert ug.bfs(1) == [1]
    ug = Graph()
    ug.add_pair(0,1)
    ug.add_pair(0,2)
    ug.add_pair(1,3)
    ug.add_pair(1,4)
    ug.add_pair(1,5)
    ug.add_pair(2,5)
    ug.add_pair(5,6)
    assert ug.bfs(0) == [0, 1, 2, 3, 4, 5, 6]
    assert ug.bfs(1) == [1, 0, 3, 4, 5, 2, 6]
    assert ug.bfs() == [0, 1, 2, 3, 4, 5, 6]
