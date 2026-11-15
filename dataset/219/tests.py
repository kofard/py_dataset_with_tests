import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert proth(6) == 25
    assert is_proth_number(1) == False
    assert is_proth_number(2) == False
    assert is_proth_number(3) == True
    assert is_proth_number(4) == False
    assert is_proth_number(5) == True
    assert is_proth_number(34) == False
