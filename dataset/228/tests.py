import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    col = [1, 2, 1]
    rec_insertion_sort(col, len(col))
    assert col == [1, 1, 2]
    col = [2, 1, 0, -1, -2]
    rec_insertion_sort(col, len(col))
    assert col == [-2, -1, 0, 1, 2]
    col = [1]
    rec_insertion_sort(col, len(col))
    assert col == [1]
    col = ['d', 'a', 'b', 'e', 'c']
    rec_insertion_sort(col, len(col))
    assert col == ['a', 'b', 'c', 'd', 'e']
    col = [2.5, -1, 0.0, 1]
    rec_insertion_sort(col, len(col))
    assert col == [-1, 0.0, 1, 2.5]
    col = [1, "a"]
    col = [3, 2, 4, 2]
    insert_next(col, 1)
    assert col == [2, 3, 4, 2]
    col = [3, 2, 3]
    insert_next(col, 2)
    assert col == [3, 2, 3]
    col = []
    insert_next(col, 1)
    assert col == []
