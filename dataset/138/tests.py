import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert partition([3, 1, 4, 5, 9, 2, 6, 5, 3, 5], 0, 9) == 4
    assert partition([7, 1, 4, 5, 9, 2, 6, 5, 8], 0, 8) == 1
    assert partition(['apple', 'cherry', 'date', 'banana'], 0, 3) == 2
    assert partition([3.1, 1.2, 5.6, 4.7], 0, 3) == 1
    assert kth_largest_element([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 3) == 5
    assert kth_largest_element([2, 5, 6, 1, 9, 3, 8, 4, 7, 3, 5], 1) == 9
    assert kth_largest_element(['apple', 'cherry', 'date', 'banana'], 2) == 'cherry'
    assert kth_largest_element([3.1, 1.2, 5.6, 4.7,7.9,5,0], 2) == 5.6
    assert kth_largest_element([-2, -5, -4, -1], 1) == -1
    assert kth_largest_element([], 1) == -1
