"""
Numerical integration or quadrature for a smooth function f with known values at x_i

This method is the classical approach of summing 'Equally Spaced Abscissas'

method 2:
"Simpson Rule"

"""

def method_2(boundary: list[int], steps: int) -> float:
    """Calculate the definite integral of a function using Simpson's Rule.
    :param boundary: A list containing the lower and upper bounds of integration.
    :param steps: The number of steps or resolution for the integration.
    :return: The approximate integral value."""
    if steps <= 0:
        raise ZeroDivisionError('Number of steps must be greater than zero')
    h = (boundary[1] - boundary[0]) / steps
    a = boundary[0]
    b = boundary[1]
    x_i = make_points(a, b, h)
    y = 0.0
    y += h / 3.0 * f(a)
    cnt = 2
    for i in x_i:
        y += h / 3 * (4 - 2 * (cnt % 2)) * f(i)
        cnt += 1
    y += h / 3.0 * f(b)
    return y

def make_points(a, b, h):
    x = a + h
    while x < b - h:
        yield x
        x = x + h

def f(x):
    y = (x - 0) * (x - 0)
    return y

def main() -> None:
    a = 0.0
    b = 1.0
    steps = 10.0
    boundary = [a, b]
    y = method_2(boundary, steps)
    print(f'y = {y}')