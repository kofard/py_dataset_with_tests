import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert get_reverse_bit_string(9) == '10010000000000000000000000000000'
    assert get_reverse_bit_string(43) == '11010100000000000000000000000000'
    assert get_reverse_bit_string(2873) == '10011100110100000000000000000000'
    assert get_reverse_bit_string(2550136832) == '00000000000000000000000000011001'
    assert reverse_bit(25) == 2550136832
    assert reverse_bit(37) == 2751463424
    assert reverse_bit(21) == 2818572288
    assert reverse_bit(58) == 1543503872
    assert reverse_bit(0) == 0
    assert reverse_bit(256) == 8388608
    assert reverse_bit(2550136832) == 25
