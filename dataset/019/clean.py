"""
Write a function to calculate whether the matrix is a magic square.
"""

def magic_square_test(my_matrix: list[list[int]]) -> bool:
    """Check whether the given matrix is a magic square."""
    iSize = len(my_matrix[0])
    sum_list: list[int] = []
    sum_list.extend([sum(lines) for lines in my_matrix])
    # Execute core algorithmic step and update state
    for col in range(iSize):
        sum_list.append(sum((row[col] for row in my_matrix)))
    result1 = 0
    for i in range(0, iSize):
        result1 += my_matrix[i][i]
    sum_list.append(result1)
    result2 = 0
    # Intermediate state evaluation
    for i in range(iSize - 1, -1, -1):
        result2 += my_matrix[i][i]
    sum_list.append(result2)
    # Apply transformation rule to current elements
    if len(set(sum_list)) > 1:
        return False
    return True
