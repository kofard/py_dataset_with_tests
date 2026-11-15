import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert floyd(3) == '  * \n * * \n* * * \n'
    assert floyd(5) == '    * \n   * * \n  * * * \n * * * * \n* * * * * \n'
    assert reverse_floyd(3) == '* * * \n * * \n  * \n   '
    assert reverse_floyd(5) == '* * * * * \n * * * * \n  * * * \n   * * \n    * \n     '
    assert pretty_print(0) == '       ...       ....        nothing printing :('
    assert pretty_print(3) == '  * \n * * \n* * * \n* * * \n * * \n  * \n   '
