import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert recursive_match('abc', 'a.c') == True
    assert recursive_match('abc', 'af*.c') == True
    assert recursive_match('abc', 'a.c*') == True
    assert recursive_match('abc', 'a.c*d') == False
    assert recursive_match('aa', '.*') == True
    assert dp_match('abc', 'a.c') == True
    assert dp_match('abc', 'af*.c') == True
    assert dp_match('abc', 'a.c*') == True
    assert dp_match('abc', 'a.c*d') == False
    assert dp_match('aa', '.*') == True
