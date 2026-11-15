import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert _linear_interpolated_quantile([-10.0, -5.0, -2.0, 1.0, 4.0], 0.25) == -5.0
    assert expected_shortfall([-10, -5, -2, 1, 4], 0.95) == 10.0
    assert expected_shortfall([-10, -5, -2, 1, 4], 0.75) == 7.5
