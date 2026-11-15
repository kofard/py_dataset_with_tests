import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert encode_to_morse("defend the east") == '-..x.x..-.x.x-.x-..xx-x....x.xx.x.-x...x-'
    assert encrypt_fractionated_morse("defend the east","Roundtable") == 'ESOAVVLJRSSTRX'
    assert decrypt_fractionated_morse("ESOAVVLJRSSTRX","Roundtable") == 'DEFEND THE EAST'
