import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert convert_si_prefix(1, SIUnit.giga, SIUnit.mega) == 1000
    assert convert_si_prefix(1, SIUnit.mega, SIUnit.giga) == 0.001
    assert convert_si_prefix(1, SIUnit.kilo, SIUnit.kilo) == 1
    assert convert_si_prefix(1, 'giga', 'mega') == 1000
    assert convert_si_prefix(1, 'gIGa', 'mEGa') == 1000
    assert convert_binary_prefix(1, BinaryUnit.giga, BinaryUnit.mega) == 1024
    assert convert_binary_prefix(1, BinaryUnit.mega, BinaryUnit.giga) == 0.0009765625
    assert convert_binary_prefix(1, BinaryUnit.kilo, BinaryUnit.kilo) == 1
    assert convert_binary_prefix(1, 'giga', 'mega') == 1024
    assert convert_binary_prefix(1, 'gIGa', 'mEGa') == 1024
