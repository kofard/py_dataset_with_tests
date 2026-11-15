import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert dutch_national_flag_sort([]) == []
    assert dutch_national_flag_sort([0]) == [0]
    assert dutch_national_flag_sort([2, 1, 0, 0, 1, 2]) == [0, 0, 1, 1, 2, 2]
    assert dutch_national_flag_sort([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]) == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
