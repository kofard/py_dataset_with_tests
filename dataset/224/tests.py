import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert _euclidean_distance((0.0, 0.0), (3.0, 4.0)) == 5.0
    assert _euclidean_distance((1.0, 1.0), (1.0, 1.0)) == 0.0
    assert _perpendicular_distance((4.0, 0.0), (0.0, 0.0), (0.0, 3.0)) == 4.0
    assert _perpendicular_distance((4.0, 0.0), (0.0, 3.0), (0.0, 0.0)) == 4.0
    assert _perpendicular_distance((4.0, 1.0), (0.0, 1.0), (0.0, 4.0)) == 4.0
    assert _perpendicular_distance((2.0, 1.0), (-2.0, 1.0), (-2.0, 4.0)) == 4.0
    assert round(_perpendicular_distance((0.0, 2.0), (1.0, 0.0), (3.0, 0.0)), 6) == 2.236068
    assert ramer_douglas_peucker([], epsilon=1.0) == []
    assert ramer_douglas_peucker([(0.0, 0.0)], epsilon=1.0) == [(0.0, 0.0)]
    assert ramer_douglas_peucker([(0.0, 0.0), (1.0, 0.0)], epsilon=1.0) == [(0.0, 0.0), (1.0, 0.0)]
    assert ramer_douglas_peucker([(0.0, 0.0), (1.0, 0.1), (2.0, 0.0)], epsilon=0.5) == [(0.0, 0.0), (2.0, 0.0)]
    assert ramer_douglas_peucker([(0.0, 0.0), (1.0, 1.0), (2.0, 0.0)], epsilon=0.5) == [(0.0, 0.0), (1.0, 1.0), (2.0, 0.0)]
