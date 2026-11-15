import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert decimal_to_any(0, 2) == '0'
    assert decimal_to_any(5, 4) == '11'
    assert decimal_to_any(20, 3) == '202'
    assert decimal_to_any(58, 16) == '3A'
    assert decimal_to_any(243, 17) == 'E5'
    assert decimal_to_any(34923, 36) == 'QY3'
    assert decimal_to_any(10, 11) == 'A'
    assert decimal_to_any(16, 16) == '10'
    assert decimal_to_any(36, 36) == '10'
