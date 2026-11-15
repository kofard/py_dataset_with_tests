import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert _validator((1,1,1), (rotor1, rotor2, rotor3), 'POLAND') == ((1, 1, 1), ('EGZWVONAHDCLFQMSIPJBYUKXTR', 'FOBHMDKEXQNRAULPGSJVTYICZW', 'ZJXESIUQLHAVRMDOYGTNFWPBKC'), {'P': 'O', 'O': 'P', 'L': 'A', 'A': 'L', 'N': 'D', 'D': 'N'})
    assert _plugboard('PICTURES') == {'P': 'I', 'I': 'P', 'C': 'T', 'T': 'C', 'U': 'R', 'R': 'U', 'E': 'S', 'S': 'E'}
    assert _plugboard('POLAND') == {'P': 'O', 'O': 'P', 'L': 'A', 'A': 'L', 'N': 'D', 'D': 'N'}
    assert enigma('Hello World!', (1, 2, 1), plugb='pictures') == 'KORYH JUHHI!'
    assert enigma('KORYH, juhhi!', (1, 2, 1), plugb='pictures') == 'HELLO, WORLD!'
    assert enigma('hello world!', (1, 1, 1), plugb='pictures') == 'FPNCZ QWOBU!'
    assert enigma('FPNCZ QWOBU', (1, 1, 1), plugb='pictures') == 'HELLO WORLD'
