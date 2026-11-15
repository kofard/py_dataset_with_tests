import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert calculate_waiting_times([5, 10, 15]) == [0, 5, 15]
    assert calculate_waiting_times([1, 2, 3, 4, 5]) == [0, 1, 3, 6, 10]
    assert calculate_waiting_times([10, 3]) == [0, 10]
    assert calculate_turnaround_times([5, 10, 15], [0, 5, 15]) == [5, 15, 30]
    assert calculate_turnaround_times([1, 2, 3, 4, 5], [0, 1, 3, 6, 10]) == [1, 3, 6, 10, 15]
    assert calculate_turnaround_times([10, 3], [0, 10]) == [10, 13]
    assert calculate_average_turnaround_time([0, 5, 16]) == 7.0
    assert calculate_average_turnaround_time([1, 5, 8, 12]) == 6.5
    assert calculate_average_turnaround_time([10, 24]) == 17.0
    assert calculate_average_waiting_time([0, 5, 16]) == 7.0
    assert calculate_average_waiting_time([1, 5, 8, 12]) == 6.5
    assert calculate_average_waiting_time([10, 24]) == 17.0
