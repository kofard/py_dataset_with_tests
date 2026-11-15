import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert fractional_cover((Item(10, 60), Item(20, 100), Item(30, 120)), capacity=50) == 240.0
    assert fractional_cover([Item(20, 100), Item(30, 120), Item(10, 60)], capacity=25) == 135.0
    assert fractional_cover([Item(10, 60), Item(20, 100), Item(30, 120)], capacity=60) == 280.0
    assert fractional_cover(items=[Item(5, 30), Item(10, 60), Item(15, 90)], capacity=30) == 180.0
    assert fractional_cover(items=[], capacity=50) == 0.0
    assert fractional_cover(items=[Item(10, 60)], capacity=5) == 30.0
    assert fractional_cover(items=[Item(10, 60)], capacity=1) == 6.0
    assert fractional_cover(items=[Item(10, 60)], capacity=0) == 0.0
    assert Item(10, 65).ratio == 6.5
    assert Item(20, 100).ratio == 5.0
    assert Item(30, 120).ratio == 4.0
