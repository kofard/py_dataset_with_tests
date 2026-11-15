import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    segment_tree = SegmentTree(15)
    assert segment_tree.left(1) == 2
    assert segment_tree.left(2) == 4
    assert segment_tree.left(12) == 24
    segment_tree = SegmentTree(15)
    assert segment_tree.right(1) == 3
    assert segment_tree.right(2) == 5
    assert segment_tree.right(12) == 25
    A = [1, 2, -4, 7, 3, -5, 6, 11, -20, 9, 14, 15, 5, 2, -8]
    segment_tree = SegmentTree(15)
    segment_tree.build(1, 1, 15, A)
    assert segment_tree.query(1, 1, 15, 4, 6) == 7
    assert segment_tree.query(1, 1, 15, 7, 11) == 14
    assert segment_tree.query(1, 1, 15, 7, 12) == 15
