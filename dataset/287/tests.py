import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert factors(12) == [1, 2, 3, 4, 6]
    assert factors(1) == [1]
    assert factors(100) == [1, 2, 4, 5, 10, 20, 25, 50]
    assert abundant(0) == True
    assert abundant(1) == False
    assert abundant(12) == True
    assert abundant(13) == False
    assert abundant(20) == True
    assert semi_perfect(0) == True
    assert semi_perfect(1) == True
    assert semi_perfect(12) == True
    assert semi_perfect(13) == False
    assert weird(0) == False
    assert weird(70) == True
    assert weird(77) == False
