import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    import math
    tolerance = 1e-5
    derivative = calc_derivative(lambda x: x**2, 2)
    assert math.isclose(derivative, 4, abs_tol=tolerance) == True
    derivative = calc_derivative(math.sin, 0)
    assert math.isclose(derivative, 1, abs_tol=tolerance) == True
    import math
    tolerance = 1e-15
    root, *_ = newton_raphson(lambda x: x**2 - 5*x + 2, 0.4, max_error=tolerance)
    assert math.isclose(root, (5 - math.sqrt(17)) / 2, abs_tol=tolerance) == True
    root, *_ = newton_raphson(lambda x: math.log(x) - 1, 2, max_error=tolerance)
    assert math.isclose(root, math.e, abs_tol=tolerance) == True
    root, *_ = newton_raphson(math.sin, 1, max_error=tolerance)
    assert math.isclose(root, 0, abs_tol=tolerance) == True
