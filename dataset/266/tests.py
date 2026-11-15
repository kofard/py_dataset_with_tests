import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert straight_line_depreciation(10, 1100.0, 100.0) == [100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0]
    assert straight_line_depreciation(6, 1250.0, 50.0) == [200.0, 200.0, 200.0, 200.0, 200.0, 200.0]
    assert straight_line_depreciation(4, 1001.0) == [250.25, 250.25, 250.25, 250.25]
    assert straight_line_depreciation(11, 380.0, 50.0) == [30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0]
    assert straight_line_depreciation(1, 4985, 100) == [4885.0]
