import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    ft = MaxFenwickTree(5)
    assert ft.query(0, 5) == 0
    ft.update(4, 100)
    assert ft.query(0, 5) == 100
    ft.update(4, 0)
    ft.update(2, 20)
    assert ft.query(0, 5) == 20
    ft.update(4, 10)
    assert ft.query(2, 5) == 20
    assert ft.query(1, 5) == 20
    ft.update(2, 0)
    assert ft.query(0, 5) == 10
    ft = MaxFenwickTree(10000)
    ft.update(255, 30)
    assert ft.query(0, 10000) == 30
    ft = MaxFenwickTree(6)
    ft.update(5, 1)
    assert ft.query(5, 6) == 1
    ft = MaxFenwickTree(6)
    ft.update(0, 1000)
    assert ft.query(0, 1) == 1000
    ft = MaxFenwickTree(8)
    ft.update(4, 20)
    ft.update(5, 1)
    assert ft.query(0, 6) == 20
    ft.update(4, 0)
    assert ft.query(0, 6) == 1
    ft.update(5, 0)
    assert ft.query(0, 6) == 0
    ft = MaxFenwickTree(8)
    ft.update(5, 100)
    ft.update(4, 0)
    assert ft.query(0, 6) == 100
