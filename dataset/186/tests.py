import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert gravitational_law(force=0, mass_1=5, mass_2=10, distance=20) == {'force': 8.342875e-12}
    assert gravitational_law(force=7367.382, mass_1=0, mass_2=74, distance=3048) == {'mass_1': 1.385816317292268e+19}
