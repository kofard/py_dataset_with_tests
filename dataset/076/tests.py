import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert decimal_to_binary_iterative(0) == '0b0'
    assert decimal_to_binary_iterative(2) == '0b10'
    assert decimal_to_binary_iterative(7) == '0b111'
    assert decimal_to_binary_iterative(35) == '0b100011'
    assert decimal_to_binary_iterative(-2) == '-0b10'
    assert decimal_to_binary_recursive_helper(1000) == '1111101000'
    assert decimal_to_binary_recursive_helper("72") == '1001000'
    assert decimal_to_binary_recursive(0) == '0b0'
    assert decimal_to_binary_recursive(40) == '0b101000'
    assert decimal_to_binary_recursive(-40) == '-0b101000'
