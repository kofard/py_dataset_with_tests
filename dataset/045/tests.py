import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    ba = BoothsAlgorithm()
    assert ba.find_minimal_rotation("baca") == 'abac'
    assert ba.find_minimal_rotation("aaab") == 'aaab'
    assert ba.find_minimal_rotation("abcd") == 'abcd'
    assert ba.find_minimal_rotation("dcba") == 'adcb'
    assert ba.find_minimal_rotation("aabaa") == 'aaaab'
