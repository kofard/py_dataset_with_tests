import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert round(kelly_criterion(0.6, 2.0), 4) == 0.4
    assert round(kelly_criterion(0.55, 1.0), 4) == 0.1
    assert kelly_criterion(0.5, 1.0) == 0.0
    assert round(kelly_criterion(0.7, 3.0), 4) == 0.6
    assert round(kelly_criterion(0.3, 2.0), 4) == -0.05
    assert round(kelly_criterion_extended(0.6, 2.0, 1.0), 4) == 0.4
    assert round(kelly_criterion_extended(0.55, 1.5, 1.5), 4) == 0.1
    assert kelly_criterion_extended(0.5, 1.0, 1.0) == 0.0
    assert round(kelly_criterion_extended(0.7, 3.0, 1.0), 4) == 0.6
    assert round(fractional_kelly(0.6, 2.0, 0.5), 4) == 0.2
    assert round(fractional_kelly(0.55, 1.0, 0.25), 4) == 0.025
    assert round(fractional_kelly(0.7, 3.0, 1.0), 4) == 0.6
