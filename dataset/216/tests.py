import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert PrefixSum([1,2,3]).get_sum(0, 2) == 6
    assert PrefixSum([1,2,3]).get_sum(1, 2) == 5
    assert PrefixSum([1,2,3]).get_sum(2, 2) == 3
    assert PrefixSum([1,2,3]).contains_sum(6) == True
    assert PrefixSum([1,2,3]).contains_sum(5) == True
    assert PrefixSum([1,2,3]).contains_sum(3) == True
    assert PrefixSum([1,2,3]).contains_sum(4) == False
    assert PrefixSum([1,2,3]).contains_sum(7) == False
    assert PrefixSum([1,-2,3]).contains_sum(2) == True
