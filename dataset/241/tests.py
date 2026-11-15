import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert apply_table("0123456789", list(range(10))) == '9012345678'
    assert apply_table("0123456789", list(range(9, -1, -1))) == '8765432109'
    assert left_shift("0123456789") == '1234567890'
    assert xor("01010101", "00001111") == '01011010'
