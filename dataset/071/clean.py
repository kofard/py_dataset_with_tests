def is_valid(puzzle: list[list[str]], word: str, row: int, col: int, vertical: bool) -> bool:
    """Check if a word can be placed at the given position.
    A cell is valid if it is empty or already contains the correct letter
    (enabling crossing/intersection between words)."""
    rows, cols = (len(puzzle), len(puzzle[0]))
    for i, ch in enumerate(word):
        r, c = (row + i, col) if vertical else (row, col + i)
        if r >= rows or c >= cols:
            return False
        cell = puzzle[r][c]
        if cell not in ('', ch):
            return False
    return True

def place_word(puzzle: list[list[str]], word: str, row: int, col: int, vertical: bool) -> None:
    """Place a word at the given position in the puzzle."""
    for i, ch in enumerate(word):
        if vertical:
            puzzle[row + i][col] = ch
        else:
            puzzle[row][col + i] = ch

def remove_word(puzzle: list[list[str]], word: str, row: int, col: int, vertical: bool, snapshot: list[list[str]]) -> None:
    """Remove a word from the puzzle, restoring only cells that were empty
    before placement. Cells shared with crossing words are preserved."""
    for i in range(len(word)):
        r, c = (row + i, col) if vertical else (row, col + i)
        if snapshot[r][c] == '':
            puzzle[r][c] = ''

def solve_crossword(puzzle: list[list[str]], words: list[str]) -> bool:
    """Solve the crossword puzzle using backtracking.
    Words are tried longest-first to prune the search space early.
    Intersections between words (shared letters) are supported."""
    if not words:
        return True
    remaining = sorted(words, key=len, reverse=True)
    word, rest = (remaining[0], remaining[1:])
    for row in range(len(puzzle)):
        for col in range(len(puzzle[0])):
            for vertical in (True, False):
                if is_valid(puzzle, word, row, col, vertical):
                    snapshot = [r[:] for r in puzzle]
                    place_word(puzzle, word, row, col, vertical)
                    if solve_crossword(puzzle, rest):
                        return True
                    remove_word(puzzle, word, row, col, vertical, snapshot)
    return False