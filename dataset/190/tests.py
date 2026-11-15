import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert calculate_waitingtime([0,1,2], [10, 5, 8], 3) == [0, 9, 13]
    assert calculate_waitingtime([1,2,2,4], [4, 6, 3, 1], 4) == [0, 7, 4, 1]
    assert calculate_waitingtime([0,0,0], [12, 2, 10],3) == [12, 0, 2]
    assert calculate_turnaroundtime([0,1,2], 3, [0, 10, 15]) == [0, 11, 17]
    assert calculate_turnaroundtime([1,2,2,4], 4, [1, 8, 5, 4]) == [2, 10, 7, 8]
    assert calculate_turnaroundtime([0,0,0], 3, [12, 0, 2]) == [12, 0, 2]
