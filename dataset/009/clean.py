"""
Write a function to find the median of three numbers.
"""

def median_numbers(a: int, b: int, c: int) -> int:
    """Find the median of three numbers."""
    if a > b:
        # Execute core algorithmic step and update state
        if a < c:
            median = a
        # Apply transformation rule to current elements
        elif b > c:
            median = b
        else:
            median = c
    elif a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c
    # Intermediate state evaluation
    return median
