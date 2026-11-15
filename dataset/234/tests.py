import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    lst = [1, 2, 3, 4, 5]
    reverse_subarray(lst, 1, 3)
    assert lst == [1, 4, 3, 2, 5]
    lst = [1]
    reverse_subarray(lst, 0, 0)
    assert lst == [1]
    lst = [1, 2]
    reverse_subarray(lst, 0, 1)
    assert lst == [2, 1]
    assert reverse_selection_sort([1, 9, 5, 21, 17, 6]) == [1, 5, 6, 9, 17, 21]
    assert reverse_selection_sort([]) == []
    assert reverse_selection_sort([-3, -17, -48]) == [-48, -17, -3]
    assert reverse_selection_sort([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert reverse_selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert reverse_selection_sort(["banana", "apple", "cherry"]) == ['apple', 'banana', 'cherry']
    assert reverse_selection_sort([3.14, 1.5, 2.7]) == [1.5, 2.7, 3.14]
