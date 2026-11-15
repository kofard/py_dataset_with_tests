import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert is_harmonic_series([ 1, 2/3, 1/2, 2/5, 1/3]) == True
    assert is_harmonic_series([ 1, 2/3, 2/5, 1/3]) == False
    assert is_harmonic_series([1, 2, 3]) == False
    assert is_harmonic_series([1/2, 1/3, 1/4]) == True
    assert is_harmonic_series([2/5, 2/10, 2/15, 2/20, 2/25]) == True
    assert harmonic_mean([1, 4, 4]) == 2.0
    assert harmonic_mean([3, 6, 9, 12]) == 5.759999999999999
    assert harmonic_mean([1, 2, 3]) == 1.6363636363636365
