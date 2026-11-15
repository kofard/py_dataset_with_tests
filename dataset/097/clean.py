"""
This is pure Python implementation of fibonacci search.

Resources used:
https://en.wikipedia.org/wiki/Fibonacci_search_technique

For doctests run following command:
python3 -m doctest -v fibonacci_search.py

For manual testing run:
python3 fibonacci_search.py
"""
from functools import lru_cache

@lru_cache
def fibonacci(k: int) -> int:
    """Finds fibonacci number in index k.

    Parameters
    ----------
    k :
        Index of fibonacci.

    Returns
    -------
    int
        Fibonacci number in position k."""
    if not isinstance(k, int):
        raise TypeError('k must be an integer.')
    if k < 0:
        raise ValueError('k integer must be greater or equal to zero.')
    match k:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return fibonacci(k - 1) + fibonacci(k - 2)

def fibonacci_search(arr: list, val: int) -> int:
    """A pure Python implementation of a fibonacci search algorithm.

    Parameters
    ----------
    arr
        List of sorted elements.
    val
        Element to search in list.

    Returns
    -------
    int
        The index of the element in the array.
        -1 if the element is not found."""
    len_list = len(arr)
    i = 0
    while True:
        if fibonacci(i) >= len_list:
            fibb_k = i
            break
        i += 1
    offset = 0
    while fibb_k > 0:
        index_k = min(offset + fibonacci(fibb_k - 1), len_list - 1)
        item_k_1 = arr[index_k]
        if item_k_1 == val:
            return index_k
        elif val < item_k_1:
            fibb_k -= 1
        elif val > item_k_1:
            offset += fibonacci(fibb_k - 1)
            fibb_k -= 2
    return -1