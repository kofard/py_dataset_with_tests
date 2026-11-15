import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert largest_square_area_in_matrix_top_down_approch(2, 2, [[1,1], [1,1]]) == 2
    assert largest_square_area_in_matrix_top_down_approch(2, 2, [[0,0], [0,0]]) == 0
    assert largest_square_area_in_matrix_top_down_approch_with_dp(2, 2, [[1,1], [1,1]]) == 2
    assert largest_square_area_in_matrix_top_down_approch_with_dp(2, 2, [[0,0], [0,0]]) == 0
    assert largest_square_area_in_matrix_bottom_up(2, 2, [[1,1], [1,1]]) == 2
    assert largest_square_area_in_matrix_bottom_up(2, 2, [[0,0], [0,0]]) == 0
    assert largest_square_area_in_matrix_bottom_up_space_optimization(2, 2, [[1,1], [1,1]]) == 2
    assert largest_square_area_in_matrix_bottom_up_space_optimization(2, 2, [[0,0], [0,0]]) == 0
