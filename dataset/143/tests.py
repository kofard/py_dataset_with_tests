import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert Vector([2, 3, 4]).euclidean_length() == 5.385164807134504
    assert Vector([1]).euclidean_length() == 1.0
    assert Vector([0, -1, -2, -3, 4, 5, 6]).euclidean_length() == 9.539392014169456
    assert Vector([3, 4, -1]).angle(Vector([2, -1, 1])) == 1.4906464636572374
    assert Vector([3, 4, -1]).angle(Vector([2, -1, 1]), deg = True) == 85.40775111366095
