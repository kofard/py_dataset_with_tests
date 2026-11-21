import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert horizontal_distance(30, 45) == 91.77
    assert horizontal_distance(100, 78) == 414.76
    assert max_height(30, 45) == 22.94
    assert max_height(100, 78) == 487.82
    assert total_time(30, 45) == 4.33
    assert total_time(100, 78) == 19.95
    v0, angle = (25, 20)
    assert horizontal_distance(v0, angle) == 40.97
    assert max_height(v0, angle) == 3.73
    assert total_time(v0, angle) == 1.74
