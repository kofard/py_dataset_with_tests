import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert couloumbs_law(force=0, charge1=3, charge2=5, distance=2000) == {'force': 33705.0}
    assert couloumbs_law(force=10, charge1=3, charge2=5, distance=0) == {'distance': 116112.01488218177}
    assert couloumbs_law(force=10, charge1=0, charge2=5, distance=2000) == {'charge1': 0.0008900756564307966}
