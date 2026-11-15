import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    mov_avg_calculator = StreamingMovingAverage(3)
    mov_avg_calculator.update(10.)
    mov_avg_calculator.update(12.)
    mov_avg_calculator.update(2.)
    mov_avg_calculator.update(1.)
    assert mov_avg_calculator.mov_avg == 5.0
    mov_avg_calculator = StreamingMovingAverage(5)
    mov_avg_calculator.update(2.)
    mov_avg_calculator.update(3.)
    assert mov_avg_calculator.mov_avg == 2.5
