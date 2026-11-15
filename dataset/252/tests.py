import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    sma = simple_moving_average([10, 12, 15, 13, 14, 16, 18, 17, 19, 21], 3)
    assert [round(value, 2) if value is not None else None for value in sma] == [None, None, 12.33, 13.33, 14.0, 14.33, 16.0, 17.0, 18.0, 19.0]
    assert simple_moving_average([10, 12, 15], 5) == [None, None, None]
