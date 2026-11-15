import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert encrypt("hello world", "coffee") == 'jsqqs avvwo'
    assert encrypt("coffee is good as python", "TheAlgorithms") == 'vvjfpk wj ohvp su ddylsv'
    assert decrypt("jsqqs avvwo", "coffee") == 'hello world'
    assert decrypt("vvjfpk wj ohvp su ddylsv", "TheAlgorithms") == 'coffee is good as python'
