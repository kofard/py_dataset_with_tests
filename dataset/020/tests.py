import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert all(armstrong_number(n) for n in PASSING) == True
    assert any(armstrong_number(n) for n in FAILING) == False
    assert all(pluperfect_number(n) for n in PASSING) == True
    assert any(pluperfect_number(n) for n in FAILING) == False
    assert all(narcissistic_number(n) for n in PASSING) == True
    assert any(narcissistic_number(n) for n in FAILING) == False
