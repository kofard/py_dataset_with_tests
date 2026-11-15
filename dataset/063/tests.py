import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert cocktail_shaker_sort([4, 5, 2, 1, 2]) == [1, 2, 2, 4, 5]
    assert cocktail_shaker_sort([-4, 5, 0, 1, 2, 11]) == [-4, 0, 1, 2, 5, 11]
    assert cocktail_shaker_sort([0.1, -2.4, 4.4, 2.2]) == [-2.4, 0.1, 2.2, 4.4]
    assert cocktail_shaker_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert cocktail_shaker_sort([-4, -5, -24, -7, -11]) == [-24, -11, -7, -5, -4]
    assert cocktail_shaker_sort(["elderberry", "banana", "date", "apple", "cherry"]) == ['apple', 'banana', 'cherry', 'date', 'elderberry']
