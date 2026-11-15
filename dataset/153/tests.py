import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert manhattan_distance([1,1], [2,2]) == 2.0
    assert manhattan_distance([1.5,1.5], [2,2]) == 1.0
    assert manhattan_distance([1.5,1.5], [2.5,2]) == 1.5
    assert manhattan_distance([-3, -3, -3], [0, 0, 0]) == 9.0
    assert manhattan_distance_one_liner([1,1], [2,2]) == 2.0
    assert manhattan_distance_one_liner([1.5,1.5], [2,2]) == 1.0
    assert manhattan_distance_one_liner([1.5,1.5], [2.5,2]) == 1.5
    assert manhattan_distance_one_liner([-3, -3, -3], [0, 0, 0]) == 9.0
