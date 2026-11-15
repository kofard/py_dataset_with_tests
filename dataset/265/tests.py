import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert stooge_sort([18.1, 0, -7.1, -1, 2, 2]) == [-7.1, -1, 0, 2, 2, 18.1]
    assert stooge_sort([]) == []
    assert stooge_sort(["c", "a", "b"]) == ['a', 'b', 'c']
    assert stooge_sort([2.5, -1, 0.0]) == [-1, 0.0, 2.5]
