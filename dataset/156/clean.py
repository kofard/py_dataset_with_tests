"""
Matrix Exponentiation is a technique to solve linear recurrences in logarithmic time.
You read more about it here:
https://zobayer.blogspot.com/2010/11/matrix-exponentiation.html
https://www.hackerearth.com/practice/notes/matrix-exponentiation-1/
"""
from __future__ import annotations
import timeit

class Matrix:

    def __init__(self, arg: list[list] | int) -> None:
        if isinstance(arg, list):
            self.t = arg
            self.n = len(arg)
        else:
            self.n = arg
            self.t = [[0 for _ in range(self.n)] for _ in range(self.n)]

    def __mul__(self, b: Matrix) -> Matrix:
        matrix = Matrix(self.n)
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    matrix.t[i][j] += self.t[i][k] * b.t[k][j]
        return matrix

def modular_exponentiation(a: Matrix, b: int) -> Matrix:
    matrix = Matrix([[1, 0], [0, 1]])
    while b > 0:
        if b & 1:
            matrix *= a
        a *= a
        b >>= 1
    return matrix

def fibonacci_with_matrix_exponentiation(n: int, f1: int, f2: int) -> int:
    """Returns the nth number of the Fibonacci sequence that
    starts with f1 and f2
    Uses the matrix exponentiation"""
    match n:
        case 1:
            return f1
        case 2:
            return f2
    matrix = Matrix([[1, 1], [1, 0]])
    matrix = modular_exponentiation(matrix, n - 2)
    return f2 * matrix.t[0][0] + f1 * matrix.t[0][1]

def simple_fibonacci(n: int, f1: int, f2: int) -> int:
    """Returns the nth number of the Fibonacci sequence that
    starts with f1 and f2
    Uses the definition"""
    match n:
        case 1:
            return f1
        case 2:
            return f2
    n -= 2
    while n > 0:
        f2, f1 = (f1 + f2, f2)
        n -= 1
    return f2

def matrix_exponentiation_time() -> float:
    setup = '\nfrom random import randint\nfrom __main__ import fibonacci_with_matrix_exponentiation\n'
    code = 'fibonacci_with_matrix_exponentiation(randint(1,70000), 1, 1)'
    exec_time = timeit.timeit(setup=setup, stmt=code, number=100)
    print('With matrix exponentiation the average execution time is ', exec_time / 100)
    return exec_time

def simple_fibonacci_time() -> float:
    setup = '\nfrom random import randint\nfrom __main__ import simple_fibonacci\n'
    code = 'simple_fibonacci(randint(1,70000), 1, 1)'
    exec_time = timeit.timeit(setup=setup, stmt=code, number=100)
    print('Without matrix exponentiation the average execution time is ', exec_time / 100)
    return exec_time

def main() -> None:
    matrix_exponentiation_time()
    simple_fibonacci_time()