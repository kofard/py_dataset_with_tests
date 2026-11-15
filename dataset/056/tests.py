import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert encrypt('The quick brown fox jumps over the lazy dog', 8) == 'bpm yCqks jzwEv nwF rCuxA wDmz Bpm tiHG lwo'
    assert encrypt('A very large key', 8000) == 's nWjq dSjYW cWq'
    assert encrypt('a lowercase alphabet', 5, 'abcdefghijklmnopqrstuvwxyz') == 'f qtbjwhfxj fqumfgjy'
    assert decrypt('bpm yCqks jzwEv nwF rCuxA wDmz Bpm tiHG lwo', 8) == 'The quick brown fox jumps over the lazy dog'
    assert decrypt('s nWjq dSjYW cWq', 8000) == 'A very large key'
    assert decrypt('f qtbjwhfxj fqumfgjy', 5, 'abcdefghijklmnopqrstuvwxyz') == 'a lowercase alphabet'
    assert brute_force("jFyuMy xIH'N vLONy zILwy Gy!")[20] == "Please don't brute force me!"
