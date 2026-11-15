import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert knapsack_with_example_solution(10, [1, 3, 5, 2], [10, 20, 100, 22]) == (142, {2, 3, 4})
    assert knapsack_with_example_solution(6, [4, 3, 2, 3], [3, 2, 4, 4]) == (8, {3, 4})
