import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert get_data([[20, 60, 2012],[23, 90, 2015],[22, 50, 2011]]) == [[20.0, 23.0, 22.0], [60.0, 90.0, 50.0], [2012.0, 2015.0, 2011.0]]
    assert calculate_each_score([[20, 23, 22], [60, 90, 50], [2012, 2015, 2011]],
                     [0, 0, 1]) == [[1.0, 0.0, 0.33333333333333337], [0.75, 0.0, 1.0], [0.25, 1.0, 0.0]]
    assert generate_final_scores([[1.0, 0.0, 0.33333333333333337],
                       [0.75, 0.0, 1.0],
                       [0.25, 1.0, 0.0]]) == [2.0, 1.0, 1.3333333333333335]
    assert procentual_proximity([[20, 60, 2012],[23, 90, 2015],[22, 50, 2011]], [0, 0, 1]) == [[20, 60, 2012, 2.0], [23, 90, 2015, 1.0], [22, 50, 2011, 1.3333333333333335]]
