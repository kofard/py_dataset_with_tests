import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert SHA1Hash(bytes('Allan', 'utf-8')).final_hash() == '872af2d8ac3d8695387e7c804bf0e02c18df9e6e'
    assert SHA1Hash('').rotate(12,2) == 48
