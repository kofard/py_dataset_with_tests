import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    joint_distribution =  joint_probability_distribution(
    [1, 2], [-2, 5, 8], [0.7, 0.3], [0.3, 0.5, 0.2]
)
    from math import isclose
    assert isclose(joint_distribution.pop((1, 8)), 0.14) == True
    assert joint_distribution == {(1, -2): 0.21, (1, 5): 0.35, (2, -2): 0.09, (2, 5): 0.15, (2, 8): 0.06}
    from math import isclose
    assert isclose(expectation([1, 2], [0.7, 0.3]), 1.3) == True
    from math import isclose
    assert isclose(variance([1,2],[0.7,0.3]), 0.21) == True
    assert covariance([1, 2], [-2, 5, 8], [0.7, 0.3], [0.3, 0.5, 0.2]) == -2.7755575615628914e-17
    assert standard_deviation(0.21) == 0.458257569495584
