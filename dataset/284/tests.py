import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert encrypt_message('HDarji', 'This is Harshil Darji from Dharmaj.') == 'Akij ra Odrjqqs Gaisq muod Mphumrs.'
    assert decrypt_message('HDarji', 'Akij ra Odrjqqs Gaisq muod Mphumrs.') == 'This is Harshil Darji from Dharmaj.'
