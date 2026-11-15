import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert binary_exp_recursive(3, 5) == 243
    assert binary_exp_recursive(11, 13) == 34522712143931
    assert binary_exp_recursive(-1, 3) == -1
    assert binary_exp_recursive(0, 5) == 0
    assert binary_exp_recursive(3, 1) == 3
    assert binary_exp_recursive(3, 0) == 1
    assert binary_exp_recursive(1.5, 4) == 5.0625
    assert binary_exp_iterative(3, 5) == 243
    assert binary_exp_iterative(11, 13) == 34522712143931
    assert binary_exp_iterative(-1, 3) == -1
    assert binary_exp_iterative(0, 5) == 0
    assert binary_exp_iterative(3, 1) == 3
    assert binary_exp_iterative(3, 0) == 1
    assert binary_exp_iterative(1.5, 4) == 5.0625
    assert binary_exp_mod_recursive(3, 4, 5) == 1
    assert binary_exp_mod_recursive(11, 13, 7) == 4
    assert binary_exp_mod_recursive(1.5, 4, 3) == 2.0625
    assert binary_exp_mod_iterative(3, 4, 5) == 1
    assert binary_exp_mod_iterative(11, 13, 7) == 4
    assert binary_exp_mod_iterative(1.5, 4, 3) == 2.0625
