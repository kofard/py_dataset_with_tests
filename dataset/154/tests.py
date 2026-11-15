import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert matrix_chain_multiply([1, 2, 3, 4, 3]) == 30
    assert matrix_chain_multiply([10]) == 0
    assert matrix_chain_multiply([10, 20]) == 0
    assert matrix_chain_multiply([19, 2, 19]) == 722
    assert matrix_chain_multiply(list(range(1, 100))) == 323398
    assert matrix_chain_order([1, 2, 3, 4, 3]) == 30
    assert matrix_chain_order([10]) == 0
    assert matrix_chain_order([10, 20]) == 0
    assert matrix_chain_order([19, 2, 19]) == 722
    assert matrix_chain_order(list(range(1, 100))) == 323398
