import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert nth_fibonacci_matrix(100) == 354224848179261915075
    assert nth_fibonacci_matrix(-100) == -100
    assert nth_fibonacci_bruteforce(100) == 354224848179261915075
    assert nth_fibonacci_bruteforce(-100) == -100
