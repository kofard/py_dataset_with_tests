import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert cycle_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert cycle_sort([-4, 20, 0, -50, 100, -1]) == [-50, -4, -1, 0, 20, 100]
    assert cycle_sort([-.1, -.2, 1.3, -.8]) == [-0.8, -0.2, -0.1, 1.3]
    assert cycle_sort(["c", "a", "b"]) == ['a', 'b', 'c']
    assert cycle_sort([]) == []
