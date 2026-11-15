import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert legendre_symbol(2, 7) == 1
    assert legendre_symbol(3, 7) == -1
    assert legendre_symbol(14, 7) == 0
    assert legendre_symbol(5, 11) == 1
    assert tonelli_shanks(5, 41) == 13
    assert pow(13, 2, 41) == 5
    assert tonelli_shanks(2, 7) == 3
    assert pow(3, 2, 7) == 2
    assert tonelli_shanks(10, 13) == 6
    assert tonelli_shanks(0, 11) == 0
    assert tonelli_shanks(8, 17) == 5
    assert pow(5, 2, 17) == 8
