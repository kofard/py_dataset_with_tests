import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert evaluate(["0"]) == 0.0
    assert evaluate(["-0"]) == -0.0
    assert evaluate(["1"]) == 1.0
    assert evaluate(["-1"]) == -1.0
    assert evaluate(["-1.1"]) == -1.1
    assert evaluate(["2", "1", "+", "3", "*"]) == 9.0
    assert evaluate(["2", "1.9", "+", "3", "*"]) == 11.7
    assert evaluate(["2", "-1.9", "+", "3", "*"]) == 0.30000000000000027
    assert evaluate(["4", "13", "5", "/", "+"]) == 6.6
    assert evaluate(["2", "-", "3", "+"]) == 1.0
    assert evaluate(["-4", "5", "*", "6", "-"]) == -26.0
    assert evaluate([]) == 0
