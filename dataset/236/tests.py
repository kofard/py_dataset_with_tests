import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert naive_cut_rod_recursive(4, [1, 5, 8, 9]) == 10
    assert naive_cut_rod_recursive(10, [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]) == 30
    assert top_down_cut_rod(4, [1, 5, 8, 9]) == 10
    assert top_down_cut_rod(10, [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]) == 30
    assert bottom_up_cut_rod(4, [1, 5, 8, 9]) == 10
    assert bottom_up_cut_rod(10, [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]) == 30
