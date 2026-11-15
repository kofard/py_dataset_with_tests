"""
LeetCode 36. Valid Sudoku
https://leetcode.com/problems/valid-sudoku/
https://en.wikipedia.org/wiki/Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
validated according to the following rules:

- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
  without repetition.

Note:

A Sudoku board (partially filled) could be valid but is not necessarily
solvable.

Only the filled cells need to be validated according to the mentioned rules.
"""
from collections import defaultdict
NUM_SQUARES = 9
EMPTY_CELL = '.'

def is_valid_sudoku_board(sudoku_board: list[list[str]]) -> bool:
    """This function validates (but does not solve) a sudoku board.
    The board may be valid but unsolvable."""
    if len(sudoku_board) != NUM_SQUARES or any((len(row) != NUM_SQUARES for row in sudoku_board)):
        error_message = f'Sudoku boards must be {NUM_SQUARES}x{NUM_SQUARES} squares.'
        raise ValueError(error_message)
    row_values: defaultdict[int, set[str]] = defaultdict(set)
    col_values: defaultdict[int, set[str]] = defaultdict(set)
    box_values: defaultdict[tuple[int, int], set[str]] = defaultdict(set)
    for row in range(NUM_SQUARES):
        for col in range(NUM_SQUARES):
            value = sudoku_board[row][col]
            if value == EMPTY_CELL:
                continue
            box = (row // 3, col // 3)
            if value in row_values[row] or value in col_values[col] or value in box_values[box]:
                return False
            row_values[row].add(value)
            col_values[col].add(value)
            box_values[box].add(value)
    return True