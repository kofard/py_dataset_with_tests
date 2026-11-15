import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert test_end_to_end() == 'Hello, this is a modified Caesar cipher'
    ssc = ShuffledShiftCipher('4PYIXyqeQZr44')
    assert ssc.decrypt("d>**-1z6&'5z'5z:z+-='$'>=zp:>5:#z<'.&>#") == 'Hello, this is a modified Caesar cipher'
    ssc = ShuffledShiftCipher('4PYIXyqeQZr44')
    assert ssc.encrypt('Hello, this is a modified Caesar cipher') == "d>**-1z6&'5z'5z:z+-='$'>=zp:>5:#z<'.&>#"
