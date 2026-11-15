import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert is_safe([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 1, 1) == True
    assert is_safe([[0, 1, 0], [0, 0, 0], [0, 0, 0]], 1, 1) == False
    assert is_safe([[1, 0, 0], [0, 0, 0], [0, 0, 0]], 1, 1) == False
    assert is_safe([[0, 0, 1], [0, 0, 0], [0, 0, 0]], 1, 1) == False
    assert is_safe([[1, 0, 0], [0, 0, 0], [0, 0, 0]], 1, 2) == True
    assert is_safe([[1, 0, 0], [0, 0, 0], [0, 0, 0]], 2, 1) == True
    assert is_safe([[0, 0, 0], [1, 0, 0], [0, 0, 0]], 0, 2) == True
    assert is_safe([[0, 0, 0], [1, 0, 0], [0, 0, 0]], 2, 2) == True
