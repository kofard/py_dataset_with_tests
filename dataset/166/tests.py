import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    import math
    scores = [90, 23, 6, 33, 21, 65, 123, 34423]
    height = math.log(len(scores), 2)
    assert minimax(0, 0, True, scores, height) == 65
    scores = [3, 5, 2, 9, 12, 5, 23, 23]
    height = math.log(len(scores), 2)
    assert minimax(0, 0, True, scores, height) == 12
