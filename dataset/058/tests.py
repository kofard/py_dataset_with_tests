import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert casimir_force(force = 0, area = 4, distance = 0.03) == {'force': 6.4248189174864216e-21}
    assert casimir_force(force = 2635e-13, area = 0.0023, distance = 0) == {'distance': 1.0323056015031114e-05}
    assert casimir_force(force = 2737e-21, area = 0, distance = 0.0023746) == {'area': 0.06688838837354052}
