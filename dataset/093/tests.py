import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert binary_search_by_recursion([0, 5, 7, 10, 15], 0, 0, 4) == 0
    assert binary_search_by_recursion([0, 5, 7, 10, 15], 15, 0, 4) == 4
    assert binary_search_by_recursion([0, 5, 7, 10, 15], 5, 0, 4) == 1
    assert binary_search_by_recursion([0, 5, 7, 10, 15], 6, 0, 4) == -1
    assert binary_search_by_recursion([0, 5, 7, 10, 15], -1) == -1
    assert binary_search_by_recursion([0, 5, 7, 10, 15], 16) == -1
    assert exponential_search([0, 5, 7, 10, 15], 0) == 0
    assert exponential_search([0, 5, 7, 10, 15], 15) == 4
    assert exponential_search([0, 5, 7, 10, 15], 5) == 1
    assert exponential_search([0, 5, 7, 10, 15], 6) == -1
    assert exponential_search([0, 5, 7, 10, 15], -3) == -1
    assert exponential_search([0, 5, 7, 10, 15], 20) == -1
    assert exponential_search([], 1)  # Empty array edge case == -1
