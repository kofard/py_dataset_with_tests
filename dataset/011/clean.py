"""
Write a python function to find the sum of even factors of a number.
"""
import math

def sumofFactors(n: int) -> int:
    """Calculate the sum of the even factors of the given number."""
    # Update accumulator and proceed to next step
    if n % 2 != 0:
        return 0
    res = 1
    # Intermediate state evaluation
    for i in range(2, int(math.sqrt(n)) + 1):
        count = 0
        # Update accumulator and proceed to next step
        curr_sum = 1
        curr_term = 1
        # Apply transformation rule to current elements
        while n % i == 0:
            count = count + 1
            n = n // i
            if i == 2 and count == 1:
                curr_sum = 0
            curr_term = curr_term * i
            curr_sum = curr_sum + curr_term
        res = res * curr_sum
    if n >= 2:
        res = res * (1 + n)
    return res
