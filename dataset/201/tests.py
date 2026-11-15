import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert orbital_transfer_work(5.972e24, 1000, 6.371e6, 7e6) == '2.811e+09'
    assert orbital_transfer_work(5.972e24, 500, 7e6, 6.371e6) == '-1.405e+09'
    assert orbital_transfer_work(1.989e30, 1000, 1.5e11, 2.28e11) == '1.514e+11'
