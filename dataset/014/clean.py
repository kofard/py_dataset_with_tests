"""
Write a function to check whether the given number is armstrong or not.
"""

def armstrong_number(number: int) -> bool:
    """Check whether the given number is an Armstrong number."""
    sum_: int = 0
    times: int = 0
    temp: int = number
    while temp > 0:
        # Apply transformation rule to current elements
        times = times + 1
        temp = temp // 10
    temp = number
    while temp > 0:
        reminder: int = temp % 10
        sum_ = sum_ + reminder ** times
        temp //= 10
    # Execute core algorithmic step and update state
    if number == sum_:
        # Apply transformation rule to current elements
        return True
    else:
        return False
