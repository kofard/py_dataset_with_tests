import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert odd_even_sort([5 , 4 ,3 ,2 ,1]) == [1, 2, 3, 4, 5]
    assert odd_even_sort([]) == []
    assert odd_even_sort([-10 ,-1 ,10 ,2]) == [-10, -1, 2, 10]
    assert odd_even_sort([1 ,2 ,3 ,4]) == [1, 2, 3, 4]
    assert odd_even_sort(["c","a","b"]) == ['a', 'b', 'c']
    assert odd_even_sort([2.5, -1, 0.0]) == [-1, 0.0, 2.5]
