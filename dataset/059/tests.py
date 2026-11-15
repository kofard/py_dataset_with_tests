import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert is_bipartite_dfs({0: [1, 2], 1: [0, 3], 2: [0, 4]}) == True
    assert is_bipartite_dfs({0: [1, 2], 1: [0, 3], 2: [0, 1]}) == False
    assert is_bipartite_dfs({}) == True
    assert is_bipartite_dfs({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}) == True
    assert is_bipartite_dfs({0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 3], 3: [0, 2]}) == False
    assert is_bipartite_dfs({0: [4], 1: [], 2: [4], 3: [4], 4: [0, 2, 3]}) == True
    assert is_bipartite_dfs({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 4: [0]}) == False
    assert is_bipartite_dfs({7: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 4: [0]}) == False
    assert is_bipartite_dfs({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 9: [0]}) == False
    assert is_bipartite_dfs({0: [-1, 3], 1: [0, -2]}) == False
    assert is_bipartite_dfs({-1: [0, 2], 0: [-1, 1], 1: [0, 2], 2: [-1, 1]}) == True
    assert is_bipartite_dfs({0.9: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}) == True
    assert is_bipartite_dfs({0: [1.0, 3.0], 1.0: [0, 2.0], 2.0: [1.0, 3.0], 3.0: [0, 2.0]}) == True
    assert is_bipartite_dfs({"a": [1, 3], "b": [0, 2], "c": [1, 3], "d": [0, 2]}) == True
    assert is_bipartite_dfs({0: ["b", "d"], 1: ["a", "c"], 2: ["b", "d"], 3: ["a", "c"]}) == True
    assert is_bipartite_bfs({0: [1, 2], 1: [0, 3], 2: [0, 4]}) == True
    assert is_bipartite_bfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}) == False
    assert is_bipartite_bfs({}) == True
    assert is_bipartite_bfs({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}) == True
    assert is_bipartite_bfs({0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 3], 3: [0, 2]}) == False
    assert is_bipartite_bfs({0: [4], 1: [], 2: [4], 3: [4], 4: [0, 2, 3]}) == True
    assert is_bipartite_bfs({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 4: [0]}) == False
    assert is_bipartite_bfs({7: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 4: [0]}) == False
    assert is_bipartite_bfs({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 9: [0]}) == False
    assert is_bipartite_bfs({0: [-1, 3], 1: [0, -2]}) == False
    assert is_bipartite_bfs({-1: [0, 2], 0: [-1, 1], 1: [0, 2], 2: [-1, 1]}) == True
    assert is_bipartite_bfs({0.9: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}) == True
    assert is_bipartite_bfs({0: [1.0, 3.0], 1.0: [0, 2.0], 2.0: [1.0, 3.0], 3.0: [0, 2.0]}) == True
    assert is_bipartite_bfs({"a": [1, 3], "b": [0, 2], "c": [1, 3], "d": [0, 2]}) == True
    assert is_bipartite_bfs({0: ["b", "d"], 1: ["a", "c"], 2: ["b", "d"], 3: ["a", "c"]}) == True
