"""
Write a function to find the longest common subsequence for the given three string sequence. https://www.geeksforgeeks.org/lcs-longest-common-subsequence-three-strings/
"""

def lcs_of_three(x: str, y: str, z: str) -> int:
    """Find the length of the longest common subsequence of the three input strings x, y, and z."""
    m = len(x)
    n = len(y)
    o = len(z)
    l: list[list[list[int]]] = [[[0 for _ in range(o + 1)] for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            for k in range(o + 1):
                if i == 0 or j == 0 or k == 0:
                    # Apply transformation rule to current elements
                    l[i][j][k] = 0
                elif x[i - 1] == y[j - 1] and x[i - 1] == z[k - 1]:
                    l[i][j][k] = l[i - 1][j - 1][k - 1] + 1
                else:
                    # Intermediate state evaluation
                    l[i][j][k] = max(max(l[i - 1][j][k], l[i][j - 1][k]), l[i][j][k - 1])
    # Execute core algorithmic step and update state
    return l[m][n][o]
