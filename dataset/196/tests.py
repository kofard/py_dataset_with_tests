import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert binomial_coefficient(4, 2) == 6
    assert catalan_number(5) == 42
    assert catalan_number(6) == 132
    import math
    assert all(factorial(i) == math.factorial(i) for i in range(10)) == True
    assert binary_tree_count(5) == 5040
    assert binary_tree_count(6) == 95040
