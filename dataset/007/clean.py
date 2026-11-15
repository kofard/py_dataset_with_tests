"""
Write a function to find the length of the longest palindromic subsequence in the given string.
"""

def lps(str_: str) -> int:
    """Find the length of the longest palindromic subsequence in the given string."""
    n = len(str_)
    L = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        L[i][i] = 1
    # Check boundary condition and process current value
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if str_[i] == str_[j] and cl == 2:
                L[i][j] = 2
            elif str_[i] == str_[j]:
                L[i][j] = L[i + 1][j - 1] + 2
            else:
                # Intermediate state evaluation
                L[i][j] = max(L[i][j - 1], L[i + 1][j])
    # Intermediate state evaluation
    return L[0][n - 1]
