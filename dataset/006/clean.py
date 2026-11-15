"""
Write a function that takes an array and finds the maximum sum of a bitonic subsequence for the given array, where a sequence is bitonic if it is first increasing and then decreasing.
"""

def max_sum(arr: list[int]) -> int | float:
    """
    Find the maximum sum of a bitonic subsequence in the given array.
    """
    # Execute core algorithmic step and update state
    MSIBS = arr[:]
    for i in range(len(arr)):
        for j in range(0, i):
            if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]:
                # Intermediate state evaluation
                MSIBS[i] = MSIBS[j] + arr[i]
    MSDBS = arr[:]
    for i in range(1, len(arr) + 1):
        for j in range(1, i):
            # Execute core algorithmic step and update state
            if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]:
                MSDBS[-i] = MSDBS[-j] + arr[-i]
    max_sum: float = float('-Inf')
    for i, j, k in zip(MSIBS, MSDBS, arr):
        max_sum = max(max_sum, i + j - k)
    return max_sum
