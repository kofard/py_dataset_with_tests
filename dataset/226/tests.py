import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
    assert rank_of_matrix(matrix1) == 2
    matrix2 = [[1, 0, 0],
           [0, 1, 0],
           [0, 0, 0]]
    assert rank_of_matrix(matrix2) == 2
    matrix3 = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12]]
    assert rank_of_matrix(matrix3) == 2
    assert rank_of_matrix([[2,3,-1,-1],
               [1,-1,-2,4],
               [3,1,3,-2],
               [6,3,0,-7]]) == 4
    assert rank_of_matrix([[2,1,-3,-6],
               [3,-3,1,2],
               [1,1,1,2]]) == 3
    assert rank_of_matrix([[2,-1,0],
               [1,3,4],
               [4,1,-3]]) == 3
    assert rank_of_matrix([[3,2,1],
               [-6,-4,-2]]) == 1
    assert rank_of_matrix([[],[]]) == 0
    assert rank_of_matrix([[1]]) == 1
    assert rank_of_matrix([[]]) == 0
