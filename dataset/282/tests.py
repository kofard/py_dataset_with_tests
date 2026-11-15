import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert convert_to_2d(1.0, 2.0, 3.0, 10.0, 10.0) == (7.6923076923076925, 15.384615384615385)
    assert convert_to_2d(1, 2, 3, 10, 10) == (7.6923076923076925, 15.384615384615385)
    assert rotate(1.0, 2.0, 3.0, 'y', 90.0) == (3.130524675073759, 2.0, 0.4470070007889556)
    assert rotate(1, 2, 3, "z", 180) == (0.999736015495891, -2.0001319704760485, 3)
    assert rotate(1, 2, 3, "x", -90) == (1, -2.5049096187183877, -2.5933429780983657)
    assert rotate(1, 2, 3, "x", 450)  # 450 wrap around to 90 == (1, 3.5776792428178217, -0.44744970165427644)
