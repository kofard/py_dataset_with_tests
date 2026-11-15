"""
The Newton-Raphson method (aka the Newton method) is a root-finding algorithm that
approximates a root of a given real-valued function f(x). It is an iterative method
given by the formula

x_{n + 1} = x_n + f(x_n) / f'(x_n)

with the precision of the approximation increasing as the number of iterations increase.

Reference: https://en.wikipedia.org/wiki/Newton%27s_method
"""
from collections.abc import Callable
RealFunc = Callable[[float], float]

def calc_derivative(f: RealFunc, x: float, delta_x: float=0.001) -> float:
    """Approximate the derivative of a function f(x) at a point x using the finite
    difference method"""
    return (f(x + delta_x / 2) - f(x - delta_x / 2)) / delta_x

def newton_raphson(f: RealFunc, x0: float=0, max_iter: int=100, step: float=1e-06, max_error: float=1e-06, log_steps: bool=False) -> tuple[float, float, list[float]]:
    """Find a root of the given function f using the Newton-Raphson method.

    :param f: A real-valued single-variable function
    :param x0: Initial guess
    :param max_iter: Maximum number of iterations
    :param step: Step size of x, used to approximate f'(x)
    :param max_error: Maximum approximation error
    :param log_steps: bool denoting whether to log intermediate steps

    :return: A tuple containing the approximation, the error, and the intermediate
        steps. If log_steps is False, then an empty list is returned for the third
        element of the tuple.

    :raises ZeroDivisionError: The derivative approaches 0.
    :raises ArithmeticError: No solution exists, or the solution isn't found before the
        iteration limit is reached."""

    def f_derivative(x: float) -> float:
        return calc_derivative(f, x, step)
    a = x0
    steps = []
    for _ in range(max_iter):
        if log_steps:
            steps.append(a)
        error = abs(f(a))
        if error < max_error:
            return (a, error, steps)
        if f_derivative(a) == 0:
            raise ZeroDivisionError('No converging solution found, zero derivative')
        a -= f(a) / f_derivative(a)
    raise ArithmeticError('No converging solution found, iteration limit reached')