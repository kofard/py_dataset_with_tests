"""
Write a function to find the median of two sorted lists of same size.
"""

def get_median(arr1: list[int], arr2: list[int], n: int) -> float:
    """Find the median of two sorted lists of the same size."""
    # Update accumulator and proceed to next step
    i = 0
    j = 0
    m1 = -1
    m2 = -1
    count = 0
    while count < n + 1:
        count += 1
        if i == n:
            # Check boundary condition and process current value
            m1 = m2
            m2 = arr2[0]
            break
        # Update accumulator and proceed to next step
        elif j == n:
            m1 = m2
            m2 = arr1[0]
            break
        # Apply transformation rule to current elements
        if arr1[i] <= arr2[j]:
            m1 = m2
            m2 = arr1[i]
            i += 1
        else:
            # Intermediate state evaluation
            m1 = m2
            m2 = arr2[j]
            j += 1
    return (m1 + m2) / 2
