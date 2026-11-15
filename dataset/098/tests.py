import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert find_triplets_with_0_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert find_triplets_with_0_sum([]) == []
    assert find_triplets_with_0_sum([0, 0, 0]) == [[0, 0, 0]]
    assert find_triplets_with_0_sum([1, 2, 3, 0, -1, -2, -3]) == [[-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
    assert find_triplets_with_0_sum_hashing([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]]
    assert find_triplets_with_0_sum_hashing([]) == []
    assert find_triplets_with_0_sum_hashing([0, 0, 0]) == [[0, 0, 0]]
    assert find_triplets_with_0_sum_hashing([1, 2, 3, 0, -1, -2, -3]) == [[-1, 0, 1], [-3, 1, 2], [-2, 0, 2], [-2, -1, 3], [-3, 0, 3]]
    assert find_triplets_with_0_sum_two_pointers([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert find_triplets_with_0_sum_two_pointers([]) == []
    assert find_triplets_with_0_sum_two_pointers([0, 0, 0, 0]) == [[0, 0, 0]]
