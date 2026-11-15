import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert ksa(b"Key")[:5] == [75, 51, 132, 157, 192]
    box = ksa(b"Key")
    stream = prga(box)
    assert [next(stream) for _ in range(5)] == [235, 159, 119, 129, 183]
    assert encrypt(b"Plaintext", b"Key") == b'\xbb\xf3\x16\xe8\xd9@\xaf\n\xd3'
    assert encrypt(b"pedia", b"Wiki") == b'\x10!\xbf\x04 '
    assert encrypt(b"\x10!\xbf\x04 ", b"Wiki") == b'pedia'
    assert decrypt(b'\x10!\xbf\x04 ', b"Wiki") == b'pedia'
