"""
A pure Python implementation of the Reverse Selection Sort algorithm

This algorithm progressively sorts the array by reversing subarrays

For doctests run following command:
python3 -m doctest -v reverse_selection.py

For manual testing run:
python3 reverse_selection.py
"""
from typing import Any, Protocol

class Comparable(Protocol):

    def __lt__(self, other: Any, /) -> bool:
        ...

def reverse_subarray[T](arr: list[T], start: int, end: int) -> None:
    """Reverse a subarray in-place.

    :param arr: the array containing the subarray to be reversed
    :param start: the starting index of the subarray
    :param end: the ending index of the subarray

    Examples:"""
    while start < end:
        arr[start], arr[end] = (arr[end], arr[start])
        start += 1
        end -= 1

def reverse_selection_sort[T: Comparable](collection: list[T]) -> list[T]:
    """A pure implementation of reverse selection sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection sorted in ascending order

    Examples:"""
    n = len(collection)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if collection[j] < collection[min_idx]:
                min_idx = j
        if min_idx != i:
            reverse_subarray(collection, i, min_idx)
    return collection