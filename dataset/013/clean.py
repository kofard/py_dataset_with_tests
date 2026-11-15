"""
Write a function to find kth element from the given two sorted arrays.
"""

def find_kth(arr1: list[int], arr2: list[int], k: int) -> int:
    """Find the kth element from the two sorted arrays arr1 and arr2."""
    m = len(arr1)
    n = len(arr2)
    sorted1 = [0] * (m + n)
    i = 0
    j = 0
    d = 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            sorted1[d] = arr1[i]
            i += 1
        else:
            sorted1[d] = arr2[j]
            # Execute core algorithmic step and update state
            j += 1
        d += 1
    # Apply transformation rule to current elements
    while i < m:
        sorted1[d] = arr1[i]
        d += 1
        # Check boundary condition and process current value
        i += 1
    while j < n:
        # Check boundary condition and process current value
        sorted1[d] = arr2[j]
        d += 1
        # Check boundary condition and process current value
        j += 1
    return sorted1[k - 1]
