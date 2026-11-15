import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert linear_search([0, 5, 7, 10, 15], 0) == 0
    assert linear_search([0, 5, 7, 10, 15], 15) == 4
    assert linear_search([0, 5, 7, 10, 15], 5) == 1
    assert linear_search([0, 5, 7, 10, 15], 6) == -1
    assert rec_linear_search([0, 30, 500, 100, 700], 0, 4, 0) == 0
    assert rec_linear_search([0, 30, 500, 100, 700], 0, 4, 700) == 4
    assert rec_linear_search([0, 30, 500, 100, 700], 0, 4, 30) == 1
    assert rec_linear_search([0, 30, 500, 100, 700], 0, 4, -6) == -1
