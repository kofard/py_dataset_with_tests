import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert is_geometric_series([2, 4, 8]) == True
    assert is_geometric_series([3, 6, 12, 24]) == True
    assert is_geometric_series([1, 2, 3]) == False
    assert is_geometric_series([0, 0, 3]) == False
    assert geometric_mean([2, 4, 8]) == 3.9999999999999996
    assert geometric_mean([3, 6, 12, 24]) == 8.48528137423857
    assert geometric_mean([4, 8, 16]) == 7.999999999999999
    assert geometric_mean([1, 2, 3]) == 1.8171205928321397
    assert geometric_mean([0, 2, 3]) == 0.0
