import math
from timeit import timeit

def num_digits(n: int) -> int:
    """Find the number of digits in a number."""
    if not isinstance(n, int):
        raise TypeError('Input must be an integer')
    digits = 0
    n = abs(n)
    while True:
        n = n // 10
        digits += 1
        if n == 0:
            break
    return digits

def num_digits_fast(n: int) -> int:
    """Find the number of digits in a number.
    abs() is used as logarithm for negative numbers is not defined."""
    if not isinstance(n, int):
        raise TypeError('Input must be an integer')
    return 1 if n == 0 else math.floor(math.log10(abs(n)) + 1)

def num_digits_faster(n: int) -> int:
    """Find the number of digits in a number.
    abs() is used for negative numbers."""
    if not isinstance(n, int):
        raise TypeError('Input must be an integer')
    return len(str(abs(n)))

def benchmark() -> None:
    """
    Benchmark multiple functions with three different integer sizes.
    """
    from collections.abc import Callable

    def benchmark_a_function(func: Callable, value: int) -> None:
        call = f'{func.__name__}({value})'
        timing = timeit(f'__main__.{call}', setup='import __main__')
        print(f'{call}: {func(value)} -- {timing:.6f} seconds')
    for value in (262144, 1125899906842624, 1267650600228229401496703205376):
        for func in (num_digits, num_digits_fast, num_digits_faster):
            benchmark_a_function(func, value)
        print()