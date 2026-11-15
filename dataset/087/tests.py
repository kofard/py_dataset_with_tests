import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert is_ear([(0, 2), (2, 2), (2,0), (1, 0), (1, 1), (0, 1)], 4,
"counter-clockwise") == False
    assert is_ear([(0, 2), (2, 2), (2,0), (1, 0), (1, 1), (0, 1)], 3,
"counter-clockwise") == True
    assert is_ear([(0, 3), (2, 2), (3, 0), (3, 3)], 3, "clockwise") == False
    assert is_ear([(0, 0), (1, 0), (1, 1), (0, 1)], 0, "clockwise") == True
    assert is_convex((1,1), (2, 2), (1, 2), "clockwise") == True
    assert is_convex((1,1), (2, 2), (1, 2), "counter-clockwise") == False
    assert is_convex((1,1), (2, 2), (3, 3), "clockwise") == True
    assert is_convex((1,1), (2, 2), (3, 3), "counter-clockwise") == True
    assert cross_product((0, 0), (1, 0), (1.5, 0.5)) == 0.5
    assert cross_product((1.5, 0.5), (1, 1), (1.5, 1.5)) == -0.5
    assert cross_product((0, 0), (1, 1), (2, 2)) == 0
    assert direction([(1, 1), (2, 2), (3, 4)]) == 'clockwise'
    assert direction([(1, 1), (2, 2), (3, -1)]) == 'counter-clockwise'
    assert is_point_inside_triangle((0, 0), (0, 2), (2, 0), (3, 3)) == False
    assert is_point_inside_triangle((0, 0), (0, 2), (2, 0), (1, 1)) == True
    assert is_point_inside_triangle((0, 0), (2, 1), (2, 0), (1, 1)) == False
    assert is_point_inside_triangle((0, 0), (2, 1), (2, 0), (2, 0)) == True
    assert is_point_inside_triangle((0, 0), (1, 1), (2, 0), (1, 0)) == True
    assert triangulate_polygon([(0, 2), (2, 2), (2, 0), (1, 0), (1, 1), (0, 1)]) == [[(0, 1), (0, 2), (2, 2)], [(2, 2), (2, 0), (1, 0)], [(2, 2), (1, 0), (1, 1)], [(0, 1), (2, 2), (1, 1)]]
    assert triangulate_polygon([(0, 3), (2, 2), (3, 0), (3, 3)]) == [[(3, 3), (0, 3), (2, 2)], [(3, 3), (2, 2), (3, 0)]]
    assert triangulate_polygon([(0, 0),(2, 0), (1, 1), (2, 2), (0,2)]) == [[(0, 0), (2, 0), (1, 1)], [(0, 2), (0, 0), (1, 1)], [(0, 2), (1, 1), (2, 2)]]
