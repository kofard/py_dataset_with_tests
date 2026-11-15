import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert matrix_chain_order([10, 30, 5]) == ([[0, 0, 0], [0, 0, 1500], [0, 0, 0]], [[0, 0, 0], [0, 0, 1], [0, 0, 0]])
