import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert NumberContainer().binary_search_delete([1,2,3], 2) == [1, 3]
    assert NumberContainer().binary_search_delete([0, 0, 0], 0) == [0, 0]
    assert NumberContainer().binary_search_delete([-1, -1, -1], -1) == [-1, -1]
    assert NumberContainer().binary_search_delete([-1, 0], 0) == [-1]
    assert NumberContainer().binary_search_delete([-1, 0], -1) == [0]
    assert NumberContainer().binary_search_delete(range(7), 3) == [0, 1, 2, 4, 5, 6]
    assert NumberContainer().binary_search_delete([1.1, 2.2, 3.3], 2.2) == [1.1, 3.3]
    assert NumberContainer().binary_search_delete("abcde", "c") == ['a', 'b', 'd', 'e']
    assert NumberContainer().binary_search_insert([1,2,3], 2) == [1, 2, 2, 3]
    assert NumberContainer().binary_search_insert([0,1,3], 2) == [0, 1, 2, 3]
    assert NumberContainer().binary_search_insert([-5, -3, 0, 0, 11, 103], 51) == [-5, -3, 0, 0, 11, 51, 103]
    assert NumberContainer().binary_search_insert([-5, -3, 0, 0, 11, 100, 103], 101) == [-5, -3, 0, 0, 11, 100, 101, 103]
    assert NumberContainer().binary_search_insert(range(10), 4) == [0, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9]
    assert NumberContainer().binary_search_insert("abd", "c") == ['a', 'b', 'c', 'd']
    cont = NumberContainer()
    cont.change(0, 10)
    cont.change(0, 20)
    cont.change(-13, 20)
    cont.change(-100030, 20032903290)
    cont = NumberContainer()
    assert cont.find(10) == -1
    cont.change(0, 10)
    assert cont.find(10) == 0
    cont.change(0, 20)
    assert cont.find(10) == -1
    assert cont.find(20) == 0
