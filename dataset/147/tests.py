import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert longest_increasing_subsequence_length([2, 5, 3, 7, 11, 8, 10, 13, 6]) == 6
    assert longest_increasing_subsequence_length([]) == 0
    assert longest_increasing_subsequence_length([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13,
                                    3, 11, 7, 15]) == 6
    assert longest_increasing_subsequence_length([5, 4, 3, 2, 1]) == 1
