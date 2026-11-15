import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert XORCipher().encrypt("", 5) == []
    assert XORCipher().encrypt("hallo welt", 1) == ['i', '`', 'm', 'm', 'n', '!', 'v', 'd', 'm', 'u']
    assert XORCipher().encrypt("HALLO WELT", 32) == ['h', 'a', 'l', 'l', 'o', '\x00', 'w', 'e', 'l', 't']
    assert XORCipher().encrypt("hallo welt", 256) == ['h', 'a', 'l', 'l', 'o', ' ', 'w', 'e', 'l', 't']
    assert XORCipher().decrypt("", 5) == []
    assert XORCipher().decrypt("hallo welt", 1) == ['i', '`', 'm', 'm', 'n', '!', 'v', 'd', 'm', 'u']
    assert XORCipher().decrypt("HALLO WELT", 32) == ['h', 'a', 'l', 'l', 'o', '\x00', 'w', 'e', 'l', 't']
    assert XORCipher().decrypt("hallo welt", 256) == ['h', 'a', 'l', 'l', 'o', ' ', 'w', 'e', 'l', 't']
    assert XORCipher().encrypt_string("", 5) == ''
    assert XORCipher().encrypt_string("hallo welt", 1) == 'i`mmn!vdmu'
    assert XORCipher().encrypt_string("HALLO WELT", 32) == 'hallo\x00welt'
    assert XORCipher().encrypt_string("hallo welt", 256) == 'hallo welt'
    assert XORCipher().decrypt_string("", 5) == ''
    assert XORCipher().decrypt_string("hallo welt", 1) == 'i`mmn!vdmu'
    assert XORCipher().decrypt_string("HALLO WELT", 32) == 'hallo\x00welt'
    assert XORCipher().decrypt_string("hallo welt", 256) == 'hallo welt'
