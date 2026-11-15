import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert angle_comparer((1,1), 0, 0) == 45.0
    assert angle_comparer((100,1), 10, 10) == -5.710593137499642
    assert angle_comparer((5,5), 2, 3) == 33.690067525979785
    assert check_direction((1,1), (2,2), (3,3)) == Direction.straight
    assert check_direction((60,1), (-50,199), (30,2)) == Direction.left
    assert check_direction((0,0), (5,5), (10,0)) == Direction.right
    assert graham_scan([(9, 6), (3, 1), (0, 0), (5, 5), (5, 2), (7, 0), (3, 3), (1, 4)]) == [(0, 0), (7, 0), (9, 6), (5, 5), (1, 4)]
    assert graham_scan([(0, 0), (1, 0), (1, 1), (0, 1)]) == [(0, 0), (1, 0), (1, 1), (0, 1)]
    assert graham_scan([(0, 0), (1, 1), (2, 2), (3, 3), (-1, 2)]) == [(0, 0), (1, 1), (2, 2), (3, 3), (-1, 2)]
    assert graham_scan([(-100, 20), (99, 3), (1, 10000001), (5133186, -25), (-66, -4)]) == [(5133186, -25), (1, 10000001), (-100, 20), (-66, -4)]
