import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})


def test_solution():
    assert lcs_of_three('AGGT12', '12TXAYB', '12XBA') == 2
    assert lcs_of_three('Reels', 'Reelsfor', 'ReelsforReels') == 5
    assert lcs_of_three('abcd1e2', 'bc12ea', 'bd1ea') == 3
