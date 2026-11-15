import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert Onepad().encrypt("") == ([], [])
    assert Onepad().encrypt([]) == ([], [])
    random.seed(1)
    assert Onepad().encrypt(" ") == ([6969], [69])
    random.seed(1)
    assert Onepad().encrypt("Hello") == ([9729, 114756, 4653, 31309, 10492], [69, 292, 33, 131, 61])
    assert Onepad().decrypt([], []) == ''
    assert Onepad().decrypt([35], []) == ''
    random.seed(1)
    assert Onepad().decrypt([9729, 114756, 4653, 31309, 10492], [69, 292, 33, 131, 61]) == 'Hello'
