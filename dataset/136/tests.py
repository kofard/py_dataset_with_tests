import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert get_valid_pos((1, 3), 4) == [(2, 1), (0, 1), (3, 2)]
    assert is_complete([[1]]) == True
    assert is_complete([[1, 2], [3, 0]]) == False
    assert open_knight_tour(1) == [[1]]
