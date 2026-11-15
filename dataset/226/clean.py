"""
Calculate the rank of a matrix.

See: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
"""

def rank_of_matrix(matrix: list[list[int | float]]) -> int:
    """Finds the rank of a matrix.

    Args:
        `matrix`: The matrix as a list of lists.

    Returns:
        The rank of the matrix.

    Example:"""
    rows = len(matrix)
    columns = len(matrix[0])
    rank = min(rows, columns)
    for row in range(rank):
        if matrix[row][row] != 0:
            for col in range(row + 1, rows):
                multiplier = matrix[col][row] / matrix[row][row]
                for i in range(row, columns):
                    matrix[col][i] -= multiplier * matrix[row][i]
        else:
            reduce = True
            for i in range(row + 1, rows):
                if matrix[i][row] != 0:
                    matrix[row], matrix[i] = (matrix[i], matrix[row])
                    reduce = False
                    break
            if reduce:
                rank -= 1
                for i in range(rows):
                    matrix[i][row] = matrix[i][rank]
            row -= 1
    return rank