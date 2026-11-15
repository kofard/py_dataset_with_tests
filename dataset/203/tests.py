import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert len(password_generator()) == 8
    assert len(password_generator(length=16)) == 16
    assert len(password_generator(257)) == 257
    assert len(password_generator(length=0)) == 0
    assert len(password_generator(-1)) == 0
    assert is_strong_password('Hwea7$2!') == True
    assert is_strong_password('Sh0r1') == False
    assert is_strong_password('Hello123') == False
    assert is_strong_password('Hello1238udfhiaf038fajdvjjf!jaiuFhkqi1') == True
    assert is_strong_password('0') == False
