import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert length_conversion(1, "meter", "kilometer") == 0.001
    assert length_conversion(1, "meter", "megametre") == 1e-06
    assert length_conversion(1, "gigametre", "meter") == 1000000000
    assert length_conversion(1, "gigametre", "terametre") == 0.001
    assert length_conversion(1, "petametre", "terametre") == 1000
    assert length_conversion(1, "petametre", "exametre") == 0.001
    assert length_conversion(1, "terametre", "zettametre") == 1e-09
    assert length_conversion(1, "yottametre", "zettametre") == 1000
