import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert encrypt("Hello World", 4) == 'HWe olordll'
    assert decrypt("HWe olordll", 4) == 'Hello World'
    assert decrypt("My key is very big", 100) == 'My key is very big'
    assert bruteforce("HWe olordll")[4] == 'Hello World'
