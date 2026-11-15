import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert jacobi_symbol(2, 13) == -1
    assert jacobi_symbol(5, 19) == 1
    assert jacobi_symbol(7, 14) == 0
    random.seed(10)
    assert solovay_strassen(13, 5) == True
    assert solovay_strassen(9, 10) == False
    assert solovay_strassen(17, 15) == True
