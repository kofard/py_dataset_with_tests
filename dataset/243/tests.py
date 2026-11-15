import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert Point(0, 0) == Point(x=0, y=0)
    assert Point(1, -3) == Point(x=1, y=-3)
    assert direction(Point(0, 0), Point(1, 0), Point(0, 1)) == -1
    assert direction(Point(0, 0), Point(0, 1), Point(1, 0)) == 1
    assert direction(Point(0, 0), Point(1, 1), Point(2, 2)) == 0
    assert on_segment(Point(0, 0), Point(4, 4), Point(2, 2)) == True
    assert on_segment(Point(0, 0), Point(4, 4), Point(5, 5)) == False
    assert on_segment(Point(0, 0), Point(4, 0), Point(2, 0)) == True
    assert segments_intersect(Point(0, 0), Point(2, 2), Point(0, 2), Point(2, 0)) == True
    assert segments_intersect(Point(0, 0), Point(2, 2), Point(1, 1), Point(3, 3)) == True
    assert segments_intersect(Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)) == False
    assert segments_intersect(Point(0, 0), Point(1, 1), Point(1, 0), Point(2, 1)) == False
    assert segments_intersect(Point(0, 0), Point(1, 1), Point(0, 1), Point(0, 2)) == False
    assert segments_intersect(Point(0, 0), Point(1, 0), Point(1, 0), Point(2, 0)) == True
