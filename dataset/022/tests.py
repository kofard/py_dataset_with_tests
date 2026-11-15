import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    t = AVLtree()
    assert t.insert(4) == None
    assert t.insert(2) == None
    assert t.insert(3) == None
    assert t.get_height() == 2
    assert t.del_node(3) == None