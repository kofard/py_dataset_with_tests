import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    adjacency_list = {0: [[1, 1], [3, 3]],
                  1: [[0, 1], [2, 6], [3, 5], [4, 1]],
                  2: [[1, 6], [4, 5], [5, 2]],
                  3: [[0, 3], [1, 5], [4, 1]],
                  4: [[1, 1], [2, 5], [3, 1], [5, 4]],
                  5: [[2, 2], [4, 4]]}
    assert prisms_algorithm(adjacency_list) == [(0, 1), (1, 4), (4, 3), (4, 5), (5, 2)]
