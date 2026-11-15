import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert remove_duplicates('Hello World!!') == 'Helo Wrd'
    assert encipher('Hello World!!', create_cipher_map('Goodbye!!')) == 'CYJJM VMQJB!!'
    cipher_map = create_cipher_map('Goodbye!!')
    assert decipher(encipher('Hello World!!', cipher_map), cipher_map) == 'HELLO WORLD!!'
