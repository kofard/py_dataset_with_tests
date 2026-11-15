import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert lin_search(0, 4, [4, 5, 6, 7], 7) == 3
    assert lin_search(0, 3, [4, 5, 6, 7], 7) == -1
    assert lin_search(0, 2, [-18, 2], -18) == 0
    assert lin_search(0, 1, [5], 5) == 0
    assert lin_search(0, 3, ['a', 'c', 'd'], 'c') == 1
    assert lin_search(0, 3, [.1, .4 , -.1], .1) == 0
    assert lin_search(0, 3, [.1, .4 , -.1], -.1) == 2
    test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    assert ite_ternary_search(test_list, 3) == -1
    assert ite_ternary_search(test_list, 13) == 4
    assert ite_ternary_search([4, 5, 6, 7], 4) == 0
    assert ite_ternary_search([4, 5, 6, 7], -10) == -1
    assert ite_ternary_search([-18, 2], -18) == 0
    assert ite_ternary_search([5], 5) == 0
    assert ite_ternary_search(['a', 'c', 'd'], 'c') == 1
    assert ite_ternary_search(['a', 'c', 'd'], 'f') == -1
    assert ite_ternary_search([], 1) == -1
    assert ite_ternary_search([.1, .4 , -.1], .1) == 0
    test_list_large = list(range(100))
    assert ite_ternary_search(test_list_large, 65) == 65
    assert ite_ternary_search(test_list_large, 105) == -1
    test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    assert rec_ternary_search(0, len(test_list), test_list, 3) == -1
    assert rec_ternary_search(4, len(test_list), test_list, 42) == 8
    assert rec_ternary_search(0, 2, [4, 5, 6, 7], 4) == 0
    assert rec_ternary_search(0, 3, [4, 5, 6, 7], -10) == -1
    assert rec_ternary_search(0, 1, [-18, 2], -18) == 0
    assert rec_ternary_search(0, 1, [5], 5) == 0
    assert rec_ternary_search(0, 2, ['a', 'c', 'd'], 'c') == 1
    assert rec_ternary_search(0, 2, ['a', 'c', 'd'], 'f') == -1
    assert rec_ternary_search(0, 0, [], 1) == -1
    assert rec_ternary_search(0, 3, [.1, .4 , -.1], .1) == 0
    test_list_large = list(range(100))
    assert rec_ternary_search(0, len(test_list_large), test_list_large, 65) == 65
    assert rec_ternary_search(20, 80, test_list_large, 65) == 65
    assert rec_ternary_search(20, 80, test_list_large, 15) == -1
