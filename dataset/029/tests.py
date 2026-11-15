import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    A = Automaton(["what", "hat", "ver", "er"])
    assert A.search_in("whatever, err ... , wherever") == {'what': [0], 'hat': [1], 'ver': [5, 25], 'er': [6, 10, 22, 26]}
