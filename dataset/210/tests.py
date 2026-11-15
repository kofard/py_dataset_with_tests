import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert points_to_polynomial([[1, 0], [2, 0], [3, 0]]) == 'f(x)=x^2*0.0+x^1*-0.0+x^0*0.0'
    assert points_to_polynomial([[1, 1], [2, 1], [3, 1]]) == 'f(x)=x^2*0.0+x^1*-0.0+x^0*1.0'
    assert points_to_polynomial([[1, 3], [2, 3], [3, 3]]) == 'f(x)=x^2*0.0+x^1*-0.0+x^0*3.0'
    assert points_to_polynomial([[1, 1], [2, 2], [3, 3]]) == 'f(x)=x^2*0.0+x^1*1.0+x^0*0.0'
    assert points_to_polynomial([[1, 1], [2, 4], [3, 9]]) == 'f(x)=x^2*1.0+x^1*-0.0+x^0*0.0'
    assert points_to_polynomial([[1, 3], [2, 6], [3, 11]]) == 'f(x)=x^2*1.0+x^1*-0.0+x^0*2.0'
    assert points_to_polynomial([[1, -3], [2, -6], [3, -11]]) == 'f(x)=x^2*-1.0+x^1*-0.0+x^0*-2.0'
    assert points_to_polynomial([[1, 5], [2, 2], [3, 9]]) == 'f(x)=x^2*5.0+x^1*-18.0+x^0*18.0'
    assert points_to_polynomial([[1, 1], [1, 2], [1, 3]]) == 'x=1'
    assert points_to_polynomial([[0, 1], [1, 2], [2, 5]]) == 'f(x)=x^2*1.0+x^1*0.0+x^0*1.0'
