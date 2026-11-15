import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert is_keith_number(14) == True
    assert is_keith_number(19) == True
    assert is_keith_number(28) == True
    assert is_keith_number(47) == True
    assert is_keith_number(61) == True
    assert is_keith_number(75) == True
    assert is_keith_number(197) == True
    assert is_keith_number(742) == True
    assert is_keith_number(1104) == True
    assert is_keith_number(1537) == True
    assert is_keith_number(10) == False
    assert is_keith_number(12) == False
    assert is_keith_number(25) == False
    assert is_keith_number(100) == False
    assert is_keith_number(9) == False
    assert is_keith_number(1) == False
    assert is_keith_number(0) == False
    assert is_keith_number(-14) == False
    assert find_keith_numbers(100) == [14, 19, 28, 47, 61, 75]
    assert find_keith_numbers(200) == [14, 19, 28, 47, 61, 75, 197]
    assert find_keith_numbers(10) == []
