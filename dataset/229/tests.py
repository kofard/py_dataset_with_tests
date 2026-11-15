import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert merge([10,9,8,7,6,5,4,3,2,1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert merge([1,2,3,4,5,6,7,8,9,10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert merge([10,22,1,2,3,9,15,23]) == [1, 2, 3, 9, 10, 15, 22, 23]
    assert merge([100]) == [100]
    assert merge([]) == []
    assert merge(["c", "a", "b"]) == ['a', 'b', 'c']
    assert merge([2.5, -1, 0.0]) == [-1, 0.0, 2.5]
    values = [3, 1, 2]
    assert merge(values) == [1, 2, 3]
    assert values == [3, 1, 2]
    assert merge(("b", "c", "a")) == ['a', 'b', 'c']
