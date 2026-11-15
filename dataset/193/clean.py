"""
Approximate the nth root of a real number using Newton's Method.

The nth root of a real number R can be computed with Newton's method,
which starts with an initial guess x_0 and then iterates using the
recurrence relation:

x_{k + 1} = x_k - ((x_k)**n - R)/(n*(x_k)**(n-1))

The recurrence relation can be rewritten for computational efficiency:

x_{k + 1} = (n-1)/n*x_k + R/(n*(x_k)**(n-1))

Given a tolerance TOL, a stopping criterion can be set as:

abs(x_{k + 1} - x_k) < TOL

References:
- https://en.wikipedia.org/wiki/Nth_root#Using_Newton's_method
- Sauer, T. (2011): Numerical analysis.
    USA. Addison-Wesley Publishing Company.
"""
from math import pow

def nth_root(radicand: float, index: int, tolerance: float=0.0001) -> float:
    """Approximate the nth root of the radicand for the given index

    Args:
        radicand: number from which the root is taken
        index: positive integer which is the degree of the root
        tolerance: positive real number that establishes the stopping criterion

    Returns:
        new_approximation: approximation of the nth root of the radicand for the
        given index

    Raises:
        TypeError: radicand is not a real number
        TypeError: index is not an integer
        ValueError: index is not a positive integer
        TypeError: tolerance is not a real number
        ValueError: tolerance is not a positive real number
        ValueError: math domain error"""
    if not isinstance(radicand, (int, float)):
        error_message = f'radicand must be a real number, not a {type(radicand).__name__}'
        raise TypeError(error_message)
    if not isinstance(index, int):
        error_message = f'index must be an integer, not a {type(index).__name__}'
        raise TypeError(error_message)
    if index <= 0:
        error_message = f'index must be a positive integer, {index} <= 0'
        raise ValueError(error_message)
    if not isinstance(tolerance, (int, float)):
        error_message = f'tolerance must be a real number, not {type(tolerance).__name__}'
        raise TypeError(error_message)
    if tolerance <= 0:
        error_message = f'tolerance must be a positive real number, {tolerance} <= 0'
        raise ValueError(error_message)
    if radicand < 0 and index % 2 == 0:
        error_message = 'math domain error, radicand must be nonnegative for even index'
        raise ValueError(error_message)
    if radicand == 0.0:
        return 0.0
    new_approximation = radicand
    old_approximation = new_approximation + tolerance + 0.1
    while tolerance <= abs(old_approximation - new_approximation):
        old_approximation = new_approximation
        first_summand = (index - 1) / index * old_approximation
        second_summand = radicand / (index * pow(old_approximation, index - 1))
        new_approximation = first_summand + second_summand
    return new_approximation