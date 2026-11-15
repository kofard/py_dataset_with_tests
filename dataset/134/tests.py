import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert kirkpatrick_reisch_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert kirkpatrick_reisch_sort([]) == []
    assert kirkpatrick_reisch_sort([1]) == [1]
    assert kirkpatrick_reisch_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert kirkpatrick_reisch_sort([-1, -3, 5, 0, 2]) == [-3, -1, 0, 2, 5]
