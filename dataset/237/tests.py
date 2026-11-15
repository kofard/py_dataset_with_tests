import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    tests = {"III": 3, "CLIV": 154, "MIX": 1009, "MMD": 2500, "MMMCMXCIX": 3999}
    assert all(roman_to_int(key) == value for key, value in tests.items()) == True
    tests = {"III": 3, "CLIV": 154, "MIX": 1009, "MMD": 2500, "MMMCMXCIX": 3999}
    assert all(int_to_roman(value) == key for key, value in tests.items()) == True
