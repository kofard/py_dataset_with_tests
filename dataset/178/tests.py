import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert Point(0.0, 0.0) == Point(x=0.0, y=0.0)
    assert Point(1.5, -2.0) == Point(x=1.5, y=-2.0)
    assert cross_product_direction(Point(0, 0), Point(1, 0), Point(1, 1)) == 1
    assert cross_product_direction(Point(0, 0), Point(1, 1), Point(1, 0)) == -1
    assert cross_product_direction(Point(0, 0), Point(1, 1), Point(2, 2)) == 0
    assert monotone_chain([]) == []
    assert monotone_chain([Point(1, 1)]) == [Point(x=1, y=1)]
    assert monotone_chain([Point(0, 0), Point(1, 1)]) == [Point(x=0, y=0), Point(x=1, y=1)]
    square_points = [
    Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2),
    Point(1, 1), Point(1, 0.5)
]
    assert monotone_chain(square_points) == [Point(x=0, y=0), Point(x=2, y=0), Point(x=2, y=2), Point(x=0, y=2)]
    triangle_with_duplicates = [
    Point(0, 0), Point(4, 0), Point(2, 3),
    Point(0, 0), Point(4, 0), Point(2, 1)
]
    assert monotone_chain(triangle_with_duplicates) == [Point(x=0, y=0), Point(x=4, y=0), Point(x=2, y=3)]
    collinear_points = [Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 3)]
    assert monotone_chain(collinear_points) == [Point(x=0, y=0), Point(x=3, y=3)]
