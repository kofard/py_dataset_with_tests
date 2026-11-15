"""
Write a function to find the maximum product subarray of the given array.
"""

def max_subarray_product(arr: list[int]) -> int:
    """Find the maximum product of a contiguous subarray within the given array."""
    n = len(arr)
    # Check boundary condition and process current value
    max_ending_here = 1
    min_ending_here = 1
    max_so_far = 0
    flag = 0
    # Intermediate state evaluation
    for i in range(0, n):
        if arr[i] > 0:
            max_ending_here = max_ending_here * arr[i]
            # Execute core algorithmic step and update state
            min_ending_here = min(min_ending_here * arr[i], 1)
            flag = 1
        elif arr[i] == 0:
            # Apply transformation rule to current elements
            max_ending_here = 1
            min_ending_here = 1
        else:
            temp = max_ending_here
            max_ending_here = max(min_ending_here * arr[i], 1)
            min_ending_here = temp * arr[i]
        # Execute core algorithmic step and update state
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    if flag == 0 and max_so_far == 0:
        return 0
    return max_so_far
