import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    check_valid_key('LFWOAYUISVKMNXPBDCRJTQEGHZ')
    assert encrypt_message('LFWOAYUISVKMNXPBDCRJTQEGHZ', 'Harshil Darji') == 'Ilcrism Olcvs'
    assert decrypt_message('LFWOAYUISVKMNXPBDCRJTQEGHZ', 'Ilcrism Olcvs') == 'Harshil Darji'
    random.seed(0)
    assert get_random_key() == 'OAXSGFHKWUECVDRLTJZPQIBNYM'
