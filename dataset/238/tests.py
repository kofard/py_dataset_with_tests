import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert calculate_waiting_times([10, 5, 8]) == [13, 10, 13]
    assert calculate_waiting_times([4, 6, 3, 1]) == [5, 8, 9, 6]
    assert calculate_waiting_times([12, 2, 10]) == [12, 2, 12]
    assert calculate_turn_around_times([1, 2, 3, 4], [0, 1, 3]) == [1, 3, 6]
    assert calculate_turn_around_times([10, 3, 7], [10, 6, 11]) == [20, 9, 18]
