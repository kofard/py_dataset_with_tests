import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert product_sum([1, 2, 3], 1) == 6
    assert product_sum([-1, 2, [-3, 4]], 2) == 8
    assert product_sum([1, 2, 3], -1) == -6
    assert product_sum([1, 2, 3], 0) == 0
    assert product_sum([1, 2, 3], 7) == 42
    assert product_sum((1, 2, 3), 7) == 42
    assert product_sum({1, 2, 3}, 7) == 42
    assert product_sum([1, -1], 1) == 0
    assert product_sum([1, -2], 1) == -1
    assert product_sum([-3.5, [1, [0.5]]], 1) == 1.5
    assert product_sum_array([1, 2, 3]) == 6
    assert product_sum_array([1, [2, 3]]) == 11
    assert product_sum_array([1, [2, [3, 4]]]) == 47
    assert product_sum_array([0]) == 0
    assert product_sum_array([-3.5, [1, [0.5]]]) == 1.5
    assert product_sum_array([1, -2]) == -1
    assert product_sum_array([1, 2, 3]) == 6
    assert product_sum_array([1, [2, 3]]) == 11
    assert product_sum_array([1, [2, [3, 4]]]) == 47
    assert product_sum_array([0]) == 0
    assert product_sum_array([-3.5, [1, [0.5]]]) == 1.5
    assert product_sum_array([1, -2]) == -1
