import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert jump_search([0, 1, 2, 3, 4, 5], 3) == 3
    assert jump_search([-5, -2, -1], -1) == 2
    assert jump_search([0, 5, 10, 20], 8) == -1
    assert jump_search([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610], 55) == 10
    assert jump_search(["aa", "bb", "cc", "dd", "ee", "ff"], "ee") == 4
    assert jump_search([], 1) == -1
