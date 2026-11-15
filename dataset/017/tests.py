import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert combination_lists(n=4, k=2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert generate_all_combinations(n=4, k=2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert generate_all_combinations(n=0, k=0) == [[]]
    assert generate_all_combinations(n=5, k=4) == [[1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 4, 5], [1, 3, 4, 5], [2, 3, 4, 5]]
    assert generate_all_combinations(n=3, k=3) == [[1, 2, 3]]
    assert generate_all_combinations(n=3, k=1) == [[1], [2], [3]]
    assert generate_all_combinations(n=1, k=0) == [[]]
    assert generate_all_combinations(n=1, k=1) == [[1]]
    from itertools import combinations
    assert all(generate_all_combinations(n, k) == combination_lists(n, k)
    for n in range(1, 6) for k in range(1, 6)) == True
    create_all_state(1, 4, 2, [], result := [])
    assert result == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    create_all_state(1, 3, 3, [], result := [])
    assert result == [[1, 2, 3]]
    create_all_state(2, 2, 1, [1], result := [])
    assert result == [[1, 2]]
    create_all_state(1, 0, 0, [], result := [])
    assert result == [[]]
    create_all_state(1, 4, 0, [1, 2], result := [])
    assert result == [[1, 2]]
    create_all_state(5, 4, 2, [1, 2], result := [])
    assert result == []
