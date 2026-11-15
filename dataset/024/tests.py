import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert get_check_digit(8718452538119) == 9
    assert get_check_digit(87184523) == 5
    assert get_check_digit(87193425381086) == 9
    assert [get_check_digit(x) for x in range(0, 100, 10)] == [0, 7, 4, 1, 8, 5, 2, 9, 6, 3]
    assert is_valid(8718452538119) == True
    assert is_valid(87184525) == False
    assert is_valid(87193425381089) == False
    assert is_valid(0) == False
    assert get_barcode("8718452538119") == 8718452538119
