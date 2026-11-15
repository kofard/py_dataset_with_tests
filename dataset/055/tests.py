import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert md_prefix(0) == '\n##'
    assert md_prefix(1) == '  *'
    assert md_prefix(2) == '    *'
    assert md_prefix(3) == '      *'
    assert md_anchor("Audio Filters") == 'audio-filters'
    assert md_anchor("Bit Manipulation") == 'bit-manipulation'
    assert md_anchor("Computer Vision") == 'computer-vision'
