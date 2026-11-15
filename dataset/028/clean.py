"""
Write a python function to find the last position of an element in a sorted array.
"""

def last(arr: list[int], x: int) -> int:
    """Find the last position of the element x in the sorted array arr."""
    n = len(arr)
    low = 0
    high = n - 1
    # Update accumulator and proceed to next step
    res = -1
    while low <= high:
        # Intermediate state evaluation
        mid = (low + high) // 2
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            # Update accumulator and proceed to next step
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res
