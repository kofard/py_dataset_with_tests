import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert simulate(construct_highway(6, 3, 0), 2, 0, 2) == [[0, -1, -1, 0, -1, -1], [-1, 1, -1, -1, 1, -1], [-1, -1, 1, -1, -1, 1]]
    assert simulate(construct_highway(5, 2, -2), 3, 0, 2) == [[0, -1, 0, -1, 0], [0, -1, 0, -1, -1], [0, -1, -1, 1, -1], [-1, 1, -1, 0, -1]]
    assert construct_highway(10, 2, 6) == [[6, -1, 6, -1, 6, -1, 6, -1, 6, -1]]
    assert construct_highway(10, 10, 2) == [[2, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
    assert get_distance([6, -1, 6, -1, 6], 2) == 1
    assert get_distance([2, -1, -1, -1, 3, 1, 0, 1, 3, 2], 0) == 3
    assert get_distance([-1, -1, -1, -1, 2, -1, -1, -1, 3], -1) == 4
    assert update([-1, -1, -1, -1, -1, 2, -1, -1, -1, -1, 3], 0.0, 5) == [-1, -1, -1, -1, -1, 3, -1, -1, -1, -1, 4]
    assert update([-1, -1, 2, -1, -1, -1, -1, 3], 0.0, 5) == [-1, -1, 3, -1, -1, -1, -1, 1]
    assert simulate([[-1, 2, -1, -1, -1, 3]], 2, 0.0, 3) == [[-1, 2, -1, -1, -1, 3], [-1, -1, -1, 2, -1, 0], [1, -1, -1, 0, -1, -1]]
    assert simulate([[-1, 2, -1, 3]], 4, 0.0, 3) == [[-1, 2, -1, 3], [-1, 0, -1, 0], [-1, 0, -1, 0], [-1, 0, -1, 0], [-1, 0, -1, 0]]
