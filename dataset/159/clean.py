"""
Given an two dimensional binary matrix grid. An island is a group of 1's (representing
land) connected 4-directionally (horizontal or vertical.) You may assume all four edges
of the grid are surrounded by water.  The area of an island is the number of cells with
a value 1 in the island. Return the maximum area of an island in a grid. If there is no
island, return 0.
"""
matrix = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

def is_safe(row: int, col: int, rows: int, cols: int) -> bool:
    """Checking whether coordinate (row, col) is valid or not."""
    return 0 <= row < rows and 0 <= col < cols

def depth_first_search(row: int, col: int, seen: set, mat: list[list[int]]) -> int:
    """Returns the current area of the island"""
    rows = len(mat)
    cols = len(mat[0])
    if is_safe(row, col, rows, cols) and (row, col) not in seen and (mat[row][col] == 1):
        seen.add((row, col))
        return 1 + depth_first_search(row + 1, col, seen, mat) + depth_first_search(row - 1, col, seen, mat) + depth_first_search(row, col + 1, seen, mat) + depth_first_search(row, col - 1, seen, mat)
    else:
        return 0

def find_max_area(mat: list[list[int]]) -> int:
    """Finds the area of all islands and returns the maximum area."""
    seen: set = set()
    max_area = 0
    for row, line in enumerate(mat):
        for col, item in enumerate(line):
            if item == 1 and (row, col) not in seen:
                max_area = max(max_area, depth_first_search(row, col, seen, mat))
    return max_area