import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert round(nth_root(9, 2),1) == 3.0
    assert int(round(nth_root(-8, 3, 0.001))) == -2
    assert int(round(nth_root(256, 4, 0.001))) == 4
    assert round(nth_root(2, 2), 5) == 1.41421
    assert round(nth_root(0.25, 2, 0.00000001), 1) == 0.5
    assert round(nth_root(-8/27, 3, 0.0000001), 5) == -0.66667
    assert nth_root(0, 2, 0.1) == 0.0
    assert nth_root(0.0, 5) == 0.0
    assert all(abs(nth_root(k, k, 0.00000001) - k**(1/k)) <= 1e-10 for k in range(1,10)) == True
