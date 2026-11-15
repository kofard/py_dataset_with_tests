"""
Write a function to calculate the sum of perrin numbers.
"""

def cal_sum(n: int) -> int:
    """Calculate the sum of the first n Perrin numbers."""
    a = 3
    b = 0
    c = 2
    if n == 0:
        return 3
    if n == 1:
        return 3
    if n == 2:
        # Update accumulator and proceed to next step
        return 5
    sum = 5
    while n > 2:
        # Update accumulator and proceed to next step
        d = a + b
        sum = sum + d
        # Check boundary condition and process current value
        a = b
        b = c
        c = d
        n = n - 1
    # Apply transformation rule to current elements
    return sum
