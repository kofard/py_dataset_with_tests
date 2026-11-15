import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    s = SegmentTree([1, 2, 3])
    assert s.left(1) == 2
    assert s.left(2) == 4
    s = SegmentTree([1, 2, 3])
    assert s.right(1) == 3
    assert s.right(2) == 5
    s = SegmentTree([1, 2, 3, 4, 5])
    assert s.update(2, 4, 10) == True
    assert s.query(1, 5) == 10
    s = SegmentTree([1, 2, 3, 4, 5])
    assert s.query(1, 3) == 3
    assert s.query(1, 5) == 5
