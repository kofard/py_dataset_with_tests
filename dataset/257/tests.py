import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert encrypt("WE ARE DISCOVERED FLEE AT ONCE", 3) == 'WA SVEFETNERDCEDL  C EIOR EAOE'
    assert decrypt('WA SVEFETNERDCEDL  C EIOR EAOE', 3) == 'WE ARE DISCOVERED FLEE AT ONCE'
    assert encrypt("HELLO", 1) == 'HELLO'
    assert decrypt("HELLO", 1) == 'HELLO'
    assert encrypt("HELLO", 5)  # key equals length == 'HELLO'
    assert decrypt("HELLO", 5) == 'HELLO'
