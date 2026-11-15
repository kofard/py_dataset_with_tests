import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert find_minimum_change([1, 5, 10, 20, 50, 100, 200, 500, 1000,2000], 18745) == [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 500, 200, 20, 20, 5]
    assert find_minimum_change([1, 2, 5, 10, 20, 50, 100, 500, 2000], 987) == [500, 100, 100, 100, 100, 50, 20, 10, 5, 2]
    assert find_minimum_change([1, 2, 5, 10, 20, 50, 100, 500, 2000], 0) == []
    assert find_minimum_change([1, 2, 5, 10, 20, 50, 100, 500, 2000], -98) == []
    assert find_minimum_change([1, 5, 100, 500, 1000], 456) == [100, 100, 100, 100, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1]
