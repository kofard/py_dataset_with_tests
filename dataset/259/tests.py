import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    data = [3, 5, 4]
    _sift(data, 2, 2)
    assert data == [3, 4, 5]
    data = [1, 2, 3]
    _sift(data, 2, 2)
    assert data == [1, 2, 3]
    data = [7]
    _sift(data, 0, 1)
    assert data == [7]
    data = [9, 1, 8, 5, 3]
    _sift(data, 4, 3)
    assert data == [3, 1, 9, 5, 8]
    data = [1, 5, 3]
    _trinkle(data, 2, [1, 1], 1)
    assert data == [1, 3, 5]
    data = [3, 5, 4]
    _trinkle(data, 2, [2], 0)
    assert data == [3, 4, 5]
    assert smoothsort([4, 1, 3, 9, 7]) == [1, 3, 4, 7, 9]
    assert smoothsort([]) == []
    assert smoothsort([1]) == [1]
    assert smoothsort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert smoothsort([3, 3, 2, 1, 2]) == [1, 2, 2, 3, 3]
    assert smoothsort(["d", "a", "c", "b"]) == ['a', 'b', 'c', 'd']
    assert smoothsort([2.5, -1, 0.0]) == [-1, 0.0, 2.5]
    assert smoothsort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert smoothsort([-3, 0, -1, 5, 2]) == [-3, -1, 0, 2, 5]
