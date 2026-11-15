import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert SelfOrganizingMap().get_winner([[1, 2, 3], [4, 5, 6]], [1, 2, 3]) == 1
    assert SelfOrganizingMap().update([[1, 2, 3], [4, 5, 6]], [1, 2, 3], 1, 0.1) == [[1, 2, 3], [3.7, 4.7, 6]]
