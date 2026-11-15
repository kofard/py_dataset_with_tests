import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert extended_euclidean_algorithm(1, 24) == (1, 0)
    assert extended_euclidean_algorithm(8, 14) == (2, -1)
    assert extended_euclidean_algorithm(240, 46) == (-9, 47)
    assert extended_euclidean_algorithm(1, -4) == (1, 0)
    assert extended_euclidean_algorithm(-2, -4) == (-1, 0)
    assert extended_euclidean_algorithm(0, -4) == (0, -1)
    assert extended_euclidean_algorithm(2, 0) == (1, 0)
