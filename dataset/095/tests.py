import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert fwht_xor([1, 2, 3, 4]) == [10, -2, -4, 0]
    assert fwht_xor([10, -2, -4, 0], inverse=True) == [1, 2, 3, 4]
    assert xor_convolution([1, 2], [3, 4]) == [11, 10]
    assert fwht_or([1, 2]) == [1, 3]
    assert fwht_or([1, 3], inverse=True) == [1, 2]
    assert or_convolution([1, 2], [3, 4]) == [3, 18]
    assert fwht_and([1, 2]) == [3, 2]
    assert fwht_and([3, 2], inverse=True) == [1, 2]
    assert and_convolution([1, 2], [3, 4]) == [13, 8]
