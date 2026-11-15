import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    arr = [100, 10, 52, 83]
    cc = CoordinateCompressor(arr)
    assert cc.compress(100) == 3
    assert cc.compress(52) == 1
    assert cc.decompress(1) == 52
    arr = [100, 10, 52, 83]
    cc = CoordinateCompressor(arr)
    assert cc.coordinate_map[83] == 2
    assert cc.reverse_map[2] == 83
    arr = [100, 10, 52, 83]
    cc = CoordinateCompressor(arr)
    assert cc.compress(100) == 3
    arr = [100, 10, 52, 83]
    cc = CoordinateCompressor(arr)
    assert cc.decompress(0) == 10
