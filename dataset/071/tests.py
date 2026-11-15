import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    puzzle = [['', '', '', ''], ['', '', '', ''],
          ['', '', '', ''], ['', '', '', '']]
    assert is_valid(puzzle, 'word', 0, 0, True) == True
    assert is_valid(puzzle, 'word', 0, 0, False) == True
    puzzle2 = [['w', '', ''], ['o', '', ''], ['r', '', ''], ['d', '', '']]
    assert is_valid(puzzle2, 'word', 0, 0, True) == True
    assert is_valid(puzzle2, 'cat', 0, 0, True) == False
    puzzle = [['', '', '', ''], ['', '', '', ''],
          ['', '', '', ''], ['', '', '', '']]
    place_word(puzzle, 'word', 0, 0, True)
    assert puzzle == [['w', '', '', ''], ['o', '', '', ''], ['r', '', '', ''], ['d', '', '', '']]
    puzzle = [['w', 'o', 'r', 'd'], ['', '', '', ''],
          ['', '', '', ''], ['', '', '', '']]
    snap = [['', 'o', 'r', 'd'], ['', '', '', ''],
        ['', '', '', ''], ['', '', '', '']]
    remove_word(puzzle, 'word', 0, 0, False, snap)
    assert puzzle == [['', 'o', 'r', 'd'], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
    puzzle = [['', '', '', ''], ['', '', '', ''],
          ['', '', '', ''], ['', '', '', '']]
    assert solve_crossword(puzzle, ['word', 'four', 'more', 'last']) == True
    puzzle2 = [['', '', '', ''], ['', '', '', ''],
           ['', '', '', ''], ['', '', '', '']]
    assert solve_crossword(puzzle2, ['word', 'four', 'more', 'paragraphs']) == False
