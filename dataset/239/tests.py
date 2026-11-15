import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert rsafactor(3, 16971, 25777) == [149, 173]
    assert rsafactor(7331, 11, 27233) == [113, 241]
    assert rsafactor(4021, 13, 17711) == [89, 199]
