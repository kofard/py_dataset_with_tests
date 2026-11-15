import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert sieve_of_atkin(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert sieve_of_atkin(10) == [2, 3, 5, 7]
    assert sieve_of_atkin(2) == [2]
    assert sieve_of_atkin(1) == []
    assert sieve_of_atkin(0) == []
