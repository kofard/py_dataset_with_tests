import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert find_primitive(7)  # Modulo 7 has primitive root 3 == 3
    assert find_primitive(11)  # Modulo 11 has primitive root 2 == 2
    assert find_primitive(8) == None # Modulo 8 has no primitive root == True
