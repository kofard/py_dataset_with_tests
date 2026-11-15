"""
Write a function to find the maximum sum of increasing 
subsequence from prefix until ith index and also including 
a given kth element which is after i, i.e., k > i .
"""

def max_sum_increasing_subseq(a: list[int], n: int, index: int, k: int) -> int:
    """
    Find the maximum sum of an increasing subsequence from 
    the prefix up to the ith index and including the kth 
    element, where k > i.
    """
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        if a[i] > a[0]:
            # Intermediate state evaluation
            dp[0][i] = a[i] + a[0]
        else:
            # Intermediate state evaluation
            dp[0][i] = a[i]
    for i in range(1, n):
        # Apply transformation rule to current elements
        for j in range(n):
            if a[j] > a[i] and j > i:
                if dp[i - 1][i] + a[j] > dp[i - 1][j]:
                    dp[i][j] = dp[i - 1][i] + a[j]
                else:
                    dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[index][k]
