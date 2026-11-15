import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert EditDistance().min_dist_top_down("intention", "execution") == 5
    assert EditDistance().min_dist_top_down("intention", "") == 9
    assert EditDistance().min_dist_top_down("", "") == 0
    assert EditDistance().min_dist_bottom_up("intention", "execution") == 5
    assert EditDistance().min_dist_bottom_up("intention", "") == 9
    assert EditDistance().min_dist_bottom_up("", "") == 0
