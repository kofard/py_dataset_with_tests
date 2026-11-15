import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert score_function('A', 'A') == 1
    assert score_function('A', 'C') == -1
    assert score_function('-', 'A') == -2
    assert score_function('A', '-') == -2
    assert score_function('-', '-') == -2
    assert smith_waterman('ACAC', 'CA') == [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]]
    assert smith_waterman('acac', 'ca') == [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]]
    assert smith_waterman('ACAC', 'ca') == [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]]
    assert smith_waterman('acac', 'CA') == [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]]
    assert smith_waterman('ACAC', '') == [[0], [0], [0], [0], [0]]
    assert smith_waterman('', 'CA') == [[0, 0, 0]]
    assert smith_waterman('ACAC', 'CA') == [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]]
    assert smith_waterman('acac', 'ca') == [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]]
    assert smith_waterman('ACAC', 'ca') == [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]]
    assert smith_waterman('acac', 'CA') == [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]]
    assert smith_waterman('ACAC', '') == [[0], [0], [0], [0], [0]]
    assert smith_waterman('', 'CA') == [[0, 0, 0]]
    assert smith_waterman('AGT', 'AGT') == [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 2, 0], [0, 0, 0, 3]]
    assert smith_waterman('AGT', 'GTA') == [[0, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0], [0, 0, 2, 0]]
    assert smith_waterman('AGT', 'GTC') == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 2, 0]]
    assert smith_waterman('AGT', 'G') == [[0, 0], [0, 0], [0, 1], [0, 0]]
    assert smith_waterman('G', 'AGT') == [[0, 0, 0, 0], [0, 0, 1, 0]]
    assert smith_waterman('AGT', 'AGTCT') == [[0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0], [0, 0, 0, 3, 1, 1]]
    assert smith_waterman('AGTCT', 'AGT') == [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 2, 0], [0, 0, 0, 3], [0, 0, 0, 1], [0, 0, 0, 1]]
    assert smith_waterman('AGTCT', 'GTC') == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 2, 0], [0, 0, 0, 3], [0, 0, 1, 1]]
    assert traceback([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]], 'ACAC', 'CA') == 'CA\nCA'
    assert traceback([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]], 'acac', 'ca') == 'CA\nCA'
    assert traceback([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]], 'ACAC', 'ca') == 'CA\nCA'
    assert traceback([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 2], [0, 1, 0]], 'acac', 'CA') == 'CA\nCA'
    assert traceback([[0, 0, 0]], 'ACAC', '') == ''
