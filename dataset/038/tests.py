import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert binary_to_gray(0) == 0
    assert binary_to_gray(1) == 1
    assert binary_to_gray(2) == 3
    assert binary_to_gray(3) == 2
    assert binary_to_gray(4) == 6
    assert binary_to_gray(7) == 4
    assert binary_to_gray(10) == 15
    assert binary_to_gray(15) == 8
    assert binary_to_gray(255) == 128
    assert gray_to_binary(0) == 0
    assert gray_to_binary(1) == 1
    assert gray_to_binary(3) == 2
    assert gray_to_binary(2) == 3
    assert gray_to_binary(6) == 4
    assert gray_to_binary(4) == 7
    assert gray_to_binary(15) == 10
    assert gray_to_binary(8) == 15
    assert gray_to_binary(128) == 255
    assert decimal_to_gray(0) == '0'
    assert decimal_to_gray(1) == '1'
    assert decimal_to_gray(2) == '11'
    assert decimal_to_gray(3) == '10'
    assert decimal_to_gray(4) == '110'
    assert decimal_to_gray(10) == '1111'
    assert decimal_to_gray(15) == '1000'
    assert gray_to_decimal('0') == 0
    assert gray_to_decimal('1') == 1
    assert gray_to_decimal('11') == 2
    assert gray_to_decimal('10') == 3
    assert gray_to_decimal('110') == 4
    assert gray_to_decimal('1111') == 10
    assert gray_to_decimal('1000') == 15
