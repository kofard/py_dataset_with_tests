import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    check_validity({'v1':2,'v2':4,'p1':6})
    assert find_target_variable({'v1':1,'v2':2,'p2':4}) == 'p1'
    assert boyles_law({'p1':100,'v2':150, 'v1':120}) == {'p2': '80.0 Pa'}
    assert boyles_law({'p1':10,'v1':20, 'p2':20}) == {'v2': '10.0 L'}
    assert boyles_law({'v1':13,'p2':17, 'v2':19}) == {'p1': '24.846 Pa'}
    assert boyles_law({'v2':27,'p1':25, 'p2':29}) == {'v1': '31.32 L'}
