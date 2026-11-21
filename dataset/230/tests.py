import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert test_rotations()
    assert test_insert()
    assert test_insert_and_search()
    assert test_insert_delete()
    assert test_floor_ceil()
    assert test_tree_traversal()
    assert test_tree_chaining()
