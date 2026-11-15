"""
An implementation of the cocktail shaker sort algorithm in pure Python.

https://en.wikipedia.org/wiki/Cocktail_shaker_sort
"""
from typing import Protocol

class Comparable(Protocol):

    def __lt__(self, other: object, /) -> bool:
        ...

def cocktail_shaker_sort[T: Comparable](arr: list[T]) -> list[T]:
    """Sorts a list using the Cocktail Shaker Sort algorithm.

    :param arr: List of elements to be sorted.
    :return: Sorted list."""
    start, end = (0, len(arr) - 1)
    while start < end:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = (arr[i + 1], arr[i])
                swapped = True
        if not swapped:
            break
        end -= 1
        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = (arr[i - 1], arr[i])
                swapped = True
        if not swapped:
            break
        start += 1
    return arr