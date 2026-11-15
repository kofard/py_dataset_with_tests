import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    unsorted = [1, 4, 3, 5, 2]
    heapify(unsorted, 0, len(unsorted))
    assert unsorted == [4, 5, 3, 1, 2]
    heapify(unsorted, 0, len(unsorted))
    assert unsorted == [5, 4, 3, 1, 2]
    assert heap_sort([0, 5, 3, 2, 2]) == [0, 2, 2, 3, 5]
    assert heap_sort([]) == []
    assert heap_sort([-2, -5, -45]) == [-45, -5, -2]
    assert heap_sort([3, 7, 9, 28, 123, -5, 8, -30, -200, 0, 4]) == [-200, -30, -5, 0, 3, 4, 7, 8, 9, 28, 123]
    assert heap_sort(["banana", "apple", "cherry"]) == ['apple', 'banana', 'cherry']
    assert heap_sort([3.14, 1.5, 2.7]) == [1.5, 2.7, 3.14]
