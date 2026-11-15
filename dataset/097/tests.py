import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert fibonacci(0) == 0
    assert fibonacci(2) == 1
    assert fibonacci(5) == 5
    assert fibonacci(15) == 610
    assert fibonacci_search([4, 5, 6, 7], 4) == 0
    assert fibonacci_search([4, 5, 6, 7], -10) == -1
    assert fibonacci_search([-18, 2], -18) == 0
    assert fibonacci_search([5], 5) == 0
    assert fibonacci_search(['a', 'c', 'd'], 'c') == 1
    assert fibonacci_search(['a', 'c', 'd'], 'f') == -1
    assert fibonacci_search([], 1) == -1
    assert fibonacci_search([.1, .4 , 7], .4) == 1
    assert fibonacci_search([], 9) == -1
    assert fibonacci_search(list(range(100)), 63) == 63
    assert fibonacci_search(list(range(100)), 99) == 99
    assert fibonacci_search(list(range(-100, 100, 3)), -97) == 1
    assert fibonacci_search(list(range(-100, 100, 3)), 0) == -1
    assert fibonacci_search(list(range(-100, 100, 5)), 0) == 20
    assert fibonacci_search(list(range(-100, 100, 5)), 95) == 39
