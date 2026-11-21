import importlib.util
from itertools import combinations
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})


def test_solution():
    jobs = [(1, 3, 5), (2, 5, 6), (4, 6, 5), (6, 7, 4), (5, 8, 11), (7, 9, 2)]
    score, chosen = select_weighted_intervals(jobs)
    assert score == 17
    assert chosen == [1, 4]
    assert compatible_intervals(jobs, chosen)
    assert total_weight(jobs, chosen) == score

    assert select_weighted_intervals([]) == (0, [])
    assert select_weighted_intervals([(1, 4, -10)]) == (0, [])
    assert select_weighted_intervals([(1, 4, 9)]) == (9, [0])
    assert select_weighted_intervals([(1, 2, 3), (2, 3, 4)]) == (7, [0, 1])
    assert select_weighted_intervals([(1, 3, 3), (2, 4, 8)]) == (8, [1])
    assert select_weighted_intervals([(0, 1, 5), (1, 2, 5), (0, 2, 10)])[0] == 10
    assert not compatible_intervals(jobs, [0, 1])
    assert total_weight(jobs, [1, 4]) == 17

    # An independent exhaustive oracle for a small set of intervals.
    small = [(0, 3, 8), (1, 4, 9), (3, 5, 2), (4, 6, 5), (6, 8, 5)]
    maximum = 0
    for size in range(len(small) + 1):
        for subset in combinations(range(len(small)), size):
            if compatible_intervals(small, list(subset)):
                maximum = max(maximum, total_weight(small, list(subset)))
    value, picked = select_weighted_intervals(small)
    assert value == maximum
    assert compatible_intervals(small, picked)

    for invalid in ([(2, 1, 5)], [(0, float('nan'), 1)], [(0, 2, float('inf'))], [(0, 2)], [(True, 2, 3)]):
        try:
            select_weighted_intervals(invalid)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid interval was accepted")
