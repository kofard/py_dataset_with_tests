import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert combination_sum_iv([1,2,5], 5) == 9
    assert combination_sum_iv_dp_array([1,2,5], 5) == 9
    assert combination_sum_iv_bottom_up(3, [1,2,5], 5) == 9
