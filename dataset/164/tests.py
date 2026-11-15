import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert merge_sort([0, 5, 3, 2, 2]) == [0, 2, 2, 3, 5]
    assert merge_sort([]) == []
    assert merge_sort([-2, -45, -5]) == [-45, -5, -2]
