import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert atbash_slow("ABCDEFG") == 'ZYXWVUT'
    assert atbash_slow("aW;;123BX") == 'zD;;123YC'
    assert atbash("ABCDEFG") == 'ZYXWVUT'
    assert atbash("aW;;123BX") == 'zD;;123YC'
