import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    arr = [12, 42, -21, 1]
    comp_and_swap(arr, 1, 2, 1)
    assert arr == [12, -21, 42, 1]
    comp_and_swap(arr, 1, 2, 0)
    assert arr == [12, 42, -21, 1]
    comp_and_swap(arr, 0, 3, 1)
    assert arr == [1, 42, -21, 12]
    comp_and_swap(arr, 0, 3, 0)
    assert arr == [12, 42, -21, 1]
    arr = [12, 42, -21, 1]
    bitonic_merge(arr, 0, 4, 1)
    assert arr == [-21, 1, 12, 42]
    bitonic_merge(arr, 0, 4, 0)
    assert arr == [42, 12, 1, -21]
    arr = [12, 34, 92, -23, 0, -121, -167, 145]
    bitonic_sort(arr, 0, 8, 1)
    assert arr == [-167, -121, -23, 0, 12, 34, 92, 145]
    bitonic_sort(arr, 0, 8, 0)
    assert arr == [145, 92, 34, 12, 0, -23, -121, -167]
    arr = ["banana", "apple", "cherry", "date"]
    bitonic_sort(arr, 0, 4, 1)
    assert arr == ['apple', 'banana', 'cherry', 'date']
    arr = [3, 1.5, 2, 4.5]
    bitonic_sort(arr, 0, 4, 1)
    assert arr == [1.5, 2, 3, 4.5]
    arr = [1, "two", 3, "four"]
