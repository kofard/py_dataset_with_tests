import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert assign_ranks([3.2, 1.5, 4.0, 2.7, 5.1]) == [3.0, 1.0, 4.0, 2.0, 5.0]
    assert assign_ranks([10.5, 8.1, 12.4, 9.3, 11.0]) == [3.0, 1.0, 5.0, 2.0, 4.0]
    assert assign_ranks([1, 1, 1, 1]) == [2.5, 2.5, 2.5, 2.5]
    x = [1, 2, 3, 4, 5]
    y = [5, 4, 3, 2, 1]
    assert calculate_spearman_rank_correlation(x, y) == -1.0
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    assert calculate_spearman_rank_correlation(x, y) == 1.0
    x = [1, 2, 3, 4, 5]
    y = [5, 1, 2, 9, 5]
    assert calculate_spearman_rank_correlation(x, y) == 0.4
    x = [5]
    y = [9]
