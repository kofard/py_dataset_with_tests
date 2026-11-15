import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert binary_search_insertion([1, 2, 7, 9, 10], 4) == [1, 2, 4, 7, 9, 10]
    assert merge([[1, 6], [9, 10]], [[2, 3], [4, 5], [7, 8]]) == [[1, 6], [2, 3], [4, 5], [7, 8], [9, 10]]
    assert sortlist_2d([[9, 10], [1, 6], [7, 8], [2, 3], [4, 5]]) == [[1, 6], [2, 3], [4, 5], [7, 8], [9, 10]]
    assert merge_insertion_sort([0, 5, 3, 2, 2]) == [0, 2, 2, 3, 5]
    assert merge_insertion_sort([99]) == [99]
    assert merge_insertion_sort([-2, -5, -45]) == [-45, -5, -2]
    import itertools
    permutations = list(itertools.permutations([0, 1, 2, 3, 4]))
    assert all(merge_insertion_sort(p) == [0, 1, 2, 3, 4] for p in permutations) == True
