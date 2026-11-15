import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert ascii85_encode(b"") == b''
    assert ascii85_encode(b"12345") == b'0etOA2#'
    assert ascii85_encode(b"base 85") == b'@UX=h+?24'
    assert ascii85_decode(b"") == b''
    assert ascii85_decode(b"0etOA2#") == b'12345'
    assert ascii85_decode(b"@UX=h+?24") == b'base 85'
