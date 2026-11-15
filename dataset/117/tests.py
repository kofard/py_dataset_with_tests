import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert int_to_base(0, 21) == '0'
    assert int_to_base(23, 2) == '10111'
    assert int_to_base(58, 5) == '213'
    assert int_to_base(167, 16) == 'A7'
    assert sum_of_digits(103, 12) == '13'
    assert sum_of_digits(1275, 4) == '30'
    assert sum_of_digits(6645, 2) == '1001'
    assert harshad_numbers_in_base(15, 2) == ['1', '10', '100', '110', '1000', '1010', '1100']
    assert harshad_numbers_in_base(12, 34) == ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B']
    assert harshad_numbers_in_base(12, 4) == ['1', '2', '3', '10', '12', '20', '21']
    assert harshad_numbers_in_base(-12, 6) == []
    assert is_harshad_number_in_base(18, 10) == True
    assert is_harshad_number_in_base(21, 10) == True
    assert is_harshad_number_in_base(-21, 5) == False
