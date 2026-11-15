import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert add([[1,2],[3,4]],[[2,3],[4,5]]) == [[3, 5], [7, 9]]
    assert add([[1.2,2.4],[3,4]],[[2,3],[4,5]]) == [[3.2, 5.4], [7, 9]]
    assert add([[1, 2], [4, 5]], [[3, 7], [3, 4]], [[3, 5], [5, 7]]) == [[7, 14], [12, 16]]
    assert subtract([[1,2],[3,4]],[[2,3],[4,5]]) == [[-1, -1], [-1, -1]]
    assert subtract([[1,2.5],[3,4]],[[2,3],[4,5.5]]) == [[-1, -0.5], [-1, -1.5]]
    assert scalar_multiply([[1,2],[3,4]],5) == [[5, 10], [15, 20]]
    assert scalar_multiply([[1.4,2.3],[3,4]],5) == [[7.0, 11.5], [15, 20]]
    assert multiply([[1,2],[3,4]],[[5,5],[7,5]]) == [[19, 15], [43, 35]]
    assert multiply([[1,2.5],[3,4.5]],[[5,5],[7,5]]) == [[22.5, 17.5], [46.5, 37.5]]
    assert multiply([[1, 2, 3]], [[2], [3], [4]]) == [[20]]
    assert identity(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert transpose([[1,2],[3,4]]) # doctest: +ELLIPSIS == <map object at ...
    assert transpose([[1,2],[3,4]], return_map=False) == [[1, 3], [2, 4]]
    assert minor([[1, 2], [3, 4]], 1, 1) == [[1]]
    assert determinant([[1, 2], [3, 4]]) == -2
    assert determinant([[1.5, 2.5], [3, 4]]) == -1.5
    assert permanent([[1, 2], [3, 4]]) == 10
    assert permanent([[1.5, 2.5], [3, 4]]) == 13.5
    assert inverse([[1, 2], [3, 4]]) == [[-2.0, 1.0], [1.5, -0.5]]
    inverse([[1, 1], [1, 1]])
