import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert logical_left_shift(0, 1) == '0b00'
    assert logical_left_shift(1, 1) == '0b10'
    assert logical_left_shift(1, 5) == '0b100000'
    assert logical_left_shift(17, 2) == '0b1000100'
    assert logical_left_shift(1983, 4) == '0b111101111110000'
    assert logical_right_shift(0, 1) == '0b0'
    assert logical_right_shift(1, 1) == '0b0'
    assert logical_right_shift(1, 5) == '0b0'
    assert logical_right_shift(17, 2) == '0b100'
    assert logical_right_shift(1983, 4) == '0b1111011'
    assert arithmetic_right_shift(0, 1) == '0b00'
    assert arithmetic_right_shift(1, 1) == '0b00'
    assert arithmetic_right_shift(-1, 1) == '0b11'
    assert arithmetic_right_shift(17, 2) == '0b000100'
    assert arithmetic_right_shift(-17, 2) == '0b111011'
    assert arithmetic_right_shift(-1983, 4) == '0b111110000100'
