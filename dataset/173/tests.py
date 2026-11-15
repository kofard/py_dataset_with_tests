import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert mincost_tickets([1, 4, 6, 7, 8, 20], [2, 7, 15]) == 11
    assert mincost_tickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31],  [2, 7, 15]) == 17
    assert mincost_tickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 90, 150]) == 24
    assert mincost_tickets([2], [2, 90, 150]) == 2
    assert mincost_tickets([], [2, 90, 150]) == 0
