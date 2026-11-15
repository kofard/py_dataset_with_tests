import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert euclidean_distance_sqr([1,2],[2,4]) == 5
    assert column_based_sort([(5, 1), (4, 2), (3, 0)], 1) == [(3, 0), (5, 1), (4, 2)]
    assert dis_between_closest_pair([[1,2],[2,4],[5,7],[8,9],[11,0]],5) == 5
    assert dis_between_closest_in_strip([[1,2],[2,4],[5,7],[8,9],[11,0]],5) == 85
    assert closest_pair_of_points_sqr([(1, 2), (3, 4)], [(5, 6), (7, 8)], 2) == 8
    assert closest_pair_of_points([(2, 3), (12, 30)], len([(2, 3), (12, 30)])) == 28.792360097775937
